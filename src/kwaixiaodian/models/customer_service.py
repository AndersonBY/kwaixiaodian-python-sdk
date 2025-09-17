"""客服服务相关模型

基于 Java SDK 参考实现：
- com.kuaishou.merchant.open.api.request.cs.*
- com.kuaishou.merchant.open.api.response.cs.*
- com.kuaishou.merchant.open.api.domain.cs.*
"""

from typing import ClassVar, List, Optional

from pydantic import Field

from .base import BaseRequest, BaseResponse, HttpMethod


# 域对象模型
class CsUser(BaseResponse):
    """客服用户信息"""

    nick_name: Optional[str] = Field(None, description="用户昵称", alias="nickName")
    role: Optional[int] = Field(None, description="用户角色", alias="role")


class HintItem(BaseResponse):
    """提示项目"""

    content_type: Optional[int] = Field(
        None, description="内容类型", alias="contentType"
    )
    content: Optional[str] = Field(None, description="内容", alias="content")


class Hint(BaseResponse):
    """提示信息"""

    hint_item_list: Optional[List[HintItem]] = Field(
        None, description="提示项目列表", alias="hintItemList"
    )


class MessageContent(BaseResponse):
    """消息内容"""

    content_type: Optional[int] = Field(
        None, description="内容类型", alias="contentType"
    )
    content: Optional[str] = Field(None, description="内容", alias="content")
    hints: Optional[List[Hint]] = Field(None, description="提示列表", alias="hints")


class CsGroupInfo(BaseResponse):
    """客服分组信息"""

    group_id: Optional[int] = Field(None, description="分组ID", alias="groupId")


# 智能消息发送
class IntelligentMessageSendRequest(BaseRequest):
    """发送AI智能客服消息请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.intelligent.message.send"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    to_user: Optional[CsUser] = Field(None, description="消息接收用户", alias="toUser")
    message_list: Optional[List[MessageContent]] = Field(
        None, description="消息内容列表", alias="messageList"
    )
    transfer_list: Optional[List[CsUser]] = Field(
        None, description="转发用户列表", alias="transferList"
    )
    generator: Optional[int] = Field(None, description="生成器", alias="generator")
    type: Optional[int] = Field(None, description="消息类型", alias="type")
    request_id: Optional[str] = Field(None, description="请求ID", alias="requestId")
    from_user: Optional[CsUser] = Field(
        None, description="消息发送用户", alias="fromUser"
    )


class IntelligentMessageSendResponse(BaseResponse):
    """发送AI智能客服消息响应"""

    pass


# 智能评估消息
class IntelligentEvaluationMessageRequest(BaseRequest):
    """智能评估消息请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.intelligent.evaluation.message"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    to_user_id: str = Field(..., description="目标用户ID", alias="toUserId")


class IntelligentEvaluationMessageResponse(BaseResponse):
    """智能评估消息响应"""

    pass


# 客服分组管理
class DispatchingGroupAddRequest(BaseRequest):
    """添加客服分组请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.group.add"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    group_name: str = Field(..., description="分组名称", alias="groupName")


class DispatchingGroupAddResponse(BaseResponse):
    """添加客服分组响应"""

    data: Optional[CsGroupInfo] = Field(None, description="分组信息")


class DispatchingGroupDelRequest(BaseRequest):
    """删除客服分组请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.group.del"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    group_id: int = Field(..., description="分组ID", alias="groupId")


class DispatchingGroupDelResponse(BaseResponse):
    """删除客服分组响应"""

    pass


class DispatchingGroupQueryRequest(BaseRequest):
    """查询客服分组请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.group.query"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    group_id: int = Field(..., description="分组ID", alias="groupId")


class DispatchingGroupQueryResponse(BaseResponse):
    """查询客服分组响应"""

    pass


class DispatchingGroupUpdateRequest(BaseRequest):
    """更新客服分组请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.group.update"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    group_id: int = Field(..., description="分组ID", alias="groupId")
    add_assistant_id: Optional[List[int]] = Field(
        None, description="要添加的助手ID列表", alias="addAssistantId"
    )
    del_assistant_id: Optional[List[int]] = Field(
        None, description="要删除的助手ID列表", alias="delAssistantId"
    )


class DispatchingGroupUpdateResponse(BaseResponse):
    """更新客服分组响应"""

    pass


# 商品映射管理
class DispatchingMappingCommodityAddRequest(BaseRequest):
    """添加商品映射请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.mapping.commodity.add"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    commodity_id: int = Field(..., description="商品ID", alias="commodityId")
    group_id: int = Field(..., description="分组ID", alias="groupId")


class DispatchingMappingCommodityAddResponse(BaseResponse):
    """添加商品映射响应"""

    pass


class DispatchingMappingCommodityDelRequest(BaseRequest):
    """删除商品映射请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.mapping.commodity.del"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    commodity_id: int = Field(
        ..., description="商品ID", alias="commodityId"
    )  # 注意：Java中是Integer类型
    group_id: int = Field(..., description="分组ID", alias="groupId")


class DispatchingMappingCommodityDelResponse(BaseResponse):
    """删除商品映射响应"""

    pass


class DispatchingMappingCommodityDelDefaultRequest(BaseRequest):
    """删除默认商品映射请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.mapping.commodity.del_default"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    group_id: int = Field(..., description="分组ID", alias="groupId")


class DispatchingMappingCommodityDelDefaultResponse(BaseResponse):
    """删除默认商品映射响应"""

    pass


class DispatchingMappingCommodityQueryRequest(BaseRequest):
    """查询商品映射请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.mapping.commodity.query"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    commodity_id: int = Field(..., description="商品ID", alias="commodityId")


class DispatchingMappingCommodityQueryResponse(BaseResponse):
    """查询商品映射响应"""

    pass


class DispatchingMappingCommodityQueryDefaultRequest(BaseRequest):
    """查询默认商品映射请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.dispatching.mapping.commodity.query_default"

    # 无参数 - 对应空的ParamDTO

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DispatchingMappingCommodityQueryDefaultResponse(BaseResponse):
    """查询默认商品映射响应"""

    pass


# 物流会话回调
class LogisticsSessionCreateCallbackRequest(BaseRequest):
    """创建物流会话回调请求"""

    @property
    def api_method(self) -> str:
        return "open.cs.logistics.session.create.callback"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    assistant_id: str = Field(..., description="助手ID", alias="assistantId")
    ks_session_id: str = Field(..., description="快手会话ID", alias="ksSessionId")
    session_id: str = Field(..., description="会话ID", alias="sessionId")
    session_type: int = Field(..., description="会话类型", alias="sessionType")


class LogisticsSessionCreateCallbackResponse(BaseResponse):
    """创建物流会话回调响应"""

    pass
