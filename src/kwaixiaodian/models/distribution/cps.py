"""CPS管理相关数据模型（按 Java 参考严格对齐）"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from ..base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== CPS 管理相关 API ====================


class CpsOrderListRequest(BaseRequest):
    """CPS订单列表请求

    Java: OpenSellerOrderCpsListRequest
    Http: GET
    """

    # Java ParamDTO fields (aliases must match exactly)
    current_page: Optional[int] = Field(
        default=None, description="当前页码", alias="currentPage"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort: Optional[int] = Field(default=None, description="排序方式", alias="sort")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    type: Optional[int] = Field(default=None, description="类型", alias="type")
    pcursor: Optional[str] = Field(
        default=None, description="分页游标", alias="pcursor"
    )
    distributor_id: Optional[int] = Field(
        default=None, description="分销商ID", alias="distributorId"
    )
    begin_time: Optional[int] = Field(
        default=None, description="开始时间", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )

    @property
    def api_method(self) -> str:
        return "open.seller.order.cps.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsOrderListResponse(BaseResponse[Dict[str, Any]]):
    """CPS订单列表响应"""

    pass


class CpsDistributorOrderListRequest(BaseRequest):
    """CPS分销商订单列表请求"""

    # Based on Java SDK: OpenDistributionCpsDistributorOrderCursorListRequest

    cps_order_status: Optional[int] = Field(
        default=None, description="CPS订单状态", alias="cpsOrderStatus"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort_type: Optional[int] = Field(
        default=None, description="排序类型", alias="sortType"
    )
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: Optional[int] = Field(
        default=None, description="开始时间", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    pcursor: Optional[str] = Field(
        default=None, description="分页游标", alias="pcursor"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.distributor.order.cursor.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsDistributorOrderListResponse(BaseResponse[Dict[str, Any]]):
    """CPS分销商订单列表响应"""

    pass


class CpsPidBindUrlRequest(BaseRequest):
    """CPS PID绑定URL请求"""

    # Based on Java SDK: OpenDistributionPidBindUrlRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.pid.bind.url"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsPidBindUrlResponse(BaseResponse[Dict[str, Any]]):
    """CPS PID绑定URL响应"""

    pass


class CpsLinkTransferRequest(BaseRequest):
    """CPS链接转换请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyLinkTransferRequest

    cps_link: str = Field(description="CPS链接", alias="cpsLink")
    kwaimoney_id: List[int] = Field(description="快手货币ID列表", alias="kwaimoneyId")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.link.transfer"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsLinkTransferResponse(BaseResponse[Dict[str, Any]]):
    """CPS链接转换响应"""

    pass


class CpsBrandThemeListRequest(BaseRequest):
    """CPS品牌主题列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionBrandThemeListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.brand.theme.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsBrandThemeListResponse(BaseResponse[Dict[str, Any]]):
    """CPS品牌主题列表响应"""

    pass


class CpsThemeEntranceListRequest(BaseRequest):
    """CPS主题入口列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionThemeEntranceListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.theme.entrance.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsThemeEntranceListResponse(BaseResponse[Dict[str, Any]]):
    """CPS主题入口列表响应"""

    pass


class CpsKwaimoneyThemeEntranceListRequest(BaseRequest):
    """CPS快手货币主题入口列表请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyThemeEntranceListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.theme.entrance.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneyThemeEntranceListResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币主题入口列表响应"""

    pass


