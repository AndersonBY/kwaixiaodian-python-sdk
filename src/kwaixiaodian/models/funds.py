"""资金管理相关数据模型"""

from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod, PagedResponse


class FundsBillType(int, Enum):
    """资金流水类型"""

    ALL = 0  # 全部
    INCOME = 1  # 收入
    EXPENSE = 2  # 支出
    REFUND = 3  # 退款
    WITHDRAWAL = 4  # 提现
    TRANSFER = 5  # 转账
    SETTLEMENT = 6  # 结算
    FEE = 7  # 手续费
    ADJUST = 8  # 调整
    BONUS = 9  # 奖励
    PENALTY = 10  # 罚金


class WithdrawType(int, Enum):
    """提现类型"""

    BANK_CARD = 1  # 银行卡提现
    ALIPAY = 2  # 支付宝提现
    WECHAT = 3  # 微信提现


class WithdrawStatus(int, Enum):
    """提现状态"""

    PENDING = 1  # 待处理
    PROCESSING = 2  # 处理中
    SUCCESS = 3  # 成功
    FAILED = 4  # 失败
    CANCELLED = 5  # 已取消


class AccountType(int, Enum):
    """账户类型"""

    MAIN = 1  # 主账户
    SETTLEMENT = 2  # 结算账户
    FREEZE = 3  # 冻结账户
    BONUS = 4  # 奖励账户


class FundsTransactionType(int, Enum):
    """资金交易类型"""

    ORDER_PAYMENT = 1  # 订单支付
    ORDER_REFUND = 2  # 订单退款
    WITHDRAW = 3  # 提现
    DEPOSIT = 4  # 充值
    TRANSFER_IN = 5  # 转入
    TRANSFER_OUT = 6  # 转出
    FEE_DEDUCTION = 7  # 手续费扣除
    SETTLEMENT = 8  # 结算
    ADJUSTMENT = 9  # 调整
    BONUS_REWARD = 10  # 奖励发放
    PENALTY_DEDUCTION = 11  # 罚金扣除


# ==================== 基础数据模型 ====================


class AccountInfo(BaseModel):
    """账户资金信息"""

    # 基本信息
    account_id: str = Field(description="账户ID")
    account_type: AccountType = Field(description="账户类型")
    account_name: str = Field(description="账户名称")

    # 余额信息（以分为单位）
    available_amount: int = Field(description="可用余额（分）")
    frozen_amount: int = Field(description="冻结余额（分）")
    total_amount: int = Field(description="总余额（分）")

    # 累计信息
    total_income: int = Field(description="累计收入（分）")
    total_expense: int = Field(description="累计支出（分）")
    total_withdraw: int = Field(description="累计提现（分）")

    # 时间信息
    create_time: str = Field(description="账户创建时间")
    update_time: str = Field(description="最后更新时间")

    # 其他信息
    currency: str = Field(default="CNY", description="货币类型")
    status: int = Field(description="账户状态")

    @property
    def available_yuan(self) -> float:
        """可用余额（元）"""
        return self.available_amount / 100

    @property
    def frozen_yuan(self) -> float:
        """冻结余额（元）"""
        return self.frozen_amount / 100

    @property
    def total_yuan(self) -> float:
        """总余额（元）"""
        return self.total_amount / 100

    @property
    def total_income_yuan(self) -> float:
        """累计收入（元）"""
        return self.total_income / 100

    @property
    def total_expense_yuan(self) -> float:
        """累计支出（元）"""
        return self.total_expense / 100

    @property
    def total_withdraw_yuan(self) -> float:
        """累计提现（元）"""
        return self.total_withdraw / 100


class BillRecord(BaseModel):
    """资金流水记录"""

    # 基本信息
    bill_id: str = Field(description="流水ID")
    bill_no: str = Field(description="流水号")
    out_bill_no: Optional[str] = Field(default=None, description="外部流水号")

    # 交易信息
    transaction_type: FundsTransactionType = Field(description="交易类型")
    bill_type: FundsBillType = Field(description="流水类型")
    amount: int = Field(description="交易金额（分）")
    balance_after: int = Field(description="交易后余额（分）")

    # 关联信息
    order_id: Optional[str] = Field(default=None, description="关联订单ID")
    payment_id: Optional[str] = Field(default=None, description="关联支付ID")
    refund_id: Optional[str] = Field(default=None, description="关联退款ID")

    # 描述信息
    title: str = Field(description="交易标题")
    description: Optional[str] = Field(default=None, description="交易描述")

    # 时间信息
    create_time: str = Field(description="创建时间")
    transaction_time: str = Field(description="交易时间")

    # 其他信息
    fee_amount: Optional[int] = Field(default=None, description="手续费（分）")
    currency: str = Field(default="CNY", description="货币类型")
    status: int = Field(description="流水状态")

    @property
    def amount_yuan(self) -> float:
        """交易金额（元）"""
        return self.amount / 100

    @property
    def balance_after_yuan(self) -> float:
        """交易后余额（元）"""
        return self.balance_after / 100

    @property
    def fee_yuan(self) -> Optional[float]:
        """手续费（元）"""
        return self.fee_amount / 100 if self.fee_amount else None

    @property
    def is_income(self) -> bool:
        """是否为收入"""
        return self.amount > 0

    @property
    def is_expense(self) -> bool:
        """是否为支出"""
        return self.amount < 0


class WithdrawRecord(BaseModel):
    """提现记录"""

    # 基本信息
    withdraw_id: str = Field(description="提现ID")
    withdraw_no: str = Field(description="提现单号")
    out_withdraw_no: Optional[str] = Field(default=None, description="外部提现单号")

    # 提现信息
    withdraw_type: WithdrawType = Field(description="提现类型")
    withdraw_amount: int = Field(description="提现金额（分）")
    actual_amount: Optional[int] = Field(default=None, description="实际到账金额（分）")
    fee_amount: Optional[int] = Field(default=None, description="手续费（分）")

    # 状态信息
    withdraw_status: WithdrawStatus = Field(description="提现状态")

    # 收款信息
    bank_name: Optional[str] = Field(default=None, description="银行名称")
    bank_account: Optional[str] = Field(default=None, description="银行账号")
    account_holder: Optional[str] = Field(default=None, description="开户人姓名")

    # 时间信息
    apply_time: str = Field(description="申请时间")
    process_time: Optional[str] = Field(default=None, description="处理时间")
    finish_time: Optional[str] = Field(default=None, description="完成时间")

    # 其他信息
    remark: Optional[str] = Field(default=None, description="备注信息")
    reject_reason: Optional[str] = Field(default=None, description="拒绝原因")
    currency: str = Field(default="CNY", description="货币类型")

    @property
    def withdraw_yuan(self) -> float:
        """提现金额（元）"""
        return self.withdraw_amount / 100

    @property
    def actual_yuan(self) -> Optional[float]:
        """实际到账金额（元）"""
        return self.actual_amount / 100 if self.actual_amount else None

    @property
    def fee_yuan(self) -> Optional[float]:
        """手续费（元）"""
        return self.fee_amount / 100 if self.fee_amount else None

    @property
    def is_success(self) -> bool:
        """是否提现成功"""
        return self.withdraw_status == WithdrawStatus.SUCCESS

    @property
    def is_processing(self) -> bool:
        """是否处理中"""
        return self.withdraw_status in [
            WithdrawStatus.PENDING,
            WithdrawStatus.PROCESSING,
        ]


class SettlementRecord(BaseModel):
    """结算记录"""

    # 基本信息
    settlement_id: str = Field(description="结算ID")
    settlement_no: str = Field(description="结算单号")

    # 结算信息
    settlement_amount: int = Field(description="结算金额（分）")
    fee_amount: int = Field(description="手续费（分）")
    actual_amount: int = Field(description="实际金额（分）")

    # 时间范围
    begin_time: str = Field(description="结算开始时间")
    end_time: str = Field(description="结算结束时间")
    settlement_time: str = Field(description="结算时间")

    # 统计信息
    order_count: int = Field(description="订单数量")
    refund_count: int = Field(description="退款数量")
    total_order_amount: int = Field(description="订单总金额（分）")
    total_refund_amount: int = Field(description="退款总金额（分）")

    # 其他信息
    currency: str = Field(default="CNY", description="货币类型")
    status: int = Field(description="结算状态")

    @property
    def settlement_yuan(self) -> float:
        """结算金额（元）"""
        return self.settlement_amount / 100

    @property
    def fee_yuan(self) -> float:
        """手续费（元）"""
        return self.fee_amount / 100

    @property
    def actual_yuan(self) -> float:
        """实际金额（元）"""
        return self.actual_amount / 100

    @property
    def total_order_yuan(self) -> float:
        """订单总金额（元）"""
        return self.total_order_amount / 100

    @property
    def total_refund_yuan(self) -> float:
        """退款总金额（元）"""
        return self.total_refund_amount / 100


class FundsStats(BaseModel):
    """资金统计信息"""

    # 时间范围
    begin_date: str = Field(description="开始日期")
    end_date: str = Field(description="结束日期")

    # 收入统计
    total_income: int = Field(description="总收入（分）")
    order_income: int = Field(description="订单收入（分）")
    other_income: int = Field(description="其他收入（分）")

    # 支出统计
    total_expense: int = Field(description="总支出（分）")
    refund_expense: int = Field(description="退款支出（分）")
    fee_expense: int = Field(description="手续费支出（分）")
    withdraw_expense: int = Field(description="提现支出（分）")

    # 净收益
    net_income: int = Field(description="净收益（分）")

    # 交易统计
    transaction_count: int = Field(description="交易笔数")
    income_count: int = Field(description="收入笔数")
    expense_count: int = Field(description="支出笔数")

    @property
    def total_income_yuan(self) -> float:
        """总收入（元）"""
        return self.total_income / 100

    @property
    def order_income_yuan(self) -> float:
        """订单收入（元）"""
        return self.order_income / 100

    @property
    def other_income_yuan(self) -> float:
        """其他收入（元）"""
        return self.other_income / 100

    @property
    def total_expense_yuan(self) -> float:
        """总支出（元）"""
        return self.total_expense / 100

    @property
    def refund_expense_yuan(self) -> float:
        """退款支出（元）"""
        return self.refund_expense / 100

    @property
    def fee_expense_yuan(self) -> float:
        """手续费支出（元）"""
        return self.fee_expense / 100

    @property
    def withdraw_expense_yuan(self) -> float:
        """提现支出（元）"""
        return self.withdraw_expense / 100

    @property
    def net_income_yuan(self) -> float:
        """净收益（元）"""
        return self.net_income / 100


# ==================== 账户信息查询 ====================


