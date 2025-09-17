"""卖家活动相关数据模型（按 Java 参考严格对齐）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from ..base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== 卖家活动相关 API ====================


class SellerActivityApplyListRequest(BaseRequest):
    """卖家活动申请列表请求

    Java: OpenDistributionSellerActivityApplyListRequest
    Http: GET
    """

    # Java ParamDTO fields
    offset: Optional[int] = Field(default=None, description="偏移量", alias="offset")
    activity_type: Optional[int] = Field(
        default=None, description="活动类型", alias="activityType"
    )
    limit: Optional[int] = Field(default=None, description="限制数量", alias="limit")
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.apply.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityApplyListResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动申请列表响应"""

    pass


class SellerActivityPromotionEffectItemRequest(BaseRequest):
    """卖家活动推广效果商品请求

    Java: OpenDistributionSellerActivityPromotionEffectItemRequest
    Http: GET
    """

    # Java ParamDTO fields
    page_cursor: Optional[int] = Field(
        default=None, description="页游标", alias="pageCursor"
    )
    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    item_title: Optional[str] = Field(
        default=None, description="商品标题", alias="itemTitle"
    )
    page_size: Optional[int] = Field(
        default=None, description="分页大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.promotion.effect.item"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributeCpsInvestItem(BaseModel):
    """Java: DistributeCpsInvestItem（代表性字段）"""

    category_name: Optional[str] = Field(default=None, alias="categoryName")
    category_name_path: Optional[List[str]] = Field(
        default=None, alias="categoryNamePath"
    )
    item_id: Optional[int] = Field(default=None, alias="itemId")
    commission_amount: Optional[int] = Field(default=None, alias="commissionAmount")
    item_price: Optional[int] = Field(default=None, alias="itemPrice")
    pay_order_amount: Optional[int] = Field(default=None, alias="payOrderAmount")
    stock_num: Optional[int] = Field(default=None, alias="stockNum")
    settled_order_num: Optional[int] = Field(default=None, alias="settledOrderNum")
    total_uv: Optional[int] = Field(default=None, alias="totalUv")
    volume: Optional[int] = Field(default=None, alias="volume")
    investment_promotion_rate: Optional[int] = Field(
        default=None, alias="investmentPromotionRate"
    )
    item_price_fen: Optional[int] = Field(default=None, alias="itemPriceFen")
    category_id: Optional[int] = Field(default=None, alias="categoryId")
    pay_order_num: Optional[int] = Field(default=None, alias="payOrderNum")
    settled_tech_service_amount: Optional[int] = Field(
        default=None, alias="settledTechServiceAmount"
    )
    item_img_url: Optional[str] = Field(default=None, alias="itemImgUrl")
    category_id_path: Optional[List[int]] = Field(default=None, alias="categoryIdPath")
    activity_id: Optional[int] = Field(default=None, alias="activityId")
    tech_service_amount: Optional[int] = Field(default=None, alias="techServiceAmount")
    commission_rate: Optional[int] = Field(default=None, alias="commissionRate")
    settled_commission_amount: Optional[int] = Field(
        default=None, alias="settledCommissionAmount"
    )
    item_title: Optional[str] = Field(default=None, alias="itemTitle")
    seller_id: Optional[int] = Field(default=None, alias="sellerId")


class DistributeCpsInvestItemView(BaseModel):
    """Java: DistributeCpsInvestItemView"""

    total: Optional[int] = Field(default=None, alias="total")
    date_time: Optional[str] = Field(default=None, alias="dateTime")
    invest_item: Optional[List[DistributeCpsInvestItem]] = Field(
        default=None, alias="investItem"
    )


class SellerActivityPromotionEffectItemResponse(
    BaseResponse[DistributeCpsInvestItemView]
):
    """卖家活动推广效果商品响应（类型化，Java对齐）"""

    pass


class SellerActivityUsableItemRequest(BaseRequest):
    """卖家活动可用商品请求

    Java: OpenDistributionSellerActivityUsableItemRequest
    Http: GET
    """

    # Java ParamDTO fields
    offset: Optional[int] = Field(default=None, description="偏移量", alias="offset")
    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )
    limit: Optional[int] = Field(default=None, description="数量限制", alias="limit")
    item_title: Optional[str] = Field(
        default=None, description="商品标题", alias="itemTitle"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.usable.item"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityUsableItemResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动可用商品响应"""

    pass


class SellerActivityApplyCancelRequest(BaseRequest):
    """卖家活动申请取消请求

    Java: OpenDistributionSellerActivityApplyCancelRequest
    Http: GET
    """

    # Java ParamDTO fields
    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.apply.cancel"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityApplyCancelResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动申请取消响应"""

    pass


class SellerActivityOpenInfoRequest(BaseRequest):
    """卖家活动开放信息请求

    Java: OpenDistributionSellerActivityOpenInfoRequest
    Http: GET
    """

    # Java ParamDTO fields
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.open.info"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityOpenInfoResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动开放信息响应"""

    pass


class SellerActivityItemListRequest(BaseRequest):
    """卖家活动商品列表请求

    Java: OpenDistributionSellerActivityItemListRequest
    Http: GET
    """

    # Java ParamDTO fields
    item_audit_status: Optional[int] = Field(
        default=None, description="商品审核状态", alias="itemAuditStatus"
    )
    category_id: Optional[int] = Field(
        default=None, description="类目ID", alias="categoryId"
    )
    offset: Optional[int] = Field(default=None, description="偏移量", alias="offset")
    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )
    limit: Optional[int] = Field(default=None, description="数量限制", alias="limit")
    item_title: Optional[str] = Field(
        default=None, description="商品标题", alias="itemTitle"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityItemListResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动商品列表响应"""

    pass


class SellerActivityOpenListRequest(BaseRequest):
    """卖家活动开放列表请求

    Java: OpenDistributionSellerActivityOpenListRequest
    Http: GET
    """

    # Java ParamDTO fields
    offset: Optional[int] = Field(default=None, description="偏移量", alias="offset")
    activity_type: Optional[int] = Field(
        default=None, description="活动类型", alias="activityType"
    )
    limit: Optional[int] = Field(default=None, description="数量限制", alias="limit")
    activity_id: Optional[int] = Field(
        default=None, description="活动ID", alias="activityId"
    )
    channel_id: Optional[List[int]] = Field(
        default=None, description="渠道ID列表", alias="channelId"
    )
    activity_title: Optional[str] = Field(
        default=None, description="活动标题", alias="activityTitle"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.open.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityOpenListResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动开放列表响应"""

    pass


class SellerActivityQueryExclusivePromoterInfoRequest(BaseRequest):
    """卖家活动查询独家推广者信息请求"""

    # Based on Java SDK: OpenDistributionSellerActivityQueryexclusivepromoterinfoRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.queryExclusivePromoterInfo"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityQueryExclusivePromoterInfoResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动查询独家推广者信息响应"""

    pass


class SellerActivityApplyRequest(BaseRequest):
    """卖家活动申请请求"""

    # Based on Java SDK: OpenDistributionSellerActivityApplyRequest

    activity_id: int = Field(description="活动ID", alias="activityId")
    apply_reason: str = Field(description="申请理由", alias="applyReason")

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.apply"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerActivityApplyResponse(BaseResponse[Dict[str, Any]]):
    """卖家活动申请响应"""

    pass


class SellerActivityPromotionEffectSummaryRequest(BaseRequest):
    """卖家活动推广效果汇总请求

    Java: OpenDistributionSellerActivityPromotionEffectSummaryRequest
    Http: GET
    """

    # Java ParamDTO fields
    activity_id: int = Field(description="活动ID", alias="activityId")
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.promotion.effect.summary"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributeCpsInvestBoardSummaryView(BaseModel):
    """Java: DistributeCpsInvestBoardSummaryView"""

    pay_order_num: Optional[int] = Field(default=None, alias="payOrderNum")
    date_time: Optional[str] = Field(default=None, alias="dateTime")
    user_id: Optional[int] = Field(default=None, alias="userId")
    commission_amount: Optional[int] = Field(default=None, alias="commissionAmount")
    settled_tech_service_amount: Optional[int] = Field(
        default=None, alias="settledTechServiceAmount"
    )
    pay_order_amount: Optional[int] = Field(default=None, alias="payOrderAmount")
    settled_order_num: Optional[int] = Field(default=None, alias="settledOrderNum")
    tech_service_amount: Optional[int] = Field(default=None, alias="techServiceAmount")
    total_uv: Optional[int] = Field(default=None, alias="totalUv")
    settled_commission_amount: Optional[int] = Field(
        default=None, alias="settledCommissionAmount"
    )
    promotion_num: Optional[int] = Field(default=None, alias="promotionNum")


class SellerActivityPromotionEffectSummaryResponse(
    BaseResponse[DistributeCpsInvestBoardSummaryView]
):
    """卖家活动推广效果汇总响应（类型化，Java对齐）"""

    pass


class SellerActivityQueryActivityPromoterAdjustHistoryRequest(BaseRequest):
    """卖家活动查询推广者调整历史请求

    Java: OpenDistributionSellerActivityQueryactivitypromoteradjusthistoryRequest
    Http: GET
    """

    # Java ParamDTO fields
    offset: Optional[int] = Field(default=None, description="偏移量", alias="offset")
    activity_id: int = Field(description="活动ID", alias="activityId")
    limit: Optional[int] = Field(default=None, description="数量限制", alias="limit")

    @property
    def api_method(self) -> str:
        return "open.distribution.seller.activity.queryActivityPromoterAdjustHistory"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerActivityQueryActivityPromoterAdjustHistoryResponse(
    BaseResponse[Dict[str, Any]]
):
    """卖家活动查询推广者调整历史响应"""

    pass