class CpsPromotionRecoTopicListRequest(BaseRequest):
    """CPS推广推荐话题列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionRecoTopicListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.reco.topic.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsPromotionRecoTopicListResponse(BaseResponse[Dict[str, Any]]):
    """CPS推广推荐话题列表响应"""

    pass


class CpsPromotionEffectDetailRequest(BaseRequest):
    """CPS推广效果详情请求

    Java: OpenDistributionCpsKwaimoneyNewPromotionEffectDetailRequest
    ParamDTO: startTime, endTime, offset, limit, orderField, orderType,
              cpsPid, linkType, carrierId, buyerType
    """

    start_time: Optional[str] = Field(
        default=None, description="开始时间", alias="startTime"
    )
    end_time: Optional[str] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    offset: Optional[int] = Field(default=None, description="偏移量", alias="offset")
    limit: Optional[int] = Field(default=None, description="返回条数", alias="limit")
    order_field: Optional[int] = Field(
        default=None, description="排序字段", alias="orderField"
    )
    order_type: Optional[int] = Field(
        default=None, description="排序方式", alias="orderType"
    )
    cps_pid: Optional[str] = Field(default=None, description="推广位ID", alias="cpsPid")
    link_type: Optional[str] = Field(
        default=None, description="链接类型", alias="linkType"
    )
    carrier_id: Optional[int] = Field(
        default=None, description="渠道ID", alias="carrierId"
    )
    buyer_type: Optional[int] = Field(
        default=None, description="买家类型", alias="buyerType"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.new.promotion.effect.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyNewPromotionEffectDetailData(BaseModel):
    """Java: KwaimoneyNewPromotionEffectDetailData（代表性字段）"""

    date: Optional[str] = Field(default=None, alias="date")
    item_id: Optional[int] = Field(default=None, alias="itemId")
    item_name: Optional[str] = Field(default=None, alias="itemName")
    item_price: Optional[int] = Field(default=None, alias="itemPrice")
    promoter_id: Optional[int] = Field(default=None, alias="promoterId")
    promoter_name: Optional[str] = Field(default=None, alias="promoterName")
    cps_pid: Optional[str] = Field(default=None, alias="cpsPid")
    uv: Optional[int] = Field(default=None, alias="uv")
    order_id: Optional[int] = Field(default=None, alias="orderId")
    virtual_device_id: Optional[str] = Field(default=None, alias="virtualDeviceId")


class KwaimoneyNewPromotionEffectDetailPageResult(BaseModel):
    """Java: KwaimoneyNewPromotionEffectDetailDataPageResult"""

    detail_list: Optional[List[KwaimoneyNewPromotionEffectDetailData]] = Field(
        default=None, alias="detailList"
    )
    total: Optional[int] = Field(default=None, alias="total")


class CpsPromotionEffectDetailResponse(
    BaseResponse[KwaimoneyNewPromotionEffectDetailPageResult]
):
    """CPS推广效果详情响应（类型化，Java对齐）"""

    pass


class CpsLeaderOrderDetailRequest(BaseRequest):
    """CPS领导者订单详情请求

    Java: OpenDistributionCpsLeaderOrderDetailRequest
    ParamDTO: oid, sellerId, fundType
    """

    oid: int = Field(description="订单ID", alias="oid")
    seller_id: Optional[int] = Field(
        default=None, description="卖家ID", alias="sellerId"
    )
    fund_type: Optional[int] = Field(
        default=None, description="资金类型", alias="fundType"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.leader.order.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsLeaderOrderDetailResponse(BaseResponse[Dict[str, Any]]):
    """CPS领导者订单详情响应"""

    pass


class CpsSelectionItemDetailRequest(BaseRequest):
    """CPS精选商品详情请求

    Java: OpenDistributionCpsKwaimoneySelectionItemDetailRequest
    ParamDTO: itemId (List<Long>)
    """

    item_id: List[int] = Field(description="商品ID列表", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.selection.item.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsSelectionItemDetailResponse(BaseResponse[Dict[str, Any]]):
    """CPS精选商品详情响应"""

    pass


class CpsLeaderOrderCursorListRequest(BaseRequest):
    """CPS团长订单游标列表请求"""

    # Based on Java SDK: OpenDistributionCpsLeaderOrderCursorListRequest

    cps_order_status: Optional[int] = Field(
        default=None, description="CPS订单状态", alias="cpsOrderStatus"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort_type: Optional[int] = Field(
        default=None, description="排序类型", alias="sortType"
    )
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: Optional[int] = Field(
        default=None, description="开始时间", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    pcursor: Optional[str] = Field(
        default=None, description="分页游标", alias="pcursor"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.leader.order.cursor.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsLeaderOrderCursorListResponse(BaseResponse[Dict[str, Any]]):
    """CPS团长订单游标列表响应"""

    pass


class CpsLinkCreateRequest(BaseRequest):
    """CPS推广链接创建请求"""

    # Based on Java SDK: OpenDistributionCpsLinkCreateRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.link.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsLinkCreateResponse(BaseResponse[Dict[str, Any]]):
    """CPS推广链接创建响应"""

    pass


class CpsPidCreateRequest(BaseRequest):
    """CPS推广位创建请求"""

    # Based on Java SDK: OpenDistributionCpsPidCreateRequest

    promotion_bit_name: str = Field(description="推广位名称", alias="promotionBitName")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.pid.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsPidCreateResponse(BaseResponse[Dict[str, Any]]):
    """CPS推广位创建响应"""

    pass


class CpsPidQueryRequest(BaseRequest):
    """CPS推广位查询请求"""

    # Based on Java SDK: OpenDistributionCpsPidQueryRequest

    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.pid.query"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsPidQueryResponse(BaseResponse[Dict[str, Any]]):
    """CPS推广位查询响应"""

    pass


class CpsPromoterOrderDetailRequest(BaseRequest):
    """CPS推广者订单详情请求"""

    # Based on Java SDK: OpenDistributionCpsPromoterOrderDetailRequest

    order_id: str = Field(description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promoter.order.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsPromoterOrderDetailResponse(BaseResponse[Dict[str, Any]]):
    """CPS推广者订单详情响应"""

    pass


class PromotionItemInfo(BaseModel):
    """Java: PromotionItemInfo（代表性字段）"""

    channel_ids: Optional[List[int]] = Field(default=None, alias="channelIds")
    sales_tip: Optional[int] = Field(default=None, alias="salesTip")
    goods_price: Optional[int] = Field(default=None, alias="goodsPrice")
    item_desc_urls: Optional[List[str]] = Field(default=None, alias="itemDescUrls")
    goods_id: Optional[int] = Field(default=None, alias="goodsId")
    goods_gallery_urls: Optional[List[str]] = Field(
        default=None, alias="goodsGalleryUrls"
    )
    promotion_rate: Optional[int] = Field(default=None, alias="promotionRate")
    goods_desc: Optional[str] = Field(default=None, alias="goodsDesc")
    promotion_amount: Optional[int] = Field(default=None, alias="promotionAmount")
    express_id: Optional[int] = Field(default=None, alias="expressId")
    goods_image_url: Optional[str] = Field(default=None, alias="goodsImageUrl")
    category_id: Optional[int] = Field(default=None, alias="categoryId")
    goods_title: Optional[str] = Field(default=None, alias="goodsTitle")
    mall_id: Optional[int] = Field(default=None, alias="mallId")
    mall_type: Optional[int] = Field(default=None, alias="mallType")
    mall_name: Optional[str] = Field(default=None, alias="mallName")
    zk_goods_price: Optional[int] = Field(default=None, alias="zkGoodsPrice")


class BrandInfo(BaseModel):
    """Java: BrandInfo（代表性字段）"""

    item_total_count: Optional[int] = Field(default=None, alias="itemTotalCount")
    brand_eng_title: Optional[str] = Field(default=None, alias="brandEngTitle")
    ska: Optional[int] = Field(default=None, alias="ska")
    brand_logo: Optional[str] = Field(default=None, alias="brandLogo")
    simple_item_info_list: Optional[List[PromotionItemInfo]] = Field(
        default=None, alias="simpleItemInfoList"
    )
    shop_total_count: Optional[int] = Field(default=None, alias="shopTotalCount")
    brand_id: Optional[int] = Field(default=None, alias="brandId")
    brand_title: Optional[str] = Field(default=None, alias="brandTitle")


class BrandThemeBrandList(BaseModel):
    """Java: BrandThemeBrandList"""

    brand_list: Optional[List[BrandInfo]] = Field(default=None, alias="brandList")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")


class CpsPromotionBrandThemeBrandListRequest(BaseRequest):
    """CPS品牌主题品牌列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionBrandThemeBrandListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.brand.theme.brand.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsPromotionBrandThemeBrandListResponse(BaseResponse[BrandThemeBrandList]):
    """CPS品牌主题品牌列表响应（类型化，Java对齐）"""

    pass


