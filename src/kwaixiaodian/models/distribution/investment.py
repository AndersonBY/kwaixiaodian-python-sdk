"""投资活动相关数据模型（按 Java 参考严格对齐）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from ..base import BaseRequest, BaseResponse, HttpMethod

# ==================== 投资活动相关 API ====================


class InvestmentActivityAdjustPromoterRequest(BaseRequest):
    """投资活动调整推广者请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityAdjustactivitypromoterRequest

    promoter_id: List[int] = Field(description="推广者ID列表", alias="promoterId")
    activity_id: int = Field(description="活动ID", alias="activityId")
    operator_type: int = Field(description="操作类型", alias="operatorType")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.adjustActivityPromoter"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class InvestmentActivityAdjustPromoterResponse(BaseResponse[Dict[str, Any]]):
    """投资活动调整推广者响应"""

    pass


class InvestmentSamplePromoterDataRequest(BaseRequest):
    """投资样本推广者数据请求"""

    # Based on Java SDK: OpenDistributionInvestmentSamplePromoterDataRequest

    promoter_id: int = Field(description="推广者ID", alias="promoterId")
    item_id: int = Field(description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.sample.promoter.data"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentSamplePromoterDataResponse(BaseResponse[Dict[str, Any]]):
    """投资样本推广者数据响应"""

    pass


class InvestmentActivityItemTokenCreateRequest(BaseRequest):
    """投资活动商品令牌创建请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityItemTokenCreateRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.item.token.create"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityItemTokenCreateResponse(BaseResponse[Dict[str, Any]]):
    """投资活动商品令牌创建响应"""

    pass


class InvestmentActivityOpenItemAuditRequest(BaseRequest):
    """投资活动开放商品审核请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenItemAuditRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.item.audit"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenItemAuditResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放商品审核响应"""

    pass


class InvestmentActivityOpenDeleteRequest(BaseRequest):
    """投资活动开放删除请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenDeleteRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.delete"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenDeleteResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放删除响应"""

    pass


class InvestmentActivityOpenCreateRequest(BaseRequest):
    """投资活动开放创建请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenCreateRequest

    activity_name: str = Field(description="活动名称", alias="activityName")
    activity_desc: str = Field(description="活动描述", alias="activityDesc")
    begin_time: int = Field(description="开始时间", alias="beginTime")
    end_time: int = Field(description="结束时间", alias="endTime")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class InvestmentActivityOpenCreateResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放创建响应"""

    pass


class InvestmentActivityOpenInfoRequest(BaseRequest):
    """投资活动开放信息请求

    Java: OpenDistributionInvestmentActivityOpenInfoRequest
    Http: GET
    """

    # Java ParamDTO: activityId
    activity_id: int = Field(description="活动ID", alias="activityId")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.info"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenInfoResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放信息响应"""

    pass


class InvestmentActivityOpenListRequest(BaseRequest):
    """投资活动开放列表请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenListRequest

    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    activity_status: Optional[int] = Field(
        default=None, description="活动状态", alias="activityStatus"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenListResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放列表响应"""

    pass


class InvestmentActivityItemDetailRequest(BaseRequest):
    """投资活动商品详情请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityItemDetailRequest

    activity_id: int = Field(description="活动ID", alias="activityId")
    item_id: int = Field(description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.item.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityItemDetailResponse(BaseResponse[Dict[str, Any]]):
    """投资活动商品详情响应"""

    pass


class InvestmentActivityOpenItemListRequest(BaseRequest):
    """投资活动开放商品列表请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenItemListRequest

    activity_id: int = Field(description="活动ID", alias="activityId")
    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenItemListResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放商品列表响应"""

    pass


class InvestmentActivityOpenCloseRequest(BaseRequest):
    """投资活动开放关闭请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenCloseRequest

    activity_id: int = Field(description="活动ID", alias="activityId")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.close"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenCloseResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放关闭响应"""

    pass


class InvestmentActivityOpenPromotionEffectRequest(BaseRequest):
    """投资活动开放推广效果请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityOpenPromotionEffectRequest

    activity_id: int = Field(description="活动ID", alias="activityId")
    begin_time: Optional[int] = Field(
        default=None, description="开始时间", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.open.promotion.effect"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityOpenPromotionEffectResponse(BaseResponse[Dict[str, Any]]):
    """投资活动开放推广效果响应"""

    pass


class InvestmentActivityInvalidItemListRequest(BaseRequest):
    """投资活动无效商品列表请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityInvalidItemListRequest

    activity_id: int = Field(description="活动ID", alias="activityId")
    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.invalid.item.list"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class InvestmentActivityInvalidItemListResponse(BaseResponse[Dict[str, Any]]):
    """投资活动无效商品列表响应"""

    pass


class InvestmentActivityQueryExclusivePromoterInfoRequest(BaseRequest):
    """投资活动查询独家推广者信息请求"""

    # Based on Java SDK: OpenDistributionInvestmentActivityQueryexclusivepromoterinfoRequest

    activity_id: int = Field(description="活动ID", alias="activityId")

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.activity.queryExclusivePromoterInfo"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentActivityQueryExclusivePromoterInfoResponse(
    BaseResponse[Dict[str, Any]]
):
    """投资活动查询独家推广者信息响应"""

    pass


class InvestmentMyCreateActivityListRequest(BaseRequest):
    """投资我的创建活动列表请求"""

    # Based on Java SDK: OpenDistributionInvestmentMyCreateActivityListRequest

    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    activity_status: Optional[int] = Field(
        default=None, description="活动状态", alias="activityStatus"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.investment.my.create.activity.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvestmentMyCreateActivityListResponse(BaseResponse[Dict[str, Any]]):
    """投资我的创建活动列表响应"""

    pass
