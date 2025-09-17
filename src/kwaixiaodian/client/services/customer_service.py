"""客服服务类

基于 Java SDK 参考实现提供完整的客服管理功能。所有方法文档严格对齐
`src/kwaixiaodian/models/customer_service.py` 中请求模型的 `api_method` 与
`http_method`，并标注对应 Java 请求类与源码路径，便于排查与比对。

异常策略
- 当开放平台返回错误码或响应解析失败时，底层会抛出 `KwaixiaodianAPIError`。
"""

from typing import List, Optional

from ...models.customer_service import (
    # 域对象
    CsUser,
    # 分组管理相关
    DispatchingGroupAddRequest,
    DispatchingGroupAddResponse,
    DispatchingGroupDelRequest,
    DispatchingGroupDelResponse,
    DispatchingGroupQueryRequest,
    DispatchingGroupQueryResponse,
    DispatchingGroupUpdateRequest,
    DispatchingGroupUpdateResponse,
    # 商品映射相关
    DispatchingMappingCommodityAddRequest,
    DispatchingMappingCommodityAddResponse,
    DispatchingMappingCommodityDelDefaultRequest,
    DispatchingMappingCommodityDelDefaultResponse,
    DispatchingMappingCommodityDelRequest,
    DispatchingMappingCommodityDelResponse,
    DispatchingMappingCommodityQueryDefaultRequest,
    DispatchingMappingCommodityQueryDefaultResponse,
    DispatchingMappingCommodityQueryRequest,
    DispatchingMappingCommodityQueryResponse,
    IntelligentEvaluationMessageRequest,
    IntelligentEvaluationMessageResponse,
    # 智能消息相关
    IntelligentMessageSendRequest,
    IntelligentMessageSendResponse,
    # 物流会话回调相关
    LogisticsSessionCreateCallbackRequest,
    LogisticsSessionCreateCallbackResponse,
    MessageContent,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncCustomerServiceService:
    """客服服务 - 异步版本

    提供完整的客服管理功能：
    1. 智能消息发送和评估
    2. 客服分组的增删改查
    3. 商品映射配置管理
    4. 物流会话回调处理
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化客服服务

        Args:
            client: 异步基础客户端实例
        """
        self._client = client

    # ==================== 智能消息管理 ====================

    async def send_intelligent_message(
        self,
        access_token: str,
        to_user: Optional[CsUser] = None,
        message_list: Optional[List[MessageContent]] = None,
        transfer_list: Optional[List[CsUser]] = None,
        generator: Optional[int] = None,
        type: Optional[int] = None,
        request_id: Optional[str] = None,
        from_user: Optional[CsUser] = None,
        uid: Optional[int] = None,
    ) -> IntelligentMessageSendResponse:
        """发送AI智能客服消息

        OpenAPI: open.cs.intelligent.message.send (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsIntelligentMessageSendRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsIntelligentMessageSendRequest.java)

        Args:
            access_token: 访问令牌
            to_user: 消息接收用户
            message_list: 消息内容列表
            transfer_list: 转发用户列表
            generator: 生成器
            type: 消息类型
            request_id: 请求ID
            from_user: 消息发送用户
            uid: 用户ID（可选）

        Returns:
            IntelligentMessageSendResponse: 发送消息响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。

        Examples:
            ```python
            response = await cs_service.send_intelligent_message(
                access_token="your_token",
                to_user=CsUser(nick_name="customer1", role=1),
                message_list=[
                    MessageContent(content_type=1, content="您好，有什么可以帮助您的？")
                ]
            )
            ```
        """
        request = IntelligentMessageSendRequest(
            access_token=access_token,
            uid=uid,
            to_user=to_user,
            message_list=message_list,
            transfer_list=transfer_list,
            generator=generator,
            type=type,
            request_id=request_id,
            from_user=from_user,
        )
        return await self._client.execute(request, IntelligentMessageSendResponse)

    async def send_intelligent_evaluation_message(
        self,
        access_token: str,
        to_user_id: str,
        uid: Optional[int] = None,
    ) -> IntelligentEvaluationMessageResponse:
        """发送智能评估消息

        OpenAPI: open.cs.intelligent.evaluation.message (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsIntelligentEvaluationMessageRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsIntelligentEvaluationMessageRequest.java)

        Args:
            access_token: 访问令牌
            to_user_id: 目标用户ID
            uid: 用户ID（可选）

        Returns:
            IntelligentEvaluationMessageResponse: 智能评估消息响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = IntelligentEvaluationMessageRequest(
            access_token=access_token,
            uid=uid,
            to_user_id=to_user_id,
        )
        return await self._client.execute(request, IntelligentEvaluationMessageResponse)

    # ==================== 客服分组管理 ====================

    async def add_dispatch_group(
        self,
        access_token: str,
        group_name: str,
        uid: Optional[int] = None,
    ) -> DispatchingGroupAddResponse:
        """添加客服分组

        OpenAPI: open.cs.dispatching.group.add (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupAddRequest.java)

        Args:
            access_token: 访问令牌
            group_name: 分组名称
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupAddResponse: 添加分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。

        Examples:
            ```python
            response = await cs_service.add_dispatch_group(
                access_token="your_token",
                group_name="VIP客服组"
            )
            print(f"创建的分组ID: {response.data.group_id}")
            ```
        """
        request = DispatchingGroupAddRequest(
            access_token=access_token,
            uid=uid,
            group_name=group_name,
        )
        return await self._client.execute(request, DispatchingGroupAddResponse)

    async def delete_dispatch_group(
        self,
        access_token: str,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingGroupDelResponse:
        """删除客服分组

        OpenAPI: open.cs.dispatching.group.del (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupDelRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupDelRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupDelResponse: 删除分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingGroupDelRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
        )
        return await self._client.execute(request, DispatchingGroupDelResponse)

    async def query_dispatch_group(
        self,
        access_token: str,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingGroupQueryResponse:
        """查询客服分组

        OpenAPI: open.cs.dispatching.group.query (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupQueryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupQueryRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupQueryResponse: 查询分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingGroupQueryRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
        )
        return await self._client.execute(request, DispatchingGroupQueryResponse)

    async def update_dispatch_group(
        self,
        access_token: str,
        group_id: int,
        add_assistant_id: Optional[List[int]] = None,
        del_assistant_id: Optional[List[int]] = None,
        uid: Optional[int] = None,
    ) -> DispatchingGroupUpdateResponse:
        """更新客服分组

        OpenAPI: open.cs.dispatching.group.update (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupUpdateRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            add_assistant_id: 要添加的助手ID列表
            del_assistant_id: 要删除的助手ID列表
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupUpdateResponse: 更新分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingGroupUpdateRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
            add_assistant_id=add_assistant_id,
            del_assistant_id=del_assistant_id,
        )
        return await self._client.execute(request, DispatchingGroupUpdateResponse)

    # ==================== 商品映射管理 ====================

    async def add_commodity_mapping(
        self,
        access_token: str,
        commodity_id: int,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityAddResponse:
        """添加商品映射

        OpenAPI: open.cs.dispatching.mapping.commodity.add (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityAddRequest.java)

        Args:
            access_token: 访问令牌
            commodity_id: 商品ID
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityAddResponse: 添加商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityAddRequest(
            access_token=access_token,
            uid=uid,
            commodity_id=commodity_id,
            group_id=group_id,
        )
        return await self._client.execute(
            request, DispatchingMappingCommodityAddResponse
        )

    async def delete_commodity_mapping(
        self,
        access_token: str,
        commodity_id: int,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityDelResponse:
        """删除商品映射

        OpenAPI: open.cs.dispatching.mapping.commodity.del (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityDelRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityDelRequest.java)

        Args:
            access_token: 访问令牌
            commodity_id: 商品ID
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityDelResponse: 删除商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityDelRequest(
            access_token=access_token,
            uid=uid,
            commodity_id=commodity_id,
            group_id=group_id,
        )
        return await self._client.execute(
            request, DispatchingMappingCommodityDelResponse
        )

    async def delete_default_commodity_mapping(
        self,
        access_token: str,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityDelDefaultResponse:
        """删除默认商品映射

        OpenAPI: open.cs.dispatching.mapping.commodity.del_default (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityDelDefaultRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityDelDefaultRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityDelDefaultResponse: 删除默认商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityDelDefaultRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
        )
        return await self._client.execute(
            request, DispatchingMappingCommodityDelDefaultResponse
        )

    async def query_commodity_mapping(
        self,
        access_token: str,
        commodity_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityQueryResponse:
        """查询商品映射

        OpenAPI: open.cs.dispatching.mapping.commodity.query (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityQueryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityQueryRequest.java)

        Args:
            access_token: 访问令牌
            commodity_id: 商品ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityQueryResponse: 查询商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityQueryRequest(
            access_token=access_token,
            uid=uid,
            commodity_id=commodity_id,
        )
        return await self._client.execute(
            request, DispatchingMappingCommodityQueryResponse
        )

    async def query_default_commodity_mapping(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityQueryDefaultResponse:
        """查询默认商品映射

        OpenAPI: open.cs.dispatching.mapping.commodity.query_default (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityQueryDefaultRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityQueryDefaultRequest.java)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityQueryDefaultResponse: 查询默认商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityQueryDefaultRequest(
            access_token=access_token,
            uid=uid,
        )
        return await self._client.execute(
            request, DispatchingMappingCommodityQueryDefaultResponse
        )

    # ==================== 物流会话回调 ====================

    async def create_logistics_session_callback(
        self,
        access_token: str,
        assistant_id: str,
        ks_session_id: str,
        session_id: str,
        session_type: int,
        uid: Optional[int] = None,
    ) -> LogisticsSessionCreateCallbackResponse:
        """创建物流会话回调

        OpenAPI: open.cs.logistics.session.create.callback (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsLogisticsSessionCreateCallbackRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsLogisticsSessionCreateCallbackRequest.java)

        Args:
            access_token: 访问令牌
            assistant_id: 助手ID
            ks_session_id: 快手会话ID
            session_id: 会话ID
            session_type: 会话类型
            uid: 用户ID（可选）

        Returns:
            LogisticsSessionCreateCallbackResponse: 创建物流会话回调响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = LogisticsSessionCreateCallbackRequest(
            access_token=access_token,
            uid=uid,
            assistant_id=assistant_id,
            ks_session_id=ks_session_id,
            session_id=session_id,
            session_type=session_type,
        )
        return await self._client.execute(
            request, LogisticsSessionCreateCallbackResponse
        )


class SyncCustomerServiceService:
    """客服服务 - 同步版本

    提供完整的客服管理功能的同步接口版本。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化同步客服服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    # ==================== 智能消息管理 ====================

    def send_intelligent_message(
        self,
        access_token: str,
        to_user: Optional[CsUser] = None,
        message_list: Optional[List[MessageContent]] = None,
        transfer_list: Optional[List[CsUser]] = None,
        generator: Optional[int] = None,
        type: Optional[int] = None,
        request_id: Optional[str] = None,
        from_user: Optional[CsUser] = None,
        uid: Optional[int] = None,
    ) -> IntelligentMessageSendResponse:
        """发送AI智能客服消息 (同步)

        OpenAPI: open.cs.intelligent.message.send (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsIntelligentMessageSendRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsIntelligentMessageSendRequest.java)

        Args:
            access_token: 访问令牌
            to_user: 消息接收用户
            message_list: 消息内容列表
            transfer_list: 转发用户列表
            generator: 生成器
            type: 消息类型
            request_id: 请求ID
            from_user: 消息发送用户
            uid: 用户ID（可选）

        Returns:
            IntelligentMessageSendResponse: 发送消息响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。

        Examples:
            ```python
            response = cs_service.send_intelligent_message(
                access_token="your_token",
                to_user=CsUser(nick_name="customer1", role=1),
                message_list=[
                    MessageContent(content_type=1, content="您好，有什么可以帮助您的？")
                ]
            )
            ```
        """
        request = IntelligentMessageSendRequest(
            access_token=access_token,
            uid=uid,
            to_user=to_user,
            message_list=message_list,
            transfer_list=transfer_list,
            generator=generator,
            type=type,
            request_id=request_id,
            from_user=from_user,
        )
        return self._client.execute(request, IntelligentMessageSendResponse)

    def send_intelligent_evaluation_message(
        self,
        access_token: str,
        to_user_id: str,
        uid: Optional[int] = None,
    ) -> IntelligentEvaluationMessageResponse:
        """发送智能评估消息 (同步)

        OpenAPI: open.cs.intelligent.evaluation.message (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsIntelligentEvaluationMessageRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsIntelligentEvaluationMessageRequest.java)

        Args:
            access_token: 访问令牌
            to_user_id: 目标用户ID
            uid: 用户ID（可选）

        Returns:
            IntelligentEvaluationMessageResponse: 智能评估消息响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = IntelligentEvaluationMessageRequest(
            access_token=access_token,
            uid=uid,
            to_user_id=to_user_id,
        )
        return self._client.execute(request, IntelligentEvaluationMessageResponse)

    # ==================== 客服分组管理 ====================

    def add_dispatch_group(
        self,
        access_token: str,
        group_name: str,
        uid: Optional[int] = None,
    ) -> DispatchingGroupAddResponse:
        """添加客服分组 (同步)

        OpenAPI: open.cs.dispatching.group.add (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupAddRequest.java)

        Args:
            access_token: 访问令牌
            group_name: 分组名称
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupAddResponse: 添加分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。

        Examples:
            ```python
            response = cs_service.add_dispatch_group(
                access_token="your_token",
                group_name="VIP客服组"
            )
            print(f"创建的分组ID: {response.data.group_id}")
            ```
        """
        request = DispatchingGroupAddRequest(
            access_token=access_token,
            uid=uid,
            group_name=group_name,
        )
        return self._client.execute(request, DispatchingGroupAddResponse)

    def delete_dispatch_group(
        self,
        access_token: str,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingGroupDelResponse:
        """删除客服分组 (同步)

        OpenAPI: open.cs.dispatching.group.del (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupDelRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupDelRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupDelResponse: 删除分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingGroupDelRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
        )
        return self._client.execute(request, DispatchingGroupDelResponse)

    def query_dispatch_group(
        self,
        access_token: str,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingGroupQueryResponse:
        """查询客服分组 (同步)

        OpenAPI: open.cs.dispatching.group.query (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupQueryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupQueryRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupQueryResponse: 查询分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingGroupQueryRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
        )
        return self._client.execute(request, DispatchingGroupQueryResponse)

    def update_dispatch_group(
        self,
        access_token: str,
        group_id: int,
        add_assistant_id: Optional[List[int]] = None,
        del_assistant_id: Optional[List[int]] = None,
        uid: Optional[int] = None,
    ) -> DispatchingGroupUpdateResponse:
        """更新客服分组 (同步)

        OpenAPI: open.cs.dispatching.group.update (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingGroupUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingGroupUpdateRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            add_assistant_id: 要添加的助手ID列表
            del_assistant_id: 要删除的助手ID列表
            uid: 用户ID（可选）

        Returns:
            DispatchingGroupUpdateResponse: 更新分组响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingGroupUpdateRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
            add_assistant_id=add_assistant_id,
            del_assistant_id=del_assistant_id,
        )
        return self._client.execute(request, DispatchingGroupUpdateResponse)

    # ==================== 商品映射管理 ====================

    def add_commodity_mapping(
        self,
        access_token: str,
        commodity_id: int,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityAddResponse:
        """添加商品映射 (同步)

        OpenAPI: open.cs.dispatching.mapping.commodity.add (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityAddRequest.java)

        Args:
            access_token: 访问令牌
            commodity_id: 商品ID
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityAddResponse: 添加商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityAddRequest(
            access_token=access_token,
            uid=uid,
            commodity_id=commodity_id,
            group_id=group_id,
        )
        return self._client.execute(request, DispatchingMappingCommodityAddResponse)

    def delete_commodity_mapping(
        self,
        access_token: str,
        commodity_id: int,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityDelResponse:
        """删除商品映射 (同步)

        OpenAPI: open.cs.dispatching.mapping.commodity.del (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityDelRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityDelRequest.java)

        Args:
            access_token: 访问令牌
            commodity_id: 商品ID
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityDelResponse: 删除商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityDelRequest(
            access_token=access_token,
            uid=uid,
            commodity_id=commodity_id,
            group_id=group_id,
        )
        return self._client.execute(request, DispatchingMappingCommodityDelResponse)

    def delete_default_commodity_mapping(
        self,
        access_token: str,
        group_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityDelDefaultResponse:
        """删除默认商品映射 (同步)

        OpenAPI: open.cs.dispatching.mapping.commodity.del_default (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityDelDefaultRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityDelDefaultRequest.java)

        Args:
            access_token: 访问令牌
            group_id: 分组ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityDelDefaultResponse: 删除默认商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityDelDefaultRequest(
            access_token=access_token,
            uid=uid,
            group_id=group_id,
        )
        return self._client.execute(
            request, DispatchingMappingCommodityDelDefaultResponse
        )

    def query_commodity_mapping(
        self,
        access_token: str,
        commodity_id: int,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityQueryResponse:
        """查询商品映射 (同步)

        OpenAPI: open.cs.dispatching.mapping.commodity.query (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityQueryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityQueryRequest.java)

        Args:
            access_token: 访问令牌
            commodity_id: 商品ID
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityQueryResponse: 查询商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityQueryRequest(
            access_token=access_token,
            uid=uid,
            commodity_id=commodity_id,
        )
        return self._client.execute(request, DispatchingMappingCommodityQueryResponse)

    def query_default_commodity_mapping(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> DispatchingMappingCommodityQueryDefaultResponse:
        """查询默认商品映射 (同步)

        OpenAPI: open.cs.dispatching.mapping.commodity.query_default (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsDispatchingMappingCommodityQueryDefaultRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsDispatchingMappingCommodityQueryDefaultRequest.java)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选）

        Returns:
            DispatchingMappingCommodityQueryDefaultResponse: 查询默认商品映射响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = DispatchingMappingCommodityQueryDefaultRequest(
            access_token=access_token,
            uid=uid,
        )
        return self._client.execute(
            request, DispatchingMappingCommodityQueryDefaultResponse
        )

    # ==================== 物流会话回调 ====================

    def create_logistics_session_callback(
        self,
        access_token: str,
        assistant_id: str,
        ks_session_id: str,
        session_id: str,
        session_type: int,
        uid: Optional[int] = None,
    ) -> LogisticsSessionCreateCallbackResponse:
        """创建物流会话回调 (同步)

        OpenAPI: open.cs.logistics.session.create.callback (POST)
        Java: com.kuaishou.merchant.open.api.request.cs.OpenCsLogisticsSessionCreateCallbackRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/cs/OpenCsLogisticsSessionCreateCallbackRequest.java)

        Args:
            access_token: 访问令牌
            assistant_id: 助手ID
            ks_session_id: 快手会话ID
            session_id: 会话ID
            session_type: 会话类型
            uid: 用户ID（可选）

        Returns:
            LogisticsSessionCreateCallbackResponse: 创建物流会话回调响应

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = LogisticsSessionCreateCallbackRequest(
            access_token=access_token,
            uid=uid,
            assistant_id=assistant_id,
            ks_session_id=ks_session_id,
            session_id=session_id,
            session_type=session_type,
        )
        return self._client.execute(request, LogisticsSessionCreateCallbackResponse)