class CpsPromotionBrandThemeItemListRequest(BaseRequest):
    """CPS品牌主题商品列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionBrandThemeItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.brand.theme.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class OrderType(BaseModel):
    """Java: OrderType"""

    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[int] = Field(default=None, alias="type")


class BrandItemList(BaseModel):
    """Java: BrandItemList"""

    item_list: Optional[List[PromotionItemInfo]] = Field(default=None, alias="itemList")
    order_type: Optional[List[OrderType]] = Field(default=None, alias="orderType")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")


class CpsPromotionBrandThemeItemListResponse(BaseResponse[BrandItemList]):
    """CPS品牌主题商品列表响应（类型化，Java对齐）"""

    pass


class CpsPromotionBrandThemeShopListRequest(BaseRequest):
    """CPS品牌主题店铺列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionBrandThemeShopListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.brand.theme.shop.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ShopScore(BaseModel):
    """Java: ShopScore"""

    value_des: Optional[str] = Field(default=None, alias="valueDes")
    type: Optional[int] = Field(default=None, alias="type")
    value: Optional[str] = Field(default=None, alias="value")
    key: Optional[str] = Field(default=None, alias="key")


class BrandShopInfo(BaseModel):
    """Java: BrandShopInfo（代表性字段）"""

    shop_id: Optional[int] = Field(default=None, alias="shopId")
    score: Optional[List[ShopScore]] = Field(default=None, alias="score")
    shop_icon_url: Optional[str] = Field(default=None, alias="shopIconUrl")
    ska: Optional[int] = Field(default=None, alias="ska")
    shop_name: Optional[str] = Field(default=None, alias="shopName")
    shop_sold_amount: Optional[str] = Field(default=None, alias="shopSoldAmount")
    simple_item_info_list: Optional[List[PromotionItemInfo]] = Field(
        default=None, alias="simpleItemInfoList"
    )
    item_num: Optional[int] = Field(default=None, alias="itemNum")


