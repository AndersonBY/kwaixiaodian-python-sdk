"""售后（退款退货）相关数据模型"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod
from .common import LogisticsInfo, RefundStatus, UserInfo


class RefundItem(BaseModel):
    """退款商品信息"""

    item_id: int = Field(description="商品ID")
    sku_id: Optional[int] = Field(default=None, description="SKU ID")
    title: str = Field(description="商品标题")
    image: Optional[str] = Field(default=None, description="商品图片")
    quantity: int = Field(description="退款数量", ge=1)
    unit_price: int = Field(description="单价（分）")
    refund_amount: int = Field(description="退款金额（分）")
    reason: Optional[str] = Field(default=None, description="退款原因")

    @property
    def unit_yuan(self) -> float:
        """单价（元）"""
        return self.unit_price / 100

    @property
    def refund_yuan(self) -> float:
        """退款金额（元）"""
        return self.refund_amount / 100


class RefundOrder(BaseModel):
    """退款单信息"""

    refund_id: str = Field(description="退款单ID")
    order_id: str = Field(description="关联订单ID")
    refund_status: RefundStatus = Field(description="退款状态")
    refund_type: int = Field(description="退款类型：1-仅退款，2-退货退款")

    # 用户信息
    buyer_info: Optional[UserInfo] = Field(default=None, description="买家信息")

    # 时间信息
    create_time: str = Field(description="创建时间")
    agree_time: Optional[str] = Field(default=None, description="商家同意时间")
    return_time: Optional[str] = Field(default=None, description="买家退货时间")
    confirm_time: Optional[str] = Field(default=None, description="商家确认收货时间")
    success_time: Optional[str] = Field(default=None, description="退款成功时间")

    # 退款商品
    items: List[RefundItem] = Field(
        default_factory=lambda: [], description="退款商品列表"
    )

    # 金额信息
    total_refund_amount: int = Field(description="总退款金额（分）")
    actual_refund_amount: int = Field(description="实际退款金额（分）")
    freight_refund: Optional[int] = Field(default=None, description="退款运费（分）")

    # 退货物流信息
    return_logistics: Optional[LogisticsInfo] = Field(
        default=None, description="退货物流信息"
    )

    # 原因和说明
    buyer_reason: Optional[str] = Field(default=None, description="买家退款原因")
    buyer_description: Optional[str] = Field(default=None, description="买家退款说明")
    seller_reason: Optional[str] = Field(default=None, description="商家拒绝原因")

    # 凭证图片
    evidence_images: List[str] = Field(
        default_factory=lambda: [], description="凭证图片列表"
    )

    @property
    def total_refund_yuan(self) -> float:
        """总退款金额（元）"""
        return self.total_refund_amount / 100

    @property
    def actual_refund_yuan(self) -> float:
        """实际退款金额（元）"""
        return self.actual_refund_amount / 100

    @property
    def is_return_required(self) -> bool:
        """是否需要退货"""
        return self.refund_type == 2

    @property
    def is_completed(self) -> bool:
        """退款是否完成"""
        return self.refund_status == RefundStatus.SUCCESS


# ==================== 售后查询相关 ====================


## 列表与详情请使用 SellerOrderRefundPcursorListRequest / SellerOrderRefundDetailRequest（见下）


# ==================== 售后处理相关 ====================


## 注意：以下 open.refund.* 能力以 Java 参考为准，当前 SDK 保留与 Java 对应的卖家审批等接口；
## 未在 Java 参考出现的 open.refund.agree/confirm.receive/negotiate 已移除。


class RefundRejectRequest(BaseRequest):
    """拒绝退款请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    reason_code: Optional[int] = Field(
        default=None, description="拒绝原因编码", alias="reasonCode"
    )
    reject_desc: Optional[str] = Field(
        default=None, description="拒绝说明", alias="rejectDesc"
    )
    reject_images: Optional[List[str]] = Field(
        default=None, description="拒绝凭证图片", alias="rejectImages"
    )
    refund_version: Optional[int] = Field(
        default=None, description="退款版本号", alias="refundVersion"
    )
    edit_handling_way: Optional[int] = Field(
        default=None, description="处理方式", alias="editHandlingWay"
    )
    edit_return_address_id: Optional[int] = Field(
        default=None, description="退货地址ID", alias="editReturnAddressId"
    )

    @property
    def api_method(self) -> str:
        return "open.refund.reject"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class RefundRejectResponse(BaseResponse[Dict[str, Any]]):
    """拒绝退款响应"""

    pass


# ==================== 扩展售后API ====================


