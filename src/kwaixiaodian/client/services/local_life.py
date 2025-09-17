"""本地生活服务

基于 Java 参考实现，提供本地生活订单管理功能。所有方法均严格对齐
`src/kwaixiaodian/models/local_life.py` 中请求模型的 `api_method` 与
`http_method`，并标注对应的 Java 请求类与源码路径，便于排查与比对。

异常策略
- 当开放平台返回错误码或响应解析失败时，底层会抛出 `KwaixiaodianAPIError`。
"""

from typing import List, Optional

from ...models.local_life import (
    LocalLifeOrderDetailParam,
    LocalLifeOrderDetailRequest,
    LocalLifeOrderDetailResponse,
    LocalLifeOrderPageParam,
    LocalLifeOrderPageRequest,
    LocalLifeOrderPageResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncLocalLifeService:
    """异步本地生活服务

    能力
    - 订单详情查询 — OpenAPI: `open.locallife.order.detail` (GET)
    - 订单分页查询 — OpenAPI: `open.locallife.order.page` (GET)

    约定
    - `uid` 始终作为最后一个可选参数出现。
    - OpenAPI/Java 映射以 Java 参考实现为准，不引入未出现在参考中的接口。
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化本地生活服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 订单管理相关 ====================

    async def get_order_detail(
        self, access_token: str, order_id: str, uid: Optional[int] = None
    ) -> LocalLifeOrderDetailResponse:
        """获取本地生活订单详情

        OpenAPI: `open.locallife.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.locallife.OpenLocallifeOrderDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/locallife/OpenLocallifeOrderDetailRequest.java)

        Args:
            access_token: 访问令牌。
            order_id: 订单ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LocalLifeOrderDetailResponse: 订单详情响应。

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = LocalLifeOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=LocalLifeOrderDetailParam(order_id=order_id),
            api_version="1",
        )
        return await self._client.execute(req, LocalLifeOrderDetailResponse)

    async def get_order_page(
        self,
        access_token: str,
        item_id_list: Optional[List[int]] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> LocalLifeOrderPageResponse:
        """分页获取本地生活订单列表

        OpenAPI: `open.locallife.order.page` (GET)
        Java: `com.kuaishou.merchant.open.api.request.locallife.OpenLocallifeOrderPageRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/locallife/OpenLocallifeOrderPageRequest.java)

        Args:
            access_token: 访问令牌。
            item_id_list: 商品ID列表（可选）。
            create_time_start: 创建开始时间（毫秒，可选）。
            create_time_end: 创建结束时间（毫秒，可选）。
            page_num: 页码（可选）。
            page_size: 页大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LocalLifeOrderPageResponse: 订单分页列表响应。

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = LocalLifeOrderPageRequest(
            access_token=access_token,
            uid=uid,
            param=LocalLifeOrderPageParam(
                item_id_list=item_id_list,
                create_time_start=create_time_start,
                create_time_end=create_time_end,
                page_num=page_num,
                page_size=page_size,
            ),
            api_version="1",
        )
        return await self._client.execute(req, LocalLifeOrderPageResponse)


class SyncLocalLifeService:
    """同步本地生活服务

    与异步版语义一致的同步方法封装。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化同步本地生活服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 订单管理相关 ====================

    def get_order_detail(
        self, access_token: str, order_id: str, uid: Optional[int] = None
    ) -> LocalLifeOrderDetailResponse:
        """获取本地生活订单详情（同步）

        OpenAPI: `open.locallife.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.locallife.OpenLocallifeOrderDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/locallife/OpenLocallifeOrderDetailRequest.java)

        Args:
            access_token: 访问令牌。
            order_id: 订单ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LocalLifeOrderDetailResponse: 订单详情响应。

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = LocalLifeOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=LocalLifeOrderDetailParam(order_id=order_id),
            api_version="1",
        )
        return self._client.execute(req, LocalLifeOrderDetailResponse)

    def get_order_page(
        self,
        access_token: str,
        item_id_list: Optional[List[int]] = None,
        create_time_start: Optional[int] = None,
        create_time_end: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> LocalLifeOrderPageResponse:
        """分页获取本地生活订单列表（同步）

        OpenAPI: `open.locallife.order.page` (GET)
        Java: `com.kuaishou.merchant.open.api.request.locallife.OpenLocallifeOrderPageRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/locallife/OpenLocallifeOrderPageRequest.java)

        Args:
            access_token: 访问令牌。
            item_id_list: 商品ID列表（可选）。
            create_time_start: 创建开始时间（毫秒，可选）。
            create_time_end: 创建结束时间（毫秒，可选）。
            page_num: 页码（可选）。
            page_size: 页大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            LocalLifeOrderPageResponse: 订单分页列表响应。

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = LocalLifeOrderPageRequest(
            access_token=access_token,
            uid=uid,
            param=LocalLifeOrderPageParam(
                item_id_list=item_id_list,
                create_time_start=create_time_start,
                create_time_end=create_time_end,
                page_num=page_num,
                page_size=page_size,
            ),
            api_version="1",
        )
        return self._client.execute(req, LocalLifeOrderPageResponse)