class BrandShopList(BaseModel):
    """Java: BrandShopList"""

    shop_list: Optional[List[BrandShopInfo]] = Field(default=None, alias="shopList")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")


class CpsPromotionBrandThemeShopListResponse(BaseResponse[BrandShopList]):
    """CPS品牌主题店铺列表响应（类型化，Java对齐）"""

    pass


class CpsPromotionRecoTopicInfoRequest(BaseRequest):
    """CPS推荐话题信息请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionRecoTopicInfoRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.reco.topic.info"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class ChannelInfo(BaseModel):
    """Java: ChannelInfo"""

    channel_name: Optional[str] = Field(default=None, alias="channelName")
    channel_id: Optional[int] = Field(default=None, alias="channelId")


class SubTopic(BaseModel):
    """Java: SubTopic"""

    sub_topic_id: Optional[int] = Field(default=None, alias="subTopicId")
    sub_topic_name: Optional[str] = Field(default=None, alias="subTopicName")


class RecoTopicInfo(BaseModel):
    """Java: RecoTopicInfo（代表性字段）"""

    total_count: Optional[int] = Field(default=None, alias="totalCount")
    topic_name: Optional[str] = Field(default=None, alias="topicName")
    topic_img: Optional[str] = Field(default=None, alias="topicImg")
    sub_topic_list: Optional[List[SubTopic]] = Field(default=None, alias="subTopicList")
    update_time_away: Optional[int] = Field(default=None, alias="updateTimeAway")
    topic_id: Optional[int] = Field(default=None, alias="topicId")
    channel_list: Optional[List[ChannelInfo]] = Field(default=None, alias="channelList")
    topic_type: Optional[int] = Field(default=None, alias="topicType")


class CpsPromotionRecoTopicInfoResponse(BaseResponse[RecoTopicInfo]):
    """CPS推荐话题信息响应（类型化，Java对齐）"""

    pass


class CpsPromotionRecoTopicItemListRequest(BaseRequest):
    """CPS推荐话题商品列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionRecoTopicItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.reco.topic.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class RecoTopicItemListInfo(BaseModel):
    """Java: RecoTopicItemListInfo"""

    item_list: Optional[List[PromotionItemInfo]] = Field(default=None, alias="itemList")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")


