"""SCM供应链管理相关数据模型
基于Java SDK参考实现，提供库存管理、商品管理、仓库管理等功能
"""

from typing import Any, ClassVar, Dict, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod


# ==================== 库存调整相关 ====================
class InventoryAdjustParam(BaseModel):
    """库存调整参数"""

    ware_out_code: str = Field(..., description="商品外部编码")
    idempotent_id: str = Field(..., description="幂等ID")
    warehouse_out_code: str = Field(..., description="仓库外部编码")
    operation_type: str = Field(..., description="操作类型")
    adjust_quantity: int = Field(..., description="调整数量")


class InventoryAdjustRequest(BaseRequest):
    """库存调整请求
    API: open.scm.inventory.adjust (POST)
    """

    param: InventoryAdjustParam = Field(..., description="调整参数")

    @property
    def api_method(self) -> str:
        return "open.scm.inventory.adjust"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class InventoryAdjustResponse(BaseResponse[Dict[str, Any]]):
    """库存调整响应"""

    pass


# ==================== 库存详情查询相关 ====================
class InventoryDetailParam(BaseModel):
    """库存详情查询参数"""

    ware_out_code: str = Field(..., description="商品外部编码")


class InventoryDetailRequest(BaseRequest):
    """库存详情查询请求
    API: open.scm.inventory.detail (GET)
    """

    param: InventoryDetailParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.inventory.detail"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InventoryDetailResponse(BaseResponse[Dict[str, Any]]):
    """库存详情查询响应"""

    pass


# ==================== 库存更新相关 ====================
class InventoryUpdateParam(BaseModel):
    """库存更新参数"""

    ware_out_code: str = Field(..., description="商品外部编码")
    quantity: int = Field(..., description="库存数量")
    warehouse_out_code: str = Field(..., description="仓库外部编码")


class InventoryUpdateRequest(BaseRequest):
    """库存更新请求
    API: open.scm.inventory.update (GET)
    """

    param: InventoryUpdateParam = Field(..., description="更新参数")

    @property
    def api_method(self) -> str:
        return "open.scm.inventory.update"

    # 固定使用 GET（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class InventoryUpdateResponse(BaseResponse[Dict[str, Any]]):
    """库存更新响应"""

    pass


# ==================== 商品添加相关 ====================
class WareAddParam(BaseModel):
    """商品添加参数"""

    ware_volume: Optional[int] = Field(None, description="商品体积")
    ware_name: str = Field(..., description="商品名称")
    ware_height: Optional[int] = Field(None, description="商品高度")
    ware_width: Optional[int] = Field(None, description="商品宽度")
    ware_out_code: str = Field(..., description="商品外部编码")
    owner_source_name: Optional[str] = Field(None, description="货主来源名称")
    ware_length: Optional[int] = Field(None, description="商品长度")
    owner_source_type_enum: Optional[str] = Field(None, description="货主来源类型")
    barcode: Optional[str] = Field(None, description="条形码")
    ware_weight: Optional[int] = Field(None, description="商品重量")


class WareAddRequest(BaseRequest):
    """商品添加请求
    API: open.scm.ware.add (GET)
    """

    param: WareAddParam = Field(..., description="商品参数")

    @property
    def api_method(self) -> str:
        return "open.scm.ware.add"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WareAddResponse(BaseResponse[Dict[str, Any]]):
    """商品添加响应"""

    pass


# ==================== 商品信息查询相关 ====================
class WareInfoParam(BaseModel):
    """商品信息查询参数"""

    ware_out_code: str = Field(..., description="商品外部编码")


class WareInfoRequest(BaseRequest):
    """商品信息查询请求
    API: open.scm.ware.info (GET)
    """

    param: WareInfoParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.ware.info"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WareInfoResponse(BaseResponse[Dict[str, Any]]):
    """商品信息查询响应"""

    pass


# ==================== 商品列表查询相关 ====================
class WareListParam(BaseModel):
    """商品列表查询参数"""

    page_size: Optional[int] = Field(20, description="页面大小", ge=1, le=100)
    page_no: Optional[int] = Field(1, description="页码", ge=1)
    warehouse_out_code: Optional[str] = Field(None, description="仓库外部编码")


class WareListRequest(BaseRequest):
    """商品列表查询请求
    API: open.scm.ware.list (GET)
    """

    param: WareListParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.ware.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WareListResponse(BaseResponse[Dict[str, Any]]):
    """商品列表查询响应"""

    pass


# ==================== 商品更新相关 ====================
class WareUpdateParam(BaseModel):
    """商品更新参数"""

    ware_volume: Optional[int] = Field(None, description="商品体积")
    ware_name: Optional[str] = Field(None, description="商品名称")
    ware_height: Optional[int] = Field(None, description="商品高度")
    ware_width: Optional[int] = Field(None, description="商品宽度")
    ware_out_code: str = Field(..., description="商品外部编码")
    owner_source_name: Optional[str] = Field(None, description="货主来源名称")
    ware_length: Optional[int] = Field(None, description="商品长度")
    owner_source_type_enum: Optional[str] = Field(None, description="货主来源类型")
    barcode: Optional[str] = Field(None, description="条形码")
    ware_weight: Optional[int] = Field(None, description="商品重量")


class WareUpdateRequest(BaseRequest):
    """商品更新请求
    API: open.scm.ware.update (GET)
    """

    param: WareUpdateParam = Field(..., description="更新参数")

    @property
    def api_method(self) -> str:
        return "open.scm.ware.update"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WareUpdateResponse(BaseResponse[Dict[str, Any]]):
    """商品更新响应"""

    pass