class RefundDirectRequest(BaseRequest):
    """直接退款请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    refund_version: int = Field(description="退款版本号", alias="refundVersion")

    @property
    def api_method(self) -> str:
        return "open.refund.direct.refund"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class RefundDirectResponse(BaseResponse[Dict[str, Any]]):
    """直接退款响应"""

    pass


class RefundCommentListRequest(BaseRequest):
    """获取退款评论列表请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.refund.comment.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class RefundCommentListResponse(BaseResponse[List[Dict[str, Any]]]):
    """获取退款评论列表响应"""

    pass


class RefundCommentBasicListRequest(BaseRequest):
    """获取退款基本评论列表请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.refund.comment.basic.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class RefundCommentBasicListResponse(BaseResponse[List[Dict[str, Any]]]):
    """获取退款基本评论列表响应"""

    pass


class RefundRejectReasonRequest(BaseRequest):
    """获取拒绝原因请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.refund.reject.reason"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class RefundRejectReasonResponse(BaseResponse[Dict[str, Any]]):
    """获取拒绝原因响应"""

    pass


class RefundEvidenceAddRequest(BaseRequest):
    """添加退款证据请求"""

    image_data: List[str] = Field(description="证据图片数据列表", alias="imageData")
    refund_id: int = Field(description="退款单ID", alias="refundId")
    content: str = Field(description="证据描述内容", max_length=500, alias="content")

    @property
    def api_method(self) -> str:
        return "open.refund.evidence.add"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class RefundEvidenceAddResponse(BaseResponse[Dict[str, Any]]):
    """添加退款证据响应"""

    pass


class RefundConfirmAndSendRequest(BaseRequest):
    """确认并发送退货请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    express_no: str = Field(description="快递单号", alias="expressNo")
    express_code: int = Field(description="快递公司代码", alias="expressCode")

    @property
    def api_method(self) -> str:
        return "open.refund.confirm.and.send"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class RefundConfirmAndSendResponse(BaseResponse[Dict[str, Any]]):
    """确认并发送退货响应"""

    pass


class RefundSubmitReturnInfoRequest(BaseRequest):
    """提交退货信息请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    express_no: str = Field(description="快递单号", alias="expressNo")
    express_code: int = Field(description="快递公司代码", alias="expressCode")

    @property
    def api_method(self) -> str:
        return "open.refund.submit.returnInfo"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class RefundSubmitReturnInfoResponse(BaseResponse[Dict[str, Any]]):
    """提交退货信息响应"""

    pass


class RefundPageOption(BaseModel):
    """退款分页选项（Java: RefundPageOption）"""

    need_exchange: Optional[bool] = Field(
        default=None, description="是否筛选换货", alias="needExchange"
    )


