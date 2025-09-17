"""评价管理相关数据模型"""

from enum import Enum
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod


class CommentType(int, Enum):
    """评价类型"""

    ALL = 0  # 全部评价
    GOOD = 1  # 好评
    MEDIUM = 2  # 中评
    BAD = 3  # 差评
    WITH_IMAGES = 4  # 有图评价
    WITH_VIDEO = 5  # 有视频评价


class CommentStatus(int, Enum):
    """评价状态"""

    NORMAL = 1  # 正常
    HIDDEN = 2  # 隐藏
    DELETED = 3  # 已删除
    UNDER_REVIEW = 4  # 审核中
    SPAM = 5  # 垃圾评价


class ReplyStatus(int, Enum):
    """回复状态"""

    NOT_REPLIED = 0  # 未回复
    REPLIED = 1  # 已回复
    PENDING = 2  # 待回复


class CommentRating(int, Enum):
    """评价星级"""

    ONE_STAR = 1  # 1星
    TWO_STAR = 2  # 2星
    THREE_STAR = 3  # 3星
    FOUR_STAR = 4  # 4星
    FIVE_STAR = 5  # 5星


class ModerationAction(str, Enum):
    """审核操作"""

    APPROVE = "approve"  # 通过
    REJECT = "reject"  # 拒绝
    HIDE = "hide"  # 隐藏
    SPAM = "spam"  # 标记垃圾
    DELETE = "delete"  # 删除


class SortOrder(str, Enum):
    """排序方式"""

    TIME_DESC = "time_desc"  # 时间倒序
    TIME_ASC = "time_asc"  # 时间正序
    RATING_DESC = "rating_desc"  # 评分倒序
    RATING_ASC = "rating_asc"  # 评分正序
    HELPFUL_DESC = "helpful_desc"  # 有用数倒序


# ==================== 基础数据模型 ====================


class CommentUser(BaseModel):
    """评价用户信息"""

    user_id: int = Field(description="用户ID")
    nickname: str = Field(description="用户昵称")
    avatar: Optional[str] = Field(default=None, description="用户头像")
    level: Optional[int] = Field(default=None, description="用户等级")
    is_vip: bool = Field(default=False, description="是否VIP")
    is_verified: bool = Field(default=False, description="是否认证用户")


class CommentMedia(BaseModel):
    """评价媒体信息"""

    media_id: str = Field(description="媒体ID")
    media_type: str = Field(description="媒体类型", pattern="^(image|video)$")
    url: str = Field(description="媒体URL")
    thumb_url: Optional[str] = Field(default=None, description="缩略图URL")
    width: Optional[int] = Field(default=None, description="宽度")
    height: Optional[int] = Field(default=None, description="高度")
    duration: Optional[int] = Field(default=None, description="时长（秒）")
    size: Optional[int] = Field(default=None, description="文件大小（字节）")


class CommentReply(BaseModel):
    """评价回复"""

    reply_id: str = Field(description="回复ID")
    comment_id: str = Field(description="评价ID")
    content: str = Field(description="回复内容")
    replier_type: str = Field(description="回复者类型")  # merchant, system, user
    replier_name: str = Field(description="回复者名称")
    create_time: str = Field(description="回复时间")
    is_official: bool = Field(default=False, description="是否官方回复")


