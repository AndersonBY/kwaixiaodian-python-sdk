"""快手SDK主客户端"""

import logging
from typing import Optional

from ..auth import AuthConfig, SignMethod
from ..http import HTTPConfig, RetryConfig
from .base import AsyncBaseClient, SyncBaseClient
from .services.comment import AsyncCommentService, SyncCommentService
from .services.customer_service import (
    AsyncCustomerServiceService,
    SyncCustomerServiceService,
)
from .services.distribution import AsyncDistributionService, SyncDistributionService
from .services.dropshipping import AsyncDropshippingService, SyncDropshippingService
from .services.funds import AsyncFundsService, SyncFundsService
from .services.industry import AsyncIndustryService, SyncIndustryService
from .services.invoice import AsyncInvoiceService, SyncInvoiceService
from .services.item import AsyncItemService, SyncItemService
from .services.live import AsyncLiveService, SyncLiveService
from .services.local_life import AsyncLocalLifeService, SyncLocalLifeService
from .services.logistics import AsyncLogisticsService, SyncLogisticsService
from .services.order import AsyncOrderService, SyncOrderService
from .services.photo import AsyncPhotoService, SyncPhotoService
from .services.promotion import AsyncPromotionService, SyncPromotionService
from .services.refund import AsyncRefundService, SyncRefundService
from .services.scm import AsyncScmService, SyncScmService
from .services.security import AsyncSecurityService, SyncSecurityService
from .services.service_market import AsyncServiceMarketService, SyncServiceMarketService
from .services.shop import AsyncShopService, SyncShopService
from .services.sms import AsyncSmsService, SyncSmsService
from .services.supply import AsyncSupplyService, SyncSupplyService
from .services.user import AsyncUserService, SyncUserService

logger = logging.getLogger(__name__)


