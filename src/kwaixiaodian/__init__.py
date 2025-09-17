"""
快手小店开放平台 Python SDK

这是一个功能完整的异步Python SDK，用于快手小店开放平台API集成。
支持所有官方API接口、OAuth认证、签名验证等功能。

主要功能:
- 🚀 异步支持 - 基于httpx的高性能异步HTTP客户端
- 🔐 安全认证 - 完整的OAuth 2.0流程和签名验证
- 📦 完整API - 涵盖896个官方API接口
- 🎯 业务模型 - 25个业务域的完整数据模型
- ⚡ 高性能 - 连接池、重试机制、并发支持
- 📚 详细文档 - 完整的API文档和使用示例

快速开始:
    ```python
    from kwaixiaodian import KwaixiaodianClient

    client = KwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret"
    )

    # 获取订单列表
    orders = await client.order.list(
        access_token="your_access_token",
        seller_id=123456,
        begin_time="2024-01-01T00:00:00",
        end_time="2024-01-31T23:59:59"
    )
    ```
"""

from .client.main import AsyncKwaixiaodianClient, SyncKwaixiaodianClient
from .client.oauth import AsyncOAuthClient, SyncOAuthClient
from .exceptions import (
    KwaixiaodianAPIError,
    KwaixiaodianAuthError,
    KwaixiaodianNetworkError,
    KwaixiaodianSDKError,
    KwaixiaodianSignatureError,
)

__version__ = "1.0.1"
__author__ = "Kuaishou SDK Team"
__email__ = "support@kwaixiaodian.com"
__description__ = "快手小店开放平台Python SDK - 全功能异步客户端库"

__all__ = [
    # 异步客户端类
    "AsyncKwaixiaodianClient",
    "AsyncOAuthClient",
    # 同步客户端类
    "SyncKwaixiaodianClient",
    "SyncOAuthClient",
    # 便捷别名
    "KwaixiaodianClient",  # AsyncKwaixiaodianClient 的别名
    "OAuthClient",  # AsyncOAuthClient 的别名
    # 异常类
    "KwaixiaodianSDKError",
    "KwaixiaodianAPIError",
    "KwaixiaodianAuthError",
    "KwaixiaodianNetworkError",
    "KwaixiaodianSignatureError",
    # 元信息
    "__version__",
    "__author__",
    "__email__",
    "__description__",
]

# 便捷别名 - 默认指向异步版本
KwaixiaodianClient = AsyncKwaixiaodianClient
OAuthClient = AsyncOAuthClient
