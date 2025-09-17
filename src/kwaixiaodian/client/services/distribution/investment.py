"""投资活动服务

提供投资活动管理、商品管理、推广者调整等功能。
"""

from typing import List, Optional

from ....models.distribution import (
    InvestmentActivityAdjustPromoterRequest,
    InvestmentActivityAdjustPromoterResponse,
    InvestmentActivityInvalidItemListRequest,
    InvestmentActivityInvalidItemListResponse,
    InvestmentActivityItemDetailRequest,
    InvestmentActivityItemDetailResponse,
    InvestmentActivityItemTokenCreateRequest,
    InvestmentActivityItemTokenCreateResponse,
    InvestmentActivityOpenCloseRequest,
    InvestmentActivityOpenCloseResponse,
    InvestmentActivityOpenCreateRequest,
    InvestmentActivityOpenCreateResponse,
    InvestmentActivityOpenDeleteRequest,
    InvestmentActivityOpenDeleteResponse,
    InvestmentActivityOpenInfoRequest,
    InvestmentActivityOpenInfoResponse,
    InvestmentActivityOpenItemAuditRequest,
    InvestmentActivityOpenItemAuditResponse,
    InvestmentActivityOpenItemListRequest,
    InvestmentActivityOpenItemListResponse,
    InvestmentActivityOpenListRequest,
    InvestmentActivityOpenListResponse,
    InvestmentActivityOpenPromotionEffectRequest,
    InvestmentActivityOpenPromotionEffectResponse,
    InvestmentActivityQueryExclusivePromoterInfoRequest,
    InvestmentActivityQueryExclusivePromoterInfoResponse,
    InvestmentMyCreateActivityListRequest,
    InvestmentMyCreateActivityListResponse,
    InvestmentSamplePromoterDataRequest,
    InvestmentSamplePromoterDataResponse,
)
from ...base import AsyncBaseClient, SyncBaseClient