class CommentDetail(BaseModel):
    """评价详情"""

    # 基本信息
    comment_id: str = Field(description="评价ID")
    item_id: str = Field(description="商品ID")
    item_name: Optional[str] = Field(default=None, description="商品名称")
    item_sku_id: Optional[str] = Field(default=None, description="SKU ID")
    order_id: str = Field(description="订单ID")

    # 评价内容
    content: str = Field(description="评价内容")
    rating: CommentRating = Field(description="评价星级")
    comment_type: CommentType = Field(description="评价类型")
    status: CommentStatus = Field(default=CommentStatus.NORMAL, description="评价状态")

    # 用户信息
    user: CommentUser = Field(description="评价用户信息")

    # 媒体文件
    images: Optional[List[CommentMedia]] = Field(default=None, description="评价图片")
    videos: Optional[List[CommentMedia]] = Field(default=None, description="评价视频")

    # 评价统计
    helpful_count: int = Field(default=0, description="有用数")
    reply_count: int = Field(default=0, description="回复数")
    view_count: int = Field(default=0, description="查看数")

    # 回复信息
    reply_status: ReplyStatus = Field(
        default=ReplyStatus.NOT_REPLIED, description="回复状态"
    )
    merchant_reply: Optional[CommentReply] = Field(default=None, description="商家回复")
    replies: Optional[List[CommentReply]] = Field(default=None, description="所有回复")

    # 时间信息
    create_time: str = Field(description="评价时间")
    update_time: str = Field(description="更新时间")

    # 额外信息
    is_anonymous: bool = Field(default=False, description="是否匿名评价")
    is_verified_purchase: bool = Field(default=True, description="是否验证购买")
    purchase_time: Optional[str] = Field(default=None, description="购买时间")
    device_info: Optional[str] = Field(default=None, description="设备信息")
    ip_location: Optional[str] = Field(default=None, description="IP地址")

    @property
    def has_media(self) -> bool:
        """是否包含媒体文件"""
        return bool(
            (self.images and len(self.images) > 0)
            or (self.videos and len(self.videos) > 0)
        )

    @property
    def is_good_comment(self) -> bool:
        """是否好评"""
        return self.rating in [CommentRating.FOUR_STAR, CommentRating.FIVE_STAR]

    @property
    def is_bad_comment(self) -> bool:
        """是否差评"""
        return self.rating in [CommentRating.ONE_STAR, CommentRating.TWO_STAR]

    @property
    def has_merchant_reply(self) -> bool:
        """是否有商家回复"""
        return self.merchant_reply is not None


class CommentStatistics(BaseModel):
    """评价统计"""

    # 时间范围
    begin_time: Optional[str] = Field(default=None, description="统计开始时间")
    end_time: Optional[str] = Field(default=None, description="统计结束时间")

    # 基础统计
    total_count: int = Field(description="总评价数")
    good_count: int = Field(description="好评数")
    medium_count: int = Field(description="中评数")
    bad_count: int = Field(description="差评数")

    # 评分统计
    rating_1_count: int = Field(description="1星评价数")
    rating_2_count: int = Field(description="2星评价数")
    rating_3_count: int = Field(description="3星评价数")
    rating_4_count: int = Field(description="4星评价数")
    rating_5_count: int = Field(description="5星评价数")

    # 媒体统计
    with_images_count: int = Field(description="有图评价数")
    with_videos_count: int = Field(description="有视频评价数")

    # 回复统计
    replied_count: int = Field(description="已回复评价数")
    pending_reply_count: int = Field(description="待回复评价数")

    # 质量统计
    helpful_total: int = Field(description="总有用数")
    verified_purchase_count: int = Field(description="验证购买评价数")
    anonymous_count: int = Field(description="匿名评价数")

    @property
    def good_rate(self) -> float:
        """好评率"""
        if self.total_count == 0:
            return 0.0
        return (self.good_count / self.total_count) * 100

    @property
    def bad_rate(self) -> float:
        """差评率"""
        if self.total_count == 0:
            return 0.0
        return (self.bad_count / self.total_count) * 100

    @property
    def average_rating(self) -> float:
        """平均评分"""
        if self.total_count == 0:
            return 0.0
        total_rating = (
            self.rating_1_count * 1
            + self.rating_2_count * 2
            + self.rating_3_count * 3
            + self.rating_4_count * 4
            + self.rating_5_count * 5
        )
        return total_rating / self.total_count

    @property
    def reply_rate(self) -> float:
        """回复率"""
        if self.total_count == 0:
            return 0.0
        return (self.replied_count / self.total_count) * 100

    @property
    def media_rate(self) -> float:
        """有媒体评价率"""
        if self.total_count == 0:
            return 0.0
        return (
            (self.with_images_count + self.with_videos_count) / self.total_count
        ) * 100


# ==================== 评价列表查询（严格对齐 Java） ====================


