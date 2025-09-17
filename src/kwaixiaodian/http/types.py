"""HTTP通信相关的类型定义"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

import httpx


@dataclass
class HTTPConfig:
    """HTTP客户端配置"""

    timeout: float = 30.0
    """请求超时时间(秒)"""

    limits: Optional[httpx.Limits] = None
    """连接池限制配置"""

    proxies: Optional[Union[str, Dict[str, str]]] = None
    """代理配置"""

    verify: Union[bool, str] = True
    """SSL验证配置，可以是布尔值或CA证书路径"""

    headers: Optional[Dict[str, str]] = None
    """默认HTTP头"""

    follow_redirects: bool = True
    """是否跟随重定向"""

    max_redirects: int = 20
    """最大重定向次数"""

    def __post_init__(self) -> None:
        """初始化后处理"""
        if self.limits is None:
            self.limits = httpx.Limits(
                max_connections=100, max_keepalive_connections=20
            )

        if self.headers is None:
            self.headers = {
                "User-Agent": "kwaixiaodian-python-sdk/1.0.0",
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
            }


@dataclass
class RetryConfig:
    """重试策略配置"""

    max_retries: int = 3
    """最大重试次数"""

    backoff_factor: float = 1.0
    """退避因子，重试间隔 = backoff_factor * (2 ** (retry_count - 1))"""

    retry_on_status: List[int] = field(
        default_factory=lambda: [429, 500, 502, 503, 504]
    )
    """需要重试的HTTP状态码"""

    retry_on_auth_error: bool = True
    """token过期时是否自动重试"""

    retry_on_network_error: bool = True
    """网络错误时是否重试"""

    max_retry_delay: float = 60.0
    """最大重试延迟时间(秒)"""


@dataclass
class RequestContext:
    """请求上下文信息"""

    method: str
    """HTTP方法"""

    url: str
    """请求URL"""

    headers: Dict[str, str]
    """请求头"""

    params: Optional[Dict[str, Any]] = None
    """URL参数"""

    data: Optional[Dict[str, Any]] = None
    """请求体数据"""

    files: Optional[Dict[str, Any]] = None
    """文件上传"""

    json_data: Optional[Dict[str, Any]] = None
    """JSON数据"""

    timeout: Optional[float] = None
    """请求超时"""