class AsyncInvestmentService:
    """异步投资活动服务

    提供投资活动管理、商品管理、推广者调整等功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化投资活动服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def adjust_investment_activity_promoter(
        self,
        access_token: str,
        promoter_id: List[int],
        activity_id: int,
        operator_type: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityAdjustPromoterResponse:
        """调整投资活动推广者

        OpenAPI: `open.distribution.investment.activity.adjustActivityPromoter` (POST)
        Java: OpenDistributionInvestmentActivityAdjustactivitypromoterRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityAdjustactivitypromoterRequest.java`

        Args:
            access_token: 访问令牌。
            promoter_id: 推广者 ID 列表。
            activity_id: 活动 ID。
            operator_type: 操作类型。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityAdjustPromoterResponse: 调整结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityAdjustPromoterRequest(
            access_token=access_token,
            uid=uid,
            promoter_id=promoter_id,
            activity_id=activity_id,
            operator_type=operator_type,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityAdjustPromoterResponse
        )

    async def get_investment_sample_promoter_data(
        self,
        access_token: str,
        promoter_id: int,
        item_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentSamplePromoterDataResponse:
        """获取投资样本推广者数据

        OpenAPI: `open.distribution.investment.sample.promoter.data` (GET)
        Java: OpenDistributionInvestmentSamplePromoterDataRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentSamplePromoterDataRequest.java`

        Args:
            access_token: 访问令牌。
            promoter_id: 推广者 ID。
            item_id: 商品 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentSamplePromoterDataResponse: 推广者在样本下的表现数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentSamplePromoterDataRequest(
            access_token=access_token,
            uid=uid,
            promoter_id=promoter_id,
            item_id=item_id,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentSamplePromoterDataResponse)

    async def create_investment_activity_item_token(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> InvestmentActivityItemTokenCreateResponse:
        """创建投资活动商品令牌

        OpenAPI: `open.distribution.investment.activity.item.token.create` (GET)
        Java: OpenDistributionInvestmentActivityItemTokenCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityItemTokenCreateRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityItemTokenCreateResponse: 令牌创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityItemTokenCreateRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityItemTokenCreateResponse
        )

    async def audit_investment_activity_open_item(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenItemAuditResponse:
        """审核投资活动开放商品

        OpenAPI: `open.distribution.investment.activity.open.item.audit` (GET)
        Java: OpenDistributionInvestmentActivityOpenItemAuditRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenItemAuditRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenItemAuditResponse: 审核结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenItemAuditRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityOpenItemAuditResponse
        )

    async def delete_investment_activity_open(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenDeleteResponse:
        """删除投资活动开放

        OpenAPI: `open.distribution.investment.activity.open.delete` (GET)
        Java: OpenDistributionInvestmentActivityOpenDeleteRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenDeleteRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenDeleteRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentActivityOpenDeleteResponse)

    async def get_investment_activity_open_info(
        self,
        access_token: str,
        activity_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenInfoResponse:
        """获取投资活动开放信息

        OpenAPI: `open.distribution.investment.activity.open.info` (GET)
        Java: OpenDistributionInvestmentActivityOpenInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenInfoRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenInfoResponse: 活动开放信息详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenInfoRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentActivityOpenInfoResponse)

    async def create_investment_activity_open(
        self,
        access_token: str,
        activity_name: str,
        activity_desc: str,
        begin_time: int,
        end_time: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenCreateResponse:
        """创建投资活动开放

        OpenAPI: `open.distribution.investment.activity.open.create` (POST)
        Java: OpenDistributionInvestmentActivityOpenCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenCreateRequest.java`

        Args:
            access_token: 访问令牌。
            activity_name: 活动名称。
            activity_desc: 活动描述。
            begin_time: 开始时间（毫秒）。
            end_time: 结束时间（毫秒）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenCreateResponse: 创建结果与活动标识信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenCreateRequest(
            access_token=access_token,
            uid=uid,
            activity_name=activity_name,
            activity_desc=activity_desc,
            begin_time=begin_time,
            end_time=end_time,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentActivityOpenCreateResponse)

    async def get_investment_activity_open_list(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        activity_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenListResponse:
        """获取投资活动开放列表

        OpenAPI: `open.distribution.investment.activity.open.list` (GET)
        Java: OpenDistributionInvestmentActivityOpenListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenListRequest.java`

        Args:
            access_token: 访问令牌。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            activity_status: 活动状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenListResponse: 活动开放列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenListRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            activity_status=activity_status,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentActivityOpenListResponse)

    async def get_investment_activity_item_detail(
        self,
        access_token: str,
        activity_id: int,
        item_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityItemDetailResponse:
        """获取投资活动商品详情

        OpenAPI: `open.distribution.investment.activity.item.detail` (GET)
        Java: OpenDistributionInvestmentActivityItemDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityItemDetailRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            item_id: 商品 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityItemDetailResponse: 商品在活动中的详细信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityItemDetailRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            item_id=item_id,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentActivityItemDetailResponse)

    async def get_investment_activity_open_item_list(
        self,
        access_token: str,
        activity_id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenItemListResponse:
        """获取投资活动开放商品列表

        OpenAPI: `open.distribution.investment.activity.open.item.list` (GET)
        Java: OpenDistributionInvestmentActivityOpenItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenItemListRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenItemListResponse: 开放商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenItemListRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityOpenItemListResponse
        )

    async def close_investment_activity_open(
        self,
        access_token: str,
        activity_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenCloseResponse:
        """关闭投资活动开放

        OpenAPI: `open.distribution.investment.activity.open.close` (GET)
        Java: OpenDistributionInvestmentActivityOpenCloseRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenCloseRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenCloseResponse: 关闭结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenCloseRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return await self._client.execute(request, InvestmentActivityOpenCloseResponse)

    async def get_investment_activity_open_promotion_effect(
        self,
        access_token: str,
        activity_id: int,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenPromotionEffectResponse:
        """获取投资活动开放推广效果

        OpenAPI: `open.distribution.investment.activity.open.promotion.effect` (GET)
        Java: OpenDistributionInvestmentActivityOpenPromotionEffectRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenPromotionEffectRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            begin_time: 开始时间（毫秒，选填）。
            end_time: 结束时间（毫秒，选填）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenPromotionEffectResponse: 推广效果统计数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenPromotionEffectRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            begin_time=begin_time,
            end_time=end_time,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityOpenPromotionEffectResponse
        )

    async def get_investment_activity_invalid_item_list(
        self,
        access_token: str,
        activity_id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityInvalidItemListResponse:
        """获取投资活动无效商品列表

        OpenAPI: `open.distribution.investment.activity.invalid.item.list` (POST)
        Java: OpenDistributionInvestmentActivityInvalidItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityInvalidItemListRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityInvalidItemListResponse: 无效商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityInvalidItemListRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityInvalidItemListResponse
        )

    async def query_investment_activity_exclusive_promoter_info(
        self,
        access_token: str,
        activity_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityQueryExclusivePromoterInfoResponse:
        """查询投资活动独家推广者信息

        OpenAPI: `open.distribution.investment.activity.queryExclusivePromoterInfo` (GET)
        Java: OpenDistributionInvestmentActivityQueryexclusivepromoterinfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityQueryexclusivepromoterinfoRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityQueryExclusivePromoterInfoResponse: 独家推广者配置与状态信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityQueryExclusivePromoterInfoRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentActivityQueryExclusivePromoterInfoResponse
        )

    async def get_investment_my_create_activity_list(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        activity_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentMyCreateActivityListResponse:
        """获取投资我的创建活动列表

        OpenAPI: `open.distribution.investment.my.create.activity.list` (GET)
        Java: OpenDistributionInvestmentMyCreateActivityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentMyCreateActivityListRequest.java`

        Args:
            access_token: 访问令牌。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            activity_status: 活动状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentMyCreateActivityListResponse: 我创建的活动列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentMyCreateActivityListRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            activity_status=activity_status,
            api_version="1",
        )
        return await self._client.execute(
            request, InvestmentMyCreateActivityListResponse
        )


