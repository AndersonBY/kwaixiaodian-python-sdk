"""CPS管理服务

提供CPS订单、推广位、链接、精选商品等管理功能。
"""

from typing import Dict, List, Optional

from ....models.distribution import (
    CpsBrandThemeListRequest,
    CpsBrandThemeListResponse,
    CpsDistributorOrderCommentListRequest,
    CpsDistributorOrderCommentListResponse,
    CpsDistributorOrderListRequest,
    CpsDistributorOrderListResponse,
    CpsKwaimoneyLinkCreateRequest,
    CpsKwaimoneyLinkCreateResponse,
    CpsKwaimoneyLinkParseRequest,
    CpsKwaimoneyLinkParseResponse,
    CpsKwaimoneyOrderDetailRequest,
    CpsKwaimoneyOrderDetailResponse,
    CpsKwaimoneyOrderListRequest,
    CpsKwaimoneyOrderListResponse,
    CpsKwaimoneyPidCreateRequest,
    CpsKwaimoneyPidCreateResponse,
    CpsKwaimoneyPidListRequest,
    CpsKwaimoneyPidListResponse,
    CpsKwaimoneyPidUpdateRequest,
    CpsKwaimoneyPidUpdateResponse,
    CpsKwaimoneyPromotionEffectTrendRequest,
    CpsKwaimoneyPromotionEffectTrendResponse,
    CpsKwaimoneySelectionChannelListRequest,
    CpsKwaimoneySelectionChannelListResponse,
    CpsKwaimoneySelectionItemListRequest,
    CpsKwaimoneySelectionItemListResponse,
    CpsKwaimoneyThemeEntranceListRequest,
    CpsKwaimoneyThemeEntranceListResponse,
    CpsKwaimoneyThemeItemListRequest,
    CpsKwaimoneyThemeItemListResponse,
    CpsLeaderOrderCursorListRequest,
    CpsLeaderOrderCursorListResponse,
    CpsLeaderOrderDetailRequest,
    CpsLeaderOrderDetailResponse,
    CpsLinkCreateRequest,
    CpsLinkCreateResponse,
    CpsLinkTransferRequest,
    CpsLinkTransferResponse,
    CpsOrderListRequest,
    CpsOrderListResponse,
    CpsPidBindUrlRequest,
    CpsPidBindUrlResponse,
    CpsPidCreateRequest,
    CpsPidCreateResponse,
    CpsPidQueryRequest,
    CpsPidQueryResponse,
    CpsPromoterOrderDetailRequest,
    CpsPromoterOrderDetailResponse,
    CpsPromotionBrandThemeBrandListRequest,
    CpsPromotionBrandThemeBrandListResponse,
    CpsPromotionBrandThemeItemListRequest,
    CpsPromotionBrandThemeItemListResponse,
    CpsPromotionBrandThemeShopListRequest,
    CpsPromotionBrandThemeShopListResponse,
    CpsPromotionEffectDetailRequest,
    CpsPromotionEffectDetailResponse,
    CpsPromotionRecoTopicInfoRequest,
    CpsPromotionRecoTopicInfoResponse,
    CpsPromotionRecoTopicItemListRequest,
    CpsPromotionRecoTopicItemListResponse,
    CpsPromotionRecoTopicListRequest,
    CpsPromotionRecoTopicListResponse,
    CpsPromotionRecoTopicSellerListRequest,
    CpsPromotionRecoTopicSellerListResponse,
    CpsPromotionThemeItemListRequest,
    CpsPromotionThemeItemListResponse,
    CpsSelectionItemDetailRequest,
    CpsSelectionItemDetailResponse,
    CpsThemeEntranceListRequest,
    CpsThemeEntranceListResponse,
    KwaimoneyAuthorityCursorListRequest,
    KwaimoneyAuthorityCursorListResponse,
    KwaimoneyItemBatchCursorListRequest,
    KwaimoneyItemBatchCursorListResponse,
    KwaimoneyLiveItemListRequest,
    KwaimoneyLiveItemListResponse,
    KwaimoneyPreheatWorkLinkRequest,
    KwaimoneyPreheatWorkLinkResponse,
    KwaimoneyRequirementBatchCursorListRequest,
    KwaimoneyRequirementBatchCursorListResponse,
    KwaimoneyRequirementCursorListRequest,
    KwaimoneyRequirementCursorListResponse,
    SelectionListRequest,
    SelectionListResponse,
    SellerOrderCpsDetailRequest,
    SellerOrderCpsDetailResponse,
)
from ...base import AsyncBaseClient, SyncBaseClient


