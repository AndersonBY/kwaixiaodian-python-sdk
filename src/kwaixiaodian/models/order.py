"""订单相关数据模型（严格对齐 Java SDK）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field, field_validator

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod
from .common import Address, LogisticsInfo, OrderStatus, UserInfo

# ==================== Java View 映射（Seller 订单 & KS 支付）====================


class MerchantLogisticsInfoView(BaseModel):
    """Java: com.kuaishou.merchant.open.api.response.view.logistics.MerchantLogisticsInfoView

    仅建模已在 Java 中出现的字段名，通过 alias 与 Java 对齐。
    """

    express_no: Optional[str] = Field(default=None, alias="expressNo")
    express_code: Optional[int] = Field(default=None, alias="expressCode")


class MerchantOrderProductInfoView(BaseModel):
    """Java: com.kuaishou.merchant.open.api.response.view.order.MerchantOrderProductInfoView

    精简映射（代表性字段），满足类型化校验与示例需要。
    """

    id: Optional[int] = Field(default=None, alias="id")
    oid: Optional[int] = Field(default=None, alias="oid")
    buyer_id: Optional[int] = Field(default=None, alias="buyerId")
    sku_id: Optional[int] = Field(default=None, alias="skuId")
    rel_sku_id: Optional[int] = Field(default=None, alias="relSkuId")
    sku_desc: Optional[str] = Field(default=None, alias="skuDesc")
    sku_nick: Optional[str] = Field(default=None, alias="skuNick")
    item_id: Optional[int] = Field(default=None, alias="itemId")
    rel_item_id: Optional[int] = Field(default=None, alias="relItemId")
    item_title: Optional[str] = Field(default=None, alias="itemTitle")
    item_link_url: Optional[str] = Field(default=None, alias="itemLinkUrl")
    item_pic_url: Optional[str] = Field(default=None, alias="itemPicUrl")
    num: Optional[int] = Field(default=None, alias="num")
    original_price: Optional[int] = Field(default=None, alias="originalPrice")
    discount_fee: Optional[int] = Field(default=None, alias="discountFee")
    price: Optional[int] = Field(default=None, alias="price")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    update_time: Optional[int] = Field(default=None, alias="updateTime")
    refund_id: Optional[int] = Field(default=None, alias="refundId")
    refund_status: Optional[int] = Field(default=None, alias="refundStatus")
    item_type: Optional[int] = Field(default=None, alias="itemType")

    # 常用金额辅助（分→元）
    @property
    def price_yuan(self) -> Optional[float]:
        return self.price / 100 if self.price is not None else None

    @property
    def original_price_yuan(self) -> Optional[float]:
        return self.original_price / 100 if self.original_price is not None else None

    @property
    def discount_fee_yuan(self) -> Optional[float]:
        return self.discount_fee / 100 if self.discount_fee is not None else None


class MerchantOrderInfoView(BaseModel):
    """Java: com.kuaishou.merchant.open.api.response.view.order.MerchantOrderInfoView

    精简映射（代表性字段），通过 alias 与 Java 对齐。
    """

    pay_time: Optional[int] = Field(default=None, alias="payTime")
    buyer_image: Optional[str] = Field(default=None, alias="buyerImage")
    oid: Optional[int] = Field(default=None, alias="oid")
    buyer_id: Optional[int] = Field(default=None, alias="buyerId")
    buyer_nick: Optional[str] = Field(default=None, alias="buyerNick")
    seller_id: Optional[int] = Field(default=None, alias="sellerId")
    seller_nick: Optional[str] = Field(default=None, alias="sellerNick")
    express_fee: Optional[int] = Field(default=None, alias="expressFee")
    discount_fee: Optional[int] = Field(default=None, alias="discountFee")
    total_fee: Optional[int] = Field(default=None, alias="totalFee")
    status: Optional[int] = Field(default=None, alias="status")
    send_time: Optional[int] = Field(default=None, alias="sendTime")
    refund_time: Optional[int] = Field(default=None, alias="refundTime")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    update_time: Optional[int] = Field(default=None, alias="updateTime")
    num: Optional[int] = Field(default=None, alias="num")
    mobile: Optional[str] = Field(default=None, alias="mobile")
    address: Optional[str] = Field(default=None, alias="address")
    refund: Optional[int] = Field(default=None, alias="refund")
    remark: Optional[str] = Field(default=None, alias="remark")
    seller_note_list: Optional[List[str]] = Field(default=None, alias="sellerNoteList")
    the_day_of_deliver_goods_time: Optional[int] = Field(
        default=None, alias="theDayOfDeliverGoodsTime"
    )
    promise_time_stamp_of_delivery: Optional[int] = Field(
        default=None, alias="promiseTimeStampOfDelivery"
    )
    order_product_info_list: Optional[List[MerchantOrderProductInfoView]] = Field(
        default=None, alias="orderProductInfoList"
    )
    logistics_info: Optional[MerchantLogisticsInfoView] = Field(
        default=None, alias="logisticsInfo"
    )
    activity_type: Optional[int] = Field(default=None, alias="activityType")
    cps_type: Optional[int] = Field(default=None, alias="cpsType")
    pay_type: Optional[int] = Field(default=None, alias="payType")

    # 常用金额辅助（分→元）
    @property
    def total_fee_yuan(self) -> Optional[float]:
        return self.total_fee / 100 if self.total_fee is not None else None

    @property
    def express_fee_yuan(self) -> Optional[float]:
        return self.express_fee / 100 if self.express_fee is not None else None

    @property
    def discount_fee_yuan(self) -> Optional[float]:
        return self.discount_fee / 100 if self.discount_fee is not None else None


class OrderItem(BaseModel):
    """订单商品信息"""

    item_id: int = Field(description="商品ID")
    sku_id: Optional[int] = Field(default=None, description="SKU ID")
    title: str = Field(description="商品标题")
    image: Optional[str] = Field(default=None, description="商品主图")
    quantity: int = Field(description="购买数量", ge=1)
    unit_price: int = Field(description="单价（分）")
    total_price: int = Field(description="总价（分）")
    spec_info: Optional[str] = Field(default=None, description="规格信息")

    @property
    def unit_yuan(self) -> float:
        """单价（元）"""
        return self.unit_price / 100

    @property
    def total_yuan(self) -> float:
        """总价（元）"""
        return self.total_price / 100


class Order(BaseModel):
    """订单信息"""

    order_id: str = Field(description="订单ID")
    order_status: OrderStatus = Field(description="订单状态")
    seller_id: int = Field(description="商家ID")
    buyer_info: Optional[UserInfo] = Field(default=None, description="买家信息")

    # 时间信息
    create_time: str = Field(description="创建时间")
    pay_time: Optional[str] = Field(default=None, description="支付时间")
    deliver_time: Optional[str] = Field(default=None, description="发货时间")
    finish_time: Optional[str] = Field(default=None, description="完成时间")

    # 收货地址
    address: Optional[Address] = Field(default=None, description="收货地址")

    # 物流信息
    logistics_info: Optional[LogisticsInfo] = Field(
        default=None, description="物流信息"
    )

    # 商品信息
    items: List[OrderItem] = Field(default_factory=lambda: [], description="商品列表")

    # 价格信息
    total_amount: int = Field(description="订单总金额（分）")
    pay_amount: int = Field(description="实付金额（分）")
    discount_amount: Optional[int] = Field(default=None, description="优惠金额（分）")
    freight: Optional[int] = Field(default=None, description="运费（分）")

    # 其他信息
    remark: Optional[str] = Field(default=None, description="买家备注")
    seller_remark: Optional[str] = Field(default=None, description="商家备注")

    @property
    def total_yuan(self) -> float:
        """订单总金额（元）"""
        return self.total_amount / 100

    @property
    def pay_yuan(self) -> float:
        """实付金额（元）"""
        return self.pay_amount / 100

    @property
    def is_paid(self) -> bool:
        """是否已支付"""
        # 处理可能的int类型，兼容枚举
        if isinstance(self.order_status, int):
            return self.order_status >= OrderStatus.WAIT_DELIVER.value
        return self.order_status.value >= OrderStatus.WAIT_DELIVER.value

    @property
    def is_delivered(self) -> bool:
        """是否已发货"""
        # 处理可能的int类型，兼容枚举
        if isinstance(self.order_status, int):
            return self.order_status >= OrderStatus.WAIT_RECEIVE.value
        return self.order_status.value >= OrderStatus.WAIT_RECEIVE.value


# ==================== 订单查询相关 ====================


class OrderListRequest(BaseRequest):
    """订单游标列表请求（open.order.cursor.list, GET）"""

    order_view_status: Optional[int] = Field(
        default=None, description="订单查看状态", alias="orderViewStatus"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort: Optional[int] = Field(default=None, description="排序方式", alias="sort")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: int = Field(description="开始时间戳", alias="beginTime")
    end_time: int = Field(description="结束时间戳", alias="endTime")

    @field_validator("begin_time", "end_time", mode="before")
    @classmethod
    def _coerce_time(cls, v):  # type: ignore[no-untyped-def]
        # Accept str like "2024-01-01 00:00:00", pendulum DateTime, or int
        try:
            from ..utils.helpers import format_timestamp

            return int(format_timestamp(v))
        except Exception:
            return v

    cps_type: Optional[int] = Field(
        default=None, description="CPS类型", alias="cpsType"
    )
    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")

    @property
    def api_method(self) -> str:
        return "open.order.cursor.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderListResponse(BaseResponse[List[Order]]):
    """订单列表响应"""

    pcursor: Optional[str] = Field(default=None, description="下一页游标")
    has_more: bool = Field(False, description="是否有更多数据")


class OrderGetRequest(BaseRequest):
    """订单详情查询请求（open.order.detail, GET）"""

    order_id: int = Field(description="订单ID", alias="oid")

    @property
    def api_method(self) -> str:
        return "open.order.detail"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderGetResponse(BaseResponse[Order]):
    """订单详情响应"""

    pass


# ==================== 商家订单（Seller）相关 ====================


class SellerOrderDetailRequest(BaseRequest):
    """商家订单详情（open.seller.order.detail, GET）"""

    order_id: int = Field(description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:  # Java: KsMerchantOrderDetailRequest
        return "open.seller.order.detail"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderDetailResponse(BaseResponse[MerchantOrderInfoView]):
    """商家订单详情响应（对齐 Java MerchantOrderInfoView）"""

    result: Optional[MerchantOrderInfoView] = None


class SellerOrderPcursorListRequest(BaseRequest):
    """商家订单游标列表（open.seller.order.pcursor.list, GET）"""

    type: Optional[int] = Field(default=None, description="类型", alias="type")
    current_page: Optional[int] = Field(
        default=None, description="当前页", alias="currentPage"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort: Optional[int] = Field(default=None, description="排序方式", alias="sort")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: int = Field(description="开始时间戳", alias="beginTime")
    end_time: int = Field(description="结束时间戳", alias="endTime")
    cps_type: Optional[int] = Field(
        default=None, description="CPS类型", alias="cpsType"
    )
    pcursor: Optional[str] = Field(
        default=None, description="游标分页标识", alias="pcursor"
    )

    @field_validator("begin_time", "end_time", mode="before")
    @classmethod
    def _coerce_time(cls, v):  # type: ignore[no-untyped-def]
        try:
            from ..utils.helpers import format_timestamp

            return int(format_timestamp(v))
        except Exception:
            return v

    @property
    def api_method(self) -> str:  # Java: KsMerchantOrderListRequest
        return "open.seller.order.pcursor.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class MerchantOrderListData(BaseModel):
    """Java: KsMerchantOrderListResponse.MerchantOrderListData（字段对齐）"""

    current_page: Optional[int] = Field(default=None, alias="currentPage")
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    total_page: Optional[int] = Field(default=None, alias="totalPage")
    total_size: Optional[int] = Field(default=None, alias="totalSize")
    begin_time: Optional[int] = Field(default=None, alias="beginTime")
    end_time: Optional[int] = Field(default=None, alias="endTime")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")
    order_info_list: Optional[List[MerchantOrderInfoView]] = Field(
        default=None, alias="orderInfoList"
    )


class SellerOrderPcursorListResponse(BaseResponse[MerchantOrderListData]):
    """商家订单游标列表响应（类型化）"""

    pass


# ==================== 订单支付优惠/外部关系 ====================


class QueryOrderKspayPromoDetailRequest(BaseRequest):
    """KS支付订单优惠详情（open.query.order.kspay.promo.detail, GET）"""

    query_source: Optional[str] = Field(
        default=None, description="查询来源", alias="querySource"
    )
    buyer_open_id: Optional[str] = Field(
        default=None, description="买家OpenID", alias="buyerOpenId"
    )
    order_id: Optional[int] = Field(default=None, description="订单ID", alias="orderId")
    seller_open_id: Optional[str] = Field(
        default=None, description="卖家OpenID", alias="sellerOpenId"
    )

    @property
    def api_method(self) -> str:  # Java: OpenQueryOrderKspayPromoDetailRequest
        return "open.query.order.kspay.promo.detail"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderBaseInfo(BaseModel):
    """Java: com.kuaishou.merchant.open.api.domain.kwaishop_pay.OrderBaseInfo"""

    provider_trade_no: Optional[str] = Field(default=None, alias="providerTradeNo")
    pay_channel: Optional[str] = Field(default=None, alias="payChannel")
    all_refund: Optional[bool] = Field(default=None, alias="allRefund")
    actual_pay_fee: Optional[int] = Field(default=None, alias="actualPayFee")

    @property
    def actual_pay_yuan(self) -> Optional[float]:
        if self.actual_pay_fee is None:
            return None
        return self.actual_pay_fee / 100


class OrderKspayPromoDetail(BaseModel):
    """Java: com.kuaishou.merchant.open.api.domain.kwaishop_pay.OrderKspayPromoDetail"""

    other_discount_amount: Optional[int] = Field(
        default=None, alias="otherDiscountAmount"
    )
    government_subsidy_amount: Optional[int] = Field(
        default=None, alias="governmentSubsidyAmount"
    )
    government_subsidy: Optional[bool] = Field(default=None, alias="governmentSubsidy")


class OrderKspayPromoData(BaseModel):
    """Java: com.kuaishou.merchant.open.api.domain.kwaishop_pay.OrderKspayPromoData"""

    order_base_info: Optional[OrderBaseInfo] = Field(
        default=None, alias="orderBaseInfo"
    )
    order_kspay_promo_detail: Optional[OrderKspayPromoDetail] = Field(
        default=None, alias="orderKspayPromoDetail"
    )


class QueryOrderKspayPromoDetailResponse(BaseResponse[OrderKspayPromoData]):
    """KS支付订单优惠详情响应（类型化）"""

    pass


class ExternalOrderRelationRequest(BaseRequest):
    """外部订单关系查询（open.external.order.relation, GET）"""

    order_id: int = Field(description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:  # Java: KsMerchantExternalOrderRelationRequest
        return "open.external.order.relation"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ExternalJdOrderData(BaseModel):
    """Java: KsMerchantExternalJdOrderData（代表性字段）"""

    channel_id: Optional[int] = Field(default=None, alias="channelId")
    pin: Optional[str] = Field(default=None, alias="pin")
    order_id: Optional[int] = Field(default=None, alias="orderId")
    jd_order_id: Optional[str] = Field(default=None, alias="jdOrderId")


class ExternalOrderRelationData(BaseModel):
    """Java: KsMerchantExternalOrderRelationData（仅建模已知字段）"""

    jd_order: Optional[ExternalJdOrderData] = Field(default=None, alias="jdOrder")


class ExternalOrderRelationResponse(BaseResponse[ExternalOrderRelationData]):
    """外部订单关系查询响应（类型化）"""

    pass


# ==================== 订单操作相关 ====================


class OrderShipRequest(BaseRequest):
    """订单发货请求

    对应 Java: OpenSellerOrderGoodsDeliverRequest -> open.seller.order.goods.deliver
    """

    order_id: int = Field(description="订单ID", alias="orderId")
    express_no: str = Field(description="快递单号", alias="expressNo")
    express_code: int = Field(description="快递公司代码", alias="expressCode")
    return_address_id: Optional[int] = Field(
        default=None, description="退货地址ID（可选）", alias="returnAddressId"
    )
    quality_param: Optional[str] = Field(
        default=None, description="质检参数（可选）", alias="qualityParam"
    )
    serial_number_list: Optional[List[str]] = Field(
        default=None, description="序列号列表（可选）", alias="serialNumberList"
    )
    imei_list: Optional[List[str]] = Field(
        default=None, description="IMEI列表（可选）", alias="imeiList"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.goods.deliver"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderShipResponse(BaseResponse[Dict[str, Any]]):
    """订单发货响应"""

    pass


class OrderUpdateRemarkRequest(BaseRequest):
    """新增商家订单备注请求

    对应 Java: OpenSellerOrderNoteAddRequest -> open.seller.order.note.add
    """

    order_id: int = Field(description="订单ID", alias="orderId")
    note: str = Field(description="备注内容", max_length=500, alias="note")
    staff_id: Optional[int] = Field(
        default=None, description="员工ID（可选）", alias="staffId"
    )
    flag: Optional[int] = Field(
        default=None, description="备注标记（可选）", alias="flag"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.note.add"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderUpdateRemarkResponse(BaseResponse[Dict[str, Any]]):
    """更新订单备注响应"""

    pass


# ==================== 订单关闭相关 ====================


class OrderCloseRequest(BaseRequest):
    """订单关闭请求"""

    # Based on Java SDK: OpenSellerOrderCloseRequest
    order_id: int = Field(description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.close"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderCloseResponse(BaseResponse[Dict[str, Any]]):
    """订单关闭响应"""

    pass


# ==================== 地址管理相关 ====================


class OrderAddressUpdateRequest(BaseRequest):
    """订单地址更新请求"""

    # Based on Java SDK: OpenOrderAddressUpdateRequest
    order_id: int = Field(description="订单ID", alias="orderId")
    consignee: str = Field(description="收货人姓名", alias="consignee")
    mobile: str = Field(description="联系电话", alias="mobile")
    province_code: int = Field(description="省份代码", alias="provinceCode")
    province: str = Field(description="省份名称", alias="province")
    city_code: int = Field(description="城市代码", alias="cityCode")
    city: str = Field(description="城市名称", alias="city")
    district_code: int = Field(description="区县代码", alias="districtCode")
    district: str = Field(description="区县名称", alias="district")
    address: str = Field(description="详细地址", alias="address")
    town_code: Optional[int] = Field(
        default=None, description="乡镇代码", alias="townCode"
    )
    town: Optional[str] = Field(default=None, description="乡镇名称", alias="town")
    is_partial_update: Optional[bool] = Field(
        default=False, description="是否部分更新", alias="isPartialUpdate"
    )

    @property
    def api_method(self) -> str:
        return "open.order.address.update"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderAddressUpdateResponse(BaseResponse[Dict[str, Any]]):
    """订单地址更新响应"""

    pass


class OrderAddressAuditRequest(BaseRequest):
    """订单地址审核请求基类"""

    order_id: int = Field(description="订单ID", alias="oid")


class OrderAddressAuditApproveRequest(OrderAddressAuditRequest):
    """订单地址审核通过请求"""

    @property
    def api_method(self) -> str:
        return "open.order.address.audit.approve"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderAddressAuditRejectRequest(OrderAddressAuditRequest):
    """订单地址审核拒绝请求"""

    @property
    def api_method(self) -> str:
        return "open.order.address.audit.reject"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderAddressAuditResponse(BaseResponse[Dict[str, Any]]):
    """订单地址审核响应"""

    pass


# ==================== 物流管理相关 ====================


class OrderLogisticsUpdateRequest(BaseRequest):
    """订单物流更新请求"""

    order_id: int = Field(description="订单ID", alias="orderId")
    express_code: int = Field(description="快递公司编码", alias="expressCode")
    express_no: str = Field(description="运单号", alias="expressNo")
    logistics_id: Optional[int] = Field(
        default=None, description="物流ID", alias="logisticsId"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.logistics.update"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderLogisticsUpdateResponse(BaseResponse[Dict[str, Any]]):
    """订单物流更新响应"""

    pass


class OrderGoodsLogisticsAppendRequest(BaseRequest):
    """追加包裹物流（open.seller.order.goods.logistics.append）"""

    express_code: int = Field(description="快递公司编码", alias="expressCode")
    order_id: int = Field(description="订单ID", alias="oid")
    express_no: str = Field(description="运单号", alias="expressNo")

    @property
    def api_method(self) -> str:
        return "open.seller.order.goods.logistics.append"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderGoodsLogisticsAppendResponse(BaseResponse[Dict[str, Any]]):
    """追加包裹物流响应"""

    pass


class SplitDeliveryGoodsOrderItemDTO(BaseModel):
    """拆分发货订单项信息（Java: SplitDeliveryGoodsOrderItemDTO）"""

    delivery_num: int = Field(description="发货数量", alias="deliveryNum")
    oid: int = Field(description="子订单ID", alias="oid")
    serial_number_list: Optional[List[str]] = Field(
        default=None, description="序列号列表", alias="serialNumberList"
    )
    imei_list: Optional[List[str]] = Field(
        default=None, description="IMEI列表", alias="imeiList"
    )


class SplitDeliveryGoodsPackageItemDTO(BaseModel):
    """拆分发货包裹项（Java: SplitDeliveryGoodsPackageItemDTO）"""

    delivery_goods_info_list: List[SplitDeliveryGoodsOrderItemDTO] = Field(
        description="发货商品信息列表", alias="deliveryGoodsInfoList"
    )
    express_code: int = Field(description="快递公司编码", alias="expressCode")
    express_no: str = Field(description="快递单号", alias="expressNo")


class SplitDeliveryGoodsStatusRequest(BaseModel):
    """拆分发货状态请求（Java: SplitDeliveryGoodsStatusRequest）"""

    oid: int = Field(description="子订单ID", alias="oid")
    confirm_delivery_status: int = Field(
        description="确认发货状态", alias="confirmDeliveryStatus"
    )


class OrderGoodsSplitDeliverRequest(BaseRequest):
    """一单多包裹发货（open.order.goods.split.deliver）"""

    main_order_id: int = Field(description="主订单ID", alias="mainOrderId")
    delivery_item_info_list: List[SplitDeliveryGoodsPackageItemDTO] = Field(
        description="包裹项列表", alias="deliveryItemInfoList"
    )
    delivery_status: List[SplitDeliveryGoodsStatusRequest] = Field(
        description="发货状态列表", alias="deliveryStatus"
    )

    @property
    def api_method(self) -> str:
        return "open.order.goods.split.deliver"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderGoodsSplitDeliverResponse(BaseResponse[Dict[str, Any]]):
    """一单多包裹发货响应"""

    pass


# ==================== 订单查询扩展 ====================


class OrderBuyerOrderListRequest(BaseRequest):
    """买家订单列表（open.order.buyer.order.list, GET）"""

    buyer_open_id: str = Field(description="买家openId", alias="buyerOpenId")
    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    limit: Optional[int] = Field(default=None, description="限制条数", alias="limit")
    order_status: Optional[List[int]] = Field(
        default=None, description="订单状态列表", alias="orderStatus"
    )
    order_source_type: Optional[List[int]] = Field(
        default=None, description="订单来源类型列表", alias="orderSourceType"
    )
    start_time: Optional[int] = Field(
        default=None, description="开始时间戳", alias="startTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间戳", alias="endTime"
    )

    @property
    def api_method(self) -> str:
        return "open.order.buyer.order.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderBuyerOrderListResponse(BaseResponse[Dict[str, Any]]):
    """买家订单列表响应（保持通用结构）"""

    pass


class OrderFeeDetail(BaseModel):
    """订单费用明细"""

    fee_type: str = Field(description="费用类型")
    fee_name: str = Field(description="费用名称")
    amount: int = Field(description="费用金额（分）")
    description: Optional[str] = Field(default=None, description="费用说明")

    @property
    def amount_yuan(self) -> float:
        """费用金额（元）"""
        return self.amount / 100


class OrderFeeDetailRequest(BaseRequest):
    """订单费用明细请求"""

    order_id: int = Field(description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.fee.detail"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderFeeDetailResponse(BaseResponse[List[OrderFeeDetail]]):
    """订单费用明细响应"""

    total_fee: Optional[int] = Field(default=None, description="总费用（分）")

    @property
    def total_fee_yuan(self) -> Optional[float]:
        """总费用（元）"""
        return self.total_fee / 100 if self.total_fee is not None else None


# ==================== SKU更新相关 ====================


class OrderSkuUpdateRequest(BaseRequest):
    """订单SKU更新请求"""

    order_id: int = Field(description="订单ID", alias="orderId")
    item_id: int = Field(description="商品ID", alias="itemId")
    old_sku_id: int = Field(description="原SKU ID", alias="oldSkuId")
    new_sku_id: int = Field(description="新SKU ID", alias="newSkuId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.sku.update"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderSkuUpdateResponse(BaseResponse[Dict[str, Any]]):
    """订单SKU更新响应"""

    pass


# ==================== 令牌验证相关 ====================


class OrderTokenVerifyRequest(BaseRequest):
    """订单令牌验证请求（对齐Java，仅需token）"""

    token: str = Field(description="验证令牌", alias="token")

    @property
    def api_method(self) -> str:
        return "open.seller.order.token.verify"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderTokenVerifyResponse(BaseResponse[Dict[str, Any]]):
    """订单令牌验证响应"""

    is_valid: bool = Field(description="令牌是否有效")
    expire_time: Optional[str] = Field(default=None, description="过期时间")


# ==================== 批量解密相关 ====================


class DecryptBaseMetaInfo(BaseModel):
    """解密基础元信息"""

    data_id: str = Field(description="数据ID", alias="bizId")
    encrypted_data: str = Field(description="加密数据", alias="encryptedData")


class OrderDecryptBatchRequest(BaseRequest):
    """订单批量解密请求"""

    batch_decrypt_list: List[DecryptBaseMetaInfo] = Field(
        description="批量解密列表", alias="batchDecryptList"
    )

    @property
    def api_method(self) -> str:
        return "open.order.decrypt.batch"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderDecryptBatchResponse(BaseResponse[Dict[str, Any]]):
    """订单批量解密响应"""

    decrypt_results: List[Dict[str, Any]] = Field(description="解密结果列表")


# ==================== 批量加密相关 ====================


class EncryptBaseMetaInfo(BaseModel):
    """加密基础元信息"""

    data_id: str = Field(description="数据ID", alias="bizId")
    plain_data: str = Field(description="明文数据", alias="decryptedData")
    data_type: Optional[int] = Field(default=None, description="数据类型", alias="type")


class OrderEncryptBatchRequest(BaseRequest):
    """订单批量加密请求"""

    batch_encrypt_list: List[EncryptBaseMetaInfo] = Field(
        description="批量加密列表", alias="batchEncryptList"
    )

    @property
    def api_method(self) -> str:
        return "open.order.encrypt.batch"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderEncryptBatchResponse(BaseResponse[Dict[str, Any]]):
    """订单批量加密响应"""

    encrypt_results: List[Dict[str, Any]] = Field(description="加密结果列表")


# ==================== 批量脱敏相关 ====================


class DesensitiseBaseMetaInfo(BaseModel):
    """脱敏基础元信息"""

    data_id: str = Field(description="数据ID", alias="bizId")
    sensitive_data: str = Field(description="敏感数据", alias="encryptedData")


class OrderDesensitiseBatchRequest(BaseRequest):
    """订单批量脱敏请求"""

    batch_desensitise_list: List[DesensitiseBaseMetaInfo] = Field(
        description="批量脱敏列表", alias="batchDesensitiseList"
    )

    @property
    def api_method(self) -> str:
        return "open.order.desensitise.batch"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderDesensitiseBatchResponse(BaseResponse[Dict[str, Any]]):
    """订单批量脱敏响应"""

    desensitise_results: List[Dict[str, Any]] = Field(description="脱敏结果列表")


# ==================== KS卖家订单地址更新相关 ====================


class KsSellerOrderAddressUpdateRequest(BaseRequest):
    """KS卖家订单地址更新请求"""

    order_id: int = Field(description="订单ID", alias="orderId")
    consignee: str = Field(description="收货人姓名", alias="consignee")
    mobile: str = Field(description="手机号码", alias="mobile")
    province_code: int = Field(description="省份代码", alias="provinceCode")
    province: str = Field(description="省份名称", alias="province")
    city_code: int = Field(description="城市代码", alias="cityCode")
    city: str = Field(description="城市名称", alias="city")
    district_code: int = Field(description="区域代码", alias="districtCode")
    district: str = Field(description="区域名称", alias="district")
    address: str = Field(description="详细地址", alias="address")

    @property
    def api_method(self) -> str:
        return "open.order.ks.seller.order.address.update"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class KsSellerOrderAddressUpdateResponse(BaseResponse[Dict[str, Any]]):
    """KS卖家订单地址更新响应"""

    success: bool = Field(description="更新是否成功")


# ==================== 批量搜索索引相关 ====================


class IndexParamData(BaseModel):
    """索引参数数据"""

    plain_text: str = Field(description="明文文本", alias="plainText")
    type: int = Field(description="类型")


class OrderSearchIndexBatchRequest(BaseRequest):
    """订单批量搜索索引请求"""

    index_param_list: List[IndexParamData] = Field(
        description="索引参数列表", alias="indexParamList"
    )

    @property
    def api_method(self) -> str:
        return "open.order.search.index.batch"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class OrderSearchIndexBatchResponse(BaseResponse[Dict[str, Any]]):
    """订单批量搜索索引响应"""

    index_results: List[Dict[str, Any]] = Field(description="索引结果列表")


# ==================== 订单标签标记相关 ====================


class OrderTagFlagRequest(BaseRequest):
    """订单标签标记请求"""

    order_view_status: Optional[int] = Field(
        default=None, description="订单查看状态", alias="orderViewStatus"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort: Optional[int] = Field(default=None, description="排序方式", alias="sort")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: Optional[int] = Field(
        default=None, description="开始时间戳", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间戳", alias="endTime"
    )
    cps_type: Optional[int] = Field(
        default=None, description="CPS类型", alias="cpsType"
    )
    cursor: Optional[str] = Field(
        default=None, description="游标，用于分页", alias="cursor"
    )

    @property
    def api_method(self) -> str:
        return "open.order.tag.flag"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderTagFlagResponse(BaseResponse[Dict[str, Any]]):
    """订单标签标记响应"""

    orders: List[Dict[str, Any]] = Field(description="订单列表")
    has_more: bool = Field(description="是否有更多数据")
    next_cursor: Optional[str] = Field(default=None, description="下一页游标")


# ==================== 佣金费率查询相关 ====================


class OrderTakerateInquiryRequest(BaseRequest):
    """订单佣金费率查询请求"""

    order_time: int = Field(description="订单时间戳", alias="orderTime")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="附加参数映射", alias="params"
    )

    @property
    def api_method(self) -> str:
        return "open.order.takerate.inquiry"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderTakerateInquiryResponse(BaseResponse[Dict[str, Any]]):
    """订单佣金费率查询响应"""

    takerate: float = Field(description="佣金费率")
    fee_details: Optional[Dict[str, Any]] = Field(default=None, description="费用详情")


# ==================== 测试加密参数相关 ====================


class OrderListEncryptParamTestRequest(BaseRequest):
    """订单列表加密参数测试请求"""

    order_view_status: Optional[int] = Field(
        default=None, description="订单查看状态", alias="orderViewStatus"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort: Optional[int] = Field(default=None, description="排序方式", alias="sort")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: Optional[int] = Field(
        default=None, description="开始时间戳", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间戳", alias="endTime"
    )
    cps_type: Optional[int] = Field(
        default=None, description="CPS类型", alias="cpsType"
    )
    cursor: Optional[str] = Field(
        default=None, description="游标，用于分页", alias="cursor"
    )

    @property
    def api_method(self) -> str:
        return "open.order.list.encrypt.param.test"

    # 固定使用 GET（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderListEncryptParamTestResponse(BaseResponse[Dict[str, Any]]):
    """订单列表加密参数测试响应"""

    test_results: List[Dict[str, Any]] = Field(description="测试结果列表")
    encryption_valid: bool = Field(description="加密是否有效")
