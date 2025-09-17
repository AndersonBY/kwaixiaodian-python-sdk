"""Customer Service 模块单元测试"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from kwaixiaodian.client.services.customer_service import (
    AsyncCustomerServiceService,
    SyncCustomerServiceService,
)
from kwaixiaodian.models.customer_service import (
    CsGroupInfo,
    CsUser,
    DispatchingGroupAddRequest,
    DispatchingGroupAddResponse,
    IntelligentMessageSendRequest,
    IntelligentMessageSendResponse,
    MessageContent,
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
def async_cs_service(mock_async_client):
    """异步客服服务实例"""
    return AsyncCustomerServiceService(mock_async_client)


@pytest.fixture
def sync_cs_service(mock_sync_client):
    """同步客服服务实例"""
    return SyncCustomerServiceService(mock_sync_client)


class TestAsyncCustomerServiceService:
    """测试异步客服服务"""

    @pytest.mark.asyncio
    async def test_send_intelligent_message(self, async_cs_service, mock_async_client):
        """测试发送智能消息"""
        # 模拟响应
        mock_response = IntelligentMessageSendResponse()
        mock_async_client.execute.return_value = mock_response

        # 准备测试数据
        to_user = CsUser(nick_name="customer1", role=1)
        message_list = [
            MessageContent(content_type=1, content="您好，有什么可以帮助您的？")
        ]

        # 调用方法
        result = await async_cs_service.send_intelligent_message(
            access_token="test_token", to_user=to_user, message_list=message_list
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        mock_async_client.execute.assert_called_once()
        call_args = mock_async_client.execute.call_args

        request = call_args[0][0]  # 第一个位置参数
        response_class = call_args[0][1]  # 第二个位置参数

        assert isinstance(request, IntelligentMessageSendRequest)
        assert request.access_token == "test_token"
        assert request.to_user == to_user
        assert request.message_list == message_list
        assert response_class == IntelligentMessageSendResponse

    @pytest.mark.asyncio
    async def test_add_dispatch_group(self, async_cs_service, mock_async_client):
        """测试添加客服分组"""
        # 模拟响应
        mock_response = DispatchingGroupAddResponse(data=CsGroupInfo(group_id=12345))
        mock_async_client.execute.return_value = mock_response

        # 调用方法
        result = await async_cs_service.add_dispatch_group(
            access_token="test_token", group_name="VIP客服组"
        )

        # 验证结果
        assert result == mock_response

        # 验证调用参数
        mock_async_client.execute.assert_called_once()
        call_args = mock_async_client.execute.call_args

        request = call_args[0][0]
        response_class = call_args[0][1]

        assert isinstance(request, DispatchingGroupAddRequest)
        assert request.access_token == "test_token"
        assert request.group_name == "VIP客服组"
        assert response_class == DispatchingGroupAddResponse

    @pytest.mark.asyncio
    async def test_add_commodity_mapping(self, async_cs_service, mock_async_client):
        """测试添加商品映射"""
        # 模拟响应
        from kwaixiaodian.models.customer_service import (
            DispatchingMappingCommodityAddResponse,
        )

        mock_response = DispatchingMappingCommodityAddResponse()
        mock_async_client.execute.return_value = mock_response

        # 调用方法
        result = await async_cs_service.add_commodity_mapping(
            access_token="test_token", commodity_id=123456, group_id=789
        )

        # 验证结果
        assert result == mock_response
        mock_async_client.execute.assert_called_once()


class TestSyncCustomerServiceService:
    """测试同步客服服务"""

    def test_send_intelligent_message(self, sync_cs_service, mock_sync_client):
        """测试发送智能消息 (同步)"""
        # 模拟响应
        mock_response = IntelligentMessageSendResponse()
        mock_sync_client.execute.return_value = mock_response

        # 准备测试数据
        to_user = CsUser(nick_name="customer1", role=1)
        message_list = [
            MessageContent(content_type=1, content="您好，有什么可以帮助您的？")
        ]

        # 调用方法
        result = sync_cs_service.send_intelligent_message(
            access_token="test_token", to_user=to_user, message_list=message_list
        )

        # 验证结果
        assert result == mock_response
        mock_sync_client.execute.assert_called_once()

    def test_add_dispatch_group(self, sync_cs_service, mock_sync_client):
        """测试添加客服分组 (同步)"""
        # 模拟响应
        mock_response = DispatchingGroupAddResponse(data=CsGroupInfo(group_id=12345))
        mock_sync_client.execute.return_value = mock_response

        # 调用方法
        result = sync_cs_service.add_dispatch_group(
            access_token="test_token", group_name="VIP客服组"
        )

        # 验证结果
        assert result == mock_response
        mock_sync_client.execute.assert_called_once()


class TestCustomerServiceModels:
    """测试客服服务数据模型"""

    def test_cs_user_model(self):
        """测试CsUser模型"""
        user = CsUser(nick_name="test_user", role=1)
        assert user.nick_name == "test_user"
        assert user.role == 1

    def test_message_content_model(self):
        """测试MessageContent模型"""
        message = MessageContent(content_type=1, content="测试消息内容")
        assert message.content_type == 1
        assert message.content == "测试消息内容"

    def test_intelligent_message_send_request(self):
        """测试智能消息发送请求模型"""
        request = IntelligentMessageSendRequest(
            access_token="test_token",
            to_user=CsUser(nick_name="customer", role=1),
            message_list=[MessageContent(content_type=1, content="Hello")],
        )

        assert request.api_method == "open.cs.intelligent.message.send"
        assert request.access_token == "test_token"
        assert request.to_user.nick_name == "customer"
        assert len(request.message_list) == 1

    def test_dispatching_group_add_request(self):
        """测试添加分组请求模型"""
        request = DispatchingGroupAddRequest(
            access_token="test_token", group_name="测试分组"
        )

        assert request.api_method == "open.cs.dispatching.group.add"
        assert request.access_token == "test_token"
        assert request.group_name == "测试分组"

    def test_cs_group_info_model(self):
        """测试客服分组信息模型"""
        group_info = CsGroupInfo(group_id=12345)
        assert group_info.group_id == 12345
