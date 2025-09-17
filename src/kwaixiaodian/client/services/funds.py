"""资金管理服务类"""

from typing import List, Optional

from ...models.funds import (
    FundsAccountInfoRequest,
    FundsAccountInfoResponse,
    FundsApplyInvoiceFileRequest,
    FundsApplyInvoiceFileResponse,
    FundsApplyInvoiceRequest,
    FundsApplyInvoiceResponse,
    FundsAuditInvoiceInfoRequest,
    FundsAuditInvoiceInfoResponse,
    FundsBillBatchDetailRequest,
    FundsBillBatchDetailResponse,
    # New missing APIs - 新增缺失API
    FundsDailyBillRequest,
    FundsDailyBillResponse,
    FundsFinancialQueryBillListRequest,
    FundsFinancialQueryBillListResponse,
    FundsFreightInsuranceListRequest,
    FundsFreightInsuranceListResponse,
    FundsPinganBillRequest,
    FundsPinganBillResponse,
    FundsPostSalesBillListRequest,
    FundsPostSalesBillListResponse,
    FundsQueryAccountBillRequest,
    FundsQueryAccountBillResponse,
    FundsSettledBillDetailRequest,
    FundsSettledBillDetailResponse,
    FundsStatementListRequest,
    FundsStatementListResponse,
    FundsWithdrawApplyRequest,
    FundsWithdrawApplyResponse,
    FundsWithdrawQueryRequest,
    FundsWithdrawQueryResponse,
    FundsWithdrawRecordRequest,
    FundsWithdrawRecordResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncFundsService:
    """异步资金管理服务

    提供账户资金查询、资金流水记录、提现管理、结算查询等功能。
    支持完整的资金生命周期管理和财务对账功能。
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化资金管理服务

        Args:
            client: 异步基础客户端实例
        """
        self._client = client

    async def get_account_info(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> FundsAccountInfoResponse:
        """获取账户资金信息。

        OpenAPI: `open.funds.center.account.info` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterAccountInfoRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterAccountInfoRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsAccountInfoResponse: 账户资金信息。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            account = await funds_service.get_account_info(
                access_token="your_token",
                account_type=AccountType.MAIN
            )

            if account.result:
                print(f"可用余额: {account.result.available_yuan}元")
                print(f"冻结余额: {account.result.frozen_yuan}元")
                print(f"总余额: {account.result.total_yuan}元")
            ```
        """
        request = FundsAccountInfoRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsAccountInfoResponse)

    # Java reference has no open.funds.bill.list; removed.

    async def apply_withdraw(
        self,
        access_token: str,
        withdraw_money: int,
        withdraw_no: Optional[str] = None,
        remark: Optional[str] = None,
        account_channel: Optional[int] = None,
        sub_merchant_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsWithdrawApplyResponse:
        """申请提现。

        OpenAPI: `open.funds.center.withdraw.apply` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterWithdrawApplyRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterWithdrawApplyRequest.java`

        Args:
            access_token: 访问令牌。
            withdraw_money: 提现金额（分）。
            withdraw_no: 提现单号（可选）。
            remark: 备注信息（可选）。
            account_channel: 出账通道（可选）。
            sub_merchant_id: 子商户 ID（可选）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsWithdrawApplyResponse: 提现申请结果。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            result = await funds_service.apply_withdraw(
                access_token="your_token",
                withdraw_amount=100000,  # 1000.00元
                withdraw_type=WithdrawType.BANK_CARD,
                bank_name="中国工商银行",
                bank_account="1234567890123456789",
                account_holder="张三",
                remark="日常提现"
            )

            if result.is_success:
                print("提现申请提交成功")
            ```
        """
        request = FundsWithdrawApplyRequest(
            access_token=access_token,
            uid=uid,
            withdraw_money=withdraw_money,
            withdraw_no=withdraw_no,
            remark=remark,
            account_channel=account_channel,
            sub_merchant_id=sub_merchant_id,
            api_version="1",
        )

        return await self._client.execute(request, FundsWithdrawApplyResponse)

    async def list_withdraw_records(
        self,
        access_token: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        account_channel: Optional[int] = None,
        sub_merchant_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsWithdrawRecordResponse:
        """获取提现记录。

        OpenAPI: `open.funds.center.wirhdraw.record.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterWirhdrawRecordListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterWirhdrawRecordListRequest.java`

        Args:
            access_token: 访问令牌。
            limit: 每页大小。
            page: 页码。
            create_time_start: 开始时间（时间戳）。
            create_time_end: 结束时间（时间戳）。
            account_channel: 出账通道。
            sub_merchant_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsWithdrawRecordResponse: 提现记录响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            records = await funds_service.list_withdraw_records(
                access_token="your_token",
                withdraw_status=WithdrawStatus.SUCCESS,
                page_size=30
            )

            if records.result and records.result.items:
                for record in records.result.items:
                    print(f"提现单号: {record.withdraw_no}")
                    print(f"提现金额: {record.withdraw_yuan}元")
                    print(f"实际到账: {record.actual_yuan}元")
                    print(f"状态: {record.withdraw_status.name}")
            ```
        """
        request = FundsWithdrawRecordRequest(
            access_token=access_token,
            uid=uid,
            limit=limit,
            page=page,
            create_time_start=create_time_start,
            create_time_end=create_time_end,
            account_channel=account_channel,
            sub_merchant_id=sub_merchant_id,
            api_version="1",
        )

        return await self._client.execute(request, FundsWithdrawRecordResponse)

    async def query_withdraw(
        self, access_token: str, withdraw_no: str, uid: Optional[int] = None
    ) -> FundsWithdrawQueryResponse:
        """查询提现状态。

        OpenAPI: `open.funds.center.get.withdraw.result` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterGetWithdrawResultRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterGetWithdrawResultRequest.java`

        Args:
            access_token: 访问令牌。
            withdraw_no: 提现单号。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsWithdrawQueryResponse: 提现状态查询响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            withdraw = await funds_service.query_withdraw(
                access_token="your_token",
                withdraw_no="WD20240101001"
            )

            if withdraw.result:
                print(f"提现状态: {withdraw.result.withdraw_status.name}")
                if withdraw.result.is_success:
                    print(f"到账金额: {withdraw.result.actual_yuan}元")
                elif withdraw.result.reject_reason:
                    print(f"拒绝原因: {withdraw.result.reject_reason}")
            ```
        """
        request = FundsWithdrawQueryRequest(
            access_token=access_token,
            uid=uid,
            withdraw_no=withdraw_no,
            api_version="1",
        )

        return await self._client.execute(request, FundsWithdrawQueryResponse)

    # Java reference has no open.funds.settlement.list; removed.

    # ==================== 新增缺失API方法 ====================

    async def get_daily_bill(
        self,
        access_token: str,
        bill_date: str,
        bill_type: Optional[str] = None,
        expire_date: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsDailyBillResponse:
        """获取日账单。

        OpenAPI: `open.funds.center.get.daily.bill` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterGetDailyBillRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterGetDailyBillRequest.java`

        Args:
            access_token: 访问令牌。
            bill_date: 账单日期，格式与平台一致（例如 `YYYY-MM-DD`）。
            bill_type: 账单类型。
            expire_date: 过期日期（毫秒时间戳），可选。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsDailyBillResponse: 日账单下载信息。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsDailyBillRequest(
            access_token=access_token,
            bill_date=bill_date,
            bill_type=bill_type,
            expire_date=expire_date,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsDailyBillResponse)

    async def get_bill_batch_detail(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        settlement_start_time: Optional[int] = None,
        settlement_end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsBillBatchDetailResponse:
        """批量账单详情。

        OpenAPI: `open.funds.financial.bill.batch.detail` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialBillBatchDetailRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialBillBatchDetailRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            settlement_start_time: 结算开始时间（毫秒时间戳）。
            settlement_end_time: 结算结束时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsBillBatchDetailResponse: 批量账单详情响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsBillBatchDetailRequest(
            access_token=access_token,
            cursor=cursor,
            settlement_start_time=settlement_start_time,
            settlement_end_time=settlement_end_time,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsBillBatchDetailResponse)

    async def get_post_sales_bill_list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsPostSalesBillListResponse:
        """售后账单列表。

        OpenAPI: `open.funds.financial.bill.post.sales.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialBillPostSalesListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialBillPostSalesListRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsPostSalesBillListResponse: 售后账单列表响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsPostSalesBillListRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsPostSalesBillListResponse)

    async def query_financial_bill_list(
        self,
        access_token: str,
        end_time: Optional[int] = None,
        scroll_id: Optional[str] = None,
        order_status: Optional[int] = None,
        start_time: Optional[int] = None,
        bill_type: Optional[str] = None,
        account_channel: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> FundsFinancialQueryBillListResponse:
        """资金财务账单列表。

        OpenAPI: `open.funds.financial.query.bill.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialQueryBillListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialQueryBillListRequest.java`

        Args:
            access_token: 访问令牌。
            end_time: 结束时间（毫秒时间戳）。
            scroll_id: 滚动游标 ID，用于游标翻页。
            order_status: 订单状态。
            start_time: 开始时间（毫秒时间戳）。
            bill_type: 账单类型。
            account_channel: 出入账渠道列表。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsFinancialQueryBillListResponse: 财务账单列表数据。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsFinancialQueryBillListRequest(
            access_token=access_token,
            end_time=end_time,
            scroll_id=scroll_id,
            order_status=order_status,
            start_time=start_time,
            bill_type=bill_type,
            account_channel=account_channel,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, FundsFinancialQueryBillListResponse)

    async def query_account_bills(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        role_type: Optional[str] = None,
        biz_type: Optional[list] = None,
        wallet_type: Optional[str] = None,
        sub_mch_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsQueryAccountBillResponse:
        """查询账户账单。

        OpenAPI: `open.funds.financial.bill.query.account` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialBillQueryAccountRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialBillQueryAccountRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            role_type: 角色类型。
            biz_type: 业务类型列表。
            wallet_type: 钱包类型。
            sub_mch_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsQueryAccountBillResponse: 查询账户账单响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsQueryAccountBillRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            role_type=role_type,
            biz_type=biz_type,
            wallet_type=wallet_type,
            sub_mch_id=sub_mch_id,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsQueryAccountBillResponse)

    async def get_settled_bill_detail(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        settlement_start_time: Optional[int] = None,
        settlement_end_time: Optional[int] = None,
        order_id: Optional[int] = None,
        size: Optional[int] = None,
        order_complete_start_time: Optional[int] = None,
        order_complete_end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsSettledBillDetailResponse:
        """结算账单详情。

        OpenAPI: `open.funds.financial.settled.bill.detail` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialSettledBillDetailRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialSettledBillDetailRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            settlement_start_time: 结算开始时间（毫秒时间戳）。
            settlement_end_time: 结算结束时间（毫秒时间戳）。
            order_id: 订单 ID。
            size: 分页大小。
            order_complete_start_time: 订单完成开始时间（毫秒时间戳）。
            order_complete_end_time: 订单完成结束时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsSettledBillDetailResponse: 结算账单详情响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsSettledBillDetailRequest(
            access_token=access_token,
            cursor=cursor,
            settlement_start_time=settlement_start_time,
            settlement_end_time=settlement_end_time,
            order_id=order_id,
            size=size,
            order_complete_start_time=order_complete_start_time,
            order_complete_end_time=order_complete_end_time,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsSettledBillDetailResponse)

    async def get_freight_insurance_list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_complete_time: Optional[int] = None,
        end_complete_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsFreightInsuranceListResponse:
        """运费险列表。

        OpenAPI: `open.funds.financial.freight.insurance.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialFreightInsuranceListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialFreightInsuranceListRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_complete_time: 开始完成时间（毫秒时间戳）。
            end_complete_time: 结束完成时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsFreightInsuranceListResponse: 运费险列表响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsFreightInsuranceListRequest(
            access_token=access_token,
            cursor=cursor,
            start_complete_time=start_complete_time,
            end_complete_time=end_complete_time,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsFreightInsuranceListResponse)

    async def get_pingan_bill(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        biz_type: Optional[list] = None,
        sub_mch_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsPinganBillResponse:
        """平安账单。

        OpenAPI: `open.funds.financial.pingan.bill` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialPinganBillRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialPinganBillRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            biz_type: 业务类型列表。
            sub_mch_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsPinganBillResponse: 平安账单响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsPinganBillRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            biz_type=biz_type,
            sub_mch_id=sub_mch_id,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsPinganBillResponse)

    async def get_statement_list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        sub_mch_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsStatementListResponse:
        """对账单列表。

        OpenAPI: `open.funds.financial.statement.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialStatementListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialStatementListRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            sub_mch_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsStatementListResponse: 对账单列表响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsStatementListRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            sub_mch_id=sub_mch_id,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsStatementListResponse)

    async def apply_invoice(
        self,
        access_token: str,
        amount: int,
        relate_order_no: str,
        invoice_type: int,
        invoice_open_kind: int,
        electron_invoice_info_list: Optional[List[dict]] = None,
        tax_rate: Optional[str] = None,
        token: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsApplyInvoiceResponse:
        """申请发票（非文件接口）。

        OpenAPI: `open.funds.subsidy.open.apply.invoice` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsSubsidyOpenApplyInvoiceRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsSubsidyOpenApplyInvoiceRequest.java`

        Args:
            access_token: 访问令牌。
            amount: 发票金额（分）。
            relate_order_no: 关联订单号。
            invoice_type: 发票类型。
            invoice_open_kind: 发票开具类型。
            electron_invoice_info_list: 电子发票明细列表。
            tax_rate: 税率。
            token: 防重放 token，可选。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsApplyInvoiceResponse: 申请结果。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsApplyInvoiceRequest(
            access_token=access_token,
            amount=amount,
            relate_order_no=relate_order_no,
            invoice_type=invoice_type,
            invoice_open_kind=invoice_open_kind,
            electron_invoice_info_list=electron_invoice_info_list,
            tax_rate=tax_rate,
            token=token,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsApplyInvoiceResponse)

    async def audit_invoice_info(
        self,
        access_token: str,
        oid: str,
        uid: Optional[int] = None,
    ) -> FundsAuditInvoiceInfoResponse:
        """审核发票信息。

        OpenAPI: `open.funds.subsidy.audit.invoice.info` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsSubsidyAuditInvoiceInfoRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsSubsidyAuditInvoiceInfoRequest.java`

        Args:
            access_token: 访问令牌。
            oid: 订单 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsAuditInvoiceInfoResponse: 审核发票信息响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsAuditInvoiceInfoRequest(
            access_token=access_token,
            oid=oid,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsAuditInvoiceInfoResponse)

    async def apply_invoice_file(
        self,
        access_token: str,
        relate_order_no: str,
        invoice_open_kind: int,
        tax_rate: str,
        cert_no: str,
        invoice_name: str,
        invoice_open_date: int,
        count: int,
        goods: str,
        invoice_code: str,
        invoice_verify_code: str,
        invoice_tax: str,
        tax_authority_code: str,
        invoice_location_code: str,
        exclude_tax_amount: str,
        isv_code: str,
        invoice_no: str,
        uid: Optional[int] = None,
        # Note: invoice_bytes file upload parameter should be handled separately
    ) -> FundsApplyInvoiceFileResponse:
        """申请发票文件。

        OpenAPI: `open.funds.subsidy.open.apply.invoice.file` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsSubsidyOpenApplyInvoiceFileRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsSubsidyOpenApplyInvoiceFileRequest.java`

        Args:
            access_token: 访问令牌。
            relate_order_no: 关联订单号。
            invoice_open_kind: 发票开具类型。
            tax_rate: 税率。
            cert_no: 证书号。
            invoice_name: 发票名称。
            invoice_open_date: 发票开具日期（毫秒时间戳）。
            count: 数量。
            goods: 商品。
            invoice_code: 发票代码。
            invoice_verify_code: 发票验证码。
            invoice_tax: 发票税额。
            tax_authority_code: 税务机关代码。
            invoice_location_code: 发票所在地代码。
            exclude_tax_amount: 不含税金额。
            isv_code: ISV 代码。
            invoice_no: 发票号码。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsApplyInvoiceFileResponse: 申请发票文件响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsApplyInvoiceFileRequest(
            access_token=access_token,
            relate_order_no=relate_order_no,
            invoice_open_kind=invoice_open_kind,
            tax_rate=tax_rate,
            cert_no=cert_no,
            invoice_name=invoice_name,
            invoice_open_date=invoice_open_date,
            count=count,
            goods=goods,
            invoice_code=invoice_code,
            invoice_verify_code=invoice_verify_code,
            invoice_tax=invoice_tax,
            tax_authority_code=tax_authority_code,
            invoice_location_code=invoice_location_code,
            exclude_tax_amount=exclude_tax_amount,
            isv_code=isv_code,
            invoice_no=invoice_no,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, FundsApplyInvoiceFileResponse)


class SyncFundsService:
    """同步资金管理服务

    提供账户资金查询、资金流水记录、提现管理、结算查询等功能的同步版本。
    支持完整的资金生命周期管理和财务对账功能。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化资金管理服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def get_account_info(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> FundsAccountInfoResponse:
        """获取账户资金信息。

        OpenAPI: `open.funds.center.account.info` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterAccountInfoRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterAccountInfoRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsAccountInfoResponse: 账户资金信息响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            account = funds_service.get_account_info(
                access_token="your_token",
                account_type=AccountType.MAIN
            )

            if account.result:
                print(f"可用余额: {account.result.available_yuan}元")
                print(f"冻结余额: {account.result.frozen_yuan}元")
                print(f"总余额: {account.result.total_yuan}元")
            ```
        """
        request = FundsAccountInfoRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsAccountInfoResponse)

    # Java reference has no open.funds.bill.list; removed.

    def apply_withdraw(
        self,
        access_token: str,
        withdraw_money: int,
        withdraw_no: Optional[str] = None,
        remark: Optional[str] = None,
        account_channel: Optional[int] = None,
        sub_merchant_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsWithdrawApplyResponse:
        """申请提现。

        OpenAPI: `open.funds.center.withdraw.apply` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterWithdrawApplyRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterWithdrawApplyRequest.java`

        Args:
            access_token: 访问令牌。
            withdraw_money: 提现金额（分）。
            withdraw_no: 提现单号，可选。
            remark: 备注信息，可选。
            account_channel: 出账通道，可选。
            sub_merchant_id: 子商户 ID，可选。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsWithdrawApplyResponse: 申请提现响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            result = funds_service.apply_withdraw(
                access_token="your_token",
                withdraw_amount=100000,  # 1000.00元
                withdraw_type=WithdrawType.BANK_CARD,
                bank_name="中国工商银行",
                bank_account="1234567890123456789",
                account_holder="张三",
                remark="日常提现"
            )

            if result.is_success:
                print("提现申请提交成功")
            ```
        """
        request = FundsWithdrawApplyRequest(
            access_token=access_token,
            uid=uid,
            withdraw_money=withdraw_money,
            withdraw_no=withdraw_no,
            remark=remark,
            account_channel=account_channel,
            sub_merchant_id=sub_merchant_id,
            api_version="1",
        )

        return self._client.execute(request, FundsWithdrawApplyResponse)

    def list_withdraw_records(
        self,
        access_token: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        account_channel: Optional[int] = None,
        sub_merchant_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsWithdrawRecordResponse:
        """获取提现记录。

        OpenAPI: `open.funds.center.wirhdraw.record.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterWirhdrawRecordListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterWirhdrawRecordListRequest.java`

        Args:
            access_token: 访问令牌。
            limit: 每页大小。
            page: 页码。
            create_time_start: 开始时间（时间戳）。
            create_time_end: 结束时间（时间戳）。
            account_channel: 出账通道。
            sub_merchant_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsWithdrawRecordResponse: 提现记录响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            records = funds_service.list_withdraw_records(
                access_token="your_token",
                withdraw_status=WithdrawStatus.SUCCESS,
                page_size=30
            )

            if records.result and records.result.items:
                for record in records.result.items:
                    print(f"提现单号: {record.withdraw_no}")
                    print(f"提现金额: {record.withdraw_yuan}元")
                    print(f"实际到账: {record.actual_yuan}元")
                    print(f"状态: {record.withdraw_status.name}")
            ```
        """
        request = FundsWithdrawRecordRequest(
            access_token=access_token,
            uid=uid,
            limit=limit,
            page=page,
            create_time_start=create_time_start,
            create_time_end=create_time_end,
            account_channel=account_channel,
            sub_merchant_id=sub_merchant_id,
            api_version="1",
        )

        return self._client.execute(request, FundsWithdrawRecordResponse)

    def query_withdraw(
        self, access_token: str, withdraw_no: str, uid: Optional[int] = None
    ) -> FundsWithdrawQueryResponse:
        """查询提现状态。

        OpenAPI: `open.funds.center.get.withdraw.result` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterGetWithdrawResultRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterGetWithdrawResultRequest.java`

        Args:
            access_token: 访问令牌。
            withdraw_no: 提现单号。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsWithdrawQueryResponse: 提现状态查询响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        Example:
            ```python
            withdraw = funds_service.query_withdraw(
                access_token="your_token",
                withdraw_no="WD20240101001"
            )

            if withdraw.result:
                print(f"提现状态: {withdraw.result.withdraw_status.name}")
                if withdraw.result.is_success:
                    print(f"到账金额: {withdraw.result.actual_yuan}元")
                elif withdraw.result.reject_reason:
                    print(f"拒绝原因: {withdraw.result.reject_reason}")
            ```
        """
        request = FundsWithdrawQueryRequest(
            access_token=access_token,
            uid=uid,
            withdraw_no=withdraw_no,
            api_version="1",
        )

        return self._client.execute(request, FundsWithdrawQueryResponse)

    # Java reference has no open.funds.settlement.list; removed.

    # Java reference has no open.funds.stats; removed.

    # ==================== 新增缺失API方法 ====================

    def get_daily_bill(
        self,
        access_token: str,
        bill_date: str,
        bill_type: Optional[str] = None,
        expire_date: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsDailyBillResponse:
        """获取日账单。

        OpenAPI: `open.funds.center.get.daily.bill` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsCenterGetDailyBillRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsCenterGetDailyBillRequest.java`

        Args:
            access_token: 访问令牌。
            bill_date: 账单日期，格式与平台一致（例如 `YYYY-MM-DD`）。
            bill_type: 账单类型。
            expire_date: 过期日期（毫秒时间戳），可选。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsDailyBillResponse: 日账单响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsDailyBillRequest(
            access_token=access_token,
            bill_date=bill_date,
            bill_type=bill_type,
            expire_date=expire_date,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsDailyBillResponse)

    def get_bill_batch_detail(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        settlement_start_time: Optional[int] = None,
        settlement_end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsBillBatchDetailResponse:
        """批量账单详情。

        OpenAPI: `open.funds.financial.bill.batch.detail` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialBillBatchDetailRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialBillBatchDetailRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            settlement_start_time: 结算开始时间（毫秒时间戳）。
            settlement_end_time: 结算结束时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsBillBatchDetailResponse: 批量账单详情响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsBillBatchDetailRequest(
            access_token=access_token,
            cursor=cursor,
            settlement_start_time=settlement_start_time,
            settlement_end_time=settlement_end_time,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsBillBatchDetailResponse)

    def get_post_sales_bill_list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsPostSalesBillListResponse:
        """售后账单列表。

        OpenAPI: `open.funds.financial.bill.post.sales.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialBillPostSalesListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialBillPostSalesListRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsPostSalesBillListResponse: 售后账单列表响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsPostSalesBillListRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsPostSalesBillListResponse)

    def query_financial_bill_list(
        self,
        access_token: str,
        end_time: Optional[int] = None,
        scroll_id: Optional[str] = None,
        order_status: Optional[int] = None,
        start_time: Optional[int] = None,
        bill_type: Optional[str] = None,
        account_channel: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> FundsFinancialQueryBillListResponse:
        """资金财务账单列表。

        OpenAPI: `open.funds.financial.query.bill.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialQueryBillListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialQueryBillListRequest.java`

        Args:
            access_token: 访问令牌。
            end_time: 结束时间（毫秒时间戳）。
            scroll_id: 滚动游标 ID，用于游标翻页。
            order_status: 订单状态。
            start_time: 开始时间（毫秒时间戳）。
            bill_type: 账单类型。
            account_channel: 出入账渠道列表。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsFinancialQueryBillListResponse: 财务账单列表数据。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsFinancialQueryBillListRequest(
            access_token=access_token,
            end_time=end_time,
            scroll_id=scroll_id,
            order_status=order_status,
            start_time=start_time,
            bill_type=bill_type,
            account_channel=account_channel,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, FundsFinancialQueryBillListResponse)

    def query_account_bills(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        role_type: Optional[str] = None,
        biz_type: Optional[list] = None,
        wallet_type: Optional[str] = None,
        sub_mch_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsQueryAccountBillResponse:
        """查询账户账单。

        OpenAPI: `open.funds.financial.bill.query.account` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialBillQueryAccountRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialBillQueryAccountRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            role_type: 角色类型。
            biz_type: 业务类型列表。
            wallet_type: 钱包类型。
            sub_mch_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsQueryAccountBillResponse: 查询账户账单响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsQueryAccountBillRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            role_type=role_type,
            biz_type=biz_type,
            wallet_type=wallet_type,
            sub_mch_id=sub_mch_id,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsQueryAccountBillResponse)

    def get_settled_bill_detail(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        settlement_start_time: Optional[int] = None,
        settlement_end_time: Optional[int] = None,
        order_id: Optional[int] = None,
        size: Optional[int] = None,
        order_complete_start_time: Optional[int] = None,
        order_complete_end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsSettledBillDetailResponse:
        """结算账单详情。

        OpenAPI: `open.funds.financial.settled.bill.detail` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialSettledBillDetailRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialSettledBillDetailRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            settlement_start_time: 结算开始时间（毫秒时间戳）。
            settlement_end_time: 结算结束时间（毫秒时间戳）。
            order_id: 订单 ID。
            size: 分页大小。
            order_complete_start_time: 订单完成开始时间（毫秒时间戳）。
            order_complete_end_time: 订单完成结束时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsSettledBillDetailResponse: 结算账单详情响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsSettledBillDetailRequest(
            access_token=access_token,
            cursor=cursor,
            settlement_start_time=settlement_start_time,
            settlement_end_time=settlement_end_time,
            order_id=order_id,
            size=size,
            order_complete_start_time=order_complete_start_time,
            order_complete_end_time=order_complete_end_time,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsSettledBillDetailResponse)

    def get_freight_insurance_list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_complete_time: Optional[int] = None,
        end_complete_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> FundsFreightInsuranceListResponse:
        """运费险列表。

        OpenAPI: `open.funds.financial.freight.insurance.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialFreightInsuranceListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialFreightInsuranceListRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_complete_time: 开始完成时间（毫秒时间戳）。
            end_complete_time: 结束完成时间（毫秒时间戳）。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsFreightInsuranceListResponse: 运费险列表响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsFreightInsuranceListRequest(
            access_token=access_token,
            cursor=cursor,
            start_complete_time=start_complete_time,
            end_complete_time=end_complete_time,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsFreightInsuranceListResponse)

    def get_pingan_bill(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        biz_type: Optional[list] = None,
        sub_mch_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsPinganBillResponse:
        """平安账单。

        OpenAPI: `open.funds.financial.pingan.bill` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialPinganBillRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialPinganBillRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            biz_type: 业务类型列表。
            sub_mch_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsPinganBillResponse: 平安账单响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsPinganBillRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            biz_type=biz_type,
            sub_mch_id=sub_mch_id,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsPinganBillResponse)

    def get_statement_list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        sub_mch_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsStatementListResponse:
        """对账单列表。

        OpenAPI: `open.funds.financial.statement.list` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsFinancialStatementListRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsFinancialStatementListRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标，用于分页。
            start_time: 开始时间（毫秒时间戳）。
            end_time: 结束时间（毫秒时间戳）。
            sub_mch_id: 子商户 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsStatementListResponse: 对账单列表响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsStatementListRequest(
            access_token=access_token,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            sub_mch_id=sub_mch_id,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsStatementListResponse)

    def apply_invoice(
        self,
        access_token: str,
        amount: int,
        relate_order_no: str,
        invoice_type: int,
        invoice_open_kind: int,
        electron_invoice_info_list: Optional[List[dict]] = None,
        tax_rate: Optional[str] = None,
        token: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> FundsApplyInvoiceResponse:
        """申请发票（非文件接口）。

        OpenAPI: `open.funds.subsidy.open.apply.invoice` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsSubsidyOpenApplyInvoiceRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsSubsidyOpenApplyInvoiceRequest.java`

        Args:
            access_token: 访问令牌。
            amount: 发票金额（分）。
            relate_order_no: 关联订单号。
            invoice_type: 发票类型。
            invoice_open_kind: 发票开具类型。
            electron_invoice_info_list: 电子发票明细列表。
            tax_rate: 税率。
            token: 防重放 token，可选。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsApplyInvoiceResponse: 申请结果。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsApplyInvoiceRequest(
            access_token=access_token,
            amount=amount,
            relate_order_no=relate_order_no,
            invoice_type=invoice_type,
            invoice_open_kind=invoice_open_kind,
            electron_invoice_info_list=electron_invoice_info_list,
            tax_rate=tax_rate,
            token=token,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsApplyInvoiceResponse)

    def audit_invoice_info(
        self,
        access_token: str,
        oid: str,
        uid: Optional[int] = None,
    ) -> FundsAuditInvoiceInfoResponse:
        """审核发票信息。

        OpenAPI: `open.funds.subsidy.audit.invoice.info` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsSubsidyAuditInvoiceInfoRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsSubsidyAuditInvoiceInfoRequest.java`

        Args:
            access_token: 访问令牌。
            oid: 订单 ID。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsAuditInvoiceInfoResponse: 审核发票信息响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsAuditInvoiceInfoRequest(
            access_token=access_token,
            oid=oid,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsAuditInvoiceInfoResponse)

    def apply_invoice_file(
        self,
        access_token: str,
        relate_order_no: str,
        invoice_open_kind: int,
        tax_rate: str,
        cert_no: str,
        invoice_name: str,
        invoice_open_date: int,
        count: int,
        goods: str,
        invoice_code: str,
        invoice_verify_code: str,
        invoice_tax: str,
        tax_authority_code: str,
        invoice_location_code: str,
        exclude_tax_amount: str,
        isv_code: str,
        invoice_no: str,
        uid: Optional[int] = None,
        # Note: invoice_bytes file upload parameter should be handled separately
    ) -> FundsApplyInvoiceFileResponse:
        """申请发票文件。

        OpenAPI: `open.funds.subsidy.open.apply.invoice.file` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.funds`
            `OpenFundsSubsidyOpenApplyInvoiceFileRequest`
        Java Source:
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/`
            `api/request/funds/OpenFundsSubsidyOpenApplyInvoiceFileRequest.java`

        Args:
            access_token: 访问令牌。
            relate_order_no: 关联订单号。
            invoice_open_kind: 发票开具类型。
            tax_rate: 税率。
            cert_no: 证书号。
            invoice_name: 发票名称。
            invoice_open_date: 发票开具日期（毫秒时间戳）。
            count: 数量。
            goods: 商品。
            invoice_code: 发票代码。
            invoice_verify_code: 发票验证码。
            invoice_tax: 发票税额。
            tax_authority_code: 税务机关代码。
            invoice_location_code: 发票所在地代码。
            exclude_tax_amount: 不含税金额。
            isv_code: ISV 代码。
            invoice_no: 发票号码。
            uid: 用户 ID，可选；保持作为最后一个可选参数。

        Returns:
            FundsApplyInvoiceFileResponse: 申请发票文件响应。

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法。
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = FundsApplyInvoiceFileRequest(
            access_token=access_token,
            relate_order_no=relate_order_no,
            invoice_open_kind=invoice_open_kind,
            tax_rate=tax_rate,
            cert_no=cert_no,
            invoice_name=invoice_name,
            invoice_open_date=invoice_open_date,
            count=count,
            goods=goods,
            invoice_code=invoice_code,
            invoice_verify_code=invoice_verify_code,
            invoice_tax=invoice_tax,
            tax_authority_code=tax_authority_code,
            invoice_location_code=invoice_location_code,
            exclude_tax_amount=exclude_tax_amount,
            isv_code=isv_code,
            invoice_no=invoice_no,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, FundsApplyInvoiceFileResponse)
