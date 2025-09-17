"""Dropshipping 模块单元测试"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from kwaixiaodian.client.services.dropshipping import (
    AsyncDropshippingService,
    SyncDropshippingService,
)
from kwaixiaodian.models.dropshipping import (
    AddressInfo,
    DsOrderGetRequest,
    EbillBatchGetRequest,
    EbillBatchGetResponse,
    EbillCancelRequest,
    EbillCancelResponse,
    OrderBatchAllocateRequest,
    OrderBatchAllocateResponse,
    OrderDeliverResponse,
    RoleQueryRequest,
    RoleQueryResponse,
)


@pytest.fixture
def mock_async_client():
    """Mock异步客户端"""
    client = AsyncMock()
    return client


@pytest.fixture
def mock_sync_client():
    """Mock同步客户端"""
    client = MagicMock()
    return client


@pytest.fixture
def async_dropshipping_service(mock_async_client):
    """异步代发服务实例"""
    return AsyncDropshippingService(mock_async_client)


@pytest.fixture
def sync_dropshipping_service(mock_sync_client):
    """同步代发服务实例"""
    return SyncDropshippingService(mock_sync_client)


class TestAsyncDropshippingService:
    """测试异步代发服务"""

    @pytest.mark.asyncio
    async def test_batch_get_ebill(self, async_dropshipping_service, mock_async_client):
        """测试批量获取电子面单"""
        # 模拟响应
        mock_response = EbillBatchGetResponse()
        mock_async_client.execute.return_value = mock_response

        # 准备测试数据
        ds_order_get_req = [
            DsOrderGetRequest(
                allocate_order_code="order123",
                user_code="user123",
                sender_address=AddressInfo(
                    province="北京市",
                    city="北京市",
                    district="朝阳区",
                    detail="某某街道123号",
                    name="张三",
                    phone="13800138000",
                ),
            )
        ]

        # 调用方法
        result = await async_dropshipping_service.batch_get_ebill(
            access_token="test_token", ds_order_get_req=ds_order_get_req
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        mock_async_client.execute.assert_called_once()
        call_args = mock_async_client.execute.call_args

        request = call_args[0][0]  # 第一个位置参数
        response_class = call_args[0][1]  # 第二个位置参数

        assert isinstance(request, EbillBatchGetRequest)
        assert request.access_token == "test_token"
        assert request.ds_order_get_req == ds_order_get_req
        assert response_class == EbillBatchGetResponse

    @pytest.mark.asyncio
    async def test_cancel_ebill(self, async_dropshipping_service, mock_async_client):
        """测试取消电子面单"""
        # 模拟响应
        mock_response = EbillCancelResponse()
        mock_async_client.execute.return_value = mock_response

        # 调用方法
        result = await async_dropshipping_service.cancel_ebill(
            access_token="test_token",
            waybill_code="12345678",
            express_company_code="SF",
            user_code="user123",
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        mock_async_client.execute.assert_called_once()
        call_args = mock_async_client.execute.call_args

        request = call_args[0][0]
        response_class = call_args[0][1]

        assert isinstance(request, EbillCancelRequest)
        assert request.access_token == "test_token"
        assert request.waybill_code == "12345678"
        assert request.express_company_code == "SF"
        assert request.user_code == "user123"
        assert response_class == EbillCancelResponse

    @pytest.mark.asyncio
    async def test_batch_allocate_order(
        self, async_dropshipping_service, mock_async_client
    ):
        """测试批量分配订单"""
        # 模拟响应
        mock_response = OrderBatchAllocateResponse()
        mock_async_client.execute.return_value = mock_response

        # 调用方法
        result = await async_dropshipping_service.batch_allocate_order(
            access_token="test_token",
            dropshipping_order_code_list=["order1", "order2", "order3"],
            factory_code="factory123",
        )

        # 验证结果
        assert result == mock_response
        mock_async_client.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_deliver_order(self, async_dropshipping_service, mock_async_client):
        """测试订单发货"""
        # 模拟响应
        mock_response = OrderDeliverResponse()
        mock_async_client.execute.return_value = mock_response

        # 调用方法
        result = await async_dropshipping_service.deliver_order(
            access_token="test_token",
            return_address_id=123,
            waybill_code="SF123456789",
            user_code="user123",
            allocate_order_code="order123",
            express_company_code="SF",
            serial_number_list=["SN001", "SN002"],
            imei_list=["IMEI001", "IMEI002"],
        )

        # 验证结果
        assert result == mock_response
        mock_async_client.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_query_role(self, async_dropshipping_service, mock_async_client):
        """测试查询角色"""
        # 模拟响应
        mock_response = RoleQueryResponse()
        mock_async_client.execute.return_value = mock_response

        # 调用方法
        result = await async_dropshipping_service.query_role(access_token="test_token")

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        mock_async_client.execute.assert_called_once()
        call_args = mock_async_client.execute.call_args

        request = call_args[0][0]
        response_class = call_args[0][1]

        assert isinstance(request, RoleQueryRequest)
        assert request.access_token == "test_token"
        assert response_class == RoleQueryResponse


class TestSyncDropshippingService:
    """测试同步代发服务"""

    def test_batch_get_ebill(self, sync_dropshipping_service, mock_sync_client):
        """测试批量获取电子面单 (同步)"""
        # 模拟响应
        mock_response = EbillBatchGetResponse()
        mock_sync_client.execute.return_value = mock_response

        # 准备测试数据
        ds_order_get_req = [
            DsOrderGetRequest(allocate_order_code="order123", user_code="user123")
        ]

        # 调用方法
        result = sync_dropshipping_service.batch_get_ebill(
            access_token="test_token", ds_order_get_req=ds_order_get_req
        )

        # 验证结果
        assert result == mock_response
        mock_sync_client.execute.assert_called_once()

    def test_cancel_ebill(self, sync_dropshipping_service, mock_sync_client):
        """测试取消电子面单 (同步)"""
        # 模拟响应
        mock_response = EbillCancelResponse()
        mock_sync_client.execute.return_value = mock_response

        # 调用方法
        result = sync_dropshipping_service.cancel_ebill(
            access_token="test_token",
            waybill_code="12345678",
            express_company_code="SF",
            user_code="user123",
        )

        # 验证结果
        assert result == mock_response
        mock_sync_client.execute.assert_called_once()

    def test_query_role(self, sync_dropshipping_service, mock_sync_client):
        """测试查询角色 (同步)"""
        # 模拟响应
        mock_response = RoleQueryResponse()
        mock_sync_client.execute.return_value = mock_response

        # 调用方法
        result = sync_dropshipping_service.query_role(access_token="test_token")

        # 验证结果
        assert result == mock_response
        mock_sync_client.execute.assert_called_once()


class TestDropshippingModels:
    """测试代发服务数据模型"""

    def test_ds_order_get_request_model(self):
        """测试DsOrderGetRequest模型"""
        order_request = DsOrderGetRequest(
            allocate_order_code="order123",
            user_code="user123",
            total_package_quantity=5,
            total_package_weight=2.5,
        )

        assert order_request.allocate_order_code == "order123"
        assert order_request.user_code == "user123"
        assert order_request.total_package_quantity == 5
        assert order_request.total_package_weight == 2.5

    def test_address_info_model(self):
        """测试AddressInfo模型"""
        address = AddressInfo(
            province="广东省",
            city="深圳市",
            district="南山区",
            detail="科技园南区12号楼",
            name="李四",
            phone="13900139000",
        )

        assert address.province == "广东省"
        assert address.city == "深圳市"
        assert address.district == "南山区"
        assert address.detail == "科技园南区12号楼"
        assert address.name == "李四"
        assert address.phone == "13900139000"

    def test_ebill_batch_get_request(self):
        """测试电子面单批量获取请求模型"""
        request = EbillBatchGetRequest(
            access_token="test_token",
            ds_order_get_req=[
                DsOrderGetRequest(allocate_order_code="order1", user_code="user1")
            ],
        )

        assert request.api_method == "open.dropshipping.ebill.batch.get"
        assert request.access_token == "test_token"
        assert len(request.ds_order_get_req) == 1
        assert request.ds_order_get_req[0].allocate_order_code == "order1"

    def test_ebill_cancel_request(self):
        """测试电子面单取消请求模型"""
        request = EbillCancelRequest(
            access_token="test_token",
            waybill_code="SF123456789",
            express_company_code="SF",
            user_code="user123",
        )

        assert request.api_method == "open.dropshipping.ebill.cancel"
        assert request.access_token == "test_token"
        assert request.waybill_code == "SF123456789"
        assert request.express_company_code == "SF"
        assert request.user_code == "user123"

    def test_order_batch_allocate_request(self):
        """测试订单批量分配请求模型"""
        request = OrderBatchAllocateRequest(
            access_token="test_token",
            dropshipping_order_code_list=["order1", "order2"],
            factory_code="factory123",
        )

        assert request.api_method == "open.dropshipping.order.batch.allocate"
        assert request.access_token == "test_token"
        assert request.dropshipping_order_code_list == ["order1", "order2"]
        assert request.factory_code == "factory123"

    def test_role_query_request(self):
        """测试查询角色请求模型"""
        request = RoleQueryRequest(access_token="test_token")

        assert request.api_method == "open.dropshipping.role.query"
        assert request.access_token == "test_token"
        assert request.http_method.value == "GET"  # 这是唯一的GET方法
