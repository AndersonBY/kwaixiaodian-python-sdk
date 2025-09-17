"""店铺管理服务（严格对齐 Java 参考）"""

from typing import Any, Dict, List, Optional

from ...models.shop import (
    # 品牌管理
    BrandBatchAddRequest,
    BrandBatchAddResponse,
    BrandPageGetRequest,
    BrandPageGetResponse,
    # 企业资质
    EnterpriseQualificationExistRequest,
    EnterpriseQualificationExistResponse,
    # 入驻结算
    InviteSettleOneStepRequest,
    InviteSettleOneStepResponse,
    MasterScoreGetRequest,
    MasterScoreGetResponse,
    # POI
    POIGetDetailByOuterPOIRequest,
    POIGetDetailByOuterPOIResponse,
    QueryCanOneStepSettleRequest,
    QueryCanOneStepSettleResponse,
    QueryCategoryListRequest,
    QueryCategoryListResponse,
    QueryIndustryCertificateByCategoryRequest,
    QueryIndustryCertificateByCategoryResponse,
    QuerySettleContractsRequest,
    QuerySettleContractsResponse,
    QuerySettleStatusRequest,
    QuerySettleStatusResponse,
    # 店铺信息/评分
    ShopInfoRequest,
    ShopInfoResponse,
    ShopScoreGetRequest,
    ShopScoreGetResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncShopService:
    """异步店铺管理服务（严格对齐 Java SDK 与文档）。

    提供以下能力：
    - open.shop.info.get 店铺信息
    - open.score.shop.get 店铺评分
    - open.score.master.get 主评分
    - open.shop.brand.batch.add 品牌批量新增
    - open.shop.brand.page.get 品牌分页查询
    - open.shop.enterprise.qualificaiton.exist 企业资质是否存在
    - open.shop.invite.settle.oneStepSettle 一步式结算入驻
    - open.shop.invite.settle.queryCanOneStepSettle 是否可一步式结算
    - open.shop.invite.settle.queryCategoryList 入驻类目列表
    - open.shop.invite.settle.queryIndustryCertificateByCategory 行业证书要求
    - open.shop.invite.settle.querySettleContracts 结算合同
    - open.shop.invite.settle.querySettleStatus 结算状态
    - open.shop.poi.getPoiDetailByOuterPoi 外部POI详情
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化店铺服务

        Args:
            client: 异步基础客户端实例
        """
        self._client = client

    async def info(
        self, access_token: str, uid: Optional[int] = None
    ) -> ShopInfoResponse:
        """获取店铺信息。

        OpenAPI: `open.shop.info.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInfoGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInfoGetRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            店铺信息响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = ShopInfoRequest(access_token=access_token, uid=uid)
        return await self._client.execute(request, ShopInfoResponse)

    # ==================== 店铺评分相关 ====================

    async def shop_score_get(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> ShopScoreGetResponse:
        """获取店铺评分。

        OpenAPI: `open.score.shop.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenScoreShopGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenScoreShopGetRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            店铺评分响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = ShopScoreGetRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ShopScoreGetResponse)

    async def master_score_get(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> MasterScoreGetResponse:
        """获取主评分信息。

        OpenAPI: `open.score.master.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenScoreMasterGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenScoreMasterGetRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            主评分信息响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = MasterScoreGetRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, MasterScoreGetResponse)

    # ==================== 品牌管理相关 ====================

    async def brand_batch_add(
        self,
        access_token: str,
        brand_list: List[Dict[str, Any]],
        uid: Optional[int] = None,
    ) -> BrandBatchAddResponse:
        """批量添加品牌。

        OpenAPI: `open.shop.brand.batch.add` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopBrandBatchAddRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopBrandBatchAddRequest.java`

        Args:
            access_token: 访问令牌
            brand_list: 品牌信息列表
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            批量添加品牌响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = BrandBatchAddRequest(
            access_token=access_token,
            brand_list=brand_list,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, BrandBatchAddResponse)

    async def brand_page_get(
        self,
        access_token: str,
        page_num: int = 1,
        page_size: int = 20,
        uid: Optional[int] = None,
    ) -> BrandPageGetResponse:
        """分页获取品牌列表。

        OpenAPI: `open.shop.brand.page.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopBrandPageGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopBrandPageGetRequest.java`

        Args:
            access_token: 访问令牌
            page_num: 页码
            page_size: 页面大小
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            品牌分页查询响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = BrandPageGetRequest(
            access_token=access_token,
            page_num=page_num,
            page_size=page_size,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, BrandPageGetResponse)

    # ==================== 企业资质管理相关 ====================

    async def enterprise_qualification_exist(
        self,
        access_token: str,
        meta_data_info: Dict[str, Any],
        uid: Optional[int] = None,
    ) -> EnterpriseQualificationExistResponse:
        """检查企业资质是否存在。

        OpenAPI: `open.shop.enterprise.qualificaiton.exist` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopEnterpriseQualificaitonExistRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopEnterpriseQualificaitonExistRequest.java`

        Args:
            access_token: 访问令牌
            meta_data_info: 元数据信息字典
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            企业资质存在性响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = EnterpriseQualificationExistRequest(
            access_token=access_token,
            meta_data_info=meta_data_info,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, EnterpriseQualificationExistResponse)

    # ==================== 入驻结算管理相关 ====================

    async def invite_settle_one_step(
        self,
        access_token: str,
        invite_type: Optional[int] = None,
        oversea_enterprise_info: Optional[Dict[str, Any]] = None,
        business_base_info: Optional[Dict[str, Any]] = None,
        brand_request: Optional[Dict[str, Any]] = None,
        industry_qualification_request: Optional[Dict[str, Any]] = None,
        mainland_enterprise_info: Optional[Dict[str, Any]] = None,
        shop_request: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> InviteSettleOneStepResponse:
        """一步式结算入驻。

        OpenAPI: `open.shop.invite.settle.oneStepSettle` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleOnestepsettleRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleOnestepsettleRequest.java`

        Args:
            access_token: 访问令牌
            invite_type: 邀请类型
            oversea_enterprise_info: 海外企业信息
            business_base_info: 业务基础信息
            brand_request: 品牌请求信息
            industry_qualification_request: 行业资质请求信息
            mainland_enterprise_info: 内地企业信息
            shop_request: 店铺请求信息
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            一步式结算入驻响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = InviteSettleOneStepRequest(
            access_token=access_token,
            invite_type=invite_type,
            oversea_enterprise_info=oversea_enterprise_info,
            business_base_info=business_base_info,
            brand_request=brand_request,
            industry_qualification_request=industry_qualification_request,
            mainland_enterprise_info=mainland_enterprise_info,
            shop_request=shop_request,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, InviteSettleOneStepResponse)

    async def query_can_one_step_settle(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> QueryCanOneStepSettleResponse:
        """查询是否可一步式结算。

        OpenAPI: `open.shop.invite.settle.queryCanOneStepSettle` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerycanonestepsettleRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerycanonestepsettleRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            是否可一步式结算响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QueryCanOneStepSettleRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, QueryCanOneStepSettleResponse)

    async def query_category_list(
        self,
        access_token: str,
        invite_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> QueryCategoryListResponse:
        """查询入驻类目列表。

        OpenAPI: `open.shop.invite.settle.queryCategoryList` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerycategorylistRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerycategorylistRequest.java`

        Args:
            access_token: 访问令牌
            invite_type: 邀请类型
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            入驻类目列表响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QueryCategoryListRequest(
            access_token=access_token,
            invite_type=invite_type,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, QueryCategoryListResponse)

    async def query_industry_certificate_by_category(
        self,
        access_token: str,
        category_ids: List[int],
        invite_type: Optional[int] = None,
        oversea: Optional[bool] = None,
        uid: Optional[int] = None,
    ) -> QueryIndustryCertificateByCategoryResponse:
        """根据类目查询行业证书要求。

        OpenAPI: `open.shop.invite.settle.queryIndustryCertificateByCategory` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQueryindustrycertificatebycategoryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQueryindustrycertificatebycategoryRequest.java`

        Args:
            access_token: 访问令牌
            category_ids: 类目ID列表
            invite_type: 邀请类型
            oversea: 是否海外
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            行业证书要求响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QueryIndustryCertificateByCategoryRequest(
            access_token=access_token,
            invite_type=invite_type,
            category_ids=category_ids,
            oversea=oversea,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(
            request, QueryIndustryCertificateByCategoryResponse
        )

    async def query_settle_contracts(
        self,
        access_token: str,
        invite_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> QuerySettleContractsResponse:
        """查询结算合同。

        OpenAPI: `open.shop.invite.settle.querySettleContracts` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerysettlecontractsRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerysettlecontractsRequest.java`

        Args:
            access_token: 访问令牌
            invite_type: 邀请类型
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            结算合同响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QuerySettleContractsRequest(
            access_token=access_token,
            invite_type=invite_type,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, QuerySettleContractsResponse)

    async def query_settle_status(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> QuerySettleStatusResponse:
        """查询结算状态。

        OpenAPI: `open.shop.invite.settle.querySettleStatus` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerysettlestatusRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerysettlestatusRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            结算状态响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QuerySettleStatusRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, QuerySettleStatusResponse)

    # ==================== POI管理相关 ====================

    async def poi_get_detail_by_outer_poi(
        self,
        access_token: str,
        outer_poi_id: str,
        source: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> POIGetDetailByOuterPOIResponse:
        """根据外部 POI ID 获取详情。

        OpenAPI: `open.shop.poi.getPoiDetailByOuterPoi` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopPoiGetpoidetailbyouterpoiRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopPoiGetpoidetailbyouterpoiRequest.java`

        Args:
            access_token: 访问令牌
            outer_poi_id: 外部POI ID
            source: 来源编号
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            POI 详情响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = POIGetDetailByOuterPOIRequest(
            access_token=access_token,
            outer_poi_id=outer_poi_id,
            source=source,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, POIGetDetailByOuterPOIResponse)


