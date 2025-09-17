"""同步客户端测试用例"""

from unittest.mock import Mock, patch

import pytest

from kwaixiaodian import SyncKwaixiaodianClient, SyncOAuthClient
from kwaixiaodian.exceptions import KwaixiaodianAPIError
from kwaixiaodian.models.order import OrderListResponse


class TestSyncKwaixiaodianClient:
    """同步客户端基础测试"""

    def setup_method(self):
        """设置测试环境"""
        self.client = SyncKwaixiaodianClient(
            app_key="test_app_key",
            app_secret="test_app_secret",
            sign_secret="test_sign_secret",
            server_url="https://test.example.com",
        )

    def teardown_method(self):
        """清理测试环境"""
        self.client.close()

    def test_client_initialization(self):
        """测试客户端初始化"""
        assert self.client.config.app_key == "test_app_key"
        assert self.client.config.app_secret == "test_app_secret"
        assert self.client.config.sign_secret == "test_sign_secret"
        assert self.client.config.server_url == "https://test.example.com"

    def test_context_manager(self):
        """测试上下文管理器"""
        with SyncKwaixiaodianClient(
            app_key="test_key", app_secret="test_secret", sign_secret="test_sign"
        ) as client:
            assert client is not None
            assert isinstance(client, SyncKwaixiaodianClient)

    def test_order_service_property(self):
        """测试订单服务属性"""
        order_service = self.client.order
        assert order_service is not None

        # 确保重复调用返回同一实例
        order_service2 = self.client.order
        assert order_service is order_service2

    def test_item_service_property(self):
        """测试商品服务属性"""
        item_service = self.client.item
        assert item_service is not None

        # 确保重复调用返回同一实例
        item_service2 = self.client.item
        assert item_service is item_service2

    @patch("kwaixiaodian.http.sync_client.SyncHTTPClient.get")
    def test_order_list_success(self, mock_get):
        """测试订单列表获取成功"""
        # 模拟HTTP响应
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": [],  # result 应该是订单列表
            "error_msg": "",
            "has_more": False,
            "pcursor": "",
        }
        mock_get.return_value = mock_response

        # 调用订单列表接口
        response = self.client.order.list(
            access_token="test_token",
            begin_time="2024-01-01 00:00:00",
            end_time="2024-01-31 23:59:59",
        )

        # 验证结果
        assert isinstance(response, OrderListResponse)
        assert response.is_success
        mock_get.assert_called_once()

    @patch("kwaixiaodian.http.sync_client.SyncHTTPClient.get")
    def test_api_error_handling(self, mock_get):
        """测试API错误处理"""
        # 模拟API错误响应
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": None,  # 错误响应时 result 为 null
            "error_msg": "参数错误",
            "error_code": "INVALID_PARAM",
            "sub_code": "PARAM_MISSING",
        }
        mock_get.return_value = mock_response

        # 验证抛出API错误
        with pytest.raises(KwaixiaodianAPIError) as exc_info:
            self.client.order.list(
                access_token="test_token",
                begin_time="2024-01-01 00:00:00",
                end_time="2024-01-31 23:59:59",
            )

        assert "参数错误" in str(exc_info.value)


class TestSyncOAuthClient:
    """同步OAuth客户端测试"""

    def setup_method(self):
        """设置测试环境"""
        self.client = SyncOAuthClient(
            app_key="test_app_key",
            app_secret="test_app_secret",
            server_url="https://test.example.com",
        )

    def teardown_method(self):
        """清理测试环境"""
        self.client.close()

    def test_oauth_client_initialization(self):
        """测试OAuth客户端初始化"""
        assert self.client.config.app_key == "test_app_key"
        assert self.client.config.app_secret == "test_app_secret"
        assert self.client.config.server_url == "https://test.example.com"

    def test_get_authorize_url(self):
        """测试获取授权URL"""
        auth_url = self.client.get_authorize_url(
            redirect_uri="https://example.com/callback",
            scope=["merchant_order", "merchant_item"],
            state="test_state",
        )

        assert "https://test.example.com/oauth2/authorize" in auth_url
        assert "client_id=test_app_key" in auth_url
        assert "redirect_uri=https%3A%2F%2Fexample.com%2Fcallback" in auth_url
        assert "scope=merchant_order%2Cmerchant_item" in auth_url
        assert "state=test_state" in auth_url

    def test_context_manager(self):
        """测试OAuth客户端上下文管理器"""
        with SyncOAuthClient(app_key="test_key", app_secret="test_secret") as client:
            assert client is not None
            assert isinstance(client, SyncOAuthClient)

    @patch("kwaixiaodian.http.sync_client.SyncHTTPClient.post")
    def test_get_access_token_success(self, mock_post):
        """测试获取访问令牌成功"""
        # 模拟成功的token响应
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "expires_in": 3600,
            "refresh_token": "test_refresh_token",
            "token_type": "Bearer",
        }
        mock_post.return_value = mock_response

        # 获取访问令牌
        token_response = self.client.get_access_token("test_code")

        # 验证结果
        assert token_response.access_token == "test_access_token"
        assert token_response.expires_in == 3600
        assert token_response.refresh_token == "test_refresh_token"
        assert token_response.token_type == "Bearer"

        mock_post.assert_called_once()


class TestSyncClientComparison:
    """同步与异步客户端对比测试"""

    def test_sync_vs_async_interface_consistency(self):
        """测试同步和异步客户端接口一致性"""
        # 同步客户端
        sync_client = SyncKwaixiaodianClient(
            app_key="test", app_secret="test", sign_secret="test"
        )

        # 检查同步客户端有相同的服务属性
        assert hasattr(sync_client, "order")
        assert hasattr(sync_client, "item")
        assert hasattr(sync_client, "close")

        # 检查同步服务有相同的方法
        sync_order_service = sync_client.order
        assert hasattr(sync_order_service, "list")
        assert hasattr(sync_order_service, "get")
        assert hasattr(sync_order_service, "ship")
        assert hasattr(sync_order_service, "update_remark")

        sync_item_service = sync_client.item
        assert hasattr(sync_item_service, "list")
        assert hasattr(sync_item_service, "get")
        assert hasattr(sync_item_service, "create")
        assert hasattr(sync_item_service, "update")
        assert hasattr(sync_item_service, "update_stock")
        assert hasattr(sync_item_service, "delete")

        sync_client.close()

    def test_import_both_clients(self):
        """测试可以同时导入异步和同步客户端"""
        from kwaixiaodian import (
            AsyncKwaixiaodianClient,
            AsyncOAuthClient,
            SyncKwaixiaodianClient,
            SyncOAuthClient,
        )

        # 验证类不相同但都可用
        assert AsyncKwaixiaodianClient != SyncKwaixiaodianClient
        assert AsyncOAuthClient != SyncOAuthClient

        # 验证都可以实例化
        async_client = AsyncKwaixiaodianClient("test", "test", "test")
        sync_client = SyncKwaixiaodianClient("test", "test", "test")

        async_oauth = AsyncOAuthClient("test", "test")
        sync_oauth = SyncOAuthClient("test", "test")

        # 清理
        import asyncio

        asyncio.run(async_client.close())
        sync_client.close()
        asyncio.run(async_oauth.close())
        sync_oauth.close()
