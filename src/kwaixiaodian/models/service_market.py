"""服务市场相关数据模型（严格对齐 Java 参考）"""

from typing import ClassVar, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== 服务订单列表相关 ====================


class ServiceMarketOrderListParam(BaseModel):
    """服务订单列表查询参数（ParamDTO 对齐）"""

    start_time: Optional[int] = Field(None, description="开始时间戳", alias="startTime")
    end_time: Optional[int] = Field(None, description="结束时间戳", alias="endTime")
    query_type: Optional[int] = Field(None, description="查询类型", alias="queryType")
    status: Optional[int] = Field(None, description="订单状态")
    page_size: Optional[int] = Field(None, description="页面大小", alias="pageSize")
    page_num: Optional[int] = Field(None, description="页面编号", alias="pageNum")
    buyer_open_id: Optional[str] = Field(
        None, description="买家开放ID", alias="buyerOpenId"
    )


class ServiceMarketOrderListRequest(BaseRequest):
    """服务订单列表查询请求
    API: open.service.market.order.list (GET)
    Java: OpenServiceMarketOrderListRequest
    """

    param: ServiceMarketOrderListParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.service.market.order.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ServiceSkuInfo(BaseModel):
    """套餐 SKU 信息（Java: ServiceSkuInfo）"""

    package_name: Optional[str] = Field(None, alias="packageName")
    period: Optional[int] = Field(None, description="时长")
    period_desc: Optional[str] = Field(None, alias="periodDesc")
    num: Optional[int] = Field(None, description="数量")
    unit_price: Optional[int] = Field(None, alias="unitPrice", description="单价（分）")

    @property
    def unit_price_yuan(self) -> Optional[float]:
        return self.unit_price / 100 if self.unit_price is not None else None


class ServiceMarketOrderInfo(BaseModel):
    """服务市场订单信息（Java: ServiceMarketOrderInfo）"""

    oid: Optional[int] = Field(None, description="订单ID")
    status: Optional[int] = Field(None, description="订单状态")
    submit_time: Optional[int] = Field(None, alias="submitTime")
    pay_time: Optional[int] = Field(None, alias="payTime")
    buyer_open_id: Optional[str] = Field(None, alias="buyerOpenId")
    buyer_shop_name: Optional[str] = Field(None, alias="buyerShopName")
    buyer_mobile: Optional[str] = Field(None, alias="buyerMobile")
    service_id: Optional[int] = Field(None, alias="serviceId")
    service_name: Optional[str] = Field(None, alias="serviceName")
    service_link_url: Optional[str] = Field(None, alias="serviceLinkUrl")
    service_pic_url: Optional[str] = Field(None, alias="servicePicUrl")
    sku_id: Optional[int] = Field(None, alias="skuId")
    package_mode: Optional[str] = Field(None, alias="packageMode")
    sku_info: Optional[ServiceSkuInfo] = Field(None, alias="skuInfo")
    trial_version: Optional[bool] = Field(None, alias="trialVersion")
    order_total_fee: Optional[int] = Field(None, alias="orderTotalFee")
    payment_fee: Optional[int] = Field(None, alias="paymentFee")
    app_key: Optional[str] = Field(None, alias="appKey")

    @property
    def order_total_fee_yuan(self) -> Optional[float]:
        return self.order_total_fee / 100 if self.order_total_fee is not None else None

    @property
    def payment_fee_yuan(self) -> Optional[float]:
        return self.payment_fee / 100 if self.payment_fee is not None else None


class ServiceMarketOrderListData(BaseModel):
    """服务订单列表数据（Java: ServiceMarketOrderListData）"""

    page_size: Optional[int] = Field(None, alias="pageSize")
    page_num: Optional[int] = Field(None, alias="pageNum")
    total_count: Optional[int] = Field(None, alias="totalCount")
    order_list: Optional[List[ServiceMarketOrderInfo]] = Field(None, alias="orderList")


class ServiceMarketOrderListResponse(BaseResponse[ServiceMarketOrderListData]):
    """服务订单列表查询响应"""

    pass


# ==================== 服务订单详情相关 ====================


class ServiceMarketOrderDetailParam(BaseModel):
    """服务订单详情查询参数（ParamDTO 对齐）"""

    oid: int = Field(..., description="订单ID")


class ServiceMarketOrderDetailRequest(BaseRequest):
    """服务订单详情查询请求
    API: open.service.market.order.detail (GET)
    Java: OpenServiceMarketOrderDetailRequest
    """

    param: ServiceMarketOrderDetailParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.service.market.order.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ServiceMarketOrderDetailResponse(BaseResponse[ServiceMarketOrderInfo]):
    """服务订单详情查询响应"""

    pass


# ==================== 买家服务信息相关 ====================


class ServiceMarketBuyerServiceInfoParam(BaseModel):
    """买家服务信息查询参数（ParamDTO 对齐）"""

    buyer_open_id: str = Field(..., description="买家开放ID", alias="buyerOpenId")


class ServiceMarketBuyerServiceInfoRequest(BaseRequest):
    """买家服务信息查询请求
    API: open.service.market.buyer.service.info (GET)
    Java: OpenServiceMarketBuyerServiceInfoRequest
    """

    param: ServiceMarketBuyerServiceInfoParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.service.market.buyer.service.info"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class BuyerServiceInfo(BaseModel):
    """买家服务信息（Java: BuyerServiceInfo）"""

    in_service: Optional[bool] = Field(None, alias="inService")
    start_time: Optional[int] = Field(None, alias="startTime")
    authorized: Optional[bool] = Field(None, alias="authorized")
    end_time: Optional[int] = Field(None, alias="endTime")
    package_name: Optional[str] = Field(None, alias="packageName")


class ServiceMarketBuyerServiceInfoResponse(BaseResponse[BuyerServiceInfo]):
    """买家服务信息查询响应"""

    pass
