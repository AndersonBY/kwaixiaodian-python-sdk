"""供应链服务相关数据模型
基于 Java SDK 参考实现，提供供应链商品同步功能。
"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== 供应链商品同步相关 ====================


class SupplySeller(BaseModel):
    """供应链商家信息"""

    name: Optional[str] = Field(default=None, description="商家名称")
    platform_name: Optional[str] = Field(
        default=None, description="平台名称", alias="platformName"
    )
    platform: Optional[int] = Field(default=None, description="平台类型")


class SupplyRight(BaseModel):
    """供应链商品权益信息"""

    name: Optional[str] = Field(default=None, description="权益名称")
    value: Optional[str] = Field(default=None, description="权益值")


class SupplySkuProp(BaseModel):
    """供应链SKU属性"""

    prop_name: Optional[str] = Field(
        default=None, description="属性名称", alias="propName"
    )
    prop_value_name: Optional[str] = Field(
        default=None, description="属性值名称", alias="propValueName"
    )


class SupplySku(BaseModel):
    """供应链SKU信息"""

    image_url: Optional[str] = Field(
        default=None, description="SKU图片", alias="imageUrl"
    )
    price: Optional[int] = Field(default=None, description="SKU价格（分）")
    sku_id: Optional[str] = Field(default=None, description="SKU ID", alias="skuId")
    change_type: Optional[int] = Field(
        default=None, description="库存变更类型", alias="changeType"
    )
    sku_change_stock: Optional[int] = Field(
        default=None, description="库存变更数量", alias="skuChangeStock"
    )
    desc: Optional[str] = Field(default=None, description="SKU描述")
    props: Optional[List[SupplySkuProp]] = Field(
        default=None, description="SKU属性列表"
    )


class SupplyItemProp(BaseModel):
    """供应链商品属性"""

    prop_name: Optional[str] = Field(
        default=None, description="属性名称", alias="propName"
    )
    text_prop_value: Optional[str] = Field(
        default=None, description="属性值文本", alias="textPropValue"
    )
    input_type: Optional[int] = Field(
        default=None, description="输入类型", alias="inputType"
    )


class SupplyItemServiceRule(BaseModel):
    """供应链商品服务规则"""

    promise_delivery_time: Optional[int] = Field(
        default=None, description="承诺发货时间", alias="promiseDeliveryTime"
    )


class SupplyItemPerformance(BaseModel):
    """供应链商品履约表现"""

    dist_order_num: Optional[int] = Field(
        default=None, description="分销订单数", alias="distOrderNum"
    )
    pickup_rate_24h: Optional[float] = Field(
        default=None, description="24小时揽收率", alias="pickupRate24h"
    )
    pickup_rate_48h: Optional[float] = Field(
        default=None, description="48小时揽收率", alias="pickupRate48h"
    )
    add_item_seller_num: Optional[int] = Field(
        default=None, description="新增商品商家数", alias="addItemSellerNum"
    )
    return_rate: Optional[float] = Field(
        default=None, description="退货率", alias="returnRate"
    )
    delivery_rate_48h: Optional[float] = Field(
        default=None, description="48小时发货率", alias="deliveryRate48h"
    )


class SupplyPerformance1688(BaseModel):
    """供应链 1688 表现信息"""

    no_reason_7d_return: Optional[bool] = Field(
        default=None, description="是否支持7天无理由退货", alias="noReason7dReturn"
    )
    ks_is_zc_hot: Optional[bool] = Field(
        default=None, description="是否中长爆品", alias="ksIsZcHot"
    )
    ship_speed: Optional[str] = Field(
        default=None, description="发货速度", alias="shipSpeed"
    )
    power_merchant: Optional[bool] = Field(
        default=None, description="是否实力商家", alias="powerMerchant"
    )
    tp_years: Optional[int] = Field(
        default=None, description="平台年限", alias="tpYears"
    )
    ks_repeat_rate_30d: Optional[float] = Field(
        default=None, description="30天复购率", alias="ksRepeatRate30d"
    )
    has_xchf: Optional[bool] = Field(
        default=None, description="是否有先拆后付", alias="hasXchf"
    )
    ks_slr_mord_7d: Optional[str] = Field(
        default=None, description="7天日均销量", alias="ksSlrMord7d"
    )
    ks_is_hj_hot: Optional[bool] = Field(
        default=None, description="是否焕新热卖", alias="ksIsHjHot"
    )
    ks_is_zb_hot: Optional[bool] = Field(
        default=None, description="是否直播爆品", alias="ksIsZbHot"
    )
    ks_slr_mord_30d: Optional[str] = Field(
        default=None, description="30天日均销量", alias="ksSlrMord30d"
    )
    pm_plus: Optional[bool] = Field(
        default=None, description="是否PMPLUS", alias="pmPlus"
    )
    ks_is_db_hot: Optional[bool] = Field(
        default=None, description="是否短播爆品", alias="ksIsDbHot"
    )
    electronic_list_no: Optional[bool] = Field(
        default=None, description="是否电子面单", alias="electronicListNo"
    )


class SupplyItem(BaseModel):
    """供应链商品信息"""

    seller: Optional[SupplySeller] = Field(default=None, description="供应商信息")
    skus: Optional[List[SupplySku]] = Field(default=None, description="SKU 列表")
    description: Optional[str] = Field(default=None, description="商品描述")
    title: Optional[str] = Field(default=None, description="商品标题")
    price_min: Optional[int] = Field(
        default=None, description="最低价（分）", alias="priceMin"
    )
    scene: Optional[int] = Field(default=None, description="场景类型")
    white_base_image_url: Optional[str] = Field(
        default=None, description="白底图地址", alias="whiteBaseImageUrl"
    )
    category_id: Optional[int] = Field(
        default=None, description="类目ID", alias="categoryId"
    )
    rights: Optional[List[SupplyRight]] = Field(
        default=None, description="权益信息列表"
    )
    is_fuli: Optional[bool] = Field(
        default=None, description="是否福利商品", alias="isFuli"
    )
    is_fuchi: Optional[bool] = Field(
        default=None, description="是否福吃商品", alias="isFuchi"
    )
    upload_method: Optional[int] = Field(
        default=None, description="上传方式", alias="uploadMethod"
    )
    images: Optional[List[str]] = Field(default=None, description="主图列表")
    rights_v2: Optional[List[int]] = Field(
        default=None, description="权益V2列表", alias="rightsV2"
    )
    item_id: Optional[str] = Field(default=None, description="商品ID", alias="itemId")
    image_url: Optional[str] = Field(
        default=None, description="主图URL", alias="imageUrl"
    )
    origin_item_url: Optional[str] = Field(
        default=None, description="原商品链接", alias="originItemUrl"
    )
    props: Optional[List[SupplyItemProp]] = Field(
        default=None, description="商品属性列表"
    )
    detail_images: Optional[List[str]] = Field(
        default=None, description="详情图列表", alias="detailImages"
    )
    service_rule: Optional[SupplyItemServiceRule] = Field(
        default=None, description="服务规则", alias="serviceRule"
    )
    performance: Optional[SupplyItemPerformance] = Field(
        default=None, description="履约表现"
    )
    extra_info: Optional[Dict[str, Any]] = Field(
        default=None, description="额外信息", alias="extraInfo"
    )
    three_quarters_image_urls: Optional[List[str]] = Field(
        default=None, description="三分之四视角图", alias="threeQuartersImageUrls"
    )
    service_desc: Optional[List[str]] = Field(
        default=None, description="服务描述", alias="serviceDesc"
    )
    performance1688: Optional[SupplyPerformance1688] = Field(
        default=None, description="1688 表现信息"
    )
    service_types: Optional[List[int]] = Field(
        default=None, description="服务类型列表", alias="serviceTypes"
    )
    kwai_item_id: Optional[int] = Field(
        default=None, description="快手商品ID", alias="kwaiItemId"
    )
    price_max: Optional[int] = Field(
        default=None, description="最高价（分）", alias="priceMax"
    )


class SupplyItemSyncParam(BaseModel):
    """供应链商品同步参数"""

    item: SupplyItem = Field(..., description="商品信息")


class SupplyItemSyncRequest(BaseRequest):
    """供应链商品同步请求
    API: open.supply.item.sync (POST)
    """

    param: SupplyItemSyncParam = Field(..., description="同步参数")

    @property
    def api_method(self) -> str:
        return "open.supply.item.sync"

    # 使用常量 HTTP 方法以对齐全局约定
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SupplyItemSyncResponse(BaseResponse[Dict[str, Any]]):
    """供应链商品同步响应"""

    pass
