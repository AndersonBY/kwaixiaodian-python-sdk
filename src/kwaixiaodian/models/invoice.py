"""发票管理相关数据模型（严格对齐 Java 参考）

仅保留 Java SDK 中存在的发票相关端点：
- open.invoice.subsidy.audit.info (GET)
- open.invoice.amount.get (GET)
"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod


class InvoiceSubsidyAuditInfoRequest(BaseRequest):
    """补贴发票审核信息请求

    API: open.invoice.subsidy.audit.info (GET)
    Java: OpenInvoiceSubsidyAuditInfoRequest
    """

    oid: str = Field(description="订单ID", alias="oid")

    @property
    def api_method(self) -> str:
        return "open.invoice.subsidy.audit.info"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SubsidyInvoiceInfo(BaseModel):
    """补贴发票审核信息（字段对齐 Java）"""

    oid: Optional[str] = Field(default=None, description="订单ID")
    amount: Optional[str] = Field(default=None, description="订单金额")
    subSidyAmount: Optional[str] = Field(default=None, description="补贴金额")
    userPayAmount: Optional[str] = Field(default=None, description="用户实付金额")
    city: Optional[str] = Field(default=None, description="城市")
    barCode: Optional[str] = Field(default=None, description="条形码")
    channelSeqNo: Optional[str] = Field(default=None, description="渠道流水号")
    openInvoiceSubjectProto: Optional[Dict[str, Any]] = Field(
        default=None, description="发票抬头主体信息"
    )


class InvoiceSubsidyAuditInfoResponse(BaseResponse[SubsidyInvoiceInfo]):
    """补贴发票审核信息响应"""

    pass


class InvoiceAmountGetRequest(BaseRequest):
    """发票可开金额查询请求

    API: open.invoice.amount.get (GET)
    Java: OpenInvoiceAmountGetRequest
    """

    from_type: str = Field(description="来源类型", alias="fromType")
    to_type: str = Field(description="目标类型", alias="toType")
    to_id: Optional[int] = Field(default=None, description="目标ID", alias="toId")
    order_id: Optional[int] = Field(default=None, description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:
        return "open.invoice.amount.get"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class QueryInvoiceAmountData(BaseModel):
    """发票可开金额查询结果（字段对齐 Java）"""

    to_receiver_invoice_amount: Optional[str] = Field(
        default=None, description="对收款方可开金额", alias="toReceiverInvoiceAmount"
    )
    to_buyer_invoice_amount: Optional[str] = Field(
        default=None, description="对购买方可开金额", alias="toBuyerInvoiceAmount"
    )
    to_platform_invoice_amount: Optional[str] = Field(
        default=None, description="对平台可开金额", alias="toPlatformInvoiceAmount"
    )
    query_time: Optional[str] = Field(
        default=None, description="查询时间", alias="queryTime"
    )
    order_invoice_amount_response: Optional[Dict[str, Any]] = Field(
        default=None, description="订单可开金额明细", alias="orderInvoiceAmountResponse"
    )
    refund_invoice_amount_response: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="退款可开金额明细列表",
        alias="refundInvoiceAmountResponse",
    )


class InvoiceAmountGetResponse(BaseResponse[QueryInvoiceAmountData]):
    """发票可开金额查询响应"""

    pass
