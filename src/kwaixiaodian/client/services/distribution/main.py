"""主分销服务

整合各个分销子服务，提供完整的分销功能接口，包括分销计划管理、推广位管理等基础功能。
"""

from typing import Any, Dict, List, Optional

from ....models.distribution import (
    DistributePlanCreateRequest,
    DistributePlanCreateResponse,
    DistributePlanUpdateRequest,
    DistributePlanUpdateResponse,
    DistributionActivityItemShareCreateRequest,
    DistributionActivityItemShareCreateResponse,
    DistributionDistributorOrderListRequest,
    DistributionDistributorOrderListResponse,
    DistributionPlanAddPromoterRequest,
    DistributionPlanAddPromoterResponse,
    DistributionPlanDeletePromoterRequest,
    DistributionPlanDeletePromoterResponse,
    DistributionPublicCategoryListRequest,
    DistributionPublicCategoryListResponse,
    DistributionSelectionOfflineRequest,
    DistributionSelectionOfflineResponse,
    DistributionSelectionPickRequest,
    DistributionSelectionPickResponse,
    DistributionSellerSampleRuleSaveRequest,
    DistributionSellerSampleRuleSaveResponse,
    DistributionTestRequest,
    DistributionTestResponse,
    ItemSelectionAddUrlRequest,
    ItemSelectionAddUrlResponse,
    ItemShelfAddUrlRequest,
    ItemShelfAddUrlResponse,
    PlanCommissionQueryRequest,
    PlanCommissionQueryResponse,
    PlanQueryRequest,
    PlanQueryResponse,
    PromoteUpdateRequest,
    PromoteUpdateResponse,
    QuerySelectionItemDetailRequest,
    QuerySelectionItemDetailResponse,
)
from ...base import AsyncBaseClient, SyncBaseClient
from .cps import AsyncCpsService, SyncCpsService
from .investment import AsyncInvestmentService, SyncInvestmentService
from .second import AsyncSecondDistributionService, SyncSecondDistributionService
from .seller import AsyncSellerActivityService, SyncSellerActivityService


