"""行业特化服务相关数据模型
基于 Java SDK 参考实现，提供虚拟商品订单管理、二手商品用户档案查询等功能。
"""

from typing import Any, ClassVar, Dict

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== 虚拟商品订单详情相关 ====================


class VirtualOrderDetailParam(BaseModel):
    """虚拟商品订单详情查询参数"""

    order_id: int = Field(..., description="订单ID")


class VirtualOrderDetailRequest(BaseRequest):
    """虚拟商品订单详情查询请求
    API: open.industry.virtual.order.detail (GET)
    """

    param: VirtualOrderDetailParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.industry.virtual.order.detail"

    # 常量 HTTP 方法（GET）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class VirtualOrderDetailResponse(BaseResponse[Dict[str, Any]]):
    """虚拟商品订单详情查询响应"""

    pass


# ==================== 虚拟商品订单审核相关 ====================


class VirtualOrderReviewParam(BaseModel):
    """虚拟商品订单审核参数"""

    review_code: int = Field(..., description="审核状态码")
    order_id: int = Field(..., description="订单ID")


class VirtualOrderReviewRequest(BaseRequest):
    """虚拟商品订单审核请求
    API: open.industry.virtual.order.review (POST)
    """

    param: VirtualOrderReviewParam = Field(..., description="审核参数")

    @property
    def api_method(self) -> str:
        return "open.industry.virtual.order.review"

    # 常量 HTTP 方法（POST）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class VirtualOrderReviewResponse(BaseResponse[Dict[str, Any]]):
    """虚拟商品订单审核响应"""

    pass


# ==================== 虚拟商品订单解密相关 ====================


class VirtualOrderDecryptParam(BaseModel):
    """虚拟商品订单解密参数"""

    order_id: int = Field(..., description="订单ID")


class VirtualOrderDecryptRequest(BaseRequest):
    """虚拟商品订单解密请求
    API: open.industry.virtual.order.decrypt (POST)
    """

    param: VirtualOrderDecryptParam = Field(..., description="解密参数")

    @property
    def api_method(self) -> str:
        return "open.industry.virtual.order.decrypt"

    # 常量 HTTP 方法（POST）
    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class VirtualOrderDecryptResponse(BaseResponse[Dict[str, Any]]):
    """虚拟商品订单解密响应"""

    pass


# ==================== 二手商品用户档案查询相关 ====================


class SecondhandUserProfileQueryParam(BaseModel):
    """二手用户档案查询参数"""

    open_id: str = Field(..., description="用户开放ID")


class SecondhandUserProfileQueryRequest(BaseRequest):
    """二手用户档案查询请求
    API: open.secondhand.wwdz.user.profile.query (GET)
    """

    param: SecondhandUserProfileQueryParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.secondhand.wwdz.user.profile.query"

    # 常量 HTTP 方法（GET）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondhandUserProfileQueryResponse(BaseResponse[Dict[str, Any]]):
    """二手用户档案查询响应"""

    pass
