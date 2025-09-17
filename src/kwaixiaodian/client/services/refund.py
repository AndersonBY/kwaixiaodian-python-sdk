"""售后服务"""

from typing import List, Optional

from ...models.common import RefundStatus
from ...models.refund import (
    RefundCommentBasicListRequest,
    RefundCommentBasicListResponse,
    RefundCommentListRequest,
    RefundCommentListResponse,
    RefundConfirmAndSendRequest,
    RefundConfirmAndSendResponse,
    RefundDirectRequest,
    RefundDirectResponse,
    RefundEvidenceAddRequest,
    RefundEvidenceAddResponse,
    # use seller order list/detail requests per Java
    RefundPageOption,
    RefundRejectReasonRequest,
    RefundRejectReasonResponse,
    RefundRejectRequest,
    RefundRejectResponse,
    RefundSubmitReturnInfoRequest,
    RefundSubmitReturnInfoResponse,
    SellerOrderRefundApplyEntryRequest,
    SellerOrderRefundApplyEntryResponse,
    SellerOrderRefundApproveRequest,
    SellerOrderRefundApproveResponse,
    SellerOrderRefundConfirmReceiptRequest,
    SellerOrderRefundConfirmReceiptResponse,
    SellerOrderRefundDetailRequest,
    SellerOrderRefundDetailResponse,
    SellerOrderRefundDisagreeRequest,
    SellerOrderRefundDisagreeResponse,
    SellerOrderRefundEvidenceHistoryRequest,
    SellerOrderRefundEvidenceHistoryResponse,
    SellerOrderRefundFeeDetailRequest,
    SellerOrderRefundFeeDetailResponse,
    SellerOrderRefundHistoryRequest,
    SellerOrderRefundHistoryResponse,
    SellerOrderRefundPcursorListRequest,
    SellerOrderRefundPcursorListResponse,
    SellerOrderRefundPostApplyEntryRequest,
    SellerOrderRefundPostApplyEntryResponse,
    SellerOrderRefundReturngoodsApproveRequest,
    SellerOrderRefundReturngoodsApproveResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncRefundService:
    """异步售后服务

    提供退款退货、协商处理、售后状态查询等功能。

    说明
    - OpenAPI 对齐策略：以 `src/kwaixiaodian/models/refund.py` 中请求模型的
      `api_method` 与 `http_method` 为准，并与 Java 参考实现严格映射。
    - Java 参考路径示例：`java_sdk_reference/decompiled_source/com/kuaishou/...`。
    - 异常：所有方法在底层请求失败或返回错误码时会抛出 `KwaixiaodianAPIError`。
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化售后服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def list(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        refund_status: Optional[RefundStatus] = None,
        refund_type: Optional[int] = None,
        page_size: int = 20,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundPcursorListResponse:
        """获取卖家退款单分页列表（游标分页）

        OpenAPI: open.seller.order.refund.pcursor.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundPcursorListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundPcursorListRequest.java)

        Args:
            access_token: 访问令牌
            begin_time: 开始时间戳（毫秒）
            end_time: 结束时间戳（毫秒）
            refund_status: 退款单状态过滤
            refund_type: 退款类型：1-仅退款，2-退货退款
            page_size: 页面大小
            pcursor: 游标，用于增量翻页
            uid: 用户ID（可选，作为最后一个可选参数）

        Returns:
            SellerOrderRefundPcursorListResponse: 卖家退款单分页列表结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回非 0 错误码或解析失败时抛出。
        """
        request = SellerOrderRefundPcursorListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            status=refund_status,
            type=refund_type,
            page_size=page_size,
            pcursor=pcursor,
        )
        return await self._client.execute(request, SellerOrderRefundPcursorListResponse)

    async def get(
        self, access_token: str, refund_id: int, uid: Optional[int] = None
    ) -> SellerOrderRefundDetailResponse:
        """获取卖家退款详情

        OpenAPI: open.seller.order.refund.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundDetailRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundDetailResponse: 卖家退款详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundDetailRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return await self._client.execute(request, SellerOrderRefundDetailResponse)

    # 移除不在 Java 参考中的 open.refund.agree 接口

    async def reject(
        self,
        access_token: str,
        refund_id: int,
        reason_code: Optional[int] = None,
        reject_desc: Optional[str] = None,
        reject_images: Optional[List[str]] = None,
        refund_version: Optional[int] = None,
        edit_handling_way: Optional[int] = None,
        edit_return_address_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> RefundRejectResponse:
        """拒绝退款

        OpenAPI: open.refund.reject (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundRejectRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundRejectRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            reason_code: 拒绝原因编码
            reject_desc: 拒绝说明
            reject_images: 拒绝凭证图片URL列表
            refund_version: 退款版本号
            edit_handling_way: 处理方式（平台定义）
            edit_return_address_id: 退货地址ID
            uid: 用户ID（可选）

        Returns:
            RefundRejectResponse: 拒绝退款结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundRejectRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            reason_code=reason_code,
            reject_desc=reject_desc,
            reject_images=reject_images,
            refund_version=refund_version,
            edit_handling_way=edit_handling_way,
            edit_return_address_id=edit_return_address_id,
        )
        return await self._client.execute(request, RefundRejectResponse)

    # 移除不在 Java 参考中的 open.refund.confirm.receive 接口

    # 移除不在 Java 参考中的 open.refund.negotiate 接口

    # ==================== 扩展售后API ====================

    async def direct_refund(
        self,
        access_token: str,
        refund_id: int,
        refund_version: int,
        uid: Optional[int] = None,
    ) -> RefundDirectResponse:
        """直接退款

        OpenAPI: open.refund.direct.refund (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundDirectRefundRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundDirectRefundRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            refund_version: 退款版本号
            uid: 用户ID（可选）

        Returns:
            RefundDirectResponse: 直接退款结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundDirectRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            refund_version=refund_version,
            api_version="1",
        )
        return await self._client.execute(request, RefundDirectResponse)

    async def list_refund_comments(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> RefundCommentListResponse:
        """获取退款评论列表

        OpenAPI: open.refund.comment.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundCommentListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundCommentListRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            RefundCommentListResponse: 退款评论列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundCommentListRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return await self._client.execute(request, RefundCommentListResponse)

    async def list_refund_basic_comments(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> RefundCommentBasicListResponse:
        """获取退款基本评论列表

        OpenAPI: open.refund.comment.basic.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundCommentBasicListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundCommentBasicListRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            RefundCommentBasicListResponse: 退款基本评论列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundCommentBasicListRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return await self._client.execute(request, RefundCommentBasicListResponse)

    async def get_reject_reason(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> RefundRejectReasonResponse:
        """获取拒绝原因

        OpenAPI: open.refund.reject.reason (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundRejectReasonRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundRejectReasonRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            RefundRejectReasonResponse: 拒绝原因详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundRejectReasonRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return await self._client.execute(request, RefundRejectReasonResponse)

    async def add_evidence(
        self,
        access_token: str,
        refund_id: int,
        image_data: List[str],
        content: str,
        uid: Optional[int] = None,
    ) -> RefundEvidenceAddResponse:
        """添加退款证据

        OpenAPI: open.refund.evidence.add (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundEvidenceAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundEvidenceAddRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            image_data: 证据图片数据列表（Base64 或平台要求的格式）
            content: 证据描述内容
            uid: 用户ID（可选）

        Returns:
            RefundEvidenceAddResponse: 添加证据的处理结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundEvidenceAddRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            image_data=image_data,
            content=content,
            api_version="1",
        )
        return await self._client.execute(request, RefundEvidenceAddResponse)

    async def confirm_and_send(
        self,
        access_token: str,
        refund_id: int,
        express_no: str,
        express_code: int,
        uid: Optional[int] = None,
    ) -> RefundConfirmAndSendResponse:
        """确认并发送退货

        OpenAPI: open.refund.confirm.and.send (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundConfirmAndSendRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundConfirmAndSendRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            express_no: 快递单号
            express_code: 快递公司代码
            uid: 用户ID（可选）

        Returns:
            RefundConfirmAndSendResponse: 确认并发送退货的结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundConfirmAndSendRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            express_no=express_no,
            express_code=express_code,
            api_version="1",
        )
        return await self._client.execute(request, RefundConfirmAndSendResponse)

    async def submit_return_info(
        self,
        access_token: str,
        refund_id: int,
        express_no: str,
        express_code: int,
        uid: Optional[int] = None,
    ) -> RefundSubmitReturnInfoResponse:
        """提交退货信息

        OpenAPI: open.refund.submit.returnInfo (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundSubmitReturninfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundSubmitReturninfoRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            express_no: 快递单号
            express_code: 快递公司代码
            uid: 用户ID（可选）

        Returns:
            RefundSubmitReturnInfoResponse: 提交退货信息的结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundSubmitReturnInfoRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            express_no=express_no,
            express_code=express_code,
            api_version="1",
        )
        return await self._client.execute(request, RefundSubmitReturnInfoResponse)

    # ==================== 卖家订单退款API ====================

    async def list_seller_refunds(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        type: Optional[int] = None,
        page_size: int = 20,
        current_page: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        negotiate_status: Optional[int] = None,
        pcursor: Optional[str] = None,
        status: Optional[int] = None,
        option: Optional[RefundPageOption] = None,
        order_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundPcursorListResponse:
        """获取卖家订单退款分页列表

        OpenAPI: open.seller.order.refund.pcursor.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundPcursorListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundPcursorListRequest.java)

        Args:
            access_token: 访问令牌
            begin_time: 开始时间戳（毫秒）
            end_time: 结束时间戳（毫秒）
            type: 退款单类型
            page_size: 页面大小
            current_page: 当前页码
            sort: 排序方式
            query_type: 查询类型
            negotiate_status: 协商状态
            pcursor: 分页游标
            status: 状态
            option: 分页选项
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundPcursorListResponse: 卖家订单退款分页结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundPcursorListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            type=type,
            page_size=page_size,
            current_page=current_page,
            sort=sort,
            query_type=query_type,
            negotiate_status=negotiate_status,
            pcursor=pcursor,
            status=status,
            option=option,
            order_id=order_id,
            api_version="1",
        )
        return await self._client.execute(request, SellerOrderRefundPcursorListResponse)

    async def get_seller_refund_detail(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundDetailResponse:
        """获取卖家订单退款详情

        OpenAPI: open.seller.order.refund.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundDetailRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundDetailResponse: 退款详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundDetailRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return await self._client.execute(request, SellerOrderRefundDetailResponse)

    async def apply_entry(
        self,
        access_token: str,
        refund_id: int,
        desc: str,
        pictures: Optional[List[str]] = None,
        status: int = 0,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundApplyEntryResponse:
        """卖家退款申请入口

        OpenAPI: open.seller.order.refund.apply.entry (POST)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundApplyEntryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundApplyEntryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            desc: 申请描述
            pictures: 图片URL列表
            status: 状态
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundApplyEntryResponse: 申请入口结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundApplyEntryRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            desc=desc,
            pictures=pictures,
            status=status,
        )
        return await self._client.execute(request, SellerOrderRefundApplyEntryResponse)

    async def post_apply_entry(
        self,
        access_token: str,
        refund_id: int,
        desc: Optional[str] = None,
        pictures: Optional[List[str]] = None,
        status: int = 0,
        post_apply_judge_reason: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundPostApplyEntryResponse:
        """卖家退款售后申诉入口

        OpenAPI: open.seller.order.refund.post.apply.entry (POST)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundPostApplyEntryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundPostApplyEntryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            desc: 申诉描述
            pictures: 申诉图片URL列表
            status: 状态
            post_apply_judge_reason: 申诉判定原因
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundPostApplyEntryResponse: 申诉入口结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundPostApplyEntryRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            desc=desc,
            pictures=pictures,
            status=status,
            post_apply_judge_reason=post_apply_judge_reason,
        )
        return await self._client.execute(
            request, SellerOrderRefundPostApplyEntryResponse
        )

    async def disagree_refund(
        self,
        access_token: str,
        refund_id: int,
        seller_disagree_reason: int,
        seller_disagree_desc: Optional[str] = None,
        seller_disagree_images: Optional[List[str]] = None,
        status: int = 0,
        negotiate_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundDisagreeResponse:
        """卖家不同意退款

        OpenAPI: open.seller.order.refund.disagree.refund (POST)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundDisagreeRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundDisagreeRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            seller_disagree_reason: 不同意原因编码
            seller_disagree_desc: 不同意说明
            seller_disagree_images: 不同意凭证图片URL列表
            status: 状态
            negotiate_status: 协商状态
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundDisagreeResponse: 处理结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundDisagreeRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            seller_disagree_reason=seller_disagree_reason,
            seller_disagree_desc=seller_disagree_desc,
            seller_disagree_images=seller_disagree_images,
            status=status,
            negotiate_status=negotiate_status,
        )
        return await self._client.execute(request, SellerOrderRefundDisagreeResponse)

    async def get_evidence_history(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundEvidenceHistoryResponse:
        """退款证据历史

        OpenAPI: open.seller.order.refund.evidence.history (GET)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundEviHistoryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundEviHistoryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundEvidenceHistoryResponse: 证据历史记录

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundEvidenceHistoryRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return await self._client.execute(
            request, SellerOrderRefundEvidenceHistoryResponse
        )

    async def get_fee_detail(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundFeeDetailResponse:
        """退款费用明细

        OpenAPI: open.seller.order.refund.fee.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundFeeDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundFeeDetailRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundFeeDetailResponse: 费用明细

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundFeeDetailRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return await self._client.execute(request, SellerOrderRefundFeeDetailResponse)

    async def get_history(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundHistoryResponse:
        """退款历史

        OpenAPI: open.seller.order.refund.history (GET)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundHistoryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundHistoryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundHistoryResponse: 历史记录

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundHistoryRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return await self._client.execute(request, SellerOrderRefundHistoryResponse)

    async def approve_seller_refund(
        self,
        access_token: str,
        refund_id: int,
        refund_amount: int,
        status: int,
        desc: Optional[str] = None,
        negotiate_status: Optional[int] = None,
        refund_handing_way: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundApproveResponse:
        """卖家订单退款审批

        OpenAPI: open.seller.order.refund.approve (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundApproveRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundApproveRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            refund_amount: 审批的退款金额（分）
            status: 审批状态码
            desc: 审批描述（可选）
            negotiate_status: 协商状态（可选）
            refund_handing_way: 退款处理方式（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundApproveResponse: 审批结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundApproveRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            desc=desc,
            refund_amount=refund_amount,
            status=status,
            negotiate_status=negotiate_status,
            refund_handing_way=refund_handing_way,
            api_version="1",
        )
        return await self._client.execute(request, SellerOrderRefundApproveResponse)

    async def approve_return_goods(
        self,
        access_token: str,
        refund_id: int,
        refund_amount: int,
        address_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundReturngoodsApproveResponse:
        """卖家订单退货审批

        OpenAPI: open.seller.order.refund.returngoods.approve (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundReturngoodsApproveRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundReturngoodsApproveRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            refund_amount: 审批的退款金额（分）
            address_id: 退货地址ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundReturngoodsApproveResponse: 审批结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundReturngoodsApproveRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            refund_amount=refund_amount,
            address_id=address_id,
            api_version="1",
        )
        return await self._client.execute(
            request, SellerOrderRefundReturngoodsApproveResponse
        )

    async def confirm_receipt(
        self,
        access_token: str,
        refund_id: int,
        status: int,
        return_freight_handling_advice: Optional[int] = None,
        return_freight_amount: Optional[int] = None,
        return_freight_reject_desc: Optional[str] = None,
        return_freight_reject_images: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundConfirmReceiptResponse:
        """卖家订单退款确认收货

        OpenAPI: open.seller.order.refund.confirm.receipt (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundConfirmReceiptRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundConfirmReceiptRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            status: 确认收货状态码
            return_freight_handling_advice: 退货运费处理建议（可选）
            return_freight_amount: 退货运费金额（分，可选）
            return_freight_reject_desc: 退货运费拒绝描述（可选）
            return_freight_reject_images: 退货运费拒绝图片列表（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundConfirmReceiptResponse: 确认结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundConfirmReceiptRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            status=status,
            return_freight_handling_advice=return_freight_handling_advice,
            return_freight_amount=return_freight_amount,
            return_freight_reject_desc=return_freight_reject_desc,
            return_freight_reject_images=return_freight_reject_images,
            api_version="1",
        )
        return await self._client.execute(
            request, SellerOrderRefundConfirmReceiptResponse
        )


class SyncRefundService:
    """同步售后服务

    提供退款退货、协商处理、售后状态查询等功能。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化售后服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def list(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        refund_status: Optional[RefundStatus] = None,
        refund_type: Optional[int] = None,
        page_size: int = 20,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundPcursorListResponse:
        """获取卖家退款单分页列表（游标分页）

        OpenAPI: open.seller.order.refund.pcursor.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundPcursorListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundPcursorListRequest.java)

        Args:
            access_token: 访问令牌
            begin_time: 开始时间戳（毫秒）
            end_time: 结束时间戳（毫秒）
            refund_status: 退款单状态过滤（可选）
            refund_type: 退款类型（可选）
            page_size: 页面大小
            pcursor: 分页游标（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundPcursorListResponse: 卖家退款单分页列表结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundPcursorListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            status=refund_status,
            type=refund_type,
            page_size=page_size,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderRefundPcursorListResponse)

    def get(
        self, access_token: str, refund_id: int, uid: Optional[int] = None
    ) -> SellerOrderRefundDetailResponse:
        """获取卖家退款详情

        OpenAPI: open.seller.order.refund.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundDetailRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundDetailResponse: 退款详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundDetailRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return self._client.execute(request, SellerOrderRefundDetailResponse)

    # 移除不在 Java 参考中的 open.refund.agree 接口（同步）

    def reject(
        self,
        access_token: str,
        refund_id: int,
        reason_code: Optional[int] = None,
        reject_desc: Optional[str] = None,
        reject_images: Optional[List[str]] = None,
        refund_version: Optional[int] = None,
        edit_handling_way: Optional[int] = None,
        edit_return_address_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> RefundRejectResponse:
        """拒绝退款

        OpenAPI: open.refund.reject (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundRejectRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundRejectRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            reason_code: 拒绝原因编码（可选）
            reject_desc: 拒绝说明（可选）
            reject_images: 拒绝凭证图片URL列表（可选）
            refund_version: 退款版本号（可选）
            edit_handling_way: 处理方式（可选）
            edit_return_address_id: 退货地址ID（可选）
            uid: 用户ID（可选）

        Returns:
            RefundRejectResponse: 拒绝退款结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundRejectRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            reason_code=reason_code,
            reject_desc=reject_desc,
            reject_images=reject_images,
            refund_version=refund_version,
            edit_handling_way=edit_handling_way,
            edit_return_address_id=edit_return_address_id,
        )
        return self._client.execute(request, RefundRejectResponse)

    # 移除不在 Java 参考中的 open.refund.confirm.receive 接口（同步）

    # 移除不在 Java 参考中的 open.refund.negotiate 接口（同步）

    # ==================== 扩展售后API ====================

    def direct_refund(
        self,
        access_token: str,
        refund_id: int,
        refund_version: int,
        uid: Optional[int] = None,
    ) -> RefundDirectResponse:
        """直接退款

        OpenAPI: open.refund.direct.refund (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundDirectRefundRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundDirectRefundRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            refund_version: 退款版本号
            uid: 用户ID（可选）

        Returns:
            RefundDirectResponse: 直接退款结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundDirectRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            refund_version=refund_version,
            api_version="1",
        )
        return self._client.execute(request, RefundDirectResponse)

    def list_refund_comments(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> RefundCommentListResponse:
        """获取退款评论列表

        OpenAPI: open.refund.comment.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundCommentListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundCommentListRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            RefundCommentListResponse: 退款评论列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundCommentListRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return self._client.execute(request, RefundCommentListResponse)

    def list_refund_basic_comments(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> RefundCommentBasicListResponse:
        """获取退款基本评论列表

        OpenAPI: open.refund.comment.basic.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundCommentBasicListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundCommentBasicListRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            RefundCommentBasicListResponse: 退款基本评论列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundCommentBasicListRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return self._client.execute(request, RefundCommentBasicListResponse)

    def get_reject_reason(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> RefundRejectReasonResponse:
        """获取拒绝原因

        OpenAPI: open.refund.reject.reason (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundRejectReasonRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundRejectReasonRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            RefundRejectReasonResponse: 拒绝原因详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundRejectReasonRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return self._client.execute(request, RefundRejectReasonResponse)

    def add_evidence(
        self,
        access_token: str,
        refund_id: int,
        image_data: List[str],
        content: str,
        uid: Optional[int] = None,
    ) -> RefundEvidenceAddResponse:
        """添加退款证据

        OpenAPI: open.refund.evidence.add (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundEvidenceAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundEvidenceAddRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            image_data: 证据图片数据列表
            content: 证据描述内容
            uid: 用户ID（可选）

        Returns:
            RefundEvidenceAddResponse: 添加证据的处理结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundEvidenceAddRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            image_data=image_data,
            content=content,
            api_version="1",
        )
        return self._client.execute(request, RefundEvidenceAddResponse)

    def confirm_and_send(
        self,
        access_token: str,
        refund_id: int,
        express_no: str,
        express_code: int,
        uid: Optional[int] = None,
    ) -> RefundConfirmAndSendResponse:
        """确认并发送退货

        OpenAPI: open.refund.confirm.and.send (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundConfirmAndSendRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundConfirmAndSendRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            express_no: 快递单号
            express_code: 快递公司代码
            uid: 用户ID（可选）

        Returns:
            RefundConfirmAndSendResponse: 确认并发送退货的结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundConfirmAndSendRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            express_no=express_no,
            express_code=express_code,
            api_version="1",
        )
        return self._client.execute(request, RefundConfirmAndSendResponse)

    def submit_return_info(
        self,
        access_token: str,
        refund_id: int,
        express_no: str,
        express_code: int,
        uid: Optional[int] = None,
    ) -> RefundSubmitReturnInfoResponse:
        """提交退货信息

        OpenAPI: open.refund.submit.returnInfo (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenRefundSubmitReturninfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenRefundSubmitReturninfoRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            express_no: 快递单号
            express_code: 快递公司代码
            uid: 用户ID（可选）

        Returns:
            RefundSubmitReturnInfoResponse: 提交退货信息的结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = RefundSubmitReturnInfoRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            express_no=express_no,
            express_code=express_code,
            api_version="1",
        )
        return self._client.execute(request, RefundSubmitReturnInfoResponse)

    # ==================== 卖家订单退款API ====================

    def list_seller_refunds(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        type: Optional[int] = None,
        page_size: int = 20,
        current_page: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        negotiate_status: Optional[int] = None,
        pcursor: Optional[str] = None,
        status: Optional[int] = None,
        option: Optional[RefundPageOption] = None,
        order_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundPcursorListResponse:
        """获取卖家订单退款分页列表

        OpenAPI: open.seller.order.refund.pcursor.list (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundPcursorListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundPcursorListRequest.java)

        Args:
            access_token: 访问令牌
            begin_time: 开始时间戳（毫秒）
            end_time: 结束时间戳（毫秒）
            type: 退款类型（可选）
            page_size: 页面大小
            current_page: 当前页码（可选）
            sort: 排序方式（可选）
            query_type: 查询类型（可选）
            negotiate_status: 协商状态（可选）
            pcursor: 分页游标（可选）
            status: 状态（可选）
            option: 分页选项（可选）
            order_id: 订单ID（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundPcursorListResponse: 卖家订单退款分页结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundPcursorListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            type=type,
            page_size=page_size,
            current_page=current_page,
            sort=sort,
            query_type=query_type,
            negotiate_status=negotiate_status,
            pcursor=pcursor,
            status=status,
            option=option,
            order_id=order_id,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderRefundPcursorListResponse)

    def get_seller_refund_detail(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundDetailResponse:
        """获取卖家订单退款详情

        OpenAPI: open.seller.order.refund.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundDetailRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundDetailResponse: 退款详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundDetailRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderRefundDetailResponse)

    def apply_entry(
        self,
        access_token: str,
        refund_id: int,
        desc: str,
        pictures: Optional[List[str]] = None,
        status: int = 0,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundApplyEntryResponse:
        """卖家退款申请入口

        OpenAPI: open.seller.order.refund.apply.entry (POST)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundApplyEntryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundApplyEntryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            desc: 申请描述
            pictures: 图片URL列表（可选）
            status: 状态（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundApplyEntryResponse: 申请入口结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundApplyEntryRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            desc=desc,
            pictures=pictures,
            status=status,
        )
        return self._client.execute(request, SellerOrderRefundApplyEntryResponse)

    def post_apply_entry(
        self,
        access_token: str,
        refund_id: int,
        desc: Optional[str] = None,
        pictures: Optional[List[str]] = None,
        status: int = 0,
        post_apply_judge_reason: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundPostApplyEntryResponse:
        """卖家退款售后申诉入口

        OpenAPI: open.seller.order.refund.post.apply.entry (POST)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundPostApplyEntryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundPostApplyEntryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            desc: 申诉描述（可选）
            pictures: 申诉图片URL列表（可选）
            status: 状态（可选）
            post_apply_judge_reason: 申诉判定原因（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundPostApplyEntryResponse: 申诉入口结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundPostApplyEntryRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            desc=desc,
            pictures=pictures,
            status=status,
            post_apply_judge_reason=post_apply_judge_reason,
        )
        return self._client.execute(request, SellerOrderRefundPostApplyEntryResponse)

    def disagree_refund(
        self,
        access_token: str,
        refund_id: int,
        seller_disagree_reason: int,
        seller_disagree_desc: Optional[str] = None,
        seller_disagree_images: Optional[List[str]] = None,
        status: int = 0,
        negotiate_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundDisagreeResponse:
        """卖家不同意退款

        OpenAPI: open.seller.order.refund.disagree.refund (POST)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundDisagreeRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundDisagreeRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            seller_disagree_reason: 不同意原因编码
            seller_disagree_desc: 不同意说明（可选）
            seller_disagree_images: 不同意凭证图片URL列表（可选）
            status: 状态（可选）
            negotiate_status: 协商状态（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundDisagreeResponse: 不同意退款结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundDisagreeRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            seller_disagree_reason=seller_disagree_reason,
            seller_disagree_desc=seller_disagree_desc,
            seller_disagree_images=seller_disagree_images,
            status=status,
            negotiate_status=negotiate_status,
        )
        return self._client.execute(request, SellerOrderRefundDisagreeResponse)

    def get_evidence_history(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundEvidenceHistoryResponse:
        """退款证据历史

        OpenAPI: open.seller.order.refund.evidence.history (GET)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundEviHistoryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundEviHistoryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundEvidenceHistoryResponse: 退款证据历史记录

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundEvidenceHistoryRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return self._client.execute(request, SellerOrderRefundEvidenceHistoryResponse)

    def get_fee_detail(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundFeeDetailResponse:
        """退款费用明细

        OpenAPI: open.seller.order.refund.fee.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundFeeDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundFeeDetailRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundFeeDetailResponse: 退款费用明细

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundFeeDetailRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return self._client.execute(request, SellerOrderRefundFeeDetailResponse)

    def get_history(
        self,
        access_token: str,
        refund_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundHistoryResponse:
        """退款历史

        OpenAPI: open.seller.order.refund.history (GET)
        Java: com.kuaishou.merchant.open.api.request.KsMerchantRefundHistoryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantRefundHistoryRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundHistoryResponse: 退款历史记录

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundHistoryRequest(
            access_token=access_token, uid=uid, refund_id=refund_id
        )
        return self._client.execute(request, SellerOrderRefundHistoryResponse)

    def approve_seller_refund(
        self,
        access_token: str,
        refund_id: int,
        refund_amount: int,
        status: int,
        desc: Optional[str] = None,
        negotiate_status: Optional[int] = None,
        refund_handing_way: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundApproveResponse:
        """卖家订单退款审批

        OpenAPI: open.seller.order.refund.approve (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundApproveRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundApproveRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            refund_amount: 审批的退款金额（分）
            status: 审批状态码
            desc: 审批描述（可选）
            negotiate_status: 协商状态（可选）
            refund_handing_way: 退款处理方式（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundApproveResponse: 审批结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundApproveRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            desc=desc,
            refund_amount=refund_amount,
            status=status,
            negotiate_status=negotiate_status,
            refund_handing_way=refund_handing_way,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderRefundApproveResponse)

    def approve_return_goods(
        self,
        access_token: str,
        refund_id: int,
        refund_amount: int,
        address_id: int,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundReturngoodsApproveResponse:
        """卖家订单退货审批

        OpenAPI: open.seller.order.refund.returngoods.approve (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundReturngoodsApproveRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundReturngoodsApproveRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            refund_amount: 审批的退款金额（分）
            address_id: 退货地址ID
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundReturngoodsApproveResponse: 审批结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundReturngoodsApproveRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            refund_amount=refund_amount,
            address_id=address_id,
            api_version="1",
        )
        return self._client.execute(
            request, SellerOrderRefundReturngoodsApproveResponse
        )

    def confirm_receipt(
        self,
        access_token: str,
        refund_id: int,
        status: int,
        return_freight_handling_advice: Optional[int] = None,
        return_freight_amount: Optional[int] = None,
        return_freight_reject_desc: Optional[str] = None,
        return_freight_reject_images: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderRefundConfirmReceiptResponse:
        """卖家订单退款确认收货

        OpenAPI: open.seller.order.refund.confirm.receipt (POST)
        Java: com.kuaishou.merchant.open.api.request.refund.OpenSellerOrderRefundConfirmReceiptRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/refund/OpenSellerOrderRefundConfirmReceiptRequest.java)

        Args:
            access_token: 访问令牌
            refund_id: 退款单ID
            status: 确认收货状态码
            return_freight_handling_advice: 退货运费处理建议（可选）
            return_freight_amount: 退货运费金额（分，可选）
            return_freight_reject_desc: 退货运费拒绝描述（可选）
            return_freight_reject_images: 退货运费拒绝图片列表（可选）
            uid: 用户ID（可选）

        Returns:
            SellerOrderRefundConfirmReceiptResponse: 确认结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = SellerOrderRefundConfirmReceiptRequest(
            access_token=access_token,
            uid=uid,
            refund_id=refund_id,
            status=status,
            return_freight_handling_advice=return_freight_handling_advice,
            return_freight_amount=return_freight_amount,
            return_freight_reject_desc=return_freight_reject_desc,
            return_freight_reject_images=return_freight_reject_images,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderRefundConfirmReceiptResponse)
