"""安全管理相关数据模型"""

from enum import Enum
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod


class RiskLevel(int, Enum):
    """风险等级"""

    LOW = 1  # 低风险
    MEDIUM = 2  # 中风险
    HIGH = 3  # 高风险
    CRITICAL = 4  # 严重风险


class RiskType(int, Enum):
    """风险类型"""

    ORDER_RISK = 1  # 订单风险
    PAYMENT_RISK = 2  # 支付风险
    ACCOUNT_RISK = 3  # 账户风险
    BEHAVIOR_RISK = 4  # 行为风险
    CONTENT_RISK = 5  # 内容风险
    IP_RISK = 6  # IP风险


class FraudType(int, Enum):
    """欺诈类型"""

    FAKE_TRANSACTION = 1  # 虚假交易
    SPAM_CONTENT = 2  # 垃圾内容
    ACCOUNT_ABUSE = 3  # 账户滥用
    PAYMENT_FRAUD = 4  # 支付欺诈
    IDENTITY_THEFT = 5  # 身份盗用
    MALICIOUS_BEHAVIOR = 6  # 恶意行为


class SecurityEventType(int, Enum):
    """安全事件类型"""

    LOGIN_ATTEMPT = 1  # 登录尝试
    PASSWORD_CHANGE = 2  # 密码修改
    ACCOUNT_LOCK = 3  # 账户锁定
    SUSPICIOUS_ACTIVITY = 4  # 可疑活动
    DATA_BREACH = 5  # 数据泄露
    UNAUTHORIZED_ACCESS = 6  # 未授权访问


class VerificationType(int, Enum):
    """验证类型"""

    SMS_CODE = 1  # 短信验证码
    EMAIL_CODE = 2  # 邮箱验证码
    ID_CARD = 3  # 身份证验证
    FACE_RECOGNITION = 4  # 人脸识别
    FINGERPRINT = 5  # 指纹验证
    TWO_FACTOR_AUTH = 6  # 双因子认证


class SecurityStatus(int, Enum):
    """安全状态"""

    NORMAL = 1  # 正常
    WARNING = 2  # 警告
    SUSPICIOUS = 3  # 可疑
    BLOCKED = 4  # 封锁
    REVIEWING = 5  # 审核中


class PolicyAction(int, Enum):
    """策略动作"""

    ALLOW = 1  # 允许
    WARN = 2  # 警告
    BLOCK = 3  # 阻止
    REVIEW = 4  # 审核
    QUARANTINE = 5  # 隔离


class AuthType(str, Enum):
    """认证类型"""

    PASSWORD = "password"  # 密码认证
    TOKEN = "token"  # 令牌认证
    OAUTH = "oauth"  # OAuth认证
    API_KEY = "api_key"  # API密钥
    CERTIFICATE = "certificate"  # 证书认证


# ==================== 基础数据模型 ====================


class SecurityEvent(BaseModel):
    """安全事件"""

    # 基本信息
    event_id: str = Field(description="事件ID")
    event_type: SecurityEventType = Field(description="事件类型")
    event_name: str = Field(description="事件名称")
    severity: RiskLevel = Field(description="严重程度")

    # 用户信息
    user_id: Optional[int] = Field(default=None, description="用户ID")
    user_name: Optional[str] = Field(default=None, description="用户名")
    user_ip: Optional[str] = Field(default=None, description="用户IP")

    # 设备信息
    device_id: Optional[str] = Field(default=None, description="设备ID")
    device_type: Optional[str] = Field(default=None, description="设备类型")
    user_agent: Optional[str] = Field(default=None, description="用户代理")

    # 事件详情
    description: str = Field(description="事件描述")
    details: Optional[Dict[str, Any]] = Field(default=None, description="详细信息")
    tags: Optional[List[str]] = Field(default=None, description="事件标签")

    # 处理信息
    status: SecurityStatus = Field(
        default=SecurityStatus.NORMAL, description="处理状态"
    )
    action_taken: Optional[str] = Field(default=None, description="已采取的措施")
    assignee: Optional[str] = Field(default=None, description="处理人")

    # 时间信息
    event_time: str = Field(description="事件发生时间")
    create_time: str = Field(description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")
    resolve_time: Optional[str] = Field(default=None, description="解决时间")

    # 关联信息
    related_events: Optional[List[str]] = Field(default=None, description="关联事件ID")
    source_system: Optional[str] = Field(default=None, description="来源系统")


class RiskAssessment(BaseModel):
    """风险评估结果"""

    # 基本信息
    assessment_id: str = Field(description="评估ID")
    target_type: str = Field(description="评估对象类型")
    target_id: str = Field(description="评估对象ID")

    # 风险信息
    risk_level: RiskLevel = Field(description="风险等级")
    risk_score: float = Field(description="风险分数", ge=0, le=100)
    risk_types: List[RiskType] = Field(description="风险类型列表")

    # 风险因子
    risk_factors: List[Dict[str, Any]] = Field(description="风险因子详情")
    confidence: float = Field(description="置信度", ge=0, le=1)

    # 建议措施
    recommended_actions: List[str] = Field(description="建议措施")
    policy_matched: Optional[List[str]] = Field(default=None, description="匹配的策略")

    # 时间信息
    assessment_time: str = Field(description="评估时间")
    valid_until: Optional[str] = Field(default=None, description="有效期至")

    # 模型信息
    model_version: Optional[str] = Field(default=None, description="模型版本")
    model_name: Optional[str] = Field(default=None, description="模型名称")

    @property
    def is_high_risk(self) -> bool:
        """是否为高风险"""
        return self.risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL]


class FraudReport(BaseModel):
    """欺诈举报"""

    # 基本信息
    report_id: str = Field(description="举报ID")
    target_type: str = Field(description="举报对象类型")
    target_id: str = Field(description="举报对象ID")
    fraud_type: FraudType = Field(description="欺诈类型")

    # 举报信息
    reporter_id: Optional[int] = Field(default=None, description="举报人ID")
    description: str = Field(description="举报描述")
    evidence_urls: Optional[List[str]] = Field(default=None, description="证据链接")
    severity: RiskLevel = Field(description="严重程度")

    # 处理信息
    status: SecurityStatus = Field(
        default=SecurityStatus.REVIEWING, description="处理状态"
    )
    review_result: Optional[str] = Field(default=None, description="审核结果")
    action_taken: Optional[str] = Field(default=None, description="采取的措施")
    reviewer: Optional[str] = Field(default=None, description="审核人")

    # 时间信息
    report_time: str = Field(description="举报时间")
    review_time: Optional[str] = Field(default=None, description="审核时间")
    close_time: Optional[str] = Field(default=None, description="关闭时间")

    # 附加信息
    tags: Optional[List[str]] = Field(default=None, description="标签")
    notes: Optional[str] = Field(default=None, description="备注")


class SecurityPolicy(BaseModel):
    """安全策略"""

    # 基本信息
    policy_id: str = Field(description="策略ID")
    policy_name: str = Field(description="策略名称")
    policy_type: str = Field(description="策略类型")
    version: str = Field(description="版本号")

    # 策略内容
    description: str = Field(description="策略描述")
    conditions: List[Dict[str, Any]] = Field(description="触发条件")
    actions: List[PolicyAction] = Field(description="执行动作")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="策略参数")

    # 适用范围
    scope: Optional[Dict[str, Any]] = Field(default=None, description="适用范围")
    priority: int = Field(default=100, description="优先级")

    # 状态信息
    is_active: bool = Field(default=True, description="是否启用")
    is_editable: bool = Field(default=True, description="是否可编辑")

    # 时间信息
    create_time: str = Field(description="创建时间")
    update_time: str = Field(description="更新时间")
    effective_time: Optional[str] = Field(default=None, description="生效时间")
    expire_time: Optional[str] = Field(default=None, description="过期时间")

    # 创建者信息
    creator: str = Field(description="创建者")
    updater: Optional[str] = Field(default=None, description="更新者")


