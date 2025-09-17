"""认证相关类型定义"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

import pendulum


class SignMethod(Enum):
    """签名算法"""

    MD5 = "MD5"
    HMAC_SHA256 = "HMAC_SHA256"


class GrantType(Enum):
    """OAuth授权类型"""

    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    REFRESH_TOKEN = "refresh_token"


@dataclass
class AuthConfig:
    """认证配置"""

    app_key: str
    """应用AppKey"""

    app_secret: str
    """应用AppSecret"""

    sign_secret: str
    """签名密钥"""

    sign_method: SignMethod = SignMethod.HMAC_SHA256
    """签名算法，推荐使用HMAC_SHA256"""

    server_url: str = "https://openapi.kwaixiaodian.com"
    """服务器地址"""

    oauth_base_url: str = "https://openapi.kwaixiaodian.com"
    """OAuth认证地址"""


@dataclass
class TokenResponse:
    """Token响应"""

    access_token: str
    """访问令牌"""

    expires_in: int
    """过期时间(秒)"""

    refresh_token: Optional[str] = None
    """刷新令牌"""

    refresh_token_expires_in: Optional[int] = None
    """刷新令牌过期时间(秒)"""

    scope: Optional[str] = None
    """授权范围"""

    token_type: str = "Bearer"
    """令牌类型"""

    created_at: Optional[pendulum.DateTime] = None
    """创建时间"""

    def __post_init__(self):
        """初始化后处理"""
        if self.created_at is None:
            self.created_at = pendulum.now()

    @property
    def expires_at(self) -> pendulum.DateTime:
        """访问令牌过期时间"""
        if self.created_at is None:
            raise ValueError("TokenResponse not initialized")
        return self.created_at.add(seconds=self.expires_in)

    @property
    def refresh_expires_at(self) -> Optional[pendulum.DateTime]:
        """刷新令牌过期时间"""
        if self.refresh_token_expires_in and self.created_at:
            return self.created_at.add(seconds=self.refresh_token_expires_in)
        return None

    @property
    def is_expired(self) -> bool:
        """访问令牌是否过期"""
        return pendulum.now() >= self.expires_at

    @property
    def is_refresh_expired(self) -> bool:
        """刷新令牌是否过期"""
        if self.refresh_expires_at is None:
            return False
        return pendulum.now() >= self.refresh_expires_at

    @property
    def scopes(self) -> List[str]:
        """授权范围列表"""
        if not self.scope:
            return []
        return self.scope.split(",")


@dataclass
class SignatureParams:
    """签名参数"""

    method: str
    """API方法名"""

    app_key: str
    """应用Key"""

    access_token: str
    """访问令牌"""

    version: str = "1"
    """API版本"""

    timestamp: Optional[str] = None
    """时间戳"""

    sign_method: str = SignMethod.HMAC_SHA256.value
    """签名方法"""

    param: Optional[str] = None
    """业务参数JSON字符串"""

    def __post_init__(self):
        """初始化后处理"""
        if self.timestamp is None:
            self.timestamp = str(int(pendulum.now().timestamp() * 1000))

    def to_dict(self) -> Dict[str, str]:
        """转换为字典"""
        result = {
            "method": self.method,
            "appkey": self.app_key,
            "access_token": self.access_token,
            "version": self.version,
            "timestamp": self.timestamp or "",
            "signMethod": self.sign_method,
        }

        if self.param is not None:
            result["param"] = self.param

        return result
