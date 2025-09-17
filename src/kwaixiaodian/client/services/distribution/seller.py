"""卖家活动服务

提供卖家活动申请、推广效果查询、活动商品管理等功能。
"""

from typing import List, Optional

from ....models.distribution import (
    SellerActivityApplyCancelRequest,
    SellerActivityApplyCancelResponse,
    SellerActivityApplyListRequest,
    SellerActivityApplyListResponse,
    SellerActivityApplyRequest,
    SellerActivityApplyResponse,
    SellerActivityItemListRequest,
    SellerActivityItemListResponse,
    SellerActivityOpenInfoRequest,
    SellerActivityOpenInfoResponse,
    SellerActivityOpenListRequest,
    SellerActivityOpenListResponse,
    SellerActivityPromotionEffectItemRequest,
    SellerActivityPromotionEffectItemResponse,
    SellerActivityPromotionEffectSummaryRequest,
    SellerActivityPromotionEffectSummaryResponse,
    SellerActivityQueryActivityPromoterAdjustHistoryRequest,
    SellerActivityQueryActivityPromoterAdjustHistoryResponse,
    SellerActivityQueryExclusivePromoterInfoRequest,
    SellerActivityQueryExclusivePromoterInfoResponse,
    SellerActivityUsableItemRequest,
    SellerActivityUsableItemResponse,
)
from ...base import AsyncBaseClient, SyncBaseClient