class AuthCredential(BaseModel):
    """认证凭据"""

    # 基本信息
    credential_id: str = Field(description="凭据ID")
    credential_name: str = Field(description="凭据名称")
    auth_type: AuthType = Field(description="认证类型")

    # 用户信息
    user_id: int = Field(description="用户ID")
    user_name: Optional[str] = Field(default=None, description="用户名")

    # 凭据信息
    is_active: bool = Field(default=True, description="是否有效")
    permissions: Optional[List[str]] = Field(default=None, description="权限列表")
    scopes: Optional[List[str]] = Field(default=None, description="作用域")

    # 使用信息
    last_used_time: Optional[str] = Field(default=None, description="最后使用时间")
    use_count: int = Field(default=0, description="使用次数")

    # 时间信息
    create_time: str = Field(description="创建时间")
    expire_time: Optional[str] = Field(default=None, description="过期时间")

    # 限制信息
    ip_whitelist: Optional[List[str]] = Field(default=None, description="IP白名单")
    rate_limit: Optional[int] = Field(default=None, description="频率限制")

    @property
    def is_expired(self) -> bool:
        """是否已过期"""
        if not self.expire_time:
            return False
        from datetime import datetime

        try:
            expire_dt = datetime.fromisoformat(self.expire_time.replace("Z", "+00:00"))
            return expire_dt < datetime.now(expire_dt.tzinfo)
        except Exception:
            return False


class BlacklistEntry(BaseModel):
    """黑名单条目"""

    # 基本信息
    entry_id: str = Field(description="条目ID")
    entry_type: str = Field(description="条目类型")  # user, ip, device, phone, email
    entry_value: str = Field(description="条目值")

    # 黑名单信息
    reason: str = Field(description="加入原因")
    severity: RiskLevel = Field(description="严重程度")
    category: Optional[str] = Field(default=None, description="分类")

    # 处理信息
    is_active: bool = Field(default=True, description="是否有效")
    auto_expire: bool = Field(default=False, description="是否自动过期")

    # 时间信息
    create_time: str = Field(description="创建时间")
    expire_time: Optional[str] = Field(default=None, description="过期时间")
    last_match_time: Optional[str] = Field(default=None, description="最后匹配时间")

    # 操作信息
    creator: str = Field(description="创建者")
    source: Optional[str] = Field(default=None, description="来源系统")

    # 统计信息
    match_count: int = Field(default=0, description="匹配次数")
    notes: Optional[str] = Field(default=None, description="备注")

    @property
    def is_expired(self) -> bool:
        """是否已过期"""
        if not self.expire_time:
            return False
        from datetime import datetime

        try:
            expire_dt = datetime.fromisoformat(self.expire_time.replace("Z", "+00:00"))
            return expire_dt < datetime.now(expire_dt.tzinfo)
        except Exception:
            return False


class SecurityAuditLog(BaseModel):
    """安全审计日志"""

    # 基本信息
    log_id: str = Field(description="日志ID")
    operation: str = Field(description="操作名称")
    resource: str = Field(description="资源")
    action: str = Field(description="动作")

    # 用户信息
    user_id: Optional[int] = Field(default=None, description="操作用户ID")
    user_name: Optional[str] = Field(default=None, description="用户名")
    user_ip: Optional[str] = Field(default=None, description="用户IP")

    # 操作详情
    description: str = Field(description="操作描述")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="操作参数")
    result: str = Field(description="操作结果")  # success, failure, partial

    # 影响信息
    affected_resources: Optional[List[str]] = Field(
        default=None, description="影响的资源"
    )
    risk_level: RiskLevel = Field(default=RiskLevel.LOW, description="风险等级")

    # 时间信息
    operation_time: str = Field(description="操作时间")
    duration: Optional[int] = Field(default=None, description="持续时间（毫秒）")

    # 系统信息
    system: Optional[str] = Field(default=None, description="系统标识")
    module: Optional[str] = Field(default=None, description="模块")
    version: Optional[str] = Field(default=None, description="版本")

    # 上下文信息
    session_id: Optional[str] = Field(default=None, description="会话ID")
    request_id: Optional[str] = Field(default=None, description="请求ID")
    trace_id: Optional[str] = Field(default=None, description="跟踪ID")