class CommentListParam(BaseModel):
    """评价列表查询参数（Java ParamDTO 对齐）"""

    out_order_no: Optional[str] = Field(None, alias="outOrderNo")
    service_score: Optional[List[int]] = Field(None, alias="serviceScore")
    quality_score: Optional[List[int]] = Field(None, alias="qualityScore")
    logistics_score: Optional[List[int]] = Field(None, alias="logisticsScore")
    offset: Optional[int] = Field(None, description="偏移量")
    limit: Optional[int] = Field(None, description="条数")
    create_time_from: Optional[int] = Field(None, alias="createTimeFrom")
    create_time_to: Optional[int] = Field(None, alias="createTimeTo")
    classify_type: Optional[int] = Field(None, alias="classifyType")
    out_item_id: Optional[int] = Field(None, alias="outItemId")
    item_title: Optional[str] = Field(None, alias="itemTitle")
    root_comment_tag: Optional[List[int]] = Field(None, alias="rootCommentTag")
    complain_status: Optional[int] = Field(None, alias="complainStatus")


class ItemCommentBaseInfo(BaseModel):
    """评价基础信息（Java: ItemCommentBaseInfo）"""

    comment_id: Optional[int] = Field(None, alias="commentId")
    item_id: Optional[int] = Field(None, alias="itemId")
    item_sku_id: Optional[int] = Field(None, alias="itemSkuId")
    order_id: Optional[int] = Field(None, alias="orderId")
    order_product_id: Optional[int] = Field(None, alias="orderProductId")
    content: Optional[str] = Field(None, alias="content")
    reply_to_comment_id: Optional[int] = Field(None, alias="replyToCommentId")
    root_comment_id: Optional[int] = Field(None, alias="rootCommentId")
    audit_status: Optional[str] = Field(None, alias="auditStatus")
    complain_status: Optional[str] = Field(None, alias="complainStatus")
    report_status: Optional[str] = Field(None, alias="reportStatus")
    cheat_status: Optional[str] = Field(None, alias="cheatStatus")
    valid: Optional[bool] = Field(None, alias="valid")
    liked: Optional[bool] = Field(None, alias="liked")
    replied: Optional[bool] = Field(None, alias="replied")
    attached: Optional[bool] = Field(None, alias="attached")
    anonymous: Optional[bool] = Field(None, alias="anonymous")
    auto: Optional[bool] = Field(None, alias="auto")
    seller_reply: Optional[bool] = Field(None, alias="sellerReply")
    credit_score: Optional[int] = Field(None, alias="creditScore")
    service_score: Optional[int] = Field(None, alias="serviceScore")
    quality_score: Optional[int] = Field(None, alias="qualityScore")
    logistics_score: Optional[int] = Field(None, alias="logisticsScore")
    image_url: Optional[List[str]] = Field(None, alias="imageUrl")
    video_id: Optional[List[int]] = Field(None, alias="videoId")
    video_cover_image_url: Optional[List[str]] = Field(None, alias="videoCoverImageUrl")
    create_time: Optional[int] = Field(None, alias="createTime")
    attached_time: Optional[int] = Field(None, alias="attachedTime")
    update_time: Optional[int] = Field(None, alias="updateTime")
    source_type: Optional[int] = Field(None, alias="sourceType")
    show_id: Optional[int] = Field(None, alias="showId")
    supply_expire_time: Optional[int] = Field(None, alias="supplyExpireTime")


class CommentListData(BaseModel):
    """评价列表数据（Java: CommentDataRes）"""

    root_comment: Optional[List[ItemCommentBaseInfo]] = Field(None, alias="rootComment")
    total: Optional[int] = Field(None, alias="total")
    hits: Optional[int] = Field(None, alias="hits")


