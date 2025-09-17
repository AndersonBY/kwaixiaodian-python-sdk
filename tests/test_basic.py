"""基础功能测试"""

import pytest

from kwaixiaodian import AsyncKwaixiaodianClient, AsyncOAuthClient
from kwaixiaodian.auth import AuthConfig, SignatureManager, SignMethod
from kwaixiaodian.models.common import OrderStatus
from kwaixiaodian.models.item import Item
from kwaixiaodian.models.order import Order, OrderListRequest


class TestAuthConfig:
    """认证配置测试"""

    def test_auth_config_creation(self):
        """测试认证配置创建"""
        config = AuthConfig(
            app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
        )

        assert config.app_key == "test_key"
        assert config.app_secret == "test_secret"
        assert config.sign_secret == "test_sign_secret"
        assert config.sign_method == SignMethod.HMAC_SHA256
        assert config.server_url == "https://openapi.kwaixiaodian.com"


class TestSignatureManager:
    """签名管理器测试"""

    def test_signature_generation(self):
        """测试签名生成"""
        config = AuthConfig(
            app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
        )

        signature_manager = SignatureManager(config)

        # 构建测试参数
        business_params = {"item_id": 123456, "status": 1}
        signed_params = signature_manager.build_signed_params(
            method="open.item.get",
            access_token="test_token",
            business_params=business_params,
        )

        # 验证必要字段存在
        assert "method" in signed_params
        assert "appkey" in signed_params
        assert "access_token" in signed_params
        assert "timestamp" in signed_params
        assert "signMethod" in signed_params
        assert "sign" in signed_params
        assert "param" in signed_params

        assert signed_params["method"] == "open.item.get"
        assert signed_params["appkey"] == "test_key"
        assert signed_params["access_token"] == "test_token"


class TestDataModels:
    """数据模型测试"""

    def test_order_model(self):
        """测试订单模型"""
        order_data = {
            "order_id": "20240101001",
            "order_status": OrderStatus.WAIT_DELIVER,  # 使用枚举而不是整数
            "seller_id": 123456,
            "create_time": "2024-01-01 10:00:00",
            "total_amount": 99900,  # 999元
            "pay_amount": 99900,
            "items": [],
        }

        order = Order(**order_data)

        assert order.order_id == "20240101001"
        assert order.total_yuan == 999.0
        assert order.pay_yuan == 999.0
        assert order.is_paid
        assert not order.is_delivered

    def test_item_model(self):
        """测试商品模型"""
        item_data = {
            "item_id": 123456,
            "title": "测试商品",
            "status": 1,
            "price": 9999,  # 99.99元
            "original_price": 12999,  # 129.99元
            "stock": 100,
            "main_image": "https://example.com/image.jpg",
            "images": ["https://example.com/image1.jpg"],
            "skus": [],
        }

        item = Item(**item_data)

        assert item.item_id == 123456
        assert item.title == "测试商品"
        assert item.price_yuan == 99.99
        assert item.original_price_yuan == 129.99
        assert item.is_in_stock
        assert not item.is_multi_sku

    def test_request_model(self):
        """测试请求模型"""
        request = OrderListRequest(
            access_token="test_token",
            begin_time="2024-01-01 00:00:00",
            end_time="2024-01-31 23:59:59",
            page_size=50,
            api_version="1",
        )

        # Java reference: open.order.cursor.list
        assert request.api_method == "open.order.cursor.list"
        assert request.access_token == "test_token"

        business_params = request.get_business_params()
        # Our models dump by alias (ParamDTO), matching Java field names
        assert "beginTime" in business_params
        assert "endTime" in business_params
        assert "pageSize" in business_params

        # 公共参数不应包含在业务参数中
        assert "access_token" not in business_params
        assert "uid" not in business_params


class TestOAuthClient:
    """OAuth客户端测试"""

    def test_oauth_client_creation(self):
        """测试OAuth客户端创建"""
        oauth_client = AsyncOAuthClient(app_key="test_key", app_secret="test_secret")

        assert oauth_client.config.app_key == "test_key"
        assert oauth_client.config.app_secret == "test_secret"

    def test_get_authorize_url(self):
        """测试获取授权URL"""
        oauth_client = AsyncOAuthClient(app_key="test_key", app_secret="test_secret")

        auth_url = oauth_client.get_authorize_url(
            redirect_uri="https://example.com/callback",
            scope=["merchant_order", "merchant_item"],
            state="test_state",
        )

        assert "response_type=code" in auth_url
        assert "client_id=test_key" in auth_url
        assert "redirect_uri=https%3A%2F%2Fexample.com%2Fcallback" in auth_url
        assert "scope=merchant_order%2Cmerchant_item" in auth_url
        assert "state=test_state" in auth_url


class TestKwaixiaodianClient:
    """快手SDK客户端测试"""

    def test_client_creation(self):
        """测试客户端创建"""
        client = AsyncKwaixiaodianClient(
            app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
        )

        assert client.config.app_key == "test_key"
        assert client.config.app_secret == "test_secret"
        assert client.config.sign_secret == "test_sign_secret"

    def test_service_properties(self):
        """测试业务服务属性"""
        client = AsyncKwaixiaodianClient(
            app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
        )

        # 测试服务属性存在
        assert hasattr(client, "order")
        assert hasattr(client, "item")

        # 测试服务类型
        from kwaixiaodian.client.services import AsyncItemService, AsyncOrderService

        assert isinstance(client.order, AsyncOrderService)
        assert isinstance(client.item, AsyncItemService)


if __name__ == "__main__":
    pytest.main([__file__])
