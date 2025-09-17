"""Shop Live models aligned with Java reference (shoplive).

Endpoints:
- open.live.shop.item.check.oncar (GET)
- open.live.shop.seller.real.uv (GET)
- open.live.shop.user.car.action (GET)
- open.live.shop.watch.time.match (GET)
"""

from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ---------- Request Models ----------


class LiveShopItemCheckOncarRequest(BaseRequest):
    """检测商品是否可上车（open.live.shop.item.check.oncar）

    Java: OpenLiveShopItemCheckOncarRequest.ParamDTO.itemId
    """

    item_id: int = Field(description="商品ID", alias="itemId")

    @property
    def api_method(self) -> str:
        return "open.live.shop.item.check.oncar"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class LiveShopSellerRealUvRequest(BaseRequest):
    """店铺直播实时UV（open.live.shop.seller.real.uv）

    Java: OpenLiveShopSellerRealUvRequest.ParamDTO (empty)
    """

    @property
    def api_method(self) -> str:
        return "open.live.shop.seller.real.uv"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class LiveShopUserCarActionRequest(BaseRequest):
    """用户购物车行为（open.live.shop.user.car.action）

    Java: OpenLiveShopUserCarActionRequest.ParamDTO.userOpenId, actionScene
    """

    user_open_id: str = Field(description="用户OpenId", alias="userOpenId")
    action_scene: Optional[List[int]] = Field(
        default=None, description="行为场景列表", alias="actionScene"
    )

    @property
    def api_method(self) -> str:
        return "open.live.shop.user.car.action"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class LiveShopWatchTimeMatchRequest(BaseRequest):
    """观看时长匹配（open.live.shop.watch.time.match）

    Java: OpenLiveShopWatchTimeMatchRequest.ParamDTO.userOpenId, threshold
    """

    user_open_id: str = Field(description="用户OpenId", alias="userOpenId")
    threshold: int = Field(description="阈值", alias="threshold")

    @property
    def api_method(self) -> str:
        return "open.live.shop.watch.time.match"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


# ---------- Response Models ----------


class CheckResult(BaseModel):
    liveCarItem: Optional[bool] = Field(default=None, description="是否可上车")


class LiveShopItemCheckOncarResponse(BaseResponse[CheckResult]):
    """检测商品是否可上车响应"""

    pass


class SellerRealUvData(BaseModel):
    realWatchUv: Optional[int] = Field(default=None, description="实时观看UV")


class LiveShopSellerRealUvResponse(BaseResponse[SellerRealUvData]):
    """店铺直播实时UV响应"""

    pass


class UserCarActionData(BaseModel):
    sceneToRes: Optional[Dict[str, Any]] = Field(
        default=None, description="场景到结果的映射"
    )


class LiveShopUserCarActionResponse(BaseResponse[UserCarActionData]):
    """用户购物车行为响应"""

    pass


class WatchTimeMatchResult(BaseModel):
    match: Optional[bool] = Field(default=None, description="是否满足阈值")


class LiveShopWatchTimeMatchResponse(BaseResponse[WatchTimeMatchResult]):
    """观看时长匹配响应"""

    pass
