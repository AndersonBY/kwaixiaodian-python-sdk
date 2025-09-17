"""供应链服务
基于 Java 参考实现，提供供应链商品同步功能。

文档规范
- OpenAPI: 展示方法名与 HTTP 动词（来自模型 `api_method`/`http_method`）
- Java: 对应 Java Request 类与源码路径（用于交叉校验）
- Raises: `KwaixiaodianAPIError`、`KwaixiaodianValidationError`
"""

from typing import Any, Dict, List, Optional

from ...models.supply import (
    SupplyItem,
    SupplyItemPerformance,
    SupplyItemProp,
    SupplyItemServiceRule,
    SupplyItemSyncParam,
    SupplyItemSyncRequest,
    SupplyItemSyncResponse,
    SupplyPerformance1688,
    SupplyRight,
    SupplySeller,
    SupplySku,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncSupplyService:
    """异步供应链服务

    提供供应链功能：
    - 商品同步
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化供应链服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 商品同步相关 ====================

    async def sync_supply_item(
        self,
        access_token: str,
        *,
        seller: Optional[SupplySeller] = None,
        skus: Optional[List[SupplySku]] = None,
        description: Optional[str] = None,
        title: Optional[str] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        scene: Optional[int] = None,
        white_base_image_url: Optional[str] = None,
        category_id: Optional[int] = None,
        rights: Optional[List[SupplyRight]] = None,
        is_fuli: Optional[bool] = None,
        is_fuchi: Optional[bool] = None,
        upload_method: Optional[int] = None,
        images: Optional[List[str]] = None,
        rights_v2: Optional[List[int]] = None,
        item_id: Optional[str] = None,
        image_url: Optional[str] = None,
        origin_item_url: Optional[str] = None,
        props: Optional[List[SupplyItemProp]] = None,
        detail_images: Optional[List[str]] = None,
        service_rule: Optional[SupplyItemServiceRule] = None,
        performance: Optional[SupplyItemPerformance] = None,
        extra_info: Optional[Dict[str, Any]] = None,
        three_quarters_image_urls: Optional[List[str]] = None,
        service_desc: Optional[List[str]] = None,
        performance_1688: Optional[SupplyPerformance1688] = None,
        service_types: Optional[List[int]] = None,
        kwai_item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SupplyItemSyncResponse:
        """同步供应商品。

        OpenAPI: `open.supply.item.sync` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.supply.OpenSupplyItemSyncRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/supply/OpenSupplyItemSyncRequest.java`)

        Args:
            access_token: 访问令牌
            seller: 供应商信息，使用 `SupplySeller`
            skus: SKU 列表，使用 `SupplySku`
            description: 商品描述
            title: 商品标题
            price_min: 最低价（分）
            price_max: 最高价（分）
            scene: 场景类型
            white_base_image_url: 白底图 URL
            category_id: 类目ID
            rights: 商品权益列表，使用 `SupplyRight`
            is_fuli: 是否福利商品
            is_fuchi: 是否福吃商品
            upload_method: 上传方式
            images: 主图列表
            rights_v2: 权益V2列表
            item_id: 商品ID
            image_url: 主图 URL
            origin_item_url: 原商品链接
            props: 商品属性列表，使用 `SupplyItemProp`
            detail_images: 详情图列表
            service_rule: 服务规则，使用 `SupplyItemServiceRule`
            performance: 履约表现，使用 `SupplyItemPerformance`
            extra_info: 额外信息字典
            three_quarters_image_urls: 三分之四视角图列表
            service_desc: 服务描述列表
            performance_1688: 1688 表现信息，使用 `SupplyPerformance1688`
            service_types: 服务类型列表
            kwai_item_id: 快手商品ID
            uid: 用户ID（可选）

        Returns:
            SupplyItemSyncResponse: 商品同步结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        item_model = SupplyItem(
            seller=seller,
            skus=skus,
            description=description,
            title=title,
            price_min=price_min,
            price_max=price_max,
            scene=scene,
            white_base_image_url=white_base_image_url,
            category_id=category_id,
            rights=rights,
            is_fuli=is_fuli,
            is_fuchi=is_fuchi,
            upload_method=upload_method,
            images=images,
            rights_v2=rights_v2,
            item_id=item_id,
            image_url=image_url,
            origin_item_url=origin_item_url,
            props=props,
            detail_images=detail_images,
            service_rule=service_rule,
            performance=performance,
            extra_info=extra_info,
            three_quarters_image_urls=three_quarters_image_urls,
            service_desc=service_desc,
            performance1688=performance_1688,
            service_types=service_types,
            kwai_item_id=kwai_item_id,
        )
        req = SupplyItemSyncRequest(
            access_token=access_token,
            uid=uid,
            param=SupplyItemSyncParam(item=item_model),
            api_version="1",
        )
        return await self._client.execute(req, SupplyItemSyncResponse)


class SyncSupplyService:
    """同步供应链服务

    提供供应链功能的同步版本。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化同步供应链服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 商品同步相关 ====================

    def sync_supply_item(
        self,
        access_token: str,
        *,
        seller: Optional[SupplySeller] = None,
        skus: Optional[List[SupplySku]] = None,
        description: Optional[str] = None,
        title: Optional[str] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        scene: Optional[int] = None,
        white_base_image_url: Optional[str] = None,
        category_id: Optional[int] = None,
        rights: Optional[List[SupplyRight]] = None,
        is_fuli: Optional[bool] = None,
        is_fuchi: Optional[bool] = None,
        upload_method: Optional[int] = None,
        images: Optional[List[str]] = None,
        rights_v2: Optional[List[int]] = None,
        item_id: Optional[str] = None,
        image_url: Optional[str] = None,
        origin_item_url: Optional[str] = None,
        props: Optional[List[SupplyItemProp]] = None,
        detail_images: Optional[List[str]] = None,
        service_rule: Optional[SupplyItemServiceRule] = None,
        performance: Optional[SupplyItemPerformance] = None,
        extra_info: Optional[Dict[str, Any]] = None,
        three_quarters_image_urls: Optional[List[str]] = None,
        service_desc: Optional[List[str]] = None,
        performance_1688: Optional[SupplyPerformance1688] = None,
        service_types: Optional[List[int]] = None,
        kwai_item_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SupplyItemSyncResponse:
        """同步供应商品。

        OpenAPI: `open.supply.item.sync` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.supply.OpenSupplyItemSyncRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/supply/OpenSupplyItemSyncRequest.java`)

        Args:
            access_token: 访问令牌
            seller: 供应商信息，使用 `SupplySeller`
            skus: SKU 列表，使用 `SupplySku`
            description: 商品描述
            title: 商品标题
            price_min: 最低价（分）
            price_max: 最高价（分）
            scene: 场景类型
            white_base_image_url: 白底图 URL
            category_id: 类目ID
            rights: 商品权益列表，使用 `SupplyRight`
            is_fuli: 是否福利商品
            is_fuchi: 是否福吃商品
            upload_method: 上传方式
            images: 主图列表
            rights_v2: 权益V2列表
            item_id: 商品ID
            image_url: 主图 URL
            origin_item_url: 原商品链接
            props: 商品属性列表，使用 `SupplyItemProp`
            detail_images: 详情图列表
            service_rule: 服务规则，使用 `SupplyItemServiceRule`
            performance: 履约表现，使用 `SupplyItemPerformance`
            extra_info: 额外信息字典
            three_quarters_image_urls: 三分之四视角图列表
            service_desc: 服务描述列表
            performance_1688: 1688 表现信息，使用 `SupplyPerformance1688`
            service_types: 服务类型列表
            kwai_item_id: 快手商品ID
            uid: 用户ID（可选）

        Returns:
            SupplyItemSyncResponse: 商品同步结果

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        item_model = SupplyItem(
            seller=seller,
            skus=skus,
            description=description,
            title=title,
            price_min=price_min,
            price_max=price_max,
            scene=scene,
            white_base_image_url=white_base_image_url,
            category_id=category_id,
            rights=rights,
            is_fuli=is_fuli,
            is_fuchi=is_fuchi,
            upload_method=upload_method,
            images=images,
            rights_v2=rights_v2,
            item_id=item_id,
            image_url=image_url,
            origin_item_url=origin_item_url,
            props=props,
            detail_images=detail_images,
            service_rule=service_rule,
            performance=performance,
            extra_info=extra_info,
            three_quarters_image_urls=three_quarters_image_urls,
            service_desc=service_desc,
            performance1688=performance_1688,
            service_types=service_types,
            kwai_item_id=kwai_item_id,
        )
        req = SupplyItemSyncRequest(
            access_token=access_token,
            uid=uid,
            param=SupplyItemSyncParam(item=item_model),
            api_version="1",
        )
        return self._client.execute(req, SupplyItemSyncResponse)