class AsyncSellerActivityService:
    """异步卖家活动服务

    提供卖家活动申请、推广效果查询、活动商品管理等功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化卖家活动服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def get_seller_activity_apply_list(
        self,
        access_token: str,
        offset: Optional[int] = None,
        activity_type: Optional[int] = None,
        limit: Optional[int] = None,
        activity_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityApplyListResponse:
        """获取卖家活动申请列表

        OpenAPI: `open.distribution.seller.activity.apply.list` (GET)
        Java: OpenDistributionSellerActivityApplyListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityApplyListRequest.java`

        Args:
            access_token: 访问令牌。
            offset: 偏移量（可选）。
            activity_type: 活动类型（可选）。
            limit: 数量限制（可选）。
            activity_id: 活动 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityApplyListResponse: 申请列表及分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityApplyListRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            activity_type=activity_type,
            limit=limit,
            activity_id=activity_id,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityApplyListResponse)

    async def get_seller_activity_promotion_effect_item(
        self,
        access_token: str,
        page_cursor: Optional[int] = None,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        end_time: Optional[int] = None,
        item_title: Optional[str] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityPromotionEffectItemResponse:
        """获取卖家活动推广效果商品

        OpenAPI: `open.distribution.seller.activity.promotion.effect.item` (GET)
        Java: OpenDistributionSellerActivityPromotionEffectItemRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityPromotionEffectItemRequest.java`

        Args:
            access_token: 访问令牌。
            page_cursor: 页游标（可选）。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            end_time: 结束时间（毫秒，可选）。
            item_title: 商品标题（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityPromotionEffectItemResponse: 推广效果商品数据集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityPromotionEffectItemRequest(
            access_token=access_token,
            uid=uid,
            page_cursor=page_cursor,
            item_id=item_id,
            activity_id=activity_id,
            end_time=end_time,
            item_title=item_title,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(
            request, SellerActivityPromotionEffectItemResponse
        )

    async def get_seller_activity_usable_item(
        self,
        access_token: str,
        offset: Optional[int] = None,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        limit: Optional[int] = None,
        item_title: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityUsableItemResponse:
        """获取卖家活动可用商品

        OpenAPI: `open.distribution.seller.activity.usable.item` (GET)
        Java: OpenDistributionSellerActivityUsableItemRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityUsableItemRequest.java`

        Args:
            access_token: 访问令牌。
            offset: 偏移量（可选）。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            limit: 数量限制（可选）。
            item_title: 商品标题（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityUsableItemResponse: 可用商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityUsableItemRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            item_id=item_id,
            activity_id=activity_id,
            limit=limit,
            item_title=item_title,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityUsableItemResponse)

    async def cancel_seller_activity_apply(
        self,
        access_token: str,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityApplyCancelResponse:
        """取消卖家活动申请

        OpenAPI: `open.distribution.seller.activity.apply.cancel` (GET)
        Java: OpenDistributionSellerActivityApplyCancelRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityApplyCancelRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityApplyCancelResponse: 取消结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityApplyCancelRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            activity_id=activity_id,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityApplyCancelResponse)

    async def get_seller_activity_open_info(
        self,
        access_token: str,
        activity_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityOpenInfoResponse:
        """获取卖家活动开放信息

        OpenAPI: `open.distribution.seller.activity.open.info` (GET)
        Java: OpenDistributionSellerActivityOpenInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityOpenInfoRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityOpenInfoResponse: 活动开放信息详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityOpenInfoRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityOpenInfoResponse)

    async def get_seller_activity_item_list(
        self,
        access_token: str,
        item_audit_status: Optional[int] = None,
        category_id: Optional[int] = None,
        offset: Optional[int] = None,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        limit: Optional[int] = None,
        item_title: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityItemListResponse:
        """获取卖家活动商品列表

        OpenAPI: `open.distribution.seller.activity.item.list` (GET)
        Java: OpenDistributionSellerActivityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            item_audit_status: 商品审核状态（可选）。
            category_id: 类目 ID（可选）。
            offset: 偏移量（可选）。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            limit: 数量限制（可选）。
            item_title: 商品标题（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityItemListResponse: 商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityItemListRequest(
            access_token=access_token,
            uid=uid,
            item_audit_status=item_audit_status,
            category_id=category_id,
            offset=offset,
            item_id=item_id,
            activity_id=activity_id,
            limit=limit,
            item_title=item_title,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityItemListResponse)

    async def get_seller_activity_open_list(
        self,
        access_token: str,
        offset: Optional[int] = None,
        activity_type: Optional[int] = None,
        limit: Optional[int] = None,
        activity_id: Optional[int] = None,
        channel_id: Optional[List[int]] = None,
        activity_title: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityOpenListResponse:
        """获取卖家活动开放列表

        OpenAPI: `open.distribution.seller.activity.open.list` (GET)
        Java: OpenDistributionSellerActivityOpenListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityOpenListRequest.java`

        Args:
            access_token: 访问令牌。
            offset: 偏移量（可选）。
            activity_type: 活动类型（可选）。
            limit: 数量限制（可选）。
            activity_id: 活动 ID（可选）。
            channel_id: 渠道 ID 列表（可选）。
            activity_title: 活动标题（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityOpenListResponse: 活动开放列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityOpenListRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            activity_type=activity_type,
            limit=limit,
            activity_id=activity_id,
            channel_id=channel_id,
            activity_title=activity_title,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityOpenListResponse)

    async def query_seller_activity_exclusive_promoter_info(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SellerActivityQueryExclusivePromoterInfoResponse:
        """查询卖家活动独家推广者信息

        OpenAPI: `open.distribution.seller.activity.queryExclusivePromoterInfo` (GET)
        Java: OpenDistributionSellerActivityQueryexclusivepromoterinfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityQueryexclusivepromoterinfoRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityQueryExclusivePromoterInfoResponse: 独家推广者相关信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityQueryExclusivePromoterInfoRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SellerActivityQueryExclusivePromoterInfoResponse
        )

    async def apply_seller_activity(
        self,
        access_token: str,
        activity_id: int,
        apply_reason: str,
        uid: Optional[int] = None,
    ) -> SellerActivityApplyResponse:
        """申请卖家活动

        OpenAPI: `open.distribution.seller.activity.apply` (POST)
        Java: OpenDistributionSellerActivityApplyRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityApplyRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            apply_reason: 申请理由。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityApplyResponse: 申请结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityApplyRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            apply_reason=apply_reason,
            api_version="1",
        )
        return await self._client.execute(request, SellerActivityApplyResponse)

    async def get_seller_activity_promotion_effect_summary(
        self,
        access_token: str,
        activity_id: int,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityPromotionEffectSummaryResponse:
        """获取卖家活动推广效果汇总

        OpenAPI: `open.distribution.seller.activity.promotion.effect.summary` (GET)
        Java: OpenDistributionSellerActivityPromotionEffectSummaryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityPromotionEffectSummaryRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            end_time: 结束时间（毫秒，选填）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityPromotionEffectSummaryResponse: 推广效果汇总数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityPromotionEffectSummaryRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            end_time=end_time,
            api_version="1",
        )
        return await self._client.execute(
            request, SellerActivityPromotionEffectSummaryResponse
        )

    async def query_seller_activity_promoter_adjust_history(
        self,
        access_token: str,
        activity_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityQueryActivityPromoterAdjustHistoryResponse:
        """查询卖家活动推广者调整历史

        OpenAPI: `open.distribution.seller.activity.queryActivityPromoterAdjustHistory` (GET)
        Java: OpenDistributionSellerActivityQueryactivitypromoteradjusthistoryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityQueryactivitypromoteradjusthistoryRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            offset: 偏移量（可选）。
            limit: 数量限制（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityQueryActivityPromoterAdjustHistoryResponse: 调整历史记录与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityQueryActivityPromoterAdjustHistoryRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            activity_id=activity_id,
            limit=limit,
            api_version="1",
        )
        return await self._client.execute(
            request, SellerActivityQueryActivityPromoterAdjustHistoryResponse
        )


class SyncSellerActivityService:
    """同步卖家活动服务

    提供卖家活动申请、推广效果查询、活动商品管理等功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: SyncBaseClient):
        """初始化卖家活动服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def get_seller_activity_apply_list(
        self,
        access_token: str,
        offset: Optional[int] = None,
        activity_type: Optional[int] = None,
        limit: Optional[int] = None,
        activity_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityApplyListResponse:
        """获取卖家活动申请列表（同步）

        OpenAPI: `open.distribution.seller.activity.apply.list` (GET)
        Java: OpenDistributionSellerActivityApplyListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityApplyListRequest.java`

        Args:
            access_token: 访问令牌。
            offset: 偏移量（可选）。
            activity_type: 活动类型（可选）。
            limit: 数量限制（可选）。
            activity_id: 活动 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityApplyListResponse: 申请列表及分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityApplyListRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            activity_type=activity_type,
            limit=limit,
            activity_id=activity_id,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityApplyListResponse)

    def get_seller_activity_promotion_effect_item(
        self,
        access_token: str,
        page_cursor: Optional[int] = None,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        end_time: Optional[int] = None,
        item_title: Optional[str] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityPromotionEffectItemResponse:
        """获取卖家活动推广效果商品（同步）

        OpenAPI: `open.distribution.seller.activity.promotion.effect.item` (GET)
        Java: OpenDistributionSellerActivityPromotionEffectItemRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityPromotionEffectItemRequest.java`

        Args:
            access_token: 访问令牌。
            page_cursor: 页游标（可选）。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            end_time: 结束时间（毫秒，可选）。
            item_title: 商品标题（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityPromotionEffectItemResponse: 推广效果商品数据集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityPromotionEffectItemRequest(
            access_token=access_token,
            uid=uid,
            page_cursor=page_cursor,
            item_id=item_id,
            activity_id=activity_id,
            end_time=end_time,
            item_title=item_title,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityPromotionEffectItemResponse)

    def get_seller_activity_usable_item(
        self,
        access_token: str,
        offset: Optional[int] = None,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        limit: Optional[int] = None,
        item_title: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityUsableItemResponse:
        """获取卖家活动可用商品（同步）

        OpenAPI: `open.distribution.seller.activity.usable.item` (GET)
        Java: OpenDistributionSellerActivityUsableItemRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityUsableItemRequest.java`

        Args:
            access_token: 访问令牌。
            offset: 偏移量（可选）。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            limit: 数量限制（可选）。
            item_title: 商品标题（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityUsableItemResponse: 可用商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityUsableItemRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            item_id=item_id,
            activity_id=activity_id,
            limit=limit,
            item_title=item_title,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityUsableItemResponse)

    def cancel_seller_activity_apply(
        self,
        access_token: str,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityApplyCancelResponse:
        """取消卖家活动申请（同步）

        OpenAPI: `open.distribution.seller.activity.apply.cancel` (GET)
        Java: OpenDistributionSellerActivityApplyCancelRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityApplyCancelRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityApplyCancelResponse: 取消结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityApplyCancelRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            activity_id=activity_id,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityApplyCancelResponse)

    def get_seller_activity_open_info(
        self,
        access_token: str,
        activity_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityOpenInfoResponse:
        """获取卖家活动开放信息（同步）

        OpenAPI: `open.distribution.seller.activity.open.info` (GET)
        Java: OpenDistributionSellerActivityOpenInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityOpenInfoRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityOpenInfoResponse: 活动开放信息详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityOpenInfoRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityOpenInfoResponse)

    def get_seller_activity_item_list(
        self,
        access_token: str,
        item_audit_status: Optional[int] = None,
        category_id: Optional[int] = None,
        offset: Optional[int] = None,
        item_id: Optional[int] = None,
        activity_id: Optional[int] = None,
        limit: Optional[int] = None,
        item_title: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityItemListResponse:
        """获取卖家活动商品列表（同步）

        OpenAPI: `open.distribution.seller.activity.item.list` (GET)
        Java: OpenDistributionSellerActivityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            item_audit_status: 商品审核状态（可选）。
            category_id: 类目 ID（可选）。
            offset: 偏移量（可选）。
            item_id: 商品 ID（可选）。
            activity_id: 活动 ID（可选）。
            limit: 数量限制（可选）。
            item_title: 商品标题（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityItemListResponse: 商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityItemListRequest(
            access_token=access_token,
            uid=uid,
            item_audit_status=item_audit_status,
            category_id=category_id,
            offset=offset,
            item_id=item_id,
            activity_id=activity_id,
            limit=limit,
            item_title=item_title,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityItemListResponse)

    def get_seller_activity_open_list(
        self,
        access_token: str,
        offset: Optional[int] = None,
        activity_type: Optional[int] = None,
        limit: Optional[int] = None,
        activity_id: Optional[int] = None,
        channel_id: Optional[List[int]] = None,
        activity_title: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityOpenListResponse:
        """获取卖家活动开放列表（同步）

        OpenAPI: `open.distribution.seller.activity.open.list` (GET)
        Java: OpenDistributionSellerActivityOpenListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityOpenListRequest.java`

        Args:
            access_token: 访问令牌。
            offset: 偏移量（可选）。
            activity_type: 活动类型（可选）。
            limit: 数量限制（可选）。
            activity_id: 活动 ID（可选）。
            channel_id: 渠道 ID 列表（可选）。
            activity_title: 活动标题（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityOpenListResponse: 活动开放列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityOpenListRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            activity_type=activity_type,
            limit=limit,
            activity_id=activity_id,
            channel_id=channel_id,
            activity_title=activity_title,
            api_version="1",
        )
        return self._client.execute(request, SellerActivityOpenListResponse)

    def get_seller_activity_promotion_effect_summary(
        self,
        access_token: str,
        activity_id: int,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityPromotionEffectSummaryResponse:
        """获取卖家活动推广效果汇总（同步）

        OpenAPI: `open.distribution.seller.activity.promotion.effect.summary` (GET)
        Java: OpenDistributionSellerActivityPromotionEffectSummaryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityPromotionEffectSummaryRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            end_time: 结束时间（毫秒，选填）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityPromotionEffectSummaryResponse: 推广效果汇总数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityPromotionEffectSummaryRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            end_time=end_time,
            api_version="1",
        )
        return self._client.execute(
            request, SellerActivityPromotionEffectSummaryResponse
        )

    def query_seller_activity_promoter_adjust_history(
        self,
        access_token: str,
        activity_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerActivityQueryActivityPromoterAdjustHistoryResponse:
        """查询卖家活动推广者调整历史（同步）

        OpenAPI: `open.distribution.seller.activity.queryActivityPromoterAdjustHistory` (GET)
        Java: OpenDistributionSellerActivityQueryactivitypromoteradjusthistoryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityQueryactivitypromoteradjusthistoryRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            offset: 偏移量（可选）。
            limit: 数量限制（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityQueryActivityPromoterAdjustHistoryResponse: 推广者调整历史记录与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityQueryActivityPromoterAdjustHistoryRequest(
            access_token=access_token,
            uid=uid,
            offset=offset,
            activity_id=activity_id,
            limit=limit,
            api_version="1",
        )
        return self._client.execute(
            request, SellerActivityQueryActivityPromoterAdjustHistoryResponse
        )

    def query_seller_activity_exclusive_promoter_info(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SellerActivityQueryExclusivePromoterInfoResponse:
        """查询卖家活动独家推广者信息（同步）

        OpenAPI: `open.distribution.seller.activity.queryExclusivePromoterInfo` (GET)
        Java: OpenDistributionSellerActivityQueryexclusivepromoterinfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSellerActivityQueryexclusivepromoterinfoRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SellerActivityQueryExclusivePromoterInfoResponse: 独家推广者配置与状态信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SellerActivityQueryExclusivePromoterInfoRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SellerActivityQueryExclusivePromoterInfoResponse
        )