## 已根据 Java 参考移除：风险检测相关接口


## 已根据 Java 参考移除：欺诈举报相关接口


## 已根据 Java 参考移除：身份验证相关接口


# ==================== 安全日志 ====================


## 已根据 Java 参考移除：open.security.log（查询）


# ==================== Java-aligned Security Logs ====================


class SecurityLogOrderRequest(BaseRequest):
    """安全订单访问日志请求

    对应 Java: OpenSecurityLogOrderRequest -> open.security.log.order
    """

    open_id: str = Field(description="用户开放ID", alias="openId")
    seller_id: int = Field(description="卖家ID", alias="sellerId")
    url: str = Field(description="访问URL", alias="url")
    user_ip: str = Field(description="用户IP", alias="userIp")
    order_ids: Optional[List[int]] = Field(
        default=None, description="订单ID列表", alias="orderIds"
    )
    operation: Optional[int] = Field(
        default=None, description="操作类型", alias="operation"
    )
    data: Optional[str] = Field(
        default=None, description="附加数据(JSON字符串)", alias="data"
    )
    order_total: Optional[int] = Field(
        default=None, description="订单总额（分）", alias="orderTotal"
    )
    time: int = Field(description="时间戳（毫秒）", alias="time")

    @property
    def api_method(self) -> str:
        return "open.security.log.order"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SecurityLogOrderResponse(BaseResponse[Dict[str, Any]]):
    """安全订单访问日志响应"""

    pass


class SecurityLogSqlRequest(BaseRequest):
    """SQL 访问日志请求

    对应 Java: OpenSecurityLogSqlRequest -> open.security.log.sql
    """

    type: str = Field(description="类型", alias="type")
    sql: str = Field(description="SQL 语句", alias="sql")
    time: int = Field(description="时间戳（毫秒）", alias="time")

    @property
    def api_method(self) -> str:
        return "open.security.log.sql"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SecurityLogSqlResponse(BaseResponse[Dict[str, Any]]):
    """SQL 访问日志响应"""

    pass


class SecurityLogBatchRequest(BaseRequest):
    """批量安全日志上报请求

    对应 Java: OpenSecurityLogBatchRequest -> open.security.log.batch
    """

    method: str = Field(description="方法名", alias="method")
    data: str = Field(description="批量数据(JSON字符串)", alias="data")

    @property
    def api_method(self) -> str:
        return "open.security.log.batch"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SecurityLogBatchResponse(BaseResponse[Dict[str, Any]]):
    """批量安全日志上报响应"""

    pass


# ==================== 其他 Java 已有日志接口 ====================


class SecurityLogOpenRequest(BaseRequest):
    """上报开放访问日志

    对应 Java: OpenSecurityLogOpenRequest -> open.security.log.open
    """

    open_id: str = Field(description="Open ID", alias="openId")
    seller_id: int = Field(description="商家ID", alias="sellerId")
    user_id: Optional[str] = Field(default=None, description="用户ID", alias="userId")
    order_ids: Optional[List[int]] = Field(
        default=None, description="订单ID列表", alias="orderIds"
    )
    client_ip: Optional[str] = Field(
        default=None, description="客户端IP", alias="clientIp"
    )
    data: Optional[str] = Field(default=None, description="附加数据", alias="data")
    order_total: Optional[int] = Field(
        default=None, description="订单总额（分）", alias="orderTotal"
    )
    url: Optional[str] = Field(default=None, description="访问URL", alias="url")
    send_to_url: Optional[str] = Field(
        default=None, description="上报目标URL", alias="sendToUrl"
    )
    time: Optional[int] = Field(default=None, description="时间戳", alias="time")

    @property
    def api_method(self) -> str:
        return "open.security.log.open"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SecurityLogOpenResponse(BaseResponse[Dict[str, Any]]):
    """开放访问日志响应"""

    pass