class CpsPromotionRecoTopicItemListResponse(BaseResponse[RecoTopicItemListInfo]):
    """CPS推荐话题商品列表响应（类型化，Java对齐）"""

    pass


class CpsPromotionRecoTopicSellerListRequest(BaseRequest):
    """CPS推荐话题卖家列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionRecoTopicSellerListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promotion.reco.topic.seller.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class RecoShopInfo(BaseModel):
    """Java: RecoShopInfo（代表性字段）"""

    shop_star: Optional[str] = Field(default=None, alias="shopStar")
    shop_id: Optional[int] = Field(default=None, alias="shopId")
    shop_icon_url: Optional[str] = Field(default=None, alias="shopIconUrl")
    shop_name: Optional[str] = Field(default=None, alias="shopName")
    simple_item_info_list: Optional[List[PromotionItemInfo]] = Field(
        default=None, alias="simpleItemInfoList"
    )


class RecoTopicSellerList(BaseModel):
    """Java: RecoTopicSellerList"""

    seller_list: Optional[List[RecoShopInfo]] = Field(default=None, alias="sellerList")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")


class CpsPromotionRecoTopicSellerListResponse(BaseResponse[RecoTopicSellerList]):
    """CPS推荐话题卖家列表响应（类型化，Java对齐）"""

    pass


class CpsPromotionThemeItemListRequest(BaseRequest):
    """CPS推广主题商品列表请求"""

    # Based on Java SDK: OpenDistributionCpsPromotionThemeItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.promtion.theme.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PromtionThemeItemList(BaseModel):
    """Java: OpenDistributionCpsPromtionThemeItemListResponse payload"""

    data: Optional[List[PromotionItemInfo]] = Field(default=None, alias="data")
    pcursor: Optional[str] = Field(default=None, alias="pcursor")


class CpsPromotionThemeItemListResponse(BaseResponse[PromtionThemeItemList]):
    """CPS推广主题商品列表响应（类型化，Java对齐）"""

    pass


# ==================== 更多CPS核心API ====================


class CpsKwaimoneyOrderListRequest(BaseRequest):
    """CPS快手货币订单列表请求

    Java: OpenDistributionCpsKwaimoneyOrderListRequest
    Http: GET
    """

    # Java ParamDTO fields with exact aliases
    cps_order_status: Optional[int] = Field(
        default=None, description="CPS订单状态", alias="cpsOrderStatus"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    sort_type: Optional[int] = Field(
        default=None, description="排序类型", alias="sortType"
    )
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )
    begin_time: Optional[int] = Field(
        default=None, description="开始时间", alias="beginTime"
    )
    end_time: Optional[int] = Field(
        default=None, description="结束时间", alias="endTime"
    )
    pcursor: Optional[str] = Field(
        default=None, description="分页游标", alias="pcursor"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.order.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneyOrderListResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币订单列表响应"""

    pass


class CpsKwaimoneyOrderDetailRequest(BaseRequest):
    """CPS快手货币订单详情请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyOrderDetailRequest

    oid: List[int] = Field(description="订单ID列表", alias="oid")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.order.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneyOrderDetailResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币订单详情响应"""

    pass


class CpsKwaimoneyPidListRequest(BaseRequest):
    """CPS快手货币PID列表请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyPidListRequest

    page: Optional[int] = Field(default=None, description="页码", alias="page")
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.pid.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneyPidListResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币PID列表响应"""

    pass


