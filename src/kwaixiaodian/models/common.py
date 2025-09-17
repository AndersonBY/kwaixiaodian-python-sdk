"""通用数据模型"""

from enum import Enum
from typing import Optional

from pydantic import Field

from .base import BaseModel


class OrderStatus(int, Enum):
    """订单状态"""

    WAIT_PAY = 1  # 待付款
    WAIT_DELIVER = 2  # 待发货
    WAIT_RECEIVE = 3  # 待收货
    FINISHED = 4  # 已完成
    CLOSED = 5  # 已关闭


class ItemStatus(int, Enum):
    """商品状态"""

    ON_SALE = 1  # 在售
    OFF_SALE = 2  # 下架
    DELETED = 3  # 已删除


class RefundStatus(int, Enum):
    """退款状态"""

    WAIT_SELLER_AGREE = 1  # 等待商家同意
    WAIT_BUYER_RETURN = 2  # 等待买家退货
    WAIT_SELLER_CONFIRM = 3  # 等待商家确认收货
    SUCCESS = 4  # 退款成功
    CLOSED = 5  # 退款关闭


class PaymentStatus(int, Enum):
    """支付状态"""

    WAIT_PAY = 1  # 待支付
    PAYING = 2  # 支付中
    PAID = 3  # 已支付
    CLOSED = 4  # 已关闭
    REFUNDED = 5  # 已退款
    PARTIAL_REFUNDED = 6  # 部分退款


class PaymentType(int, Enum):
    """支付方式"""

    WECHAT_PAY = 1  # 微信支付
    ALIPAY = 2  # 支付宝
    BANK_CARD = 3  # 银行卡
    BALANCE = 4  # 余额支付
    CREDIT = 5  # 授信支付


class Address(BaseModel):
    """地址信息"""

    receiver_name: str = Field(description="收件人姓名")
    receiver_phone: str = Field(description="收件人电话")
    province: str = Field(description="省份")
    city: str = Field(description="城市")
    county: str = Field(description="区县")
    detail: str = Field(description="详细地址")
    province_id: Optional[int] = Field(default=None, description="省份ID")
    city_id: Optional[int] = Field(default=None, description="城市ID")
    county_id: Optional[int] = Field(default=None, description="区县ID")


class LogisticsInfo(BaseModel):
    """物流信息"""

    logistics_company: str = Field(description="物流公司编码")
    tracking_number: str = Field(description="运单号")
    logistics_company_name: Optional[str] = Field(
        default=None, description="物流公司名称"
    )
    ship_time: Optional[str] = Field(default=None, description="发货时间")


class PriceInfo(BaseModel):
    """价格信息（单位：分）"""

    original_price: int = Field(description="原价")
    sell_price: int = Field(description="售价")
    discount_amount: Optional[int] = Field(default=None, description="优惠金额")

    @property
    def original_yuan(self) -> float:
        """原价（元）"""
        return self.original_price / 100

    @property
    def sell_yuan(self) -> float:
        """售价（元）"""
        return self.sell_price / 100

    @property
    def discount_yuan(self) -> Optional[float]:
        """优惠金额（元）"""
        if self.discount_amount is not None:
            return self.discount_amount / 100
        return None


class Image(BaseModel):
    """图片信息"""

    url: str = Field(description="图片URL")
    width: Optional[int] = Field(default=None, description="图片宽度")
    height: Optional[int] = Field(default=None, description="图片高度")


class UserInfo(BaseModel):
    """用户信息"""

    user_id: Optional[int] = Field(default=None, description="用户ID")
    nickname: Optional[str] = Field(default=None, description="用户昵称")
    avatar: Optional[str] = Field(default=None, description="头像URL")
    phone: Optional[str] = Field(default=None, description="手机号（脱敏）")


class ShopInfo(BaseModel):
    """店铺信息"""

    shop_id: Optional[int] = Field(default=None, description="店铺ID")
    shop_name: Optional[str] = Field(default=None, description="店铺名称")
    logo: Optional[str] = Field(default=None, description="店铺Logo")


class TimeRange(BaseModel):
    """时间范围"""

    begin_time: str = Field(description="开始时间")
    end_time: str = Field(description="结束时间")

    def __post_init__(self):
        """验证时间范围"""
        from ..utils import parse_timestamp

        begin = parse_timestamp(self.begin_time)
        end = parse_timestamp(self.end_time)

        if end <= begin:
            raise ValueError("结束时间必须晚于开始时间")


class PageInfo(BaseModel):
    """分页信息"""

    page_num: int = Field(1, description="页码", ge=1)
    page_size: int = Field(20, description="页面大小", ge=1, le=100)
    pcursor: Optional[str] = Field(default=None, description="游标")

    @property
    def offset(self) -> int:
        """偏移量"""
        return (self.page_num - 1) * self.page_size


class SortInfo(BaseModel):
    """排序信息"""

    field: str = Field(description="排序字段")
    order: str = Field("asc", description="排序方向", pattern="^(asc|desc)$")


class ApiError(BaseModel):
    """API错误信息"""

    error_code: str = Field(description="错误码")
    error_msg: str = Field(description="错误信息")
    sub_code: Optional[str] = Field(default=None, description="子错误码")
    sub_msg: Optional[str] = Field(default=None, description="子错误信息")
    request_id: Optional[str] = Field(default=None, description="请求ID")
