"""Promotion domain models (aligned with Java reference)

Java packages:
- com.kuaishou.merchant.open.api.request.promotion
- com.kuaishou.merchant.open.api.request (KsMerchantPromotionDetailRequest)

Families:
- coupon.*
- crowd.*
- open.promotion.seller.statistic (GET)
- open.promotion.shop.newbie.create (POST)
- open.promotion.order.detail (GET, deprecated in Java but present)
"""

from typing import ClassVar, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# -------------------- Domain models --------------------


class TagCondition(BaseModel):
    start_time: Optional[str] = Field(None, alias="startTime")
    tag_name: Optional[str] = Field(None, alias="tagName")
    condition_operator: Optional[str] = Field(None, alias="conditionOperator")
    end_time: Optional[str] = Field(None, alias="endTime")
    value: Optional[List[str]] = Field(None, alias="value")


# -------------------- Params --------------------


class PromotionCouponCreateParam(BaseModel):
    valid_start_time: Optional[int] = Field(None, alias="validStartTime")
    outer_unique_key: Optional[str] = Field(None, alias="outerUniqueKey")
    item_ids: Optional[List[int]] = Field(None, alias="itemIds")
    fixed_validity_time: Optional[int] = Field(None, alias="fixedValidityTime")
    receive_channel: Optional[str] = Field(None, alias="receiveChannel")
    reduce_amount: Optional[int] = Field(None, alias="reduceAmount")
    receive_start_time: Optional[int] = Field(None, alias="receiveStartTime")
    threshold: Optional[int] = Field(None, alias="threshold")
    coupon_target_type: Optional[int] = Field(None, alias="couponTargetType")
    ext_info: Optional[str] = Field(None, alias="extInfo")
    validity_type: Optional[int] = Field(None, alias="validityType")
    valid_end_time: Optional[int] = Field(None, alias="validEndTime")
    receive_end_time: Optional[int] = Field(None, alias="receiveEndTime")
    name: Optional[str] = Field(None, alias="name")
    total_stock: Optional[int] = Field(None, alias="totalStock")
    receive_per_limit: Optional[int] = Field(None, alias="receivePerLimit")
    coupon_front_type: Optional[int] = Field(None, alias="couponFrontType")


class PromotionCouponIdParam(BaseModel):
    coupon_id: int = Field(..., alias="couponId")


class PromotionCouponIdsParam(BaseModel):
    coupon_id: List[int] = Field(..., alias="couponId")


class PromotionCouponPageListParam(BaseModel):
    coupon_target_type: Optional[int] = Field(None, alias="couponTargetType")
    page_no: Optional[int] = Field(None, alias="pageNo")
    seller_coupon_status: Optional[int] = Field(None, alias="sellerCouponStatus")
    page_size: Optional[int] = Field(None, alias="pageSize")


class PromotionCouponSendParam(BaseModel):
    coupon_config_id: int = Field(..., alias="couponConfigId")
    outer_id: Optional[str] = Field(None, alias="outerId")
    receive_channel: Optional[int] = Field(None, alias="receiveChannel")
    user_open_id: Optional[str] = Field(None, alias="userOpenId")


class PromotionCouponStatisticParam(BaseModel):
    coupon_id: int = Field(..., alias="couponId")
    business_line: Optional[int] = Field(None, alias="businessLine")


class PromotionCouponStockAddParam(BaseModel):
    coupon_id: int = Field(..., alias="couponId")
    increment_num: int = Field(..., alias="incrementNum")


class PromotionCrowdCreateParam(BaseModel):
    crowd_desc: Optional[str] = Field(None, alias="crowdDesc")
    ext_json: Optional[str] = Field(None, alias="extJson")
    crowd_name: Optional[str] = Field(None, alias="crowdName")
    tag_condition: Optional[List[TagCondition]] = Field(None, alias="tagCondition")


class PromotionCrowdDetailParam(BaseModel):
    crowd_id: int = Field(..., alias="crowdId")


