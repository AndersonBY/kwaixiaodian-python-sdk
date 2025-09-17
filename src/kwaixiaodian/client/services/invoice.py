"""发票管理服务（严格对齐 Java SDK）

仅保留并实现以下端点：
- open.invoice.subsidy.audit.info (GET)
- open.invoice.amount.get (GET)
"""

from typing import Optional

from ...models.invoice import (
    InvoiceAmountGetRequest,
    InvoiceAmountGetResponse,
    InvoiceSubsidyAuditInfoRequest,
    InvoiceSubsidyAuditInfoResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncInvoiceService:
    """异步发票管理服务（对齐 Java SDK 与开放平台）。"""

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def subsidy_audit_info(
        self, access_token: str, oid: str, uid: Optional[int] = None
    ) -> InvoiceSubsidyAuditInfoResponse:
        """查询补贴发票审核信息。

        OpenAPI: `open.invoice.subsidy.audit.info` (GET)
        Java: `com.kuaishou.merchant.open.api.request.invoice.OpenInvoiceSubsidyAuditInfoRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/invoice/OpenInvoiceSubsidyAuditInfoRequest.java)

        Args:
            access_token: 访问令牌
            oid: 订单ID
            uid: 用户ID（可选）

        Returns:
            InvoiceSubsidyAuditInfoResponse: 补贴发票审核信息响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = InvoiceSubsidyAuditInfoRequest(
            access_token=access_token, uid=uid, oid=oid, api_version="1"
        )
        return await self._client.execute(request, InvoiceSubsidyAuditInfoResponse)

    async def amount_get(
        self,
        access_token: str,
        from_type: str,
        to_type: str,
        to_id: Optional[int] = None,
        order_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvoiceAmountGetResponse:
        """查询可开票金额。

        OpenAPI: `open.invoice.amount.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.invoice.OpenInvoiceAmountGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/invoice/OpenInvoiceAmountGetRequest.java)

        Args:
            access_token: 访问令牌
            from_type: 来源类型
            to_type: 目标类型
            to_id: 目标ID（可选）
            order_id: 订单ID（可选）
            uid: 用户ID（可选）

        Returns:
            InvoiceAmountGetResponse: 可开票金额查询响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = InvoiceAmountGetRequest(
            access_token=access_token,
            uid=uid,
            from_type=from_type,
            to_type=to_type,
            to_id=to_id,
            order_id=order_id,
            api_version="1",
        )
        return await self._client.execute(request, InvoiceAmountGetResponse)


class SyncInvoiceService:
    """同步发票管理服务（对齐 Java SDK 与开放平台）。"""

    def __init__(self, client: SyncBaseClient):
        self._client = client

    def subsidy_audit_info(
        self, access_token: str, oid: str, uid: Optional[int] = None
    ) -> InvoiceSubsidyAuditInfoResponse:
        """查询补贴发票审核信息（同步）。

        OpenAPI: `open.invoice.subsidy.audit.info` (GET)
        Java: `com.kuaishou.merchant.open.api.request.invoice.OpenInvoiceSubsidyAuditInfoRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/invoice/OpenInvoiceSubsidyAuditInfoRequest.java)

        Args:
            access_token: 访问令牌
            oid: 订单ID
            uid: 用户ID（可选）

        Returns:
            InvoiceSubsidyAuditInfoResponse: 补贴发票审核信息响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = InvoiceSubsidyAuditInfoRequest(
            access_token=access_token, uid=uid, oid=oid, api_version="1"
        )
        return self._client.execute(request, InvoiceSubsidyAuditInfoResponse)

    def amount_get(
        self,
        access_token: str,
        from_type: str,
        to_type: str,
        to_id: Optional[int] = None,
        order_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvoiceAmountGetResponse:
        """查询可开票金额（同步）。

        OpenAPI: `open.invoice.amount.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.invoice.OpenInvoiceAmountGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/invoice/OpenInvoiceAmountGetRequest.java)

        Args:
            access_token: 访问令牌
            from_type: 来源类型
            to_type: 目标类型
            to_id: 目标ID（可选）
            order_id: 订单ID（可选）
            uid: 用户ID（可选）

        Returns:
            InvoiceAmountGetResponse: 可开票金额查询响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = InvoiceAmountGetRequest(
            access_token=access_token,
            uid=uid,
            from_type=from_type,
            to_type=to_type,
            to_id=to_id,
            order_id=order_id,
            api_version="1",
        )
        return self._client.execute(request, InvoiceAmountGetResponse)
