"""商品相关数据模型"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod, PagedResponse
from .common import ItemStatus


class ItemSpec(BaseModel):
    """商品规格"""

    spec_id: int = Field(description="规格ID")
    spec_name: str = Field(description="规格名称")
    spec_value: str = Field(description="规格值")


class ItemSku(BaseModel):
    """商品SKU"""

    sku_id: int = Field(description="SKU ID")
    specs: List[ItemSpec] = Field(default_factory=lambda: [], description="规格列表")
    price: int = Field(description="价格（分）")
    original_price: Optional[int] = Field(default=None, description="原价（分）")
    stock: int = Field(description="库存", ge=0)
    sku_code: Optional[str] = Field(default=None, description="SKU编码")
    barcode: Optional[str] = Field(default=None, description="条形码")

    @property
    def price_yuan(self) -> float:
        """价格（元）"""
        return self.price / 100

    @property
    def original_price_yuan(self) -> Optional[float]:
        """原价（元）"""
        return self.original_price / 100 if self.original_price else None

    @property
    def spec_text(self) -> str:
        """规格文本描述"""
        return ", ".join([f"{spec.spec_name}:{spec.spec_value}" for spec in self.specs])


class ItemCategory(BaseModel):
    """商品类目"""

    category_id: int = Field(description="类目ID")
    category_name: str = Field(description="类目名称")
    parent_id: Optional[int] = Field(default=None, description="父类目ID")
    level: Optional[int] = Field(default=None, description="类目层级")


class Item(BaseModel):
    """商品信息"""

    item_id: int = Field(description="商品ID")
    title: str = Field(description="商品标题")
    sub_title: Optional[str] = Field(default=None, description="副标题")
    status: ItemStatus = Field(description="商品状态")

    # 分类信息
    category: Optional[ItemCategory] = Field(default=None, description="商品类目")

    # 价格信息
    price: int = Field(description="价格（分）")
    original_price: Optional[int] = Field(default=None, description="原价（分）")

    # 库存信息
    stock: int = Field(description="总库存", ge=0)
    sold_count: Optional[int] = Field(default=None, description="销量")

    # 图片信息
    main_image: Optional[str] = Field(default=None, description="主图URL")
    images: List[str] = Field(default_factory=lambda: [], description="图片列表")

    # SKU信息
    skus: List[ItemSku] = Field(default_factory=lambda: [], description="SKU列表")

    # 描述信息
    description: Optional[str] = Field(default=None, description="商品描述")
    detail_images: List[str] = Field(default_factory=lambda: [], description="详情图片")

    # 时间信息
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")

    # 其他信息
    weight: Optional[int] = Field(default=None, description="重量（克）")
    brand: Optional[str] = Field(default=None, description="品牌")
    item_code: Optional[str] = Field(default=None, description="商品编码")

    @property
    def price_yuan(self) -> float:
        """价格（元）"""
        return self.price / 100

    @property
    def original_price_yuan(self) -> Optional[float]:
        """原价（元）"""
        return self.original_price / 100 if self.original_price else None

    @property
    def is_multi_sku(self) -> bool:
        """是否多SKU商品"""
        return len(self.skus) > 1

    @property
    def is_in_stock(self) -> bool:
        """是否有库存"""
        return self.stock > 0


# ==================== 商品查询相关 ====================


class ItemListRequest(BaseRequest):
    """商品列表查询请求（对齐 Java: open.item.list.get）"""

    # Java ParamDTO: kwaiItemId, relItemId, itemStatus, itemType, pageNumber, pageSize, onOfflineStatus
    kwai_item_id: Optional[int] = Field(
        default=None, description="快手商品ID", alias="kwaiItemId"
    )
    rel_item_id: Optional[int] = Field(
        default=None, description="关联商品ID", alias="relItemId"
    )
    item_status: Optional[int] = Field(
        default=None, description="商品状态", alias="itemStatus"
    )
    item_type: Optional[int] = Field(
        default=None, description="商品类型", alias="itemType"
    )
    page_number: Optional[int] = Field(
        default=1, description="页码", alias="pageNumber"
    )
    page_size: Optional[int] = Field(
        default=20, description="页面大小", alias="pageSize"
    )
    on_offline_status: Optional[int] = Field(
        default=None, description="上下线状态", alias="onOfflineStatus"
    )

    # Java: OpenItemListGetRequest -> HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.list.get"


class ItemListResponse(BaseResponse[List[Item]]):
    """商品列表响应"""

    total: Optional[int] = Field(default=None, description="总数量")
    has_more: Optional[bool] = Field(default=None, description="是否有更多")


class ItemGetRequest(BaseRequest):
    """商品详情查询请求"""

    kwai_item_id: int = Field(description="快手商品ID", alias="kwaiItemId")

    @property
    def api_method(self) -> str:
        return "open.item.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemGetResponse(BaseResponse[Item]):
    """商品详情响应"""

    pass


# ==================== 商品管理相关 ====================


## Removed deprecated open.item.add / open.item.update in favor of open.item.new/edit


class ItemUpdateStockRequest(BaseRequest):
    """商品SKU库存更新请求

    对应 Java: OpenItemSkuStockUpdateRequest -> open.item.sku.stock.update
    """

    item_id: int = Field(description="商品ID", alias="kwaiItemId")
    sku_id: int = Field(description="SKU ID", alias="skuId")
    stock: int = Field(description="库存变化数量或设定值", ge=0, alias="skuChangeStock")
    change_type: Optional[int] = Field(
        default=None, description="变更类型（平台定义）", alias="changeType"
    )

    @property
    def api_method(self) -> str:
        return "open.item.sku.stock.update"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemUpdateStockResponse(BaseResponse[Dict[str, Any]]):
    """商品库存更新响应"""

    pass


class ItemDeleteRequest(BaseRequest):
    """商品删除请求"""

    kwai_item_id: int = Field(description="快手商品ID", alias="kwaiItemId")
    rel_item_id: Optional[int] = Field(
        default=None, description="关联商品ID", alias="relItemId"
    )

    @property
    def api_method(self) -> str:
        return "open.item.delete"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemDeleteResponse(BaseResponse[Dict[str, Any]]):
    """商品删除响应"""

    pass


# ==================== 分类管理相关 ====================


class ItemCategoryRequest(BaseRequest):
    """获取商品分类请求"""

    # Based on Java SDK: KsMerchantItemCategoryRequest
    @property
    def api_method(self) -> str:
        return "open.item.category"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemCategoryResponse(BaseResponse[List[ItemCategory]]):
    """获取商品分类响应"""

    pass


class CategoryConfig(BaseModel):
    """分类配置信息"""

    category_id: int = Field(description="分类ID")
    category_name: str = Field(description="分类名称")
    level: int = Field(description="层级")
    parent_id: Optional[int] = Field(default=None, description="父分类ID")
    is_leaf: bool = Field(description="是否叶子节点")
    sort_order: Optional[int] = Field(default=None, description="排序")
    status: int = Field(description="状态")


class ItemCategoryConfigRequest(BaseRequest):
    """获取分类配置请求"""

    category_id: Optional[int] = Field(
        default=None, description="分类ID", alias="categoryId"
    )

    @property
    def api_method(self) -> str:
        return "open.item.category.config"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemCategoryConfigResponse(BaseResponse[List[CategoryConfig]]):
    """获取分类配置响应"""

    pass


class ItemOptionalCategoryRequest(BaseRequest):
    """获取可选分类请求"""

    @property
    def api_method(self) -> str:
        return "open.item.category.optional.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemOptionalCategoryResponse(BaseResponse[List[ItemCategory]]):
    """获取可选分类响应"""

    pass


class SuggestedCategory(BaseModel):
    """推荐分类"""

    category_id: int = Field(description="分类ID")
    category_name: str = Field(description="分类名称")
    confidence: Optional[float] = Field(default=None, description="置信度")
    reason: Optional[str] = Field(default=None, description="推荐原因")


class ItemSuggestedCategoryRequest(BaseRequest):
    """获取推荐分类请求"""

    image_urls: Optional[List[str]] = Field(
        default=None, description="商品图片URL列表", alias="imageUrls"
    )
    item_title: Optional[str] = Field(
        default=None, description="商品标题", alias="itemTitle"
    )
    item_desc: Optional[str] = Field(
        default=None, description="商品描述", alias="itemDesc"
    )

    @property
    def api_method(self) -> str:
        return "open.item.category.suggested.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemSuggestedCategoryResponse(BaseResponse[List[SuggestedCategory]]):
    """获取推荐分类响应"""

    pass


class PropStandard(BaseModel):
    """属性标准"""

    prop_id: int = Field(description="属性ID")
    prop_name: str = Field(description="属性名称")
    prop_type: str = Field(description="属性类型")
    required: bool = Field(description="是否必填")
    values: Optional[List[str]] = Field(default=None, description="可选值列表")


class ItemCategoryPropStandardRequest(BaseRequest):
    """获取分类属性标准请求"""

    leaf_category_id: int = Field(description="叶子分类ID", alias="leafCategoryId")

    @property
    def api_method(self) -> str:
        return "open.item.category.prop.standard.get"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemCategoryPropStandardResponse(BaseResponse[List[PropStandard]]):
    """获取分类属性标准响应"""

    pass


class PropValue(BaseModel):
    """属性值"""

    value_id: int = Field(description="属性值ID")
    value_name: str = Field(description="属性值名称")
    parent_value_id: Optional[int] = Field(default=None, description="父属性值ID")


class ItemCategoryPropValueSearchRequest(BaseRequest):
    """搜索分类属性值请求"""

    category_id: int = Field(description="分类ID", alias="categoryId")
    prop_id: int = Field(description="属性ID", alias="propId")
    prop_value: Optional[str] = Field(
        default=None, description="属性值搜索", alias="propValue"
    )
    cursor: Optional[int] = Field(default=None, description="游标", alias="cursor")
    limit: Optional[int] = Field(default=None, description="条数限制", alias="limit")

    @property
    def api_method(self) -> str:
        return "open.item.category.prop.value.search"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemCategoryPropValueSearchResponse(PagedResponse[PropValue]):
    """搜索分类属性值响应"""

    pass


class StandardCheckResult(BaseModel):
    """标准检查结果"""

    is_pass: bool = Field(description="是否通过检查")
    error_message: Optional[str] = Field(default=None, description="错误信息")
    suggestions: Optional[List[str]] = Field(default=None, description="建议列表")


class ItemCategoryStandardCheckRequest(BaseRequest):
    """检查分类标准请求"""

    leaf_category_id: int = Field(description="叶子分类ID", alias="leafCategoryId")

    @property
    def api_method(self) -> str:
        return "open.item.category.standard.check"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemCategoryStandardCheckResponse(BaseResponse[StandardCheckResult]):
    """检查分类标准响应"""

    pass


class CategoryStandard(BaseModel):
    """分类标准"""

    category_id: int = Field(description="分类ID")
    standard_id: str = Field(description="标准ID")
    standard_name: str = Field(description="标准名称")
    description: Optional[str] = Field(default=None, description="标准描述")


class StandardKeyProp(BaseModel):
    """标准关键属性（Java: StandardKeyProp）"""

    prop_id: Optional[int] = Field(default=None, alias="propId")
    prop_name: Optional[str] = Field(default=None, alias="propName")
    input_type: Optional[str] = Field(default=None, alias="inputType")
    prop_value_id: Optional[int] = Field(default=None, alias="propValueId")
    prop_value_name: Optional[str] = Field(default=None, alias="propValueName")


class ItemCategoryStandardSearchRequest(BaseRequest):
    """搜索分类标准请求（对齐 Java）"""

    standard_id: Optional[int] = Field(default=None, alias="standardId")
    leaf_category_id: Optional[int] = Field(default=None, alias="leafCategoryId")
    standard_key_prop_list: Optional[List[StandardKeyProp]] = Field(
        default=None, alias="standardKeyPropList"
    )

    @property
    def api_method(self) -> str:
        return "open.item.category.standard.search"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemCategoryStandardSearchResponse(BaseResponse[Dict[str, Any]]):
    """搜索分类标准响应（data: StandardInfoForOpenApiDTO）"""

    pass


# ==================== 品牌管理相关 ====================


class Brand(BaseModel):
    """品牌信息"""

    brand_id: int = Field(description="品牌ID")
    brand_name: str = Field(description="品牌名称")
    brand_logo: Optional[str] = Field(default=None, description="品牌Logo")
    brand_desc: Optional[str] = Field(default=None, description="品牌描述")
    status: int = Field(description="状态")


class ItemBrandListRequest(BaseRequest):
    """获取品牌列表请求"""

    cursor: Optional[int] = Field(default=None, description="游标", alias="cursor")
    category_id: Optional[int] = Field(
        default=None, description="分类ID", alias="categoryId"
    )
    prop_id: Optional[int] = Field(default=None, description="属性ID", alias="propId")
    prop_value: Optional[str] = Field(
        default=None, description="属性值", alias="propValue"
    )

    @property
    def api_method(self) -> str:
        return "open.item.brand.list.get"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemBrandListResponse(PagedResponse[Brand]):
    """获取品牌列表响应"""

    pass


# ==================== 资质配置相关 ====================


class QualificationConfig(BaseModel):
    """资质配置"""

    category_id: int = Field(description="分类ID")
    qualification_type: str = Field(description="资质类型")
    qualification_name: str = Field(description="资质名称")
    required: bool = Field(description="是否必需")
    description: Optional[str] = Field(default=None, description="资质描述")


class ItemQualificationConfigRequest(BaseRequest):
    """获取资质配置请求"""

    category_id: int = Field(description="分类ID", alias="categoryId")

    @property
    def api_method(self) -> str:
        return "open.item.qualification.collection.config"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemQualificationConfigResponse(BaseResponse[List[QualificationConfig]]):
    """获取资质配置响应"""

    pass


# ==================== 销售属性规则相关 ====================


class SalePropRule(BaseModel):
    """销售属性规则"""

    category_id: int = Field(description="分类ID")
    prop_rules: List[Dict[str, Any]] = Field(description="属性规则列表")
    combinations: Optional[List[Dict[str, Any]]] = Field(
        default=None, description="属性组合规则"
    )


class ItemSalePropRuleRequest(BaseRequest):
    """获取销售属性规则请求（Java: OpenItemSalepropRuleRequest）"""

    category_id: int = Field(description="分类ID", alias="categoryId")
    spu_id: Optional[int] = Field(default=None, description="SPU ID", alias="spuId")
    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.item.saleprop.rule"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemSalePropRuleResponse(BaseResponse[Dict[str, Any]]):
    """获取销售属性规则响应（data: OpenApiSalePropConfigModelProto）"""

    pass


# ==================== SKU管理相关 ====================


class ItemSkuListRequest(BaseRequest):
    """获取SKU列表请求"""

    # Based on Java SDK: OpenItemSkuListGetRequest
    kwai_item_id: int = Field(description="快手商品ID", alias="kwaiItemId")
    rel_sku_id: Optional[int] = Field(
        default=None, description="关联SKU ID", alias="relSkuId"
    )
    sku_status: Optional[int] = Field(
        default=None, description="SKU状态", alias="skuStatus"
    )

    @property
    def api_method(self) -> str:
        return "open.item.sku.list.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemSkuListResponse(BaseResponse[List[ItemSku]]):
    """获取SKU列表响应"""

    pass


class ItemSkuPriceUpdateRequest(BaseRequest):
    """更新SKU价格请求"""

    # Based on Java SDK: OpenItemSkuPriceUpdateRequest
    item_id: int = Field(description="商品ID", alias="itemId")
    price: int = Field(description="新价格（分）", alias="price")
    sku_id: int = Field(description="SKU ID", alias="skuId")

    @property
    def api_method(self) -> str:
        return "open.item.sku.price.update"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemSkuPriceUpdateResponse(BaseResponse[Dict[str, Any]]):
    """更新SKU价格响应"""

    pass


class SkuGoodsRelationParam(BaseModel):
    """SKU与商品关系参数（Java: SkuGoodsRelationParam）"""

    goods_id: str = Field(description="商品ID", alias="goodsId")
    sku_id: int = Field(description="SKU ID", alias="skuId")


class ItemSkuGoodsRelationAddRequest(BaseRequest):
    """添加SKU商品关系请求"""

    item_id: int = Field(description="商品ID", alias="itemId")
    sku_goods_relation: List[SkuGoodsRelationParam] = Field(
        description="SKU关系参数列表", alias="skuGoodsRelation"
    )

    @property
    def api_method(self) -> str:
        return "open.item.sku.goods.relation.add"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemSkuGoodsRelationUpdateRequest(BaseRequest):
    """更新SKU商品关系请求"""

    item_id: int = Field(description="商品ID", alias="itemId")
    sku_goods_relation: List[SkuGoodsRelationParam] = Field(
        description="SKU关系参数列表", alias="skuGoodsRelation"
    )

    @property
    def api_method(self) -> str:
        return "open.item.sku.goods.relation.update"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemSkuGoodsRelationGetRequest(BaseRequest):
    """获取SKU商品关系请求"""

    sku_id: List[int] = Field(description="SKU ID 列表", alias="skuId")

    @property
    def api_method(self) -> str:
        return "open.item.sku.goods.relation.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemSkuGoodsRelationDeleteRequest(BaseRequest):
    """删除SKU商品关系请求"""

    item_id: int = Field(description="商品ID", alias="itemId")
    sku_goods_relation: List[SkuGoodsRelationParam] = Field(
        description="SKU关系参数列表", alias="skuGoodsRelation"
    )
    update_item_stock_model: Optional[bool] = Field(
        default=None, description="是否更新商品库存模型", alias="updateItemStockModel"
    )

    @property
    def api_method(self) -> str:
        return "open.item.sku.goods.relation.delete"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SkuGoodsRelationDTO(BaseModel):
    """SKU商品关系（Java: SkuGoodsRelationDTO）"""

    item_id: Optional[int] = Field(default=None, alias="itemId")
    sku_id: Optional[int] = Field(default=None, alias="skuId")
    goods_id: Optional[str] = Field(default=None, alias="goodsId")
    goods_code: Optional[str] = Field(default=None, alias="goodsCode")


class ItemSkuGoodsRelationResponse(BaseResponse[List[SkuGoodsRelationDTO]]):
    """SKU商品关系响应"""

    pass


class ItemSkuGoodsRelationModifyResponse(BaseResponse[Dict[str, Any]]):
    """SKU商品关系修改响应"""

    pass


class SkuStockInfo(BaseModel):
    """SKU库存信息（Java: SkuStockInfo）"""

    sku_id: int = Field(description="SKU ID", alias="skuId")
    stock_type: Optional[str] = Field(
        default=None, description="库存类型", alias="stockType"
    )
    amount: Optional[int] = Field(default=None, description="数量", alias="amount")
    operation_type: Optional[str] = Field(
        default=None, description="操作类型", alias="operationType"
    )


class ItemStockManageRequest(BaseRequest):
    """库存管理请求（对齐 Java: open.stock.manage）"""

    seq_no: Optional[str] = Field(default=None, description="序列号", alias="seqNo")
    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")
    category_id: Optional[int] = Field(
        default=None, description="类目ID", alias="categoryId"
    )
    sku_stock_infos: List[SkuStockInfo] = Field(
        default_factory=list, description="SKU库存列表", alias="skuStockInfos"
    )
    support_negative_stock: Optional[bool] = Field(
        default=None, description="是否支持负库存", alias="supportNegativeStock"
    )

    @property
    def api_method(self) -> str:
        return "open.stock.manage"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemStockManageResponse(BaseResponse[Dict[str, Any]]):
    """库存管理响应"""

    pass


# ==================== 媒体管理相关 ====================


class ItemImageUploadRequest(BaseRequest):
    """商品图片上传请求"""

    # Based on Java SDK: OpenItemImageUploadRequest
    img_url: Optional[str] = Field(default=None, description="图片URL", alias="imgUrl")
    upload_type: int = Field(description="上传类型", alias="uploadType")
    img_bytes: Optional[bytes] = Field(
        default=None, description="图片字节数据", alias="imgBytes"
    )

    @property
    def api_method(self) -> str:
        return "open.item.image.upload"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemImageUploadResponse(BaseResponse[Dict[str, Any]]):
    """商品图片上传响应"""

    image_url: Optional[str] = Field(default=None, description="上传后的图片URL")


class ItemMaterialUploadTokenIssueRequest(BaseRequest):
    """申请上传凭证请求"""

    # Based on Java SDK: OpenItemMaterialUploadTokenIssueRequest
    material_upload_type: int = Field(
        description="素材上传类型", alias="materialUploadType"
    )
    file_name: str = Field(description="文件名", alias="fileName")
    file_length: int = Field(description="文件大小", alias="fileLength")

    @property
    def api_method(self) -> str:
        return "open.item.material.upload.token.issue"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UploadToken(BaseModel):
    """上传凭证"""

    token: str = Field(description="上传凭证")
    upload_url: str = Field(description="上传URL")
    expire_time: Optional[str] = Field(default=None, description="过期时间")


class ItemMaterialUploadTokenIssueResponse(BaseResponse[UploadToken]):
    """申请上传凭证响应"""

    pass


class ItemMaterialUploadTokenVerifyRequest(BaseRequest):
    """验证上传凭证请求"""

    token: str = Field(description="上传凭证", alias="token")
    material_upload_type: Optional[int] = Field(
        default=None, description="素材上传类型", alias="materialUploadType"
    )

    @property
    def api_method(self) -> str:
        return "open.item.material.upload.token.verify"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemMaterialUploadTokenVerifyResponse(BaseResponse[Dict[str, Any]]):
    """验证上传凭证响应"""

    is_valid: bool = Field(description="凭证是否有效")


class ItemMaterialDetailGetRequest(BaseRequest):
    """获取素材详情请求"""

    material_id: int = Field(description="素材ID", alias="materialId")
    material_upload_type: Optional[int] = Field(
        default=None, description="素材上传类型", alias="materialUploadType"
    )

    @property
    def api_method(self) -> str:
        return "open.item.material.detail.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class MaterialDetail(BaseModel):
    """素材详情"""

    material_id: str = Field(description="素材ID")
    material_url: str = Field(description="素材URL")
    material_type: str = Field(description="素材类型")
    file_size: Optional[int] = Field(default=None, description="文件大小")
    width: Optional[int] = Field(default=None, description="宽度")
    height: Optional[int] = Field(default=None, description="高度")
    duration: Optional[int] = Field(default=None, description="时长（视频）")
    create_time: Optional[str] = Field(default=None, description="创建时间")


class ItemMaterialDetailGetResponse(BaseResponse[MaterialDetail]):
    """获取素材详情响应"""

    pass


class ItemVideoListRequest(BaseRequest):
    """获取视频列表请求"""

    video_type: Optional[int] = Field(
        default=None, description="视频类型", alias="videoType"
    )
    aspect_ratio: Optional[int] = Field(
        default=None, description="宽高比", alias="aspectRatio"
    )
    audit_status: Optional[int] = Field(
        default=None, description="审核状态", alias="auditStatus"
    )
    create_time_start: Optional[int] = Field(
        default=None, description="创建开始时间", alias="createTimeStart"
    )
    create_time_end: Optional[int] = Field(
        default=None, description="创建结束时间", alias="createTimeEnd"
    )
    page_index: Optional[int] = Field(
        default=None, description="页码", alias="pageIndex"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.item.video.list"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class VideoInfo(BaseModel):
    """视频信息"""

    video_id: str = Field(description="视频ID")
    video_url: str = Field(description="视频URL")
    cover_url: Optional[str] = Field(default=None, description="封面URL")
    duration: Optional[int] = Field(default=None, description="时长（秒）")
    width: Optional[int] = Field(default=None, description="宽度")
    height: Optional[int] = Field(default=None, description="高度")
    status: int = Field(description="状态")
    create_time: Optional[str] = Field(default=None, description="创建时间")


class ItemVideoListResponse(PagedResponse[VideoInfo]):
    """获取视频列表响应"""

    pass


## Note: Java reference uses videoType/aspectRatio filters; duplicate earlier
## request/response classes removed in favor of Java-aligned versions below.


class ItemVideoDeleteRequest(BaseRequest):
    """删除视频请求"""

    video_type: Optional[int] = Field(
        default=None, description="视频类型", alias="videoType"
    )
    video_id: List[str] = Field(description="视频ID列表", alias="videoId")

    @property
    def api_method(self) -> str:
        return "open.item.video.delete"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemVideoDeleteResponse(BaseResponse[Dict[str, Any]]):
    """删除视频响应"""

    pass


# ==================== 高级操作 API 模型 ====================


class ItemAutopassEditRequest(BaseRequest):
    """商品自动通过编辑请求"""

    # Based on Java SDK: OpenItemAutopassEditRequest

    item_id: int = Field(description="商品ID", alias="itemId")
    purchase_limit: Optional[bool] = Field(
        default=None, description="购买限制", alias="purchaseLimit"
    )
    limit_count: Optional[int] = Field(
        default=None, description="限制数量", alias="limitCount"
    )
    item_remark: Optional[str] = Field(
        default=None, description="商品备注", alias="itemRemark"
    )
    sku_list: Optional[List["OpenApiAutoPassSkuDTO"]] = Field(
        default=None, description="SKU列表", alias="skuList"
    )
    service_rule: Optional["ServiceRule"] = Field(
        default=None, description="服务规则", alias="serviceRule"
    )
    express_template_id: Optional[int] = Field(
        default=None, description="快递模板ID", alias="expressTemplateId"
    )
    sale_time_flag: Optional[bool] = Field(
        default=None, description="销售时间标志", alias="saleTimeFlag"
    )
    time_of_sale: Optional[int] = Field(
        default=None, description="销售时间", alias="timeOfSale"
    )
    pay_way: Optional[int] = Field(default=None, description="支付方式", alias="payWay")

    @property
    def api_method(self) -> str:
        return "open.item.autopass.edit"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemAutopassEditResponse(BaseResponse[Dict[str, Any]]):
    """商品自动通过编辑响应"""

    pass


class ItemDetailImagesUpdateRequest(BaseRequest):
    """商品详情图片更新请求"""

    # Based on Java SDK: OpenItemDetailImagesUpdateRequest

    kwai_item_id: int = Field(description="快手商品ID", alias="kwaiItemId")
    detail_image_urls: List[str] = Field(
        description="详情图片URL列表", alias="detailImageUrls"
    )

    @property
    def api_method(self) -> str:
        return "open.item.detail.images.update"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemDetailImagesUpdateResponse(BaseResponse[Dict[str, Any]]):
    """商品详情图片更新响应"""

    pass


class ItemDetailPageLinkRequest(BaseRequest):
    """商品详情页链接请求"""

    # Based on Java SDK: OpenItemDetailPageLinkRequest

    item_id: int = Field(description="商品ID", alias="itemId")
    type: int = Field(description="类型", alias="type")
    item_product_client_info: Optional[Dict[str, Any]] = Field(
        default=None, description="商品客户端信息", alias="itemProductClientInfo"
    )

    @property
    def api_method(self) -> str:
        return "open.item.detail.page.link"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemDetailPageLinkResponse(BaseResponse[Dict[str, Any]]):
    """商品详情页链接响应"""

    pass


class ItemDiagnosisGetRequest(BaseRequest):
    """商品诊断获取请求"""

    # Based on Java SDK: OpenItemDiagnosisGetRequest

    item_id: int = Field(description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.item.diagnosis.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemDiagnosisGetResponse(BaseResponse[Dict[str, Any]]):
    """商品诊断获取响应"""

    pass


class ItemMainPicVideoApplyRequest(BaseRequest):
    """商品主图视频申请请求"""

    # Based on Java SDK: OpenItemMainPicVideoApplyRequest

    item_id: int = Field(description="商品ID", alias="itemId")
    video_id: str = Field(description="视频ID", alias="videoId")
    video_type: int = Field(description="视频类型", alias="videoType")

    @property
    def api_method(self) -> str:
        return "open.item.main.pic.video.apply"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemMainPicVideoApplyResponse(BaseResponse[Dict[str, Any]]):
    """商品主图视频申请响应"""

    pass


class ItemMainPicVideoDeleteRequest(BaseRequest):
    """商品主图视频删除请求"""

    # Based on Java SDK: OpenItemMainPicVideoDeleteRequest

    item_id: int = Field(description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.item.main.pic.video.delete"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemMainPicVideoDeleteResponse(BaseResponse[Dict[str, Any]]):
    """商品主图视频删除响应"""

    pass


class ItemShelfStatusUpdateRequest(BaseRequest):
    """商品上下架状态更新请求"""

    # Based on Java SDK: OpenItemShelfStatusUpdateRequest

    kwai_item_id: int = Field(description="快手商品ID", alias="kwaiItemId")
    shelf_status: int = Field(description="上架状态", alias="shelfStatus")

    @property
    def api_method(self) -> str:
        return "open.item.shelf.status.update"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemShelfStatusUpdateResponse(BaseResponse[Dict[str, Any]]):
    """商品上下架状态更新响应"""

    pass


class ItemNewPrecheckRequest(BaseRequest):
    """商品新建预检请求"""

    # Based on Java SDK: OpenItemNewPrecheckRequest

    leaf_category_id: int = Field(description="叶子类目ID", alias="leafCategoryId")

    @property
    def api_method(self) -> str:
        return "open.item.new.precheck"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemNewPrecheckResponse(BaseResponse[Dict[str, Any]]):
    """商品新建预检响应"""

    pass


# ==================== 缺失API模型 - 尺码表管理 ====================


class ItemSizeChartGroupListGetRequest(BaseRequest):
    """获取尺码表分组列表请求"""

    # Java: OpenItemSizeChartGroupListGetRequest -> GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.group.list.get"


class ItemSizeChartGroupListGetResponse(BaseResponse[List[Dict[str, Any]]]):
    """获取尺码表分组列表响应"""

    pass


class SizeChartUnit(BaseModel):
    """尺码表单元定义（Java: SizeChartUnit）"""

    param_name: str = Field(description="参数名", alias="paramName")
    param_type: str = Field(description="参数类型", alias="paramType")
    param_value_list: List[str] = Field(
        description="参数值列表", alias="paramValueList"
    )


class SizeChartUnitList(BaseModel):
    """尺码表行（Java: SizeChartUnitList）"""

    size_chart_unit: List[SizeChartUnit] = Field(
        description="尺码表单元列表", alias="sizeChartUnit"
    )


class SizeChartTable(BaseModel):
    """尺码表数据（Java: SizeChartTable）"""

    header_param: List[str] = Field(description="表头", alias="headerParam")
    size_chart_row: List[SizeChartUnitList] = Field(
        description="数据行", alias="sizeChartRow"
    )


class AddSizeChartParam(BaseModel):
    """添加尺码表参数"""

    name: str = Field(description="尺码表名称")
    template_type_prop_value_id: Optional[int] = Field(
        default=None, description="模板类型属性值ID", alias="templateTypePropValueId"
    )
    group_id: Optional[int] = Field(default=None, description="分组ID", alias="groupId")
    size_chart_note: Optional[str] = Field(
        default=None, description="尺码表说明", alias="sizeChartNote"
    )
    size_chart_table: Optional[SizeChartTable] = Field(
        default=None, description="尺码表数据", alias="sizeChartTable"
    )


class ItemSizeChartTemplateAddRequest(BaseRequest):
    """添加尺码表模板请求"""

    size_chart: AddSizeChartParam = Field(
        description="尺码表模板数据", alias="sizeChart"
    )

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.template.add"


class ItemSizeChartTemplateAddResponse(BaseResponse[Dict[str, Any]]):
    """添加尺码表模板响应"""

    pass


class ItemSizeChartTemplateDeleteRequest(BaseRequest):
    """删除尺码表模板请求"""

    size_chart_id: int = Field(description="尺码表模板ID", alias="sizeChartId")

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.template.delete"


class ItemSizeChartTemplateDeleteResponse(BaseResponse[Dict[str, Any]]):
    """删除尺码表模板响应"""

    pass


class SizeChartParam(BaseModel):
    """尺码表参数"""

    size_chart_id: int = Field(description="尺码表ID", alias="sizeChartId")
    name: str = Field(description="尺码表名称")
    template_type_prop_value_id: Optional[int] = Field(
        default=None, description="模板类型属性值ID", alias="templateTypePropValueId"
    )
    group_id: Optional[int] = Field(default=None, description="分组ID", alias="groupId")
    size_chart_note: Optional[str] = Field(
        default=None, description="尺码表说明", alias="sizeChartNote"
    )
    size_chart_table: Optional[SizeChartTable] = Field(
        default=None, description="尺码表数据", alias="sizeChartTable"
    )


class ItemSizeChartTemplateEditRequest(BaseRequest):
    """编辑尺码表模板请求"""

    size_chart: SizeChartParam = Field(description="尺码表模板数据", alias="sizeChart")

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.template.edit"


class ItemSizeChartTemplateEditResponse(BaseResponse[Dict[str, Any]]):
    """编辑尺码表模板响应"""

    pass


class ItemSizeChartTemplateGetRequest(BaseRequest):
    """获取尺码表模板请求"""

    size_chart_id: int = Field(description="尺码表模板ID", alias="sizeChartId")

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.template.get"


class ItemSizeChartTemplateGetResponse(BaseResponse[Dict[str, Any]]):
    """获取尺码表模板响应"""

    pass


class ItemSizeChartTemplateListGetRequest(BaseRequest):
    """获取尺码表模板列表请求"""

    template_type_prop_value_id: Optional[int] = Field(
        default=None, description="模板类型属性值ID", alias="templateTypePropValueId"
    )
    page_num: Optional[int] = Field(
        default=1, description="页码", ge=1, alias="pageNum"
    )
    page_size: Optional[int] = Field(
        default=20, description="页面大小", ge=1, le=100, alias="pageSize"
    )

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.template.list.get"


class ItemSizeChartTemplateListGetResponse(PagedResponse[Dict[str, Any]]):
    """获取尺码表模板列表响应"""

    pass


class ItemSizeChartTemplateMetaGetRequest(BaseRequest):
    """获取尺码表模板元数据请求"""

    category_id: int = Field(description="类目ID", alias="categoryId")

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET

    @property
    def api_method(self) -> str:
        return "open.item.size.chart.template.meta.get"


class ItemSizeChartTemplateMetaGetResponse(BaseResponse[Dict[str, Any]]):
    """获取尺码表模板元数据响应"""

    pass


# ==================== 缺失API模型 - 其他功能 ====================


class ItemDeletedGetRequest(BaseRequest):
    """获取已删除商品请求"""

    item_id: Optional[int] = Field(default=None, description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.item.deleted.get"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemDeletedGetResponse(BaseResponse[Dict[str, Any]]):
    """获取已删除商品响应"""

    pass


## Note: Duplicate material detail/upload token verify classes removed; see earlier definitions.


class KeyPropOpenApiDTO(BaseModel):
    """关键属性DTO"""

    prop_id: int = Field(description="属性ID")
    prop_value_id: Optional[int] = Field(default=None, description="属性值ID")
    prop_value: Optional[str] = Field(default=None, description="属性值")


class SPUPropOpenApiDTO(BaseModel):
    """SPU属性DTO"""

    prop_id: int = Field(description="属性ID")
    prop_value_id: Optional[int] = Field(default=None, description="属性值ID")
    prop_value: Optional[str] = Field(default=None, description="属性值")


class ItemStandardApplyRequest(BaseRequest):
    """申请商品标准请求"""

    key_prop_list: Optional[List[KeyPropOpenApiDTO]] = Field(
        default=None, description="关键属性列表", alias="keyPropList"
    )
    category_id: int = Field(description="类目ID", alias="categoryId")
    spu_prop_list: Optional[List[SPUPropOpenApiDTO]] = Field(
        default=None, description="SPU属性列表", alias="spuPropList"
    )
    standard_images: Optional[List[str]] = Field(
        default=None, description="标准图片URL列表", alias="standardImages"
    )

    @property
    def api_method(self) -> str:
        return "open.item.standard.apply"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemStandardApplyResponse(BaseResponse[Dict[str, Any]]):
    """申请商品标准响应"""

    pass


class ItemStandardApplyQueryRequest(BaseRequest):
    """查询标准申请状态请求"""

    category_id: Optional[List[int]] = Field(
        default=None, description="类目ID列表", alias="categoryId"
    )
    standard_status: Optional[int] = Field(
        default=None, description="标准状态", alias="standardStatus"
    )
    standard_name: Optional[str] = Field(
        default=None, description="标准名称", alias="standardName"
    )
    apply_type: Optional[int] = Field(
        default=None, description="申请类型", alias="applyType"
    )
    standard_audit_status: Optional[int] = Field(
        default=None, description="标准审核状态", alias="standardAuditStatus"
    )
    limit: Optional[int] = Field(
        default=None, description="限制数量", ge=1, alias="limit"
    )
    cursor: Optional[int] = Field(
        default=None, description="游标", ge=0, alias="cursor"
    )

    @property
    def api_method(self) -> str:
        return "open.item.standard.apply.query"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemStandardApplyQueryResponse(BaseResponse[List[Dict[str, Any]]]):
    """查询标准申请状态响应"""

    pass


class ItemStandardCorrectRequest(BaseRequest):
    """纠正商品标准请求"""

    key_prop_list: Optional[List[KeyPropOpenApiDTO]] = Field(
        default=None, description="关键属性列表", alias="keyPropList"
    )
    category_id: int = Field(description="类目ID", alias="categoryId")
    spu_prop_list: Optional[List[SPUPropOpenApiDTO]] = Field(
        default=None, description="SPU属性列表", alias="spuPropList"
    )
    standard_id: int = Field(description="标准ID", alias="standardId")
    modify_reason: Optional[str] = Field(
        default=None, description="修改原因", alias="modifyReason"
    )
    modify_image_url: Optional[str] = Field(
        default=None, description="修改图片URL", alias="modifyImageUrl"
    )
    standard_images: Optional[List[str]] = Field(
        default=None, description="标准图片URL列表", alias="standardImages"
    )

    @property
    def api_method(self) -> str:
        return "open.item.standard.correct"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemStandardCorrectResponse(BaseResponse[Dict[str, Any]]):
    """纠正商品标准响应"""

    pass


class ItemVideoCaptionEditRequest(BaseRequest):
    """编辑视频字幕请求"""

    video_id: str = Field(description="视频ID", alias="videoId")
    video_type: Optional[int] = Field(
        default=None, description="视频类型", alias="videoType"
    )
    caption: str = Field(description="字幕内容", alias="caption")

    @property
    def api_method(self) -> str:
        return "open.item.video.caption.edit"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemVideoCaptionEditResponse(BaseResponse[Dict[str, Any]]):
    """编辑视频字幕响应"""

    pass


class ItemVideoCountRequest(BaseRequest):
    """获取视频数量请求"""

    video_type: Optional[int] = Field(
        default=None, description="视频类型", alias="videoType"
    )
    aspect_ratio: Optional[int] = Field(
        default=None, description="宽高比", alias="aspectRatio"
    )
    audit_status: Optional[int] = Field(
        default=None, description="审核状态", alias="auditStatus"
    )
    create_time_start: Optional[int] = Field(
        default=None, description="创建开始时间", alias="createTimeStart"
    )
    create_time_end: Optional[int] = Field(
        default=None, description="创建结束时间", alias="createTimeEnd"
    )

    @property
    def api_method(self) -> str:
        return "open.item.video.count"

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ItemVideoCountResponse(BaseResponse[Dict[str, Any]]):
    """获取视频数量响应"""

    total: int = Field(description="视频总数")


class ItemVideoInfoRequest(BaseRequest):
    """获取视频信息请求"""

    video_id: str = Field(description="视频ID", alias="videoId")
    video_type: Optional[int] = Field(
        default=None, description="视频类型", alias="videoType"
    )

    @property
    def api_method(self) -> str:
        return "open.item.video.info"

    # Java: GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ItemVideoInfoResponse(BaseResponse[VideoInfo]):
    """获取视频信息响应"""

    pass


# ==================== 新版发品与编辑（对齐 Java: open.item.new / open.item.edit） ====================


class OpenapiSkuPropMeasureValueProto(BaseModel):
    """SKU规格度量值（Java: OpenapiSkuPropMeasureValueProto）"""

    type: Optional[str] = Field(default=None, description="类型")
    value: Optional[str] = Field(default=None, description="值")
    unit_value_id: Optional[int] = Field(default=None, alias="unitValueId")
    unit_value_name: Optional[str] = Field(default=None, alias="unitValueName")


class OpenapiSkuPropMeasureProto(BaseModel):
    """SKU规格度量（Java: OpenapiSkuPropMeasureProto）"""

    template_id: Optional[int] = Field(default=None, alias="templateId")
    value: Optional[List[OpenapiSkuPropMeasureValueProto]] = Field(default=None)


class OpenApiAddSkuPropDTO(BaseModel):
    """新增SKU属性（Java: OpenApiAddSkuPropDTO）"""

    prop_name: Optional[str] = Field(default=None, alias="propName")
    prop_value_name: Optional[str] = Field(default=None, alias="propValueName")
    image_url: Optional[str] = Field(default=None, alias="imageUrl")
    is_main_prop: Optional[int] = Field(default=None, alias="isMainProp")
    prop_value_group_id: Optional[int] = Field(default=None, alias="propValueGroupId")
    prop_version: Optional[int] = Field(default=None, alias="propVersion")
    prop_sort_num: Optional[int] = Field(default=None, alias="propSortNum")
    prop_value_sort_num: Optional[int] = Field(default=None, alias="propValueSortNum")
    prop_value_remarks: Optional[str] = Field(default=None, alias="propValueRemarks")
    measure_info: Optional[OpenapiSkuPropMeasureProto] = Field(
        default=None, alias="measureInfo"
    )


class MealContentDTO(BaseModel):
    """套餐内容（Java: MealContentDTO）"""

    title: Optional[str] = Field(default=None)
    count: Optional[int] = Field(default=None)
    price: Optional[int] = Field(default=None)


class MealGroupDTO(BaseModel):
    """套餐分组（Java: MealGroupDTO）"""

    title: Optional[str] = Field(default=None)
    meal_content_dto_list: Optional[List[MealContentDTO]] = Field(
        default=None, alias="mealContentDTOList"
    )
    from_num: Optional[int] = Field(default=None, alias="fromNum")
    select_num: Optional[int] = Field(default=None, alias="selectNum")


class MealDetailDTO(BaseModel):
    """套餐详情（Java: MealDetailDTO）"""

    meal_group_dto_list: Optional[List[MealGroupDTO]] = Field(
        default=None, alias="mealGroupDTOList"
    )
    lowest_people_num: Optional[int] = Field(default=None, alias="lowestPeopleNum")
    highest_people_num: Optional[int] = Field(default=None, alias="highestPeopleNum")
    remark: Optional[str] = Field(default=None)


class SkuCertificatePropParam(BaseModel):
    """二手/认证属性（Java: SkuCertificatePropParam）"""

    condition: Optional[str] = Field(default=None)
    purchasing_channels: Optional[str] = Field(default=None, alias="purchasingChannels")
    battery_efficiency: Optional[str] = Field(default=None, alias="batteryEfficiency")
    main_board: Optional[str] = Field(default=None, alias="mainBoard")
    battery_condition: Optional[str] = Field(default=None, alias="batteryCondition")
    screen_condition: Optional[str] = Field(default=None, alias="screenCondition")
    shell_collision: Optional[str] = Field(default=None, alias="shellCollision")
    report_url: Optional[str] = Field(default=None, alias="reportUrl")
    quality_inspection_no: Optional[str] = Field(
        default=None, alias="qualityInspectionNo"
    )
    sn: Optional[str] = Field(default=None)
    shell_scratch: Optional[str] = Field(default=None, alias="shellScratch")
    shell_paint: Optional[str] = Field(default=None, alias="shellPaint")
    device_system: Optional[str] = Field(default=None, alias="deviceSystem")


class OpenApiAutoPassSkuDTO(BaseModel):
    """自动通过编辑SKU（Java: OpenApiAutoPassSkuDTO）"""

    sku_id: Optional[int] = Field(default=None, alias="skuId")
    sku_change_stock: Optional[int] = Field(default=None, alias="skuChangeStock")
    sku_stock_change_type: Optional[int] = Field(
        default=None, alias="skuStockChangeType"
    )
    sku_sale_price: Optional[int] = Field(default=None, alias="skuSalePrice")
    sku_market_price: Optional[int] = Field(default=None, alias="skuMarketPrice")
    sku_nick: Optional[str] = Field(default=None, alias="skuNick")
    rel_sku_id: Optional[int] = Field(default=None, alias="relSkuId")
    sku_certificate_prop_values: Optional[SkuCertificatePropParam] = Field(
        default=None, alias="skuCertificatePropValues"
    )
    gtin_code: Optional[str] = Field(default=None, alias="gtinCode")


class OpenApiAddSkuDTO(BaseModel):
    """新增SKU（Java: OpenApiAddSkuDTO）"""

    rel_sku_id: Optional[int] = Field(default=None, alias="relSkuId")
    sku_stock: Optional[int] = Field(default=None, alias="skuStock")
    sku_sale_price: Optional[int] = Field(default=None, alias="skuSalePrice")
    sku_nick: Optional[str] = Field(default=None, alias="skuNick")
    sku_props: Optional[List[OpenApiAddSkuPropDTO]] = Field(
        default=None, alias="skuProps"
    )
    sku_certificate: Optional[SkuCertificatePropParam] = Field(
        default=None, alias="skuCertificate"
    )
    sku_market_price: Optional[int] = Field(default=None, alias="skuMarketPrice")
    goods_id: Optional[str] = Field(default=None, alias="goodsId")
    gtin_code: Optional[str] = Field(default=None, alias="gtinCode")
    meal_detail: Optional[MealDetailDTO] = Field(default=None, alias="mealDetail")


class OpenApiUpdateSkuDTO(BaseModel):
    """编辑SKU（Java: OpenApiUpdateSkuDTO）"""

    sku_id: Optional[int] = Field(default=None, alias="skuId")
    rel_sku_id: Optional[int] = Field(default=None, alias="relSkuId")
    sku_sale_price: Optional[int] = Field(default=None, alias="skuSalePrice")
    sku_nick: Optional[str] = Field(default=None, alias="skuNick")
    sku_props: Optional[List[OpenApiAddSkuPropDTO]] = Field(
        default=None, alias="skuProps"
    )
    sku_certificate: Optional[SkuCertificatePropParam] = Field(
        default=None, alias="skuCertificate"
    )
    sku_stock_change_type: Optional[int] = Field(
        default=None, alias="skuStockChangeType"
    )
    sku_change_stock: Optional[int] = Field(default=None, alias="skuChangeStock")
    sku_market_price: Optional[int] = Field(default=None, alias="skuMarketPrice")
    gtin_code: Optional[str] = Field(default=None, alias="gtinCode")
    meal_detail: Optional[MealDetailDTO] = Field(default=None, alias="mealDetail")


class CategoryPropValueParam(BaseModel):
    """类目属性值（Java: CategoryPropValueParam）"""

    prop_value_id: Optional[int] = Field(default=None, alias="propValueId")
    prop_value: Optional[str] = Field(default=None, alias="propValue")


class DateRangeParam(BaseModel):
    """时间范围（Java: DateRangeParam）"""

    start_time_timestamp: Optional[int] = Field(
        default=None, alias="startTimeTimestamp"
    )
    end_time_timestamp: Optional[int] = Field(default=None, alias="endTimeTimestamp")


class ItemPropValue(BaseModel):
    """编辑场景的商品属性（Java: ItemPropValue）"""

    prop_id: Optional[int] = Field(default=None, alias="propId")
    radio_prop_value: Optional[CategoryPropValueParam] = Field(
        default=None, alias="radioPropValue"
    )
    check_box_prop_values_list: Optional[List[CategoryPropValueParam]] = Field(
        default=None, alias="checkBoxPropValuesList"
    )
    text_prop_value: Optional[str] = Field(default=None, alias="textPropValue")
    datetime_timestamp: Optional[int] = Field(default=None, alias="datetimeTimestamp")
    date_range: Optional[DateRangeParam] = Field(default=None, alias="dateRange")
    sort_num: Optional[int] = Field(default=None, alias="sortNum")
    image_prop_values: Optional[List[str]] = Field(
        default=None, alias="imagePropValues"
    )
    prop_name: Optional[str] = Field(default=None, alias="propName")
    prop_alias: Optional[str] = Field(default=None, alias="propAlias")
    input_type: Optional[int] = Field(default=None, alias="inputType")
    prop_type: Optional[int] = Field(default=None, alias="propType")
    unit_prop_value_id: Optional[int] = Field(default=None, alias="unitPropValueId")
    unit_prop_value_name: Optional[str] = Field(default=None, alias="unitPropValueName")


class AddItemPropValue(BaseModel):
    """新增场景的商品属性（Java: AddItemPropValue）"""

    prop_id: Optional[int] = Field(default=None, alias="propId")
    radio_prop_value: Optional[CategoryPropValueParam] = Field(
        default=None, alias="radioPropValue"
    )
    check_box_prop_values_list: Optional[List[CategoryPropValueParam]] = Field(
        default=None, alias="checkBoxPropValuesList"
    )
    text_prop_value: Optional[str] = Field(default=None, alias="textPropValue")
    datetime_timestamp: Optional[int] = Field(default=None, alias="datetimeTimestamp")
    date_range: Optional[DateRangeParam] = Field(default=None, alias="dateRange")
    sort_num: Optional[int] = Field(default=None, alias="sortNum")
    image_prop_values: Optional[List[str]] = Field(
        default=None, alias="imagePropValues"
    )
    prop_name: Optional[str] = Field(default=None, alias="propName")
    prop_alias: Optional[str] = Field(default=None, alias="propAlias")
    input_type: Optional[int] = Field(default=None, alias="inputType")
    prop_type: Optional[int] = Field(default=None, alias="propType")
    unit_prop_value_id: Optional[int] = Field(default=None, alias="unitPropValueId")
    unit_prop_value_name: Optional[str] = Field(default=None, alias="unitPropValueName")


class QualificationDataDTO(BaseModel):
    """资质数据（Java: QualificationDataDTO）"""

    meta_id: Optional[int] = Field(default=None, alias="metaId")
    existed_qualification_data_id: Optional[int] = Field(
        default=None, alias="existedQualificationDataId"
    )
    prop: Optional[List[AddItemPropValue]] = Field(default=None)


class OpenApiTimeRange(BaseModel):
    """不可售时间段（Java: OpenApiTimeRange）"""

    start_time: Optional[int] = Field(default=None, alias="startTime")
    end_time: Optional[int] = Field(default=None, alias="endTime")


class OpenApiUnavailableTimeRule(BaseModel):
    """不可售时间规则（Java: OpenApiUnavailableTimeRule）"""

    weeks: Optional[List[int]] = Field(default=None)
    holidays: Optional[List[int]] = Field(default=None)
    time_ranges: Optional[List[OpenApiTimeRange]] = Field(
        default=None, alias="timeRanges"
    )


class OpenApiServicePromise(BaseModel):
    """服务承诺（Java: OpenApiServicePromise）"""

    fresh_rot_refund: Optional[bool] = Field(default=None, alias="freshRotRefund")
    broken_refund: Optional[bool] = Field(default=None, alias="brokenRefund")
    allergy_refund: Optional[bool] = Field(default=None, alias="allergyRefund")
    crab_refund: Optional[bool] = Field(default=None, alias="crabRefund")
    weight_guarantee: Optional[bool] = Field(default=None, alias="weightGuarantee")


class CustomerInfo(BaseModel):
    """客户信息（Java: CustomerInfo）"""

    customer_info_type: Optional[str] = Field(default=None, alias="customerInfoType")
    customer_certificate_type: Optional[List[str]] = Field(
        default=None, alias="customerCertificateType"
    )


class ServiceRule(BaseModel):
    """服务规则（Java: ServiceRule）"""

    refund_rule: Optional[str] = Field(default=None, alias="refundRule")
    deliver_goods_interal_time: Optional[int] = Field(
        default=None, alias="deliverGoodsInteralTime"
    )
    promise_delivery_time: Optional[int] = Field(
        default=None, alias="promiseDeliveryTime"
    )
    immediately_on_offline_flag: Optional[int] = Field(
        default=None, alias="immediatelyOnOfflineFlag"
    )
    delivery_method: Optional[str] = Field(default=None, alias="deliveryMethod")
    service_promise: Optional[OpenApiServicePromise] = Field(
        default=None, alias="servicePromise"
    )
    unavailable_time_rule: Optional[OpenApiUnavailableTimeRule] = Field(
        default=None, alias="unavailableTimeRule"
    )
    cert_merchant_code: Optional[str] = Field(default=None, alias="certMerchantCode")
    cert_expire_type: Optional[int] = Field(default=None, alias="certExpireType")
    cert_start_time: Optional[int] = Field(default=None, alias="certStartTime")
    cert_end_time: Optional[int] = Field(default=None, alias="certEndTime")
    cert_exp_days: Optional[int] = Field(default=None, alias="certExpDays")
    order_purchase_limit_type: Optional[int] = Field(
        default=None, alias="orderPurchaseLimitType"
    )
    min_order_count: Optional[int] = Field(default=None, alias="minOrderCount")
    max_order_count: Optional[int] = Field(default=None, alias="maxOrderCount")
    customer_info: Optional[CustomerInfo] = Field(default=None, alias="customerInfo")
    price_protect_days: Optional[int] = Field(default=None, alias="priceProtectDays")
    delivery_time_mode: Optional[str] = Field(default=None, alias="deliveryTimeMode")


class ItemVideoProto(BaseModel):
    """商品视频（Java: ItemVideoProto）"""

    video_id: Optional[str] = Field(default=None, alias="videoId")
    video_type: Optional[int] = Field(default=None, alias="videoType")


class ItemNewRequest(BaseRequest):
    """新建商品（对齐 Java: open.item.new）"""

    title: Optional[str] = Field(default=None, alias="title")
    rel_item_id: Optional[int] = Field(default=None, alias="relItemId")
    category_id: Optional[int] = Field(default=None, alias="categoryId")
    image_urls: Optional[List[str]] = Field(default=None, alias="imageUrls")
    sku_list: Optional[List[OpenApiAddSkuDTO]] = Field(default=None, alias="skuList")
    purchase_limit: Optional[bool] = Field(default=None, alias="purchaseLimit")
    limit_count: Optional[int] = Field(default=None, alias="limitCount")
    item_prop_values: Optional[List[AddItemPropValue]] = Field(
        default=None, alias="itemPropValues"
    )
    details: Optional[str] = Field(default=None, alias="details")
    detail_image_urls: Optional[List[str]] = Field(
        default=None, alias="detailImageUrls"
    )
    stock_partner: Optional[bool] = Field(default=None, alias="stockPartner")
    item_remark: Optional[str] = Field(default=None, alias="itemRemark")
    service_rule: Optional[ServiceRule] = Field(default=None, alias="serviceRule")
    express_template_id: Optional[int] = Field(default=None, alias="expressTemplateId")
    sale_time_flag: Optional[bool] = Field(default=None, alias="saleTimeFlag")
    time_of_sale: Optional[int] = Field(default=None, alias="timeOfSale")
    pay_way: Optional[int] = Field(default=None, alias="payWay")
    multiple_stock: Optional[bool] = Field(default=None, alias="multipleStock")
    poi_ids: Optional[List[int]] = Field(default=None, alias="poiIds")
    white_base_image_url: Optional[str] = Field(default=None, alias="whiteBaseImageUrl")
    transparent_image_url: Optional[str] = Field(
        default=None, alias="transparentImageUrl"
    )
    short_title: Optional[str] = Field(default=None, alias="shortTitle")
    selling_point: Optional[str] = Field(default=None, alias="sellingPoint")
    instructions: Optional[str] = Field(default=None, alias="instructions")
    save_shelf_item_qualification_data: Optional[List[QualificationDataDTO]] = Field(
        default=None, alias="saveShelfItemQualificationData"
    )
    off_shore_mode: Optional[int] = Field(default=None, alias="offShoreMode")
    spu_id: Optional[int] = Field(default=None, alias="spuId")
    item_video_id: Optional[str] = Field(default=None, alias="itemVideoId")
    three_quarters_image_urls: Optional[List[str]] = Field(
        default=None, alias="threeQuartersImageUrls"
    )
    item_video: Optional[ItemVideoProto] = Field(default=None, alias="itemVideo")
    size_chart_template_id: Optional[int] = Field(
        default=None, alias="sizeChartTemplateId"
    )

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    @property
    def api_method(self) -> str:
        return "open.item.new"


class ItemNewResponse(BaseResponse[Dict[str, Any]]):
    """新建商品响应"""

    pass


class ItemEditRequest(BaseRequest):
    """编辑商品（对齐 Java: open.item.edit）"""

    item_id: Optional[int] = Field(default=None, alias="itemId")
    title: Optional[str] = Field(default=None, alias="title")
    category_id: Optional[int] = Field(default=None, alias="categoryId")
    image_urls: Optional[List[str]] = Field(default=None, alias="imageUrls")
    sku_list: Optional[List[OpenApiUpdateSkuDTO]] = Field(default=None, alias="skuList")
    item_video_id: Optional[str] = Field(default=None, alias="itemVideoId")
    purchase_limit: Optional[bool] = Field(default=None, alias="purchaseLimit")
    limit_count: Optional[int] = Field(default=None, alias="limitCount")
    item_prop_values: Optional[List[ItemPropValue]] = Field(
        default=None, alias="itemPropValues"
    )
    details: Optional[str] = Field(default=None, alias="details")
    detail_image_urls: Optional[List[str]] = Field(
        default=None, alias="detailImageUrls"
    )
    update_detail_image_urls: Optional[bool] = Field(
        default=None, alias="updateDetailImageUrls"
    )
    item_remark: Optional[str] = Field(default=None, alias="itemRemark")
    service_rule: Optional[ServiceRule] = Field(default=None, alias="serviceRule")
    express_template_id: Optional[int] = Field(default=None, alias="expressTemplateId")
    sale_time_flag: Optional[bool] = Field(default=None, alias="saleTimeFlag")
    time_of_sale: Optional[int] = Field(default=None, alias="timeOfSale")
    pay_way: Optional[int] = Field(default=None, alias="payWay")
    update_item_prop_values: Optional[bool] = Field(
        default=None, alias="updateItemPropValues"
    )
    poi_ids: Optional[List[int]] = Field(default=None, alias="poiIds")
    white_base_image_url: Optional[str] = Field(default=None, alias="whiteBaseImageUrl")
    transparent_image_url: Optional[str] = Field(
        default=None, alias="transparentImageUrl"
    )
    short_title: Optional[str] = Field(default=None, alias="shortTitle")
    selling_point: Optional[str] = Field(default=None, alias="sellingPoint")
    instructions: Optional[str] = Field(default=None, alias="instructions")
    save_shelf_item_qualification_data: Optional[List[QualificationDataDTO]] = Field(
        default=None, alias="saveShelfItemQualificationData"
    )
    update_item_qualification: Optional[bool] = Field(
        default=None, alias="updateItemQualification"
    )
    spu_id: Optional[int] = Field(default=None, alias="spuId")
    update_three_quarters_image_urls: Optional[bool] = Field(
        default=None, alias="updateThreeQuartersImageUrls"
    )
    three_quarters_image_urls: Optional[List[str]] = Field(
        default=None, alias="threeQuartersImageUrls"
    )
    item_video: Optional[ItemVideoProto] = Field(default=None, alias="itemVideo")
    size_chart_template_id: Optional[int] = Field(
        default=None, alias="sizeChartTemplateId"
    )

    # Java: POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST

    @property
    def api_method(self) -> str:
        return "open.item.edit"


class ItemEditResponse(BaseResponse[Dict[str, Any]]):
    """编辑商品响应"""

    pass
