"""直播服务（对齐 Java shoplive 能力，仅保留 open.live.shop.*）"""

from typing import Optional

from ...models.live_shop import (
    LiveShopItemCheckOncarRequest,
    LiveShopItemCheckOncarResponse,
    LiveShopSellerRealUvRequest,
    LiveShopSellerRealUvResponse,
    LiveShopUserCarActionRequest,
    LiveShopUserCarActionResponse,
    LiveShopWatchTimeMatchRequest,
    LiveShopWatchTimeMatchResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncLiveService:
    """异步直播服务（shoplive）"""

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def check_item_oncar(
        self, access_token: str, item_id: int, uid: Optional[int] = None
    ) -> LiveShopItemCheckOncarResponse:
        """检测商品是否可上车

        OpenAPI: `open.live.shop.item.check.oncar` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopItemCheckOncarRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopItemCheckOncarRequest.java)

        Args:
            access_token: 访问令牌。
            item_id: 商品ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopItemCheckOncarResponse: 可上车检测结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopItemCheckOncarRequest(
            access_token=access_token, uid=uid, item_id=item_id, api_version="1"
        )
        return await self._client.execute(request, LiveShopItemCheckOncarResponse)

    async def get_seller_real_uv(
        self, access_token: str, uid: Optional[int] = None
    ) -> LiveShopSellerRealUvResponse:
        """获取店铺直播实时UV

        OpenAPI: `open.live.shop.seller.real.uv` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopSellerRealUvRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopSellerRealUvRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopSellerRealUvResponse: 实时UV数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopSellerRealUvRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return await self._client.execute(request, LiveShopSellerRealUvResponse)

    async def get_user_car_action(
        self,
        access_token: str,
        user_open_id: str,
        action_scene: Optional[list[int]] = None,
        uid: Optional[int] = None,
    ) -> LiveShopUserCarActionResponse:
        """查询用户购物车行为

        OpenAPI: `open.live.shop.user.car.action` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopUserCarActionRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopUserCarActionRequest.java)

        Args:
            access_token: 访问令牌。
            user_open_id: 用户 OpenId。
            action_scene: 行为场景列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopUserCarActionResponse: 行为场景到结果的映射。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopUserCarActionRequest(
            access_token=access_token,
            uid=uid,
            user_open_id=user_open_id,
            action_scene=action_scene,
            api_version="1",
        )
        return await self._client.execute(request, LiveShopUserCarActionResponse)

    async def match_watch_time(
        self,
        access_token: str,
        user_open_id: str,
        threshold: int,
        uid: Optional[int] = None,
    ) -> LiveShopWatchTimeMatchResponse:
        """匹配用户观看时长阈值

        OpenAPI: `open.live.shop.watch.time.match` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopWatchTimeMatchRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopWatchTimeMatchRequest.java)

        Args:
            access_token: 访问令牌。
            user_open_id: 用户 OpenId。
            threshold: 阈值（单位与平台定义一致）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopWatchTimeMatchResponse: 是否满足阈值的判断结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopWatchTimeMatchRequest(
            access_token=access_token,
            uid=uid,
            user_open_id=user_open_id,
            threshold=threshold,
            api_version="1",
        )
        return await self._client.execute(request, LiveShopWatchTimeMatchResponse)


class SyncLiveService:
    """同步直播服务（shoplive）"""

    def __init__(self, client: SyncBaseClient):
        self._client = client

    def check_item_oncar(
        self, access_token: str, item_id: int, uid: Optional[int] = None
    ) -> LiveShopItemCheckOncarResponse:
        """检测商品是否可上车（同步）

        OpenAPI: `open.live.shop.item.check.oncar` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopItemCheckOncarRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopItemCheckOncarRequest.java)

        Args:
            access_token: 访问令牌。
            item_id: 商品ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopItemCheckOncarResponse: 可上车检测结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopItemCheckOncarRequest(
            access_token=access_token, uid=uid, item_id=item_id, api_version="1"
        )
        return self._client.execute(request, LiveShopItemCheckOncarResponse)

    def get_seller_real_uv(
        self, access_token: str, uid: Optional[int] = None
    ) -> LiveShopSellerRealUvResponse:
        """获取店铺直播实时UV（同步）

        OpenAPI: `open.live.shop.seller.real.uv` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopSellerRealUvRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopSellerRealUvRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopSellerRealUvResponse: 实时UV数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopSellerRealUvRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return self._client.execute(request, LiveShopSellerRealUvResponse)

    def get_user_car_action(
        self,
        access_token: str,
        user_open_id: str,
        action_scene: Optional[list[int]] = None,
        uid: Optional[int] = None,
    ) -> LiveShopUserCarActionResponse:
        """查询用户购物车行为（同步）

        OpenAPI: `open.live.shop.user.car.action` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopUserCarActionRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopUserCarActionRequest.java)

        Args:
            access_token: 访问令牌。
            user_open_id: 用户 OpenId。
            action_scene: 行为场景列表（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopUserCarActionResponse: 行为场景到结果的映射。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopUserCarActionRequest(
            access_token=access_token,
            uid=uid,
            user_open_id=user_open_id,
            action_scene=action_scene,
            api_version="1",
        )
        return self._client.execute(request, LiveShopUserCarActionResponse)

    def match_watch_time(
        self,
        access_token: str,
        user_open_id: str,
        threshold: int,
        uid: Optional[int] = None,
    ) -> LiveShopWatchTimeMatchResponse:
        """匹配用户观看时长阈值（同步）

        OpenAPI: `open.live.shop.watch.time.match` (GET)
        Java: `com.kuaishou.merchant.open.api.request.shoplive.OpenLiveShopWatchTimeMatchRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/shoplive/OpenLiveShopWatchTimeMatchRequest.java)

        Args:
            access_token: 访问令牌。
            user_open_id: 用户 OpenId。
            threshold: 阈值（单位与平台定义一致）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LiveShopWatchTimeMatchResponse: 是否满足阈值的判断结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = LiveShopWatchTimeMatchRequest(
            access_token=access_token,
            uid=uid,
            user_open_id=user_open_id,
            threshold=threshold,
            api_version="1",
        )
        return self._client.execute(request, LiveShopWatchTimeMatchResponse)