class CommentListRequest(BaseRequest):
    """获取评价列表请求（open.comment.list.get, GET）"""

    # 与其他域保持一致，支持 ParamDTO 包装
    param: Optional[CommentListParam] = Field(None, description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.comment.list.get"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class CommentListResponse(BaseResponse[Dict[str, Any]]):
    """获取评价列表响应（对齐测试使用通用结构）"""

    pass


# ==================== 评价回复管理 ====================


class CommentReplyRequest(BaseRequest):
    """新增评价/回复请求

    对应 Java: OpenCommentAddRequest -> open.comment.add
    """

    out_info: Optional[Dict[str, Any]] = Field(
        default=None, description="外部信息", alias="outInfo"
    )
    reply_to_comment_id: Optional[int] = Field(
        default=None, description="回复的上级评价ID", alias="replyToCommentId"
    )
    content: str = Field(
        description="内容", min_length=1, max_length=1000, alias="content"
    )
    option: Optional[Dict[str, Any]] = Field(
        default=None, description="创建选项", alias="option"
    )

    @property
    def api_method(self) -> str:
        return "open.comment.add"

    # Java: HttpRequestMethod.POST
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class CommentReplyResponse(BaseResponse[Dict[str, Any]]):
    """回复评价响应"""

    pass


# ==================== 评价通知处理 ====================


class CommentNotification(BaseModel):
    """评价通知"""

    comment_id: str = Field(description="评价ID")
    item_id: str = Field(description="商品ID")
    order_id: str = Field(description="订单ID")
    user_id: int = Field(description="用户ID")
    action: str = Field(description="操作动作")  # created, updated, replied, deleted
    content: Optional[str] = Field(default=None, description="评价内容")
    rating: Optional[CommentRating] = Field(default=None, description="评价星级")
    create_time: str = Field(description="创建时间")
    sign: str = Field(description="签名")


class CommentReplyNotification(BaseModel):
    """评价回复通知"""

    reply_id: str = Field(description="回复ID")
    comment_id: str = Field(description="评价ID")
    reply_content: str = Field(description="回复内容")
    replier_type: str = Field(description="回复者类型")
    replier_name: str = Field(description="回复者名称")
    create_time: str = Field(description="回复时间")
    sign: str = Field(description="签名")


class CommentModerationNotification(BaseModel):
    """评价审核结果通知"""

    comment_id: str = Field(description="评价ID")
    action: ModerationAction = Field(description="审核操作")
    result: str = Field(description="审核结果")  # approved, rejected, hidden, deleted
    reason: Optional[str] = Field(default=None, description="审核原因")
    operator: str = Field(description="操作人")
    process_time: str = Field(description="处理时间")
    sign: str = Field(description="签名")


# ==================== Java SDK 缺失的API模型 ====================


class SubCommentInfo(BaseModel):
    """子评价信息"""

    subcomment_id: str = Field(description="子评价ID")
    parent_comment_id: str = Field(description="父评价ID")
    content: str = Field(description="子评价内容")
    user_info: CommentUser = Field(description="评价用户信息")
    create_time: str = Field(description="创建时间")
    status: CommentStatus = Field(description="状态")
    is_seller_reply: bool = Field(default=False, description="是否商家回复")
    media_list: Optional[List[CommentMedia]] = Field(
        default=None, description="媒体列表"
    )


class VirtualOrderReview(BaseModel):
    """虚拟订单审核信息"""

    order_id: str = Field(description="订单ID")
    review_code: str = Field(description="审核码")
    review_status: str = Field(description="审核状态")
    review_message: Optional[str] = Field(default=None, description="审核消息")
    review_time: Optional[str] = Field(default=None, description="审核时间")
    reviewer: Optional[str] = Field(default=None, description="审核人")


class RefundCommentInfo(BaseModel):
    """退款评价信息"""

    comment_id: str = Field(description="评价ID")
    refund_id: str = Field(description="退款ID")
    content: str = Field(description="评价内容")
    user_info: CommentUser = Field(description="用户信息")
    create_time: str = Field(description="创建时间")
    comment_type: str = Field(description="评价类型")
    media_list: Optional[List[CommentMedia]] = Field(
        default=None, description="媒体列表"
    )


class DistributorOrderCommentInfo(BaseModel):
    """分销商订单评价信息"""

    comment_id: str = Field(description="评价ID")
    order_id: str = Field(description="订单ID")
    distributor_id: str = Field(description="分销商ID")
    seller_id: str = Field(description="卖家ID")
    content: str = Field(description="评价内容")
    rating: CommentRating = Field(description="评分")
    user_info: CommentUser = Field(description="用户信息")
    create_time: str = Field(description="创建时间")
    status: CommentStatus = Field(description="状态")
    media_list: Optional[List[CommentMedia]] = Field(
        default=None, description="媒体列表"
    )
