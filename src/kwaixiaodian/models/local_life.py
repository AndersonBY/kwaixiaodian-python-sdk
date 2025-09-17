"""本地生活服务相关数据模型
基于 Java SDK 参考实现，提供本地生活订单管理功能。
"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== 本地生活订单详情相关 ====================


class LocalLifeOrderDetailParam(BaseModel):
    """本地生活订单详情查询参数"""

    order_id: str = Field(..., description="订单ID", alias="orderId")


class LocalLifeOrderDetailRequest(BaseRequest):
    """本地生活订单详情查询请求
    API: open.locallife.order.detail (GET)
    """

    param: LocalLifeOrderDetailParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.locallife.order.detail"

    # 常量 HTTP 方法（GET）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class LocalLifeOrderDetailResponse(BaseResponse[Dict[str, Any]]):
    """本地生活订单详情查询响应"""

    pass


# ==================== 本地生活订单分页相关 ====================


class LocalLifeOrderPageParam(BaseModel):
    """本地生活订单分页查询参数"""

    item_id_list: Optional[List[int]] = Field(
        None, description="商品ID列表", alias="itemIdList"
    )
    create_time_start: Optional[int] = Field(
        None, description="创建时间开始", alias="createTimeStart"
    )
    create_time_end: Optional[int] = Field(
        None, description="创建时间结束", alias="createTimeEnd"
    )
    page_num: Optional[int] = Field(None, description="页面编号", alias="pageNum")
    page_size: Optional[int] = Field(None, description="页面大小", alias="pageSize")


class LocalLifeOrderPageRequest(BaseRequest):
    """本地生活订单分页查询请求
    API: open.locallife.order.page (GET)
    """

    param: LocalLifeOrderPageParam = Field(..., description="查询参数")

    @property
    def api_method(self) -> str:
        return "open.locallife.order.page"

    # 常量 HTTP 方法（GET）
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class LocalLifeOrderPageResponse(BaseResponse[Dict[str, Any]]):
    """本地生活订单分页查询响应"""

    pass
