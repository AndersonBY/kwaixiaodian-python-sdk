"""SCM 供应链管理服务（对齐 Java SDK 与开放平台）。

- OpenAPI 范围：`open.scm.*`
- Java 对应包：`com.kuaishou.merchant.open.api.request.scm`
- 平台规范参考：`docs/开发指南和规则协议/` 与 `docs/开发者支持文档/`
"""

from typing import Any, Dict, Optional

from ...models.scm import (
    InventoryAdjustParam,
    InventoryAdjustRequest,
    InventoryAdjustResponse,
    InventoryDetailParam,
    InventoryDetailRequest,
    InventoryDetailResponse,
    InventoryUpdateParam,
    InventoryUpdateRequest,
    InventoryUpdateResponse,
    WareAddParam,
    WareAddRequest,
    WareAddResponse,
    WarehouseAddParam,
    WarehouseAddRequest,
    WarehouseAddResponse,
    WarehouseInfoParam,
    WarehouseInfoRequest,
    WarehouseInfoResponse,
    WarehousePackageWeightExpressParam,
    WarehousePackageWeightExpressRequest,
    WarehousePackageWeightExpressResponse,
    WarehouseQueryParam,
    WarehouseQueryRequest,
    WarehouseQueryResponse,
    WarehouseSalescopeTemplateInfoParam,
    WarehouseSalescopeTemplateInfoRequest,
    WarehouseSalescopeTemplateInfoResponse,
    WarehouseSalescopeTemplateOperationParam,
    WarehouseSalescopeTemplateOperationRequest,
    WarehouseSalescopeTemplateOperationResponse,
    WarehouseUpdateParam,
    WarehouseUpdateRequest,
    WarehouseUpdateResponse,
    WareInfoParam,
    WareInfoRequest,
    WareInfoResponse,
    WareListParam,
    WareListRequest,
    WareListResponse,
    WareUpdateParam,
    WareUpdateRequest,
    WareUpdateResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncScmService:
    """异步SCM供应链管理服务

    提供库存管理、商品管理、仓库管理等功能：
    - 库存调整、详情查询、更新
    - 商品添加、信息查询、列表查询、更新
    - 仓库添加、信息查询、列表查询、更新
    - 仓库包裹重量快递查询
    - 仓库销售范围模板操作
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化SCM服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 库存管理相关 ====================
    async def inventory_adjust(
        self,
        access_token: str,
        ware_out_code: str,
        idempotent_id: str,
        warehouse_out_code: str,
        operation_type: str,
        adjust_quantity: int,
    ) -> InventoryAdjustResponse:
        """库存调整

        OpenAPI: open.scm.inventory.adjust (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmInventoryAdjustRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmInventoryAdjustRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码
            idempotent_id: 幂等ID
            warehouse_out_code: 仓库外部编码
            operation_type: 操作类型（如 INCREASE/DECREASE）
            adjust_quantity: 调整数量

        Returns:
            InventoryAdjustResponse: 库存调整结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = InventoryAdjustRequest(
            access_token=access_token,
            param=InventoryAdjustParam(
                ware_out_code=ware_out_code,
                idempotent_id=idempotent_id,
                warehouse_out_code=warehouse_out_code,
                operation_type=operation_type,
                adjust_quantity=adjust_quantity,
            ),
            api_version="1",
        )
        return await self._client.execute(request, InventoryAdjustResponse)

    async def inventory_detail(
        self,
        access_token: str,
        ware_out_code: str,
    ) -> InventoryDetailResponse:
        """库存详情查询

        OpenAPI: open.scm.inventory.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmInventoryDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmInventoryDetailRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码

        Returns:
            InventoryDetailResponse: 库存详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = InventoryDetailRequest(
            access_token=access_token,
            param=InventoryDetailParam(ware_out_code=ware_out_code),
            api_version="1",
        )
        return await self._client.execute(request, InventoryDetailResponse)

    async def inventory_update(
        self,
        access_token: str,
        ware_out_code: str,
        quantity: int,
        warehouse_out_code: str,
    ) -> InventoryUpdateResponse:
        """库存更新

        OpenAPI: open.scm.inventory.update (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmInventoryUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmInventoryUpdateRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码
            quantity: 更新后的库存数量
            warehouse_out_code: 仓库外部编码

        Returns:
            InventoryUpdateResponse: 库存更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = InventoryUpdateRequest(
            access_token=access_token,
            param=InventoryUpdateParam(
                ware_out_code=ware_out_code,
                quantity=quantity,
                warehouse_out_code=warehouse_out_code,
            ),
            api_version="1",
        )
        return await self._client.execute(request, InventoryUpdateResponse)

    # ==================== 商品管理相关 ====================
    async def ware_add(
        self,
        access_token: str,
        ware_name: str,
        ware_out_code: str,
        ware_volume: Optional[int] = None,
        ware_height: Optional[int] = None,
        ware_width: Optional[int] = None,
        owner_source_name: Optional[str] = None,
        ware_length: Optional[int] = None,
        owner_source_type_enum: Optional[str] = None,
        barcode: Optional[str] = None,
        ware_weight: Optional[int] = None,
    ) -> WareAddResponse:
        """商品添加

        OpenAPI: open.scm.ware.add (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareAddRequest.java)

        Args:
            access_token: 访问令牌
            ware_name: 商品名称
            ware_out_code: 商品外部编码
            ware_volume: 商品体积（可选）
            ware_height: 商品高度（可选）
            ware_width: 商品宽度（可选）
            owner_source_name: 货主来源名称（可选）
            ware_length: 商品长度（可选）
            owner_source_type_enum: 货主来源类型（可选）
            barcode: 商品条码（可选）
            ware_weight: 商品重量（克，可选）

        Returns:
            WareAddResponse: 商品添加结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareAddRequest(
            access_token=access_token,
            param=WareAddParam(
                ware_name=ware_name,
                ware_out_code=ware_out_code,
                ware_volume=ware_volume,
                ware_height=ware_height,
                ware_width=ware_width,
                owner_source_name=owner_source_name,
                ware_length=ware_length,
                owner_source_type_enum=owner_source_type_enum,
                barcode=barcode,
                ware_weight=ware_weight,
            ),
            api_version="1",
        )
        return await self._client.execute(request, WareAddResponse)

    async def ware_info(
        self, access_token: str, ware_out_code: str
    ) -> WareInfoResponse:
        """商品信息查询

        OpenAPI: open.scm.ware.info (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareInfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareInfoRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码

        Returns:
            WareInfoResponse: 商品信息详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareInfoRequest(
            access_token=access_token,
            param=WareInfoParam(ware_out_code=ware_out_code),
            api_version="1",
        )
        return await self._client.execute(request, WareInfoResponse)

    async def ware_list(
        self,
        access_token: str,
        page_size: Optional[int] = None,
        page_no: Optional[int] = None,
        warehouse_out_code: Optional[str] = None,
    ) -> WareListResponse:
        """商品列表查询

        OpenAPI: open.scm.ware.list (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareListRequest.java)

        Args:
            access_token: 访问令牌
            page_size: 页面大小（可选）
            page_no: 页码（可选）
            warehouse_out_code: 仓库外部编码（可选）

        Returns:
            WareListResponse: 商品列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareListRequest(
            access_token=access_token,
            param=WareListParam(
                page_size=page_size,
                page_no=page_no,
                warehouse_out_code=warehouse_out_code,
            ),
            api_version="1",
        )
        return await self._client.execute(request, WareListResponse)

    async def ware_update(
        self,
        access_token: str,
        ware_out_code: str,
        ware_volume: Optional[int] = None,
        ware_name: Optional[str] = None,
        ware_height: Optional[int] = None,
        ware_width: Optional[int] = None,
        owner_source_name: Optional[str] = None,
        ware_length: Optional[int] = None,
        owner_source_type_enum: Optional[str] = None,
        barcode: Optional[str] = None,
        ware_weight: Optional[int] = None,
    ) -> WareUpdateResponse:
        """商品更新

        OpenAPI: open.scm.ware.update (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareUpdateRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码
            ware_volume: 商品体积（可选）
            ware_name: 商品名称（可选）
            ware_height: 商品高度（可选）
            ware_width: 商品宽度（可选）
            owner_source_name: 货主来源名称（可选）
            ware_length: 商品长度（可选）
            owner_source_type_enum: 货主来源类型（可选）
            barcode: 商品条码（可选）
            ware_weight: 商品重量（克，可选）

        Returns:
            WareUpdateResponse: 商品更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareUpdateRequest(
            access_token=access_token,
            param=WareUpdateParam(
                ware_out_code=ware_out_code,
                ware_volume=ware_volume,
                ware_name=ware_name,
                ware_height=ware_height,
                ware_width=ware_width,
                owner_source_name=owner_source_name,
                ware_length=ware_length,
                owner_source_type_enum=owner_source_type_enum,
                barcode=barcode,
                ware_weight=ware_weight,
            ),
            api_version="1",
        )
        return await self._client.execute(request, WareUpdateResponse)

    # ==================== 仓库管理相关 ====================
    async def warehouse_add(
        self,
        access_token: str,
        warehouse_name: str,
        warehouse_out_code: str,
        province: str,
        city: str,
        district: str,
        address: str,
        contact_person: Optional[str] = None,
        contact_phone: Optional[str] = None,
    ) -> WarehouseAddResponse:
        """仓库添加

        OpenAPI: open.scm.warehouse.add (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseAddRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_name: 仓库名称
            warehouse_out_code: 仓库外部编码
            province: 省份
            city: 城市
            district: 区县
            address: 详细地址
            contact_person: 联系人姓名（可选）
            contact_phone: 联系人电话（可选）

        Returns:
            WarehouseAddResponse: 仓库添加结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseAddRequest(
            access_token=access_token,
            param=WarehouseAddParam(
                warehouse_name=warehouse_name,
                warehouse_out_code=warehouse_out_code,
                province=province,
                city=city,
                district=district,
                address=address,
                contact_person=contact_person,
                contact_phone=contact_phone,
            ),
            api_version="1",
        )
        return await self._client.execute(request, WarehouseAddResponse)

    async def warehouse_info(
        self, access_token: str, warehouse_out_code: str
    ) -> WarehouseInfoResponse:
        """仓库信息查询

        OpenAPI: open.scm.warehouse.info (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseInfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseInfoRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码

        Returns:
            WarehouseInfoResponse: 仓库详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseInfoRequest(
            access_token=access_token,
            param=WarehouseInfoParam(warehouse_out_code=warehouse_out_code),
            api_version="1",
        )
        return await self._client.execute(request, WarehouseInfoResponse)

    async def warehouse_query(
        self,
        access_token: str,
        page_size: Optional[int] = None,
        page_no: Optional[int] = None,
    ) -> WarehouseQueryResponse:
        """仓库列表查询

        OpenAPI: open.scm.warehouse.query (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseQueryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseQueryRequest.java)

        Args:
            access_token: 访问令牌
            page_size: 页面大小（可选）
            page_no: 页码（可选）

        Returns:
            WarehouseQueryResponse: 仓库列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseQueryRequest(
            access_token=access_token,
            param=WarehouseQueryParam(page_size=page_size, page_no=page_no),
            api_version="1",
        )
        return await self._client.execute(request, WarehouseQueryResponse)

    async def warehouse_update(
        self,
        access_token: str,
        warehouse_out_code: str,
        warehouse_name: Optional[str] = None,
        province: Optional[str] = None,
        city: Optional[str] = None,
        district: Optional[str] = None,
        address: Optional[str] = None,
        contact_person: Optional[str] = None,
        contact_phone: Optional[str] = None,
    ) -> WarehouseUpdateResponse:
        """仓库更新

        OpenAPI: open.scm.warehouse.update (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseUpdateRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码
            warehouse_name: 仓库名称（可选）
            province: 省份（可选）
            city: 城市（可选）
            district: 区县（可选）
            address: 详细地址（可选）
            contact_person: 联系人姓名（可选）
            contact_phone: 联系人电话（可选）

        Returns:
            WarehouseUpdateResponse: 仓库更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseUpdateRequest(
            access_token=access_token,
            param=WarehouseUpdateParam(
                warehouse_out_code=warehouse_out_code,
                warehouse_name=warehouse_name,
                province=province,
                city=city,
                district=district,
                address=address,
                contact_person=contact_person,
                contact_phone=contact_phone,
            ),
            api_version="1",
        )
        return await self._client.execute(request, WarehouseUpdateResponse)

    # ==================== 仓库高级功能 ====================
    async def warehouse_package_weight_express(
        self,
        access_token: str,
        warehouse_out_code: str,
        package_weight: int,
    ) -> WarehousePackageWeightExpressResponse:
        """仓库包裹重量快递查询

        OpenAPI: open.scm.package.weight.express (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmPackageWeightExpressRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmPackageWeightExpressRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码
            package_weight: 包裹重量（克）

        Returns:
            WarehousePackageWeightExpressResponse: 快递费用或推荐信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehousePackageWeightExpressRequest(
            access_token=access_token,
            param=WarehousePackageWeightExpressParam(
                warehouse_out_code=warehouse_out_code, package_weight=package_weight
            ),
            api_version="1",
        )
        return await self._client.execute(
            request, WarehousePackageWeightExpressResponse
        )

    async def warehouse_salescope_template_info(
        self, access_token: str, warehouse_out_code: str
    ) -> WarehouseSalescopeTemplateInfoResponse:
        """仓库销售范围模板信息查询

        OpenAPI: open.scm.warehouse.saleScopeTemplate.info (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseSalescopetemplateInfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseSalescopetemplateInfoRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码

        Returns:
            WarehouseSalescopeTemplateInfoResponse: 销售范围模板信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseSalescopeTemplateInfoRequest(
            access_token=access_token,
            param=WarehouseSalescopeTemplateInfoParam(
                warehouse_out_code=warehouse_out_code
            ),
            api_version="1",
        )
        return await self._client.execute(
            request, WarehouseSalescopeTemplateInfoResponse
        )

    async def warehouse_salescope_template_operation(
        self,
        access_token: str,
        warehouse_out_code: str,
        operation_type: str,
        template_data: Optional[Dict[str, Any]] = None,
    ) -> WarehouseSalescopeTemplateOperationResponse:
        """仓库销售范围模板操作

        OpenAPI: open.scm.warehouse.saleScopeTemplate.operation (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseSalescopetemplateOperationRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseSalescopetemplateOperationRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码
            operation_type: 操作类型（如 CREATE/UPDATE）
            template_data: 模板数据（可选）

        Returns:
            WarehouseSalescopeTemplateOperationResponse: 操作结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseSalescopeTemplateOperationRequest(
            access_token=access_token,
            param=WarehouseSalescopeTemplateOperationParam(
                warehouse_out_code=warehouse_out_code,
                operation_type=operation_type,
                template_data=template_data,
            ),
            api_version="1",
        )
        return await self._client.execute(
            request, WarehouseSalescopeTemplateOperationResponse
        )


class SyncScmService:
    """同步SCM供应链管理服务

    提供库存管理、商品管理、仓库管理等功能的同步版本。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化同步SCM服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 库存管理相关 ====================
    def inventory_adjust(
        self,
        access_token: str,
        ware_out_code: str,
        idempotent_id: str,
        warehouse_out_code: str,
        operation_type: str,
        adjust_quantity: int,
    ) -> InventoryAdjustResponse:
        """库存调整（同步）

        OpenAPI: open.scm.inventory.adjust (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmInventoryAdjustRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmInventoryAdjustRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码
            idempotent_id: 幂等ID
            warehouse_out_code: 仓库外部编码
            operation_type: 操作类型（如 INCREASE/DECREASE）
            adjust_quantity: 调整数量

        Returns:
            InventoryAdjustResponse: 库存调整结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = InventoryAdjustRequest(
            access_token=access_token,
            param=InventoryAdjustParam(
                ware_out_code=ware_out_code,
                idempotent_id=idempotent_id,
                warehouse_out_code=warehouse_out_code,
                operation_type=operation_type,
                adjust_quantity=adjust_quantity,
            ),
            api_version="1",
        )
        return self._client.execute(request, InventoryAdjustResponse)

    def inventory_detail(
        self, access_token: str, ware_out_code: str
    ) -> InventoryDetailResponse:
        """库存详情查询（同步）

        OpenAPI: open.scm.inventory.detail (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmInventoryDetailRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmInventoryDetailRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码

        Returns:
            InventoryDetailResponse: 库存详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = InventoryDetailRequest(
            access_token=access_token,
            param=InventoryDetailParam(ware_out_code=ware_out_code),
            api_version="1",
        )
        return self._client.execute(request, InventoryDetailResponse)

    def inventory_update(
        self,
        access_token: str,
        ware_out_code: str,
        quantity: int,
        warehouse_out_code: str,
    ) -> InventoryUpdateResponse:
        """库存更新（同步）

        OpenAPI: open.scm.inventory.update (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmInventoryUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmInventoryUpdateRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码
            quantity: 更新后的库存数量
            warehouse_out_code: 仓库外部编码

        Returns:
            InventoryUpdateResponse: 库存更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = InventoryUpdateRequest(
            access_token=access_token,
            param=InventoryUpdateParam(
                ware_out_code=ware_out_code,
                quantity=quantity,
                warehouse_out_code=warehouse_out_code,
            ),
            api_version="1",
        )
        return self._client.execute(request, InventoryUpdateResponse)

    # ==================== 商品管理相关 ====================
    def ware_add(
        self,
        access_token: str,
        ware_name: str,
        ware_out_code: str,
        ware_volume: Optional[int] = None,
        ware_height: Optional[int] = None,
        ware_width: Optional[int] = None,
        owner_source_name: Optional[str] = None,
        ware_length: Optional[int] = None,
        owner_source_type_enum: Optional[str] = None,
        barcode: Optional[str] = None,
        ware_weight: Optional[int] = None,
    ) -> WareAddResponse:
        """商品添加（同步）

        OpenAPI: open.scm.ware.add (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareAddRequest.java)

        Args:
            access_token: 访问令牌
            ware_name: 商品名称
            ware_out_code: 商品外部编码
            ware_volume: 商品体积（可选）
            ware_height: 商品高度（可选）
            ware_width: 商品宽度（可选）
            owner_source_name: 货主来源名称（可选）
            ware_length: 商品长度（可选）
            owner_source_type_enum: 货主来源类型（可选）
            barcode: 商品条码（可选）
            ware_weight: 商品重量（克，可选）

        Returns:
            WareAddResponse: 商品添加结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareAddRequest(
            access_token=access_token,
            param=WareAddParam(
                ware_name=ware_name,
                ware_out_code=ware_out_code,
                ware_volume=ware_volume,
                ware_height=ware_height,
                ware_width=ware_width,
                owner_source_name=owner_source_name,
                ware_length=ware_length,
                owner_source_type_enum=owner_source_type_enum,
                barcode=barcode,
                ware_weight=ware_weight,
            ),
            api_version="1",
        )
        return self._client.execute(request, WareAddResponse)

    def ware_info(self, access_token: str, ware_out_code: str) -> WareInfoResponse:
        """商品信息查询（同步）

        OpenAPI: open.scm.ware.info (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareInfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareInfoRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码

        Returns:
            WareInfoResponse: 商品信息详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareInfoRequest(
            access_token=access_token,
            param=WareInfoParam(ware_out_code=ware_out_code),
            api_version="1",
        )
        return self._client.execute(request, WareInfoResponse)

    def ware_list(
        self,
        access_token: str,
        page_size: Optional[int] = None,
        page_no: Optional[int] = None,
        warehouse_out_code: Optional[str] = None,
    ) -> WareListResponse:
        """商品列表查询（同步）

        OpenAPI: open.scm.ware.list (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareListRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareListRequest.java)

        Args:
            access_token: 访问令牌
            page_size: 页面大小（可选）
            page_no: 页码（可选）
            warehouse_out_code: 仓库外部编码（可选）

        Returns:
            WareListResponse: 商品列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareListRequest(
            access_token=access_token,
            param=WareListParam(
                page_size=page_size,
                page_no=page_no,
                warehouse_out_code=warehouse_out_code,
            ),
            api_version="1",
        )
        return self._client.execute(request, WareListResponse)

    def ware_update(
        self,
        access_token: str,
        ware_out_code: str,
        ware_volume: Optional[int] = None,
        ware_name: Optional[str] = None,
        ware_height: Optional[int] = None,
        ware_width: Optional[int] = None,
        owner_source_name: Optional[str] = None,
        ware_length: Optional[int] = None,
        owner_source_type_enum: Optional[str] = None,
        barcode: Optional[str] = None,
        ware_weight: Optional[int] = None,
    ) -> WareUpdateResponse:
        """商品更新（同步）

        OpenAPI: open.scm.ware.update (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWareUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWareUpdateRequest.java)

        Args:
            access_token: 访问令牌
            ware_out_code: 商品外部编码
            ware_volume: 商品体积（可选）
            ware_name: 商品名称（可选）
            ware_height: 商品高度（可选）
            ware_width: 商品宽度（可选）
            owner_source_name: 货主来源名称（可选）
            ware_length: 商品长度（可选）
            owner_source_type_enum: 货主来源类型（可选）
            barcode: 商品条码（可选）
            ware_weight: 商品重量（克，可选）

        Returns:
            WareUpdateResponse: 商品更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WareUpdateRequest(
            access_token=access_token,
            param=WareUpdateParam(
                ware_out_code=ware_out_code,
                ware_volume=ware_volume,
                ware_name=ware_name,
                ware_height=ware_height,
                ware_width=ware_width,
                owner_source_name=owner_source_name,
                ware_length=ware_length,
                owner_source_type_enum=owner_source_type_enum,
                barcode=barcode,
                ware_weight=ware_weight,
            ),
            api_version="1",
        )
        return self._client.execute(request, WareUpdateResponse)

    # ==================== 仓库管理相关 ====================
    def warehouse_add(
        self,
        access_token: str,
        warehouse_name: str,
        warehouse_out_code: str,
        province: str,
        city: str,
        district: str,
        address: str,
        contact_person: Optional[str] = None,
        contact_phone: Optional[str] = None,
    ) -> WarehouseAddResponse:
        """仓库添加（同步）

        OpenAPI: open.scm.warehouse.add (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseAddRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseAddRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_name: 仓库名称
            warehouse_out_code: 仓库外部编码
            province: 省份
            city: 城市
            district: 区县
            address: 详细地址
            contact_person: 联系人姓名（可选）
            contact_phone: 联系人电话（可选）

        Returns:
            WarehouseAddResponse: 仓库添加结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseAddRequest(
            access_token=access_token,
            param=WarehouseAddParam(
                warehouse_name=warehouse_name,
                warehouse_out_code=warehouse_out_code,
                province=province,
                city=city,
                district=district,
                address=address,
                contact_person=contact_person,
                contact_phone=contact_phone,
            ),
            api_version="1",
        )
        return self._client.execute(request, WarehouseAddResponse)

    def warehouse_info(
        self, access_token: str, warehouse_out_code: str
    ) -> WarehouseInfoResponse:
        """仓库信息查询（同步）

        OpenAPI: open.scm.warehouse.info (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseInfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseInfoRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码

        Returns:
            WarehouseInfoResponse: 仓库详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseInfoRequest(
            access_token=access_token,
            param=WarehouseInfoParam(warehouse_out_code=warehouse_out_code),
            api_version="1",
        )
        return self._client.execute(request, WarehouseInfoResponse)

    def warehouse_query(
        self,
        access_token: str,
        page_size: Optional[int] = None,
        page_no: Optional[int] = None,
    ) -> WarehouseQueryResponse:
        """仓库列表查询（同步）

        OpenAPI: open.scm.warehouse.query (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseQueryRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseQueryRequest.java)

        Args:
            access_token: 访问令牌
            page_size: 页面大小（可选）
            page_no: 页码（可选）

        Returns:
            WarehouseQueryResponse: 仓库列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseQueryRequest(
            access_token=access_token,
            param=WarehouseQueryParam(page_size=page_size, page_no=page_no),
            api_version="1",
        )
        return self._client.execute(request, WarehouseQueryResponse)

    def warehouse_update(
        self,
        access_token: str,
        warehouse_out_code: str,
        warehouse_name: Optional[str] = None,
        province: Optional[str] = None,
        city: Optional[str] = None,
        district: Optional[str] = None,
        address: Optional[str] = None,
        contact_person: Optional[str] = None,
        contact_phone: Optional[str] = None,
    ) -> WarehouseUpdateResponse:
        """仓库更新（同步）

        OpenAPI: open.scm.warehouse.update (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseUpdateRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseUpdateRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码
            warehouse_name: 仓库名称（可选）
            province: 省份（可选）
            city: 城市（可选）
            district: 区县（可选）
            address: 详细地址（可选）
            contact_person: 联系人姓名（可选）
            contact_phone: 联系人电话（可选）

        Returns:
            WarehouseUpdateResponse: 仓库更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseUpdateRequest(
            access_token=access_token,
            param=WarehouseUpdateParam(
                warehouse_out_code=warehouse_out_code,
                warehouse_name=warehouse_name,
                province=province,
                city=city,
                district=district,
                address=address,
                contact_person=contact_person,
                contact_phone=contact_phone,
            ),
            api_version="1",
        )
        return self._client.execute(request, WarehouseUpdateResponse)

    # ==================== 仓库高级功能 ====================
    def warehouse_package_weight_express(
        self, access_token: str, warehouse_out_code: str, package_weight: int
    ) -> WarehousePackageWeightExpressResponse:
        """仓库包裹重量快递查询（同步）

        OpenAPI: open.scm.package.weight.express (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmPackageWeightExpressRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmPackageWeightExpressRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码
            package_weight: 包裹重量（克）

        Returns:
            WarehousePackageWeightExpressResponse: 快递费用或推荐信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehousePackageWeightExpressRequest(
            access_token=access_token,
            param=WarehousePackageWeightExpressParam(
                warehouse_out_code=warehouse_out_code, package_weight=package_weight
            ),
            api_version="1",
        )
        return self._client.execute(request, WarehousePackageWeightExpressResponse)

    def warehouse_salescope_template_info(
        self, access_token: str, warehouse_out_code: str
    ) -> WarehouseSalescopeTemplateInfoResponse:
        """仓库销售范围模板信息查询（同步）

        OpenAPI: open.scm.warehouse.saleScopeTemplate.info (GET)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseSalescopetemplateInfoRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseSalescopetemplateInfoRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码

        Returns:
            WarehouseSalescopeTemplateInfoResponse: 销售范围模板信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseSalescopeTemplateInfoRequest(
            access_token=access_token,
            param=WarehouseSalescopeTemplateInfoParam(
                warehouse_out_code=warehouse_out_code
            ),
            api_version="1",
        )
        return self._client.execute(request, WarehouseSalescopeTemplateInfoResponse)

    def warehouse_salescope_template_operation(
        self,
        access_token: str,
        warehouse_out_code: str,
        operation_type: str,
        template_data: Optional[Dict[str, Any]] = None,
    ) -> WarehouseSalescopeTemplateOperationResponse:
        """仓库销售范围模板操作（同步）

        OpenAPI: open.scm.warehouse.saleScopeTemplate.operation (POST)
        Java: com.kuaishou.merchant.open.api.request.scm.OpenScmWarehouseSalescopetemplateOperationRequest
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/scm/OpenScmWarehouseSalescopetemplateOperationRequest.java)

        Args:
            access_token: 访问令牌
            warehouse_out_code: 仓库外部编码
            operation_type: 操作类型（如 CREATE/UPDATE）
            template_data: 模板数据（可选）

        Returns:
            WarehouseSalescopeTemplateOperationResponse: 操作结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = WarehouseSalescopeTemplateOperationRequest(
            access_token=access_token,
            param=WarehouseSalescopeTemplateOperationParam(
                warehouse_out_code=warehouse_out_code,
                operation_type=operation_type,
                template_data=template_data,
            ),
            api_version="1",
        )
        return self._client.execute(
            request, WarehouseSalescopeTemplateOperationResponse
        )