class SyncShopService:
    """同步店铺管理服务（严格对齐 Java SDK 与文档）。"""

    def __init__(self, client: SyncBaseClient):
        """初始化店铺服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def info(self, access_token: str, uid: Optional[int] = None) -> ShopInfoResponse:
        """获取店铺信息（同步）。

        OpenAPI: `open.shop.info.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInfoGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInfoGetRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            店铺信息响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = ShopInfoRequest(access_token=access_token, uid=uid)
        return self._client.execute(request, ShopInfoResponse)

    # ==================== 店铺评分相关 ====================

    def shop_score_get(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> ShopScoreGetResponse:
        """获取店铺评分（同步）。

        OpenAPI: `open.score.shop.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenScoreShopGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenScoreShopGetRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            店铺评分响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = ShopScoreGetRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ShopScoreGetResponse)

    def master_score_get(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> MasterScoreGetResponse:
        """获取主评分信息（同步）。

        OpenAPI: `open.score.master.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenScoreMasterGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenScoreMasterGetRequest.java`

        Args:
            access_token: 访问令牌
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            主评分信息响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = MasterScoreGetRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, MasterScoreGetResponse)

    # ==================== 品牌管理相关 ====================

    def brand_batch_add(
        self,
        access_token: str,
        brand_list: List[Dict[str, Any]],
        uid: Optional[int] = None,
    ) -> BrandBatchAddResponse:
        """批量添加品牌（同步）。

        OpenAPI: `open.shop.brand.batch.add` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopBrandBatchAddRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopBrandBatchAddRequest.java`

        Args:
            access_token: 访问令牌
            brand_list: 品牌信息列表
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            批量添加品牌响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = BrandBatchAddRequest(
            access_token=access_token,
            brand_list=brand_list,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, BrandBatchAddResponse)

    def brand_page_get(
        self,
        access_token: str,
        page_num: int = 1,
        page_size: int = 20,
        uid: Optional[int] = None,
    ) -> BrandPageGetResponse:
        """分页获取品牌列表（同步）。

        OpenAPI: `open.shop.brand.page.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopBrandPageGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopBrandPageGetRequest.java`

        Args:
            access_token: 访问令牌
            page_num: 页码
            page_size: 页面大小
            uid: 可选用户ID（最后一个可选参数）

        Returns:
            品牌分页查询响应对象

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = BrandPageGetRequest(
            access_token=access_token,
            page_num=page_num,
            page_size=page_size,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, BrandPageGetResponse)

    # ==================== 企业资质管理相关 ====================

    def enterprise_qualification_exist(
        self,
        access_token: str,
        meta_data_info: Dict[str, Any],
        uid: Optional[int] = None,
    ) -> EnterpriseQualificationExistResponse:
        """检查企业资质是否存在（同步）。

        Args:
            access_token: 访问令牌
            meta_data_info: 元数据信息字典
            uid: 可选用户ID

        Returns:
            企业资质存在性响应对象

        OpenAPI: `open.shop.enterprise.qualificaiton.exist` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopEnterpriseQualificaitonExistRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopEnterpriseQualificaitonExistRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = EnterpriseQualificationExistRequest(
            access_token=access_token,
            meta_data_info=meta_data_info,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, EnterpriseQualificationExistResponse)

    # ==================== 入驻结算管理相关 ====================

    def invite_settle_one_step(
        self,
        access_token: str,
        invite_type: Optional[int] = None,
        oversea_enterprise_info: Optional[Dict[str, Any]] = None,
        business_base_info: Optional[Dict[str, Any]] = None,
        brand_request: Optional[Dict[str, Any]] = None,
        industry_qualification_request: Optional[Dict[str, Any]] = None,
        mainland_enterprise_info: Optional[Dict[str, Any]] = None,
        shop_request: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> InviteSettleOneStepResponse:
        """一步式结算入驻（同步）。

        Args:
            access_token: 访问令牌
            invite_type: 邀请类型
            oversea_enterprise_info: 海外企业信息
            business_base_info: 业务基础信息
            brand_request: 品牌请求信息
            industry_qualification_request: 行业资质请求信息
            mainland_enterprise_info: 内地企业信息
            shop_request: 店铺请求信息
            uid: 可选用户ID

        Returns:
            一步式结算入驻响应对象

        OpenAPI: `open.shop.invite.settle.oneStepSettle` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleOnestepsettleRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleOnestepsettleRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = InviteSettleOneStepRequest(
            access_token=access_token,
            invite_type=invite_type,
            oversea_enterprise_info=oversea_enterprise_info,
            business_base_info=business_base_info,
            brand_request=brand_request,
            industry_qualification_request=industry_qualification_request,
            mainland_enterprise_info=mainland_enterprise_info,
            shop_request=shop_request,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, InviteSettleOneStepResponse)

    def query_can_one_step_settle(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> QueryCanOneStepSettleResponse:
        """查询是否可一步式结算（同步）。

        Args:
            access_token: 访问令牌
            uid: 可选用户ID

        Returns:
            是否可一步式结算响应对象

        OpenAPI: `open.shop.invite.settle.queryCanOneStepSettle` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerycanonestepsettleRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerycanonestepsettleRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QueryCanOneStepSettleRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, QueryCanOneStepSettleResponse)

    def query_category_list(
        self,
        access_token: str,
        invite_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> QueryCategoryListResponse:
        """查询入驻类目列表（同步）。

        Args:
            access_token: 访问令牌
            invite_type: 邀请类型
            uid: 可选用户ID

        Returns:
            入驻类目列表响应对象

        OpenAPI: `open.shop.invite.settle.queryCategoryList` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerycategorylistRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerycategorylistRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QueryCategoryListRequest(
            access_token=access_token,
            invite_type=invite_type,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, QueryCategoryListResponse)

    def query_industry_certificate_by_category(
        self,
        access_token: str,
        category_ids: List[int],
        invite_type: Optional[int] = None,
        oversea: Optional[bool] = None,
        uid: Optional[int] = None,
    ) -> QueryIndustryCertificateByCategoryResponse:
        """根据类目查询行业证书要求（同步）。

        Args:
            access_token: 访问令牌
            category_ids: 类目ID列表
            invite_type: 邀请类型
            oversea: 是否海外
            uid: 可选用户ID

        Returns:
            行业证书要求响应对象

        OpenAPI: `open.shop.invite.settle.queryIndustryCertificateByCategory` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQueryindustrycertificatebycategoryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQueryindustrycertificatebycategoryRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QueryIndustryCertificateByCategoryRequest(
            access_token=access_token,
            invite_type=invite_type,
            category_ids=category_ids,
            oversea=oversea,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, QueryIndustryCertificateByCategoryResponse)

    def query_settle_contracts(
        self,
        access_token: str,
        invite_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> QuerySettleContractsResponse:
        """查询结算合同（同步）。

        Args:
            access_token: 访问令牌
            uid: 可选用户ID

        Returns:
            结算合同响应对象

        OpenAPI: `open.shop.invite.settle.querySettleContracts` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerysettlecontractsRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerysettlecontractsRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QuerySettleContractsRequest(
            access_token=access_token,
            invite_type=invite_type,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, QuerySettleContractsResponse)

    def query_settle_status(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> QuerySettleStatusResponse:
        """查询结算状态（同步）。

        Args:
            access_token: 访问令牌
            uid: 可选用户ID

        Returns:
            结算状态响应对象

        OpenAPI: `open.shop.invite.settle.querySettleStatus` (POST)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopInviteSettleQuerysettlestatusRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopInviteSettleQuerysettlestatusRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = QuerySettleStatusRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, QuerySettleStatusResponse)

    # ==================== POI管理相关 ====================

    def poi_get_detail_by_outer_poi(
        self,
        access_token: str,
        outer_poi_id: str,
        source: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> POIGetDetailByOuterPOIResponse:
        """根据外部 POI ID 获取详情（同步）。

        Args:
            access_token: 访问令牌
            outer_poi_id: 外部POI ID
            uid: 可选用户ID

        Returns:
            POI 详情响应对象

        OpenAPI: `open.shop.poi.getPoiDetailByOuterPoi` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shop.OpenShopPoiGetpoidetailbyouterpoiRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shop/OpenShopPoiGetpoidetailbyouterpoiRequest.java`

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = POIGetDetailByOuterPOIRequest(
            access_token=access_token,
            outer_poi_id=outer_poi_id,
            source=source,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, POIGetDetailByOuterPOIResponse)
