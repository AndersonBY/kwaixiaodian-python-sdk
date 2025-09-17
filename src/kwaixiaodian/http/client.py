"""异步HTTP客户端实现"""

import asyncio
import logging
import time
from typing import Any, Dict, Optional

import httpx
import orjson
from httpx import AsyncClient, Client, NetworkError, Response, Timeout, TimeoutException

from ..exceptions import KwaixiaodianNetworkError, KwaixiaodianSDKError
from .types import HTTPConfig, RequestContext, RetryConfig

logger = logging.getLogger(__name__)


class AsyncHTTPClient:
    """异步HTTP客户端

    基于httpx实现的高性能异步HTTP客户端，支持：
    - 连接池复用
    - 自动重试机制
    - 超时控制
    - 代理支持
    - SSL验证
    """

    def __init__(
        self,
        http_config: Optional[HTTPConfig] = None,
        retry_config: Optional[RetryConfig] = None,
        enable_logging: bool = False,
    ) -> None:
        """初始化HTTP客户端

        Args:
            http_config: HTTP配置
            retry_config: 重试配置
            enable_logging: 是否启用日志
        """
        self.http_config = http_config or HTTPConfig()
        self.retry_config = retry_config or RetryConfig()
        self.enable_logging = enable_logging

        # 创建httpx客户端
        # 处理可能为 None 的参数
        proxy_config = None
        if self.http_config.proxies:
            if isinstance(self.http_config.proxies, str):
                proxy_config = self.http_config.proxies
            elif isinstance(self.http_config.proxies, dict):
                # httpx 不直接支持字典格式代理，转换为字符串或忽略
                # 这里简化处理，可以根据需要实现更复杂的转换逻辑
                proxy_config = None

        self._client = AsyncClient(
            timeout=Timeout(self.http_config.timeout),
            limits=self.http_config.limits or httpx.Limits(),
            proxy=proxy_config,
            verify=self.http_config.verify,
            headers=self.http_config.headers,
            follow_redirects=self.http_config.follow_redirects,
        )

        if self.enable_logging:
            logger.setLevel(logging.DEBUG)

    async def __aenter__(self):
        """异步上下文管理器入口"""
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ):
        """异步上下文管理器退出"""
        await self.close()

    async def close(self) -> None:
        """关闭HTTP客户端"""
        if hasattr(self, "_client"):
            await self._client.aclose()

    async def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """发起HTTP请求

        Args:
            method: HTTP方法
            url: 请求URL
            headers: 请求头
            params: URL参数
            data: 表单数据
            json_data: JSON数据
            files: 文件上传
            timeout: 请求超时

        Returns:
            HTTP响应对象

        Raises:
            KwaixiaodianNetworkError: 网络错误
            KwaixiaodianSDKError: SDK错误
        """
        context = RequestContext(
            method=method,
            url=url,
            headers=headers or {},
            params=params,
            data=data,
            json_data=json_data,
            files=files,
            timeout=timeout,
        )

        if self.enable_logging:
            logger.debug(f"发起请求: {method} {url}")
            if params:
                logger.debug(f"URL参数: {params}")
            if json_data:
                logger.debug(f"JSON数据: {orjson.dumps(json_data).decode()}")

        return await self._request_with_retry(context)

    async def _request_with_retry(self, context: RequestContext) -> Response:
        """带重试机制的请求执行"""
        last_exception: Exception | None = None

        for attempt in range(self.retry_config.max_retries + 1):
            try:
                response = await self._execute_request(context)

                # 检查是否需要重试
                if self._should_retry_on_status(response.status_code, attempt):
                    if attempt < self.retry_config.max_retries:
                        delay = self._calculate_retry_delay(attempt)
                        if self.enable_logging:
                            logger.warning(
                                f"请求失败(状态码: {response.status_code})，{delay}秒后进行第{attempt + 1}次重试"
                            )
                        await asyncio.sleep(delay)
                        continue

                return response

            except (httpx.NetworkError, httpx.TimeoutException) as e:
                last_exception = e
                if (
                    self.retry_config.retry_on_network_error
                    and attempt < self.retry_config.max_retries
                ):
                    delay = self._calculate_retry_delay(attempt)
                    if self.enable_logging:
                        logger.warning(
                            f"网络错误: {e}，{delay}秒后进行第{attempt + 1}次重试"
                        )
                    await asyncio.sleep(delay)
                    continue
                break

            except Exception as e:
                last_exception = e
                break

        # 重试耗尽，抛出异常
        if isinstance(last_exception, (httpx.NetworkError, httpx.TimeoutException)):
            raise KwaixiaodianNetworkError(
                f"网络请求失败: {last_exception}"
            ) from last_exception
        elif last_exception:
            raise KwaixiaodianSDKError(
                f"请求执行失败: {last_exception}"
            ) from last_exception
        else:
            raise KwaixiaodianSDKError("未知请求错误")

    async def _execute_request(self, context: RequestContext) -> Response:
        """执行单次HTTP请求"""
        request_kwargs: Dict[str, Dict[str, Any] | str | float] = {
            "method": context.method,
            "url": context.url,
            "headers": context.headers,
        }

        if context.params:
            request_kwargs["params"] = context.params

        if context.json_data:
            request_kwargs["json"] = context.json_data
        elif context.data:
            request_kwargs["data"] = context.data

        if context.files:
            request_kwargs["files"] = context.files

        if context.timeout:
            request_kwargs["timeout"] = context.timeout

        return await self._client.request(**request_kwargs)  # type: ignore

    def _should_retry_on_status(self, status_code: int, attempt: int) -> bool:
        """判断状态码是否需要重试"""
        if attempt >= self.retry_config.max_retries:
            return False

        return status_code in self.retry_config.retry_on_status

    def _calculate_retry_delay(self, attempt: int) -> float:
        """计算重试延迟时间"""
        delay = self.retry_config.backoff_factor * (2**attempt)
        return min(delay, self.retry_config.max_retry_delay)

    async def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """GET请求"""
        return await self.request(
            "GET", url, headers=headers, params=params, timeout=timeout
        )

    async def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """POST请求"""
        return await self.request(
            "POST",
            url,
            headers=headers,
            data=data,
            json_data=json_data,
            files=files,
            timeout=timeout,
        )

    async def put(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """PUT请求"""
        return await self.request(
            "PUT", url, headers=headers, data=data, json_data=json_data, timeout=timeout
        )

    async def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """DELETE请求"""
        return await self.request("DELETE", url, headers=headers, timeout=timeout)


class SyncHTTPClient:
    """同步HTTP客户端

    基于httpx实现的同步HTTP客户端，支持：
    - 连接池复用
    - 自动重试机制
    - 超时控制
    - 代理支持
    - SSL验证
    """

    def __init__(
        self,
        http_config: Optional[HTTPConfig] = None,
        retry_config: Optional[RetryConfig] = None,
        enable_logging: bool = False,
    ) -> None:
        """初始化HTTP客户端

        Args:
            http_config: HTTP配置
            retry_config: 重试配置
            enable_logging: 是否启用日志
        """
        self.http_config = http_config or HTTPConfig()
        self.retry_config = retry_config or RetryConfig()
        self.enable_logging = enable_logging

        # 创建httpx客户端
        # 处理可能为 None 的参数
        proxy_config = None
        if self.http_config.proxies:
            if isinstance(self.http_config.proxies, str):
                proxy_config = self.http_config.proxies
            elif isinstance(self.http_config.proxies, dict):
                # httpx 不直接支持字典格式代理，转换为字符串或忽略
                # 这里简化处理，可以根据需要实现更复杂的转换逻辑
                proxy_config = None

        self._client = Client(
            timeout=Timeout(self.http_config.timeout),
            limits=self.http_config.limits or httpx.Limits(),
            proxy=proxy_config,
            verify=self.http_config.verify,
            headers=self.http_config.headers,
            follow_redirects=self.http_config.follow_redirects,
        )

        if self.enable_logging:
            logger.setLevel(logging.DEBUG)

    def __enter__(self):
        """上下文管理器入口"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出"""
        self.close()

    def close(self) -> None:
        """关闭HTTP客户端"""
        if hasattr(self, "_client"):
            self._client.close()

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """发起HTTP请求

        Args:
            method: HTTP方法
            url: 请求URL
            headers: 请求头
            params: URL参数
            data: 表单数据
            json_data: JSON数据
            files: 文件上传
            timeout: 请求超时

        Returns:
            HTTP响应对象

        Raises:
            KwaixiaodianNetworkError: 网络错误
            KwaixiaodianSDKError: SDK错误
        """
        context = RequestContext(
            method=method,
            url=url,
            headers=headers or {},
            params=params,
            data=data,
            json_data=json_data,
            files=files,
            timeout=timeout,
        )

        if self.enable_logging:
            logger.debug(f"发起请求: {method} {url}")
            if params:
                logger.debug(f"URL参数: {params}")
            if json_data:
                logger.debug(f"JSON数据: {orjson.dumps(json_data).decode()}")

        return self._request_with_retry(context)

    def _request_with_retry(self, context: RequestContext) -> Response:
        """带重试机制的请求执行"""
        last_exception: Exception | None = None

        for attempt in range(self.retry_config.max_retries + 1):
            try:
                response = self._execute_request(context)

                # 检查是否需要重试
                if self._should_retry_on_status(response.status_code, attempt):
                    if attempt < self.retry_config.max_retries:
                        delay = self._calculate_retry_delay(attempt)
                        if self.enable_logging:
                            logger.warning(
                                f"请求失败(状态码: {response.status_code})，{delay}秒后进行第{attempt + 1}次重试"
                            )
                        time.sleep(delay)
                        continue

                return response

            except (NetworkError, TimeoutException) as e:
                last_exception = e
                if (
                    self.retry_config.retry_on_network_error
                    and attempt < self.retry_config.max_retries
                ):
                    delay = self._calculate_retry_delay(attempt)
                    if self.enable_logging:
                        logger.warning(
                            f"网络错误: {e}，{delay}秒后进行第{attempt + 1}次重试"
                        )
                    time.sleep(delay)
                    continue
                break

            except Exception as e:
                last_exception = e
                break

        # 重试耗尽，抛出异常
        if isinstance(last_exception, (NetworkError, TimeoutException)):
            raise KwaixiaodianNetworkError(
                f"网络请求失败: {last_exception}"
            ) from last_exception
        elif last_exception:
            raise KwaixiaodianSDKError(
                f"请求执行失败: {last_exception}"
            ) from last_exception
        else:
            raise KwaixiaodianSDKError("未知请求错误")

    def _execute_request(self, context: RequestContext) -> Response:
        """执行单次HTTP请求"""
        request_kwargs: Dict[str, Dict[str, Any] | str | float] = {
            "method": context.method,
            "url": context.url,
            "headers": context.headers,
        }

        if context.params:
            request_kwargs["params"] = context.params

        if context.json_data:
            request_kwargs["json"] = context.json_data
        elif context.data:
            request_kwargs["data"] = context.data

        if context.files:
            request_kwargs["files"] = context.files

        if context.timeout:
            request_kwargs["timeout"] = context.timeout

        return self._client.request(**request_kwargs)  # type: ignore

    def _should_retry_on_status(self, status_code: int, attempt: int) -> bool:
        """判断状态码是否需要重试"""
        if attempt >= self.retry_config.max_retries:
            return False

        return status_code in self.retry_config.retry_on_status

    def _calculate_retry_delay(self, attempt: int) -> float:
        """计算重试延迟时间"""
        delay = self.retry_config.backoff_factor * (2**attempt)
        return min(delay, self.retry_config.max_retry_delay)

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """GET请求"""
        return self.request("GET", url, headers=headers, params=params, timeout=timeout)

    def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """POST请求"""
        return self.request(
            "POST",
            url,
            headers=headers,
            data=data,
            json_data=json_data,
            files=files,
            timeout=timeout,
        )

    def put(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """PUT请求"""
        return self.request(
            "PUT", url, headers=headers, data=data, json_data=json_data, timeout=timeout
        )

    def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Response:
        """DELETE请求"""
        return self.request("DELETE", url, headers=headers, timeout=timeout)