class SyncInvestmentService:
    """同步投资活动服务

    提供投资活动管理、商品管理、推广者调整等功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: SyncBaseClient):
        """初始化投资活动服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def adjust_investment_activity_promoter(
        self,
        access_token: str,
        promoter_id: List[int],
        activity_id: int,
        operator_type: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityAdjustPromoterResponse:
        """调整投资活动推广者（同步）

        OpenAPI: `open.distribution.investment.activity.adjustActivityPromoter` (POST)
        Java: OpenDistributionInvestmentActivityAdjustactivitypromoterRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityAdjustactivitypromoterRequest.java`

        Args:
            access_token: 访问令牌。
            promoter_id: 推广者 ID 列表。
            activity_id: 活动 ID。
            operator_type: 操作类型。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityAdjustPromoterResponse: 调整结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityAdjustPromoterRequest(
            access_token=access_token,
            uid=uid,
            promoter_id=promoter_id,
            activity_id=activity_id,
            operator_type=operator_type,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityAdjustPromoterResponse)

    def get_investment_sample_promoter_data(
        self,
        access_token: str,
        promoter_id: int,
        item_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentSamplePromoterDataResponse:
        """获取投资样本推广者数据（同步）

        OpenAPI: `open.distribution.investment.sample.promoter.data` (GET)
        Java: OpenDistributionInvestmentSamplePromoterDataRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentSamplePromoterDataRequest.java`

        Args:
            access_token: 访问令牌。
            promoter_id: 推广者 ID。
            item_id: 商品 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentSamplePromoterDataResponse: 推广者在样本下的表现数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentSamplePromoterDataRequest(
            access_token=access_token,
            uid=uid,
            promoter_id=promoter_id,
            item_id=item_id,
            api_version="1",
        )
        return self._client.execute(request, InvestmentSamplePromoterDataResponse)

    def create_investment_activity_item_token(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> InvestmentActivityItemTokenCreateResponse:
        """创建投资活动商品令牌（同步）

        OpenAPI: `open.distribution.investment.activity.item.token.create` (GET)
        Java: OpenDistributionInvestmentActivityItemTokenCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityItemTokenCreateRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityItemTokenCreateResponse: 令牌创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityItemTokenCreateRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityItemTokenCreateResponse)

    def audit_investment_activity_open_item(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenItemAuditResponse:
        """审核投资活动开放商品（同步）

        OpenAPI: `open.distribution.investment.activity.open.item.audit` (GET)
        Java: OpenDistributionInvestmentActivityOpenItemAuditRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenItemAuditRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenItemAuditResponse: 审核结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenItemAuditRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenItemAuditResponse)

    def delete_investment_activity_open(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenDeleteResponse:
        """删除投资活动开放（同步）

        OpenAPI: `open.distribution.investment.activity.open.delete` (GET)
        Java: OpenDistributionInvestmentActivityOpenDeleteRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenDeleteRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenDeleteRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenDeleteResponse)

    def create_investment_activity_open(
        self,
        access_token: str,
        activity_name: str,
        activity_desc: str,
        begin_time: int,
        end_time: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenCreateResponse:
        """创建投资活动开放（同步）

        OpenAPI: `open.distribution.investment.activity.open.create` (POST)
        Java: OpenDistributionInvestmentActivityOpenCreateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenCreateRequest.java`

        Args:
            access_token: 访问令牌。
            activity_name: 活动名称。
            activity_desc: 活动描述。
            begin_time: 开始时间（毫秒）。
            end_time: 结束时间（毫秒）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenCreateResponse: 创建结果与活动标识信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenCreateRequest(
            access_token=access_token,
            uid=uid,
            activity_name=activity_name,
            activity_desc=activity_desc,
            begin_time=begin_time,
            end_time=end_time,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenCreateResponse)

    def get_investment_activity_open_info(
        self,
        access_token: str,
        activity_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenInfoResponse:
        """获取投资活动开放信息（同步）

        OpenAPI: `open.distribution.investment.activity.open.info` (GET)
        Java: OpenDistributionInvestmentActivityOpenInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenInfoRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenInfoResponse: 活动开放信息详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenInfoRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenInfoResponse)

    def get_investment_activity_open_list(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        activity_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenListResponse:
        """获取投资活动开放列表（同步）

        OpenAPI: `open.distribution.investment.activity.open.list` (GET)
        Java: OpenDistributionInvestmentActivityOpenListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenListRequest.java`

        Args:
            access_token: 访问令牌。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            activity_status: 活动状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenListResponse: 活动开放列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenListRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            activity_status=activity_status,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenListResponse)

    def get_investment_activity_item_detail(
        self,
        access_token: str,
        activity_id: int,
        item_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityItemDetailResponse:
        """获取投资活动商品详情（同步）

        OpenAPI: `open.distribution.investment.activity.item.detail` (GET)
        Java: OpenDistributionInvestmentActivityItemDetailRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityItemDetailRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            item_id: 商品 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityItemDetailResponse: 商品详情数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityItemDetailRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            item_id=item_id,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityItemDetailResponse)

    def get_investment_activity_open_item_list(
        self,
        access_token: str,
        activity_id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenItemListResponse:
        """获取投资活动开放商品列表（同步）

        OpenAPI: `open.distribution.investment.activity.open.item.list` (GET)
        Java: OpenDistributionInvestmentActivityOpenItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenItemListRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenItemListResponse: 开放商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenItemListRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenItemListResponse)

    def close_investment_activity_open(
        self,
        access_token: str,
        activity_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenCloseResponse:
        """关闭投资活动开放（同步）

        OpenAPI: `open.distribution.investment.activity.open.close` (GET)
        Java: OpenDistributionInvestmentActivityOpenCloseRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenCloseRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenCloseResponse: 关闭结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenCloseRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityOpenCloseResponse)

    def get_investment_activity_open_promotion_effect(
        self,
        access_token: str,
        activity_id: int,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityOpenPromotionEffectResponse:
        """获取投资活动开放推广效果（同步）

        OpenAPI: `open.distribution.investment.activity.open.promotion.effect` (GET)
        Java: OpenDistributionInvestmentActivityOpenPromotionEffectRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityOpenPromotionEffectRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            begin_time: 开始时间（毫秒，选填）。
            end_time: 结束时间（毫秒，选填）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityOpenPromotionEffectResponse: 推广效果统计数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityOpenPromotionEffectRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            begin_time=begin_time,
            end_time=end_time,
            api_version="1",
        )
        return self._client.execute(
            request, InvestmentActivityOpenPromotionEffectResponse
        )

    def get_investment_activity_invalid_item_list(
        self,
        access_token: str,
        activity_id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentActivityInvalidItemListResponse:
        """获取投资活动无效商品列表（同步）

        OpenAPI: `open.distribution.investment.activity.invalid.item.list` (POST)
        Java: OpenDistributionInvestmentActivityInvalidItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityInvalidItemListRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityInvalidItemListResponse: 无效商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityInvalidItemListRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            page=page,
            page_size=page_size,
            api_version="1",
        )
        return self._client.execute(request, InvestmentActivityInvalidItemListResponse)

    def query_investment_activity_exclusive_promoter_info(
        self,
        access_token: str,
        activity_id: int,
        uid: Optional[int] = None,
    ) -> InvestmentActivityQueryExclusivePromoterInfoResponse:
        """查询投资活动独家推广者信息（同步）

        OpenAPI: `open.distribution.investment.activity.queryExclusivePromoterInfo` (GET)
        Java: OpenDistributionInvestmentActivityQueryexclusivepromoterinfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentActivityQueryexclusivepromoterinfoRequest.java`

        Args:
            access_token: 访问令牌。
            activity_id: 活动 ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentActivityQueryExclusivePromoterInfoResponse: 独家推广者配置与状态信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentActivityQueryExclusivePromoterInfoRequest(
            access_token=access_token,
            uid=uid,
            activity_id=activity_id,
            api_version="1",
        )
        return self._client.execute(
            request, InvestmentActivityQueryExclusivePromoterInfoResponse
        )

    def get_investment_my_create_activity_list(
        self,
        access_token: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        activity_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> InvestmentMyCreateActivityListResponse:
        """获取投资我的创建活动列表（同步）

        OpenAPI: `open.distribution.investment.my.create.activity.list` (GET)
        Java: OpenDistributionInvestmentMyCreateActivityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionInvestmentMyCreateActivityListRequest.java`

        Args:
            access_token: 访问令牌。
            page: 页码（可选）。
            page_size: 页大小（可选）。
            activity_status: 活动状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            InvestmentMyCreateActivityListResponse: 我创建的活动列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = InvestmentMyCreateActivityListRequest(
            access_token=access_token,
            uid=uid,
            page=page,
            page_size=page_size,
            activity_status=activity_status,
            api_version="1",
        )
        return self._client.execute(request, InvestmentMyCreateActivityListResponse)
