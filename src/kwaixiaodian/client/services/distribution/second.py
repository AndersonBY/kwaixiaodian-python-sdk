"""二级分销服务

提供二级分销活动申请、合作管理、投资活动等功能。
"""

from typing import Optional

from ....models.distribution import (
    SecondActionApplyAgainInvestmentActicityRequest,
    SecondActionApplyAgainInvestmentActicityResponse,
    SecondActionApplyAgainInvestmentActivityRequest,
    SecondActionApplyAgainInvestmentActivityResponse,
    SecondActionApplyInvestmentActivityRequest,
    SecondActionApplyInvestmentActivityResponse,
    SecondActionApplyInvestmentActivityStandardRequest,
    SecondActionApplyInvestmentActivityStandardResponse,
    SecondActionCancelCooperationRequest,
    SecondActionCancelCooperationResponse,
    SecondActionEditApplyInvestmentActivityRequest,
    SecondActionEditApplyInvestmentActivityResponse,
    SecondActionEditApplyInvestmentActivityStandardRequest,
    SecondActionEditApplyInvestmentActivityStandardResponse,
    SecondActionHandleCooperationRequest,
    SecondActionHandleCooperationResponse,
    SecondAllowInvestmentActivityItemListAltRequest,
    SecondAllowInvestmentActivityItemListAltResponse,
    SecondAllowInvestmentActivityItemListRequest,
    SecondAllowInvestmentActivityItemListResponse,
    SecondApplyInvestmentActivityItemListAltRequest,
    SecondApplyInvestmentActivityItemListAltResponse,
    SecondApplyInvestmentActivityItemListStandardRequest,
    SecondApplyInvestmentActivityItemListStandardResponse,
    SecondApplyInvestmentActivityListAltRequest,
    SecondApplyInvestmentActivityListAltResponse,
    SecondApplyInvestmentActivityListRequest,
    SecondApplyInvestmentActivityListResponse,
    SecondInvestmentActivityListAltRequest,
    SecondInvestmentActivityListAltResponse,
    SecondInvestmentActivityListStandardRequest,
    SecondInvestmentActivityListStandardResponse,
)
from ...base import AsyncBaseClient, SyncBaseClient


