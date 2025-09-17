"""店铺相关数据模型（严格对齐 Java 参考）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod


class ShopInfo(BaseModel):
    """店铺信息"""

    shop_id: Optional[int] = Field(default=None, description="店铺ID")
    shop_name: str = Field(description="店铺名称")
    shop_logo: Optional[str] = Field(default=None, description="店铺logo")
    shop_description: Optional[str] = Field(default=None, description="店铺描述")
    shop_status: Optional[int] = Field(default=None, description="店铺状态")
    shop_type: Optional[int] = Field(default=None, description="店铺类型")
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")

    # 经营信息
    business_license: Optional[str] = Field(default=None, description="营业执照")
    business_scope: Optional[str] = Field(default=None, description="经营范围")
    legal_person: Optional[str] = Field(default=None, description="法人代表")

    # 联系信息
    contact_phone: Optional[str] = Field(default=None, description="联系电话")
    contact_email: Optional[str] = Field(default=None, description="联系邮箱")
    contact_address: Optional[str] = Field(default=None, description="联系地址")

    # 认证信息
    is_verified: Optional[bool] = Field(default=None, description="是否已认证")
    verification_status: Optional[int] = Field(default=None, description="认证状态")
    verification_time: Optional[str] = Field(default=None, description="认证时间")

    # 经营时间
    business_hours: Optional[str] = Field(default=None, description="营业时间")
    service_phone: Optional[str] = Field(default=None, description="客服电话")


# ==================== 店铺信息相关 ====================


class ShopInfoRequest(BaseRequest):
    """获取店铺信息请求"""

    @property
    def api_method(self) -> str:
        # Align with Java: OpenShopInfoGetRequest -> open.shop.info.get
        return "open.shop.info.get"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ShopInfoResponse(BaseResponse[ShopInfo]):
    """获取店铺信息响应"""

    pass


# ==================== 店铺评分相关 ====================


class ShopScore(BaseModel):
    """店铺评分信息"""

    # 总体评分
    overall_score: Optional[float] = Field(default=None, description="总体评分")

    # 各维度评分
    product_score: Optional[float] = Field(default=None, description="商品质量评分")
    service_score: Optional[float] = Field(default=None, description="服务态度评分")
    logistics_score: Optional[float] = Field(default=None, description="物流服务评分")
    after_sale_score: Optional[float] = Field(default=None, description="售后服务评分")

    # 评分统计
    total_reviews: Optional[int] = Field(default=None, description="总评价数")
    good_reviews: Optional[int] = Field(default=None, description="好评数")
    medium_reviews: Optional[int] = Field(default=None, description="中评数")
    bad_reviews: Optional[int] = Field(default=None, description="差评数")

    # 时间信息
    last_update_time: Optional[str] = Field(default=None, description="最后更新时间")

    @property
    def good_rate(self) -> Optional[float]:
        """好评率"""
        if (
            self.total_reviews
            and self.total_reviews > 0
            and self.good_reviews is not None
        ):
            return (self.good_reviews / self.total_reviews) * 100
        return None


class MasterScore(BaseModel):
    """主评分信息"""

    # 主要评分
    master_score: Optional[float] = Field(default=None, description="主评分")
    level: Optional[str] = Field(default=None, description="评分等级")

    # 分类评分
    category_scores: Optional[Dict[str, float]] = Field(
        default=None, description="分类评分"
    )

    # 统计信息
    score_count: Optional[int] = Field(default=None, description="评分次数")
    average_score: Optional[float] = Field(default=None, description="平均评分")

    # 时间信息
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")


class ShopScoreGetRequest(BaseRequest):
    """获取店铺评分请求"""

    @property
    def api_method(self) -> str:
        return "open.score.shop.get"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ShopScoreGetResponse(BaseResponse[ShopScore]):
    """获取店铺评分响应"""

    pass


class MasterScoreGetRequest(BaseRequest):
    """获取主评分信息请求"""

    @property
    def api_method(self) -> str:
        return "open.score.master.get"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class MasterScoreGetResponse(BaseResponse[MasterScore]):
    """获取主评分信息响应"""

    pass


# ==================== 品牌管理相关 ====================


class ShopBrand(BaseModel):
    """店铺品牌信息"""

    brand_id: Optional[int] = Field(default=None, description="品牌ID")
    brand_name: str = Field(description="品牌名称")
    brand_name_en: Optional[str] = Field(default=None, description="品牌英文名称")
    brand_logo: Optional[str] = Field(default=None, description="品牌logo")
    brand_description: Optional[str] = Field(default=None, description="品牌描述")

    # 授权信息
    authorization_status: Optional[int] = Field(default=None, description="授权状态")
    authorization_time: Optional[str] = Field(default=None, description="授权时间")
    expire_time: Optional[str] = Field(default=None, description="授权到期时间")

    # 证书信息
    certificate_url: Optional[str] = Field(default=None, description="授权证书URL")
    certificate_type: Optional[str] = Field(default=None, description="证书类型")

    # 状态信息
    status: Optional[int] = Field(default=None, description="状态：1-正常，0-禁用")
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")


class BrandBatchAddRequest(BaseRequest):
    """批量添加品牌请求"""

    brand_list: List[Dict[str, Any]] = Field(
        description="品牌信息列表", alias="brandList"
    )

    @property
    def api_method(self) -> str:
        return "open.shop.brand.batch.add"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class BrandBatchAddResponse(BaseResponse[Dict[str, Any]]):
    """批量添加品牌响应"""

    pass


class BrandPageGetRequest(BaseRequest):
    """分页获取品牌列表请求"""

    page_num: int = Field(1, description="页码", ge=1, alias="pageNum")
    page_size: int = Field(20, description="页面大小", ge=1, le=100, alias="pageSize")

    @property
    def api_method(self) -> str:
        return "open.shop.brand.page.get"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class BrandPageGetResponse(BaseResponse[List[ShopBrand]]):
    """分页获取品牌列表响应"""

    total: Optional[int] = Field(default=None, description="总数量")
    page: Optional[int] = Field(default=None, description="当前页码")
    page_size: Optional[int] = Field(default=None, description="页面大小")


# ==================== 企业资质管理相关 ====================


class EnterpriseQualification(BaseModel):
    """企业资质信息"""

    qualification_id: Optional[int] = Field(default=None, description="资质ID")
    qualification_type: str = Field(description="资质类型")
    qualification_name: str = Field(description="资质名称")
    qualification_number: Optional[str] = Field(default=None, description="资质编号")

    # 证书信息
    certificate_url: Optional[str] = Field(default=None, description="证书URL")
    certificate_start_time: Optional[str] = Field(
        default=None, description="证书生效时间"
    )
    certificate_end_time: Optional[str] = Field(
        default=None, description="证书失效时间"
    )

    # 审核信息
    audit_status: Optional[int] = Field(default=None, description="审核状态")
    audit_message: Optional[str] = Field(default=None, description="审核信息")
    audit_time: Optional[str] = Field(default=None, description="审核时间")

    # 基本信息
    company_name: Optional[str] = Field(default=None, description="公司名称")
    legal_person: Optional[str] = Field(default=None, description="法人代表")
    business_scope: Optional[str] = Field(default=None, description="经营范围")

    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")


class EnterpriseQualificationExistRequest(BaseRequest):
    """检查企业资质是否存在请求"""

    meta_data_info: Dict[str, Any] = Field(description="元数据", alias="metaDataInfo")

    @property
    def api_method(self) -> str:
        return "open.shop.enterprise.qualificaiton.exist"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class EnterpriseQualificationExistResponse(BaseResponse[Dict[str, Any]]):
    """检查企业资质是否存在响应"""

    exists: Optional[bool] = Field(default=None, description="是否存在")
    qualification_info: Optional[EnterpriseQualification] = Field(
        default=None, description="资质信息"
    )


# ==================== 入驻结算管理相关 ====================


class SettleContract(BaseModel):
    """结算合同信息"""

    contract_id: Optional[str] = Field(default=None, description="合同ID")
    contract_name: str = Field(description="合同名称")
    contract_type: Optional[str] = Field(default=None, description="合同类型")
    contract_url: Optional[str] = Field(default=None, description="合同URL")
    contract_status: Optional[int] = Field(default=None, description="合同状态")

    # 签署信息
    sign_time: Optional[str] = Field(default=None, description="签署时间")
    effective_time: Optional[str] = Field(default=None, description="生效时间")
    expire_time: Optional[str] = Field(default=None, description="到期时间")

    create_time: Optional[str] = Field(default=None, description="创建时间")


class SettleCategory(BaseModel):
    """入驻类目信息"""

    category_id: int = Field(description="类目ID")
    category_name: str = Field(description="类目名称")
    parent_id: Optional[int] = Field(default=None, description="父类目ID")
    level: Optional[int] = Field(default=None, description="层级")

    # 准入要求
    qualification_required: Optional[bool] = Field(
        default=None, description="是否需要资质"
    )
    qualifications: Optional[List[str]] = Field(
        default=None, description="所需资质列表"
    )

    # 费用信息
    deposit_amount: Optional[int] = Field(default=None, description="保证金金额（分）")
    commission_rate: Optional[float] = Field(default=None, description="佣金费率")


class InviteSettleOneStepRequest(BaseRequest):
    """一步式结算入驻请求"""

    invite_type: Optional[int] = Field(
        default=None, description="邀请类型", alias="inviteType"
    )
    oversea_enterprise_info: Optional[Dict[str, Any]] = Field(
        default=None, description="海外企业信息", alias="overseaEnterpriseInfo"
    )
    business_base_info: Optional[Dict[str, Any]] = Field(
        default=None, description="基础商业信息", alias="businessBaseInfo"
    )
    brand_request: Optional[Dict[str, Any]] = Field(
        default=None, description="品牌与商标信息", alias="brandRequest"
    )
    industry_qualification_request: Optional[Dict[str, Any]] = Field(
        default=None, description="行业资质请求", alias="industryQualificationRequest"
    )
    mainland_enterprise_info: Optional[Dict[str, Any]] = Field(
        default=None, description="内地企业信息", alias="mainlandEnterpriseInfo"
    )
    shop_request: Optional[Dict[str, Any]] = Field(
        default=None, description="店铺信息", alias="shopRequest"
    )

    @property
    def api_method(self) -> str:
        return "open.shop.invite.settle.oneStepSettle"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class InviteSettleOneStepResponse(BaseResponse[Dict[str, Any]]):
    """一步式结算入驻响应"""

    pass


class QueryCanOneStepSettleRequest(BaseRequest):
    """查询是否可一步式结算请求"""

    @property
    def api_method(self) -> str:
        return "open.shop.invite.settle.queryCanOneStepSettle"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class QueryCanOneStepSettleResponse(BaseResponse[Dict[str, Any]]):
    """查询是否可一步式结算响应"""

    can_settle: Optional[bool] = Field(default=None, description="是否可以一步式结算")
    reason: Optional[str] = Field(default=None, description="不可结算原因")


class QueryCategoryListRequest(BaseRequest):
    """查询入驻类目列表请求"""

    invite_type: Optional[int] = Field(
        default=None, description="邀请类型", alias="inviteType"
    )

    @property
    def api_method(self) -> str:
        return "open.shop.invite.settle.queryCategoryList"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class QueryCategoryListResponse(BaseResponse[List[SettleCategory]]):
    """查询入驻类目列表响应"""

    pass


class QueryIndustryCertificateByCategoryRequest(BaseRequest):
    """根据类目查询行业证书要求请求"""

    invite_type: Optional[int] = Field(
        default=None, description="邀请类型", alias="inviteType"
    )
    category_ids: List[int] = Field(description="类目ID列表", alias="categoryIds")
    oversea: Optional[bool] = Field(
        default=None, description="是否海外", alias="oversea"
    )

    @property
    def api_method(self) -> str:
        return "open.shop.invite.settle.queryIndustryCertificateByCategory"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class QueryIndustryCertificateByCategoryResponse(BaseResponse[List[Dict[str, Any]]]):
    """根据类目查询行业证书要求响应"""

    pass


class QuerySettleContractsRequest(BaseRequest):
    """查询结算合同请求"""

    invite_type: Optional[int] = Field(
        default=None, description="邀请类型", alias="inviteType"
    )

    @property
    def api_method(self) -> str:
        return "open.shop.invite.settle.querySettleContracts"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class QuerySettleContractsResponse(BaseResponse[List[SettleContract]]):
    """查询结算合同响应"""

    pass


class QuerySettleStatusRequest(BaseRequest):
    """查询结算状态请求"""

    @property
    def api_method(self) -> str:
        return "open.shop.invite.settle.querySettleStatus"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class QuerySettleStatusResponse(BaseResponse[Dict[str, Any]]):
    """查询结算状态响应"""

    status: Optional[int] = Field(default=None, description="结算状态")
    status_desc: Optional[str] = Field(default=None, description="状态描述")
    message: Optional[str] = Field(default=None, description="状态消息")


# ==================== POI管理相关 ====================


class POIDetail(BaseModel):
    """POI详情信息"""

    poi_id: Optional[str] = Field(default=None, description="POI ID")
    outer_poi_id: Optional[str] = Field(default=None, description="外部POI ID")
    poi_name: str = Field(description="POI名称")

    # 地址信息
    province: Optional[str] = Field(default=None, description="省份")
    city: Optional[str] = Field(default=None, description="城市")
    district: Optional[str] = Field(default=None, description="区县")
    address: Optional[str] = Field(default=None, description="详细地址")

    # 坐标信息
    longitude: Optional[float] = Field(default=None, description="经度")
    latitude: Optional[float] = Field(default=None, description="纬度")

    # 营业信息
    business_hours: Optional[str] = Field(default=None, description="营业时间")
    phone: Optional[str] = Field(default=None, description="联系电话")

    # 状态信息
    status: Optional[int] = Field(default=None, description="状态")
    create_time: Optional[str] = Field(default=None, description="创建时间")
    update_time: Optional[str] = Field(default=None, description="更新时间")


class POIGetDetailByOuterPOIRequest(BaseRequest):
    """根据外部POI ID获取详情请求"""

    outer_poi_id: str = Field(description="外部POI ID", alias="outerPoiId")
    source: Optional[int] = Field(default=None, description="来源", alias="source")

    @property
    def api_method(self) -> str:
        return "open.shop.poi.getPoiDetailByOuterPoi"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class POIGetDetailByOuterPOIResponse(BaseResponse[POIDetail]):
    """根据外部POI ID获取详情响应"""

    pass
