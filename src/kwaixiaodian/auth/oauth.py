"""OAuth 2.0认证管理器"""

import logging
from typing import Dict, List, Optional
from urllib.parse import urlencode

import httpx

from ..exceptions import KwaixiaodianAuthError
from ..http import AsyncHTTPClient, SyncHTTPClient
from .types import AuthConfig, GrantType, TokenResponse

logger = logging.getLogger(__name__)


class AsyncOAuthManager:
    """OAuth 2.0认证管理器

    负责处理快手开放平台的OAuth认证流程，包括：
    - 获取授权URL
    - 授权码换取token
    - 刷新访问token
    - 客户端凭证模式
    """

    def __init__(
        self, config: AuthConfig, http_client: Optional[AsyncHTTPClient] = None
    ):
        """初始化OAuth管理器

        Args:
            config: 认证配置
            http_client: HTTP客户端，如果为None会创建新实例
        """
        self.config = config
        self.http_client = http_client or AsyncHTTPClient()
        self._should_close_http_client = http_client is None

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
        if self._should_close_http_client:
            await self.http_client.close()

    def get_authorize_url(
        self,
        redirect_uri: str,
        scope: Optional[List[str]] = None,
        state: Optional[str] = None,
    ) -> str:
        """获取授权URL

        Args:
            redirect_uri: 回调地址
            scope: 授权范围列表
            state: 状态参数，防CSRF攻击

        Returns:
            授权URL
        """
        params = {
            "response_type": "code",
            "client_id": self.config.app_key,
            "redirect_uri": redirect_uri,
        }

        if scope:
            params["scope"] = ",".join(scope)

        if state:
            params["state"] = state

        query_string = urlencode(params)
        return f"{self.config.oauth_base_url}/oauth2/authorize?{query_string}"

    async def get_access_token(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> TokenResponse:
        """使用授权码获取访问令牌

        Args:
            code: 授权码
            redirect_uri: 回调地址（某些情况下需要）

        Returns:
            Token响应

        Raises:
            KwaixiaodianAuthError: 认证失败
        """
        data = {
            "grant_type": GrantType.AUTHORIZATION_CODE.value,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
            "code": code,
        }

        if redirect_uri:
            data["redirect_uri"] = redirect_uri

        return await self._request_token("/oauth2/access_token", data)

    async def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        """刷新访问令牌

        Args:
            refresh_token: 刷新令牌

        Returns:
            新的Token响应

        Raises:
            KwaixiaodianAuthError: 刷新失败
        """
        data = {
            "grant_type": GrantType.REFRESH_TOKEN.value,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
            "refresh_token": refresh_token,
        }

        return await self._request_token("/oauth2/refresh_token", data)

    async def get_client_credentials_token(self) -> TokenResponse:
        """客户端凭证模式获取令牌

        Returns:
            Token响应

        Raises:
            KwaixiaodianAuthError: 认证失败
        """
        data = {
            "grant_type": GrantType.CLIENT_CREDENTIALS.value,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
        }

        return await self._request_token("/oauth2/access_token", data)

    async def _request_token(
        self, endpoint: str, data: Dict[str, str]
    ) -> TokenResponse:
        """请求令牌的通用方法

        Args:
            endpoint: API端点
            data: 请求数据

        Returns:
            Token响应

        Raises:
            KwaixiaodianAuthError: 请求失败
        """
        url = f"{self.config.oauth_base_url}{endpoint}"

        try:
            logger.debug(f"请求Token: {endpoint}")

            response = await self.http_client.post(
                url,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            if response.status_code != 200:
                raise KwaixiaodianAuthError(
                    f"OAuth请求失败: HTTP {response.status_code}",
                    details={"response": response.text},
                )

            result = response.json()

            # 检查是否有错误
            if "error" in result:
                error_msg = result.get(
                    "error_description", result.get("error", "Unknown error")
                )
                raise KwaixiaodianAuthError(
                    f"OAuth认证失败: {error_msg}", details=result
                )

            # 构建Token响应
            return TokenResponse(
                access_token=result["access_token"],
                expires_in=result["expires_in"],
                refresh_token=result.get("refresh_token"),
                refresh_token_expires_in=result.get("refresh_token_expires_in"),
                scope=result.get("scope"),
                token_type=result.get("token_type", "Bearer"),
            )

        except httpx.RequestError as e:
            logger.error(f"OAuth HTTP请求失败: {e}")
            raise KwaixiaodianAuthError(f"OAuth网络请求失败: {e}") from e
        except Exception as e:
            logger.error(f"OAuth处理失败: {e}")
            raise KwaixiaodianAuthError(f"OAuth处理失败: {e}") from e

    async def revoke_token(self, token: str, token_type: str = "access_token") -> bool:
        """撤销令牌

        Args:
            token: 要撤销的令牌
            token_type: 令牌类型（access_token或refresh_token）

        Returns:
            撤销是否成功
        """
        url = f"{self.config.oauth_base_url}/oauth2/revoke"
        data = {
            "token": token,
            "token_type_hint": token_type,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
        }

        try:
            response = await self.http_client.post(
                url,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            return response.status_code == 200

        except Exception as e:
            logger.error(f"令牌撤销失败: {e}")
            return False


class SyncOAuthManager:
    """同步OAuth 2.0认证管理器

    负责处理快手开放平台的OAuth认证流程，包括：
    - 获取授权URL
    - 授权码换取token
    - 刷新访问token
    - 客户端凭证模式
    """

    def __init__(
        self, config: AuthConfig, http_client: Optional[SyncHTTPClient] = None
    ):
        """初始化同步OAuth管理器

        Args:
            config: 认证配置
            http_client: 同步HTTP客户端，如果为None会创建新实例
        """
        self.config = config
        self.http_client = http_client or SyncHTTPClient()
        self._should_close_http_client = http_client is None

    def __enter__(self):
        """上下文管理器入口"""
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ):
        """上下文管理器退出"""
        if self._should_close_http_client:
            self.http_client.close()

    def get_authorize_url(
        self,
        redirect_uri: str,
        scope: Optional[List[str]] = None,
        state: Optional[str] = None,
    ) -> str:
        """获取授权URL

        Args:
            redirect_uri: 回调地址
            scope: 授权范围列表
            state: 状态参数，防CSRF攻击

        Returns:
            授权URL
        """
        params = {
            "response_type": "code",
            "client_id": self.config.app_key,
            "redirect_uri": redirect_uri,
        }

        if scope:
            params["scope"] = ",".join(scope)

        if state:
            params["state"] = state

        query_string = urlencode(params)
        return f"{self.config.oauth_base_url}/oauth2/authorize?{query_string}"

    def get_access_token(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> TokenResponse:
        """使用授权码获取访问令牌

        Args:
            code: 授权码
            redirect_uri: 回调地址（某些情况下需要）

        Returns:
            Token响应

        Raises:
            KwaixiaodianAuthError: 认证失败
        """
        data = {
            "grant_type": GrantType.AUTHORIZATION_CODE.value,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
            "code": code,
        }

        if redirect_uri:
            data["redirect_uri"] = redirect_uri

        return self._request_token("/oauth2/access_token", data)

    def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        """刷新访问令牌

        Args:
            refresh_token: 刷新令牌

        Returns:
            新的Token响应

        Raises:
            KwaixiaodianAuthError: 刷新失败
        """
        data = {
            "grant_type": GrantType.REFRESH_TOKEN.value,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
            "refresh_token": refresh_token,
        }

        return self._request_token("/oauth2/refresh_token", data)

    def get_client_credentials_token(self) -> TokenResponse:
        """客户端凭证模式获取令牌

        Returns:
            Token响应

        Raises:
            KwaixiaodianAuthError: 认证失败
        """
        data = {
            "grant_type": GrantType.CLIENT_CREDENTIALS.value,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
        }

        return self._request_token("/oauth2/access_token", data)

    def _request_token(self, endpoint: str, data: Dict[str, str]) -> TokenResponse:
        """请求令牌的通用方法

        Args:
            endpoint: API端点
            data: 请求数据

        Returns:
            Token响应

        Raises:
            KwaixiaodianAuthError: 请求失败
        """
        url = f"{self.config.oauth_base_url}{endpoint}"

        try:
            logger.debug(f"请求Token: {endpoint}")

            response = self.http_client.post(
                url,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            if response.status_code != 200:
                raise KwaixiaodianAuthError(
                    f"OAuth请求失败: HTTP {response.status_code}",
                    details={"response": response.text},
                )

            result = response.json()

            # 检查是否有错误
            if "error" in result:
                error_msg = result.get(
                    "error_description", result.get("error", "Unknown error")
                )
                raise KwaixiaodianAuthError(
                    f"OAuth认证失败: {error_msg}", details=result
                )

            # 构建Token响应
            return TokenResponse(
                access_token=result["access_token"],
                expires_in=result["expires_in"],
                refresh_token=result.get("refresh_token"),
                refresh_token_expires_in=result.get("refresh_token_expires_in"),
                scope=result.get("scope"),
                token_type=result.get("token_type", "Bearer"),
            )

        except httpx.RequestError as e:
            logger.error(f"OAuth HTTP请求失败: {e}")
            raise KwaixiaodianAuthError(f"OAuth网络请求失败: {e}") from e
        except Exception as e:
            logger.error(f"OAuth处理失败: {e}")
            raise KwaixiaodianAuthError(f"OAuth处理失败: {e}") from e

    def revoke_token(self, token: str, token_type: str = "access_token") -> bool:
        """撤销令牌

        Args:
            token: 要撤销的令牌
            token_type: 令牌类型（access_token或refresh_token）

        Returns:
            撤销是否成功
        """
        url = f"{self.config.oauth_base_url}/oauth2/revoke"
        data = {
            "token": token,
            "token_type_hint": token_type,
            "client_id": self.config.app_key,
            "client_secret": self.config.app_secret,
        }

        try:
            response = self.http_client.post(
                url,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            return response.status_code == 200

        except Exception as e:
            logger.error(f"令牌撤销失败: {e}")
            return False
