"""商品服务类"""

from typing import Any, Dict, List, Optional

from ...models.item import (
    AddItemPropValue,
    # Additional nested imports needed
    AddSizeChartParam,
    # 更多缺失的API类
    ItemAutopassEditRequest,
    ItemAutopassEditResponse,
    # 缺失的API类
    ItemBrandListRequest,
    ItemBrandListResponse,
    ItemCategoryConfigRequest,
    ItemCategoryConfigResponse,
    ItemCategoryPropStandardRequest,
    ItemCategoryPropStandardResponse,
    ItemCategoryPropValueSearchRequest,
    ItemCategoryPropValueSearchResponse,
    ItemCategoryRequest,
    ItemCategoryResponse,
    ItemCategoryStandardCheckRequest,
    ItemCategoryStandardCheckResponse,
    ItemCategoryStandardSearchRequest,
    ItemCategoryStandardSearchResponse,
    # Basic item operations (new/edit only)
    # New missing API imports - Other functionality
    ItemDeletedGetRequest,
    ItemDeletedGetResponse,
    ItemDeleteRequest,
    ItemDeleteResponse,
    ItemDetailImagesUpdateRequest,
    ItemDetailImagesUpdateResponse,
    ItemDetailPageLinkRequest,
    ItemDetailPageLinkResponse,
    ItemDiagnosisGetRequest,
    ItemDiagnosisGetResponse,
    ItemEditRequest,
    ItemEditResponse,
    ItemGetRequest,
    ItemGetResponse,
    ItemImageUploadRequest,
    ItemImageUploadResponse,
    ItemListRequest,
    ItemListResponse,
    ItemMainPicVideoApplyRequest,
    ItemMainPicVideoApplyResponse,
    ItemMainPicVideoDeleteRequest,
    ItemMainPicVideoDeleteResponse,
    ItemMaterialDetailGetRequest,
    ItemMaterialDetailGetResponse,
    ItemMaterialUploadTokenIssueRequest,
    ItemMaterialUploadTokenIssueResponse,
    ItemMaterialUploadTokenVerifyRequest,
    ItemMaterialUploadTokenVerifyResponse,
    ItemNewPrecheckRequest,
    ItemNewPrecheckResponse,
    ItemNewRequest,
    ItemNewResponse,
    ItemOptionalCategoryRequest,
    ItemOptionalCategoryResponse,
    ItemPropValue,
    ItemQualificationConfigRequest,
    ItemQualificationConfigResponse,
    # Sale prop rules
    ItemSalePropRuleRequest,
    ItemSalePropRuleResponse,
    ItemShelfStatusUpdateRequest,
    ItemShelfStatusUpdateResponse,
    # New missing API imports - Size Chart Management
    ItemSizeChartGroupListGetRequest,
    ItemSizeChartGroupListGetResponse,
    ItemSizeChartTemplateAddRequest,
    ItemSizeChartTemplateAddResponse,
    ItemSizeChartTemplateDeleteRequest,
    ItemSizeChartTemplateDeleteResponse,
    ItemSizeChartTemplateEditRequest,
    ItemSizeChartTemplateEditResponse,
    ItemSizeChartTemplateGetRequest,
    ItemSizeChartTemplateGetResponse,
    ItemSizeChartTemplateListGetRequest,
    ItemSizeChartTemplateListGetResponse,
    ItemSizeChartTemplateMetaGetRequest,
    ItemSizeChartTemplateMetaGetResponse,
    ItemSkuGoodsRelationAddRequest,
    ItemSkuGoodsRelationDeleteRequest,
    ItemSkuGoodsRelationGetRequest,
    ItemSkuGoodsRelationModifyResponse,
    ItemSkuGoodsRelationResponse,
    ItemSkuGoodsRelationUpdateRequest,
    # SKU management
    ItemSkuListRequest,
    ItemSkuListResponse,
    ItemSkuPriceUpdateRequest,
    ItemSkuPriceUpdateResponse,
    ItemStandardApplyQueryRequest,
    ItemStandardApplyQueryResponse,
    ItemStandardApplyRequest,
    ItemStandardApplyResponse,
    ItemStandardCorrectRequest,
    ItemStandardCorrectResponse,
    ItemStockManageRequest,
    ItemStockManageResponse,
    ItemSuggestedCategoryRequest,
    ItemSuggestedCategoryResponse,
    ItemUpdateStockRequest,
    ItemUpdateStockResponse,
    ItemVideoCaptionEditRequest,
    ItemVideoCaptionEditResponse,
    ItemVideoCountRequest,
    ItemVideoCountResponse,
    ItemVideoDeleteRequest,
    ItemVideoDeleteResponse,
    ItemVideoInfoRequest,
    ItemVideoInfoResponse,
    ItemVideoListRequest,
    ItemVideoListResponse,
    ItemVideoProto,
    KeyPropOpenApiDTO,
    OpenApiAddSkuDTO,
    OpenApiAutoPassSkuDTO,
    OpenApiUpdateSkuDTO,
    QualificationDataDTO,
    ServiceRule,
    SizeChartParam,
    SkuGoodsRelationParam,
    SkuStockInfo,
    SPUPropOpenApiDTO,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncItemService:
    """商品服务

    提供商品创建、更新、查询、库存与媒体管理等功能。

    说明
    - Source of truth: 仅以 `java_sdk_reference/` 与 `docs/` 为准，不做接口猜测。
    - 异常：底层 `execute` 在开放平台返回非 0 错误码或解析失败时抛出
      `KwaixiaodianAPIError`；网络异常会抛出 `KwaixiaodianNetworkError`。
    - `uid` 必须保持为最后一个可选参数；本类与同步版在参数顺序与含义上保持一致。
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化商品服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def list(
        self,
        access_token: str,
        kwai_item_id: Optional[int] = None,
        rel_item_id: Optional[int] = None,
        item_status: Optional[int] = None,
        item_type: Optional[int] = None,
        page_number: int = 1,
        page_size: int = 20,
        on_offline_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemListResponse:
        """获取商品列表

        OpenAPI: `open.item.list.get` (GET)
        Java: OpenItemListGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemListGetRequest.java`

        Args:
            access_token: 访问令牌。
            kwai_item_id: 快手商品ID（可选）。
            rel_item_id: 关联商品ID（可选）。
            item_status: 商品状态（可选）。
            item_type: 商品类型（可选）。
            page_number: 页码，默认 1。
            page_size: 页大小，默认 20。
            on_offline_status: 上下线状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemListResponse: 商品列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。

        See Also:
            docs/开发指南和规则协议/开发文档/API限流说明.md
        """
        request = ItemListRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            rel_item_id=rel_item_id,
            item_status=item_status,
            item_type=item_type,
            page_number=page_number,
            page_size=page_size,
            on_offline_status=on_offline_status,
            api_version="1",
        )
        return await self._client.execute(request, ItemListResponse)

    async def get(
        self, access_token: str, item_id: int, uid: Optional[int] = None
    ) -> ItemGetResponse:
        """获取商品详情

        OpenAPI: `open.item.get` (GET)
        Java: OpenItemGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemGetRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品ID（`kwaiItemId`）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemGetResponse: 商品详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemGetRequest(
            access_token=access_token, uid=uid, kwai_item_id=item_id, api_version="1"
        )

        return await self._client.execute(request, ItemGetResponse)

    # ==================== 分类管理 ====================

    async def get_categories(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> ItemCategoryResponse:
        """获取商品分类

        OpenAPI: `open.item.category` (GET)
        Java: OpenItemCategoryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemCategoryResponse: 商品分类列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemCategoryRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, ItemCategoryResponse)

    async def get_category_config(
        self,
        access_token: str,
        category_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemCategoryConfigResponse:
        """获取分类配置

        OpenAPI: `open.item.category.config` (GET)
        Java: OpenItemCategoryConfigRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryConfigRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 分类ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemCategoryConfigResponse: 类目配置集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemCategoryConfigRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemCategoryConfigResponse)

    async def get_optional_categories(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> ItemOptionalCategoryResponse:
        """获取可选分类

        OpenAPI: `open.item.category.optional.get` (GET)
        Java: OpenItemCategoryOptionalGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryOptionalGetRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemOptionalCategoryResponse: 可选类目列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemOptionalCategoryRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, ItemOptionalCategoryResponse)

    async def get_suggested_categories(
        self,
        access_token: str,
        item_title: Optional[str] = None,
        image_urls: Optional[List[str]] = None,
        item_desc: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ItemSuggestedCategoryResponse:
        """获取推荐分类

        OpenAPI: `open.item.category.suggested.get` (GET)
        Java: OpenItemCategorySuggestedGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategorySuggestedGetRequest.java`

        Args:
            access_token: 访问令牌。
            item_title: 商品标题（可选）。
            image_urls: 商品图片URL列表（可选）。
            item_desc: 商品描述（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSuggestedCategoryResponse: 推荐类目集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSuggestedCategoryRequest(
            access_token=access_token,
            uid=uid,
            item_title=item_title,
            image_urls=image_urls,
            item_desc=item_desc,
            api_version="1",
        )

        return await self._client.execute(request, ItemSuggestedCategoryResponse)

    async def get_category_prop_standard(
        self,
        access_token: str,
        leaf_category_id: int,
        uid: Optional[int] = None,
    ) -> ItemCategoryPropStandardResponse:
        """获取分类属性标准

        OpenAPI: `open.item.category.prop.standard.get` (POST)
        Java: OpenItemCategoryPropStandardGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryPropStandardGetRequest.java`

        Args:
            access_token: 访问令牌。
            leaf_category_id: 叶子类目ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemCategoryPropStandardResponse: 属性标准列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemCategoryPropStandardRequest(
            access_token=access_token,
            uid=uid,
            leaf_category_id=leaf_category_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemCategoryPropStandardResponse)

    async def search_category_prop_values(
        self,
        access_token: str,
        category_id: int,
        prop_id: int,
        prop_value: Optional[str] = None,
        cursor: Optional[int] = None,
        limit: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemCategoryPropValueSearchResponse:
        """搜索分类属性值

        OpenAPI: `open.item.category.prop.value.search` (GET)
        Java: OpenItemCategoryPropValueSearchRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryPropValueSearchRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 分类ID。
            prop_id: 属性ID。
            prop_value: 属性值搜索关键字（可选）。
            cursor: 分页游标（可选）。
            limit: 条数限制（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemCategoryPropValueSearchResponse: 属性值分页结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemCategoryPropValueSearchRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            prop_id=prop_id,
            prop_value=prop_value,
            cursor=cursor,
            limit=limit,
            api_version="1",
        )

        return await self._client.execute(request, ItemCategoryPropValueSearchResponse)

    async def check_category_standard(
        self,
        access_token: str,
        leaf_category_id: int,
        uid: Optional[int] = None,
    ) -> ItemCategoryStandardCheckResponse:
        """检查分类标准

        OpenAPI: `open.item.category.standard.check` (GET)
        Java: OpenItemCategoryStandardCheckRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryStandardCheckRequest.java`

        Args:
            access_token: 访问令牌。
            leaf_category_id: 叶子类目ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemCategoryStandardCheckResponse: 标准检查结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemCategoryStandardCheckRequest(
            access_token=access_token,
            uid=uid,
            leaf_category_id=leaf_category_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemCategoryStandardCheckResponse)

    async def search_category_standard(
        self,
        access_token: str,
        standard_id: Optional[int] = None,
        leaf_category_id: Optional[int] = None,
        standard_key_prop_list: Optional[List[Dict[str, Any]]] = None,
        uid: Optional[int] = None,
    ) -> ItemCategoryStandardSearchResponse:
        """搜索分类标准

        OpenAPI: `open.item.category.standard.search` (POST)
        Java: OpenItemCategoryStandardSearchRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemCategoryStandardSearchRequest.java`

        Args:
            access_token: 访问令牌。
            standard_id: 标准ID（可选）。
            leaf_category_id: 叶子类目ID（可选）。
            standard_key_prop_list: 关键属性列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemCategoryStandardSearchResponse: 标准信息数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemCategoryStandardSearchRequest(
            access_token=access_token,
            uid=uid,
            standard_id=standard_id,
            leaf_category_id=leaf_category_id,
            standard_key_prop_list=standard_key_prop_list,
            api_version="1",
        )

        return await self._client.execute(request, ItemCategoryStandardSearchResponse)

    # ==================== 品牌管理 ====================

    async def get_brand_list(
        self,
        access_token: str,
        cursor: Optional[int] = None,
        category_id: Optional[int] = None,
        prop_id: Optional[int] = None,
        prop_value: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ItemBrandListResponse:
        """获取品牌列表

        OpenAPI: `open.item.brand.list.get` (POST)
        Java: OpenItemBrandListGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemBrandListGetRequest.java`

        Args:
            access_token: 访问令牌。
            cursor: 游标（可选）。
            category_id: 类目ID（可选）。
            prop_id: 属性ID（可选）。
            prop_value: 属性值（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemBrandListResponse: 品牌分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemBrandListRequest(
            access_token=access_token,
            uid=uid,
            cursor=cursor,
            category_id=category_id,
            prop_id=prop_id,
            prop_value=prop_value,
            api_version="1",
        )

        return await self._client.execute(request, ItemBrandListResponse)

    # ==================== 资质配置 ====================

    async def get_qualification_config(
        self,
        access_token: str,
        category_id: int,
        uid: Optional[int] = None,
    ) -> ItemQualificationConfigResponse:
        """获取资质配置

        OpenAPI: `open.item.qualification.collection.config` (POST)
        Java: OpenItemQualificationCollectionConfigRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemQualificationCollectionConfigRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 分类ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemQualificationConfigResponse: 资质配置集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemQualificationConfigRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemQualificationConfigResponse)

    # ==================== 销售属性规则 ====================

    async def get_saleprop_rule(
        self,
        access_token: str,
        category_id: int,
        spu_id: Optional[int] = None,
        item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemSalePropRuleResponse:
        """获取销售属性规则

        OpenAPI: `open.item.saleprop.rule` (POST)
        Java: OpenItemSalepropRuleRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSalepropRuleRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            spu_id: SPU ID（可选）。
            item_id: 商品ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSalePropRuleResponse: 销售属性规则配置。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSalePropRuleRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            spu_id=spu_id,
            item_id=item_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemSalePropRuleResponse)

    # ==================== SKU 管理 ====================

    async def get_sku_list(
        self,
        access_token: str,
        kwai_item_id: int,
        rel_sku_id: Optional[int] = None,
        sku_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemSkuListResponse:
        """获取SKU列表

        OpenAPI: `open.item.sku.list.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSkuListGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuListGetRequest.java)

        Args:
            access_token: 访问令牌
            kwai_item_id: 快手商品ID
            rel_sku_id: 关联SKU ID（可选）
            sku_status: SKU状态（可选）
            uid: 用户ID（可选）

        Returns:
            ItemSkuListResponse: SKU 列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            skus = await item_service.get_sku_list(
                access_token="your_token",
                kwai_item_id=12345
            )

            for sku in skus.result:
                print(f"SKU ID: {sku.sku_id}, 价格: {sku.price_yuan}元, 库存: {sku.stock}")
            ```
        """
        request = ItemSkuListRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            rel_sku_id=rel_sku_id,
            sku_status=sku_status,
            api_version="1",
        )

        return await self._client.execute(request, ItemSkuListResponse)

    async def update_sku_price(
        self,
        access_token: str,
        item_id: int,
        sku_id: int,
        price: int,
        uid: Optional[int] = None,
    ) -> ItemSkuPriceUpdateResponse:
        """更新SKU价格

        OpenAPI: `open.item.sku.price.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSkuPriceUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuPriceUpdateRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            sku_id: SKU ID
            price: 新价格（分）
            uid: 用户ID（可选）

        Returns:
            ItemSkuPriceUpdateResponse: 价格更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.update_sku_price(
                access_token="your_token",
                item_id=12345,
                sku_id=67890,
                price=9900  # 99元
            )

            if result.is_success:
                print("SKU价格更新成功")
            ```
        """
        request = ItemSkuPriceUpdateRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            sku_id=sku_id,
            price=price,
            api_version="1",
        )

        return await self._client.execute(request, ItemSkuPriceUpdateResponse)

    async def add_sku_goods_relation(
        self,
        access_token: str,
        item_id: int,
        relations: List[SkuGoodsRelationParam],
        uid: Optional[int] = None,
    ) -> ItemSkuGoodsRelationModifyResponse:
        """添加SKU商品关系

        OpenAPI: `open.item.sku.goods.relation.add` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSkuGoodsRelationAddRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuGoodsRelationAddRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            relations: SKU 与三方货品关系列表
            uid: 用户ID（可选）

        Returns:
            ItemSkuGoodsRelationModifyResponse: 修改结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemSkuGoodsRelationAddRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            sku_goods_relation=relations,
            api_version="1",
        )

        return await self._client.execute(request, ItemSkuGoodsRelationModifyResponse)

    async def update_sku_goods_relation(
        self,
        access_token: str,
        item_id: int,
        relations: List[SkuGoodsRelationParam],
        uid: Optional[int] = None,
    ) -> ItemSkuGoodsRelationModifyResponse:
        """更新SKU商品关系

        OpenAPI: `open.item.sku.goods.relation.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSkuGoodsRelationUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuGoodsRelationUpdateRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            relations: SKU 与三方货品关系列表
            uid: 用户ID（可选）

        Returns:
            ItemSkuGoodsRelationModifyResponse: 修改结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemSkuGoodsRelationUpdateRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            sku_goods_relation=relations,
            api_version="1",
        )

        return await self._client.execute(request, ItemSkuGoodsRelationModifyResponse)

    async def get_sku_goods_relation(
        self,
        access_token: str,
        sku_ids: List[int],
        uid: Optional[int] = None,
    ) -> ItemSkuGoodsRelationResponse:
        """获取SKU商品关系

        OpenAPI: `open.item.sku.goods.relation.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSkuGoodsRelationGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuGoodsRelationGetRequest.java)

        Args:
            access_token: 访问令牌
            sku_ids: SKU ID 列表
            uid: 用户ID（可选）

        Returns:
            ItemSkuGoodsRelationResponse: 关系数据

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemSkuGoodsRelationGetRequest(
            access_token=access_token,
            uid=uid,
            sku_id=sku_ids,
            api_version="1",
        )

        return await self._client.execute(request, ItemSkuGoodsRelationResponse)

    async def delete_sku_goods_relation(
        self,
        access_token: str,
        item_id: int,
        relations: List[SkuGoodsRelationParam],
        update_item_stock_model: Optional[bool] = None,
        uid: Optional[int] = None,
    ) -> ItemSkuGoodsRelationModifyResponse:
        """删除SKU商品关系

        OpenAPI: `open.item.sku.goods.relation.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSkuGoodsRelationDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuGoodsRelationDeleteRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            relations: SKU 与三方货品关系列表
            update_item_stock_model: 是否更新商品库存模型（可选）
            uid: 用户ID（可选）

        Returns:
            ItemSkuGoodsRelationModifyResponse: 修改结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemSkuGoodsRelationDeleteRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            sku_goods_relation=relations,
            update_item_stock_model=update_item_stock_model,
            api_version="1",
        )

        return await self._client.execute(request, ItemSkuGoodsRelationModifyResponse)

    async def manage_stock(
        self,
        access_token: str,
        sku_stock_infos: List[SkuStockInfo],
        seq_no: Optional[str] = None,
        item_id: Optional[int] = None,
        category_id: Optional[int] = None,
        support_negative_stock: Optional[bool] = None,
        uid: Optional[int] = None,
    ) -> ItemStockManageResponse:
        """库存管理

        OpenAPI: `open.stock.manage` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenStockManageRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenStockManageRequest.java)

        Args:
            access_token: 访问令牌
            sku_stock_infos: SKU 库存操作列表
            seq_no: 幂等序列号（可选）
            item_id: 商品ID（可选）
            category_id: 类目ID（可选）
            support_negative_stock: 是否支持负库存（可选）
            uid: 用户ID（可选）

        Returns:
            ItemStockManageResponse: 操作结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemStockManageRequest(
            access_token=access_token,
            uid=uid,
            seq_no=seq_no,
            item_id=item_id,
            category_id=category_id,
            sku_stock_infos=sku_stock_infos,
            support_negative_stock=support_negative_stock,
            api_version="1",
        )

        return await self._client.execute(request, ItemStockManageResponse)

    # ==================== 媒体管理 API ====================

    async def upload_image(
        self,
        access_token: str,
        upload_type: int,
        img_url: Optional[str] = None,
        img_bytes: Optional[bytes] = None,
        uid: Optional[int] = None,
    ) -> ItemImageUploadResponse:
        """商品图片上传

        OpenAPI: `open.item.image.upload` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemImageUploadRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemImageUploadRequest.java)

        Args:
            access_token: 访问令牌
            upload_type: 上传类型（1: URL, 2: 文件）
            img_url: 图片URL（URL上传时使用）
            img_bytes: 图片字节数据（文件上传时使用）
            uid: 用户ID（可选）

        Returns:
            ItemImageUploadResponse: 图片上传结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            # URL上传
            result = await item_service.upload_image(
                access_token="your_token",
                upload_type=1,
                img_url="https://example.com/image.jpg"
            )
            # 文件上传
            with open("image.jpg", "rb") as f:
                img_bytes = f.read()
            result = await item_service.upload_image(
                access_token="your_token",
                upload_type=2,
                img_bytes=img_bytes
            )
            ```
        """
        request = ItemImageUploadRequest(
            access_token=access_token,
            uid=uid,
            img_url=img_url,
            upload_type=upload_type,
            img_bytes=img_bytes,
            api_version="1",
        )

        return await self._client.execute(request, ItemImageUploadResponse)

    async def issue_upload_token(
        self,
        access_token: str,
        material_upload_type: int,
        file_name: str,
        file_length: int,
        uid: Optional[int] = None,
    ) -> ItemMaterialUploadTokenIssueResponse:
        """素材上传 token 签发

        OpenAPI: `open.item.material.upload.token.issue` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMaterialUploadTokenIssueRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMaterialUploadTokenIssueRequest.java)

        Args:
            access_token: 访问令牌
            material_upload_type: 素材上传类型
            file_name: 文件名
            file_length: 文件长度
            uid: 用户ID（可选）

        Returns:
            ItemMaterialUploadTokenIssueResponse: 签发结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.issue_upload_token(
                access_token="your_token",
                material_upload_type=1,
                file_name="video.mp4",
                file_length=1024000
            )
            ```
        """
        request = ItemMaterialUploadTokenIssueRequest(
            access_token=access_token,
            uid=uid,
            material_upload_type=material_upload_type,
            file_name=file_name,
            file_length=file_length,
            api_version="1",
        )

        return await self._client.execute(request, ItemMaterialUploadTokenIssueResponse)

    async def get_video_list(
        self,
        access_token: str,
        video_type: Optional[int] = None,
        aspect_ratio: Optional[int] = None,
        audit_status: Optional[int] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        page_index: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoListResponse:
        """获取视频列表

        OpenAPI: `open.item.video.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoListRequest.java)

        Args:
            access_token: 访问令牌
            video_type: 视频类型（可选）
            aspect_ratio: 视频宽高比（可选）
            audit_status: 审核状态（可选）
            create_time_start: 创建开始时间（毫秒，可选）
            create_time_end: 创建结束时间（毫秒，可选）
            page_index: 页码（可选）
            page_size: 页面大小（可选）
            uid: 用户ID（可选）

        Returns:
            ItemVideoListResponse: 视频分页列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemVideoListRequest(
            access_token=access_token,
            uid=uid,
            video_type=video_type,
            aspect_ratio=aspect_ratio,
            audit_status=audit_status,
            create_time_start=create_time_start,
            create_time_end=create_time_end,
            page_index=page_index,
            page_size=page_size,
            api_version="1",
        )

        return await self._client.execute(request, ItemVideoListResponse)

    async def delete_video(
        self,
        access_token: str,
        video_ids: List[str],
        video_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoDeleteResponse:
        """删除视频

        OpenAPI: `open.item.video.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoDeleteRequest.java)

        Args:
            access_token: 访问令牌
            video_ids: 视频ID列表
            video_type: 视频类型（可选）
            uid: 用户ID（可选）

        Returns:
            ItemVideoDeleteResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemVideoDeleteRequest(
            access_token=access_token,
            uid=uid,
            video_id=video_ids,
            video_type=video_type,
            api_version="1",
        )

        return await self._client.execute(request, ItemVideoDeleteResponse)

    # ==================== 高级操作 API ====================

    async def edit_autopass(
        self,
        access_token: str,
        item_id: int,
        purchase_limit: Optional[bool] = None,
        limit_count: Optional[int] = None,
        item_remark: Optional[str] = None,
        sku_list: Optional[List[OpenApiAutoPassSkuDTO]] = None,
        service_rule: Optional[ServiceRule] = None,
        express_template_id: Optional[int] = None,
        sale_time_flag: Optional[bool] = None,
        time_of_sale: Optional[int] = None,
        pay_way: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemAutopassEditResponse:
        """商品自动通过编辑

        OpenAPI: `open.item.autopass.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemAutopassEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemAutopassEditRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            purchase_limit: 购买限制
            limit_count: 限制数量
            item_remark: 商品备注
            sku_list: SKU列表
            service_rule: 服务规则
            express_template_id: 快递模板ID
            sale_time_flag: 销售时间标志
            time_of_sale: 销售时间
            pay_way: 支付方式
            uid: 用户ID（可选）

        Returns:
            ItemAutopassEditResponse: 编辑结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.edit_autopass(
                access_token="your_token",
                item_id=12345,
                purchase_limit=True,
                limit_count=100
            )
            ```
        """
        request = ItemAutopassEditRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            purchase_limit=purchase_limit,
            limit_count=limit_count,
            item_remark=item_remark,
            sku_list=sku_list,
            service_rule=service_rule,
            express_template_id=express_template_id,
            sale_time_flag=sale_time_flag,
            time_of_sale=time_of_sale,
            pay_way=pay_way,
            api_version="1",
        )

        return await self._client.execute(request, ItemAutopassEditResponse)

    async def update_detail_images(
        self,
        access_token: str,
        kwai_item_id: int,
        detail_image_urls: List[str],
        uid: Optional[int] = None,
    ) -> ItemDetailImagesUpdateResponse:
        """更新商品详情图片

        OpenAPI: `open.item.detail.images.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDetailImagesUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDetailImagesUpdateRequest.java)

        Args:
            access_token: 访问令牌
            kwai_item_id: 快手商品ID
            detail_image_urls: 详情图片URL列表
            uid: 用户ID（可选）

        Returns:
            ItemDetailImagesUpdateResponse: 更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.update_detail_images(
                access_token="your_token",
                kwai_item_id=12345,
                detail_image_urls=[
                    "https://example.com/image1.jpg",
                    "https://example.com/image2.jpg"
                ]
            )
            ```
        """
        request = ItemDetailImagesUpdateRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            detail_image_urls=detail_image_urls,
            api_version="1",
        )

        return await self._client.execute(request, ItemDetailImagesUpdateResponse)

    async def get_detail_page_link(
        self,
        access_token: str,
        item_id: int,
        type: int,
        item_product_client_info: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> ItemDetailPageLinkResponse:
        """获取商品详情页链接

        OpenAPI: `open.item.detail.page.link` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDetailPageLinkRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDetailPageLinkRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            type: 类型
            item_product_client_info: 商品客户端信息
            uid: 用户ID（可选）

        Returns:
            ItemDetailPageLinkResponse: 详情页链接

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.get_detail_page_link(
                access_token="your_token",
                item_id=12345,
                type=1
            )
            ```
        """
        request = ItemDetailPageLinkRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            type=type,
            item_product_client_info=item_product_client_info,
            api_version="1",
        )

        return await self._client.execute(request, ItemDetailPageLinkResponse)

    async def get_diagnosis(
        self,
        access_token: str,
        item_id: int,
        uid: Optional[int] = None,
    ) -> ItemDiagnosisGetResponse:
        """获取商品诊断信息

        OpenAPI: `open.item.diagnosis.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDiagnosisGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDiagnosisGetRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            uid: 用户ID（可选）

        Returns:
            ItemDiagnosisGetResponse: 诊断信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.get_diagnosis(
                access_token="your_token",
                item_id=12345
            )
            ```
        """
        request = ItemDiagnosisGetRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemDiagnosisGetResponse)

    async def apply_main_pic_video(
        self,
        access_token: str,
        item_id: int,
        video_id: str,
        video_type: int,
        uid: Optional[int] = None,
    ) -> ItemMainPicVideoApplyResponse:
        """申请商品主图视频

        OpenAPI: `open.item.main.pic.video.apply` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMainPicVideoApplyRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMainPicVideoApplyRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            video_id: 视频ID
            video_type: 视频类型
            uid: 用户ID（可选）

        Returns:
            ItemMainPicVideoApplyResponse: 申请结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.apply_main_pic_video(
                access_token="your_token",
                item_id=12345,
                video_id="video_123",
                video_type=1
            )
            ```
        """
        request = ItemMainPicVideoApplyRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            video_id=video_id,
            video_type=video_type,
            api_version="1",
        )

        return await self._client.execute(request, ItemMainPicVideoApplyResponse)

    async def delete_main_pic_video(
        self,
        access_token: str,
        item_id: int,
        uid: Optional[int] = None,
    ) -> ItemMainPicVideoDeleteResponse:
        """删除商品主图视频

        OpenAPI: `open.item.main.pic.video.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMainPicVideoDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMainPicVideoDeleteRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            uid: 用户ID（可选）

        Returns:
            ItemMainPicVideoDeleteResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.delete_main_pic_video(
                access_token="your_token",
                item_id=12345
            )
            ```
        """
        request = ItemMainPicVideoDeleteRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemMainPicVideoDeleteResponse)

    async def update_shelf_status(
        self,
        access_token: str,
        kwai_item_id: int,
        shelf_status: int,
        uid: Optional[int] = None,
    ) -> ItemShelfStatusUpdateResponse:
        """更新商品上下架状态

        OpenAPI: `open.item.shelf.status.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemShelfStatusUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemShelfStatusUpdateRequest.java)

        Args:
            access_token: 访问令牌
            kwai_item_id: 快手商品ID
            shelf_status: 上架状态
            uid: 用户ID（可选）

        Returns:
            ItemShelfStatusUpdateResponse: 更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.update_shelf_status(
                access_token="your_token",
                kwai_item_id=12345,
                shelf_status=1  # 1: 上架, 0: 下架
            )
            ```
        """
        request = ItemShelfStatusUpdateRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            shelf_status=shelf_status,
            api_version="1",
        )

        return await self._client.execute(request, ItemShelfStatusUpdateResponse)

    async def precheck_new_item(
        self,
        access_token: str,
        leaf_category_id: int,
        uid: Optional[int] = None,
    ) -> ItemNewPrecheckResponse:
        """新建商品预检

        OpenAPI: `open.item.new.precheck` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemNewPrecheckRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemNewPrecheckRequest.java)

        Args:
            access_token: 访问令牌
            leaf_category_id: 叶子类目ID
            uid: 用户ID（可选）

        Returns:
            ItemNewPrecheckResponse: 预检结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出

        Examples:
            ```python
            result = await item_service.precheck_new_item(
                access_token="your_token",
                leaf_category_id=12345
            )
            ```
        """
        request = ItemNewPrecheckRequest(
            access_token=access_token,
            uid=uid,
            leaf_category_id=leaf_category_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemNewPrecheckResponse)

    async def new(
        self,
        access_token: str,
        title: Optional[str] = None,
        rel_item_id: Optional[int] = None,
        category_id: Optional[int] = None,
        image_urls: Optional[List[str]] = None,
        sku_list: Optional[List[OpenApiAddSkuDTO]] = None,
        purchase_limit: Optional[bool] = None,
        limit_count: Optional[int] = None,
        item_prop_values: Optional[List[AddItemPropValue]] = None,
        details: Optional[str] = None,
        detail_image_urls: Optional[List[str]] = None,
        stock_partner: Optional[bool] = None,
        item_remark: Optional[str] = None,
        service_rule: Optional[ServiceRule] = None,
        express_template_id: Optional[int] = None,
        sale_time_flag: Optional[bool] = None,
        time_of_sale: Optional[int] = None,
        pay_way: Optional[int] = None,
        multiple_stock: Optional[bool] = None,
        poi_ids: Optional[List[int]] = None,
        white_base_image_url: Optional[str] = None,
        transparent_image_url: Optional[str] = None,
        short_title: Optional[str] = None,
        selling_point: Optional[str] = None,
        instructions: Optional[str] = None,
        save_shelf_item_qualification_data: Optional[List[QualificationDataDTO]] = None,
        off_shore_mode: Optional[int] = None,
        spu_id: Optional[int] = None,
        item_video_id: Optional[str] = None,
        three_quarters_image_urls: Optional[List[str]] = None,
        item_video: Optional[ItemVideoProto] = None,
        size_chart_template_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemNewResponse:
        """新建商品

        OpenAPI: `open.item.new` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemNewRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemNewRequest.java)

        Args:
            access_token: 访问令牌
            title: 商品标题（可选）
            rel_item_id: 关联商品ID（可选）
            category_id: 分类ID（可选）
            image_urls: 图片URL列表（可选）
            sku_list: SKU 列表（可选）
            purchase_limit: 购买限制（可选）
            limit_count: 限制数量（可选）
            item_prop_values: 属性列表（可选）
            details: 详情描述（可选）
            detail_image_urls: 详情图片（可选）
            stock_partner: 库存合作（可选）
            item_remark: 备注（可选）
            service_rule: 服务规则（可选）
            express_template_id: 运费模板ID（可选）
            sale_time_flag: 定时上架标记（可选）
            time_of_sale: 上架时间戳（可选）
            pay_way: 支付方式（可选）
            multiple_stock: 多库存开关（可选）
            poi_ids: 门店ID列表（可选）
            white_base_image_url: 白底图（可选）
            transparent_image_url: 透明图（可选）
            short_title: 短标题（可选）
            selling_point: 卖点（可选）
            instructions: 使用说明（可选）
            save_shelf_item_qualification_data: 资质数据（可选）
            off_shore_mode: 跨境模式（可选）
            spu_id: SPU ID（可选）
            item_video_id: 视频ID（可选）
            three_quarters_image_urls: 3/4图（可选）
            item_video: 视频对象（可选）
            size_chart_template_id: 尺码表模板ID（可选）
            uid: 用户ID（可选）

        Returns:
            ItemNewResponse: 新建结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemNewRequest(
            access_token=access_token,
            uid=uid,
            title=title,
            rel_item_id=rel_item_id,
            category_id=category_id,
            image_urls=image_urls,
            sku_list=sku_list,
            purchase_limit=purchase_limit,
            limit_count=limit_count,
            item_prop_values=item_prop_values,
            details=details,
            detail_image_urls=detail_image_urls,
            stock_partner=stock_partner,
            item_remark=item_remark,
            service_rule=service_rule,
            express_template_id=express_template_id,
            sale_time_flag=sale_time_flag,
            time_of_sale=time_of_sale,
            pay_way=pay_way,
            multiple_stock=multiple_stock,
            poi_ids=poi_ids,
            white_base_image_url=white_base_image_url,
            transparent_image_url=transparent_image_url,
            short_title=short_title,
            selling_point=selling_point,
            instructions=instructions,
            save_shelf_item_qualification_data=save_shelf_item_qualification_data,
            off_shore_mode=off_shore_mode,
            spu_id=spu_id,
            item_video_id=item_video_id,
            three_quarters_image_urls=three_quarters_image_urls,
            item_video=item_video,
            size_chart_template_id=size_chart_template_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemNewResponse)

    async def edit(
        self,
        access_token: str,
        item_id: int,
        title: Optional[str] = None,
        category_id: Optional[int] = None,
        image_urls: Optional[List[str]] = None,
        sku_list: Optional[List[OpenApiUpdateSkuDTO]] = None,
        item_video_id: Optional[str] = None,
        purchase_limit: Optional[bool] = None,
        limit_count: Optional[int] = None,
        item_prop_values: Optional[List[ItemPropValue]] = None,
        details: Optional[str] = None,
        detail_image_urls: Optional[List[str]] = None,
        update_detail_image_urls: Optional[bool] = None,
        item_remark: Optional[str] = None,
        service_rule: Optional[ServiceRule] = None,
        express_template_id: Optional[int] = None,
        sale_time_flag: Optional[bool] = None,
        time_of_sale: Optional[int] = None,
        pay_way: Optional[int] = None,
        update_item_prop_values: Optional[bool] = None,
        poi_ids: Optional[List[int]] = None,
        white_base_image_url: Optional[str] = None,
        transparent_image_url: Optional[str] = None,
        short_title: Optional[str] = None,
        selling_point: Optional[str] = None,
        instructions: Optional[str] = None,
        save_shelf_item_qualification_data: Optional[List[QualificationDataDTO]] = None,
        update_item_qualification: Optional[bool] = None,
        spu_id: Optional[int] = None,
        update_three_quarters_image_urls: Optional[bool] = None,
        three_quarters_image_urls: Optional[List[str]] = None,
        item_video: Optional[ItemVideoProto] = None,
        size_chart_template_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemEditResponse:
        """编辑商品

        OpenAPI: `open.item.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemEditRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            title: 商品标题（可选）
            category_id: 分类ID（可选）
            image_urls: 图片URL列表（可选）
            sku_list: SKU 列表（可选）
            item_video_id: 视频ID（可选）
            purchase_limit: 购买限制（可选）
            limit_count: 限制数量（可选）
            item_prop_values: 属性列表（可选）
            details: 详情描述（可选）
            detail_image_urls: 详情图片（可选）
            update_detail_image_urls: 是否更新详情图（可选）
            item_remark: 备注（可选）
            service_rule: 服务规则（可选）
            express_template_id: 运费模板ID（可选）
            sale_time_flag: 定时上架标记（可选）
            time_of_sale: 上架时间戳（可选）
            pay_way: 支付方式（可选）
            update_item_prop_values: 是否更新属性（可选）
            poi_ids: 门店ID列表（可选）
            white_base_image_url: 白底图（可选）
            transparent_image_url: 透明图（可选）
            short_title: 短标题（可选）
            selling_point: 卖点（可选）
            instructions: 使用说明（可选）
            save_shelf_item_qualification_data: 资质数据（可选）
            update_item_qualification: 是否更新资质（可选）
            spu_id: SPU ID（可选）
            update_three_quarters_image_urls: 是否更新3/4图（可选）
            three_quarters_image_urls: 3/4图（可选）
            item_video: 视频对象（可选）
            size_chart_template_id: 尺码表模板ID（可选）
            uid: 用户ID（可选）

        Returns:
            ItemEditResponse: 编辑结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemEditRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            title=title,
            category_id=category_id,
            image_urls=image_urls,
            sku_list=sku_list,
            item_video_id=item_video_id,
            purchase_limit=purchase_limit,
            limit_count=limit_count,
            item_prop_values=item_prop_values,
            details=details,
            detail_image_urls=detail_image_urls,
            update_detail_image_urls=update_detail_image_urls,
            item_remark=item_remark,
            service_rule=service_rule,
            express_template_id=express_template_id,
            sale_time_flag=sale_time_flag,
            time_of_sale=time_of_sale,
            pay_way=pay_way,
            update_item_prop_values=update_item_prop_values,
            poi_ids=poi_ids,
            white_base_image_url=white_base_image_url,
            transparent_image_url=transparent_image_url,
            short_title=short_title,
            selling_point=selling_point,
            instructions=instructions,
            save_shelf_item_qualification_data=save_shelf_item_qualification_data,
            update_item_qualification=update_item_qualification,
            spu_id=spu_id,
            update_three_quarters_image_urls=update_three_quarters_image_urls,
            three_quarters_image_urls=three_quarters_image_urls,
            item_video=item_video,
            size_chart_template_id=size_chart_template_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemEditResponse)

    # ==================== 缺失API方法 - 尺码表管理 ====================

    async def get_size_chart_group_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> ItemSizeChartGroupListGetResponse:
        """获取尺码表分组列表

        OpenAPI: `open.item.size.chart.group.list.get` (GET)
        Java: OpenItemSizeChartGroupListGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartGroupListGetRequest.java`

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartGroupListGetResponse: 尺码表分组列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartGroupListGetRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartGroupListGetResponse)

    async def add_size_chart_template(
        self,
        access_token: str,
        size_chart: AddSizeChartParam,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateAddResponse:
        """添加尺码表模板

        OpenAPI: `open.item.size.chart.template.add` (POST)
        Java: OpenItemSizeChartTemplateAddRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateAddRequest.java`

        Args:
            access_token: 访问令牌。
            size_chart: 尺码表模板数据。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateAddResponse: 添加结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateAddRequest(
            access_token=access_token,
            uid=uid,
            size_chart=size_chart,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartTemplateAddResponse)

    async def delete_size_chart_template(
        self,
        access_token: str,
        size_chart_id: int,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateDeleteResponse:
        """删除尺码表模板

        OpenAPI: `open.item.size.chart.template.delete` (GET)
        Java: OpenItemSizeChartTemplateDeleteRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateDeleteRequest.java`

        Args:
            access_token: 访问令牌。
            size_chart_id: 尺码表模板ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateDeleteRequest(
            access_token=access_token,
            uid=uid,
            size_chart_id=size_chart_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartTemplateDeleteResponse)

    async def edit_size_chart_template(
        self,
        access_token: str,
        size_chart: SizeChartParam,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateEditResponse:
        """编辑尺码表模板

        OpenAPI: `open.item.size.chart.template.edit` (GET)
        Java: OpenItemSizeChartTemplateEditRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateEditRequest.java`

        Args:
            access_token: 访问令牌。
            size_chart: 尺码表模板数据。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateEditResponse: 编辑结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateEditRequest(
            access_token=access_token,
            uid=uid,
            size_chart=size_chart,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartTemplateEditResponse)

    async def get_size_chart_template(
        self,
        access_token: str,
        size_chart_id: int,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateGetResponse:
        """获取尺码表模板

        OpenAPI: `open.item.size.chart.template.get` (GET)
        Java: OpenItemSizeChartTemplateGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateGetRequest.java`

        Args:
            access_token: 访问令牌。
            size_chart_id: 尺码表模板ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateGetResponse: 模板详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateGetRequest(
            access_token=access_token,
            uid=uid,
            size_chart_id=size_chart_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartTemplateGetResponse)

    async def get_size_chart_template_list(
        self,
        access_token: str,
        template_type_prop_value_id: Optional[int] = None,
        page_num: Optional[int] = 1,
        page_size: Optional[int] = 20,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateListGetResponse:
        """获取尺码表模板列表

        OpenAPI: `open.item.size.chart.template.list.get` (GET)
        Java: OpenItemSizeChartTemplateListGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateListGetRequest.java`

        Args:
            access_token: 访问令牌。
            template_type_prop_value_id: 模板类型属性值ID（可选）。
            page_num: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateListGetResponse: 模板分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateListGetRequest(
            access_token=access_token,
            uid=uid,
            template_type_prop_value_id=template_type_prop_value_id,
            page_num=page_num,
            page_size=page_size,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartTemplateListGetResponse)

    async def get_size_chart_template_meta(
        self,
        access_token: str,
        category_id: int,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateMetaGetResponse:
        """获取尺码表模板元数据

        OpenAPI: `open.item.size.chart.template.meta.get` (GET)
        Java: OpenItemSizeChartTemplateMetaGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateMetaGetRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateMetaGetResponse: 元数据内容。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateMetaGetRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemSizeChartTemplateMetaGetResponse)

    # ==================== 缺失API方法 - 其他功能 ====================

    async def get_deleted_items(
        self,
        access_token: str,
        item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemDeletedGetResponse:
        """获取已删除商品

        OpenAPI: `open.item.deleted.get` (GET)
        Java: OpenItemDeletedGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDeletedGetRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemDeletedGetResponse: 已删除商品数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemDeletedGetRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemDeletedGetResponse)

    async def get_material_detail(
        self,
        access_token: str,
        material_id: int,
        material_upload_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemMaterialDetailGetResponse:
        """获取素材详情

        OpenAPI: `open.item.material.detail.get` (GET)
        Java: OpenItemMaterialDetailGetRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMaterialDetailGetRequest.java`

        Args:
            access_token: 访问令牌。
            material_id: 素材ID。
            material_upload_type: 素材上传类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemMaterialDetailGetResponse: 素材详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemMaterialDetailGetRequest(
            access_token=access_token,
            uid=uid,
            material_id=material_id,
            material_upload_type=material_upload_type,
            api_version="1",
        )

        return await self._client.execute(request, ItemMaterialDetailGetResponse)

    async def verify_upload_token(
        self,
        access_token: str,
        token: str,
        material_upload_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemMaterialUploadTokenVerifyResponse:
        """验证上传令牌

        OpenAPI: `open.item.material.upload.token.verify` (POST)
        Java: OpenItemMaterialUploadTokenVerifyRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMaterialUploadTokenVerifyRequest.java`

        Args:
            access_token: 访问令牌。
            token: 上传令牌。
            material_upload_type: 素材上传类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemMaterialUploadTokenVerifyResponse: 验证结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemMaterialUploadTokenVerifyRequest(
            access_token=access_token,
            uid=uid,
            token=token,
            material_upload_type=material_upload_type,
            api_version="1",
        )

        return await self._client.execute(
            request, ItemMaterialUploadTokenVerifyResponse
        )

    async def apply_item_standard(
        self,
        access_token: str,
        category_id: int,
        key_prop_list: Optional[List[KeyPropOpenApiDTO]] = None,
        spu_prop_list: Optional[List[SPUPropOpenApiDTO]] = None,
        standard_images: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> ItemStandardApplyResponse:
        """申请商品标准

        OpenAPI: `open.item.standard.apply` (POST)
        Java: OpenItemStandardApplyRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemStandardApplyRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            key_prop_list: 关键属性列表（可选）。
            spu_prop_list: SPU属性列表（可选）。
            standard_images: 标准图片URL列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemStandardApplyResponse: 申请结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemStandardApplyRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            key_prop_list=key_prop_list,
            spu_prop_list=spu_prop_list,
            standard_images=standard_images,
            api_version="1",
        )

        return await self._client.execute(request, ItemStandardApplyResponse)

    async def query_standard_apply(
        self,
        access_token: str,
        category_id: Optional[List[int]] = None,
        standard_status: Optional[int] = None,
        standard_name: Optional[str] = None,
        apply_type: Optional[int] = None,
        standard_audit_status: Optional[int] = None,
        limit: Optional[int] = None,
        cursor: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemStandardApplyQueryResponse:
        """查询标准申请状态

        OpenAPI: `open.item.standard.apply.query` (GET)
        Java: OpenItemStandardApplyQueryRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemStandardApplyQueryRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 类目ID列表（可选）。
            standard_status: 标准状态（可选）。
            standard_name: 标准名称（可选）。
            apply_type: 申请类型（可选）。
            standard_audit_status: 标准审核状态（可选）。
            limit: 限制数量（可选）。
            cursor: 游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemStandardApplyQueryResponse: 申请状态数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemStandardApplyQueryRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            standard_status=standard_status,
            standard_name=standard_name,
            apply_type=apply_type,
            standard_audit_status=standard_audit_status,
            limit=limit,
            cursor=cursor,
            api_version="1",
        )

        return await self._client.execute(request, ItemStandardApplyQueryResponse)

    async def correct_item_standard(
        self,
        access_token: str,
        category_id: int,
        standard_id: int,
        key_prop_list: Optional[List[KeyPropOpenApiDTO]] = None,
        spu_prop_list: Optional[List[SPUPropOpenApiDTO]] = None,
        modify_reason: Optional[str] = None,
        modify_image_url: Optional[str] = None,
        standard_images: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> ItemStandardCorrectResponse:
        """纠正商品标准

        OpenAPI: `open.item.standard.correct` (POST)
        Java: OpenItemStandardCorrectRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemStandardCorrectRequest.java`

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            standard_id: 标准ID。
            key_prop_list: 关键属性列表（可选）。
            spu_prop_list: SPU属性列表（可选）。
            modify_reason: 修改原因（可选）。
            modify_image_url: 修改图片URL（可选）。
            standard_images: 标准图片URL列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemStandardCorrectResponse: 提交纠正结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemStandardCorrectRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            standard_id=standard_id,
            key_prop_list=key_prop_list,
            spu_prop_list=spu_prop_list,
            modify_reason=modify_reason,
            modify_image_url=modify_image_url,
            standard_images=standard_images,
            api_version="1",
        )

        return await self._client.execute(request, ItemStandardCorrectResponse)

    async def edit_video_caption(
        self,
        access_token: str,
        video_id: str,
        caption: str,
        video_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoCaptionEditResponse:
        """编辑视频字幕

        OpenAPI: `open.item.video.caption.edit` (POST)
        Java: OpenItemVideoCaptionEditRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoCaptionEditRequest.java`

        Args:
            access_token: 访问令牌。
            video_id: 视频ID。
            caption: 字幕内容。
            video_type: 视频类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemVideoCaptionEditResponse: 编辑提交结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemVideoCaptionEditRequest(
            access_token=access_token,
            uid=uid,
            video_id=video_id,
            caption=caption,
            video_type=video_type,
            api_version="1",
        )

        return await self._client.execute(request, ItemVideoCaptionEditResponse)

    async def get_video_count(
        self,
        access_token: str,
        video_type: Optional[int] = None,
        aspect_ratio: Optional[int] = None,
        audit_status: Optional[int] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoCountResponse:
        """获取视频数量

        OpenAPI: `open.item.video.count` (POST)
        Java: OpenItemVideoCountRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoCountRequest.java`

        Args:
            access_token: 访问令牌。
            video_type: 视频类型（可选）。
            aspect_ratio: 视频宽高比（可选）。
            audit_status: 审核状态（可选）。
            create_time_start: 创建开始时间（毫秒，可选）。
            create_time_end: 创建结束时间（毫秒，可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemVideoCountResponse: 数量聚合结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemVideoCountRequest(
            access_token=access_token,
            uid=uid,
            video_type=video_type,
            aspect_ratio=aspect_ratio,
            audit_status=audit_status,
            create_time_start=create_time_start,
            create_time_end=create_time_end,
            api_version="1",
        )

        return await self._client.execute(request, ItemVideoCountResponse)

    async def get_video_info(
        self,
        access_token: str,
        video_id: str,
        video_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoInfoResponse:
        """获取视频信息

        OpenAPI: `open.item.video.info` (GET)
        Java: OpenItemVideoInfoRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoInfoRequest.java`

        Args:
            access_token: 访问令牌。
            video_id: 视频ID。
            video_type: 视频类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemVideoInfoResponse: 视频详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemVideoInfoRequest(
            access_token=access_token,
            uid=uid,
            video_id=video_id,
            video_type=video_type,
            api_version="1",
        )

        return await self._client.execute(request, ItemVideoInfoResponse)

    async def delete(
        self, access_token: str, item_id: int, uid: Optional[int] = None
    ) -> ItemDeleteResponse:
        """删除商品

        OpenAPI: `open.item.delete` (POST)
        Java: OpenItemDeleteRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDeleteRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品ID（`kwaiItemId`）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemDeleteRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=item_id,
            api_version="1",
        )

        return await self._client.execute(request, ItemDeleteResponse)

    async def update_stock(
        self,
        access_token: str,
        item_id: int,
        sku_id: int,
        stock: int,
        change_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemUpdateStockResponse:
        """更新商品SKU库存

        OpenAPI: `open.item.sku.stock.update` (POST)
        Java: OpenItemSkuStockUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuStockUpdateRequest.java`

        Args:
            access_token: 访问令牌。
            item_id: 商品ID。
            sku_id: SKU ID。
            stock: 库存数量。
            change_type: 变更类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemUpdateStockResponse: 库存更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemUpdateStockRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            sku_id=sku_id,
            stock=stock,
            change_type=change_type,
            api_version="1",
        )

        return await self._client.execute(request, ItemUpdateStockResponse)


class SyncItemService:
    """同步商品服务

    提供商品创建、更新、查询、库存管理等功能的同步版本。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化商品服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def list(
        self,
        access_token: str,
        kwai_item_id: Optional[int] = None,
        rel_item_id: Optional[int] = None,
        item_status: Optional[int] = None,
        item_type: Optional[int] = None,
        page_number: int = 1,
        page_size: int = 20,
        on_offline_status: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemListResponse:
        """获取商品列表（同步）

        OpenAPI: `open.item.list.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemListGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemListGetRequest.java)

        Args:
            access_token: 访问令牌
            kwai_item_id: 快手商品ID（可选）
            rel_item_id: 关联商品ID（可选）
            item_status: 商品状态（可选）
            item_type: 商品类型（可选）
            page_number: 页码，默认 1
            page_size: 页大小，默认 20
            on_offline_status: 上下线状态（可选）
            uid: 用户ID（可选）

        Returns:
            ItemListResponse: 商品列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemListRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            rel_item_id=rel_item_id,
            item_status=item_status,
            item_type=item_type,
            page_number=page_number,
            page_size=page_size,
            on_offline_status=on_offline_status,
            api_version="1",
        )

        return self._client.execute(request, ItemListResponse)

    def get(
        self, access_token: str, item_id: int, uid: Optional[int] = None
    ) -> ItemGetResponse:
        """获取商品详情（同步）

        OpenAPI: `open.item.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemGetRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID（kwaiItemId）
            uid: 用户ID（可选）

        Returns:
            ItemGetResponse: 商品详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemGetRequest(
            access_token=access_token, uid=uid, kwai_item_id=item_id, api_version="1"
        )

        return self._client.execute(request, ItemGetResponse)

    # ==================== 销售属性规则 ====================

    def get_saleprop_rule(
        self,
        access_token: str,
        category_id: int,
        spu_id: Optional[int] = None,
        item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemSalePropRuleResponse:
        """获取销售属性规则（同步）

        OpenAPI: `open.item.saleprop.rule` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSalepropRuleRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSalepropRuleRequest.java)

        Args:
            access_token: 访问令牌
            category_id: 类目ID
            spu_id: SPU ID（可选）
            item_id: 商品ID（可选）
            uid: 用户ID（可选）

        Returns:
            ItemSalePropRuleResponse: 规则配置

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemSalePropRuleRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            spu_id=spu_id,
            item_id=item_id,
            api_version="1",
        )

        return self._client.execute(request, ItemSalePropRuleResponse)

    # create/update removed; please use new/edit
    # update removed; use edit()

    def update_stock(
        self,
        access_token: str,
        item_id: int,
        sku_id: int,
        stock: int,
        change_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemUpdateStockResponse:
        """更新商品SKU库存（同步）

        OpenAPI: `open.item.sku.stock.update` (POST)
        Java: OpenItemSkuStockUpdateRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSkuStockUpdateRequest.java`
        """
        request = ItemUpdateStockRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            sku_id=sku_id,
            stock=stock,
            change_type=change_type,
            api_version="1",
        )

        return self._client.execute(request, ItemUpdateStockResponse)

    # Compatibility aliases for common method names expected by tests/tools
    def create(self, *args, **kwargs):  # pragma: no cover - simple alias
        return self.new(*args, **kwargs)

    def update(self, *args, **kwargs):  # pragma: no cover - simple alias
        return self.edit(*args, **kwargs)

    def delete(
        self, access_token: str, item_id: int, uid: Optional[int] = None
    ) -> ItemDeleteResponse:
        """删除商品（同步）

        OpenAPI: `open.item.delete` (POST)
        Java: OpenItemDeleteRequest
        Path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDeleteRequest.java`
        """
        request = ItemDeleteRequest(
            access_token=access_token, uid=uid, kwai_item_id=item_id, api_version="1"
        )
        return self._client.execute(request, ItemDeleteResponse)

    # ==================== 媒体管理 API ====================

    def upload_image(
        self,
        access_token: str,
        upload_type: int,
        img_url: Optional[str] = None,
        img_bytes: Optional[bytes] = None,
        uid: Optional[int] = None,
    ) -> ItemImageUploadResponse:
        """商品图片上传（同步）

        OpenAPI: `open.item.image.upload` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemImageUploadRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemImageUploadRequest.java)

        Args:
            access_token: 访问令牌
            upload_type: 上传类型（1: URL, 2: 文件）
            img_url: 图片URL（URL上传时使用）
            img_bytes: 图片字节数据（文件上传时使用）
            uid: 用户ID（可选）

        Returns:
            ItemImageUploadResponse: 图片上传结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemImageUploadRequest(
            access_token=access_token,
            uid=uid,
            img_url=img_url,
            upload_type=upload_type,
            img_bytes=img_bytes,
            api_version="1",
        )

        return self._client.execute(request, ItemImageUploadResponse)

    def issue_upload_token(
        self,
        access_token: str,
        material_upload_type: int,
        file_name: str,
        file_length: int,
        uid: Optional[int] = None,
    ) -> ItemMaterialUploadTokenIssueResponse:
        """素材上传 token 签发（同步）

        OpenAPI: `open.item.material.upload.token.issue` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMaterialUploadTokenIssueRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMaterialUploadTokenIssueRequest.java)

        Args:
            access_token: 访问令牌
            material_upload_type: 素材上传类型
            file_name: 文件名
            file_length: 文件长度
            uid: 用户ID（可选）

        Returns:
            ItemMaterialUploadTokenIssueResponse: 签发结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemMaterialUploadTokenIssueRequest(
            access_token=access_token,
            uid=uid,
            material_upload_type=material_upload_type,
            file_name=file_name,
            file_length=file_length,
            api_version="1",
        )

        return self._client.execute(request, ItemMaterialUploadTokenIssueResponse)

    def get_video_list(
        self,
        access_token: str,
        video_type: Optional[int] = None,
        aspect_ratio: Optional[int] = None,
        audit_status: Optional[int] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        page_index: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoListResponse:
        """获取视频列表（同步）

        OpenAPI: `open.item.video.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoListRequest.java)

        Args:
            access_token: 访问令牌
            video_type: 视频类型（可选）
            aspect_ratio: 视频宽高比（可选）
            audit_status: 审核状态（可选）
            create_time_start: 创建开始时间（毫秒，可选）
            create_time_end: 创建结束时间（毫秒，可选）
            page_index: 页码（可选）
            page_size: 页面大小（可选）
            uid: 用户ID（可选）

        Returns:
            ItemVideoListResponse: 视频分页列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemVideoListRequest(
            access_token=access_token,
            uid=uid,
            video_type=video_type,
            aspect_ratio=aspect_ratio,
            audit_status=audit_status,
            create_time_start=create_time_start,
            create_time_end=create_time_end,
            page_index=page_index,
            page_size=page_size,
            api_version="1",
        )

        return self._client.execute(request, ItemVideoListResponse)

    def delete_video(
        self,
        access_token: str,
        video_ids: List[str],
        video_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoDeleteResponse:
        """删除视频（同步）

        OpenAPI: `open.item.video.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoDeleteRequest.java)

        Args:
            access_token: 访问令牌
            video_ids: 视频ID列表
            video_type: 视频类型（可选）
            uid: 用户ID（可选）

        Returns:
            ItemVideoDeleteResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemVideoDeleteRequest(
            access_token=access_token,
            uid=uid,
            video_id=video_ids,
            video_type=video_type,
            api_version="1",
        )

        return self._client.execute(request, ItemVideoDeleteResponse)

    # ==================== 高级操作 API ====================

    def edit_autopass(
        self,
        access_token: str,
        item_id: int,
        purchase_limit: Optional[bool] = None,
        limit_count: Optional[int] = None,
        item_remark: Optional[str] = None,
        sku_list: Optional[List[OpenApiAutoPassSkuDTO]] = None,
        service_rule: Optional[ServiceRule] = None,
        express_template_id: Optional[int] = None,
        sale_time_flag: Optional[bool] = None,
        time_of_sale: Optional[int] = None,
        pay_way: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemAutopassEditResponse:
        """商品自动通过编辑（同步）

        OpenAPI: `open.item.autopass.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemAutopassEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemAutopassEditRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            purchase_limit: 购买限制（可选）
            limit_count: 限制数量（可选）
            item_remark: 商品备注（可选）
            sku_list: SKU 列表（可选）
            service_rule: 服务规则（可选）
            express_template_id: 运费模板ID（可选）
            sale_time_flag: 定时上架标记（可选）
            time_of_sale: 上架时间戳（可选）
            pay_way: 支付方式（可选）
            uid: 用户ID（可选）

        Returns:
            ItemAutopassEditResponse: 编辑结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemAutopassEditRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            purchase_limit=purchase_limit,
            limit_count=limit_count,
            item_remark=item_remark,
            sku_list=sku_list,
            service_rule=service_rule,
            express_template_id=express_template_id,
            sale_time_flag=sale_time_flag,
            time_of_sale=time_of_sale,
            pay_way=pay_way,
            api_version="1",
        )

        return self._client.execute(request, ItemAutopassEditResponse)

    def update_detail_images(
        self,
        access_token: str,
        kwai_item_id: int,
        detail_image_urls: List[str],
        uid: Optional[int] = None,
    ) -> ItemDetailImagesUpdateResponse:
        """更新商品详情图片（同步）

        OpenAPI: `open.item.detail.images.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDetailImagesUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDetailImagesUpdateRequest.java)

        Args:
            access_token: 访问令牌
            kwai_item_id: 快手商品ID
            detail_image_urls: 详情图片URL列表
            uid: 用户ID（可选）

        Returns:
            ItemDetailImagesUpdateResponse: 更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemDetailImagesUpdateRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            detail_image_urls=detail_image_urls,
            api_version="1",
        )

        return self._client.execute(request, ItemDetailImagesUpdateResponse)

    def get_detail_page_link(
        self,
        access_token: str,
        item_id: int,
        type: int,
        item_product_client_info: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> ItemDetailPageLinkResponse:
        """获取商品详情页链接（同步）

        OpenAPI: `open.item.detail.page.link` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDetailPageLinkRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDetailPageLinkRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            type: 链接类型
            item_product_client_info: 客户端信息（可选）
            uid: 用户ID（可选）

        Returns:
            ItemDetailPageLinkResponse: 详情链接

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemDetailPageLinkRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            type=type,
            item_product_client_info=item_product_client_info,
            api_version="1",
        )

        return self._client.execute(request, ItemDetailPageLinkResponse)

    def get_diagnosis(
        self,
        access_token: str,
        item_id: int,
        uid: Optional[int] = None,
    ) -> ItemDiagnosisGetResponse:
        """获取商品诊断信息（同步）

        OpenAPI: `open.item.diagnosis.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDiagnosisGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDiagnosisGetRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            uid: 用户ID（可选）

        Returns:
            ItemDiagnosisGetResponse: 诊断详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemDiagnosisGetRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )

        return self._client.execute(request, ItemDiagnosisGetResponse)

    def apply_main_pic_video(
        self,
        access_token: str,
        item_id: int,
        video_id: str,
        video_type: int,
        uid: Optional[int] = None,
    ) -> ItemMainPicVideoApplyResponse:
        """申请商品主图视频（同步）

        OpenAPI: `open.item.main.pic.video.apply` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMainPicVideoApplyRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMainPicVideoApplyRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            video_id: 视频ID
            video_type: 视频类型
            uid: 用户ID（可选）

        Returns:
            ItemMainPicVideoApplyResponse: 申请结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemMainPicVideoApplyRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            video_id=video_id,
            video_type=video_type,
            api_version="1",
        )

        return self._client.execute(request, ItemMainPicVideoApplyResponse)

    def delete_main_pic_video(
        self,
        access_token: str,
        item_id: int,
        uid: Optional[int] = None,
    ) -> ItemMainPicVideoDeleteResponse:
        """删除商品主图视频（同步）

        OpenAPI: `open.item.main.pic.video.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMainPicVideoDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMainPicVideoDeleteRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            uid: 用户ID（可选）

        Returns:
            ItemMainPicVideoDeleteResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemMainPicVideoDeleteRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )

        return self._client.execute(request, ItemMainPicVideoDeleteResponse)

    def update_shelf_status(
        self,
        access_token: str,
        kwai_item_id: int,
        shelf_status: int,
        uid: Optional[int] = None,
    ) -> ItemShelfStatusUpdateResponse:
        """更新商品上下架状态（同步）

        OpenAPI: `open.item.shelf.status.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemShelfStatusUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemShelfStatusUpdateRequest.java)

        Args:
            access_token: 访问令牌
            kwai_item_id: 快手商品ID
            shelf_status: 上下架状态
            uid: 用户ID（可选）

        Returns:
            ItemShelfStatusUpdateResponse: 更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemShelfStatusUpdateRequest(
            access_token=access_token,
            uid=uid,
            kwai_item_id=kwai_item_id,
            shelf_status=shelf_status,
            api_version="1",
        )

        return self._client.execute(request, ItemShelfStatusUpdateResponse)

    def precheck_new_item(
        self,
        access_token: str,
        leaf_category_id: int,
        uid: Optional[int] = None,
    ) -> ItemNewPrecheckResponse:
        """新建商品预检（同步）

        OpenAPI: `open.item.new.precheck` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemNewPrecheckRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemNewPrecheckRequest.java)

        Args:
            access_token: 访问令牌
            leaf_category_id: 叶子类目ID
            uid: 用户ID（可选）

        Returns:
            ItemNewPrecheckResponse: 预检结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemNewPrecheckRequest(
            access_token=access_token,
            uid=uid,
            leaf_category_id=leaf_category_id,
            api_version="1",
        )

        return self._client.execute(request, ItemNewPrecheckResponse)

    def new(
        self,
        access_token: str,
        title: Optional[str] = None,
        rel_item_id: Optional[int] = None,
        category_id: Optional[int] = None,
        image_urls: Optional[List[str]] = None,
        sku_list: Optional[List[OpenApiAddSkuDTO]] = None,
        purchase_limit: Optional[bool] = None,
        limit_count: Optional[int] = None,
        item_prop_values: Optional[List[AddItemPropValue]] = None,
        details: Optional[str] = None,
        detail_image_urls: Optional[List[str]] = None,
        stock_partner: Optional[bool] = None,
        item_remark: Optional[str] = None,
        service_rule: Optional[ServiceRule] = None,
        express_template_id: Optional[int] = None,
        sale_time_flag: Optional[bool] = None,
        time_of_sale: Optional[int] = None,
        pay_way: Optional[int] = None,
        multiple_stock: Optional[bool] = None,
        poi_ids: Optional[List[int]] = None,
        white_base_image_url: Optional[str] = None,
        transparent_image_url: Optional[str] = None,
        short_title: Optional[str] = None,
        selling_point: Optional[str] = None,
        instructions: Optional[str] = None,
        save_shelf_item_qualification_data: Optional[List[QualificationDataDTO]] = None,
        off_shore_mode: Optional[int] = None,
        spu_id: Optional[int] = None,
        item_video_id: Optional[str] = None,
        three_quarters_image_urls: Optional[List[str]] = None,
        item_video: Optional[ItemVideoProto] = None,
        size_chart_template_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemNewResponse:
        """新建商品（同步）

        OpenAPI: `open.item.new` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemNewRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemNewRequest.java)

        Args:
            access_token: 访问令牌
            title: 商品标题（可选）
            rel_item_id: 关联商品ID（可选）
            category_id: 分类ID（可选）
            image_urls: 图片URL列表（可选）
            sku_list: SKU 列表（可选）
            purchase_limit: 购买限制（可选）
            limit_count: 限制数量（可选）
            item_prop_values: 属性列表（可选）
            details: 详情描述（可选）
            detail_image_urls: 详情图片（可选）
            stock_partner: 库存合作（可选）
            item_remark: 备注（可选）
            service_rule: 服务规则（可选）
            express_template_id: 运费模板ID（可选）
            sale_time_flag: 定时上架标记（可选）
            time_of_sale: 上架时间戳（可选）
            pay_way: 支付方式（可选）
            multiple_stock: 多库存开关（可选）
            poi_ids: 门店ID列表（可选）
            white_base_image_url: 白底图（可选）
            transparent_image_url: 透明图（可选）
            short_title: 短标题（可选）
            selling_point: 卖点（可选）
            instructions: 使用说明（可选）
            save_shelf_item_qualification_data: 资质数据（可选）
            off_shore_mode: 跨境模式（可选）
            spu_id: SPU ID（可选）
            item_video_id: 视频ID（可选）
            three_quarters_image_urls: 3/4图（可选）
            item_video: 视频对象（可选）
            size_chart_template_id: 尺码表模板ID（可选）
            uid: 用户ID（可选）

        Returns:
            ItemNewResponse: 新建结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemNewRequest(
            access_token=access_token,
            uid=uid,
            title=title,
            rel_item_id=rel_item_id,
            category_id=category_id,
            image_urls=image_urls,
            sku_list=sku_list,
            purchase_limit=purchase_limit,
            limit_count=limit_count,
            item_prop_values=item_prop_values,
            details=details,
            detail_image_urls=detail_image_urls,
            stock_partner=stock_partner,
            item_remark=item_remark,
            service_rule=service_rule,
            express_template_id=express_template_id,
            sale_time_flag=sale_time_flag,
            time_of_sale=time_of_sale,
            pay_way=pay_way,
            multiple_stock=multiple_stock,
            poi_ids=poi_ids,
            white_base_image_url=white_base_image_url,
            transparent_image_url=transparent_image_url,
            short_title=short_title,
            selling_point=selling_point,
            instructions=instructions,
            save_shelf_item_qualification_data=save_shelf_item_qualification_data,
            off_shore_mode=off_shore_mode,
            spu_id=spu_id,
            item_video_id=item_video_id,
            three_quarters_image_urls=three_quarters_image_urls,
            item_video=item_video,
            size_chart_template_id=size_chart_template_id,
            api_version="1",
        )

        return self._client.execute(request, ItemNewResponse)

    def edit(
        self,
        access_token: str,
        item_id: int,
        title: Optional[str] = None,
        category_id: Optional[int] = None,
        image_urls: Optional[List[str]] = None,
        sku_list: Optional[List[OpenApiUpdateSkuDTO]] = None,
        item_video_id: Optional[str] = None,
        purchase_limit: Optional[bool] = None,
        limit_count: Optional[int] = None,
        item_prop_values: Optional[List[ItemPropValue]] = None,
        details: Optional[str] = None,
        detail_image_urls: Optional[List[str]] = None,
        update_detail_image_urls: Optional[bool] = None,
        item_remark: Optional[str] = None,
        service_rule: Optional[ServiceRule] = None,
        express_template_id: Optional[int] = None,
        sale_time_flag: Optional[bool] = None,
        time_of_sale: Optional[int] = None,
        pay_way: Optional[int] = None,
        update_item_prop_values: Optional[bool] = None,
        poi_ids: Optional[List[int]] = None,
        white_base_image_url: Optional[str] = None,
        transparent_image_url: Optional[str] = None,
        short_title: Optional[str] = None,
        selling_point: Optional[str] = None,
        instructions: Optional[str] = None,
        save_shelf_item_qualification_data: Optional[List[QualificationDataDTO]] = None,
        update_item_qualification: Optional[bool] = None,
        spu_id: Optional[int] = None,
        update_three_quarters_image_urls: Optional[bool] = None,
        three_quarters_image_urls: Optional[List[str]] = None,
        item_video: Optional[ItemVideoProto] = None,
        size_chart_template_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemEditResponse:
        """编辑商品（同步）

        OpenAPI: `open.item.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemEditRequest.java)

        Args:
            access_token: 访问令牌
            item_id: 商品ID
            title: 商品标题（可选）
            category_id: 分类ID（可选）
            image_urls: 图片URL列表（可选）
            sku_list: SKU 列表（可选）
            item_video_id: 视频ID（可选）
            purchase_limit: 购买限制（可选）
            limit_count: 限制数量（可选）
            item_prop_values: 属性列表（可选）
            details: 详情描述（可选）
            detail_image_urls: 详情图片（可选）
            update_detail_image_urls: 是否更新详情图（可选）
            item_remark: 备注（可选）
            service_rule: 服务规则（可选）
            express_template_id: 运费模板ID（可选）
            sale_time_flag: 定时上架标记（可选）
            time_of_sale: 上架时间戳（可选）
            pay_way: 支付方式（可选）
            update_item_prop_values: 是否更新属性（可选）
            poi_ids: 门店ID列表（可选）
            white_base_image_url: 白底图（可选）
            transparent_image_url: 透明图（可选）
            short_title: 短标题（可选）
            selling_point: 卖点（可选）
            instructions: 使用说明（可选）
            save_shelf_item_qualification_data: 资质数据（可选）
            update_item_qualification: 是否更新资质（可选）
            spu_id: SPU ID（可选）
            update_three_quarters_image_urls: 是否更新3/4图（可选）
            three_quarters_image_urls: 3/4图（可选）
            item_video: 视频对象（可选）
            size_chart_template_id: 尺码表模板ID（可选）
            uid: 用户ID（可选）

        Returns:
            ItemEditResponse: 编辑结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出
        """
        request = ItemEditRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            title=title,
            category_id=category_id,
            image_urls=image_urls,
            sku_list=sku_list,
            item_video_id=item_video_id,
            purchase_limit=purchase_limit,
            limit_count=limit_count,
            item_prop_values=item_prop_values,
            details=details,
            detail_image_urls=detail_image_urls,
            update_detail_image_urls=update_detail_image_urls,
            item_remark=item_remark,
            service_rule=service_rule,
            express_template_id=express_template_id,
            sale_time_flag=sale_time_flag,
            time_of_sale=time_of_sale,
            pay_way=pay_way,
            update_item_prop_values=update_item_prop_values,
            poi_ids=poi_ids,
            white_base_image_url=white_base_image_url,
            transparent_image_url=transparent_image_url,
            short_title=short_title,
            selling_point=selling_point,
            instructions=instructions,
            save_shelf_item_qualification_data=save_shelf_item_qualification_data,
            update_item_qualification=update_item_qualification,
            spu_id=spu_id,
            update_three_quarters_image_urls=update_three_quarters_image_urls,
            three_quarters_image_urls=three_quarters_image_urls,
            item_video=item_video,
            size_chart_template_id=size_chart_template_id,
            api_version="1",
        )

        return self._client.execute(request, ItemEditResponse)

    # ==================== 缺失API方法 - 尺码表管理 ====================

    def get_size_chart_group_list(
        self,
        access_token: str,
        uid: Optional[int] = None,
    ) -> ItemSizeChartGroupListGetResponse:
        """获取尺码表分组列表（同步）

        OpenAPI: `open.item.size.chart.group.list.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartGroupListGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartGroupListGetRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartGroupListGetResponse: 尺码表分组列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartGroupListGetRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartGroupListGetResponse)

    def add_size_chart_template(
        self,
        access_token: str,
        size_chart: AddSizeChartParam,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateAddResponse:
        """添加尺码表模板（同步）

        OpenAPI: `open.item.size.chart.template.add` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartTemplateAddRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateAddRequest.java)

        Args:
            access_token: 访问令牌。
            size_chart: 尺码表模板数据。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateAddResponse: 添加结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateAddRequest(
            access_token=access_token,
            uid=uid,
            size_chart=size_chart,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartTemplateAddResponse)

    def delete_size_chart_template(
        self,
        access_token: str,
        size_chart_id: int,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateDeleteResponse:
        """删除尺码表模板（同步）

        OpenAPI: `open.item.size.chart.template.delete` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartTemplateDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateDeleteRequest.java)

        Args:
            access_token: 访问令牌。
            size_chart_id: 尺码表模板ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateDeleteRequest(
            access_token=access_token,
            uid=uid,
            size_chart_id=size_chart_id,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartTemplateDeleteResponse)

    def edit_size_chart_template(
        self,
        access_token: str,
        size_chart: SizeChartParam,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateEditResponse:
        """编辑尺码表模板（同步）

        OpenAPI: `open.item.size.chart.template.edit` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartTemplateEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateEditRequest.java)

        Args:
            access_token: 访问令牌。
            size_chart: 尺码表模板数据。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateEditResponse: 编辑结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateEditRequest(
            access_token=access_token,
            uid=uid,
            size_chart=size_chart,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartTemplateEditResponse)

    def get_size_chart_template(
        self,
        access_token: str,
        size_chart_id: int,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateGetResponse:
        """获取尺码表模板（同步）

        OpenAPI: `open.item.size.chart.template.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartTemplateGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateGetRequest.java)

        Args:
            access_token: 访问令牌。
            size_chart_id: 尺码表模板ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateGetResponse: 模板详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateGetRequest(
            access_token=access_token,
            uid=uid,
            size_chart_id=size_chart_id,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartTemplateGetResponse)

    def get_size_chart_template_list(
        self,
        access_token: str,
        template_type_prop_value_id: Optional[int] = None,
        page_num: Optional[int] = 1,
        page_size: Optional[int] = 20,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateListGetResponse:
        """获取尺码表模板列表（同步）

        OpenAPI: `open.item.size.chart.template.list.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartTemplateListGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateListGetRequest.java)

        Args:
            access_token: 访问令牌。
            template_type_prop_value_id: 模板类型属性值ID（可选）。
            page_num: 页码（可选，默认 1）。
            page_size: 页面大小（可选，默认 20）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateListGetResponse: 模板分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateListGetRequest(
            access_token=access_token,
            uid=uid,
            template_type_prop_value_id=template_type_prop_value_id,
            page_num=page_num,
            page_size=page_size,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartTemplateListGetResponse)

    def get_size_chart_template_meta(
        self,
        access_token: str,
        category_id: int,
        uid: Optional[int] = None,
    ) -> ItemSizeChartTemplateMetaGetResponse:
        """获取尺码表模板元数据（同步）

        OpenAPI: `open.item.size.chart.template.meta.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemSizeChartTemplateMetaGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemSizeChartTemplateMetaGetRequest.java)

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemSizeChartTemplateMetaGetResponse: 元数据内容。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemSizeChartTemplateMetaGetRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            api_version="1",
        )

        return self._client.execute(request, ItemSizeChartTemplateMetaGetResponse)

    # ==================== 缺失API方法 - 其他功能 ====================

    def get_deleted_items(
        self,
        access_token: str,
        item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemDeletedGetResponse:
        """获取已删除商品（同步）

        OpenAPI: `open.item.deleted.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemDeletedGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemDeletedGetRequest.java)

        Args:
            access_token: 访问令牌。
            item_id: 商品ID（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemDeletedGetResponse: 已删除商品数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemDeletedGetRequest(
            access_token=access_token,
            uid=uid,
            item_id=item_id,
            api_version="1",
        )

        return self._client.execute(request, ItemDeletedGetResponse)

    def get_material_detail(
        self,
        access_token: str,
        material_id: int,
        material_upload_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemMaterialDetailGetResponse:
        """获取素材详情（同步）

        OpenAPI: `open.item.material.detail.get` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMaterialDetailGetRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMaterialDetailGetRequest.java)

        Args:
            access_token: 访问令牌。
            material_id: 素材ID。
            material_upload_type: 素材上传类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemMaterialDetailGetResponse: 素材详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemMaterialDetailGetRequest(
            access_token=access_token,
            uid=uid,
            material_id=material_id,
            material_upload_type=material_upload_type,
            api_version="1",
        )

        return self._client.execute(request, ItemMaterialDetailGetResponse)

    def verify_upload_token(
        self,
        access_token: str,
        token: str,
        material_upload_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemMaterialUploadTokenVerifyResponse:
        """验证上传令牌（同步）

        OpenAPI: `open.item.material.upload.token.verify` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemMaterialUploadTokenVerifyRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemMaterialUploadTokenVerifyRequest.java)

        Args:
            access_token: 访问令牌。
            token: 上传令牌。
            material_upload_type: 素材上传类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemMaterialUploadTokenVerifyResponse: 验证结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemMaterialUploadTokenVerifyRequest(
            access_token=access_token,
            uid=uid,
            token=token,
            material_upload_type=material_upload_type,
            api_version="1",
        )

        return self._client.execute(request, ItemMaterialUploadTokenVerifyResponse)

    def apply_item_standard(
        self,
        access_token: str,
        category_id: int,
        key_prop_list: Optional[List[KeyPropOpenApiDTO]] = None,
        spu_prop_list: Optional[List[SPUPropOpenApiDTO]] = None,
        standard_images: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> ItemStandardApplyResponse:
        """申请商品标准（同步）

        OpenAPI: `open.item.standard.apply` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemStandardApplyRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemStandardApplyRequest.java)

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            key_prop_list: 关键属性列表（可选）。
            spu_prop_list: SPU属性列表（可选）。
            standard_images: 标准图片URL列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemStandardApplyResponse: 申请结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemStandardApplyRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            key_prop_list=key_prop_list,
            spu_prop_list=spu_prop_list,
            standard_images=standard_images,
            api_version="1",
        )

        return self._client.execute(request, ItemStandardApplyResponse)

    def query_standard_apply(
        self,
        access_token: str,
        category_id: Optional[List[int]] = None,
        standard_status: Optional[int] = None,
        standard_name: Optional[str] = None,
        apply_type: Optional[int] = None,
        standard_audit_status: Optional[int] = None,
        limit: Optional[int] = None,
        cursor: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemStandardApplyQueryResponse:
        """查询标准申请状态（同步）

        OpenAPI: `open.item.standard.apply.query` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemStandardApplyQueryRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemStandardApplyQueryRequest.java)

        Args:
            access_token: 访问令牌。
            category_id: 类目ID列表（可选）。
            standard_status: 标准状态（可选）。
            standard_name: 标准名称（可选）。
            apply_type: 申请类型（可选）。
            standard_audit_status: 标准审核状态（可选）。
            limit: 限制数量（可选）。
            cursor: 游标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemStandardApplyQueryResponse: 申请状态数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemStandardApplyQueryRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            standard_status=standard_status,
            standard_name=standard_name,
            apply_type=apply_type,
            standard_audit_status=standard_audit_status,
            limit=limit,
            cursor=cursor,
            api_version="1",
        )

        return self._client.execute(request, ItemStandardApplyQueryResponse)

    def correct_item_standard(
        self,
        access_token: str,
        category_id: int,
        standard_id: int,
        key_prop_list: Optional[List[KeyPropOpenApiDTO]] = None,
        spu_prop_list: Optional[List[SPUPropOpenApiDTO]] = None,
        modify_reason: Optional[str] = None,
        modify_image_url: Optional[str] = None,
        standard_images: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> ItemStandardCorrectResponse:
        """纠正商品标准（同步）

        OpenAPI: `open.item.standard.correct` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemStandardCorrectRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemStandardCorrectRequest.java)

        Args:
            access_token: 访问令牌。
            category_id: 类目ID。
            standard_id: 标准ID。
            key_prop_list: 关键属性列表（可选）。
            spu_prop_list: SPU属性列表（可选）。
            modify_reason: 修改原因（可选）。
            modify_image_url: 修改图片URL（可选）。
            standard_images: 标准图片URL列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemStandardCorrectResponse: 提交纠正结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemStandardCorrectRequest(
            access_token=access_token,
            uid=uid,
            category_id=category_id,
            standard_id=standard_id,
            key_prop_list=key_prop_list,
            spu_prop_list=spu_prop_list,
            modify_reason=modify_reason,
            modify_image_url=modify_image_url,
            standard_images=standard_images,
            api_version="1",
        )

        return self._client.execute(request, ItemStandardCorrectResponse)

    def edit_video_caption(
        self,
        access_token: str,
        video_id: str,
        caption: str,
        video_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoCaptionEditResponse:
        """编辑视频字幕（同步）

        OpenAPI: `open.item.video.caption.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoCaptionEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoCaptionEditRequest.java)

        Args:
            access_token: 访问令牌。
            video_id: 视频ID。
            caption: 字幕内容。
            video_type: 视频类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemVideoCaptionEditResponse: 编辑提交结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemVideoCaptionEditRequest(
            access_token=access_token,
            uid=uid,
            video_id=video_id,
            caption=caption,
            video_type=video_type,
            api_version="1",
        )

        return self._client.execute(request, ItemVideoCaptionEditResponse)

    def get_video_count(
        self,
        access_token: str,
        video_type: Optional[int] = None,
        aspect_ratio: Optional[int] = None,
        audit_status: Optional[int] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoCountResponse:
        """获取视频数量（同步）

        OpenAPI: `open.item.video.count` (POST)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoCountRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoCountRequest.java)

        Args:
            access_token: 访问令牌。
            video_type: 视频类型（可选）。
            aspect_ratio: 视频宽高比（可选）。
            audit_status: 审核状态（可选）。
            create_time_start: 创建开始时间（毫秒，可选）。
            create_time_end: 创建结束时间（毫秒，可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemVideoCountResponse: 数量聚合结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemVideoCountRequest(
            access_token=access_token,
            uid=uid,
            video_type=video_type,
            aspect_ratio=aspect_ratio,
            audit_status=audit_status,
            create_time_start=create_time_start,
            create_time_end=create_time_end,
            api_version="1",
        )

        return self._client.execute(request, ItemVideoCountResponse)

    def get_video_info(
        self,
        access_token: str,
        video_id: str,
        video_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ItemVideoInfoResponse:
        """获取视频信息（同步）

        OpenAPI: `open.item.video.info` (GET)
        Java: `com.kuaishou.merchant.open.api.request.item.OpenItemVideoInfoRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/item/OpenItemVideoInfoRequest.java)

        Args:
            access_token: 访问令牌。
            video_id: 视频ID。
            video_type: 视频类型（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            ItemVideoInfoResponse: 视频详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = ItemVideoInfoRequest(
            access_token=access_token,
            uid=uid,
            video_id=video_id,
            video_type=video_type,
            api_version="1",
        )

        return self._client.execute(request, ItemVideoInfoResponse)