class AsyncSecondDistributionService:
    """异步二级分销服务

    提供二级分销活动申请、合作管理、投资活动等功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化二级分销服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def get_second_allow_investment_activity_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondAllowInvestmentActivityItemListResponse:
        """获取二级允许投资活动商品列表

        OpenAPI: `open.distribution.second.allow.investment.activity.item.list` (GET)
        Java: OpenDistributionSecondAllowInvestmentActivityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondAllowInvestmentActivityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondAllowInvestmentActivityItemListResponse: 可允许的投资活动商品列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondAllowInvestmentActivityItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondAllowInvestmentActivityItemListResponse
        )

    async def get_second_apply_investment_activity_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityListResponse:
        """获取二级申请投资活动列表

        OpenAPI: `open.distribution.second.apply.investment.activity.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActicityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActicityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityListResponse: 已申请的投资活动列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondApplyInvestmentActivityListResponse
        )

    async def cancel_second_cooperation(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionCancelCooperationResponse:
        """取消二级合作

        OpenAPI: `open.distribution.second.action.cancel.cooperation` (GET)
        Java: OpenDistributionSecondActionCancelCooperationRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionCancelCooperationRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionCancelCooperationResponse: 取消合作的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionCancelCooperationRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionCancelCooperationResponse
        )

    async def apply_again_second_investment_activity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyAgainInvestmentActivityResponse:
        """重新申请二级投资活动

        OpenAPI: `open.distribution.second.action.apply.again.investment.activity` (GET)
        Java: OpenDistributionSecondActionApplyAgainInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyAgainInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyAgainInvestmentActivityResponse: 重新申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyAgainInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionApplyAgainInvestmentActivityResponse
        )

    async def handle_second_cooperation(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionHandleCooperationResponse:
        """处理二级合作

        OpenAPI: `open.distribution.second.action.handle.cooperation` (GET)
        Java: OpenDistributionSecondActionHandleCooperationRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionHandleCooperationRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionHandleCooperationResponse: 处理结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionHandleCooperationRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionHandleCooperationResponse
        )

    async def apply_again_second_investment_activity_new(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyAgainInvestmentActivityResponse:
        """二级分销重新申请投资活动（新方法）

        OpenAPI: `open.distribution.second.action.apply.again.investment.activity` (GET)
        Java: OpenDistributionSecondActionApplyAgainInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyAgainInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyAgainInvestmentActivityResponse: 重新申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyAgainInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionApplyAgainInvestmentActivityResponse
        )

    async def apply_again_second_investment_acticity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyAgainInvestmentActicityResponse:
        """二级分销重新申请投资活动（Acticity 变体，对齐 Java）

        OpenAPI: `open.distribution.second.action.apply.again.investment.acticity` (GET)
        Java: OpenDistributionSecondActionApplyAgainInvestmentActicityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyAgainInvestmentActicityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyAgainInvestmentActicityResponse: 重新申请处理结果（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyAgainInvestmentActicityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionApplyAgainInvestmentActicityResponse
        )

    async def apply_second_investment_activity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyInvestmentActivityResponse:
        """二级分销申请投资活动

        OpenAPI: `open.distribution.second.action.apply.investment.acticity` (GET)
        Java: OpenDistributionSecondActionApplyInvestmentActicityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyInvestmentActicityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyInvestmentActivityResponse: 申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionApplyInvestmentActivityResponse
        )

    async def apply_second_investment_activity_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyInvestmentActivityStandardResponse:
        """二级分销申请投资活动（标准版）

        OpenAPI: `open.distribution.second.action.apply.investment.activity` (GET)
        Java: OpenDistributionSecondActionApplyInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyInvestmentActivityStandardResponse: 申请处理结果（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyInvestmentActivityStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionApplyInvestmentActivityStandardResponse
        )

    async def edit_apply_second_investment_activity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionEditApplyInvestmentActivityResponse:
        """二级分销编辑申请投资活动

        OpenAPI: `open.distribution.second.action.edit.apply.investment.acticity` (GET)
        Java: OpenDistributionSecondActionEditApplyInvestmentActicityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionEditApplyInvestmentActicityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionEditApplyInvestmentActivityResponse: 编辑申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionEditApplyInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionEditApplyInvestmentActivityResponse
        )

    async def edit_apply_second_investment_activity_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionEditApplyInvestmentActivityStandardResponse:
        """二级分销编辑申请投资活动（标准版）

        OpenAPI: `open.distribution.second.action.edit.apply.investment.activity` (GET)
        Java: OpenDistributionSecondActionEditApplyInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionEditApplyInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionEditApplyInvestmentActivityStandardResponse: 编辑申请处理结果（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionEditApplyInvestmentActivityStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondActionEditApplyInvestmentActivityStandardResponse
        )

    async def get_second_allow_investment_activity_item_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondAllowInvestmentActivityItemListAltResponse:
        """获取二级分销允许投资活动商品列表（变体）

        OpenAPI: `open.distribution.second.allow.investment.acticity.item.list` (GET)
        Java: OpenDistributionSecondAllowInvestmentActicityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondAllowInvestmentActicityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondAllowInvestmentActivityItemListAltResponse: 可允许商品列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondAllowInvestmentActivityItemListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondAllowInvestmentActivityItemListAltResponse
        )

    async def get_second_apply_investment_activity_item_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityItemListAltResponse:
        """获取二级分销申请投资活动商品列表（变体）

        OpenAPI: `open.distribution.second.apply.investment.acticity.item.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActicityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActicityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityItemListAltResponse: 已申请商品列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityItemListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondApplyInvestmentActivityItemListAltResponse
        )

    async def get_second_apply_investment_activity_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityListAltResponse:
        """获取二级分销申请投资活动列表（变体）

        OpenAPI: `open.distribution.second.apply.investment.acticity.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActicityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActicityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityListAltResponse: 已申请活动列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondApplyInvestmentActivityListAltResponse
        )

    async def get_second_apply_investment_activity_item_list_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityItemListStandardResponse:
        """获取二级分销申请投资活动商品列表（标准版）

        OpenAPI: `open.distribution.second.apply.investment.activity.item.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActivityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActivityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityItemListStandardResponse: 已申请商品列表（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityItemListStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondApplyInvestmentActivityItemListStandardResponse
        )

    async def get_second_investment_activity_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondInvestmentActivityListAltResponse:
        """获取二级分销投资活动列表（变体）

        OpenAPI: `open.distribution.second.investment.acticity.list` (GET)
        Java: OpenDistributionSecondInvestmentActicityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondInvestmentActicityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondInvestmentActivityListAltResponse: 投资活动列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondInvestmentActivityListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondInvestmentActivityListAltResponse
        )

    async def get_second_investment_activity_list_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondInvestmentActivityListStandardResponse:
        """获取二级分销投资活动列表（标准版）

        OpenAPI: `open.distribution.second.investment.activity.list` (GET)
        Java: OpenDistributionSecondInvestmentActivityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondInvestmentActivityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondInvestmentActivityListStandardResponse: 投资活动列表（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondInvestmentActivityListStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, SecondInvestmentActivityListStandardResponse
        )


class SyncSecondDistributionService:
    """同步二级分销服务

    提供二级分销活动申请、合作管理、投资活动等功能。

    参考
    - 开发文档（限流）: `docs/开发指南和规则协议/开发文档/API限流说明.md`
    - 开发文档（授权）: `docs/开发指南和规则协议/开发文档/APP授权说明.md`
    - 规则协议（日志接入规范）: `docs/开发指南和规则协议/规则协议/开放平台/开放平台日志接入规范.md`
    - 错误处理: `docs/error-handling.md`
    """

    def __init__(self, client: SyncBaseClient):
        """初始化二级分销服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def get_second_allow_investment_activity_item_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondAllowInvestmentActivityItemListResponse:
        """获取二级允许投资活动商品列表

        OpenAPI: `open.distribution.second.allow.investment.activity.item.list` (GET)
        Java: OpenDistributionSecondAllowInvestmentActivityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondAllowInvestmentActivityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondAllowInvestmentActivityItemListResponse: 可允许的投资活动商品列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondAllowInvestmentActivityItemListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondAllowInvestmentActivityItemListResponse
        )

    def get_second_apply_investment_activity_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityListResponse:
        """获取二级申请投资活动列表

        OpenAPI: `open.distribution.second.apply.investment.activity.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActicityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActicityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityListResponse: 已申请的投资活动列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SecondApplyInvestmentActivityListResponse)

    def cancel_second_cooperation(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionCancelCooperationResponse:
        """取消二级合作

        OpenAPI: `open.distribution.second.action.cancel.cooperation` (GET)
        Java: OpenDistributionSecondActionCancelCooperationRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionCancelCooperationRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionCancelCooperationResponse: 取消合作的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionCancelCooperationRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SecondActionCancelCooperationResponse)

    def apply_again_second_investment_activity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyAgainInvestmentActivityResponse:
        """重新申请二级投资活动

        OpenAPI: `open.distribution.second.action.apply.again.investment.activity` (GET)
        Java: OpenDistributionSecondActionApplyAgainInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyAgainInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyAgainInvestmentActivityResponse: 重新申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyAgainInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionApplyAgainInvestmentActivityResponse
        )

    def handle_second_cooperation(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionHandleCooperationResponse:
        """处理二级合作

        OpenAPI: `open.distribution.second.action.handle.cooperation` (GET)
        Java: OpenDistributionSecondActionHandleCooperationRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionHandleCooperationRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionHandleCooperationResponse: 处理结果信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionHandleCooperationRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SecondActionHandleCooperationResponse)

    def apply_again_second_investment_activity_new(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyAgainInvestmentActivityResponse:
        """二级分销重新申请投资活动（新方法）

        OpenAPI: `open.distribution.second.action.apply.again.investment.activity` (GET)
        Java: OpenDistributionSecondActionApplyAgainInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyAgainInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyAgainInvestmentActivityResponse: 重新申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyAgainInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionApplyAgainInvestmentActivityResponse
        )

    def apply_again_second_investment_acticity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyAgainInvestmentActicityResponse:
        """二级分销重新申请投资活动（Acticity 变体，对齐 Java）

        OpenAPI: `open.distribution.second.action.apply.again.investment.acticity` (GET)
        Java: OpenDistributionSecondActionApplyAgainInvestmentActicityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyAgainInvestmentActicityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyAgainInvestmentActicityResponse: 重新申请处理结果（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyAgainInvestmentActicityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionApplyAgainInvestmentActicityResponse
        )

    def apply_second_investment_activity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyInvestmentActivityResponse:
        """二级分销申请投资活动

        OpenAPI: `open.distribution.second.action.apply.investment.acticity` (GET)
        Java: OpenDistributionSecondActionApplyInvestmentActicityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyInvestmentActicityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyInvestmentActivityResponse: 申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionApplyInvestmentActivityResponse
        )

    def apply_second_investment_activity_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionApplyInvestmentActivityStandardResponse:
        """二级分销申请投资活动（标准版）

        OpenAPI: `open.distribution.second.action.apply.investment.activity` (GET)
        Java: OpenDistributionSecondActionApplyInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionApplyInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionApplyInvestmentActivityStandardResponse: 申请处理结果（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionApplyInvestmentActivityStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionApplyInvestmentActivityStandardResponse
        )

    def edit_apply_second_investment_activity(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionEditApplyInvestmentActivityResponse:
        """二级分销编辑申请投资活动

        OpenAPI: `open.distribution.second.action.edit.apply.investment.acticity` (GET)
        Java: OpenDistributionSecondActionEditApplyInvestmentActicityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionEditApplyInvestmentActicityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionEditApplyInvestmentActivityResponse: 编辑申请处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionEditApplyInvestmentActivityRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionEditApplyInvestmentActivityResponse
        )

    def edit_apply_second_investment_activity_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondActionEditApplyInvestmentActivityStandardResponse:
        """二级分销编辑申请投资活动（标准版）

        OpenAPI: `open.distribution.second.action.edit.apply.investment.activity` (GET)
        Java: OpenDistributionSecondActionEditApplyInvestmentActivityRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondActionEditApplyInvestmentActivityRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondActionEditApplyInvestmentActivityStandardResponse: 编辑申请处理结果（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondActionEditApplyInvestmentActivityStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondActionEditApplyInvestmentActivityStandardResponse
        )

    def get_second_allow_investment_activity_item_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondAllowInvestmentActivityItemListAltResponse:
        """获取二级分销允许投资活动商品列表（变体）

        OpenAPI: `open.distribution.second.allow.investment.acticity.item.list` (GET)
        Java: OpenDistributionSecondAllowInvestmentActicityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondAllowInvestmentActicityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondAllowInvestmentActivityItemListAltResponse: 可允许的投资活动商品列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondAllowInvestmentActivityItemListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondAllowInvestmentActivityItemListAltResponse
        )

    def get_second_apply_investment_activity_item_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityItemListAltResponse:
        """获取二级分销申请投资活动商品列表（变体）

        OpenAPI: `open.distribution.second.apply.investment.acticity.item.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActicityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActicityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityItemListAltResponse: 已申请商品列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityItemListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondApplyInvestmentActivityItemListAltResponse
        )

    def get_second_apply_investment_activity_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityListAltResponse:
        """获取二级分销申请投资活动列表（变体）

        OpenAPI: `open.distribution.second.apply.investment.acticity.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActicityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActicityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityListAltResponse: 已申请活动列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondApplyInvestmentActivityListAltResponse
        )

    def get_second_apply_investment_activity_item_list_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondApplyInvestmentActivityItemListStandardResponse:
        """获取二级分销申请投资活动商品列表（标准版）

        OpenAPI: `open.distribution.second.apply.investment.activity.item.list` (GET)
        Java: OpenDistributionSecondApplyInvestmentActivityItemListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondApplyInvestmentActivityItemListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondApplyInvestmentActivityItemListStandardResponse: 已申请商品列表（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondApplyInvestmentActivityItemListStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondApplyInvestmentActivityItemListStandardResponse
        )

    def get_second_investment_activity_list_alt(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondInvestmentActivityListAltResponse:
        """获取二级分销投资活动列表（变体）

        OpenAPI: `open.distribution.second.investment.acticity.list` (GET)
        Java: OpenDistributionSecondInvestmentActicityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondInvestmentActicityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondInvestmentActivityListAltResponse: 投资活动列表（变体）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondInvestmentActivityListAltRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SecondInvestmentActivityListAltResponse)

    def get_second_investment_activity_list_standard(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> SecondInvestmentActivityListStandardResponse:
        """获取二级分销投资活动列表（标准版）

        OpenAPI: `open.distribution.second.investment.activity.list` (GET)
        Java: OpenDistributionSecondInvestmentActivityListRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/distribution/OpenDistributionSecondInvestmentActivityListRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            SecondInvestmentActivityListStandardResponse: 投资活动列表（标准版）。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = SecondInvestmentActivityListStandardRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(
            request, SecondInvestmentActivityListStandardResponse
        )