class CpsKwaimoneyPidUpdateRequest(BaseRequest):
    """CPS快手货币PID更新请求

    Java: OpenDistributionCpsKwaimoneyPidUpdateRequest
    Http: POST
    """

    # Java ParamDTO
    promotion_bit_name: str = Field(description="推广位名称", alias="promotionBitName")
    cps_pid: str = Field(description="CPS推广位ID", alias="cpsPid")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.pid.update"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsKwaimoneyPidUpdateResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币PID更新响应"""

    pass


class CpsKwaimoneyPromotionEffectTrendRequest(BaseRequest):
    """CPS快手货币推广效果趋势请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyNewPromotionEffectTrendRequest

    begin_time: int = Field(description="开始时间", alias="beginTime")
    end_time: int = Field(description="结束时间", alias="endTime")
    query_type: Optional[int] = Field(
        default=None, description="查询类型", alias="queryType"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.new.promotion.effect.trend"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyNewPromotionTrendData(BaseModel):
    """Java: KwaimoneyNewPromotionTrendData"""

    date: Optional[str] = Field(default=None, alias="date")
    total_uv: Optional[int] = Field(default=None, alias="totalUv")


class CpsKwaimoneyPromotionEffectTrendResponse(
    BaseResponse[List[KwaimoneyNewPromotionTrendData]]
):
    """CPS快手货币推广效果趋势响应（类型化，Java对齐）"""

    pass


class CpsDistributorOrderCommentListRequest(BaseRequest):
    """CPS分销商订单评论列表请求

    Java: OpenDistributionCpsDistributorOrderCommentListRequest
    ParamDTO: oid (List<Long>), sellerId (Long)
    """

    oid: List[int] = Field(description="订单ID列表", alias="oid")
    seller_id: Optional[int] = Field(
        default=None, description="卖家ID", alias="sellerId"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.distributor.order.comment.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsDistributorOrderCommentListResponse(BaseResponse[Dict[str, Any]]):
    """CPS分销商订单评论列表响应"""

    pass


class SellerOrderCpsDetailRequest(BaseRequest):
    """卖家CPS订单详情请求"""

    # Based on Java SDK: OpenSellerOrderCpsDetailRequest

    order_id: str = Field(description="订单ID", alias="orderId")

    @property
    def api_method(self) -> str:
        return "open.seller.order.cps.detail"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SellerOrderCpsDetailResponse(BaseResponse[Dict[str, Any]]):
    """卖家CPS订单详情响应"""

    pass


class KwaimoneyPreheatWorkLinkRequest(BaseRequest):
    """快手货币预热工作链接请求"""

    # Based on Java SDK: OpenDistributionKwaimoneyPreheatWorkLinkRequest

    preheat_work_id: int = Field(description="预热工作ID", alias="preheatWorkId")

    @property
    def api_method(self) -> str:
        return "open.distribution.kwaimoney.preheat.work.link"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyPreheatWorkLinkResponse(BaseResponse[Dict[str, Any]]):
    """快手货币预热工作链接响应"""

    pass


class CpsKwaimoneyLinkParseRequest(BaseRequest):
    """CPS快手货币链接解析请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyLinkParseRequest

    cps_link: str = Field(description="CPS链接", alias="cpsLink")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.link.parse"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsKwaimoneyLinkParseResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币链接解析响应"""

    pass


class CpsKwaimoneyPidCreateRequest(BaseRequest):
    """CPS快手货币PID创建请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyPidCreateRequest

    promotion_bit_name: str = Field(description="推广位名称", alias="promotionBitName")

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.pid.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsKwaimoneyPidCreateResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币PID创建响应"""

    pass


class CpsKwaimoneyLinkCreateRequest(BaseRequest):
    """CPS快手货币链接创建请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyLinkCreateRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.link.create"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CpsKwaimoneyLinkCreateResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币链接创建响应"""

    pass


