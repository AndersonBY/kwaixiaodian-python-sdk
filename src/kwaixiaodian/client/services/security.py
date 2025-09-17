"""安全管理服务类（严格对齐 Java SDK）

本模块仅暴露官方 Java 参考存在的 6 个安全接口，提供异步/同步两套服务层。
所有方法均遵循以下文档规范：
- OpenAPI: 展示网关方法名与 HTTP 动词，来源于对应 Request 模型 `api_method` 与 `http_method`
- Java: 对应的 Java Request 类与反编译源码路径，便于交叉验证
- Raises: 统一声明可能抛出的 `KwaixiaodianAPIError`、`KwaixiaodianValidationError`

参考文档
- 错误处理: `docs/error-handling.md`
- 基础模块: `docs/api/base-modules.md`
"""

from typing import List, Optional

from ...models.security import (
    PeriodDecryptData,
    SecurityInstantDecryptBatchRequest,
    SecurityInstantDecryptBatchResponse,
    SecurityLogBatchRequest,
    SecurityLogBatchResponse,
    SecurityLogLoginRequest,
    SecurityLogLoginResponse,
    SecurityLogOpenRequest,
    SecurityLogOpenResponse,
    SecurityLogOrderRequest,
    SecurityLogOrderResponse,
    SecurityLogSqlRequest,
    SecurityLogSqlResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncSecurityService:
    """异步安全服务，仅保留 Java 支持的 6 个接口。

    说明
    - 覆盖接口: order、sql、batch、open、login 日志上报与 instant.decrypt.batch
    - 与 Java 对齐: 端点、参数、语义均以 `java_sdk_reference/` 为准，不增删臆测接口
    """

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def log_order_event(
        self,
        access_token: str,
        open_id: str,
        seller_id: int,
        url: str,
        user_ip: str,
        order_ids: Optional[List[int]] = None,
        operation: Optional[int] = None,
        data: Optional[str] = None,
        order_total: Optional[int] = None,
        time: int = 0,
    ) -> SecurityLogOrderResponse:
        """记录订单相关安全日志。

        OpenAPI: `open.security.log.order` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogOrderRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogOrderRequest.java`

        Args:
            access_token: 访问令牌
            open_id: 开放平台 openId
            seller_id: 商家ID
            url: 触发日志的页面/接口地址
            user_ip: 用户IP
            order_ids: 相关订单ID列表
            operation: 操作类型编码
            data: 额外的上下文数据（JSON 字符串）
            order_total: 订单金额（分）
            time: 日志时间戳（毫秒）

        Returns:
            安全日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误

        参考: docs/error-handling.md
        """

        request = SecurityLogOrderRequest(
            access_token=access_token,
            open_id=open_id,
            seller_id=seller_id,
            url=url,
            user_ip=user_ip,
            order_ids=order_ids,
            operation=operation,
            data=data,
            order_total=order_total,
            time=time,
            api_version="1",
        )
        return await self._client.execute(request, SecurityLogOrderResponse)

    async def log_sql_event(
        self, access_token: str, type: str, sql: str, time: int
    ) -> SecurityLogSqlResponse:
        """记录 SQL 相关安全日志。

        OpenAPI: `open.security.log.sql` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogSqlRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogSqlRequest.java`

        Args:
            access_token: 访问令牌
            type: SQL 类型或场景标识
            sql: 语句内容（请自行脱敏）
            time: 日志时间戳（毫秒）

        Returns:
            安全日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogSqlRequest(
            access_token=access_token, type=type, sql=sql, time=time, api_version="1"
        )
        return await self._client.execute(request, SecurityLogSqlResponse)

    async def log_batch(
        self, access_token: str, method: str, data: str
    ) -> SecurityLogBatchResponse:
        """批量安全日志上报。

        OpenAPI: `open.security.log.batch` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogBatchRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogBatchRequest.java`

        Args:
            access_token: 访问令牌
            method: 业务方法或分类
            data: 日志批量数据（JSON 字符串）

        Returns:
            批量上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogBatchRequest(
            access_token=access_token, method=method, data=data, api_version="1"
        )
        return await self._client.execute(request, SecurityLogBatchResponse)

    async def log_open_event(
        self,
        access_token: str,
        open_id: str,
        seller_id: int,
        user_id: Optional[str] = None,
        order_ids: Optional[List[int]] = None,
        client_ip: Optional[str] = None,
        data: Optional[str] = None,
        order_total: Optional[int] = None,
        url: Optional[str] = None,
        send_to_url: Optional[str] = None,
        time: Optional[int] = None,
    ) -> SecurityLogOpenResponse:
        """记录开放平台相关安全日志。

        OpenAPI: `open.security.log.open` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogOpenRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogOpenRequest.java`

        Args:
            access_token: 访问令牌
            open_id: 开放平台 openId
            seller_id: 商家ID
            user_id: 业务用户ID
            order_ids: 相关订单ID列表
            client_ip: 客户端IP
            data: 额外上下文（JSON 字符串）
            order_total: 订单金额（分）
            url: 当前请求URL
            send_to_url: 上报目的URL
            time: 日志时间戳（毫秒）

        Returns:
            安全日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogOpenRequest(
            access_token=access_token,
            open_id=open_id,
            seller_id=seller_id,
            user_id=user_id,
            order_ids=order_ids,
            client_ip=client_ip,
            data=data,
            order_total=order_total,
            url=url,
            send_to_url=send_to_url,
            time=time,
            api_version="1",
        )
        return await self._client.execute(request, SecurityLogOpenResponse)

    async def log_login_event(
        self,
        access_token: str,
        open_id: str,
        seller_id: int,
        user_ip: Optional[str] = None,
        login_result: Optional[str] = None,
        login_message: Optional[str] = None,
        time: Optional[int] = None,
    ) -> SecurityLogLoginResponse:
        """记录登录相关安全日志。

        OpenAPI: `open.security.log.login` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogLoginRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogLoginRequest.java`

        Args:
            access_token: 访问令牌
            open_id: 开放平台 openId
            seller_id: 商家ID
            user_ip: 用户IP
            login_result: 登录结果
            login_message: 登录信息
            time: 日志时间戳（毫秒）

        Returns:
            安全日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogLoginRequest(
            access_token=access_token,
            open_id=open_id,
            seller_id=seller_id,
            user_ip=user_ip,
            login_result=login_result,
            login_message=login_message,
            time=time,
            api_version="1",
        )
        return await self._client.execute(request, SecurityLogLoginResponse)

    async def instant_decrypt_batch(
        self, access_token: str, decrypt_data_list: List[PeriodDecryptData]
    ) -> SecurityInstantDecryptBatchResponse:
        """批量即时解密。

        OpenAPI: `open.security.instant.decrypt.batch` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityInstantDecryptBatchRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityInstantDecryptBatchRequest.java`

        Args:
            access_token: 访问令牌
            decrypt_data_list: 待解密数据列表

        Returns:
            批量解密结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityInstantDecryptBatchRequest(
            access_token=access_token,
            decrypt_data_list=decrypt_data_list,
            api_version="1",
        )
        return await self._client.execute(request, SecurityInstantDecryptBatchResponse)


class SyncSecurityService:
    """同步安全服务，仅保留 Java 支持的 6 个接口。"""

    def __init__(self, client: SyncBaseClient):
        self._client = client

    def log_order_event(
        self,
        access_token: str,
        open_id: str,
        seller_id: int,
        url: str,
        user_ip: str,
        order_ids: Optional[List[int]] = None,
        operation: Optional[int] = None,
        data: Optional[str] = None,
        order_total: Optional[int] = None,
        time: int = 0,
    ) -> SecurityLogOrderResponse:
        """记录订单相关安全日志（同步）。

        OpenAPI: `open.security.log.order` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogOrderRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogOrderRequest.java`)

        Args:
            access_token: 访问令牌
            open_id: 开放平台 `openId`
            seller_id: 商家ID
            url: 触发日志的页面/接口地址
            user_ip: 用户IP
            order_ids: 相关订单ID列表（可选）
            operation: 操作类型编码（可选）
            data: 额外上下文数据（JSON， 可选）
            order_total: 订单金额（分，可选）
            time: 日志时间戳（毫秒，可选，默认 0）

        Returns:
            SecurityLogOrderResponse: 日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogOrderRequest(
            access_token=access_token,
            open_id=open_id,
            seller_id=seller_id,
            url=url,
            user_ip=user_ip,
            order_ids=order_ids,
            operation=operation,
            data=data,
            order_total=order_total,
            time=time,
            api_version="1",
        )
        return self._client.execute(request, SecurityLogOrderResponse)

    def log_sql_event(
        self, access_token: str, type: str, sql: str, time: int
    ) -> SecurityLogSqlResponse:
        """记录 SQL 相关安全日志（同步）。

        OpenAPI: `open.security.log.sql` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogSqlRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogSqlRequest.java`)

        Args:
            access_token: 访问令牌
            type: SQL 类型或业务场景标识
            sql: SQL 语句（需调用方自行脱敏）
            time: 日志时间戳（毫秒）

        Returns:
            SecurityLogSqlResponse: 日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogSqlRequest(
            access_token=access_token, type=type, sql=sql, time=time, api_version="1"
        )
        return self._client.execute(request, SecurityLogSqlResponse)

    def log_batch(
        self, access_token: str, method: str, data: str
    ) -> SecurityLogBatchResponse:
        """批量安全日志上报（同步）。

        OpenAPI: `open.security.log.batch` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogBatchRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogBatchRequest.java`)

        Args:
            access_token: 访问令牌
            method: 业务方法或分类标识
            data: 批量日志数据（JSON 字符串）

        Returns:
            SecurityLogBatchResponse: 批量上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogBatchRequest(
            access_token=access_token, method=method, data=data, api_version="1"
        )
        return self._client.execute(request, SecurityLogBatchResponse)

    def log_open_event(
        self,
        access_token: str,
        open_id: str,
        seller_id: int,
        user_id: Optional[str] = None,
        order_ids: Optional[List[int]] = None,
        client_ip: Optional[str] = None,
        data: Optional[str] = None,
        order_total: Optional[int] = None,
        url: Optional[str] = None,
        send_to_url: Optional[str] = None,
        time: Optional[int] = None,
    ) -> SecurityLogOpenResponse:
        """记录开放平台相关安全日志（同步）。

        OpenAPI: `open.security.log.open` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogOpenRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogOpenRequest.java`)

        Args:
            access_token: 访问令牌
            open_id: 开放平台 `openId`
            seller_id: 商家ID
            user_id: 业务用户ID（可选）
            order_ids: 相关订单ID列表（可选）
            client_ip: 客户端IP（可选）
            data: 额外上下文（JSON，可选）
            order_total: 订单金额（分，可选）
            url: 当前请求URL（可选）
            send_to_url: 日志发送目标URL（可选）
            time: 日志时间戳（毫秒，可选）

        Returns:
            SecurityLogOpenResponse: 日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogOpenRequest(
            access_token=access_token,
            open_id=open_id,
            seller_id=seller_id,
            user_id=user_id,
            order_ids=order_ids,
            client_ip=client_ip,
            data=data,
            order_total=order_total,
            url=url,
            send_to_url=send_to_url,
            time=time,
            api_version="1",
        )
        return self._client.execute(request, SecurityLogOpenResponse)

    def log_login_event(
        self,
        access_token: str,
        open_id: str,
        seller_id: int,
        user_ip: Optional[str] = None,
        login_result: Optional[str] = None,
        login_message: Optional[str] = None,
        time: Optional[int] = None,
    ) -> SecurityLogLoginResponse:
        """记录登录相关安全日志（同步）。

        OpenAPI: `open.security.log.login` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityLogLoginRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityLogLoginRequest.java`)

        Args:
            access_token: 访问令牌
            open_id: 开放平台 `openId`
            seller_id: 商家ID
            user_ip: 用户IP（可选）
            login_result: 登录结果（可选）
            login_message: 登录信息（可选）
            time: 日志时间戳（毫秒，可选）

        Returns:
            SecurityLogLoginResponse: 日志上报结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityLogLoginRequest(
            access_token=access_token,
            open_id=open_id,
            seller_id=seller_id,
            user_ip=user_ip,
            login_result=login_result,
            login_message=login_message,
            time=time,
            api_version="1",
        )
        return self._client.execute(request, SecurityLogLoginResponse)

    def instant_decrypt_batch(
        self, access_token: str, decrypt_data_list: List[PeriodDecryptData]
    ) -> SecurityInstantDecryptBatchResponse:
        """批量即时解密（同步）。

        OpenAPI: `open.security.instant.decrypt.batch` (POST)
        Java: `com.kuaishou.merchant.open.api.request.security.OpenSecurityInstantDecryptBatchRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/security/OpenSecurityInstantDecryptBatchRequest.java`)

        Args:
            access_token: 访问令牌
            decrypt_data_list: 待解密数据列表

        Returns:
            SecurityInstantDecryptBatchResponse: 批量解密结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """

        request = SecurityInstantDecryptBatchRequest(
            access_token=access_token,
            decrypt_data_list=decrypt_data_list,
            api_version="1",
        )
        return self._client.execute(request, SecurityInstantDecryptBatchResponse)