class SecurityLogLoginRequest(BaseRequest):
    """上报登录访问日志

    对应 Java: OpenSecurityLogLoginRequest -> open.security.log.login
    """

    open_id: str = Field(description="Open ID", alias="openId")
    seller_id: int = Field(description="商家ID", alias="sellerId")
    user_ip: Optional[str] = Field(default=None, description="用户IP", alias="userIp")
    login_result: Optional[str] = Field(
        default=None, description="登录结果", alias="loginResult"
    )
    login_message: Optional[str] = Field(
        default=None, description="登录信息", alias="loginMessage"
    )
    time: Optional[int] = Field(default=None, description="时间戳", alias="time")

    @property
    def api_method(self) -> str:
        return "open.security.log.login"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SecurityLogLoginResponse(BaseResponse[Dict[str, Any]]):
    """登录访问日志响应"""

    pass


class PeriodDecryptData(BaseModel):
    """周期加密数据（Java: PeriodDecryptData）"""

    encrypted_data: str = Field(description="加密数据", alias="encryptedData")


class PeriodDecryptResult(BaseModel):
    """周期解密结果（Java: PeriodDecryptResult）"""

    error_code: Optional[int] = Field(
        default=None, description="错误码", alias="errorCode"
    )
    error_msg: Optional[str] = Field(
        default=None, description="错误信息", alias="errorMsg"
    )
    decrypted_data: Optional[str] = Field(
        default=None, description="解密后的数据", alias="decryptedData"
    )
    encrypted_data: Optional[str] = Field(
        default=None, description="原加密数据", alias="encryptedData"
    )


class SecurityInstantDecryptBatchRequest(BaseRequest):
    """批量即时解密请求

    对应 Java: OpenSecurityInstantDecryptBatchRequest -> open.security.instant.decrypt.batch
    """

    decrypt_data_list: List[PeriodDecryptData] = Field(
        description="解密数据列表", alias="decryptDataList"
    )

    @property
    def api_method(self) -> str:
        return "open.security.instant.decrypt.batch"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SecurityInstantDecryptBatchResponse(BaseResponse[List[PeriodDecryptResult]]):
    """批量即时解密响应"""

    pass


## 已根据 Java 参考移除：open.security.audit.log


## 已根据 Java 参考移除：open.security.blacklist.*


# ==================== 安全策略管理 ====================


## 已根据 Java 参考移除：open.security.policies / policy.create / policy.update


# ==================== 认证凭据管理 ====================


## 已根据 Java 参考移除：open.security.auth.*


## 已根据 Java 参考移除：open.security.stats


# ==================== 安全通知 ====================


class SecurityEventNotification(BaseModel):
    """安全事件通知"""

    event_id: str = Field(description="事件ID")
    event_type: SecurityEventType = Field(description="事件类型")
    event_name: str = Field(description="事件名称")
    severity: RiskLevel = Field(description="严重程度")
    user_id: Optional[int] = Field(default=None, description="用户ID")
    description: str = Field(description="事件描述")
    event_time: str = Field(description="事件发生时间")
    sign: str = Field(description="签名")


class RiskAssessmentNotification(BaseModel):
    """风险评估通知"""

    assessment_id: str = Field(description="评估ID")
    target_type: str = Field(description="评估对象类型")
    target_id: str = Field(description="评估对象ID")
    risk_level: RiskLevel = Field(description="风险等级")
    risk_score: float = Field(description="风险分数")
    assessment_time: str = Field(description="评估时间")
    sign: str = Field(description="签名")


class FraudReportNotification(BaseModel):
    """欺诈举报通知"""

    report_id: str = Field(description="举报ID")
    target_type: str = Field(description="举报对象类型")
    target_id: str = Field(description="举报对象ID")
    fraud_type: FraudType = Field(description="欺诈类型")
    severity: RiskLevel = Field(description="严重程度")
    status: SecurityStatus = Field(description="处理状态")
    report_time: str = Field(description="举报时间")
    sign: str = Field(description="签名")
