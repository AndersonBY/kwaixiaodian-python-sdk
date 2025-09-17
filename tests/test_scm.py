"""SCM 模块单元测试"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from kwaixiaodian.client.services.scm import AsyncScmService, SyncScmService
from kwaixiaodian.models.scm import (
    InventoryAdjustParam,
    InventoryAdjustRequest,
    InventoryAdjustResponse,
    InventoryDetailParam,
    InventoryDetailRequest,
    InventoryDetailResponse,
    InventoryUpdateResponse,
    WareAddParam,
    WareAddResponse,
    WarehouseAddParam,
    WarehouseAddResponse,
    WarehouseQueryParam,
    WarehouseQueryRequest,
    WarehouseQueryResponse,
    WareListResponse,
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
def async_scm_service(mock_async_client):
    """异步SCM服务实例"""
    return AsyncScmService(mock_async_client)


@pytest.fixture
def sync_scm_service(mock_sync_client):
    """同步SCM服务实例"""
    return SyncScmService(mock_sync_client)


class TestAsyncScmService:
    """测试异步SCM服务"""

    @pytest.mark.asyncio
    async def test_inventory_adjust(self, async_scm_service, mock_async_client):
        """测试库存调整"""
        # 模拟响应
        mock_response = InventoryAdjustResponse(data={"result": "success"})
        mock_async_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = await async_scm_service.inventory_adjust(
            access_token="test_token",
            ware_out_code="WARE001",
            idempotent_id="test-id-001",
            warehouse_out_code="WH001",
            operation_type="INCREASE",
            adjust_quantity=10,
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_async_client.execute.call_args
        assert args[1] is InventoryAdjustResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.ware_out_code == "WARE001"
        assert req.param.idempotent_id == "test-id-001"
        assert req.param.warehouse_out_code == "WH001"
        assert req.param.operation_type == "INCREASE"
        assert req.param.adjust_quantity == 10

    @pytest.mark.asyncio
    async def test_inventory_detail(self, async_scm_service, mock_async_client):
        """测试库存详情查询"""
        # 模拟响应
        mock_response = InventoryDetailResponse(
            data={"ware_out_code": "WARE001", "total_quantity": 100}
        )
        mock_async_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = await async_scm_service.inventory_detail(
            access_token="test_token", ware_out_code="WARE001"
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_async_client.execute.call_args
        assert args[1] is InventoryDetailResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.ware_out_code == "WARE001"

    @pytest.mark.asyncio
    async def test_inventory_update(self, async_scm_service, mock_async_client):
        """测试库存更新"""
        # 模拟响应
        mock_response = InventoryUpdateResponse(data={"result": "success"})
        mock_async_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = await async_scm_service.inventory_update(
            access_token="test_token",
            ware_out_code="WARE001",
            quantity=50,
            warehouse_out_code="WH001",
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_async_client.execute.call_args
        assert args[1] is InventoryUpdateResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.ware_out_code == "WARE001"
        assert req.param.quantity == 50
        assert req.param.warehouse_out_code == "WH001"

    @pytest.mark.asyncio
    async def test_ware_add(self, async_scm_service, mock_async_client):
        """测试商品添加"""
        # 模拟响应
        mock_response = WareAddResponse(data={"ware_id": 789})
        mock_async_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = await async_scm_service.ware_add(
            access_token="test_token",
            ware_name="测试商品",
            ware_out_code="WARE001",
            ware_weight=1000,
            ware_volume=2000,
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_async_client.execute.call_args
        assert args[1] is WareAddResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.ware_name == "测试商品"
        assert req.param.ware_out_code == "WARE001"
        assert req.param.ware_weight == 1000
        assert req.param.ware_volume == 2000

    @pytest.mark.asyncio
    async def test_warehouse_add(self, async_scm_service, mock_async_client):
        """测试仓库添加"""
        # 模拟响应
        mock_response = WarehouseAddResponse(data={"warehouse_id": 999})
        mock_async_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = await async_scm_service.warehouse_add(
            access_token="test_token",
            warehouse_name="测试仓库",
            warehouse_out_code="WH001",
            province="北京",
            city="北京",
            district="朝阳区",
            address="测试地址",
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_async_client.execute.call_args
        assert args[1] is WarehouseAddResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.warehouse_name == "测试仓库"
        assert req.param.warehouse_out_code == "WH001"
        assert req.param.province == "北京"
        assert req.param.city == "北京"
        assert req.param.district == "朝阳区"
        assert req.param.address == "测试地址"

    @pytest.mark.asyncio
    async def test_warehouse_query(self, async_scm_service, mock_async_client):
        """测试仓库列表查询"""
        # 模拟响应
        mock_response = WarehouseQueryResponse(
            data={"warehouses": [{"warehouse_id": 123, "warehouse_name": "仓库1"}]}
        )
        mock_async_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = await async_scm_service.warehouse_query(
            access_token="test_token", page_no=1, page_size=10
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_async_client.execute.call_args
        assert args[1] is WarehouseQueryResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.page_no == 1
        assert req.param.page_size == 10


class TestSyncScmService:
    """测试同步SCM服务"""

    def test_inventory_adjust(self, sync_scm_service, mock_sync_client):
        """测试库存调整 (同步)"""
        # 模拟响应
        mock_response = InventoryAdjustResponse(data={"result": "success"})
        mock_sync_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = sync_scm_service.inventory_adjust(
            access_token="test_token",
            ware_out_code="WARE001",
            idempotent_id="test-id-001",
            warehouse_out_code="WH001",
            operation_type="INCREASE",
            adjust_quantity=10,
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_sync_client.execute.call_args
        assert args[1] is InventoryAdjustResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.ware_out_code == "WARE001"
        assert req.param.idempotent_id == "test-id-001"
        assert req.param.warehouse_out_code == "WH001"
        assert req.param.operation_type == "INCREASE"
        assert req.param.adjust_quantity == 10

    def test_warehouse_add(self, sync_scm_service, mock_sync_client):
        """测试仓库添加 (同步)"""
        # 模拟响应
        mock_response = WarehouseAddResponse(data={"warehouse_id": 999})
        mock_sync_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = sync_scm_service.warehouse_add(
            access_token="test_token",
            warehouse_name="测试仓库",
            warehouse_out_code="WH001",
            province="北京",
            city="北京",
            district="朝阳区",
            address="测试地址",
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_sync_client.execute.call_args
        assert args[1] is WarehouseAddResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.warehouse_name == "测试仓库"
        assert req.param.warehouse_out_code == "WH001"
        assert req.param.province == "北京"
        assert req.param.city == "北京"
        assert req.param.district == "朝阳区"
        assert req.param.address == "测试地址"

    def test_ware_list(self, sync_scm_service, mock_sync_client):
        """测试商品列表查询 (同步)"""
        # 模拟响应
        mock_response = WareListResponse(
            data={"wares": [{"ware_id": 123, "ware_name": "商品1"}]}
        )
        mock_sync_client.execute.return_value = mock_response

        # 调用方法（展开入参）
        result = sync_scm_service.ware_list(
            access_token="test_token",
            warehouse_out_code="WH001",
            page_no=1,
            page_size=10,
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        args, kwargs = mock_sync_client.execute.call_args
        assert args[1] is WareListResponse
        req = args[0]
        assert req.access_token == "test_token"
        assert req.param.warehouse_out_code == "WH001"
        assert req.param.page_no == 1
        assert req.param.page_size == 10


class TestScmModels:
    """测试SCM服务数据模型"""

    def test_inventory_adjust_param(self):
        """测试库存调整参数模型"""
        param = InventoryAdjustParam(
            ware_out_code="WARE001",
            idempotent_id="test-id-001",
            warehouse_out_code="WH001",
            operation_type="INCREASE",
            adjust_quantity=10,
        )

        assert param.ware_out_code == "WARE001"
        assert param.idempotent_id == "test-id-001"
        assert param.warehouse_out_code == "WH001"
        assert param.operation_type == "INCREASE"
        assert param.adjust_quantity == 10

    def test_inventory_adjust_request(self):
        """测试库存调整请求模型"""
        param = InventoryAdjustParam(
            ware_out_code="WARE001",
            idempotent_id="test-id-001",
            warehouse_out_code="WH001",
            operation_type="INCREASE",
            adjust_quantity=10,
        )
        request = InventoryAdjustRequest(access_token="test_token", param=param)

        assert request.access_token == "test_token"
        assert request.param == param
        assert request.api_method == "open.scm.inventory.adjust"
        assert request.http_method == "POST"

    def test_warehouse_add_param(self):
        """测试仓库添加参数模型"""
        param = WarehouseAddParam(
            warehouse_name="测试仓库",
            warehouse_out_code="WH001",
            province="北京",
            city="北京",
            district="朝阳区",
            address="测试地址",
        )

        assert param.warehouse_name == "测试仓库"
        assert param.warehouse_out_code == "WH001"
        assert param.province == "北京"
        assert param.city == "北京"
        assert param.district == "朝阳区"
        assert param.address == "测试地址"

    def test_ware_add_param(self):
        """测试商品添加参数模型"""
        param = WareAddParam(
            ware_name="测试商品",
            ware_out_code="WARE001",
            ware_weight=1000,
            ware_volume=2000,
        )

        assert param.ware_name == "测试商品"
        assert param.ware_out_code == "WARE001"
        assert param.ware_weight == 1000
        assert param.ware_volume == 2000

    def test_inventory_detail_request(self):
        """测试库存详情请求模型"""
        param = InventoryDetailParam(ware_out_code="WARE001")
        request = InventoryDetailRequest(access_token="test_token", param=param)

        assert request.access_token == "test_token"
        assert request.param.ware_out_code == "WARE001"
        assert request.api_method == "open.scm.inventory.detail"
        assert request.http_method == "GET"

    def test_warehouse_query_request(self):
        """测试仓库查询请求模型"""
        param = WarehouseQueryParam(page_no=1, page_size=20)
        request = WarehouseQueryRequest(access_token="test_token", param=param)

        assert request.access_token == "test_token"
        assert request.param.page_no == 1
        assert request.param.page_size == 20
        assert request.api_method == "open.scm.warehouse.query"
        assert request.http_method == "GET"