class AsyncKwaixiaodianClient:
    """快手小店开放平台主客户端

    对齐 Java 参考与 docs 的开放能力集合。

    支持的业务域：
        - 订单管理 (order) - 订单查询、发货、状态更新
        - 商品管理 (item) - 商品CRUD、库存、规格管理
        - 售后管理 (refund) - 退款退货、协商处理
        - 物流管理 (logistics) - 物流跟踪、发货管理
        - 营销推广 (promotion) - 优惠券、活动管理
        - 资金管理 (funds) - 账户资金、财务结算、提现管理
        - 评论管理 (comment) - 评论查询、回复管理
        - 店铺管理 (shop) - 店铺信息、装修配置
        - 用户管理 (user) - 用户信息、粉丝管理
        - 安全管理 (security) - 风控检测、安全认证
        - 发票管理 (invoice) - 发票开具、发票查询
        - 支付管理 (payment) - 支付配置、支付查询
        - 直播管理 (live) - 直播间管理、直播数据
        - 短信服务 (sms) - 短信发送、短信模板
        - 分销管理 (distribution) - 分销商管理、分销政策
        - 虚拟商品 (virtual) - 无 open.virtual.* 商家侧接口（请使用 industry 域）
        - 视频管理 (video) - 视频上传、视频审核

    Features:
        - 🚀 异步支持 - 基于asyncio的高性能异步调用
        - 🔐 安全认证 - 完整的OAuth和签名支持
        - 📦 业务模型 - 类型安全的请求/响应模型
        - ⚡ 自动重试 - 网络异常和token过期自动重试
        - 🛡️ 错误处理 - 详细的异常信息和错误码映射
    """

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        sign_secret: str,
        server_url: str = "https://openapi.kwaixiaodian.com",
        sign_method: SignMethod = SignMethod.HMAC_SHA256,
        http_config: Optional[HTTPConfig] = None,
        retry_config: Optional[RetryConfig] = None,
        enable_logging: bool = False,
    ):
        """初始化快手SDK客户端

        Args:
            app_key: 应用AppKey，从快手开放平台获取
            app_secret: 应用AppSecret，从快手开放平台获取
            sign_secret: 签名密钥SignSecret，从快手开放平台获取
            server_url: API服务器地址，默认为线上环境
            sign_method: 签名算法，推荐使用HMAC_SHA256
            http_config: HTTP客户端配置，用于自定义超时、代理等
            retry_config: 重试策略配置
            enable_logging: 是否启用调试日志
        """
        # 认证配置
        self.config = AuthConfig(
            app_key=app_key,
            app_secret=app_secret,
            sign_secret=sign_secret,
            sign_method=sign_method,
            server_url=server_url,
        )

        # 基础客户端
        self._base_client = AsyncBaseClient(
            config=self.config,
            http_config=http_config,
            retry_config=retry_config,
            enable_logging=enable_logging,
        )

        # 业务服务
        self._order_service: Optional[AsyncOrderService] = None
        self._item_service: Optional[AsyncItemService] = None
        self._refund_service: Optional[AsyncRefundService] = None
        self._logistics_service: Optional[AsyncLogisticsService] = None
        self._funds_service: Optional[AsyncFundsService] = None
        self._industry_service: Optional[AsyncIndustryService] = None
        self._service_market_service: Optional[AsyncServiceMarketService] = None
        self._local_life_service: Optional[AsyncLocalLifeService] = None
        self._comment_service: Optional[AsyncCommentService] = None
        self._customer_service_service: Optional[AsyncCustomerServiceService] = None
        self._dropshipping_service: Optional[AsyncDropshippingService] = None
        self._shop_service: Optional[AsyncShopService] = None
        self._user_service: Optional[AsyncUserService] = None
        self._security_service: Optional[AsyncSecurityService] = None
        self._invoice_service: Optional[AsyncInvoiceService] = None
        self._live_service: Optional[AsyncLiveService] = None
        self._distribution_service: Optional[AsyncDistributionService] = None
        self._photo_service: Optional[AsyncPhotoService] = None
        self._sms_service: Optional[AsyncSmsService] = None
        self._promotion_service: Optional[AsyncPromotionService] = None
        self._supply_service: Optional[AsyncSupplyService] = None
        # SCM service holder
        self._scm_service: Optional[AsyncScmService] = None

    async def __aenter__(self):
        """异步上下文管理器入口"""
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ):
        """异步上下文管理器退出"""
        await self.close()

    async def close(self) -> None:
        """关闭客户端，释放资源"""
        await self._base_client.close()

    @property
    def order(self) -> AsyncOrderService:
        """订单服务

        提供订单查询、发货、备注更新等功能。
        """
        if self._order_service is None:
            self._order_service = AsyncOrderService(self._base_client)
        return self._order_service

    @property
    def item(self) -> AsyncItemService:
        """商品服务

        提供商品创建、更新、查询、库存管理等功能。
        """
        if self._item_service is None:
            self._item_service = AsyncItemService(self._base_client)
        return self._item_service

    @property
    def refund(self) -> AsyncRefundService:
        """售后服务

        提供退款退货、协商处理、售后状态查询等功能。
        """
        if self._refund_service is None:
            self._refund_service = AsyncRefundService(self._base_client)
        return self._refund_service

    @property
    def logistics(self) -> AsyncLogisticsService:
        """物流服务

        提供物流跟踪、发货管理、配送查询等功能。
        """
        if self._logistics_service is None:
            self._logistics_service = AsyncLogisticsService(self._base_client)
        return self._logistics_service

        # promotion service removed per Java reference; distribution.* covers promo topics

    @property
    def funds(self) -> AsyncFundsService:
        """资金管理服务

        提供账户资金查询、资金流水记录、提现管理、结算查询等功能。
        支持完整的资金生命周期管理和财务对账功能。
        """
        if self._funds_service is None:
            self._funds_service = AsyncFundsService(self._base_client)
        return self._funds_service

    @property
    def industry(self) -> AsyncIndustryService:
        """行业特化服务

        提供垂直行业特化功能：虚拟商品订单详情查询、审核、解密和二手商品用户档案查询。
        """
        if self._industry_service is None:
            self._industry_service = AsyncIndustryService(self._base_client)
        return self._industry_service

    @property
    def service_market(self) -> AsyncServiceMarketService:
        """服务市场服务

        提供服务市场订单管理功能：服务订单列表查询、详情查询和买家服务信息查询。
        """
        if self._service_market_service is None:
            self._service_market_service = AsyncServiceMarketService(self._base_client)
        return self._service_market_service

    @property
    def local_life(self) -> AsyncLocalLifeService:
        """本地生活服务

        提供本地生活订单管理功能：订单详情查询和订单分页查询。
        """
        if self._local_life_service is None:
            self._local_life_service = AsyncLocalLifeService(self._base_client)
        return self._local_life_service

    @property
    def comment(self) -> AsyncCommentService:
        """评价管理服务

        提供完整的商品评价管理功能，包括评价查询与筛选、回复管理、评价审核、统计分析、有用性管理、模板管理、数据导出等。
        """
        if self._comment_service is None:
            self._comment_service = AsyncCommentService(self._base_client)
        return self._comment_service

    @property
    def customer_service(self) -> AsyncCustomerServiceService:
        """客服服务

        提供完整的客服管理功能，包括智能消息发送、客服分组管理、商品映射配置、物流会话回调等。
        """
        if self._customer_service_service is None:
            self._customer_service_service = AsyncCustomerServiceService(
                self._base_client
            )
        return self._customer_service_service

    @property
    def dropshipping(self) -> AsyncDropshippingService:
        """代发服务

        提供完整的代发管理功能，包括电子面单管理、订单分配、发货管理、关系管理等。
        """
        if self._dropshipping_service is None:
            self._dropshipping_service = AsyncDropshippingService(self._base_client)
        return self._dropshipping_service

    @property
    def shop(self) -> AsyncShopService:
        """店铺管理服务

        提供店铺信息、装修配置、经营数据等功能。
        """
        if self._shop_service is None:
            self._shop_service = AsyncShopService(self._base_client)
        return self._shop_service

    @property
    def user(self) -> AsyncUserService:
        """用户管理服务
        提供用户信息、卖家信息、粉丝关系与子账号管理。
        """
        if self._user_service is None:
            self._user_service = AsyncUserService(self._base_client)
        return self._user_service

    @property
    def security(self) -> AsyncSecurityService:
        """安全管理服务

        提供风控检测、安全认证、权限管理等功能。
        """
        if self._security_service is None:
            self._security_service = AsyncSecurityService(self._base_client)
        return self._security_service

    @property
    def invoice(self) -> AsyncInvoiceService:
        """发票管理服务

        仅保留以下 Java 对齐端点：
        - open.invoice.subsidy.audit.info
        - open.invoice.amount.get
        """
        if self._invoice_service is None:
            self._invoice_service = AsyncInvoiceService(self._base_client)
        return self._invoice_service

    # payment service removed per Java reference (open.payment.* not available)

    @property
    def live(self) -> AsyncLiveService:
        """直播管理服务

        提供直播间管理、直播数据、直播商品等功能。
        """
        if self._live_service is None:
            self._live_service = AsyncLiveService(self._base_client)
        return self._live_service

    @property
    def photo(self) -> AsyncPhotoService:
        """照片管理服务（open.photo.*）"""
        if self._photo_service is None:
            self._photo_service = AsyncPhotoService(self._base_client)
        return self._photo_service

    @property
    def sms(self) -> AsyncSmsService:
        """短信服务（open.sms.*）"""
        if self._sms_service is None:
            self._sms_service = AsyncSmsService(self._base_client)
        return self._sms_service

    @property
    def promotion(self) -> AsyncPromotionService:
        """营销推广服务（open.promotion.*）"""
        if self._promotion_service is None:
            self._promotion_service = AsyncPromotionService(self._base_client)
        return self._promotion_service

    @property
    def distribution(self) -> AsyncDistributionService:
        """分销管理服务

        提供分销商管理、分销政策、佣金结算等功能。
        """
        if self._distribution_service is None:
            self._distribution_service = AsyncDistributionService(self._base_client)
        return self._distribution_service

    # video service removed (use item.video.* endpoints)
    def scm(self) -> AsyncScmService:
        """SCM供应链管理服务

        提供库存管理、商品管理、仓库管理等功能：
        - 库存调整、详情查询和更新
        - 商品添加、查询、列表和更新
        - 仓库添加、信息查询、列表查询和更新
        - 包裹重量快递查询
        - 销售范围模板管理

        Returns:
            ScmService: SCM服务实例
        """
        if self._scm_service is None:
            self._scm_service = AsyncScmService(self._base_client)
        return self._scm_service

    @property
    def supply(self) -> AsyncSupplyService:
        """供应链服务

        提供供应链同步功能：商品同步。
        """
        if self._supply_service is None:
            self._supply_service = AsyncSupplyService(self._base_client)
        return self._supply_service


