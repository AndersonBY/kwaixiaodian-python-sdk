"""物流相关数据模型（严格对齐 Java SDK）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod


class LogisticsCompany(BaseModel):
    """物流公司信息"""

    company_code: str = Field(description="物流公司编码")
    company_name: str = Field(description="物流公司名称")
    support_track: Optional[bool] = Field(default=None, description="是否支持轨迹查询")
    support_cod: Optional[bool] = Field(default=None, description="是否支持货到付款")


class TrackingEvent(BaseModel):
    """物流跟踪事件"""

    time: str = Field(description="事件时间")
    desc: str = Field(description="事件描述")
    location: Optional[str] = Field(default=None, description="所在地点")
    status: Optional[str] = Field(default=None, description="状态")


class TrackingInfo(BaseModel):
    """物流跟踪信息"""

    logistics_company: str = Field(description="物流公司编码")
    logistics_company_name: Optional[str] = Field(
        default=None, description="物流公司名称"
    )
    tracking_number: str = Field(description="运单号")
    status: Optional[str] = Field(default=None, description="物流状态")
    events: List[TrackingEvent] = Field(
        default_factory=lambda: [], description="物流轨迹事件列表"
    )


class FreightRule(BaseModel):
    """运费计算规则"""

    first_weight: Optional[int] = Field(default=None, description="首重（克）")
    first_price: Optional[int] = Field(default=None, description="首重价格（分）")
    additional_weight: Optional[int] = Field(default=None, description="续重（克）")
    additional_price: Optional[int] = Field(default=None, description="续重价格（分）")
    free_threshold: Optional[int] = Field(
        default=None, description="包邮门槛金额（分）"
    )

    @property
    def first_price_yuan(self) -> Optional[float]:
        """首重价格（元）"""
        if self.first_price is not None:
            return self.first_price / 100
        return None

    @property
    def additional_price_yuan(self) -> Optional[float]:
        """续重价格（元）"""
        if self.additional_price is not None:
            return self.additional_price / 100
        return None

    @property
    def free_threshold_yuan(self) -> Optional[float]:
        """包邮门槛（元）"""
        if self.free_threshold is not None:
            return self.free_threshold / 100
        return None


class FreightTemplate(BaseModel):
    """运费模板"""

    template_id: Optional[int] = Field(default=None, description="模板ID")
    template_name: str = Field(description="模板名称")
    charge_type: int = Field(description="计费方式：1-按重量，2-按件数")
    delivery_type: int = Field(description="配送类型：1-快递，2-物流")
    is_free_shipping: Optional[bool] = Field(default=None, description="是否包邮")
    rules: List[FreightRule] = Field(
        default_factory=lambda: [], description="运费规则列表"
    )
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")


class FreightCalculation(BaseModel):
    """运费计算结果"""

    freight_amount: int = Field(description="运费金额（分）")
    is_free_shipping: bool = Field(description="是否包邮")
    template_id: Optional[int] = Field(default=None, description="使用的模板ID")
    calculation_details: Optional[Dict[str, Any]] = Field(
        default=None, description="计算详情"
    )

    @property
    def freight_yuan(self) -> float:
        """运费（元）"""
        return self.freight_amount / 100


## 注：open.logistics.company.list 与 open.logistics.track 未在 Java 参考中提供，已移除。


# ==================== 运费模板相关（使用 Express 模板接口，对齐 Java 参考） ====================


## 注：open.logistics.calculate.freight 未在 Java 参考中提供，已移除。


# ==================== 地址管理相关 ====================


class District(BaseModel):
    """地区信息"""

    id: int = Field(description="地区ID")
    name: str = Field(description="地区名称")
    parent_id: Optional[int] = Field(default=None, description="父级ID")
    level: Optional[int] = Field(default=None, description="层级：1-省，2-市，3-区县")


class SellerAddress(BaseModel):
    """商家地址信息"""

    address_id: Optional[int] = Field(default=None, description="地址ID")
    name: str = Field(description="联系人姓名")
    phone: str = Field(description="联系电话")
    province_id: int = Field(description="省份ID")
    city_id: int = Field(description="城市ID")
    county_id: int = Field(description="区县ID")
    detail_address: str = Field(description="详细地址")
    zip_code: Optional[str] = Field(default=None, description="邮编")
    is_default: Optional[bool] = Field(default=None, description="是否默认地址")
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")

    @property
    def full_address(self) -> str:
        """完整地址"""
        return f"{self.detail_address}"


class DistrictListRequest(BaseRequest):
    """地区列表查询请求（open.address.district.list, GET）"""

    district_version: Optional[str] = Field(
        default=None, description="地区版本号", alias="districtVersion"
    )

    @property
    def api_method(self) -> str:
        return "open.address.district.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class DistrictListResponse(BaseResponse[List[District]]):
    """地区列表响应"""

    pass


class BaseAddressInfo(BaseModel):
    """基础地址信息（Java: BaseAddressInfo）"""

    consignee: str = Field(description="收件人")
    mobile: str = Field(description="手机号")
    province_code: int = Field(description="省代码", alias="provinceCode")
    province: str = Field(description="省名称")
    city_code: int = Field(description="市代码", alias="cityCode")
    city: str = Field(description="市名称")
    district_code: int = Field(description="区县代码", alias="districtCode")
    district: str = Field(description="区县名称")
    address: str = Field(description="详细地址")
    town: Optional[str] = Field(default=None, description="乡镇")
    town_code: Optional[int] = Field(
        default=None, description="乡镇代码", alias="townCode"
    )
    address_meta_version: Optional[int] = Field(
        default=None, description="地址元版本", alias="addressMetaVersion"
    )


class SellerAddressCreateRequest(BaseRequest):
    """创建商家地址请求（open.address.seller.create, GET）"""

    base_info: BaseAddressInfo = Field(description="基础地址信息", alias="baseInfo")
    default_address: Optional[bool] = Field(
        default=None, description="是否默认地址", alias="defaultAddress"
    )
    address_type: Optional[int] = Field(
        default=None, description="地址类型", alias="addressType"
    )

    @property
    def api_method(self) -> str:
        return "open.address.seller.create"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerAddressCreateResponse(BaseResponse[Dict[str, Any]]):
    """创建商家地址响应"""

    pass


class SellerAddressListRequest(BaseRequest):
    """商家地址列表查询请求（open.address.seller.list, GET）"""

    address_type: Optional[int] = Field(
        default=None, description="地址类型", alias="addressType"
    )

    @property
    def api_method(self) -> str:
        return "open.address.seller.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerAddressListResponse(BaseResponse[List[SellerAddress]]):
    """商家地址列表响应"""

    pass


class SellerAddressGetRequest(BaseRequest):
    """商家地址详情查询请求（open.address.seller.get, GET）"""

    address_id: int = Field(description="地址ID", alias="addressId")

    @property
    def api_method(self) -> str:
        return "open.address.seller.get"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerAddressGetResponse(BaseResponse[SellerAddress]):
    """商家地址详情响应"""

    pass


class SellerAddressUpdateRequest(BaseRequest):
    """更新商家地址请求（open.address.seller.update, GET）"""

    base_info: BaseAddressInfo = Field(description="基础地址信息", alias="baseInfo")
    default_address: Optional[bool] = Field(
        default=None, description="是否默认地址", alias="defaultAddress"
    )
    address_id: int = Field(description="地址ID", alias="addressId")

    @property
    def api_method(self) -> str:
        return "open.address.seller.update"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerAddressUpdateResponse(BaseResponse[Dict[str, Any]]):
    """更新商家地址响应"""

    pass


class SellerAddressDeleteRequest(BaseRequest):
    """删除商家地址请求（open.address.seller.delete, GET）"""

    address_id: int = Field(description="地址ID", alias="addressId")

    @property
    def api_method(self) -> str:
        return "open.address.seller.delete"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerAddressDeleteResponse(BaseResponse[Dict[str, Any]]):
    """删除商家地址响应"""

    pass


# ==================== 电子面单与订阅（严格对齐 Java） ====================


class ExpressSubscribeQueryRequest(BaseRequest):
    """查询快递订阅状态请求（open.express.subscribe.query, POST）"""

    express_company_code: str = Field(alias="expressCompanyCode")

    @property
    def api_method(self) -> str:
        return "open.express.subscribe.query"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressSubscribeQueryResponse(BaseResponse[Dict[str, Any]]):
    """查询快递订阅状态响应"""

    pass


class ExpressEbillGetRequest(BaseRequest):
    """获取电子面单信息请求（open.express.ebill.get, POST）"""

    get_ebill_order_request: List["GetEbillOrderRequest"] = Field(
        alias="getEbillOrderRequest"
    )

    @property
    def api_method(self) -> str:
        return "open.express.ebill.get"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressEbillGetResponse(BaseResponse[Dict[str, Any]]):
    """获取电子面单信息响应"""

    pass


class ExpressEbillCancelRequest(BaseRequest):
    """取消电子面单请求（open.express.ebill.cancel, POST）"""

    express_company_code: str = Field(alias="expressCompanyCode")
    waybill_code: str = Field(alias="waybillCode")

    @property
    def api_method(self) -> str:
        return "open.express.ebill.cancel"

    # 固定使用 GET（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ExpressEbillCancelResponse(BaseResponse[Dict[str, Any]]):
    """取消电子面单响应"""

    pass


class ExpressEbillUpdateRequest(BaseRequest):
    """更新电子面单信息请求（open.express.ebill.update, POST）"""

    goods_description: Optional[str] = Field(default=None, alias="goodsDescription")
    packaging_description: Optional[str] = Field(
        default=None, alias="packagingDescription"
    )
    total_package_length: Optional[float] = Field(
        default=None, alias="totalPackageLength"
    )
    item_list: Optional[List["ItemDTO"]] = Field(default=None, alias="itemList")
    ext_data: Optional[str] = Field(default=None, alias="extData")
    receiver_contract: Optional["Contract"] = Field(
        default=None, alias="receiverContract"
    )
    sender_contract: Optional["Contract"] = Field(default=None, alias="senderContract")
    express_company_code: Optional[str] = Field(
        default=None, alias="expressCompanyCode"
    )
    total_package_width: Optional[float] = Field(
        default=None, alias="totalPackageWidth"
    )
    total_package_weight: Optional[float] = Field(
        default=None, alias="totalPackageWeight"
    )
    trade_order_remark: Optional[str] = Field(default=None, alias="tradeOrderRemark")
    total_package_volume: Optional[float] = Field(
        default=None, alias="totalPackageVolume"
    )
    total_package_height: Optional[float] = Field(
        default=None, alias="totalPackageHeight"
    )
    receiver_address: Optional["AddressDTO"] = Field(
        default=None, alias="receiverAddress"
    )
    waybill_code: Optional[str] = Field(default=None, alias="waybillCode")

    @property
    def api_method(self) -> str:
        return "open.express.ebill.update"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressEbillUpdateResponse(BaseResponse[Dict[str, Any]]):
    """更新电子面单信息响应"""

    pass


class ExpressEbillAppendRequest(BaseRequest):
    """电子面单追加包裹请求（open.express.ebill.append, POST）"""

    parent_waybill_code: str = Field(alias="parentWaybillCode")
    express_company_code: str = Field(alias="expressCompanyCode")
    add_package_quantity: int = Field(alias="addPackageQuantity", ge=1)

    @property
    def api_method(self) -> str:
        return "open.express.ebill.append"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressEbillAppendResponse(BaseResponse[Dict[str, Any]]):
    """电子面单追加包裹响应"""

    pass


# ==================== 快递服务查询相关 ====================


class ExpressReachable(BaseModel):
    """快递可达性信息"""

    logistics_company: str = Field(description="物流公司编码")
    province_id: int = Field(description="省份ID")
    city_id: Optional[int] = Field(default=None, description="城市ID")
    county_id: Optional[int] = Field(default=None, description="区县ID")
    is_reachable: bool = Field(description="是否可达")
    service_type: Optional[str] = Field(default=None, description="服务类型")


class AddressDTO(BaseModel):
    """地址数据（Java: AddressDTO）"""

    province_name: Optional[str] = Field(default=None, alias="provinceName")
    province_code: Optional[int] = Field(default=None, alias="provinceCode")
    city_name: Optional[str] = Field(default=None, alias="cityName")
    city_code: Optional[int] = Field(default=None, alias="cityCode")
    district_name: Optional[str] = Field(default=None, alias="districtName")
    district_code: Optional[int] = Field(default=None, alias="districtCode")
    town_name: Optional[str] = Field(default=None, alias="townName")
    town_code: Optional[int] = Field(default=None, alias="townCode")
    detail_address: Optional[str] = Field(default=None, alias="detailAddress")


class ExpressServiceDTO(BaseModel):
    """快递服务项（Java: ExpressServiceDTO）"""

    service_code: Optional[str] = Field(default=None, alias="serviceCode")
    service_value: Optional[str] = Field(default=None, alias="serviceValue")


class Contract(BaseModel):
    """联系人信息（Java: Contract）"""

    name: Optional[str] = Field(default=None, alias="name")
    mobile: Optional[str] = Field(default=None, alias="mobile")
    telephone: Optional[str] = Field(default=None, alias="telephone")


class ItemDTO(BaseModel):
    """货品信息（Java: ItemDTO）"""

    item_length: Optional[float] = Field(default=None, alias="itemLength")
    item_width: Optional[float] = Field(default=None, alias="itemWidth")
    item_height: Optional[float] = Field(default=None, alias="itemHeight")
    item_weight: Optional[float] = Field(default=None, alias="itemWeight")
    item_specs: Optional[str] = Field(default=None, alias="itemSpecs")
    item_volume: Optional[float] = Field(default=None, alias="itemVolume")
    item_title: Optional[str] = Field(default=None, alias="itemTitle")
    item_quantity: Optional[int] = Field(default=None, alias="itemQuantity")


class WarehouseDTO(BaseModel):
    """仓库信息（Java: WarehouseDTO）"""

    consign_type: Optional[int] = Field(default=None, alias="consignType")
    warehouse_order_id: Optional[str] = Field(default=None, alias="warehouseOrderId")
    warehouse_code: Optional[str] = Field(default=None, alias="warehouseCode")
    warehouse_name: Optional[str] = Field(default=None, alias="warehouseName")
    consign_net_site_code: Optional[str] = Field(
        default=None, alias="consignNetSiteCode"
    )
    secret_key: Optional[str] = Field(default=None, alias="secretKey")


class GetEbillOrderRequest(BaseModel):
    """电子面单下单请求项（Java: GetEbillOrderRequest）"""

    merchant_code: Optional[str] = Field(default=None, alias="merchantCode")
    merchant_name: Optional[str] = Field(default=None, alias="merchantName")
    total_package_quantity: Optional[int] = Field(
        default=None, alias="totalPackageQuantity"
    )
    goods_description: Optional[str] = Field(default=None, alias="goodsDescription")
    packaging_description: Optional[str] = Field(
        default=None, alias="packagingDescription"
    )
    total_package_length: Optional[float] = Field(
        default=None, alias="totalPackageLength"
    )
    package_code: Optional[str] = Field(default=None, alias="packageCode")
    express_product_code: Optional[str] = Field(
        default=None, alias="expressProductCode"
    )
    item_list: Optional[List[ItemDTO]] = Field(default=None, alias="itemList")
    ext_data: Optional[str] = Field(default=None, alias="extData")
    receiver_contract: Optional[Contract] = Field(
        default=None, alias="receiverContract"
    )
    sender_contract: Optional[Contract] = Field(default=None, alias="senderContract")
    has_freight_insurance: Optional[bool] = Field(
        default=None, alias="hasFreightInsurance"
    )
    net_site_code: Optional[str] = Field(default=None, alias="netSiteCode")
    net_site_name: Optional[str] = Field(default=None, alias="netSiteName")
    express_company_code: Optional[str] = Field(
        default=None, alias="expressCompanyCode"
    )
    order_channel: Optional[str] = Field(default=None, alias="orderChannel")
    pod_model_address: Optional[AddressDTO] = Field(
        default=None, alias="podModelAddress"
    )
    total_package_width: Optional[float] = Field(
        default=None, alias="totalPackageWidth"
    )
    total_package_weight: Optional[float] = Field(
        default=None, alias="totalPackageWeight"
    )
    trade_order_remark: Optional[str] = Field(default=None, alias="tradeOrderRemark")
    total_package_volume: Optional[float] = Field(
        default=None, alias="totalPackageVolume"
    )
    is_sign_back: Optional[bool] = Field(default=None, alias="isSignBack")
    pay_amount: Optional[int] = Field(default=None, alias="payAmount")
    pay_method: Optional[int] = Field(default=None, alias="payMethod")
    total_package_height: Optional[float] = Field(
        default=None, alias="totalPackageHeight"
    )
    trade_order_code: Optional[str] = Field(default=None, alias="tradeOrderCode")
    sender_address: Optional[AddressDTO] = Field(default=None, alias="senderAddress")
    template_url: Optional[str] = Field(default=None, alias="templateUrl")
    reserve_time: Optional[int] = Field(default=None, alias="reserveTime")
    reserve_end_time: Optional[int] = Field(default=None, alias="reserveEndTime")
    receiver_address: Optional[AddressDTO] = Field(
        default=None, alias="receiverAddress"
    )
    request_id: Optional[str] = Field(default=None, alias="requestId")
    express_services: Optional[List[ExpressServiceDTO]] = Field(
        default=None, alias="expressServices"
    )
    settle_account: Optional[str] = Field(default=None, alias="settleAccount")
    warehouse: Optional[WarehouseDTO] = Field(default=None, alias="warehouse")


class QueryRoutingReachableRequest(BaseModel):
    """可达性请求项（Java: QueryRoutingReachableRequest）"""

    request_id: Optional[str] = Field(default=None, alias="requestId")
    express_company_code: str = Field(alias="expressCompanyCode")
    type: Optional[int] = Field(default=None)
    sender_address: Optional[AddressDTO] = Field(default=None, alias="senderAddress")
    receiver_address: Optional[AddressDTO] = Field(
        default=None, alias="receiverAddress"
    )
    express_product_code: Optional[str] = Field(
        default=None, alias="expressProductCode"
    )
    express_services: Optional[List[ExpressServiceDTO]] = Field(
        default=None, alias="expressServices"
    )


class ExpressReachableQueryRequest(BaseRequest):
    """查询快递可达性请求（open.express.reachable.query, POST）"""

    reachable_requests: List[QueryRoutingReachableRequest] = Field(
        description="可达性请求列表", alias="reachableRequests"
    )

    @property
    def api_method(self) -> str:
        return "open.express.reachable.query"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressReachableQueryResponse(BaseResponse[ExpressReachable]):
    """查询快递可达性响应"""

    pass


class ExpressStandardTemplate(BaseModel):
    """标准快递模板（字段对齐 Java）"""

    template_id: Optional[str] = Field(default=None, alias="templateId")
    template_name: Optional[str] = Field(default=None, alias="templateName")
    logistics_company: Optional[str] = Field(default=None, alias="logisticsCompany")
    template_type: Optional[str] = Field(default=None, alias="templateType")


class ExpressStandardTemplateListRequest(BaseRequest):
    """获取标准模板列表请求（open.express.standard.template.list.get, POST）"""

    express_company_code: Optional[str] = Field(
        default=None, description="物流公司编码", alias="expressCompanyCode"
    )

    @property
    def api_method(self) -> str:
        return "open.express.standard.template.list.get"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressStandardTemplateListResponse(BaseResponse[List[ExpressStandardTemplate]]):
    """获取标准模板列表响应"""

    pass


class ExpressCustomTemplate(BaseModel):
    """自定义快递模板（字段对齐 Java）"""

    template_id: Optional[str] = Field(default=None, alias="templateId")
    template_name: Optional[str] = Field(default=None, alias="templateName")
    logistics_company: Optional[str] = Field(default=None, alias="logisticsCompany")
    template_content: Optional[Dict[str, Any]] = Field(
        default=None, alias="templateContent"
    )
    create_time: Optional[str] = Field(default=None, alias="createTime")


class ExpressCustomTemplateQueryRequest(BaseRequest):
    """查询自定义模板列表请求（open.express.custom.tempate.list.query, GET）"""

    standard_template_code: Optional[str] = Field(
        default=None, description="标准模板编码", alias="standardTemplateCode"
    )
    type: Optional[int] = Field(default=None, description="类型", alias="type")

    @property
    def api_method(self) -> str:
        return "open.express.custom.tempate.list.query"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ExpressCustomTemplateQueryResponse(BaseResponse[List[ExpressCustomTemplate]]):
    """查询自定义模板列表响应"""

    pass


class ExpressPrinterElementQueryRequest(BaseRequest):
    """打印元素查询请求（open.express.printer.element.query, GET）"""

    @property
    def api_method(self) -> str:
        return "open.express.printer.element.query"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ExpressPrinterElementQueryResponse(BaseResponse[Dict[str, Any]]):
    """打印元素查询响应"""

    pass


# 订单物流更新相关接口属于订单模块，已移至 models/order.py


# ==================== 物流轨迹回调相关 ====================


class ExtendField(BaseModel):
    """扩展字段（Java: ExtendField）"""

    value: Optional[str] = Field(default=None, alias="value")
    key: Optional[str] = Field(default=None, alias="key")


class TraceInfoDTO(BaseModel):
    """轨迹信息（Java: TraceInfoDTO）"""

    country: Optional[str] = Field(default=None, alias="country")
    station_address: Optional[str] = Field(default=None, alias="stationAddress")
    map_provider: Optional[str] = Field(default=None, alias="mapProvider")
    city: Optional[str] = Field(default=None, alias="city")
    latitude: Optional[str] = Field(default=None, alias="latitude")
    scan_type: Optional[str] = Field(default=None, alias="scanType")
    remark: Optional[str] = Field(default=None, alias="remark")
    next_way_bill_code: Optional[str] = Field(default=None, alias="nextWayBillCode")
    courier_phone: Optional[str] = Field(default=None, alias="courierPhone")
    province: Optional[str] = Field(default=None, alias="province")
    problem_code: Optional[str] = Field(default=None, alias="problemCode")
    next_express_company_code: Optional[str] = Field(
        default=None, alias="nextExpressCompanyCode"
    )
    net_site_name: Optional[str] = Field(default=None, alias="netSiteName")
    extend_fields: Optional[List[ExtendField]] = Field(
        default=None, alias="extendFields"
    )
    operate_time: Optional[str] = Field(default=None, alias="operateTime")
    next_node_code: Optional[str] = Field(default=None, alias="nextNodeCode")
    longitude: Optional[str] = Field(default=None, alias="longitude")
    next_node_type: Optional[int] = Field(default=None, alias="nextNodeType")
    town: Optional[str] = Field(default=None, alias="town")
    weight: Optional[int] = Field(default=None, alias="weight")
    net_site_type: Optional[int] = Field(default=None, alias="netSiteType")
    time_zone: Optional[str] = Field(default=None, alias="timeZone")
    net_site_code: Optional[str] = Field(default=None, alias="netSiteCode")
    next_city: Optional[str] = Field(default=None, alias="nextCity")
    courier: Optional[str] = Field(default=None, alias="courier")
    district: Optional[str] = Field(default=None, alias="district")
    next_node_name: Optional[str] = Field(default=None, alias="nextNodeName")
    request_id: Optional[str] = Field(default=None, alias="requestId")
    desc: Optional[str] = Field(default=None, alias="desc")
    station_name: Optional[str] = Field(default=None, alias="stationName")
    station_brand: Optional[str] = Field(default=None, alias="stationBrand")
    transport_type: Optional[str] = Field(default=None, alias="transportType")


class TraceNotifyDetailDTO(BaseModel):
    """轨迹通知明细（Java: TraceNotifyDetailDTO）"""

    waybill_code: Optional[str] = Field(default=None, alias="waybillCode")
    traces: Optional[List[TraceInfoDTO]] = Field(default=None, alias="traces")
    express_company_code: Optional[str] = Field(
        default=None, alias="expressCompanyCode"
    )


class LogisticsTraceNotifyRequest(BaseRequest):
    """物流轨迹通知回调请求（open.logistics.trace.notify, POST）"""

    traces: List[TraceNotifyDetailDTO] = Field(
        description="轨迹通知列表", alias="traces"
    )

    @property
    def api_method(self) -> str:
        return "open.logistics.trace.notify"

    # 固定使用 POST（Java 对齐）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class LogisticsTraceNotifyResponse(BaseResponse[Dict[str, Any]]):
    """物流轨迹通知回调响应"""

    pass


# ==================== Express Template APIs ====================


class ExpressTemplateAddParam(BaseModel):
    """快递模板添加参数"""

    send_province_name: str = Field(
        ..., description="发货省份名称", alias="sendProvinceName"
    )
    send_district_code: int = Field(
        ..., description="发货区域代码", alias="sendDistrictCode"
    )
    send_time: int = Field(..., description="发货时间", alias="sendTime")
    send_city_name: str = Field(..., description="发货城市名称", alias="sendCityName")
    cal_type: int = Field(..., description="计费类型", alias="calType")
    name: str = Field(..., description="模板名称")
    source_type: int = Field(..., description="来源类型", alias="sourceType")
    send_province_code: int = Field(
        ..., description="发货省份代码", alias="sendProvinceCode"
    )
    send_city_code: int = Field(..., description="发货城市代码", alias="sendCityCode")
    config: str = Field(..., description="配置信息")
    send_district_name: str = Field(
        ..., description="发货区域名称", alias="sendDistrictName"
    )


class ExpressTemplateAddRequest(BaseRequest):
    """快递模板添加请求
    API: open.logistics.express.template.add (POST)
    """

    param: ExpressTemplateAddParam = Field(..., description="模板参数")

    @property
    def api_method(self) -> str:
        return "open.logistics.express.template.add"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressTemplateAddResponse(BaseResponse[Dict[str, Any]]):
    """快递模板添加响应"""

    pass


class ExpressTemplateDetailParam(BaseModel):
    """快递模板详情查询参数"""

    id: int = Field(..., description="模板ID")


class ExpressTemplateDetailRequest(BaseRequest):
    """快递模板详情查询请求
    API: open.logistics.express.template.detail (GET)
    """

    param: ExpressTemplateDetailParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.logistics.express.template.detail"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ExpressTemplateDetailResponse(BaseResponse[Dict[str, Any]]):
    """快递模板详情查询响应"""

    pass


class ExpressTemplateListParam(BaseModel):
    """快递模板列表查询参数（对齐 Java: offset/limit/searchUsed）"""

    offset: Optional[int] = Field(default=None, description="偏移量")
    limit: Optional[int] = Field(default=None, description="限制条数")
    search_used: Optional[bool] = Field(
        default=None, description="是否仅查询使用中的", alias="searchUsed"
    )


class ExpressTemplateListRequest(BaseRequest):
    """快递模板列表查询请求
    API: open.logistics.express.template.list (GET)
    """

    param: ExpressTemplateListParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.logistics.express.template.list"

    # 固定使用 GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ExpressTemplateListResponse(BaseResponse[Dict[str, Any]]):
    """快递模板列表查询响应"""

    pass


class ExpressTemplateUpdateParam(BaseModel):
    """快递模板更新参数"""

    id: int = Field(..., description="模板ID")
    send_province_name: Optional[str] = Field(
        None, description="发货省份名称", alias="sendProvinceName"
    )
    send_district_code: Optional[int] = Field(
        None, description="发货区域代码", alias="sendDistrictCode"
    )
    send_time: Optional[int] = Field(None, description="发货时间", alias="sendTime")
    send_city_name: Optional[str] = Field(
        None, description="发货城市名称", alias="sendCityName"
    )
    cal_type: Optional[int] = Field(None, description="计费类型", alias="calType")
    name: Optional[str] = Field(None, description="模板名称")
    source_type: Optional[int] = Field(None, description="来源类型", alias="sourceType")
    send_province_code: Optional[int] = Field(
        None, description="发货省份代码", alias="sendProvinceCode"
    )
    send_city_code: Optional[int] = Field(
        None, description="发货城市代码", alias="sendCityCode"
    )
    config: Optional[str] = Field(None, description="配置信息")
    send_district_name: Optional[str] = Field(
        None, description="发货区域名称", alias="sendDistrictName"
    )


class ExpressTemplateUpdateRequest(BaseRequest):
    """快递模板更新请求
    API: open.logistics.express.template.update (POST)
    """

    param: ExpressTemplateUpdateParam = Field(..., description="更新参数")

    @property
    def api_method(self) -> str:
        return "open.logistics.express.template.update"

    # 固定使用 POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class ExpressTemplateUpdateResponse(BaseResponse[Dict[str, Any]]):
    """快递模板更新响应"""

    pass