# ==================== 仓库添加相关 ====================
class WarehouseAddParam(BaseModel):
    """仓库添加参数"""

    warehouse_name: str = Field(..., description="仓库名称")
    warehouse_out_code: str = Field(..., description="仓库外部编码")
    province: str = Field(..., description="省份")
    city: str = Field(..., description="城市")
    district: str = Field(..., description="区域")
    address: str = Field(..., description="详细地址")
    contact_person: Optional[str] = Field(None, description="联系人")
    contact_phone: Optional[str] = Field(None, description="联系电话")


class WarehouseAddRequest(BaseRequest):
    """仓库添加请求
    API: open.scm.warehouse.add (POST)
    """

    param: WarehouseAddParam = Field(..., description="仓库参数")

    @property
    def api_method(self) -> str:
        return "open.scm.warehouse.add"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class WarehouseAddResponse(BaseResponse[Dict[str, Any]]):
    """仓库添加响应"""

    pass


# ==================== 仓库信息查询相关 ====================
class WarehouseInfoParam(BaseModel):
    """仓库信息查询参数"""

    warehouse_out_code: str = Field(..., description="仓库外部编码")


class WarehouseInfoRequest(BaseRequest):
    """仓库信息查询请求
    API: open.scm.warehouse.info (GET)
    """

    param: WarehouseInfoParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.warehouse.info"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WarehouseInfoResponse(BaseResponse[Dict[str, Any]]):
    """仓库信息查询响应"""

    pass


# ==================== 仓库列表查询相关 ====================
class WarehouseQueryParam(BaseModel):
    """仓库列表查询参数"""

    page_size: Optional[int] = Field(20, description="页面大小", ge=1, le=100)
    page_no: Optional[int] = Field(1, description="页码", ge=1)


class WarehouseQueryRequest(BaseRequest):
    """仓库列表查询请求
    API: open.scm.warehouse.query (GET)
    """

    param: WarehouseQueryParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.warehouse.query"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WarehouseQueryResponse(BaseResponse[Dict[str, Any]]):
    """仓库列表查询响应"""

    pass


# ==================== 仓库更新相关 ====================
class WarehouseUpdateParam(BaseModel):
    """仓库更新参数"""

    warehouse_out_code: str = Field(..., description="仓库外部编码")
    warehouse_name: Optional[str] = Field(None, description="仓库名称")
    province: Optional[str] = Field(None, description="省份")
    city: Optional[str] = Field(None, description="城市")
    district: Optional[str] = Field(None, description="区域")
    address: Optional[str] = Field(None, description="详细地址")
    contact_person: Optional[str] = Field(None, description="联系人")
    contact_phone: Optional[str] = Field(None, description="联系电话")


class WarehouseUpdateRequest(BaseRequest):
    """仓库更新请求
    API: open.scm.warehouse.update (POST)
    """

    param: WarehouseUpdateParam = Field(..., description="更新参数")

    @property
    def api_method(self) -> str:
        return "open.scm.warehouse.update"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class WarehouseUpdateResponse(BaseResponse[Dict[str, Any]]):
    """仓库更新响应"""

    pass


# ==================== 仓库包裹重量快递查询相关 ====================
class WarehousePackageWeightExpressParam(BaseModel):
    """仓库包裹重量快递查询参数"""

    warehouse_out_code: str = Field(..., description="仓库外部编码")
    package_weight: int = Field(..., description="包裹重量(克)")


class WarehousePackageWeightExpressRequest(BaseRequest):
    """仓库包裹重量快递查询请求
    API: open.scm.package.weight.express (POST)
    """

    param: WarehousePackageWeightExpressParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.package.weight.express"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class WarehousePackageWeightExpressResponse(BaseResponse[Dict[str, Any]]):
    """仓库包裹重量快递查询响应"""

    pass


# ==================== 仓库销售范围模板信息查询相关 ====================
class WarehouseSalescopeTemplateInfoParam(BaseModel):
    """仓库销售范围模板信息查询参数"""

    warehouse_out_code: str = Field(..., description="仓库外部编码")


class WarehouseSalescopeTemplateInfoRequest(BaseRequest):
    """仓库销售范围模板信息查询请求
    API: open.scm.warehouse.saleScopeTemplate.info (GET)
    """

    param: WarehouseSalescopeTemplateInfoParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.scm.warehouse.saleScopeTemplate.info"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class WarehouseSalescopeTemplateInfoResponse(BaseResponse[Dict[str, Any]]):
    """仓库销售范围模板信息查询响应"""

    pass


# ==================== 仓库销售范围模板操作相关 ====================
class WarehouseSalescopeTemplateOperationParam(BaseModel):
    """仓库销售范围模板操作参数"""

    warehouse_out_code: str = Field(..., description="仓库外部编码")
    operation_type: str = Field(..., description="操作类型")
    template_data: Optional[Dict[str, Any]] = Field(None, description="模板数据")


class WarehouseSalescopeTemplateOperationRequest(BaseRequest):
    """仓库销售范围模板操作请求
    API: open.scm.warehouse.saleScopeTemplate.operation (POST)
    """

    param: WarehouseSalescopeTemplateOperationParam = Field(..., description="操作参数")

    @property
    def api_method(self) -> str:
        return "open.scm.warehouse.saleScopeTemplate.operation"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class WarehouseSalescopeTemplateOperationResponse(BaseResponse[Dict[str, Any]]):
    """仓库销售范围模板操作响应"""

    pass