class FundsAccountInfoRequest(BaseRequest):
    """获取账户资金信息请求（Java: OpenFundsCenterAccountInfoRequest）"""

    @property
    def api_method(self) -> str:
        return "open.funds.center.account.info"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class FundsAccountInfoResponse(BaseResponse[AccountInfo]):
    """获取账户资金信息响应"""

    pass


# ==================== 资金流水查询 ====================


## Java reference lacks open.funds.bill.list; removed.


# ==================== 提现申请 ====================


class FundsWithdrawApplyRequest(BaseRequest):
    """申请提现请求（Java: OpenFundsCenterWithdrawApplyRequest）"""

    withdraw_money: int = Field(
        description="提现金额（分）", gt=0, alias="withdrawMoney"
    )
    withdraw_no: Optional[str] = Field(
        default=None, description="提现单号", alias="withdrawNo"
    )
    remark: Optional[str] = Field(default=None, description="备注信息", alias="remark")
    account_channel: Optional[int] = Field(
        default=None, description="出账通道", alias="accountChannel"
    )
    sub_merchant_id: Optional[str] = Field(
        default=None, description="子商户ID", alias="subMerchantId"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.center.withdraw.apply"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class FundsWithdrawApplyResponse(BaseResponse[Dict[str, Any]]):
    """申请提现响应"""

    pass


# ==================== 提现记录查询 ====================


class FundsWithdrawRecordRequest(BaseRequest):
    """提现记录列表请求（Java: OpenFundsCenterWirhdrawRecordListRequest）"""

    limit: Optional[int] = Field(default=None, description="每页大小", alias="limit")
    page: Optional[int] = Field(default=None, description="页码", alias="page")
    create_time_start: Optional[int] = Field(
        default=None, description="开始时间", alias="createTimeStart"
    )
    create_time_end: Optional[int] = Field(
        default=None, description="结束时间", alias="createTimeEnd"
    )
    account_channel: Optional[int] = Field(
        default=None, description="出账通道", alias="accountChannel"
    )
    sub_merchant_id: Optional[str] = Field(
        default=None, description="子商户ID", alias="subMerchantId"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.center.wirhdraw.record.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class FundsWithdrawRecordResponse(PagedResponse[WithdrawRecord]):
    """获取提现记录响应"""

    pass


# ==================== 提现状态查询 ====================


class FundsWithdrawQueryRequest(BaseRequest):
    """查询提现状态请求（Java: OpenFundsCenterGetWithdrawResultRequest）"""

    withdraw_no: str = Field(description="提现单号", alias="withdrawNo")

    @property
    def api_method(self) -> str:
        return "open.funds.center.get.withdraw.result"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class FundsWithdrawQueryResponse(BaseResponse[WithdrawRecord]):
    """查询提现状态响应"""

    pass


# ==================== 结算记录查询 ====================


## Java reference lacks open.funds.settlement.list; removed.


# ==================== 资金统计查询 ====================


## Java reference lacks open.funds.stats; removed.


# ==================== 余额变动通知 ====================


class FundsBalanceNotification(BaseModel):
    """余额变动通知"""

    account_id: str = Field(description="账户ID")
    bill_id: str = Field(description="流水ID")
    transaction_type: FundsTransactionType = Field(description="交易类型")
    amount: int = Field(description="变动金额（分）")
    balance_before: int = Field(description="变动前余额（分）")
    balance_after: int = Field(description="变动后余额（分）")
    order_id: Optional[str] = Field(default=None, description="关联订单ID")
    transaction_time: str = Field(description="交易时间")
    sign: str = Field(description="签名")

    @property
    def amount_yuan(self) -> float:
        """变动金额（元）"""
        return self.amount / 100

    @property
    def balance_before_yuan(self) -> float:
        """变动前余额（元）"""
        return self.balance_before / 100

    @property
    def balance_after_yuan(self) -> float:
        """变动后余额（元）"""
        return self.balance_after / 100


class FundsWithdrawNotification(BaseModel):
    """提现状态通知"""

    withdraw_id: str = Field(description="提现ID")
    withdraw_no: str = Field(description="提现单号")
    withdraw_status: WithdrawStatus = Field(description="提现状态")
    withdraw_amount: int = Field(description="提现金额（分）")
    actual_amount: Optional[int] = Field(default=None, description="实际到账金额（分）")
    fee_amount: Optional[int] = Field(default=None, description="手续费（分）")
    finish_time: Optional[str] = Field(default=None, description="完成时间")
    reject_reason: Optional[str] = Field(default=None, description="拒绝原因")
    sign: str = Field(description="签名")

    @property
    def withdraw_yuan(self) -> float:
        """提现金额（元）"""
        return self.withdraw_amount / 100

    @property
    def actual_yuan(self) -> Optional[float]:
        """实际到账金额（元）"""
        return self.actual_amount / 100 if self.actual_amount else None

    @property
    def fee_yuan(self) -> Optional[float]:
        """手续费（元）"""
        return self.fee_amount / 100 if self.fee_amount else None


## Note: 日账单查询见下方 FundsDailyBillRequest/Response 定义


# ==================== 保证金管理 ====================


class FundsDepositInfoRequest(BaseRequest):
    """保证金信息请求"""

    # Based on Java SDK: OpenFundsCenterGetDepositinfoRequest
    security_deposit_type: Optional[int] = Field(
        default=None, description="保证金类型", alias="securityDepositType"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.center.get.depositinfo"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DepositInfo(BaseModel):
    """保证金信息"""

    deposit_type: str = Field(description="保证金类型")
    deposit_amount: int = Field(description="保证金金额（分）")
    available_amount: int = Field(description="可用金额（分）")
    frozen_amount: int = Field(description="冻结金额（分）")
    status: str = Field(description="状态")

    @property
    def deposit_yuan(self) -> float:
        """保证金金额（元）"""
        return self.deposit_amount / 100

    @property
    def available_yuan(self) -> float:
        """可用金额（元）"""
        return self.available_amount / 100

    @property
    def frozen_yuan(self) -> float:
        """冻结金额（元）"""
        return self.frozen_amount / 100


class FundsDepositInfoResponse(BaseResponse[List[DepositInfo]]):
    """保证金信息响应"""

    pass


class FundsDepositRecordRequest(BaseRequest):
    """保证金记录请求"""

    # Based on Java SDK: OpenFundsCenterGetDepositrecordRequest
    start_time: Optional[int] = Field(
        default=None, description="开始时间", alias="startTime"
    )
    size: Optional[int] = Field(default=None, description="每页大小", alias="size")
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    page: Optional[int] = Field(default=None, description="页码", alias="page")
    deposit_type: Optional[int] = Field(
        default=None, description="保证金类型", alias="depositType"
    )
    operator_types: Optional[int] = Field(
        default=None, description="操作类型", alias="operatorTypes"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.center.get.depositrecord"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DepositRecord(BaseModel):
    """保证金记录"""

    record_id: str = Field(description="记录ID")
    deposit_type: str = Field(description="保证金类型")
    operation_type: str = Field(description="操作类型")
    amount: int = Field(description="金额（分）")
    balance: int = Field(description="余额（分）")
    operation_time: str = Field(description="操作时间")
    description: Optional[str] = Field(default=None, description="描述")

    @property
    def amount_yuan(self) -> float:
        """金额（元）"""
        return self.amount / 100

    @property
    def balance_yuan(self) -> float:
        """余额（元）"""
        return self.balance / 100


class FundsDepositRecordResponse(PagedResponse[DepositRecord]):
    """保证金记录响应"""

    pass


# ==================== 日账单相关 ====================


class FundsDailyBillRequest(BaseRequest):
    """获取日账单请求（Java: OpenFundsCenterGetDailyBillRequest）"""

    bill_date: str = Field(description="账单日期", alias="billDate")
    bill_type: Optional[str] = Field(
        default=None, description="账单类型", alias="billType"
    )
    expire_date: Optional[int] = Field(
        default=None, description="过期日期", alias="expireDate"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.center.get.daily.bill"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DailyBillInfo(BaseModel):
    """日账单信息"""

    bill_date: str = Field(description="账单日期", alias="billDate")
    bill_type: str = Field(description="账单类型", alias="billType")
    total_amount: int = Field(description="总金额（分）")
    details: List[Dict[str, Any]] = Field(description="账单详情")

    @property
    def total_yuan(self) -> float:
        """总金额（元）"""
        return self.total_amount / 100


class FundsDailyBillResponse(BaseResponse[DailyBillInfo]):
    """获取日账单响应"""

    pass


# ==================== 批量账单详情相关 ====================


class FundsBillBatchDetailRequest(BaseRequest):
    """批量账单详情请求（Java: OpenFundsFinancialBillBatchDetailRequest）"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    settlement_end_time: Optional[int] = Field(
        default=None, description="结算结束时间", alias="settlementEndTime"
    )
    settlement_start_time: Optional[int] = Field(
        default=None, description="结算开始时间", alias="settlementStartTime"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.bill.batch.detail"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class BatchBillDetail(BaseModel):
    """批量账单详情"""

    bill_id: str = Field(description="账单ID")
    settlement_time: int = Field(description="结算时间")
    amount: int = Field(description="金额（分）")
    details: Dict[str, Any] = Field(description="详情信息")

    @property
    def amount_yuan(self) -> float:
        """金额（元）"""
        return self.amount / 100


class FundsBillBatchDetailResponse(BaseResponse[List[BatchBillDetail]]):
    """批量账单详情响应"""

    pass


# ==================== 售后账单列表相关 ====================


class FundsPostSalesBillListRequest(BaseRequest):
    """售后账单列表请求（Java: OpenFundsFinancialBillPostSalesListRequest）"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    start_time: Optional[int] = Field(
        default=None, description="开始时间", alias="startTime"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.bill.post.sales.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PostSalesBillInfo(BaseModel):
    """售后账单信息"""

    bill_id: str = Field(description="账单ID")
    order_id: str = Field(description="订单ID")
    amount: int = Field(description="金额（分）")
    bill_time: int = Field(description="账单时间")
    bill_type: str = Field(description="账单类型")

    @property
    def amount_yuan(self) -> float:
        """金额（元）"""
        return self.amount / 100


class FundsPostSalesBillListResponse(BaseResponse[List[PostSalesBillInfo]]):
    """售后账单列表响应"""

    pass


# ==================== 查询账户账单相关 ====================


class FundsQueryAccountBillRequest(BaseRequest):
    """查询账户账单请求（Java: OpenFundsFinancialBillQueryAccountRequest）"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    start_time: Optional[int] = Field(
        default=None, description="开始时间", alias="startTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    role_type: Optional[str] = Field(
        default=None, description="角色类型", alias="roleType"
    )
    biz_type: Optional[List[str]] = Field(
        default=None, description="业务类型列表", alias="bizType"
    )
    wallet_type: Optional[str] = Field(
        default=None, description="钱包类型", alias="walletType"
    )
    sub_mch_id: Optional[str] = Field(
        default=None, description="子商户ID", alias="subMchId"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.bill.query.account"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class AccountBillInfo(BaseModel):
    """账户账单信息"""

    bill_id: str = Field(description="账单ID")
    account_type: str = Field(description="账户类型")
    biz_type: str = Field(description="业务类型")
    amount: int = Field(description="金额（分）")
    balance: int = Field(description="余额（分）")
    bill_time: int = Field(description="账单时间")

    @property
    def amount_yuan(self) -> float:
        """金额（元）"""
        return self.amount / 100

    @property
    def balance_yuan(self) -> float:
        """余额（元）"""
        return self.balance / 100


class FundsQueryAccountBillResponse(BaseResponse[List[AccountBillInfo]]):
    """查询账户账单响应"""

    pass


# ==================== 结算账单详情相关 ====================


class FundsSettledBillDetailRequest(BaseRequest):
    """结算账单详情请求（Java: OpenFundsFinancialSettledBillDetailRequest, GET）"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    settlement_start_time: Optional[int] = Field(
        default=None, description="结算开始时间", alias="settlementStartTime"
    )
    settlement_end_time: Optional[int] = Field(
        default=None, description="结算结束时间", alias="settlementEndTime"
    )
    order_id: Optional[int] = Field(default=None, description="订单ID", alias="orderId")
    size: Optional[int] = Field(default=None, description="分页大小", alias="size")
    order_complete_start_time: Optional[int] = Field(
        default=None, description="订单完成开始时间", alias="orderCompleteStartTime"
    )
    order_complete_end_time: Optional[int] = Field(
        default=None, description="订单完成结束时间", alias="orderCompleteEndTime"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.settled.bill.detail"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class GeneralRefundInfo(BaseModel):
    """退款信息（Java: GeneralRefundInfo，金额字段以分为单位，字符串或长整型）"""

    platform_allowance_refund: Optional[int] = Field(
        default=None, alias="platformAllowanceRefund"
    )
    actual_pay_refund: Optional[int] = Field(default=None, alias="actualPayRefund")
    refund_id: Optional[int] = Field(default=None, alias="refundId")
    platform_pay_market_allowance_refund: Optional[int] = Field(
        default=None, alias="platformPayMarketAllowanceRefund"
    )


class GeneralOrderBillDetail(BaseModel):
    """订单账单详情（Java: GeneralOrderBillDetail）

    仅映射代表性字段，完全对齐 Java 字段命名（alias）。
    金额类部分字段在 Java 为字符串，保持字符串以避免精度误差；整型金额字段使用 int。
    """

    order_no: Optional[int] = Field(default=None, alias="orderNo")
    product_id: Optional[str] = Field(default=None, alias="productId")
    product_name: Optional[str] = Field(default=None, alias="productName")
    product_num: Optional[int] = Field(default=None, alias="productNum")
    order_create_time: Optional[str] = Field(default=None, alias="orderCreateTime")
    actual_pay_amount: Optional[str] = Field(default=None, alias="actualPayAmount")
    platform_allowance_amount: Optional[str] = Field(
        default=None, alias="platformAllowanceAmount"
    )
    total_income: Optional[str] = Field(default=None, alias="totalIncome")
    total_refund_amount: Optional[str] = Field(default=None, alias="totalRefundAmount")
    platform_commission_amount: Optional[str] = Field(
        default=None, alias="platformCommissionAmount"
    )
    distributor_id: Optional[str] = Field(default=None, alias="distributorId")
    distributor_commission_amount: Optional[str] = Field(
        default=None, alias="distributorCommissionAmount"
    )
    activity_user_id: Optional[str] = Field(default=None, alias="activityUserId")
    activity_user_commission_amount: Optional[str] = Field(
        default=None, alias="activityUserCommissionAmount"
    )
    collect_mode: Optional[str] = Field(default=None, alias="collectMode")
    kzk_id: Optional[str] = Field(default=None, alias="kzkId")
    kzk_commission_amount: Optional[str] = Field(
        default=None, alias="kzkCommissionAmount"
    )
    service_user_id: Optional[str] = Field(default=None, alias="serviceUserId")
    service_amount: Optional[str] = Field(default=None, alias="serviceAmount")
    service_commission_role: Optional[str] = Field(
        default=None, alias="serviceCommissionRole"
    )
    total_outgoing_amount: Optional[str] = Field(
        default=None, alias="totalOutgoingAmount"
    )
    settlement_status: Optional[str] = Field(default=None, alias="settlementStatus")
    settlement_amount: Optional[str] = Field(default=None, alias="settlementAmount")
    settlement_time: Optional[str] = Field(default=None, alias="settlementTime")
    settlement_rule: Optional[str] = Field(default=None, alias="settlementRule")
    account_channel: Optional[str] = Field(default=None, alias="accountChannel")
    account_name: Optional[str] = Field(default=None, alias="accountName")
    merchant_id: Optional[str] = Field(default=None, alias="merchantId")
    order_remark: Optional[str] = Field(default=None, alias="orderRemark")
    czj_amount: Optional[str] = Field(default=None, alias="czjAmount")
    refund_info: Optional[List[GeneralRefundInfo]] = Field(
        default=None, alias="refundInfo"
    )
    other_amount: Optional[int] = Field(default=None, alias="otherAmount")
    other_amount_detail: Optional[str] = Field(default=None, alias="otherAmountDetail")
    mcn_id: Optional[str] = Field(default=None, alias="mcnId")
    other_amount_desc: Optional[str] = Field(default=None, alias="otherAmountDesc")
    platform_pay_market_allowance_amount: Optional[int] = Field(
        default=None, alias="platformPayMarketAllowanceAmount"
    )
    government_subsidy_amount: Optional[int] = Field(
        default=None, alias="governmentSubsidyAmount"
    )
    presell_settle_amount: Optional[int] = Field(
        default=None, alias="presellSettleAmount"
    )

    # -------- Decimal helpers for string money fields (non-breaking) --------
    @property
    def actual_pay_amount_decimal(self) -> Optional[Decimal]:
        v = self.actual_pay_amount
        return Decimal(v) if v is not None else None

    @property
    def platform_allowance_amount_decimal(self) -> Optional[Decimal]:
        v = self.platform_allowance_amount
        return Decimal(v) if v is not None else None

    @property
    def total_income_decimal(self) -> Optional[Decimal]:
        v = self.total_income
        return Decimal(v) if v is not None else None

    @property
    def total_refund_amount_decimal(self) -> Optional[Decimal]:
        v = self.total_refund_amount
        return Decimal(v) if v is not None else None

    @property
    def platform_commission_amount_decimal(self) -> Optional[Decimal]:
        v = self.platform_commission_amount
        return Decimal(v) if v is not None else None

    @property
    def distributor_commission_amount_decimal(self) -> Optional[Decimal]:
        v = self.distributor_commission_amount
        return Decimal(v) if v is not None else None

    @property
    def service_amount_decimal(self) -> Optional[Decimal]:
        v = self.service_amount
        return Decimal(v) if v is not None else None

    @property
    def settlement_amount_decimal(self) -> Optional[Decimal]:
        v = self.settlement_amount
        return Decimal(v) if v is not None else None

    @property
    def total_outgoing_amount_decimal(self) -> Optional[Decimal]:
        v = self.total_outgoing_amount
        return Decimal(v) if v is not None else None


class OrderBillDetailPageData(BaseModel):
    """结算账单详情分页数据（Java: OpenApiQueryOrderBillDetailResponse）"""

    orders: Optional[List[GeneralOrderBillDetail]] = Field(default=None, alias="orders")
    cursor: Optional[str] = Field(default=None, alias="cursor")


class FundsSettledBillDetailResponse(BaseResponse[OrderBillDetailPageData]):
    """结算账单详情响应（类型化，Java对齐）"""

    pass


# ==================== 运费险列表相关 ====================


class FundsFreightInsuranceListRequest(BaseRequest):
    """运费险列表请求"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    start_complete_time: Optional[int] = Field(
        default=None, description="开始完成时间", alias="startCompleteTime"
    )
    end_complete_time: Optional[int] = Field(
        default=None, description="结束完成时间", alias="endCompleteTime"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.freight.insurance.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class FreightInsuranceInfo(BaseModel):
    """运费险信息"""

    insurance_id: str = Field(description="保险ID")
    order_id: str = Field(description="订单ID")
    insurance_amount: int = Field(description="保险金额（分）")
    complete_time: int = Field(description="完成时间")
    status: str = Field(description="状态")

    @property
    def insurance_yuan(self) -> float:
        """保险金额（元）"""
        return self.insurance_amount / 100


class FundsFreightInsuranceListResponse(BaseResponse[List[FreightInsuranceInfo]]):
    """运费险列表响应"""

    pass


# ==================== 平安账单相关 ====================


class FundsPinganBillRequest(BaseRequest):
    """平安账单请求"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    start_time: Optional[int] = Field(
        default=None, description="开始时间", alias="startTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    biz_type: Optional[List[str]] = Field(
        default=None, description="业务类型列表", alias="bizType"
    )
    sub_mch_id: Optional[str] = Field(
        default=None, description="子商户ID", alias="subMchId"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.pingan.bill"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PinganBillInfo(BaseModel):
    """平安账单信息"""

    bill_id: str = Field(description="账单ID")
    biz_type: str = Field(description="业务类型")
    amount: int = Field(description="金额（分）")
    bill_time: int = Field(description="账单时间")
    sub_mch_id: Optional[str] = Field(default=None, description="子商户ID")

    @property
    def amount_yuan(self) -> float:
        """金额（元）"""
        return self.amount / 100


class FundsPinganBillResponse(BaseResponse[List[PinganBillInfo]]):
    """平安账单响应"""

    pass


# ==================== 账单列表查询（financial.query.bill.list） ====================


class FundsFinancialQueryBillListRequest(BaseRequest):
    """资金财务账单列表（open.funds.financial.query.bill.list, GET）"""

    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    scroll_id: Optional[str] = Field(
        default=None, description="滚动游标ID", alias="scrollId"
    )
    order_status: Optional[int] = Field(
        default=None, description="订单状态", alias="orderStatus"
    )
    start_time: Optional[int] = Field(
        default=None, description="开始时间", alias="startTime"
    )
    bill_type: Optional[str] = Field(
        default=None, description="账单类型", alias="billType"
    )
    account_channel: Optional[List[str]] = Field(
        default=None, description="出入账渠道", alias="accountChannel"
    )

    @property
    def api_method(self) -> str:  # Java: OpenFundsFinancialQueryBillListRequest
        return "open.funds.financial.query.bill.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistributorSettledOrderItem(BaseModel):
    """Java: AppDistributorSettledOrderSearchAfterData（代表性字段）"""

    order_no: Optional[int] = Field(default=None, alias="orderNo")
    account_type: Optional[str] = Field(default=None, alias="accountType")
    user_id: Optional[int] = Field(default=None, alias="userId")
    distributor_id: Optional[int] = Field(default=None, alias="distributorId")
    product_id: Optional[str] = Field(default=None, alias="productId")
    product_name: Optional[str] = Field(default=None, alias="productName")
    order_time: Optional[str] = Field(default=None, alias="orderTime")
    settlement_time: Optional[str] = Field(default=None, alias="settlementTime")
    actual_pay_amount: Optional[str] = Field(default=None, alias="actualPayAmount")
    distributor_commission_amount: Optional[str] = Field(
        default=None, alias="distributorCommissionAmount"
    )
    mcn_commission_amount: Optional[str] = Field(
        default=None, alias="mcnCommissionAmount"
    )
    platform_allowance_amount: Optional[str] = Field(
        default=None, alias="platformAllowanceAmount"
    )
    government_subsidy_amount: Optional[str] = Field(
        default=None, alias="governmentSubsidyAmount"
    )
    service_amount: Optional[str] = Field(default=None, alias="serviceAmount")
    czj_amount: Optional[str] = Field(default=None, alias="czjAmount")
    kzk_amount: Optional[str] = Field(default=None, alias="kzkAmount")
    distributor_commission_rate: Optional[str] = Field(
        default=None, alias="distributorCommissionRate"
    )
    account_channel: Optional[str] = Field(default=None, alias="accountChannel")


class DistributorUnSettledOrderItem(BaseModel):
    """Java: AppDistributorUnSettledOrderSearchAfterData（代表性字段）"""

    order_no: Optional[int] = Field(default=None, alias="orderNo")
    user_id: Optional[int] = Field(default=None, alias="userId")
    distributor_id: Optional[int] = Field(default=None, alias="distributorId")
    product_id: Optional[str] = Field(default=None, alias="productId")
    product_name: Optional[str] = Field(default=None, alias="productName")
    order_time: Optional[str] = Field(default=None, alias="orderTime")
    expect_settlement_time: Optional[str] = Field(
        default=None, alias="expectSettlementTime"
    )
    actual_pay_amount: Optional[str] = Field(default=None, alias="actualPayAmount")
    distributor_commission_amount: Optional[str] = Field(
        default=None, alias="distributorCommissionAmount"
    )
    mcn_commission_amount: Optional[str] = Field(
        default=None, alias="mcnCommissionAmount"
    )
    platform_amount: Optional[str] = Field(default=None, alias="platformAmount")
    platform_allowance_amount: Optional[str] = Field(
        default=None, alias="platformAllowanceAmount"
    )
    government_subsidy_amount: Optional[str] = Field(
        default=None, alias="governmentSubsidyAmount"
    )
    service_amount: Optional[str] = Field(default=None, alias="serviceAmount")
    czj_amount: Optional[str] = Field(default=None, alias="czjAmount")
    kzk_amount: Optional[str] = Field(default=None, alias="kzkAmount")
    distributor_commission_rate: Optional[str] = Field(
        default=None, alias="distributorCommissionRate"
    )


class DistributorSettledOrderBillListDTO(BaseModel):
    """Java: DistributorSettledOrderBillListDTO"""

    data: Optional[List[DistributorSettledOrderItem]] = Field(
        default=None, alias="data"
    )


class DistributorUnSettledOrderBillListDTO(BaseModel):
    """Java: DistributorUnSettledOrderBillListDTO"""

    data: Optional[List[DistributorUnSettledOrderItem]] = Field(
        default=None, alias="data"
    )


class FundsFinancialBillListData(BaseModel):
    """开放平台财务账单列表数据（Java对齐字段）"""

    total: Optional[int] = Field(default=None, alias="total")
    scroll_id: Optional[str] = Field(default=None, alias="scrollId")
    distributor_settled_order_data: Optional[DistributorSettledOrderBillListDTO] = (
        Field(default=None, alias="distributorSettledOrderData")
    )
    distributor_unsettled_order_data: Optional[DistributorUnSettledOrderBillListDTO] = (
        Field(default=None, alias="distributorUnSettledOrderData")
    )


class FundsFinancialQueryBillListResponse(BaseResponse[FundsFinancialBillListData]):
    """资金财务账单列表响应（类型化，Java对齐）"""

    pass


# ==================== 审核发票信息相关 ====================


class FundsAuditInvoiceInfoRequest(BaseRequest):
    """审核发票信息请求"""

    oid: str = Field(description="订单ID", alias="oid")

    @property
    def api_method(self) -> str:
        return "open.funds.subsidy.audit.invoice.info"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class InvoiceAuditInfo(BaseModel):
    """发票审核信息"""

    oid: str = Field(description="订单ID")
    audit_status: str = Field(description="审核状态")
    audit_result: Optional[str] = Field(default=None, description="审核结果")
    audit_time: Optional[int] = Field(default=None, description="审核时间")


class FundsAuditInvoiceInfoResponse(BaseResponse[InvoiceAuditInfo]):
    """审核发票信息响应"""

    pass


# ==================== 申请发票（非文件） ====================


class InvoiceDetailInfo(BaseModel):
    """发票明细信息（Java: InvoiceDetailInfoProto）"""

    amount: Optional[int] = Field(default=None, alias="amount")
    cert_no: Optional[str] = Field(default=None, alias="certNo")
    invoice_location_code: Optional[str] = Field(
        default=None, alias="invoiceLocationCode"
    )
    file_name: Optional[str] = Field(default=None, alias="fileName")
    invoice_no: Optional[str] = Field(default=None, alias="invoiceNo")
    invoice_open_date: Optional[int] = Field(default=None, alias="invoiceOpenDate")
    tax_authority_code: Optional[str] = Field(default=None, alias="taxAuthorityCode")
    count: Optional[int] = Field(default=None, alias="count")
    goods: Optional[str] = Field(default=None, alias="goods")
    invoice_code: Optional[str] = Field(default=None, alias="invoiceCode")
    file_key: Optional[str] = Field(default=None, alias="fileKey")
    invoice_forever_url: Optional[str] = Field(default=None, alias="invoiceForeverUrl")
    exclude_tax_amount: Optional[str] = Field(default=None, alias="excludeTaxAmount")
    invoice_verify_code: Optional[str] = Field(default=None, alias="invoiceVerifyCode")
    safe_file_key: Optional[str] = Field(default=None, alias="safeFileKey")
    invoice_tax: Optional[str] = Field(default=None, alias="invoiceTax")


class FundsApplyInvoiceRequest(BaseRequest):
    """申请发票请求（Java: OpenFundsSubsidyOpenApplyInvoiceRequest）"""

    amount: int = Field(description="金额（分）", alias="amount")
    relate_order_no: str = Field(description="关联订单号", alias="relateOrderNo")
    invoice_type: int = Field(description="发票类型", alias="invoiceType")
    invoice_open_kind: int = Field(description="发票开具类型", alias="invoiceOpenKind")
    electron_invoice_info_list: Optional[List[InvoiceDetailInfo]] = Field(
        default=None, alias="electronInvoiceInfoList"
    )
    tax_rate: Optional[str] = Field(default=None, alias="taxRate")
    token: Optional[str] = Field(default=None, alias="token")

    @property
    def api_method(self) -> str:
        return "open.funds.subsidy.open.apply.invoice"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class FundsApplyInvoiceResponse(BaseResponse[Dict[str, Any]]):
    """申请发票响应"""

    pass


# ==================== 对账单列表 ====================


class FundsStatementListRequest(BaseRequest):
    """对账单列表请求（Java: OpenFundsFinancialStatementListRequest）"""

    cursor: Optional[str] = Field(default=None, description="游标", alias="cursor")
    start_time: Optional[int] = Field(
        default=None, description="开始时间", alias="startTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    sub_mch_id: Optional[str] = Field(
        default=None, description="子商户ID", alias="subMchId"
    )

    @property
    def api_method(self) -> str:
        return "open.funds.financial.statement.list"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class StatementInfo(BaseModel):
    """对账单信息"""

    statement_id: Optional[str] = Field(default=None, alias="statementId")
    amount: Optional[int] = Field(default=None, alias="amount")
    statement_time: Optional[int] = Field(default=None, alias="statementTime")

    @property
    def amount_yuan(self) -> Optional[float]:
        return self.amount / 100 if self.amount is not None else None


class FundsStatementListResponse(BaseResponse[List[StatementInfo]]):
    """对账单列表响应"""

    pass


# ==================== 申请发票文件相关 ====================


class FundsApplyInvoiceFileRequest(BaseRequest):
    """申请发票文件请求"""

    relate_order_no: str = Field(description="关联订单号", alias="relateOrderNo")
    invoice_open_kind: int = Field(description="发票开具类型", alias="invoiceOpenKind")
    tax_rate: str = Field(description="税率", alias="taxRate")
    cert_no: str = Field(description="证书号", alias="certNo")
    invoice_name: str = Field(description="发票名称", alias="invoiceName")
    invoice_open_date: int = Field(description="发票开具日期", alias="invoiceOpenDate")
    count: int = Field(description="数量", alias="count")
    goods: str = Field(description="商品", alias="goods")
    invoice_code: str = Field(description="发票代码", alias="invoiceCode")
    invoice_verify_code: str = Field(
        description="发票验证码", alias="invoiceVerifyCode"
    )
    invoice_tax: str = Field(description="发票税额", alias="invoiceTax")
    tax_authority_code: str = Field(
        description="税务机关代码", alias="taxAuthorityCode"
    )
    invoice_location_code: str = Field(
        description="发票所在地代码", alias="invoiceLocationCode"
    )
    exclude_tax_amount: str = Field(description="不含税金额", alias="excludeTaxAmount")
    isv_code: str = Field(description="ISV代码", alias="isvCode")
    invoice_no: str = Field(description="发票号码", alias="invoiceNo")
    # 注意：invoice_bytes (文件上传参数) 需要在服务层处理

    @property
    def api_method(self) -> str:
        return "open.funds.subsidy.open.apply.invoice.file"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InvoiceFileApplyResult(BaseModel):
    """发票文件申请结果"""

    apply_id: str = Field(description="申请ID")
    status: str = Field(description="申请状态")
    file_url: Optional[str] = Field(default=None, description="文件URL")


class FundsApplyInvoiceFileResponse(BaseResponse[InvoiceFileApplyResult]):
    """申请发票文件响应"""

    pass