class CpsKwaimoneySelectionChannelListRequest(BaseRequest):
    """CPS快手货币精选渠道列表请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneySelectionChannelListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.selection.channel.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneySelectionChannelListResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币精选渠道列表响应"""

    pass


class KwaimoneyRequirementCursorListRequest(BaseRequest):
    """快手货币需求游标列表请求"""

    # Based on Java SDK: OpenDistributionKwaimoneyRequirementCursorListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.kwaimoney.requirement.cursor.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyRequirementCursorListResponse(BaseResponse[Dict[str, Any]]):
    """快手货币需求游标列表响应"""

    pass


class CpsKwaimoneySelectionItemListRequest(BaseRequest):
    """CPS快手货币精选商品列表请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneySelectionItemListRequest

    range_list: Optional[List[Dict[str, Any]]] = Field(
        default=None, description="范围列表", alias="rangeList"
    )
    sort_type: Optional[str] = Field(
        default=None, description="排序类型", alias="sortType"
    )
    page_index: Optional[str] = Field(
        default=None, description="页面索引", alias="pageIndex"
    )
    channel_id: Optional[List[int]] = Field(
        default=None, description="渠道ID列表", alias="channelId"
    )
    page_size: Optional[int] = Field(
        default=None, description="页面大小", alias="pageSize"
    )
    express_type: Optional[int] = Field(
        default=None, description="快递类型", alias="expressType"
    )
    plan_type: Optional[int] = Field(
        default=None, description="计划类型", alias="planType"
    )
    keyword: Optional[str] = Field(default=None, description="关键词", alias="keyword")
    item_level: Optional[str] = Field(
        default=None, description="商品等级", alias="itemLevel"
    )
    seller_id: Optional[int] = Field(
        default=None, description="商家ID", alias="sellerId"
    )
    item_tag: Optional[List[str]] = Field(
        default=None, description="商品标签", alias="itemTag"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.selection.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneySelectionItemListResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币精选商品列表响应"""

    pass


class CpsKwaimoneyThemeItemListRequest(BaseRequest):
    """CPS快手货币主题商品列表请求"""

    # Based on Java SDK: OpenDistributionCpsKwaimoneyThemeItemListRequest

    theme_id: Optional[int] = Field(default=None, description="主题ID", alias="themeId")
    sub_theme_id: Optional[int] = Field(
        default=None, description="子主题ID", alias="subThemeId"
    )
    pcursor: Optional[str] = Field(
        default=None, description="分页游标", alias="pcursor"
    )

    @property
    def api_method(self) -> str:
        return "open.distribution.cps.kwaimoney.theme.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CpsKwaimoneyThemeItemListResponse(BaseResponse[Dict[str, Any]]):
    """CPS快手货币主题商品列表响应"""

    pass


# ==================== 补齐缺失的快手小店相关API ====================


class KwaimoneyAuthorityCursorListRequest(BaseRequest):
    """快手小店权限游标列表请求"""

    # Based on Java SDK: OpenDistributionKwaimoneyAuthorityCursorListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.kwaimoney.authority.cursor.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyAuthorityCursorListResponse(BaseResponse[Dict[str, Any]]):
    """快手小店权限游标列表响应"""

    pass


class KwaimoneyItemBatchCursorListRequest(BaseRequest):
    """快手小店商品批量游标列表请求"""

    # Based on Java SDK: OpenDistributionKwaimoneyItemBatchCursorListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.kwaimoney.item.batch.cursor.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyItemBatchCursorListResponse(BaseResponse[Dict[str, Any]]):
    """快手小店商品批量游标列表响应"""

    pass


class KwaimoneyRequirementBatchCursorListRequest(BaseRequest):
    """快手小店需求批量游标列表请求"""

    # Based on Java SDK: OpenDistributionKwaimoneyRequirementBatchCursorListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.kwaimoney.requirement.batch.cursor.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class KwaimoneyRequirementBatchCursorListResponse(BaseResponse[Dict[str, Any]]):
    """快手小店需求批量游标列表响应"""

    pass