class AsyncCpsService:
    """异步CPS管理服务

    提供CPS订单、推广位、链接、精选商品等管理功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化CPS服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def get_cps_order_list(
        self,
        access_token: str,
        current_page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        type: Optional[int] = None,
        pcursor: Optional[str] = None,
        distributor_id: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsOrderListResponse:
        """获取 CPS 订单列表

        OpenAPI: `open.seller.order.cps.list` (GET)
        Java: OpenSellerOrderCpsListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenSellerOrderCpsListRequest.java`

        Args:
            access_token: 访问令牌。
            current_page: 页码（可选）。
            page_size: 页大小（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            type: 订单类型（可选）。
            pcursor: 分页游标（可选）。
            distributor_id: 分销商ID（可选）。
            begin_time: 开始时间（毫秒）（可选）。
            end_time: 结束时间（毫秒）（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsOrderListResponse: CPS 订单分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsOrderListRequest(
            access_token=access_token,
            uid=uid,
            current_page=current_page,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            type=type,
            pcursor=pcursor,
            distributor_id=distributor_id,
            begin_time=begin_time,
            end_time=end_time,
            api_version="1",
        )
        return await self._client.execute(request, CpsOrderListResponse)

    async def get_cps_distributor_order_list(
        self,
        access_token: str,
        cps_order_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_type: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsDistributorOrderListResponse:
        """获取 CPS 分销商订单列表

        OpenAPI: `open.distribution.cps.distributor.order.cursor.list` (GET)
        Java: OpenDistributionCpsDistributorOrderCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsDistributorOrderCursorListRequest.java`

        Args:
            access_token: 访问令牌。
            cps_order_status: CPS 订单状态（可选）。
            page_size: 页面大小（可选）。
            sort_type: 排序类型（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间（毫秒）（可选）。
            end_time: 结束时间（毫秒）（可选）。
            pcursor: 分页游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsDistributorOrderListResponse: 订单游标分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsDistributorOrderListRequest(
            access_token=access_token,
            uid=uid,
            cps_order_status=cps_order_status,
            page_size=page_size,
            sort_type=sort_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            pcursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, CpsDistributorOrderListResponse)

    async def get_cps_kwaimoney_order_list(
        self,
        access_token: str,
        cps_order_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_type: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyOrderListResponse:
        """获取 CPS 快手货币订单列表

        OpenAPI: `open.distribution.cps.kwaimoney.order.list` (GET)
        Java: OpenDistributionCpsKwaimoneyOrderListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyOrderListRequest.java`

        Args:
            access_token: 访问令牌。
            cps_order_status: CPS 订单状态（可选）。
            page_size: 页面大小（可选）。
            sort_type: 排序类型（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间（毫秒）（可选）。
            end_time: 结束时间（毫秒）（可选）。
            pcursor: 分页游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyOrderListResponse: 订单游标分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyOrderListRequest(
            access_token=access_token,
            uid=uid,
            cps_order_status=cps_order_status,
            page_size=page_size,
            sort_type=sort_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            pcursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyOrderListResponse)

    async def get_cps_kwaimoney_order_detail(
        self,
        access_token: str,
        oid: List[int],
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyOrderDetailResponse:
        """获取 CPS 快手货币订单详情

        OpenAPI: `open.distribution.cps.kwaimoney.order.detail` (GET)
        Java: OpenDistributionCpsKwaimoneyOrderDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyOrderDetailRequest.java`

        Args:
            access_token: 访问令牌。
            oid: 订单ID 列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyOrderDetailResponse: 订单详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            oid=oid,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyOrderDetailResponse)

    async def get_cps_pid_bind_url(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPidBindUrlResponse:
        """获取 CPS PID 绑定 URL

        OpenAPI: `open.distribution.pid.bind.url` (GET)
        Java: OpenDistributionPidBindUrlRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPidBindUrlRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPidBindUrlResponse: 用于前往绑定推广位（PID）的 URL 信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPidBindUrlRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsPidBindUrlResponse)

    async def transfer_cps_link(
        self,
        access_token: str,
        cps_link: str,
        kwaimoney_id: List[int],
        uid: Optional[int] = None,
    ) -> CpsLinkTransferResponse:
        """转换 CPS 链接（转为快手币推广链接）

        OpenAPI: `open.distribution.cps.kwaimoney.link.transfer` (POST)
        Java: OpenDistributionCpsKwaimoneyLinkTransferRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyLinkTransferRequest.java`

        Args:
            access_token: 访问令牌。
            cps_link: 原始 CPS 推广链接。
            kwaimoney_id: 目标快手币 ID 列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsLinkTransferResponse: 转链后的链接或相关转换结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsLinkTransferRequest(
            access_token=access_token,
            uid=uid,
            cps_link=cps_link,
            kwaimoney_id=kwaimoney_id,
            api_version="1",
        )
        return await self._client.execute(request, CpsLinkTransferResponse)

    async def get_cps_brand_theme_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsBrandThemeListResponse:
        """获取 CPS 品牌主题列表

        OpenAPI: `open.distribution.cps.promotion.brand.theme.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsBrandThemeListResponse: 品牌主题列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsBrandThemeListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsBrandThemeListResponse)

    async def get_cps_theme_entrance_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsThemeEntranceListResponse:
        """获取 CPS 主题入口列表

        OpenAPI: `open.distribution.cps.promotion.theme.entrance.list` (GET)
        Java: OpenDistributionCpsPromotionThemeEntranceListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionThemeEntranceListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsThemeEntranceListResponse: 主题入口集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsThemeEntranceListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsThemeEntranceListResponse)

    async def get_cps_kwaimoney_theme_entrance_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyThemeEntranceListResponse:
        """获取 CPS 快手币主题入口列表

        OpenAPI: `open.distribution.cps.kwaimoney.theme.entrance.list` (GET)
        Java: OpenDistributionCpsKwaimoneyThemeEntranceListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyThemeEntranceListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyThemeEntranceListResponse: 快手币主题入口集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyThemeEntranceListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsKwaimoneyThemeEntranceListResponse
        )

    async def get_cps_promotion_reco_topic_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicListResponse:
        """获取 CPS 推广推荐话题列表

        OpenAPI: `open.distribution.cps.promotion.reco.topic.list` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionRecoTopicListResponse: 推荐话题列表与元数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionRecoTopicListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsPromotionRecoTopicListResponse)

    async def get_cps_promotion_effect_detail(
        self,
        access_token: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        order_field: Optional[int] = None,
        order_type: Optional[int] = None,
        cps_pid: Optional[str] = None,
        link_type: Optional[str] = None,
        carrier_id: Optional[int] = None,
        buyer_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsPromotionEffectDetailResponse:
        """获取 CPS 推广效果详情

        OpenAPI: `open.distribution.cps.kwaimoney.new.promotion.effect.detail` (GET)
        Java: OpenDistributionCpsKwaimoneyNewPromotionEffectDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyNewPromotionEffectDetailRequest.java`

        Args:
            access_token: 访问令牌。
            start_time: 开始时间（字符串，毫秒）（可选）。
            end_time: 结束时间（字符串，毫秒）（可选）。
            offset: 偏移量（可选）。
            limit: 返回条数（可选）。
            order_field: 排序字段（可选）。
            order_type: 排序方式（可选）。
            cps_pid: 推广位ID（可选）。
            link_type: 链接类型（可选）。
            carrier_id: 渠道ID（可选）。
            buyer_type: 买家类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionEffectDetailResponse: 效果明细数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionEffectDetailRequest(
            access_token=access_token,
            uid=uid,
            start_time=start_time,
            end_time=end_time,
            offset=offset,
            limit=limit,
            order_field=order_field,
            order_type=order_type,
            cps_pid=cps_pid,
            link_type=link_type,
            carrier_id=carrier_id,
            buyer_type=buyer_type,
            api_version="1",
        )
        return await self._client.execute(request, CpsPromotionEffectDetailResponse)

    async def get_cps_leader_order_detail(
        self,
        access_token: str,
        order_id: int,
        seller_id: Optional[int] = None,
        fund_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsLeaderOrderDetailResponse:
        """获取 CPS 团长订单详情

        OpenAPI: `open.distribution.cps.leader.order.detail` (GET)
        Java: OpenDistributionCpsLeaderOrderDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsLeaderOrderDetailRequest.java`

        Args:
            access_token: 访问令牌。
            order_id: 订单ID。
            seller_id: 卖家ID（可选）。
            fund_type: 资金类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsLeaderOrderDetailResponse: 订单详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsLeaderOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            oid=order_id,
            seller_id=seller_id,
            fund_type=fund_type,
            api_version="1",
        )
        return await self._client.execute(request, CpsLeaderOrderDetailResponse)

    async def get_cps_kwaimoney_promotion_effect_trend(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        query_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPromotionEffectTrendResponse:
        """获取 CPS 快手货币推广效果趋势

        OpenAPI: `open.distribution.cps.kwaimoney.new.promotion.effect.trend` (GET)
        Java: OpenDistributionCpsKwaimoneyNewPromotionEffectTrendRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyNewPromotionEffectTrendRequest.java`

        Args:
            access_token: 访问令牌。
            begin_time: 开始时间（毫秒）。
            end_time: 结束时间（毫秒）。
            query_type: 查询类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyPromotionEffectTrendResponse: 趋势数据集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyPromotionEffectTrendRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            query_type=query_type,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsKwaimoneyPromotionEffectTrendResponse
        )

    async def update_cps_kwaimoney_pid(
        self,
        access_token: str,
        cps_pid: str,
        promotion_bit_name: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPidUpdateResponse:
        """更新 CPS 快手币推广位（PID）

        OpenAPI: `open.distribution.cps.kwaimoney.pid.update` (POST)
        Java: OpenDistributionCpsKwaimoneyPidUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyPidUpdateRequest.java`

        Args:
            access_token: 访问令牌。
            cps_pid: 待更新的推广位 ID。
            promotion_bit_name: 新的推广位名称。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyPidUpdateResponse: 更新结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyPidUpdateRequest(
            access_token=access_token,
            uid=uid,
            cps_pid=cps_pid,
            promotion_bit_name=promotion_bit_name,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyPidUpdateResponse)

    async def get_cps_selection_item_detail(
        self,
        access_token: str,
        item_ids: List[int],
        uid: Optional[int] = None,
    ) -> CpsSelectionItemDetailResponse:
        """获取 CPS 精选商品详情

        OpenAPI: `open.distribution.cps.kwaimoney.selection.item.detail` (GET)
        Java: OpenDistributionCpsKwaimoneySelectionItemDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneySelectionItemDetailRequest.java`

        Args:
            access_token: 访问令牌。
            item_ids: 商品 ID 列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsSelectionItemDetailResponse: 精选商品详情集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsSelectionItemDetailRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_ids,
            api_version="1",
        )
        return await self._client.execute(request, CpsSelectionItemDetailResponse)

    async def get_kwaimoney_preheat_work_link(
        self,
        access_token: str,
        preheat_work_id: int,
        uid: Optional[int] = None,
    ) -> KwaimoneyPreheatWorkLinkResponse:
        """获取快手货币预热工作链接

        OpenAPI: `open.distribution.kwaimoney.preheat.work.link` (GET)
        Java: OpenDistributionKwaimoneyPreheatWorkLinkRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyPreheatWorkLinkRequest.java`

        Args:
            access_token: 访问令牌。
            preheat_work_id: 预热工作 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            KwaimoneyPreheatWorkLinkResponse: 预热链接等信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = KwaimoneyPreheatWorkLinkRequest(
            access_token=access_token,
            uid=uid,
            preheat_work_id=preheat_work_id,
            api_version="1",
        )
        return await self._client.execute(request, KwaimoneyPreheatWorkLinkResponse)

    async def parse_cps_kwaimoney_link(
        self,
        access_token: str,
        cps_link: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyLinkParseResponse:
        """解析 CPS 快手币链接

        OpenAPI: `open.distribution.cps.kwaimoney.link.parse` (POST)
        Java: OpenDistributionCpsKwaimoneyLinkParseRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyLinkParseRequest.java`

        Args:
            access_token: 访问令牌。
            cps_link: 待解析的 CPS 链接。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyLinkParseResponse: 解析后的链接明细。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyLinkParseRequest(
            access_token=access_token,
            uid=uid,
            cps_link=cps_link,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyLinkParseResponse)

    async def create_cps_kwaimoney_pid(
        self,
        access_token: str,
        promotion_bit_name: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPidCreateResponse:
        """创建 CPS 快手币推广位（PID）

        OpenAPI: `open.distribution.cps.kwaimoney.pid.create` (POST)
        Java: OpenDistributionCpsKwaimoneyPidCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyPidCreateRequest.java`

        Args:
            access_token: 访问令牌。
            promotion_bit_name: 推广位名称。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyPidCreateResponse: 创建结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyPidCreateRequest(
            access_token=access_token,
            uid=uid,
            promotion_bit_name=promotion_bit_name,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyPidCreateResponse)

    async def get_cps_kwaimoney_pid_list(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPidListResponse:
        """获取 CPS 快手币推广位（PID）列表

        OpenAPI: `open.distribution.cps.kwaimoney.pid.list` (GET)
        Java: OpenDistributionCpsKwaimoneyPidListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyPidListRequest.java`

        Args:
            access_token: 访问令牌。
            page: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyPidListResponse: 推广位列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyPidListRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyPidListResponse)

    async def create_cps_kwaimoney_link(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyLinkCreateResponse:
        """创建 CPS 快手币推广链接

        OpenAPI: `open.distribution.cps.kwaimoney.link.create` (POST)
        Java: OpenDistributionCpsKwaimoneyLinkCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyLinkCreateRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyLinkCreateResponse: 创建后的链接信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyLinkCreateRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyLinkCreateResponse)

    async def get_cps_kwaimoney_selection_channel_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneySelectionChannelListResponse:
        """获取 CPS 快手币精选渠道列表

        OpenAPI: `open.distribution.cps.kwaimoney.selection.channel.list` (GET)
        Java: OpenDistributionCpsKwaimoneySelectionChannelListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneySelectionChannelListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneySelectionChannelListResponse: 渠道列表与元数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneySelectionChannelListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsKwaimoneySelectionChannelListResponse
        )

    async def get_kwaimoney_requirement_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyRequirementCursorListResponse:
        """获取快手币需求游标列表

        OpenAPI: `open.distribution.kwaimoney.requirement.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyRequirementCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyRequirementCursorListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            KwaimoneyRequirementCursorListResponse: 需求游标分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = KwaimoneyRequirementCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, KwaimoneyRequirementCursorListResponse
        )

    async def get_selection_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SelectionListResponse:
        """获取精选列表

        OpenAPI: `open.distribution.selection.list` (GET)
        Java: OpenDistributionSelectionListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSelectionListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SelectionListResponse: 精选列表与元数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SelectionListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, SelectionListResponse)

    # ==================== 32个缺失的async方法 ====================

    async def get_cps_kwaimoney_selection_item_list(
        self,
        access_token: str,
        range_list: Optional[List[Dict]] = None,
        sort_type: Optional[str] = None,
        page_index: Optional[str] = None,
        channel_id: Optional[List[int]] = None,
        page_size: Optional[int] = None,
        express_type: Optional[int] = None,
        plan_type: Optional[int] = None,
        keyword: Optional[str] = None,
        item_level: Optional[str] = None,
        seller_id: Optional[int] = None,
        item_tag: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneySelectionItemListResponse:
        """获取 CPS 快手币精选商品列表

        OpenAPI: `open.distribution.cps.kwaimoney.selection.item.list` (GET)
        Java: OpenDistributionCpsKwaimoneySelectionItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneySelectionItemListRequest.java`

        Args:
            access_token: 访问令牌。
            range_list: 范围过滤（可选）。
            sort_type: 排序类型（可选）。
            page_index: 页索引（可选）。
            channel_id: 渠道 ID 列表（可选）。
            page_size: 页面大小（可选）。
            express_type: 物流类型（可选）。
            plan_type: 计划类型（可选）。
            keyword: 关键词（可选）。
            item_level: 商品等级（可选）。
            seller_id: 商家 ID（可选）。
            item_tag: 商品标签（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneySelectionItemListResponse: 精选商品列表与分页。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneySelectionItemListRequest(
            access_token=access_token,
            uid=uid,
            range_list=range_list,
            sort_type=sort_type,
            page_index=page_index,
            channel_id=channel_id,
            page_size=page_size,
            express_type=express_type,
            plan_type=plan_type,
            keyword=keyword,
            item_level=item_level,
            seller_id=seller_id,
            item_tag=item_tag,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsKwaimoneySelectionItemListResponse
        )

    async def get_cps_kwaimoney_theme_item_list(
        self,
        access_token: str,
        theme_id: Optional[int] = None,
        sub_theme_id: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyThemeItemListResponse:
        """获取 CPS 快手币主题商品列表

        OpenAPI: `open.distribution.cps.kwaimoney.theme.item.list` (GET)
        Java: OpenDistributionCpsKwaimoneyThemeItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyThemeItemListRequest.java`

        Args:
            access_token: 访问令牌。
            theme_id: 主题 ID（可选）。
            sub_theme_id: 子主题 ID（可选）。
            pcursor: 分页游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsKwaimoneyThemeItemListResponse: 主题商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsKwaimoneyThemeItemListRequest(
            access_token=access_token,
            uid=uid,
            theme_id=theme_id,
            sub_theme_id=sub_theme_id,
            pcursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, CpsKwaimoneyThemeItemListResponse)

    async def get_cps_leader_order_cursor_list(
        self,
        access_token: str,
        cps_order_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_type: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsLeaderOrderCursorListResponse:
        """获取 CPS 团长订单游标列表

        OpenAPI: `open.distribution.cps.leader.order.cursor.list` (GET)
        Java: OpenDistributionCpsLeaderOrderCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsLeaderOrderCursorListRequest.java`

        Args:
            access_token: 访问令牌。
            cps_order_status: CPS 订单状态（可选）。
            page_size: 页面大小（可选）。
            sort_type: 排序类型（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间（毫秒）（可选）。
            end_time: 结束时间（毫秒）（可选）。
            pcursor: 分页游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsLeaderOrderCursorListResponse: 订单游标分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsLeaderOrderCursorListRequest(
            access_token=access_token,
            uid=uid,
            cps_order_status=cps_order_status,
            page_size=page_size,
            sort_type=sort_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            pcursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, CpsLeaderOrderCursorListResponse)

    async def create_cps_link(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsLinkCreateResponse:
        """创建 CPS 推广链接

        OpenAPI: `open.distribution.cps.link.create` (POST)
        Java: OpenDistributionCpsLinkCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsLinkCreateRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsLinkCreateResponse: 推广链接创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsLinkCreateRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsLinkCreateResponse)

    async def create_cps_pid(
        self,
        access_token: str,
        promotion_bit_name: str,
        uid: Optional[int] = None,
    ) -> CpsPidCreateResponse:
        """创建 CPS 推广位（PID）

        OpenAPI: `open.distribution.cps.pid.create` (POST)
        Java: OpenDistributionCpsPidCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPidCreateRequest.java`

        Args:
            access_token: 访问令牌。
            promotion_bit_name: 推广位名称。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPidCreateResponse: 推广位创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPidCreateRequest(
            access_token=access_token,
            uid=uid,
            promotion_bit_name=promotion_bit_name,
            api_version="1",
        )
        return await self._client.execute(request, CpsPidCreateResponse)

    async def query_cps_pid(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsPidQueryResponse:
        """查询 CPS 推广位（PID）

        OpenAPI: `open.distribution.cps.pid.query` (GET)
        Java: OpenDistributionCpsPidQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPidQueryRequest.java`

        Args:
            access_token: 访问令牌。
            page: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPidQueryResponse: 推广位列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPidQueryRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(request, CpsPidQueryResponse)

    async def get_cps_promoter_order_detail(
        self,
        access_token: str,
        order_id: str,
        uid: Optional[int] = None,
    ) -> CpsPromoterOrderDetailResponse:
        """获取 CPS 推广者订单详情

        OpenAPI: `open.distribution.cps.promoter.order.detail` (GET)
        Java: OpenDistributionCpsPromoterOrderDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromoterOrderDetailRequest.java`

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromoterOrderDetailResponse: 订单详情信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromoterOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            api_version="1",
        )
        return await self._client.execute(request, CpsPromoterOrderDetailResponse)

    async def get_cps_promotion_brand_theme_brand_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionBrandThemeBrandListResponse:
        """获取 CPS 品牌主题品牌列表

        OpenAPI: `open.distribution.cps.promotion.brand.theme.brand.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeBrandListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeBrandListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionBrandThemeBrandListResponse: 品牌主题-品牌列表数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionBrandThemeBrandListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsPromotionBrandThemeBrandListResponse
        )

    async def get_cps_promotion_brand_theme_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionBrandThemeItemListResponse:
        """获取 CPS 品牌主题商品列表

        OpenAPI: `open.distribution.cps.promotion.brand.theme.item.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionBrandThemeItemListResponse: 品牌主题下的商品列表数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionBrandThemeItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsPromotionBrandThemeItemListResponse
        )

    async def get_cps_promotion_brand_theme_shop_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionBrandThemeShopListResponse:
        """获取 CPS 品牌主题店铺列表

        OpenAPI: `open.distribution.cps.promotion.brand.theme.shop.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeShopListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeShopListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionBrandThemeShopListResponse: 品牌主题下的店铺列表数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionBrandThemeShopListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsPromotionBrandThemeShopListResponse
        )

    async def get_cps_promotion_reco_topic_info(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicInfoResponse:
        """获取 CPS 推荐话题信息

        OpenAPI: `open.distribution.cps.promotion.reco.topic.info` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicInfoRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionRecoTopicInfoResponse: 推荐话题信息与子主题等数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionRecoTopicInfoRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsPromotionRecoTopicInfoResponse)

    async def get_cps_promotion_reco_topic_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicItemListResponse:
        """获取 CPS 推荐话题商品列表

        OpenAPI: `open.distribution.cps.promotion.reco.topic.item.list` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionRecoTopicItemListResponse: 推荐话题下的商品列表数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionRecoTopicItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsPromotionRecoTopicItemListResponse
        )

    async def get_cps_promotion_reco_topic_seller_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicSellerListResponse:
        """获取 CPS 推荐话题卖家列表

        OpenAPI: `open.distribution.cps.promotion.reco.topic.seller.list` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicSellerListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicSellerListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionRecoTopicSellerListResponse: 推荐话题下的卖家列表数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionRecoTopicSellerListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsPromotionRecoTopicSellerListResponse
        )

    async def get_cps_promotion_theme_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionThemeItemListResponse:
        """获取 CPS 推广主题商品列表

        OpenAPI: `open.distribution.cps.promtion.theme.item.list` (GET)
        Java: OpenDistributionCpsPromtionThemeItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromtionThemeItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsPromotionThemeItemListResponse: 推广主题下商品列表数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsPromotionThemeItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, CpsPromotionThemeItemListResponse)

    async def get_kwaimoney_authority_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyAuthorityCursorListResponse:
        """获取 快手小店 权限游标列表

        OpenAPI: `open.distribution.kwaimoney.authority.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyAuthorityCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyAuthorityCursorListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            KwaimoneyAuthorityCursorListResponse: 权限游标分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = KwaimoneyAuthorityCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, KwaimoneyAuthorityCursorListResponse)

    async def get_kwaimoney_item_batch_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyItemBatchCursorListResponse:
        """获取 快手小店 商品批量游标列表

        OpenAPI: `open.distribution.kwaimoney.item.batch.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyItemBatchCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyItemBatchCursorListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            KwaimoneyItemBatchCursorListResponse: 商品批量游标分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = KwaimoneyItemBatchCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, KwaimoneyItemBatchCursorListResponse)

    async def get_kwaimoney_requirement_batch_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyRequirementBatchCursorListResponse:
        """获取 快手小店 需求批量游标列表

        OpenAPI: `open.distribution.kwaimoney.requirement.batch.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyRequirementBatchCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyRequirementBatchCursorListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            KwaimoneyRequirementBatchCursorListResponse: 需求批量游标分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = KwaimoneyRequirementBatchCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, KwaimoneyRequirementBatchCursorListResponse
        )

    async def get_cps_distributor_order_comment_list(
        self,
        access_token: str,
        oids: List[int],
        seller_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsDistributorOrderCommentListResponse:
        """获取 CPS 分销商订单评论列表

        OpenAPI: `open.distribution.cps.distributor.order.comment.list` (GET)
        Java: OpenDistributionCpsDistributorOrderCommentListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsDistributorOrderCommentListRequest.java`

        Args:
            access_token: 访问令牌。
            oids: 订单 ID 列表。
            seller_id: 卖家 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            CpsDistributorOrderCommentListResponse: 评论信息集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = CpsDistributorOrderCommentListRequest(
            access_token=access_token,
            uid=uid,
            oid=oids,
            seller_id=seller_id,
            api_version="1",
        )
        return await self._client.execute(
            request, CpsDistributorOrderCommentListResponse
        )

    async def get_seller_order_cps_detail(
        self,
        access_token: str,
        order_id: str,
        uid: Optional[int] = None,
    ) -> SellerOrderCpsDetailResponse:
        """获取卖家 CPS 订单详情

        OpenAPI: `open.seller.order.cps.detail` (GET)
        Java: OpenSellerOrderCpsDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenSellerOrderCpsDetailRequest.java`

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerOrderCpsDetailResponse: 订单详情数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerOrderCpsDetailRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            api_version="1",
        )
        return await self._client.execute(request, SellerOrderCpsDetailResponse)

    async def get_kwaimoney_live_item_list(
        self,
        access_token: str,
        live_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> KwaimoneyLiveItemListResponse:
        """获取快手币直播商品列表

        OpenAPI: `open.distribution.kwaimoney.live.item.list` (GET)
        Java: OpenDistributionKwaimoneyLiveItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyLiveItemListRequest.java`

        Args:
            access_token: 访问令牌。
            live_id: 直播 ID。
            page: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            KwaimoneyLiveItemListResponse: 直播关联商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = KwaimoneyLiveItemListRequest(
            access_token=access_token,
            uid=uid,
            live_id=live_id,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(request, KwaimoneyLiveItemListResponse)


class SyncCpsService:
    """同步CPS管理服务

    提供CPS订单、推广位、链接、精选商品等管理功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: SyncBaseClient):
        """初始化CPS服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def get_cps_order_list(
        self,
        access_token: str,
        current_page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        type: Optional[int] = None,
        pcursor: Optional[str] = None,
        distributor_id: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsOrderListResponse:
        """获取 CPS 订单列表（同步）

        OpenAPI: `open.seller.order.cps.list` (GET)
        Java: OpenSellerOrderCpsListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenSellerOrderCpsListRequest.java`
        """
        request = CpsOrderListRequest(
            access_token=access_token,
            uid=uid,
            current_page=current_page,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            type=type,
            pcursor=pcursor,
            distributor_id=distributor_id,
            begin_time=begin_time,
            end_time=end_time,
            api_version="1",
        )
        return self._client.execute(request, CpsOrderListResponse)

    def get_cps_distributor_order_list(
        self,
        access_token: str,
        cps_order_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_type: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsDistributorOrderListResponse:
        """获取 CPS 分销商订单列表（同步）

        OpenAPI: `open.distribution.cps.distributor.order.cursor.list` (GET)
        Java: OpenDistributionCpsDistributorOrderCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsDistributorOrderCursorListRequest.java`
        """
        request = CpsDistributorOrderListRequest(
            access_token=access_token,
            uid=uid,
            cps_order_status=cps_order_status,
            page_size=page_size,
            sort_type=sort_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, CpsDistributorOrderListResponse)

    def get_cps_kwaimoney_order_list(
        self,
        access_token: str,
        cps_order_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_type: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyOrderListResponse:
        """获取 CPS 快手货币订单列表（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.order.list` (GET)
        Java: OpenDistributionCpsKwaimoneyOrderListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyOrderListRequest.java`
        """
        request = CpsKwaimoneyOrderListRequest(
            access_token=access_token,
            uid=uid,
            cps_order_status=cps_order_status,
            page_size=page_size,
            sort_type=sort_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyOrderListResponse)

    def get_cps_kwaimoney_order_detail(
        self,
        access_token: str,
        oid: List[int],
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyOrderDetailResponse:
        """获取 CPS 快手货币订单详情（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.order.detail` (GET)
        Java: OpenDistributionCpsKwaimoneyOrderDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyOrderDetailRequest.java`
        """
        request = CpsKwaimoneyOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            oid=oid,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyOrderDetailResponse)

    def get_cps_pid_bind_url(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPidBindUrlResponse:
        """获取 CPS PID 绑定 URL（同步）

        OpenAPI: `open.distribution.pid.bind.url` (GET)
        Java: OpenDistributionPidBindUrlRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionPidBindUrlRequest.java`
        """
        request = CpsPidBindUrlRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPidBindUrlResponse)

    def transfer_cps_link(
        self,
        access_token: str,
        cps_link: str,
        kwaimoney_id: List[int],
        uid: Optional[int] = None,
    ) -> CpsLinkTransferResponse:
        """转换 CPS 链接（转为快手币推广链接，同步）

        OpenAPI: `open.distribution.cps.kwaimoney.link.transfer` (POST)
        Java: OpenDistributionCpsKwaimoneyLinkTransferRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyLinkTransferRequest.java`
        """
        request = CpsLinkTransferRequest(
            access_token=access_token,
            uid=uid,
            cps_link=cps_link,
            kwaimoney_id=kwaimoney_id,
            api_version="1",
        )
        return self._client.execute(request, CpsLinkTransferResponse)

    def get_cps_brand_theme_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsBrandThemeListResponse:
        """获取 CPS 品牌主题列表（同步）

        OpenAPI: `open.distribution.cps.promotion.brand.theme.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeListRequest.java`
        """
        request = CpsBrandThemeListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsBrandThemeListResponse)

    def get_cps_theme_entrance_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsThemeEntranceListResponse:
        """获取 CPS 主题入口列表（同步）

        OpenAPI: `open.distribution.cps.promotion.theme.entrance.list` (GET)
        Java: OpenDistributionCpsPromotionThemeEntranceListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionThemeEntranceListRequest.java`
        """
        request = CpsThemeEntranceListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsThemeEntranceListResponse)

    def get_cps_kwaimoney_theme_entrance_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyThemeEntranceListResponse:
        """获取 CPS 快手币主题入口列表（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.theme.entrance.list` (GET)
        Java: OpenDistributionCpsKwaimoneyThemeEntranceListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyThemeEntranceListRequest.java`
        """
        request = CpsKwaimoneyThemeEntranceListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyThemeEntranceListResponse)

    def get_cps_promotion_reco_topic_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicListResponse:
        """获取 CPS 推广推荐话题列表（同步）

        OpenAPI: `open.distribution.cps.promotion.reco.topic.list` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicListRequest.java`
        """
        request = CpsPromotionRecoTopicListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionRecoTopicListResponse)

    def get_cps_promotion_effect_detail(
        self,
        access_token: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        order_field: Optional[int] = None,
        order_type: Optional[int] = None,
        cps_pid: Optional[str] = None,
        link_type: Optional[str] = None,
        carrier_id: Optional[int] = None,
        buyer_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsPromotionEffectDetailResponse:
        """获取 CPS 推广效果详情（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.new.promotion.effect.detail` (GET)
        Java: OpenDistributionCpsKwaimoneyNewPromotionEffectDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyNewPromotionEffectDetailRequest.java`
        """
        request = CpsPromotionEffectDetailRequest(
            access_token=access_token,
            uid=uid,
            start_time=start_time,
            end_time=end_time,
            offset=offset,
            limit=limit,
            order_field=order_field,
            order_type=order_type,
            cps_pid=cps_pid,
            link_type=link_type,
            carrier_id=carrier_id,
            buyer_type=buyer_type,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionEffectDetailResponse)

    def get_cps_leader_order_detail(
        self,
        access_token: str,
        order_id: int,
        seller_id: Optional[int] = None,
        fund_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsLeaderOrderDetailResponse:
        """获取 CPS 团长订单详情（同步）

        OpenAPI: `open.distribution.cps.leader.order.detail` (GET)
        Java: OpenDistributionCpsLeaderOrderDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsLeaderOrderDetailRequest.java`
        """
        request = CpsLeaderOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            oid=order_id,
            seller_id=seller_id,
            fund_type=fund_type,
            api_version="1",
        )
        return self._client.execute(request, CpsLeaderOrderDetailResponse)

    def get_cps_selection_item_detail(
        self,
        access_token: str,
        item_ids: List[int],
        uid: Optional[int] = None,
    ) -> CpsSelectionItemDetailResponse:
        """获取 CPS 精选商品详情（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.selection.item.detail` (GET)
        Java: OpenDistributionCpsKwaimoneySelectionItemDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneySelectionItemDetailRequest.java`
        """
        request = CpsSelectionItemDetailRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_ids,
            api_version="1",
        )
        return self._client.execute(request, CpsSelectionItemDetailResponse)

    def get_kwaimoney_preheat_work_link(
        self,
        access_token: str,
        preheat_work_id: int,
        uid: Optional[int] = None,
    ) -> KwaimoneyPreheatWorkLinkResponse:
        """获取快手货币预热工作链接（同步）

        OpenAPI: `open.distribution.kwaimoney.preheat.work.link` (GET)
        Java: OpenDistributionKwaimoneyPreheatWorkLinkRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyPreheatWorkLinkRequest.java`
        """
        request = KwaimoneyPreheatWorkLinkRequest(
            access_token=access_token,
            uid=uid,
            preheat_work_id=preheat_work_id,
            api_version="1",
        )
        return self._client.execute(request, KwaimoneyPreheatWorkLinkResponse)

    def parse_cps_kwaimoney_link(
        self,
        access_token: str,
        cps_link: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyLinkParseResponse:
        """解析 CPS 快手币链接（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.link.parse` (POST)
        Java: OpenDistributionCpsKwaimoneyLinkParseRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyLinkParseRequest.java`
        """
        request = CpsKwaimoneyLinkParseRequest(
            access_token=access_token,
            uid=uid,
            cps_link=cps_link,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyLinkParseResponse)

    def create_cps_kwaimoney_pid(
        self,
        access_token: str,
        promotion_bit_name: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPidCreateResponse:
        """创建 CPS 快手币推广位（PID）（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.pid.create` (POST)
        Java: OpenDistributionCpsKwaimoneyPidCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyPidCreateRequest.java`
        """
        request = CpsKwaimoneyPidCreateRequest(
            access_token=access_token,
            uid=uid,
            promotion_bit_name=promotion_bit_name,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyPidCreateResponse)

    def get_cps_kwaimoney_pid_list(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPidListResponse:
        """获取 CPS 快手币推广位（PID）列表（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.pid.list` (GET)
        Java: OpenDistributionCpsKwaimoneyPidListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyPidListRequest.java`
        """
        request = CpsKwaimoneyPidListRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyPidListResponse)

    def update_cps_kwaimoney_pid(
        self,
        access_token: str,
        cps_pid: str,
        promotion_bit_name: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPidUpdateResponse:
        """更新 CPS 快手币推广位（PID）（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.pid.update` (POST)
        Java: OpenDistributionCpsKwaimoneyPidUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyPidUpdateRequest.java`
        """
        request = CpsKwaimoneyPidUpdateRequest(
            access_token=access_token,
            uid=uid,
            cps_pid=cps_pid,
            promotion_bit_name=promotion_bit_name,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyPidUpdateResponse)

    def create_cps_kwaimoney_link(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyLinkCreateResponse:
        """创建 CPS 快手币推广链接（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.link.create` (POST)
        Java: OpenDistributionCpsKwaimoneyLinkCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyLinkCreateRequest.java`
        """
        request = CpsKwaimoneyLinkCreateRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyLinkCreateResponse)

    def get_cps_kwaimoney_selection_channel_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneySelectionChannelListResponse:
        """获取 CPS 快手币精选渠道列表（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.selection.channel.list` (GET)
        Java: OpenDistributionCpsKwaimoneySelectionChannelListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneySelectionChannelListRequest.java`
        """
        request = CpsKwaimoneySelectionChannelListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneySelectionChannelListResponse)

    def get_cps_kwaimoney_promotion_effect_trend(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        query_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyPromotionEffectTrendResponse:
        """获取 CPS 快手货币推广效果趋势（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.new.promotion.effect.trend` (GET)
        Java: OpenDistributionCpsKwaimoneyNewPromotionEffectTrendRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyNewPromotionEffectTrendRequest.java`
        """
        request = CpsKwaimoneyPromotionEffectTrendRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            query_type=query_type,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyPromotionEffectTrendResponse)

    def get_kwaimoney_requirement_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyRequirementCursorListResponse:
        """获取 快手币 需求游标列表（同步）

        OpenAPI: `open.distribution.kwaimoney.requirement.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyRequirementCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyRequirementCursorListRequest.java`
        """
        request = KwaimoneyRequirementCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, KwaimoneyRequirementCursorListResponse)

    def get_selection_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SelectionListResponse:
        """获取 精选列表（同步）

        OpenAPI: `open.distribution.selection.list` (GET)
        Java: OpenDistributionSelectionListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSelectionListRequest.java`
        """
        request = SelectionListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SelectionListResponse)

    # 继续添加其他同步方法...
    # [其余同步方法与异步方法相同，只是去掉了async/await关键字]

    def get_cps_kwaimoney_selection_item_list(
        self,
        access_token: str,
        range_list: Optional[List[Dict]] = None,
        sort_type: Optional[str] = None,
        page_index: Optional[str] = None,
        channel_id: Optional[List[int]] = None,
        page_size: Optional[int] = None,
        express_type: Optional[int] = None,
        plan_type: Optional[int] = None,
        keyword: Optional[str] = None,
        item_level: Optional[str] = None,
        seller_id: Optional[int] = None,
        item_tag: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneySelectionItemListResponse:
        """获取 CPS 快手币精选商品列表（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.selection.item.list` (GET)
        Java: OpenDistributionCpsKwaimoneySelectionItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneySelectionItemListRequest.java`
        """
        request = CpsKwaimoneySelectionItemListRequest(
            access_token=access_token,
            uid=uid,
            range_list=range_list,
            sort_type=sort_type,
            page_index=page_index,
            channel_id=channel_id,
            page_size=page_size,
            express_type=express_type,
            plan_type=plan_type,
            keyword=keyword,
            item_level=item_level,
            seller_id=seller_id,
            item_tag=item_tag,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneySelectionItemListResponse)

    def get_cps_kwaimoney_theme_item_list(
        self,
        access_token: str,
        theme_id: Optional[int] = None,
        sub_theme_id: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsKwaimoneyThemeItemListResponse:
        """获取 CPS 快手币主题商品列表（同步）

        OpenAPI: `open.distribution.cps.kwaimoney.theme.item.list` (GET)
        Java: OpenDistributionCpsKwaimoneyThemeItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsKwaimoneyThemeItemListRequest.java`
        """
        request = CpsKwaimoneyThemeItemListRequest(
            access_token=access_token,
            uid=uid,
            theme_id=theme_id,
            sub_theme_id=sub_theme_id,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, CpsKwaimoneyThemeItemListResponse)

    def get_cps_leader_order_cursor_list(
        self,
        access_token: str,
        cps_order_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_type: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> CpsLeaderOrderCursorListResponse:
        """获取 CPS 团长订单游标列表（同步）

        OpenAPI: `open.distribution.cps.leader.order.cursor.list` (GET)
        Java: OpenDistributionCpsLeaderOrderCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsLeaderOrderCursorListRequest.java`
        """
        request = CpsLeaderOrderCursorListRequest(
            access_token=access_token,
            uid=uid,
            cps_order_status=cps_order_status,
            page_size=page_size,
            sort_type=sort_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, CpsLeaderOrderCursorListResponse)

    def create_cps_link(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsLinkCreateResponse:
        """创建 CPS 推广链接（同步）

        OpenAPI: `open.distribution.cps.link.create` (POST)
        Java: OpenDistributionCpsLinkCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsLinkCreateRequest.java`
        """
        request = CpsLinkCreateRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsLinkCreateResponse)

    def create_cps_pid(
        self,
        access_token: str,
        promotion_bit_name: str,
        uid: Optional[int] = None,
    ) -> CpsPidCreateResponse:
        """创建 CPS 推广位（PID）（同步）

        OpenAPI: `open.distribution.cps.pid.create` (POST)
        Java: OpenDistributionCpsPidCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPidCreateRequest.java`
        """
        request = CpsPidCreateRequest(
            access_token=access_token,
            uid=uid,
            promotion_bit_name=promotion_bit_name,
            api_version="1",
        )
        return self._client.execute(request, CpsPidCreateResponse)

    def query_cps_pid(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsPidQueryResponse:
        """查询 CPS 推广位（PID）（同步）

        OpenAPI: `open.distribution.cps.pid.query` (GET)
        Java: OpenDistributionCpsPidQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPidQueryRequest.java`
        """
        request = CpsPidQueryRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, CpsPidQueryResponse)

    def get_cps_promoter_order_detail(
        self,
        access_token: str,
        order_id: str,
        uid: Optional[int] = None,
    ) -> CpsPromoterOrderDetailResponse:
        """获取 CPS 推广者订单详情（同步）

        OpenAPI: `open.distribution.cps.promoter.order.detail` (GET)
        Java: OpenDistributionCpsPromoterOrderDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromoterOrderDetailRequest.java`
        """
        request = CpsPromoterOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            api_version="1",
        )
        return self._client.execute(request, CpsPromoterOrderDetailResponse)

    def get_cps_promotion_brand_theme_brand_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionBrandThemeBrandListResponse:
        """获取 CPS 品牌主题品牌列表（同步）

        OpenAPI: `open.distribution.cps.promotion.brand.theme.brand.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeBrandListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeBrandListRequest.java`
        """
        request = CpsPromotionBrandThemeBrandListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionBrandThemeBrandListResponse)

    def get_cps_promotion_brand_theme_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionBrandThemeItemListResponse:
        """获取 CPS 品牌主题商品列表（同步）

        OpenAPI: `open.distribution.cps.promotion.brand.theme.item.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeItemListRequest.java`
        """
        request = CpsPromotionBrandThemeItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionBrandThemeItemListResponse)

    def get_cps_promotion_brand_theme_shop_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionBrandThemeShopListResponse:
        """获取 CPS 品牌主题店铺列表（同步）

        OpenAPI: `open.distribution.cps.promotion.brand.theme.shop.list` (GET)
        Java: OpenDistributionCpsPromotionBrandThemeShopListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionBrandThemeShopListRequest.java`
        """
        request = CpsPromotionBrandThemeShopListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionBrandThemeShopListResponse)

    def get_cps_promotion_reco_topic_info(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicInfoResponse:
        """获取 CPS 推荐话题信息（同步）

        OpenAPI: `open.distribution.cps.promotion.reco.topic.info` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicInfoRequest.java`
        """
        request = CpsPromotionRecoTopicInfoRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionRecoTopicInfoResponse)

    def get_cps_promotion_reco_topic_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicItemListResponse:
        """获取 CPS 推荐话题商品列表（同步）

        OpenAPI: `open.distribution.cps.promotion.reco.topic.item.list` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicItemListRequest.java`
        """
        request = CpsPromotionRecoTopicItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionRecoTopicItemListResponse)

    def get_cps_promotion_reco_topic_seller_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionRecoTopicSellerListResponse:
        """获取 CPS 推荐话题卖家列表（同步）

        OpenAPI: `open.distribution.cps.promotion.reco.topic.seller.list` (GET)
        Java: OpenDistributionCpsPromotionRecoTopicSellerListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromotionRecoTopicSellerListRequest.java`
        """
        request = CpsPromotionRecoTopicSellerListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionRecoTopicSellerListResponse)

    def get_cps_promotion_theme_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> CpsPromotionThemeItemListResponse:
        """获取 CPS 推广主题商品列表（同步）

        OpenAPI: `open.distribution.cps.promtion.theme.item.list` (GET)
        Java: OpenDistributionCpsPromtionThemeItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsPromtionThemeItemListRequest.java`
        """
        request = CpsPromotionThemeItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, CpsPromotionThemeItemListResponse)

    def get_kwaimoney_authority_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyAuthorityCursorListResponse:
        """获取 快手小店 权限游标列表（同步）

        OpenAPI: `open.distribution.kwaimoney.authority.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyAuthorityCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyAuthorityCursorListRequest.java`
        """
        request = KwaimoneyAuthorityCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, KwaimoneyAuthorityCursorListResponse)

    def get_kwaimoney_item_batch_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyItemBatchCursorListResponse:
        """获取 快手小店 商品批量游标列表（同步）

        OpenAPI: `open.distribution.kwaimoney.item.batch.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyItemBatchCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyItemBatchCursorListRequest.java`
        """
        request = KwaimoneyItemBatchCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, KwaimoneyItemBatchCursorListResponse)

    def get_kwaimoney_requirement_batch_cursor_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> KwaimoneyRequirementBatchCursorListResponse:
        """获取 快手小店 需求批量游标列表（同步）

        OpenAPI: `open.distribution.kwaimoney.requirement.batch.cursor.list` (GET)
        Java: OpenDistributionKwaimoneyRequirementBatchCursorListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyRequirementBatchCursorListRequest.java`
        """
        request = KwaimoneyRequirementBatchCursorListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, KwaimoneyRequirementBatchCursorListResponse
        )

    def get_cps_distributor_order_comment_list(
        self,
        access_token: str,
        oids: List[int],
        seller_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> CpsDistributorOrderCommentListResponse:
        """获取 CPS 分销商订单评论列表（同步）

        OpenAPI: `open.distribution.cps.distributor.order.comment.list` (GET)
        Java: OpenDistributionCpsDistributorOrderCommentListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionCpsDistributorOrderCommentListRequest.java`
        """
        request = CpsDistributorOrderCommentListRequest(
            access_token=access_token,
            uid=uid,
            oid=oids,
            seller_id=seller_id,
            api_version="1",
        )
        return self._client.execute(request, CpsDistributorOrderCommentListResponse)

    def get_seller_order_cps_detail(
        self,
        access_token: str,
        order_id: str,
        uid: Optional[int] = None,
    ) -> SellerOrderCpsDetailResponse:
        """获取卖家 CPS 订单详情（同步）

        OpenAPI: `open.seller.order.cps.detail` (GET)
        Java: OpenSellerOrderCpsDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenSellerOrderCpsDetailRequest.java`
        """
        request = SellerOrderCpsDetailRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderCpsDetailResponse)

    def get_kwaimoney_live_item_list(
        self,
        access_token: str,
        live_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> KwaimoneyLiveItemListResponse:
        """获取快手币直播商品列表（同步）

        OpenAPI: `open.distribution.kwaimoney.live.item.list` (GET)
        Java: OpenDistributionKwaimoneyLiveItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionKwaimoneyLiveItemListRequest.java`
        """
        request = KwaimoneyLiveItemListRequest(
            access_token=access_token,
            uid=uid,
            live_id=live_id,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, KwaimoneyLiveItemListResponse)
