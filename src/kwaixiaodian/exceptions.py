"""快手SDK异常定义

定义了SDK中使用的所有异常类型，提供详细的错误信息和处理建议。
"""

from typing import Any, Dict, Optional


class KwaixiaodianSDKError(Exception):
    """快手SDK基础异常"""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class KwaixiaodianAPIError(KwaixiaodianSDKError):
    """快手API调用异常

    当API返回错误状态或错误码时抛出此异常。
    """

    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        sub_code: Optional[str] = None,
        http_status: Optional[int] = None,
        request_id: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, details)
        self.error_code = error_code
        self.sub_code = sub_code
        self.http_status = http_status
        self.request_id = request_id

    def __str__(self) -> str:
        parts = [self.message]

        if self.error_code:
            parts.append(f"Error Code: {self.error_code}")

        if self.sub_code:
            parts.append(f"Sub Code: {self.sub_code}")

        if self.http_status:
            parts.append(f"HTTP Status: {self.http_status}")

        if self.request_id:
            parts.append(f"Request ID: {self.request_id}")

        return " | ".join(parts)


class KwaixiaodianAuthError(KwaixiaodianSDKError):
    """认证相关异常

    包括OAuth认证失败、token过期、签名验证失败等。
    """

    def __init__(
        self,
        message: str,
        auth_type: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, details)
        self.auth_type = auth_type

    def __str__(self) -> str:
        if self.auth_type:
            return f"[{self.auth_type}] {self.message}"
        return self.message


class KwaixiaodianSignatureError(KwaixiaodianAuthError):
    """签名验证异常"""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, "signature", details)


class KwaixiaodianNetworkError(KwaixiaodianSDKError):
    """网络连接异常

    包括超时、连接失败、DNS解析失败等网络问题。
    """

    pass


class KwaixiaodianConfigError(KwaixiaodianSDKError):
    """配置错误异常

    包括参数配置错误、必要参数缺失等。
    """

    pass


class KwaixiaodianValidationError(KwaixiaodianSDKError):
    """数据验证异常

    包括请求参数验证失败、响应数据格式错误等。
    """

    def __init__(
        self,
        message: str,
        field: Optional[str] = None,
        value: Optional[Any] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, details)
        self.field = field
        self.value = value

    def __str__(self) -> str:
        parts = [self.message]

        if self.field:
            parts.append(f"Field: {self.field}")

        if self.value is not None:
            parts.append(f"Value: {self.value}")

        return " | ".join(parts)


class KwaixiaodianRateLimitError(KwaixiaodianAPIError):
    """API限流异常"""

    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, "RATE_LIMIT_EXCEEDED", details=details)
        self.retry_after = retry_after

    def __str__(self) -> str:
        if self.retry_after:
            return f"{self.message} | Retry after: {self.retry_after}s"
        return self.message


# 错误码映射
ERROR_CODE_MAPPING = {
    # 认证相关错误
    "AUTHORIZATION_REVOKED": "授权已被撤销",
    "ACCESS_TOKEN_EXPIRED": "访问令牌已过期",
    "ACCESS_TOKEN_INVALID": "访问令牌无效",
    "REFRESH_TOKEN_EXPIRED": "刷新令牌已过期",
    "REFRESH_TOKEN_INVALID": "刷新令牌无效",
    "SIGNATURE_INVALID": "签名验证失败",
    "APP_NOT_FOUND": "应用不存在",
    "APP_SUSPENDED": "应用已被暂停",
    # 权限相关错误
    "PERMISSION_DENIED": "权限不足",
    "SCOPE_INSUFFICIENT": "授权范围不足",
    "USER_NOT_AUTHORIZED": "用户未授权",
    # 业务相关错误
    "ITEM_NOT_FOUND": "商品不存在",
    "ORDER_NOT_FOUND": "订单不存在",
    "REFUND_NOT_FOUND": "退款单不存在",
    "INVALID_ORDER_STATUS": "订单状态无效",
    "INSUFFICIENT_STOCK": "库存不足",
    # 系统相关错误
    "SYSTEM_ERROR": "系统错误",
    "SERVICE_UNAVAILABLE": "服务不可用",
    "RATE_LIMIT_EXCEEDED": "API调用频率超限",
    "REQUEST_TIMEOUT": "请求超时",
    "INVALID_REQUEST": "请求参数错误",
    "METHOD_NOT_ALLOWED": "HTTP方法不允许",
}