class PromotionCrowdEditParam(BaseModel):
    crowd_desc: Optional[str] = Field(None, alias="crowdDesc")
    crowd_name: Optional[str] = Field(None, alias="crowdName")
    crowd_id: int = Field(..., alias="crowdId")


class PromotionCrowdListParam(BaseModel):
    crowd_type: Optional[int] = Field(None, alias="crowdType")
    page_num: Optional[int] = Field(None, alias="pageNum")
    page_size: Optional[int] = Field(None, alias="pageSize")


class PromotionCrowdPredictParam(BaseModel):
    ext_json: Optional[str] = Field(None, alias="extJson")
    tag_condition: Optional[List[TagCondition]] = Field(None, alias="tagCondition")


class PromotionCrowdUpdateParam(BaseModel):
    ext_json: Optional[str] = Field(None, alias="extJson")
    crowd_id: int = Field(..., alias="crowdId")


class PromotionSellerStatisticParam(BaseModel):
    start_time: Optional[int] = Field(None, alias="startTime")
    end_time: Optional[int] = Field(None, alias="endTime")
    business_line: Optional[int] = Field(None, alias="businessLine")
    coupon_target: Optional[int] = Field(None, alias="couponTarget")


class PromotionShopNewbieCreateParam(BaseModel):
    coupon_target_type: int = Field(..., alias="couponTargetType")
    item_id: List[int] = Field(..., alias="itemId")
    coupon_price: int = Field(..., alias="couponPrice")
    coupon_end: int = Field(..., alias="couponEnd")
    coupon_front_type: int = Field(..., alias="couponFrontType")
    coupon_base: int = Field(..., alias="couponBase")
    status: Optional[int] = Field(None, alias="status")


class PromotionOrderDetailParam(BaseModel):
    order_id: int = Field(..., alias="orderId")


# -------------------- Requests --------------------


class PromotionCouponCreateRequest(BaseRequest):
    param: PromotionCouponCreateParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.create"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCouponDeleteRequest(BaseRequest):
    param: PromotionCouponIdParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.delete"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCouponOverRequest(BaseRequest):
    param: PromotionCouponIdParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.over"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCouponPageListRequest(BaseRequest):
    param: PromotionCouponPageListParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.page.list"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PromotionCouponQueryRequest(BaseRequest):
    param: PromotionCouponIdsParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.query"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCouponSendRequest(BaseRequest):
    param: PromotionCouponSendParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.send"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCouponStatisticRequest(BaseRequest):
    param: PromotionCouponStatisticParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.statistic"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PromotionCouponStockAddRequest(BaseRequest):
    param: PromotionCouponStockAddParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.coupon.stock.add"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCrowdCreateRequest(BaseRequest):
    param: PromotionCrowdCreateParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.crowd.create"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCrowdDetailRequest(BaseRequest):
    param: PromotionCrowdDetailParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.crowd.detail"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCrowdEditRequest(BaseRequest):
    param: PromotionCrowdEditParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.crowd.edit"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCrowdListRequest(BaseRequest):
    param: PromotionCrowdListParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.crowd.list"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionCrowdPredictRequest(BaseRequest):
    param: PromotionCrowdPredictParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.crowd.predict"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PromotionCrowdUpdateRequest(BaseRequest):
    param: PromotionCrowdUpdateParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.crowd.update"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionSellerStatisticRequest(BaseRequest):
    param: PromotionSellerStatisticParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.seller.statistic"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PromotionShopNewbieCreateRequest(BaseRequest):
    param: PromotionShopNewbieCreateParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.shop.newbie.create"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PromotionOrderDetailRequest(BaseRequest):
    param: PromotionOrderDetailParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.promotion.order.detail"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


# -------------------- Responses --------------------


class PromotionGenericResponse(BaseResponse[dict]):
    pass