class SyncKwaixiaodianClient:
    """快手小店开放平台同步客户端

    提供对快手开放平台所有API的同步访问能力，支持25个业务域和896个API接口。

    支持的业务域：
        - 订单管理 (order) - 订单查询、发货、状态更新
        - 商品管理 (item) - 商品CRUD、库存、规格管理
        - 售后管理 (refund) - 退款退货、协商处理
        - 物流管理 (logistics) - 物流跟踪、发货管理
        - 营销推广 (promotion) - 优惠券、活动管理
        - 资金管理 (funds) - 账户资金、财务结算、提现管理
        - 评论管理 (comment) - 评论查询、回复管理
        - 店铺管理 (shop) - 店铺信息、装修配置
        - 用户管理 (user) - 用户信息、粉丝管理
        - 安全管理 (security) - 风控检测、安全认证
        - 发票管理 (invoice) - 发票开具、发票查询
        - 支付管理 (payment) - 支付配置、支付查询
        - 直播管理 (live) - 直播间管理、直播数据
        - 短信服务 (sms) - 短信发送、短信模板
        - 分销管理 (distribution) - 分销商管理、分销政策
        - 视频管理 (video) - 视频上传、视频审核

    Features:
        - 🔄 同步调用 - 基于httpx的同步HTTP客户端
        - 🔐 安全认证 - 完整的OAuth和签名支持
        - 📦 业务模型 - 类型安全的请求/响应模型
        - ⚡ 自动重试 - 网络异常和token过期自动重试
        - 🛡️ 错误处理 - 详细的异常信息和错误码映射

    """

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        sign_secret: str,
        server_url: str = "https://openapi.kwaixiaodian.com",
        sign_method: SignMethod = SignMethod.HMAC_SHA256,
        http_config: Optional[HTTPConfig] = None,
        retry_config: Optional[RetryConfig] = None,
        enable_logging: bool = False,
    ):
        """初始化快手SDK同步客户端

        Args:
            app_key: 应用AppKey，从快手开放平台获取
            app_secret: 应用AppSecret，从快手开放平台获取
            sign_secret: 签名密钥SignSecret，从快手开放平台获取
            server_url: API服务器地址，默认为线上环境
            sign_method: 签名算法，推荐使用HMAC_SHA256
            http_config: HTTP客户端配置，用于自定义超时、代理等
            retry_config: 重试策略配置
            enable_logging: 是否启用调试日志
        """
        # 认证配置
        self.config = AuthConfig(
            app_key=app_key,
            app_secret=app_secret,
            sign_secret=sign_secret,
            sign_method=sign_method,
            server_url=server_url,
        )

        # 基础客户端
        self._base_client = SyncBaseClient(
            config=self.config,
            http_config=http_config,
            retry_config=retry_config,
            enable_logging=enable_logging,
        )

        # 业务服务
        self._order_service: Optional[SyncOrderService] = None
        self._item_service: Optional[SyncItemService] = None
        self._refund_service: Optional[SyncRefundService] = None
        self._logistics_service: Optional[SyncLogisticsService] = None
        self._funds_service: Optional[SyncFundsService] = None
        self._industry_service: Optional[SyncIndustryService] = None
        self._service_market_service: Optional[SyncServiceMarketService] = None
        self._local_life_service: Optional[SyncLocalLifeService] = None
        self._comment_service: Optional[SyncCommentService] = None
        self._customer_service_service: Optional[SyncCustomerServiceService] = None
        self._dropshipping_service: Optional[SyncDropshippingService] = None
        self._shop_service: Optional[SyncShopService] = None
        self._user_service: Optional[SyncUserService] = None
        self._security_service: Optional[SyncSecurityService] = None
        self._invoice_service: Optional[SyncInvoiceService] = None
        self._live_service: Optional[SyncLiveService] = None
        self._distribution_service: Optional[SyncDistributionService] = None
        self._photo_service: Optional[SyncPhotoService] = None
        self._sms_service: Optional[SyncSmsService] = None
        self._promotion_service: Optional[SyncPromotionService] = None
        self._supply_service: Optional[SyncSupplyService] = None
        # SCM service holder
        self._scm_service: Optional[SyncScmService] = None

    def __enter__(self):
        """上下文管理器入口"""
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ):
        """上下文管理器退出"""
        self.close()

    def close(self) -> None:
        """关闭客户端，释放资源"""
        self._base_client.close()

    @property
    def order(self) -> SyncOrderService:
        """订单服务

        提供订单查询、发货、备注更新等功能。
        """
        if self._order_service is None:
            self._order_service = SyncOrderService(self._base_client)
        return self._order_service

    @property
    def item(self) -> SyncItemService:
        """商品服务

        提供商品创建、更新、查询、库存管理等功能。
        """
        if self._item_service is None:
            self._item_service = SyncItemService(self._base_client)
        return self._item_service

    @property
    def refund(self) -> SyncRefundService:
        """售后服务

        提供退款退货、协商处理、售后状态查询等功能。
        """
        if self._refund_service is None:
            self._refund_service = SyncRefundService(self._base_client)
        return self._refund_service

    @property
    def logistics(self) -> SyncLogisticsService:
        """物流服务

        提供物流跟踪、发货管理、配送查询等功能。
        """
        if self._logistics_service is None:
            self._logistics_service = SyncLogisticsService(self._base_client)
        return self._logistics_service

        # promotion service removed per Java reference; distribution.* covers promo topics

    @property
    def funds(self) -> SyncFundsService:
        """资金管理服务

        提供账户资金查询、资金流水记录、提现管理、结算查询等功能。
        支持完整的资金生命周期管理和财务对账功能。
        """
        if self._funds_service is None:
            self._funds_service = SyncFundsService(self._base_client)
        return self._funds_service

    @property
    def industry(self) -> SyncIndustryService:
        """行业特化服务 (同步)

        提供垂直行业特化功能的同步版本。
        """
        if self._industry_service is None:
            self._industry_service = SyncIndustryService(self._base_client)
        return self._industry_service

    @property
    def service_market(self) -> SyncServiceMarketService:
        """服务市场服务 (同步)

        提供服务市场订单管理功能的同步版本。
        """
        if self._service_market_service is None:
            self._service_market_service = SyncServiceMarketService(self._base_client)
        return self._service_market_service

    @property
    def local_life(self) -> SyncLocalLifeService:
        """本地生活服务 (同步)

        提供本地生活订单管理功能的同步版本。
        """
        if self._local_life_service is None:
            self._local_life_service = SyncLocalLifeService(self._base_client)
        return self._local_life_service

    @property
    def comment(self) -> SyncCommentService:
        """评价管理服务

        提供完整的商品评价管理功能，包括评价查询与筛选、回复管理、评价审核、统计分析、有用性管理、模板管理、数据导出等。
        """
        if self._comment_service is None:
            self._comment_service = SyncCommentService(self._base_client)
        return self._comment_service

    @property
    def customer_service(self) -> SyncCustomerServiceService:
        """客服服务 (同步)

        提供完整的客服管理功能，包括智能消息发送、客服分组管理、商品映射配置、物流会话回调等。
        """
        if self._customer_service_service is None:
            self._customer_service_service = SyncCustomerServiceService(
                self._base_client
            )
        return self._customer_service_service

    @property
    def dropshipping(self) -> SyncDropshippingService:
        """代发服务 (同步)

        提供完整的代发管理功能，包括电子面单管理、订单分配、发货管理、关系管理等。
        """
        if self._dropshipping_service is None:
            self._dropshipping_service = SyncDropshippingService(self._base_client)
        return self._dropshipping_service

    @property
    def shop(self) -> SyncShopService:
        """店铺管理服务

        提供店铺信息、装修配置、经营数据等功能。
        """
        if self._shop_service is None:
            self._shop_service = SyncShopService(self._base_client)
        return self._shop_service

    @property
    def user(self) -> SyncUserService:
        """用户管理服务
        提供用户信息、卖家信息、粉丝关系与子账号管理。
        """
        if self._user_service is None:
            self._user_service = SyncUserService(self._base_client)
        return self._user_service

    @property
    def security(self) -> SyncSecurityService:
        """安全管理服务

        提供风控检测、安全认证、权限管理等功能。
        """
        if self._security_service is None:
            self._security_service = SyncSecurityService(self._base_client)
        return self._security_service

    @property
    def invoice(self) -> SyncInvoiceService:
        """发票管理服务

        仅保留以下 Java 对齐端点：
        - open.invoice.subsidy.audit.info
        - open.invoice.amount.get
        """
        if self._invoice_service is None:
            self._invoice_service = SyncInvoiceService(self._base_client)
        return self._invoice_service

    # payment service removed per Java reference (open.payment.* not available)

    @property
    def live(self) -> SyncLiveService:
        """直播管理服务

        提供直播间管理、直播数据、直播商品等功能。
        """
        if self._live_service is None:
            self._live_service = SyncLiveService(self._base_client)
        return self._live_service

    @property
    def photo(self) -> SyncPhotoService:
        if self._photo_service is None:
            self._photo_service = SyncPhotoService(self._base_client)
        return self._photo_service

    @property
    def sms(self) -> SyncSmsService:
        if self._sms_service is None:
            self._sms_service = SyncSmsService(self._base_client)
        return self._sms_service

    @property
    def promotion(self) -> SyncPromotionService:
        if self._promotion_service is None:
            self._promotion_service = SyncPromotionService(self._base_client)
        return self._promotion_service

    @property
    def distribution(self) -> SyncDistributionService:
        """分销管理服务

        提供分销商管理、分销政策、佣金结算等功能。
        """
        if self._distribution_service is None:
            self._distribution_service = SyncDistributionService(self._base_client)
        return self._distribution_service

    # video service removed (use item.video.* endpoints)
    def scm(self) -> SyncScmService:
        """SCM供应链管理服务

        提供库存管理、商品管理、仓库管理等功能：
        - 库存调整、详情查询和更新
        - 商品添加、查询、列表和更新
        - 仓库添加、信息查询、列表查询和更新
        - 包裹重量快递查询
        - 销售范围模板管理

        Returns:
            SyncScmService: SCM服务实例
        """
        if self._scm_service is None:
            self._scm_service = SyncScmService(self._base_client)
        return self._scm_service

    @property
    def supply(self) -> SyncSupplyService:
        """供应链服务 (同步)

        提供供应链同步功能的同步版本。
        """
        if self._supply_service is None:
            self._supply_service = SyncSupplyService(self._base_client)
        return self._supply_service
