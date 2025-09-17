"""分销基础数据模型（按 Java 参考严格对齐）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from ..base import BaseModel, BaseRequest, BaseResponse, HttpMethod


class Distributor(BaseModel):
    """分销商信息"""

    distributor_id: str = Field(description="分销商ID")
    user_id: str = Field(description="用户ID")
    nickname: str = Field(description="昵称")
    avatar: Optional[str] = Field(default=None, description="头像")
    level: int = Field(description="分销等级")
    status: int = Field(description="状态：1-正常，2-禁用")
    apply_time: str = Field(description="申请时间")
    approve_time: Optional[str] = Field(default=None, description="审核通过时间")
    total_commission: int = Field(description="累计佣金（分）")
    available_commission: int = Field(description="可用佣金（分）")

    @property
    def total_commission_yuan(self) -> float:
        """累计佣金（元）"""
        return self.total_commission / 100

    @property
    def available_commission_yuan(self) -> float:
        """可用佣金（元）"""
        return self.available_commission / 100


class DistributionProduct(BaseModel):
    """分销商品信息"""

    product_id: str = Field(description="商品ID")
    title: str = Field(description="商品标题")
    image: Optional[str] = Field(default=None, description="商品主图")
    price: int = Field(description="商品价格（分）")
    commission_rate: float = Field(description="佣金比例")
    commission_amount: int = Field(description="佣金金额（分）")
    category_id: Optional[str] = Field(default=None, description="分类ID")
    status: int = Field(description="商品状态")

    @property
    def price_yuan(self) -> float:
        """商品价格（元）"""
        return self.price / 100

    @property
    def commission_yuan(self) -> float:
        """佣金金额（元）"""
        return self.commission_amount / 100


class DistributionOrder(BaseModel):
    """分销订单信息"""

    order_id: str = Field(description="订单ID")
    distributor_id: str = Field(description="分销商ID")
    product_id: str = Field(description="商品ID")
    buyer_id: str = Field(description="买家ID")
    quantity: int = Field(description="数量")
    order_amount: int = Field(description="订单金额（分）")
    commission_amount: int = Field(description="佣金金额（分）")
    status: int = Field(description="订单状态")
    create_time: str = Field(description="创建时间")
    settle_time: Optional[str] = Field(default=None, description="结算时间")

    @property
    def order_yuan(self) -> float:
        """订单金额（元）"""
        return self.order_amount / 100

    @property
    def commission_yuan(self) -> float:
        """佣金金额（元）"""
        return self.commission_amount / 100


# ==================== 通用分销功能API ====================


class DistributionSelectionOfflineRequest(BaseRequest):
    """分销精选下线请求"""

    # Based on Java SDK: OpenDistributionSelectionOfflineRequest

    selection_id: int = Field(description="精选ID", alias="selectionId")

    @property
    def api_method(self) -> str:
        return "open.distribution.selection.offline"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DistributionSelectionOfflineResponse(BaseResponse[Dict[str, Any]]):
    """分销精选下线响应"""

    pass


class DistributionSelectionPickRequest(BaseRequest):
    """分销精选选品请求"""

    # Based on Java SDK: OpenDistributionSelectionPickRequest

    item_ids: List[int] = Field(description="商品ID列表", alias="itemIds")
    selection_id: int = Field(description="精选ID", alias="selectionId")

    @property
    def api_method(self) -> str:
        return "open.distribution.selection.pick"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DistributionSelectionPickResponse(BaseResponse[Dict[str, Any]]):
    """分销精选选品响应"""

    pass


class DistributionActivityItemShareCreateRequest(BaseRequest):
    """分销活动商品分享创建请求"""

    # Based on Java SDK: OpenDistributionActivityItemShareCreateRequest

    activity_id: int = Field(description="活动ID", alias="activityId")
    item_id: int = Field(description="商品ID", alias="itemId")
    share_title: str = Field(description="分享标题", alias="shareTitle")
    share_desc: Optional[str] = Field(
        default=None, description="分享描述", alias="shareDesc"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.activity.item.share.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DistributionActivityItemShareCreateResponse(BaseResponse[Dict[str, Any]]):
    """分销活动商品分享创建响应"""

    pass


class DistributionDistributorOrderListRequest(BaseRequest):
    """分销商订单列表请求"""

    # Based on Java SDK: OpenDistributionDistributorOrderListRequest

    distributor_id: int = Field(description="分销商ID", alias="distributorId")
    begin_time: Optional[int] = Field(
        default=None, description="开始时间", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    order_status: Optional[int] = Field(
        default=None, description="订单状态", alias="orderStatus"
    )
    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.distributor.order.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributionDistributorOrderListResponse(BaseResponse[Dict[str, Any]]):
    """分销商订单列表响应"""

    pass


class DistributionPublicCategoryListRequest(BaseRequest):
    """分销公开分类列表请求"""

    # Based on Java SDK: OpenDistributionPublicCategoryListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.public.category.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributionPublicCategoryListResponse(BaseResponse[Dict[str, Any]]):
    """分销公开分类列表响应"""

    pass


class DistributionSellerSampleRuleSaveRequest(BaseRequest):
    """分销卖家样本规则保存请求"""

    # Based on Java SDK: OpenDistributionSellerSampleRuleSaveRequest

    rule_config: Dict[str, Any] = Field(description="规则配置", alias="ruleConfig")
    rule_name: str = Field(description="规则名称", alias="ruleName")

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.sample.rule.save"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DistributionSellerSampleRuleSaveResponse(BaseResponse[Dict[str, Any]]):
    """分销卖家样本规则保存响应"""

    pass


class DistributionTestRequest(BaseRequest):
    """分销测试请求"""

    # Based on Java SDK: OpenDistributionTestRequest

    test_param: str = Field(description="测试参数", alias="testParam")

    @property
    def api_method(self) -> str:
        return "open.distribution.test"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributionTestResponse(BaseResponse[Dict[str, Any]]):
    """分销测试响应"""

    pass


class ItemSelectionAddUrlRequest(BaseRequest):
    """商品选品添加URL请求"""

    # Based on Java SDK: OpenDistributionItemSelectionAddUrlRequest

    selection_id: int = Field(description="选品ID", alias="selectionId")
    url: str = Field(description="URL地址", alias="url")

    @property
    def api_method(self) -> str:
        return "open.distribution.item.selection.add.url"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemSelectionAddUrlResponse(BaseResponse[Dict[str, Any]]):
    """商品选品添加URL响应"""

    pass


class ItemShelfAddUrlRequest(BaseRequest):
    """商品货架添加URL请求"""

    # Based on Java SDK: OpenDistributionItemShelfAddUrlRequest

    shelf_id: int = Field(description="货架ID", alias="shelfId")
    url: str = Field(description="URL地址", alias="url")

    @property
    def api_method(self) -> str:
        return "open.distribution.item.shelf.add.url"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemShelfAddUrlResponse(BaseResponse[Dict[str, Any]]):
    """商品货架添加URL响应"""

    pass


class QuerySelectionItemDetailRequest(BaseRequest):
    """查询选品商品详情请求"""

    # Based on Java SDK: OpenDistributionQuerySelectionItemDetailRequest

    selection_id: int = Field(description="选品ID", alias="selectionId")
    item_id: int = Field(description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.distribution.query.selection.item.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class QuerySelectionItemDetailResponse(BaseResponse[Dict[str, Any]]):
    """查询选品商品详情响应"""

    pass


class PromoteUpdateRequest(BaseRequest):
    """推广更新请求

    Java: OpenDistributionPromoteUpdateRequest
    Http: POST
    """

    commission_id: List[int] = Field(description="佣金ID列表", alias="commissionId")
    status: int = Field(description="状态", alias="status")

    @property
    def api_method(self) -> str:
        return "open.distribution.promote.update"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromoteUpdateResponse(BaseResponse[Dict[str, Any]]):
    """推广更新响应"""

    pass


class DistributePlanCreateRequest(BaseRequest):
    """分销计划创建请求

    Java: OpenDistributionPlanCreateRequest
    Http: POST
    """

    # Java ParamDTO fields
    plan_create_type: Optional[str] = Field(
        default=None, description="计划创建类型", alias="planCreateType"
    )
    normal_plan_param: Optional[Dict[str, Any]] = Field(
        default=None, description="普通计划参数", alias="normalPlanParam"
    )
    exclusive_plan_param: Optional[Dict[str, Any]] = Field(
        default=None, description="独家计划参数", alias="exclusivePlanParam"
    )
    orientation_plan_param: Optional[Dict[str, Any]] = Field(
        default=None, description="定向计划参数", alias="orientationPlanParam"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.plan.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DistributePlanCreateResponse(BaseResponse[Dict[str, Any]]):
    """分销计划创建响应"""

    pass


class DistributePlanUpdateRequest(BaseRequest):
    """分销计划更新请求

    Java: OpenDistributionPlanUpdateRequest
    Http: POST
    """

    # Java ParamDTO fields
    plan_id: Optional[int] = Field(default=None, description="计划ID", alias="planId")
    update_type: Optional[str] = Field(
        default=None, description="更新类型", alias="updateType"
    )
    update_plan_status_param: Optional[Dict[str, Any]] = Field(
        default=None, description="更新计划状态参数", alias="updatePlanStatusParam"
    )
    update_normal_commission_param: Optional[Dict[str, Any]] = Field(
        default=None,
        description="更新普通佣金参数",
        alias="updateNormalCommissionParam",
    )
    update_orientation_commission_param: Optional[Dict[str, Any]] = Field(
        default=None,
        description="更新定向佣金参数",
        alias="updateOrientationCommissionParam",
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.plan.update"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class DistributePlanUpdateResponse(BaseResponse[Dict[str, Any]]):
    """分销计划更新响应"""

    pass


class DistributionPlanAddPromoterRequest(BaseRequest):
    """分销计划添加推广者请求"""

    # Based on Java SDK: OpenDistributionDistributionPlanAddPromoterRequest

    plan_id: int = Field(description="计划ID", alias="planId")
    promoter_ids: List[int] = Field(description="推广者ID列表", alias="promoterIds")

    @property
    def api_method(self) -> str:
        return "open.distribution.distribution.plan.add.promoter"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributionPlanAddPromoterResponse(BaseResponse[Dict[str, Any]]):
    """分销计划添加推广者响应"""

    pass


class DistributionPlanDeletePromoterRequest(BaseRequest):
    """分销计划删除推广者请求"""

    # Based on Java SDK: OpenDistributionDistributionPlanDeletePromoterRequest

    plan_id: int = Field(description="计划ID", alias="planId")
    promoter_ids: List[int] = Field(description="推广者ID列表", alias="promoterIds")

    @property
    def api_method(self) -> str:
        return "open.distribution.distribution.plan.delete.promoter"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributionPlanDeletePromoterResponse(BaseResponse[Dict[str, Any]]):
    """分销计划删除推广者响应"""

    pass


class PlanCommissionQueryRequest(BaseRequest):
    """分销计划佣金查询请求

    Java: OpenDistributionPlanCommissionQueryRequest
    Http: GET
    """

    plan_id: int = Field(description="计划ID", alias="planId")
    pcursor: Optional[str] = Field(default=None, description="游标", alias="pcursor")

    @property
    def api_method(self) -> str:
        return "open.distribution.plan.commission.query"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PlanCommissionQueryResponse(BaseResponse[Dict[str, Any]]):
    """分销计划佣金查询响应"""

    pass


class PlanQueryRequest(BaseRequest):
    """分销计划查询请求

    Java: OpenDistributionPlanQueryRequest
    Http: GET
    """

    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.distribution.plan.query"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PlanQueryResponse(BaseResponse[Dict[str, Any]]):
    """分销计划查询响应"""

    pass


class SelectionListRequest(BaseRequest):
    """精选列表请求"""

    # Based on Java SDK: OpenDistributionSelectionListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.selection.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SelectionListResponse(BaseResponse[Dict[str, Any]]):
    """精选列表响应"""

    pass


class KwaimoneyLiveItemListRequest(BaseRequest):
    """快手币直播商品列表请求"""

    # Based on Java SDK: OpenDistributionKwaimoneyLiveItemListRequest

    live_id: str = Field(description="直播ID", alias="liveId")
    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.kwaimoney.live.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyLiveItemListResponse(BaseResponse[Dict[str, Any]]):
    """快手币直播商品列表响应"""

    pass
