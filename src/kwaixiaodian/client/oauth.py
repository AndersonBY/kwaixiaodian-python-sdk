"""OAuth认证客户端"""

import logging
from typing import List, Optional

from ..auth import AsyncOAuthManager, AuthConfig, SyncOAuthManager, TokenResponse
from ..http import AsyncHTTPClient, HTTPConfig, SyncHTTPClient

logger = logging.getLogger(__name__)


class AsyncOAuthClient:
    """OAuth认证客户端

    专门处理OAuth认证流程的客户端类。
    """

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        server_url: str = "https://openapi.kwaixiaodian.com",
        http_config: Optional[HTTPConfig] = None,
    ):
        """初始化OAuth客户端

        Args:
            app_key: 应用Key
            app_secret: 应用Secret
            server_url: 服务器地址
            http_config: HTTP配置
        """
        self.config = AuthConfig(
            app_key=app_key,
            app_secret=app_secret,
            sign_secret="",  # OAuth不需要签名密钥
            server_url=server_url,
            oauth_base_url=server_url,
        )

        self.http_client = AsyncHTTPClient(http_config)
        self._oauth_manager = AsyncOAuthManager(self.config, self.http_client)

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
        """关闭客户端"""
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
            scope: 授权范围列表，如 ["merchant_order", "merchant_item"]
            state: 状态参数，用于防CSRF攻击

        Returns:
            授权URL

        Example:
            ```python
            client = OAuthClient("your_app_key", "your_app_secret")
            auth_url = client.get_authorize_url(
                redirect_uri="https://your-app.com/callback",
                scope=["merchant_order", "merchant_item"],
                state="random_state_string"
            )
            print(f"请访问: {auth_url}")
            ```
        """
        return self._oauth_manager.get_authorize_url(redirect_uri, scope, state)

    async def get_access_token(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> TokenResponse:
        """使用授权码获取访问令牌

        Args:
            code: 授权回调返回的授权码
            redirect_uri: 回调地址（某些情况下需要）

        Returns:
            Token响应对象

        Example:
            ```python
            token_response = await client.get_access_token("authorization_code")
            access_token = token_response.access_token
            refresh_token = token_response.refresh_token
            expires_in = token_response.expires_in
            ```
        """
        return await self._oauth_manager.get_access_token(code, redirect_uri)

    async def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        """刷新访问令牌

        Args:
            refresh_token: 刷新令牌

        Returns:
            新的Token响应对象

        Example:
            ```python
            new_token = await client.refresh_access_token(old_refresh_token)
            # 使用新的access_token进行API调用
            ```
        """
        return await self._oauth_manager.refresh_access_token(refresh_token)

    async def get_client_credentials_token(self) -> TokenResponse:
        """客户端凭证模式获取令牌

        用于不需要用户授权的场景，通常用于获取应用级别的访问权限。

        Returns:
            Token响应对象

        Example:
            ```python
            app_token = await client.get_client_credentials_token()
            # 使用应用级别的token调用相关API
            ```
        """
        return await self._oauth_manager.get_client_credentials_token()

    async def revoke_token(self, token: str, token_type: str = "access_token") -> bool:
        """撤销令牌

        Args:
            token: 要撤销的令牌
            token_type: 令牌类型，"access_token" 或 "refresh_token"

        Returns:
            是否撤销成功

        Example:
            ```python
            success = await client.revoke_token(access_token, "access_token")
            if success:
                print("令牌已撤销")
            ```
        """
        return await self._oauth_manager.revoke_token(token, token_type)


class SyncOAuthClient:
    """同步OAuth认证客户端

    专门处理OAuth认证流程的同步客户端类。
    """

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        server_url: str = "https://openapi.kwaixiaodian.com",
        http_config: Optional[HTTPConfig] = None,
    ):
        """初始化同步OAuth客户端

        Args:
            app_key: 应用Key
            app_secret: 应用Secret
            server_url: 服务器地址
            http_config: HTTP配置
        """
        self.config = AuthConfig(
            app_key=app_key,
            app_secret=app_secret,
            sign_secret="",  # OAuth不需要签名密钥
            server_url=server_url,
            oauth_base_url=server_url,
        )

        self.http_client = SyncHTTPClient(http_config)
        self._oauth_manager = SyncOAuthManager(self.config, self.http_client)

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
        self.close()

    def close(self) -> None:
        """关闭客户端"""
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
            scope: 授权范围列表，如 ["merchant_order", "merchant_item"]
            state: 状态参数，用于防CSRF攻击

        Returns:
            授权URL

        Example:
            ```python
            client = SyncOAuthClient("your_app_key", "your_app_secret")
            auth_url = client.get_authorize_url(
                redirect_uri="https://your-app.com/callback",
                scope=["merchant_order", "merchant_item"],
                state="random_state_string"
            )
            print(f"请访问: {auth_url}")
            ```
        """
        return self._oauth_manager.get_authorize_url(redirect_uri, scope, state)

    def get_access_token(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> TokenResponse:
        """使用授权码获取访问令牌

        Args:
            code: 授权回调返回的授权码
            redirect_uri: 回调地址（某些情况下需要）

        Returns:
            Token响应对象

        Example:
            ```python
            token_response = client.get_access_token("authorization_code")
            access_token = token_response.access_token
            refresh_token = token_response.refresh_token
            expires_in = token_response.expires_in
            ```
        """
        return self._oauth_manager.get_access_token(code, redirect_uri)

    def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        """刷新访问令牌

        Args:
            refresh_token: 刷新令牌

        Returns:
            新的Token响应对象

        Example:
            ```python
            new_token = await client.refresh_access_token(old_refresh_token)
            # 使用新的access_token进行API调用
            ```
        """
        return self._oauth_manager.refresh_access_token(refresh_token)

    def get_client_credentials_token(self) -> TokenResponse:
        """客户端凭证模式获取令牌

        用于不需要用户授权的场景，通常用于获取应用级别的访问权限。

        Returns:
            Token响应对象

        Example:
            ```python
            app_token = client.get_client_credentials_token()
            # 使用应用级别的token调用相关API
            ```
        """
        return self._oauth_manager.get_client_credentials_token()

    def revoke_token(self, token: str, token_type: str = "access_token") -> bool:
        """撤销令牌

        Args:
            token: 要撤销的令牌
            token_type: 令牌类型，"access_token" 或 "refresh_token"

        Returns:
            是否撤销成功

        Example:
            ```python
            success = await client.revoke_token(access_token, "access_token")
            if success:
                print("令牌已撤销")
            ```
        """
        return self._oauth_manager.revoke_token(token, token_type)