class SellerOrderRefundPcursorListRequest(BaseRequest):
    """卖家订单退款分页列表请求"""

    begin_time: int = Field(description="开始时间戳", alias="beginTime")
    end_time: int = Field(description="结束时间戳", alias="endTime")
    type: Optional[int] = Field(default=None, description="类型", alias="type")
    page_size: int = Field(20, description="页面大小", ge=1, le=100, alias="pageSize")
    current_page: Optional[int] = Field(
        default=None, description="当前页码", alias="currentPage"
    )
    sort: Optional[int] = Field(default=None, description="排序方式", alias="sort")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    negotiate_status: Optional[int] = Field(
        default=None, description="协商状态", alias="negotiateStatus"
    )
    pcursor: Optional[str] = Field(
        default=None, description="分页游标", alias="pcursor"
    )
    status: Optional[int] = Field(default=None, description="状态", alias="status")
    option: Optional[RefundPageOption] = Field(
        default=None, description="分页选项", alias="option"
    )
    order_id: Optional[int] = Field(default=None, description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.pcursor.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderRefundPcursorListResponse(BaseResponse[Dict[str, Any]]):
    """卖家订单退款分页列表响应（data 为 MerchantRefundListDataView）"""

    pass


class SellerOrderRefundDetailRequest(BaseRequest):
    """卖家订单退款详情请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.detail"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderRefundDetailResponse(BaseResponse[Dict[str, Any]]):
    """卖家订单退款详情响应（data 为 MerchantRefundDetailDataView）"""

    pass


class SellerOrderRefundApproveRequest(BaseRequest):
    """卖家订单退款审批请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    desc: Optional[str] = Field(
        default=None, description="描述", max_length=200, alias="desc"
    )
    refund_amount: int = Field(description="退款金额（分）", gt=0, alias="refundAmount")
    status: int = Field(description="状态", alias="status")
    negotiate_status: Optional[int] = Field(
        default=None, description="协商状态", alias="negotiateStatus"
    )
    refund_handing_way: Optional[int] = Field(
        default=None, description="退款处理方式", alias="refundHandingWay"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.approve"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerOrderRefundApproveResponse(BaseResponse[Dict[str, Any]]):
    """卖家订单退款审批响应"""

    pass


class SellerOrderRefundReturngoodsApproveRequest(BaseRequest):
    """卖家订单退货审批请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    refund_amount: int = Field(description="退款金额（分）", gt=0, alias="refundAmount")
    address_id: int = Field(description="地址ID", alias="addressId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.returngoods.approve"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerOrderRefundReturngoodsApproveResponse(BaseResponse[Dict[str, Any]]):
    """卖家订单退货审批响应"""

    pass


class SellerOrderRefundConfirmReceiptRequest(BaseRequest):
    """卖家订单退款确认收货请求"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    status: int = Field(description="状态", alias="status")
    return_freight_handling_advice: Optional[int] = Field(
        default=None,
        description="退货运费处理建议",
        alias="returnFreightHandlingAdvice",
    )
    return_freight_amount: Optional[int] = Field(
        default=None, description="退货运费金额（分）", alias="returnFreightAmount"
    )
    return_freight_reject_desc: Optional[str] = Field(
        default=None,
        description="退货运费拒绝描述",
        max_length=200,
        alias="returnFreightRejectDesc",
    )
    return_freight_reject_images: Optional[List[str]] = Field(
        default=None,
        description="退货运费拒绝图片列表",
        alias="returnFreightRejectImages",
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.confirm.receipt"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerOrderRefundConfirmReceiptResponse(BaseResponse[Dict[str, Any]]):
    """卖家订单退款确认收货响应"""

    pass


# ==================== 卖家退款其他 API（对齐 Java） ====================


class SellerOrderRefundApplyEntryRequest(BaseRequest):
    """卖家退款申请入口（open.seller.order.refund.apply.entry, POST）"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    desc: str = Field(description="描述", alias="desc")
    pictures: Optional[List[str]] = Field(
        default=None, description="图片列表", alias="pictures"
    )
    status: int = Field(description="状态", alias="status")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.apply.entry"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerOrderRefundApplyEntryResponse(BaseResponse[Dict[str, Any]]):
    """卖家退款申请入口响应"""

    pass


class SellerOrderRefundPostApplyEntryRequest(BaseRequest):
    """卖家退款售后申诉入口（open.seller.order.refund.post.apply.entry, POST）"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    desc: Optional[str] = Field(default=None, description="描述", alias="desc")
    pictures: Optional[List[str]] = Field(
        default=None, description="图片列表", alias="pictures"
    )
    status: int = Field(description="状态", alias="status")
    post_apply_judge_reason: Optional[int] = Field(
        default=None, description="售后判定原因", alias="postApplyJudgeReason"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.post.apply.entry"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerOrderRefundPostApplyEntryResponse(BaseResponse[Dict[str, Any]]):
    """卖家退款售后申诉入口响应"""

    pass


class SellerOrderRefundDisagreeRequest(BaseRequest):
    """卖家不同意退款（open.seller.order.refund.disagree.refund, POST）"""

    refund_id: int = Field(description="退款单ID", alias="refundId")
    seller_disagree_reason: int = Field(
        description="不同意原因", alias="sellerDisagreeReason"
    )
    seller_disagree_desc: Optional[str] = Field(
        default=None, description="不同意说明", alias="sellerDisagreeDesc"
    )
    seller_disagree_images: Optional[List[str]] = Field(
        default=None, description="不同意凭证图", alias="sellerDisagreeImages"
    )
    status: int = Field(description="状态", alias="status")
    negotiate_status: Optional[int] = Field(
        default=None, description="协商状态", alias="negotiateStatus"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.disagree.refund"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SellerOrderRefundDisagreeResponse(BaseResponse[Dict[str, Any]]):
    """卖家不同意退款响应"""

    pass


class SellerOrderRefundEvidenceHistoryRequest(BaseRequest):
    """退款证据历史（open.seller.order.refund.evidence.history, GET）"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.evidence.history"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderRefundEvidenceHistoryResponse(BaseResponse[Dict[str, Any]]):
    """退款证据历史响应"""

    pass


class SellerOrderRefundFeeDetailRequest(BaseRequest):
    """退款费用明细（open.seller.order.refund.fee.detail, GET）"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.fee.detail"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderRefundFeeDetailResponse(BaseResponse[Dict[str, Any]]):
    """退款费用明细响应"""

    pass


class SellerOrderRefundHistoryRequest(BaseRequest):
    """退款历史（open.seller.order.refund.history, GET）"""

    refund_id: int = Field(description="退款单ID", alias="refundId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.refund.history"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderRefundHistoryResponse(BaseResponse[Dict[str, Any]]):
    """退款历史响应"""

    pass