class AsyncDistributionService:
    """异步分销服务

    整合各个分销子服务，提供完整的分销功能接口。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化分销服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

        # 初始化各个子服务
        self.cps = AsyncCpsService(client)
        self.investment = AsyncInvestmentService(client)
        self.seller = AsyncSellerActivityService(client)
        self.second = AsyncSecondDistributionService(client)

    # ==================== 向后兼容的委托方法 ====================
    # 为了保持API向后兼容，将子服务方法委托到主服务

    # CPS服务委托方法
    async def get_cps_order_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS订单列表方法"""
        return await self.cps.get_cps_order_list(*args, **kwargs)

    async def get_cps_distributor_order_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS分销商订单列表方法"""
        return await self.cps.get_cps_distributor_order_list(*args, **kwargs)

    async def get_cps_kwaimoney_order_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币订单列表方法"""
        return await self.cps.get_cps_kwaimoney_order_list(*args, **kwargs)

    async def get_cps_kwaimoney_order_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币订单详情方法"""
        return await self.cps.get_cps_kwaimoney_order_detail(*args, **kwargs)

    async def get_cps_pid_bind_url(self, *args, **kwargs):
        """委托到CPS服务的获取CPS PID绑定URL方法"""
        return await self.cps.get_cps_pid_bind_url(*args, **kwargs)

    async def transfer_cps_link(self, *args, **kwargs):
        """委托到CPS服务的转换CPS链接方法"""
        return await self.cps.transfer_cps_link(*args, **kwargs)

    async def get_cps_brand_theme_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题列表方法"""
        return await self.cps.get_cps_brand_theme_list(*args, **kwargs)

    async def get_cps_theme_entrance_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS主题入口列表方法"""
        return await self.cps.get_cps_theme_entrance_list(*args, **kwargs)

    async def get_cps_kwaimoney_theme_entrance_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币主题入口列表方法"""
        return await self.cps.get_cps_kwaimoney_theme_entrance_list(*args, **kwargs)

    async def get_cps_promotion_reco_topic_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推广推荐话题列表方法"""
        return await self.cps.get_cps_promotion_reco_topic_list(*args, **kwargs)

    async def get_cps_promotion_effect_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推广效果详情方法"""
        return await self.cps.get_cps_promotion_effect_detail(*args, **kwargs)

    async def get_cps_leader_order_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS领导者订单详情方法"""
        return await self.cps.get_cps_leader_order_detail(*args, **kwargs)

    async def get_cps_kwaimoney_promotion_effect_trend(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币推广效果趋势方法"""
        return await self.cps.get_cps_kwaimoney_promotion_effect_trend(*args, **kwargs)

    async def update_cps_kwaimoney_pid(self, *args, **kwargs):
        """委托到CPS服务的更新CPS快手货币PID方法"""
        return await self.cps.update_cps_kwaimoney_pid(*args, **kwargs)

    async def get_cps_selection_item_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS精选商品详情方法"""
        return await self.cps.get_cps_selection_item_detail(*args, **kwargs)

    async def get_kwaimoney_preheat_work_link(self, *args, **kwargs):
        """委托到CPS服务的获取快手货币预热工作链接方法"""
        return await self.cps.get_kwaimoney_preheat_work_link(*args, **kwargs)

    async def parse_cps_kwaimoney_link(self, *args, **kwargs):
        """委托到CPS服务的解析CPS快手货币链接方法"""
        return await self.cps.parse_cps_kwaimoney_link(*args, **kwargs)

    async def create_cps_kwaimoney_pid(self, *args, **kwargs):
        """委托到CPS服务的创建CPS快手货币PID方法"""
        return await self.cps.create_cps_kwaimoney_pid(*args, **kwargs)

    async def get_cps_kwaimoney_pid_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币PID列表方法"""
        return await self.cps.get_cps_kwaimoney_pid_list(*args, **kwargs)

    async def create_cps_kwaimoney_link(self, *args, **kwargs):
        """委托到CPS服务的创建CPS快手货币链接方法"""
        return await self.cps.create_cps_kwaimoney_link(*args, **kwargs)

    async def get_cps_kwaimoney_selection_channel_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币精选渠道列表方法"""
        return await self.cps.get_cps_kwaimoney_selection_channel_list(*args, **kwargs)

    async def get_kwaimoney_requirement_cursor_list(self, *args, **kwargs):
        """委托到CPS服务的获取快手货币需求游标列表方法"""
        return await self.cps.get_kwaimoney_requirement_cursor_list(*args, **kwargs)

    async def get_selection_list(self, *args, **kwargs):
        """委托到CPS服务的获取精选列表方法"""
        return await self.cps.get_selection_list(*args, **kwargs)

    async def get_cps_kwaimoney_selection_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币精选商品列表方法"""
        return await self.cps.get_cps_kwaimoney_selection_item_list(*args, **kwargs)

    async def get_cps_kwaimoney_theme_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币主题商品列表方法"""
        return await self.cps.get_cps_kwaimoney_theme_item_list(*args, **kwargs)

    async def get_cps_leader_order_cursor_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS团长订单游标列表方法"""
        return await self.cps.get_cps_leader_order_cursor_list(*args, **kwargs)

    async def create_cps_link(self, *args, **kwargs):
        """委托到CPS服务的创建CPS推广链接方法"""
        return await self.cps.create_cps_link(*args, **kwargs)

    async def create_cps_pid(self, *args, **kwargs):
        """委托到CPS服务的创建CPS推广位方法"""
        return await self.cps.create_cps_pid(*args, **kwargs)

    async def query_cps_pid(self, *args, **kwargs):
        """委托到CPS服务的查询CPS推广位方法"""
        return await self.cps.query_cps_pid(*args, **kwargs)

    async def get_cps_promoter_order_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推广者订单详情方法"""
        return await self.cps.get_cps_promoter_order_detail(*args, **kwargs)

    # 投资活动服务委托方法
    async def adjust_investment_activity_promoter(self, *args, **kwargs):
        """委托到投资服务的调整投资活动推广者方法"""
        return await self.investment.adjust_investment_activity_promoter(
            *args, **kwargs
        )

    async def get_investment_sample_promoter_data(self, *args, **kwargs):
        """委托到投资服务的获取投资样本推广者数据方法"""
        return await self.investment.get_investment_sample_promoter_data(
            *args, **kwargs
        )

    async def create_investment_activity_item_token(self, *args, **kwargs):
        """委托到投资服务的创建投资活动商品令牌方法"""
        return await self.investment.create_investment_activity_item_token(
            *args, **kwargs
        )

    async def audit_investment_activity_open_item(self, *args, **kwargs):
        """委托到投资服务的审核投资活动开放商品方法"""
        return await self.investment.audit_investment_activity_open_item(
            *args, **kwargs
        )

    async def delete_investment_activity_open(self, *args, **kwargs):
        """委托到投资服务的删除投资活动开放方法"""
        return await self.investment.delete_investment_activity_open(*args, **kwargs)

    async def get_investment_activity_open_info(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放信息方法"""
        return await self.investment.get_investment_activity_open_info(*args, **kwargs)

    async def create_investment_activity_open(self, *args, **kwargs):
        """委托到投资服务的创建投资活动开放方法"""
        return await self.investment.create_investment_activity_open(*args, **kwargs)

    async def get_investment_activity_open_list(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放列表方法"""
        return await self.investment.get_investment_activity_open_list(*args, **kwargs)

    async def get_investment_activity_item_detail(self, *args, **kwargs):
        """委托到投资服务的获取投资活动商品详情方法"""
        return await self.investment.get_investment_activity_item_detail(
            *args, **kwargs
        )

    async def get_investment_activity_open_item_list(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放商品列表方法"""
        return await self.investment.get_investment_activity_open_item_list(
            *args, **kwargs
        )

    async def close_investment_activity_open(self, *args, **kwargs):
        """委托到投资服务的关闭投资活动开放方法"""
        return await self.investment.close_investment_activity_open(*args, **kwargs)

    async def get_investment_activity_open_promotion_effect(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放推广效果方法"""
        return await self.investment.get_investment_activity_open_promotion_effect(
            *args, **kwargs
        )

    async def get_investment_activity_invalid_item_list(self, *args, **kwargs):
        """委托到投资服务的获取投资活动无效商品列表方法"""
        return await self.investment.get_investment_activity_invalid_item_list(
            *args, **kwargs
        )

    async def query_investment_activity_exclusive_promoter_info(self, *args, **kwargs):
        """委托到投资服务的查询投资活动独家推广者信息方法"""
        return await self.investment.query_investment_activity_exclusive_promoter_info(
            *args, **kwargs
        )

    async def get_investment_my_create_activity_list(self, *args, **kwargs):
        """委托到投资服务的获取投资我的创建活动列表方法"""
        return await self.investment.get_investment_my_create_activity_list(
            *args, **kwargs
        )

    # 卖家活动服务委托方法
    async def get_seller_activity_apply_list(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动申请列表方法"""
        return await self.seller.get_seller_activity_apply_list(*args, **kwargs)

    async def get_seller_activity_promotion_effect_item(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动推广效果商品方法"""
        return await self.seller.get_seller_activity_promotion_effect_item(
            *args, **kwargs
        )

    async def get_seller_activity_usable_item(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动可用商品方法"""
        return await self.seller.get_seller_activity_usable_item(*args, **kwargs)

    async def cancel_seller_activity_apply(self, *args, **kwargs):
        """委托到卖家活动服务的取消卖家活动申请方法"""
        return await self.seller.cancel_seller_activity_apply(*args, **kwargs)

    async def get_seller_activity_open_info(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动开放信息方法"""
        return await self.seller.get_seller_activity_open_info(*args, **kwargs)

    async def get_seller_activity_item_list(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动商品列表方法"""
        return await self.seller.get_seller_activity_item_list(*args, **kwargs)

    async def get_seller_activity_open_list(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动开放列表方法"""
        return await self.seller.get_seller_activity_open_list(*args, **kwargs)

    async def query_seller_activity_exclusive_promoter_info(self, *args, **kwargs):
        """委托到卖家活动服务的查询卖家活动独家推广者信息方法"""
        return await self.seller.query_seller_activity_exclusive_promoter_info(
            *args, **kwargs
        )

    async def apply_seller_activity(self, *args, **kwargs):
        """委托到卖家活动服务的申请卖家活动方法"""
        return await self.seller.apply_seller_activity(*args, **kwargs)

    async def get_seller_activity_promotion_effect_summary(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动推广效果汇总方法"""
        return await self.seller.get_seller_activity_promotion_effect_summary(
            *args, **kwargs
        )

    async def query_seller_activity_promoter_adjust_history(self, *args, **kwargs):
        """委托到卖家活动服务的查询卖家活动推广者调整历史方法"""
        return await self.seller.query_seller_activity_promoter_adjust_history(
            *args, **kwargs
        )

    # 二级分销服务委托方法
    async def get_second_allow_investment_activity_item_list(self, *args, **kwargs):
        """委托到二级分销服务的获取二级允许投资活动商品列表方法"""
        return await self.second.get_second_allow_investment_activity_item_list(
            *args, **kwargs
        )

    async def get_second_apply_investment_activity_list(self, *args, **kwargs):
        """委托到二级分销服务的获取二级申请投资活动列表方法"""
        return await self.second.get_second_apply_investment_activity_list(
            *args, **kwargs
        )

    async def cancel_second_cooperation(self, *args, **kwargs):
        """委托到二级分销服务的取消二级合作方法"""
        return await self.second.cancel_second_cooperation(*args, **kwargs)

    async def apply_again_second_investment_activity(self, *args, **kwargs):
        """委托到二级分销服务的重新申请二级投资活动方法"""
        return await self.second.apply_again_second_investment_activity(*args, **kwargs)

    async def handle_second_cooperation(self, *args, **kwargs):
        """委托到二级分销服务的处理二级合作方法"""
        return await self.second.handle_second_cooperation(*args, **kwargs)

    # ==================== 基础分销功能 API ====================

    async def create_distribute_plan(
        self,
        access_token: str,
        plan_create_type: Optional[str] = None,
        normal_plan_param: Optional[Dict[str, Any]] = None,
        exclusive_plan_param: Optional[Dict[str, Any]] = None,
        orientation_plan_param: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> DistributePlanCreateResponse:
        """创建分销计划

        OpenAPI: `open.distribution.plan.create` (POST)
        Java: OpenDistributionPlanCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanCreateRequest.java`

        Args:
            access_token: 访问令牌。
            plan_create_type: 计划创建类型（可选）。
            normal_plan_param: 普通计划参数（可选）。
            exclusive_plan_param: 独家计划参数（可选）。
            orientation_plan_param: 定向计划参数（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributePlanCreateResponse: 分销计划创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributePlanCreateRequest(
            access_token=access_token,
            uid=uid,
            plan_create_type=plan_create_type,
            normal_plan_param=normal_plan_param,
            exclusive_plan_param=exclusive_plan_param,
            orientation_plan_param=orientation_plan_param,
            api_version="1",
        )
        return await self._client.execute(request, DistributePlanCreateResponse)

    async def update_distribute_plan(
        self,
        access_token: str,
        plan_id: Optional[int] = None,
        update_type: Optional[str] = None,
        update_plan_status_param: Optional[Dict[str, Any]] = None,
        update_normal_commission_param: Optional[Dict[str, Any]] = None,
        update_orientation_commission_param: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> DistributePlanUpdateResponse:
        """更新分销计划

        OpenAPI: `open.distribution.plan.update` (POST)
        Java: OpenDistributionPlanUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanUpdateRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID（可选）。
            update_type: 更新类型（可选）。
            update_plan_status_param: 更新计划状态参数（可选）。
            update_normal_commission_param: 更新普通佣金参数（可选）。
            update_orientation_commission_param: 更新定向佣金参数（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributePlanUpdateResponse: 分销计划更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributePlanUpdateRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            update_type=update_type,
            update_plan_status_param=update_plan_status_param,
            update_normal_commission_param=update_normal_commission_param,
            update_orientation_commission_param=update_orientation_commission_param,
            api_version="1",
        )
        return await self._client.execute(request, DistributePlanUpdateResponse)

    async def query_plan(
        self,
        access_token: str,
        item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> PlanQueryResponse:
        """查询分销计划

        OpenAPI: `open.distribution.plan.query` (GET)
        Java: OpenDistributionPlanQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanQueryRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PlanQueryResponse: 分销计划信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = PlanQueryRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )
        return await self._client.execute(request, PlanQueryResponse)

    async def query_plan_commission(
        self,
        access_token: str,
        plan_id: int,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> PlanCommissionQueryResponse:
        """查询分销计划佣金

        OpenAPI: `open.distribution.plan.commission.query` (GET)
        Java: OpenDistributionPlanCommissionQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanCommissionQueryRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID。
            pcursor: 分页游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PlanCommissionQueryResponse: 佣金明细或汇总数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = PlanCommissionQueryRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            pcursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, PlanCommissionQueryResponse)

    async def add_distribution_plan_promoter(
        self,
        access_token: str,
        plan_id: int,
        promoter_ids: List[int],
        uid: Optional[int] = None,
    ) -> DistributionPlanAddPromoterResponse:
        """添加分销计划推广者

        OpenAPI: `open.distribution.distribution.plan.add.promoter` (GET)
        Java: OpenDistributionDistributionPlanAddPromoterRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionDistributionPlanAddPromoterRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID。
            promoter_ids: 推广者ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionPlanAddPromoterResponse: 添加推广者的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionPlanAddPromoterRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            promoter_ids=promoter_ids,
            api_version="1",
        )
        return await self._client.execute(request, DistributionPlanAddPromoterResponse)

    async def delete_distribution_plan_promoter(
        self,
        access_token: str,
        plan_id: int,
        promoter_ids: List[int],
        uid: Optional[int] = None,
    ) -> DistributionPlanDeletePromoterResponse:
        """删除分销计划推广者

        OpenAPI: `open.distribution.distribution.plan.delete.promoter` (GET)
        Java: OpenDistributionDistributionPlanDeletePromoterRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionDistributionPlanDeletePromoterRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID。
            promoter_ids: 推广者ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionPlanDeletePromoterResponse: 删除推广者的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionPlanDeletePromoterRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            promoter_ids=promoter_ids,
            api_version="1",
        )
        return await self._client.execute(
            request, DistributionPlanDeletePromoterResponse
        )

    async def update_promote(
        self,
        access_token: str,
        commission_id: List[int],
        status: int,
        uid: Optional[int] = None,
    ) -> PromoteUpdateResponse:
        """推广更新

        OpenAPI: `open.distribution.promote.update` (POST)
        Java: OpenDistributionPromoteUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPromoteUpdateRequest.java`

        Args:
            access_token: 访问令牌。
            commission_id: 佣金ID列表。
            status: 状态码。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromoteUpdateResponse: 推广更新处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = PromoteUpdateRequest(
            access_token=access_token,
            uid=uid,
            commission_id=commission_id,
            status=status,
            api_version="1",
        )
        return await self._client.execute(request, PromoteUpdateResponse)

    async def add_item_selection_url(
        self,
        access_token: str,
        selection_id: int,
        url: str,
        uid: Optional[int] = None,
    ) -> ItemSelectionAddUrlResponse:
        """商品选品添加URL

        OpenAPI: `open.distribution.item.selection.add.url` (GET)
        Java: OpenDistributionItemSelectionAddUrlRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionItemSelectionAddUrlRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 选品ID。
            url: URL地址。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSelectionAddUrlResponse: 添加结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = ItemSelectionAddUrlRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            url=url,
            api_version="1",
        )
        return await self._client.execute(request, ItemSelectionAddUrlResponse)

    async def add_item_shelf_url(
        self,
        access_token: str,
        shelf_id: int,
        url: str,
        uid: Optional[int] = None,
    ) -> ItemShelfAddUrlResponse:
        """商品货架添加URL

        OpenAPI: `open.distribution.item.shelf.add.url` (GET)
        Java: OpenDistributionItemShelfAddUrlRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionItemShelfAddUrlRequest.java`

        Args:
            access_token: 访问令牌。
            shelf_id: 货架ID。
            url: URL地址。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemShelfAddUrlResponse: 添加结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = ItemShelfAddUrlRequest(
            access_token=access_token,
            uid=uid,
            shelf_id=shelf_id,
            url=url,
            api_version="1",
        )
        return await self._client.execute(request, ItemShelfAddUrlResponse)

    async def query_selection_item_detail(
        self,
        access_token: str,
        selection_id: int,
        item_id: int,
        uid: Optional[int] = None,
    ) -> QuerySelectionItemDetailResponse:
        """查询选品商品详情

        OpenAPI: `open.distribution.query.selection.item.detail` (GET)
        Java: OpenDistributionQuerySelectionItemDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionQuerySelectionItemDetailRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 选品ID。
            item_id: 商品ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            QuerySelectionItemDetailResponse: 选品商品详情数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = QuerySelectionItemDetailRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            item_id=item_id,
            api_version="1",
        )
        return await self._client.execute(request, QuerySelectionItemDetailResponse)

    async def offline_distribution_selection(
        self,
        access_token: str,
        selection_id: int,
        uid: Optional[int] = None,
    ) -> DistributionSelectionOfflineResponse:
        """分销精选下线

        OpenAPI: `open.distribution.selection.offline` (POST)
        Java: OpenDistributionSelectionOfflineRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSelectionOfflineRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 精选ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionSelectionOfflineResponse: 下线操作结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionSelectionOfflineRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            api_version="1",
        )
        return await self._client.execute(request, DistributionSelectionOfflineResponse)

    async def pick_distribution_selection(
        self,
        access_token: str,
        selection_id: int,
        item_ids: List[int],
        uid: Optional[int] = None,
    ) -> DistributionSelectionPickResponse:
        """分销精选选品

        OpenAPI: `open.distribution.selection.pick` (POST)
        Java: OpenDistributionSelectionPickRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSelectionPickRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 精选ID。
            item_ids: 商品ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionSelectionPickResponse: 选品操作结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionSelectionPickRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            item_ids=item_ids,
            api_version="1",
        )
        return await self._client.execute(request, DistributionSelectionPickResponse)

    async def create_distribution_activity_item_share(
        self,
        access_token: str,
        activity_id: int,
        item_id: int,
        share_title: str,
        share_desc: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> DistributionActivityItemShareCreateResponse:
        """创建分销活动商品分享

        OpenAPI: `open.distribution.activity.item.share.create` (POST)
        Java: OpenDistributionActivityItemShareCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionActivityItemShareCreateRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动ID。
            item_id: 商品ID。
            share_title: 分享标题。
            share_desc: 分享描述（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionActivityItemShareCreateResponse: 分享创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionActivityItemShareCreateRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            item_id=item_id,
            share_title=share_title,
            share_desc=share_desc,
            api_version="1",
        )
        return await self._client.execute(
            request, DistributionActivityItemShareCreateResponse
        )

    async def get_distribution_distributor_order_list(
        self,
        access_token: str,
        distributor_id: int,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        order_status: Optional[int] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> DistributionDistributorOrderListResponse:
        """获取分销商订单列表

        OpenAPI: `open.distribution.distributor.order.list` (GET)
        Java: OpenDistributionDistributorOrderListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionDistributorOrderListRequest.java`

        Args:
            access_token: 访问令牌。
            distributor_id: 分销商ID。
            begin_time: 开始时间（毫秒）（可选）。
            end_time: 结束时间（毫秒）（可选）。
            order_status: 订单状态（可选）。
            page: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionDistributorOrderListResponse: 订单分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionDistributorOrderListRequest(
            access_token=access_token,
            uid=uid,
            distributor_id=distributor_id,
            begin_time=begin_time,
            end_time=end_time,
            order_status=order_status,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(
            request, DistributionDistributorOrderListResponse
        )

    async def get_distribution_public_category_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> DistributionPublicCategoryListResponse:
        """获取分销公开分类列表

        OpenAPI: `open.distribution.public.category.list` (GET)
        Java: OpenDistributionPublicCategoryListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPublicCategoryListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionPublicCategoryListResponse: 公开分类列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionPublicCategoryListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, DistributionPublicCategoryListResponse
        )

    async def save_distribution_seller_sample_rule(
        self,
        access_token: str,
        rule_name: str,
        rule_config: Dict[str, Any],
        uid: Optional[int] = None,
    ) -> DistributionSellerSampleRuleSaveResponse:
        """保存分销卖家样本规则

        OpenAPI: `open.distribution.seller.sample.rule.save` (POST)
        Java: OpenDistributionSellerSampleRuleSaveRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerSampleRuleSaveRequest.java`

        Args:
            access_token: 访问令牌。
            rule_name: 规则名称。
            rule_config: 规则配置。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionSellerSampleRuleSaveResponse: 保存结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionSellerSampleRuleSaveRequest(
            access_token=access_token,
            uid=uid,
            rule_name=rule_name,
            rule_config=rule_config,
            api_version="1",
        )
        return await self._client.execute(
            request, DistributionSellerSampleRuleSaveResponse
        )

    async def test_distribution(
        self,
        access_token: str,
        test_param: str,
        uid: Optional[int] = None,
    ) -> DistributionTestResponse:
        """分销测试

        OpenAPI: `open.distribution.test` (GET)
        Java: OpenDistributionTestRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionTestRequest.java`

        Args:
            access_token: 访问令牌。
            test_param: 测试参数。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionTestResponse: 测试调用结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionTestRequest(
            access_token=access_token,
            uid=uid,
            test_param=test_param,
            api_version="1",
        )
        return await self._client.execute(request, DistributionTestResponse)

    # CPS 委托方法 - 缺失的异步方法
    async def get_cps_promotion_brand_theme_brand_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题品牌列表方法"""
        return await self.cps.get_cps_promotion_brand_theme_brand_list(*args, **kwargs)

    async def get_cps_promotion_reco_topic_info(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推荐话题信息方法"""
        return await self.cps.get_cps_promotion_reco_topic_info(*args, **kwargs)

    async def get_cps_promotion_reco_topic_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推荐话题商品列表方法"""
        return await self.cps.get_cps_promotion_reco_topic_item_list(*args, **kwargs)

    async def get_cps_promotion_brand_theme_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题商品列表方法"""
        return await self.cps.get_cps_promotion_brand_theme_item_list(*args, **kwargs)

    async def get_cps_promotion_brand_theme_shop_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题店铺列表方法"""
        return await self.cps.get_cps_promotion_brand_theme_shop_list(*args, **kwargs)

    async def get_cps_promotion_reco_topic_seller_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推荐话题卖家列表方法"""
        return await self.cps.get_cps_promotion_reco_topic_seller_list(*args, **kwargs)


class SyncDistributionService:
    """同步分销服务

    整合各个分销子服务，提供完整的分销功能接口。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: SyncBaseClient):
        """初始化分销服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

        # 初始化各个子服务
        self.cps = SyncCpsService(client)
        self.investment = SyncInvestmentService(client)
        self.seller = SyncSellerActivityService(client)
        self.second = SyncSecondDistributionService(client)

    # ==================== 向后兼容的委托方法 ====================
    # 为了保持API向后兼容，将子服务方法委托到主服务

    # CPS服务委托方法
    def get_cps_order_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS订单列表方法"""
        return self.cps.get_cps_order_list(*args, **kwargs)

    def get_cps_distributor_order_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS分销商订单列表方法"""
        return self.cps.get_cps_distributor_order_list(*args, **kwargs)

    def get_cps_kwaimoney_order_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币订单列表方法"""
        return self.cps.get_cps_kwaimoney_order_list(*args, **kwargs)

    def get_cps_kwaimoney_order_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币订单详情方法"""
        return self.cps.get_cps_kwaimoney_order_detail(*args, **kwargs)

    def get_cps_pid_bind_url(self, *args, **kwargs):
        """委托到CPS服务的获取CPS PID绑定URL方法"""
        return self.cps.get_cps_pid_bind_url(*args, **kwargs)

    def transfer_cps_link(self, *args, **kwargs):
        """委托到CPS服务的转换CPS链接方法"""
        return self.cps.transfer_cps_link(*args, **kwargs)

    def get_cps_brand_theme_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题列表方法"""
        return self.cps.get_cps_brand_theme_list(*args, **kwargs)

    def get_cps_theme_entrance_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS主题入口列表方法"""
        return self.cps.get_cps_theme_entrance_list(*args, **kwargs)

    def get_cps_kwaimoney_theme_entrance_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币主题入口列表方法"""
        return self.cps.get_cps_kwaimoney_theme_entrance_list(*args, **kwargs)

    def get_cps_promotion_reco_topic_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推广推荐话题列表方法"""
        return self.cps.get_cps_promotion_reco_topic_list(*args, **kwargs)

    def get_cps_promotion_effect_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推广效果详情方法"""
        return self.cps.get_cps_promotion_effect_detail(*args, **kwargs)

    def get_cps_leader_order_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS领导者订单详情方法"""
        return self.cps.get_cps_leader_order_detail(*args, **kwargs)

    def get_cps_kwaimoney_promotion_effect_trend(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币推广效果趋势方法"""
        return self.cps.get_cps_kwaimoney_promotion_effect_trend(*args, **kwargs)

    def update_cps_kwaimoney_pid(self, *args, **kwargs):
        """委托到CPS服务的更新CPS快手货币PID方法"""
        return self.cps.update_cps_kwaimoney_pid(*args, **kwargs)

    def get_cps_selection_item_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS精选商品详情方法"""
        return self.cps.get_cps_selection_item_detail(*args, **kwargs)

    def get_kwaimoney_preheat_work_link(self, *args, **kwargs):
        """委托到CPS服务的获取快手货币预热工作链接方法"""
        return self.cps.get_kwaimoney_preheat_work_link(*args, **kwargs)

    def parse_cps_kwaimoney_link(self, *args, **kwargs):
        """委托到CPS服务的解析CPS快手货币链接方法"""
        return self.cps.parse_cps_kwaimoney_link(*args, **kwargs)

    def create_cps_kwaimoney_pid(self, *args, **kwargs):
        """委托到CPS服务的创建CPS快手货币PID方法"""
        return self.cps.create_cps_kwaimoney_pid(*args, **kwargs)

    def get_cps_kwaimoney_pid_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币PID列表方法"""
        return self.cps.get_cps_kwaimoney_pid_list(*args, **kwargs)

    def create_cps_kwaimoney_link(self, *args, **kwargs):
        """委托到CPS服务的创建CPS快手货币链接方法"""
        return self.cps.create_cps_kwaimoney_link(*args, **kwargs)

    def get_cps_kwaimoney_selection_channel_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币精选渠道列表方法"""
        return self.cps.get_cps_kwaimoney_selection_channel_list(*args, **kwargs)

    def get_kwaimoney_requirement_cursor_list(self, *args, **kwargs):
        """委托到CPS服务的获取快手货币需求游标列表方法"""
        return self.cps.get_kwaimoney_requirement_cursor_list(*args, **kwargs)

    def get_selection_list(self, *args, **kwargs):
        """委托到CPS服务的获取精选列表方法"""
        return self.cps.get_selection_list(*args, **kwargs)

    def get_cps_kwaimoney_selection_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币精选商品列表方法"""
        return self.cps.get_cps_kwaimoney_selection_item_list(*args, **kwargs)

    def get_cps_kwaimoney_theme_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS快手货币主题商品列表方法"""
        return self.cps.get_cps_kwaimoney_theme_item_list(*args, **kwargs)

    def get_cps_leader_order_cursor_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS团长订单游标列表方法"""
        return self.cps.get_cps_leader_order_cursor_list(*args, **kwargs)

    def create_cps_link(self, *args, **kwargs):
        """委托到CPS服务的创建CPS推广链接方法"""
        return self.cps.create_cps_link(*args, **kwargs)

    def create_cps_pid(self, *args, **kwargs):
        """委托到CPS服务的创建CPS推广位方法"""
        return self.cps.create_cps_pid(*args, **kwargs)

    def query_cps_pid(self, *args, **kwargs):
        """委托到CPS服务的查询CPS推广位方法"""
        return self.cps.query_cps_pid(*args, **kwargs)

    def get_cps_promoter_order_detail(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推广者订单详情方法"""
        return self.cps.get_cps_promoter_order_detail(*args, **kwargs)

    # 投资活动服务委托方法
    def adjust_investment_activity_promoter(self, *args, **kwargs):
        """委托到投资服务的调整投资活动推广者方法"""
        return self.investment.adjust_investment_activity_promoter(*args, **kwargs)

    def get_investment_sample_promoter_data(self, *args, **kwargs):
        """委托到投资服务的获取投资样本推广者数据方法"""
        return self.investment.get_investment_sample_promoter_data(*args, **kwargs)

    def create_investment_activity_item_token(self, *args, **kwargs):
        """委托到投资服务的创建投资活动商品令牌方法"""
        return self.investment.create_investment_activity_item_token(*args, **kwargs)

    def audit_investment_activity_open_item(self, *args, **kwargs):
        """委托到投资服务的审核投资活动开放商品方法"""
        return self.investment.audit_investment_activity_open_item(*args, **kwargs)

    def delete_investment_activity_open(self, *args, **kwargs):
        """委托到投资服务的删除投资活动开放方法"""
        return self.investment.delete_investment_activity_open(*args, **kwargs)

    def create_investment_activity_open(self, *args, **kwargs):
        """委托到投资服务的创建投资活动开放方法"""
        return self.investment.create_investment_activity_open(*args, **kwargs)

    def get_investment_activity_open_info(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放信息方法"""
        return self.investment.get_investment_activity_open_info(*args, **kwargs)

    def get_investment_activity_open_list(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放列表方法"""
        return self.investment.get_investment_activity_open_list(*args, **kwargs)

    def get_investment_activity_item_detail(self, *args, **kwargs):
        """委托到投资服务的获取投资活动商品详情方法"""
        return self.investment.get_investment_activity_item_detail(*args, **kwargs)

    def get_investment_activity_open_item_list(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放商品列表方法"""
        return self.investment.get_investment_activity_open_item_list(*args, **kwargs)

    def close_investment_activity_open(self, *args, **kwargs):
        """委托到投资服务的关闭投资活动开放方法"""
        return self.investment.close_investment_activity_open(*args, **kwargs)

    def get_investment_activity_open_promotion_effect(self, *args, **kwargs):
        """委托到投资服务的获取投资活动开放推广效果方法"""
        return self.investment.get_investment_activity_open_promotion_effect(
            *args, **kwargs
        )

    def get_investment_activity_invalid_item_list(self, *args, **kwargs):
        """委托到投资服务的获取投资活动无效商品列表方法"""
        return self.investment.get_investment_activity_invalid_item_list(
            *args, **kwargs
        )

    def query_investment_activity_exclusive_promoter_info(self, *args, **kwargs):
        """委托到投资服务的查询投资活动独家推广者信息方法"""
        return self.investment.query_investment_activity_exclusive_promoter_info(
            *args, **kwargs
        )

    def get_investment_my_create_activity_list(self, *args, **kwargs):
        """委托到投资服务的获取投资我的创建活动列表方法"""
        return self.investment.get_investment_my_create_activity_list(*args, **kwargs)

    # 卖家活动服务委托方法
    def get_seller_activity_apply_list(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动申请列表方法"""
        return self.seller.get_seller_activity_apply_list(*args, **kwargs)

    def get_seller_activity_promotion_effect_item(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动推广效果商品方法"""
        return self.seller.get_seller_activity_promotion_effect_item(*args, **kwargs)

    def get_seller_activity_usable_item(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动可用商品方法"""
        return self.seller.get_seller_activity_usable_item(*args, **kwargs)

    def cancel_seller_activity_apply(self, *args, **kwargs):
        """委托到卖家活动服务的取消卖家活动申请方法"""
        return self.seller.cancel_seller_activity_apply(*args, **kwargs)

    def get_seller_activity_open_info(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动开放信息方法"""
        return self.seller.get_seller_activity_open_info(*args, **kwargs)

    def get_seller_activity_item_list(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动商品列表方法"""
        return self.seller.get_seller_activity_item_list(*args, **kwargs)

    def get_seller_activity_open_list(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动开放列表方法"""
        return self.seller.get_seller_activity_open_list(*args, **kwargs)

    def get_seller_activity_promotion_effect_summary(self, *args, **kwargs):
        """委托到卖家活动服务的获取卖家活动推广效果汇总方法"""
        return self.seller.get_seller_activity_promotion_effect_summary(*args, **kwargs)

    def query_seller_activity_promoter_adjust_history(self, *args, **kwargs):
        """委托到卖家活动服务的查询卖家活动推广者调整历史方法"""
        return self.seller.query_seller_activity_promoter_adjust_history(
            *args, **kwargs
        )

    def query_seller_activity_exclusive_promoter_info(self, *args, **kwargs):
        """委托到卖家活动服务的查询卖家活动独家推广者信息方法"""
        return self.seller.query_seller_activity_exclusive_promoter_info(
            *args, **kwargs
        )

    # 二级分销服务委托方法
    def get_second_allow_investment_activity_item_list(self, *args, **kwargs):
        """委托到二级分销服务的获取二级允许投资活动商品列表方法"""
        return self.second.get_second_allow_investment_activity_item_list(
            *args, **kwargs
        )

    def get_second_apply_investment_activity_list(self, *args, **kwargs):
        """委托到二级分销服务的获取二级申请投资活动列表方法"""
        return self.second.get_second_apply_investment_activity_list(*args, **kwargs)

    def cancel_second_cooperation(self, *args, **kwargs):
        """委托到二级分销服务的取消二级合作方法"""
        return self.second.cancel_second_cooperation(*args, **kwargs)

    def apply_again_second_investment_activity(self, *args, **kwargs):
        """委托到二级分销服务的重新申请二级投资活动方法"""
        return self.second.apply_again_second_investment_activity(*args, **kwargs)

    def handle_second_cooperation(self, *args, **kwargs):
        """委托到二级分销服务的处理二级合作方法"""
        return self.second.handle_second_cooperation(*args, **kwargs)

    # ==================== 基础分销功能 API ====================

    def create_distribute_plan(
        self,
        access_token: str,
        plan_create_type: Optional[str] = None,
        normal_plan_param: Optional[Dict[str, Any]] = None,
        exclusive_plan_param: Optional[Dict[str, Any]] = None,
        orientation_plan_param: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> DistributePlanCreateResponse:
        """创建分销计划

        OpenAPI: `open.distribution.plan.create` (POST)
        Java: OpenDistributionPlanCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanCreateRequest.java`

        Args:
            access_token: 访问令牌。
            plan_create_type: 计划创建类型（可选）。
            normal_plan_param: 普通计划参数（可选）。
            exclusive_plan_param: 独家计划参数（可选）。
            orientation_plan_param: 定向计划参数（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributePlanCreateResponse: 分销计划创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributePlanCreateRequest(
            access_token=access_token,
            uid=uid,
            plan_create_type=plan_create_type,
            normal_plan_param=normal_plan_param,
            exclusive_plan_param=exclusive_plan_param,
            orientation_plan_param=orientation_plan_param,
            api_version="1",
        )
        return self._client.execute(request, DistributePlanCreateResponse)

    def update_distribute_plan(
        self,
        access_token: str,
        plan_id: Optional[int] = None,
        update_type: Optional[str] = None,
        update_plan_status_param: Optional[Dict[str, Any]] = None,
        update_normal_commission_param: Optional[Dict[str, Any]] = None,
        update_orientation_commission_param: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> DistributePlanUpdateResponse:
        """更新分销计划

        OpenAPI: `open.distribution.plan.update` (POST)
        Java: OpenDistributionPlanUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanUpdateRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID（可选）。
            update_type: 更新类型（可选）。
            update_plan_status_param: 更新计划状态参数（可选）。
            update_normal_commission_param: 更新普通佣金参数（可选）。
            update_orientation_commission_param: 更新定向佣金参数（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributePlanUpdateResponse: 分销计划更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributePlanUpdateRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            update_type=update_type,
            update_plan_status_param=update_plan_status_param,
            update_normal_commission_param=update_normal_commission_param,
            update_orientation_commission_param=update_orientation_commission_param,
            api_version="1",
        )
        return self._client.execute(request, DistributePlanUpdateResponse)

    def query_plan(
        self,
        access_token: str,
        item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> PlanQueryResponse:
        """查询分销计划

        OpenAPI: `open.distribution.plan.query` (GET)
        Java: OpenDistributionPlanQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanQueryRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PlanQueryResponse: 分销计划信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = PlanQueryRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )
        return self._client.execute(request, PlanQueryResponse)

    def query_plan_commission(
        self,
        access_token: str,
        plan_id: int,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> PlanCommissionQueryResponse:
        """查询分销计划佣金

        OpenAPI: `open.distribution.plan.commission.query` (GET)
        Java: OpenDistributionPlanCommissionQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPlanCommissionQueryRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID。
            pcursor: 分页游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PlanCommissionQueryResponse: 佣金明细或汇总数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = PlanCommissionQueryRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, PlanCommissionQueryResponse)

    def add_distribution_plan_promoter(
        self,
        access_token: str,
        plan_id: int,
        promoter_ids: List[int],
        uid: Optional[int] = None,
    ) -> DistributionPlanAddPromoterResponse:
        """添加分销计划推广者

        OpenAPI: `open.distribution.distribution.plan.add.promoter` (GET)
        Java: OpenDistributionDistributionPlanAddPromoterRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionDistributionPlanAddPromoterRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID。
            promoter_ids: 推广者ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionPlanAddPromoterResponse: 添加推广者的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionPlanAddPromoterRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            promoter_ids=promoter_ids,
            api_version="1",
        )
        return self._client.execute(request, DistributionPlanAddPromoterResponse)

    def delete_distribution_plan_promoter(
        self,
        access_token: str,
        plan_id: int,
        promoter_ids: List[int],
        uid: Optional[int] = None,
    ) -> DistributionPlanDeletePromoterResponse:
        """删除分销计划推广者

        OpenAPI: `open.distribution.distribution.plan.delete.promoter` (GET)
        Java: OpenDistributionDistributionPlanDeletePromoterRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionDistributionPlanDeletePromoterRequest.java`

        Args:
            access_token: 访问令牌。
            plan_id: 计划ID。
            promoter_ids: 推广者ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionPlanDeletePromoterResponse: 删除推广者的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionPlanDeletePromoterRequest(
            access_token=access_token,
            uid=uid,
            plan_id=plan_id,
            promoter_ids=promoter_ids,
            api_version="1",
        )
        return self._client.execute(request, DistributionPlanDeletePromoterResponse)

    def update_promote(
        self,
        access_token: str,
        commission_id: List[int],
        status: int,
        uid: Optional[int] = None,
    ) -> PromoteUpdateResponse:
        """推广更新

        OpenAPI: `open.distribution.promote.update` (POST)
        Java: OpenDistributionPromoteUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPromoteUpdateRequest.java`

        Args:
            access_token: 访问令牌。
            commission_id: 佣金ID列表。
            status: 状态码。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromoteUpdateResponse: 推广更新处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = PromoteUpdateRequest(
            access_token=access_token,
            uid=uid,
            commission_id=commission_id,
            status=status,
            api_version="1",
        )
        return self._client.execute(request, PromoteUpdateResponse)

    def add_item_selection_url(
        self,
        access_token: str,
        selection_id: int,
        url: str,
        uid: Optional[int] = None,
    ) -> ItemSelectionAddUrlResponse:
        """商品选品添加URL

        OpenAPI: `open.distribution.item.selection.add.url` (GET)
        Java: OpenDistributionItemSelectionAddUrlRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionItemSelectionAddUrlRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 选品ID。
            url: URL地址。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSelectionAddUrlResponse: 添加结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = ItemSelectionAddUrlRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            url=url,
            api_version="1",
        )
        return self._client.execute(request, ItemSelectionAddUrlResponse)

    def add_item_shelf_url(
        self,
        access_token: str,
        shelf_id: int,
        url: str,
        uid: Optional[int] = None,
    ) -> ItemShelfAddUrlResponse:
        """商品货架添加URL

        OpenAPI: `open.distribution.item.shelf.add.url` (GET)
        Java: OpenDistributionItemShelfAddUrlRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionItemShelfAddUrlRequest.java`

        Args:
            access_token: 访问令牌。
            shelf_id: 货架ID。
            url: URL地址。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemShelfAddUrlResponse: 添加结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = ItemShelfAddUrlRequest(
            access_token=access_token,
            uid=uid,
            shelf_id=shelf_id,
            url=url,
            api_version="1",
        )
        return self._client.execute(request, ItemShelfAddUrlResponse)

    def query_selection_item_detail(
        self,
        access_token: str,
        selection_id: int,
        item_id: int,
        uid: Optional[int] = None,
    ) -> QuerySelectionItemDetailResponse:
        """查询选品商品详情

        OpenAPI: `open.distribution.query.selection.item.detail` (GET)
        Java: OpenDistributionQuerySelectionItemDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionQuerySelectionItemDetailRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 选品ID。
            item_id: 商品ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            QuerySelectionItemDetailResponse: 选品商品详情数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = QuerySelectionItemDetailRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            item_id=item_id,
            api_version="1",
        )
        return self._client.execute(request, QuerySelectionItemDetailResponse)

    def offline_distribution_selection(
        self,
        access_token: str,
        selection_id: int,
        uid: Optional[int] = None,
    ) -> DistributionSelectionOfflineResponse:
        """分销精选下线

        OpenAPI: `open.distribution.selection.offline` (POST)
        Java: OpenDistributionSelectionOfflineRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSelectionOfflineRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 精选ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionSelectionOfflineResponse: 下线操作结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionSelectionOfflineRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            api_version="1",
        )
        return self._client.execute(request, DistributionSelectionOfflineResponse)

    def pick_distribution_selection(
        self,
        access_token: str,
        selection_id: int,
        item_ids: List[int],
        uid: Optional[int] = None,
    ) -> DistributionSelectionPickResponse:
        """分销精选选品

        OpenAPI: `open.distribution.selection.pick` (POST)
        Java: OpenDistributionSelectionPickRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSelectionPickRequest.java`

        Args:
            access_token: 访问令牌。
            selection_id: 精选ID。
            item_ids: 商品ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionSelectionPickResponse: 选品操作结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionSelectionPickRequest(
            access_token=access_token,
            uid=uid,
            selection_id=selection_id,
            item_ids=item_ids,
            api_version="1",
        )
        return self._client.execute(request, DistributionSelectionPickResponse)

    def create_distribution_activity_item_share(
        self,
        access_token: str,
        activity_id: int,
        item_id: int,
        share_title: str,
        share_desc: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> DistributionActivityItemShareCreateResponse:
        """创建分销活动商品分享

        OpenAPI: `open.distribution.activity.item.share.create` (POST)
        Java: OpenDistributionActivityItemShareCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionActivityItemShareCreateRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动ID。
            item_id: 商品ID。
            share_title: 分享标题。
            share_desc: 分享描述（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionActivityItemShareCreateResponse: 分享创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionActivityItemShareCreateRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            item_id=item_id,
            share_title=share_title,
            share_desc=share_desc,
            api_version="1",
        )
        return self._client.execute(
            request, DistributionActivityItemShareCreateResponse
        )

    def get_distribution_distributor_order_list(
        self,
        access_token: str,
        distributor_id: int,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        order_status: Optional[int] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> DistributionDistributorOrderListResponse:
        """获取分销商订单列表

        OpenAPI: `open.distribution.distributor.order.list` (GET)
        Java: OpenDistributionDistributorOrderListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionDistributorOrderListRequest.java`

        Args:
            access_token: 访问令牌。
            distributor_id: 分销商ID。
            begin_time: 开始时间（毫秒）（可选）。
            end_time: 结束时间（毫秒）（可选）。
            order_status: 订单状态（可选）。
            page: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionDistributorOrderListResponse: 订单分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionDistributorOrderListRequest(
            access_token=access_token,
            uid=uid,
            distributor_id=distributor_id,
            begin_time=begin_time,
            end_time=end_time,
            order_status=order_status,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, DistributionDistributorOrderListResponse)

    def get_distribution_public_category_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> DistributionPublicCategoryListResponse:
        """获取分销公开分类列表

        OpenAPI: `open.distribution.public.category.list` (GET)
        Java: OpenDistributionPublicCategoryListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPublicCategoryListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionPublicCategoryListResponse: 公开分类列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionPublicCategoryListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, DistributionPublicCategoryListResponse)

    def save_distribution_seller_sample_rule(
        self,
        access_token: str,
        rule_name: str,
        rule_config: Dict[str, Any],
        uid: Optional[int] = None,
    ) -> DistributionSellerSampleRuleSaveResponse:
        """保存分销卖家样本规则

        OpenAPI: `open.distribution.seller.sample.rule.save` (POST)
        Java: OpenDistributionSellerSampleRuleSaveRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerSampleRuleSaveRequest.java`

        Args:
            access_token: 访问令牌。
            rule_name: 规则名称。
            rule_config: 规则配置。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionSellerSampleRuleSaveResponse: 保存结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionSellerSampleRuleSaveRequest(
            access_token=access_token,
            uid=uid,
            rule_name=rule_name,
            rule_config=rule_config,
            api_version="1",
        )
        return self._client.execute(request, DistributionSellerSampleRuleSaveResponse)

    def test_distribution(
        self,
        access_token: str,
        test_param: str,
        uid: Optional[int] = None,
    ) -> DistributionTestResponse:
        """分销测试

        OpenAPI: `open.distribution.test` (GET)
        Java: OpenDistributionTestRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionTestRequest.java`

        Args:
            access_token: 访问令牌。
            test_param: 测试参数。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            DistributionTestResponse: 测试调用结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = DistributionTestRequest(
            access_token=access_token,
            uid=uid,
            test_param=test_param,
            api_version="1",
        )
        return self._client.execute(request, DistributionTestResponse)

    # CPS 委托方法 - 缺失的同步方法
    def get_cps_promotion_brand_theme_brand_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题品牌列表方法"""
        return self.cps.get_cps_promotion_brand_theme_brand_list(*args, **kwargs)

    def get_cps_promotion_reco_topic_info(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推荐话题信息方法"""
        return self.cps.get_cps_promotion_reco_topic_info(*args, **kwargs)

    def get_cps_promotion_reco_topic_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推荐话题商品列表方法"""
        return self.cps.get_cps_promotion_reco_topic_item_list(*args, **kwargs)

    def get_cps_promotion_brand_theme_item_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题商品列表方法"""
        return self.cps.get_cps_promotion_brand_theme_item_list(*args, **kwargs)

    def get_cps_promotion_brand_theme_shop_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS品牌主题店铺列表方法"""
        return self.cps.get_cps_promotion_brand_theme_shop_list(*args, **kwargs)

    def get_cps_promotion_reco_topic_seller_list(self, *args, **kwargs):
        """委托到CPS服务的获取CPS推荐话题卖家列表方法"""
        return self.cps.get_cps_promotion_reco_topic_seller_list(*args, **kwargs)
