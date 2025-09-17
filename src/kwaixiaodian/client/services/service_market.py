"""服务市场服务
基于 Java 参考实现；服务方法接收显式参数并内部构建请求。
"""

from typing import Optional

from ...models.service_market import (
    ServiceMarketBuyerServiceInfoParam,
    ServiceMarketBuyerServiceInfoRequest,
    ServiceMarketBuyerServiceInfoResponse,
    ServiceMarketOrderDetailParam,
    ServiceMarketOrderDetailRequest,
    ServiceMarketOrderDetailResponse,
    ServiceMarketOrderListParam,
    ServiceMarketOrderListRequest,
    ServiceMarketOrderListResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncServiceMarketService:
    """异步服务市场服务（对齐 Java SDK 与开放平台）。

    - OpenAPI 范围：`open.service.market.*`
    - Java 包：`com.kuaishou.merchant.open.api.request.servicemarket`
    - 规则与协议：见 `docs/开发指南和规则协议/`。
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化服务市场服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 服务订单管理相关 ====================

    async def get_service_order_list(
        self,
        access_token: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        query_type: Optional[int] = None,
        status: Optional[int] = None,
        page_size: Optional[int] = None,
        page_num: Optional[int] = None,
        buyer_open_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ServiceMarketOrderListResponse:
        """获取服务订单列表。

        Args:
            access_token: 访问令牌。
            start_time: 开始时间（秒级时间戳）。
            end_time: 结束时间（秒级时间戳）。
            query_type: 查询类型（平台定义）。
            status: 订单状态。
            page_size: 每页数量。
            page_num: 页码。
            buyer_open_id: 买家 openId。
            uid: 可选用户 ID。

        Returns:
            ServiceMarketOrderListResponse: 服务订单列表。

        OpenAPI: `open.service.market.order.list` (GET)
        Java: `OpenServiceMarketOrderListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/servicemarket/OpenServiceMarketOrderListRequest.java`
        """

        request = ServiceMarketOrderListRequest(
            access_token=access_token,
            uid=uid,
            param=ServiceMarketOrderListParam(
                start_time=start_time,
                end_time=end_time,
                query_type=query_type,
                status=status,
                page_size=page_size,
                page_num=page_num,
                buyer_open_id=buyer_open_id,
            ),
            api_version="1",
        )

        return await self._client.execute(request, ServiceMarketOrderListResponse)

    async def get_service_order_detail(
        self, access_token: str, oid: int, uid: Optional[int] = None
    ) -> ServiceMarketOrderDetailResponse:
        """获取服务订单详情。

        Args:
            access_token: 访问令牌。
            oid: 服务订单 ID。
            uid: 可选用户 ID。

        Returns:
            ServiceMarketOrderDetailResponse: 服务订单详情。

        OpenAPI: `open.service.market.order.detail` (GET)
        Java: `OpenServiceMarketOrderDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/servicemarket/OpenServiceMarketOrderDetailRequest.java`
        """

        request = ServiceMarketOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=ServiceMarketOrderDetailParam(oid=oid),
            api_version="1",
        )

        return await self._client.execute(request, ServiceMarketOrderDetailResponse)

    async def get_buyer_service_info(
        self, access_token: str, buyer_open_id: str, uid: Optional[int] = None
    ) -> ServiceMarketBuyerServiceInfoResponse:
        """获取买家服务信息。

        Args:
            access_token: 访问令牌。
            buyer_open_id: 买家 openId。
            uid: 可选用户 ID。

        Returns:
            ServiceMarketBuyerServiceInfoResponse: 买家服务信息。

        OpenAPI: `open.service.market.buyer.service.info` (GET)
        Java: `OpenServiceMarketBuyerServiceInfoRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/servicemarket/OpenServiceMarketBuyerServiceInfoRequest.java`
        """

        request = ServiceMarketBuyerServiceInfoRequest(
            access_token=access_token,
            uid=uid,
            param=ServiceMarketBuyerServiceInfoParam(buyer_open_id=buyer_open_id),
            api_version="1",
        )
        return await self._client.execute(
            request, ServiceMarketBuyerServiceInfoResponse
        )


class SyncServiceMarketService:
    """同步服务市场服务（语义与异步版本一致，OpenAPI/Java 映射相同）。"""

    def __init__(self, client: SyncBaseClient):
        """初始化同步服务市场服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 服务订单管理相关 ====================

    def get_service_order_list(
        self,
        access_token: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        query_type: Optional[int] = None,
        status: Optional[int] = None,
        page_size: Optional[int] = None,
        page_num: Optional[int] = None,
        buyer_open_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ServiceMarketOrderListResponse:
        """获取服务订单列表（同步）。

        OpenAPI: `open.service.market.order.list` (GET)
        Java: `com.kuaishou.merchant.open.api.request.servicemarket.OpenServiceMarketOrderListRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/servicemarket/OpenServiceMarketOrderListRequest.java`)

        Args:
            access_token: 访问令牌
            start_time: 开始时间（秒级时间戳，可选）
            end_time: 结束时间（秒级时间戳，可选）
            query_type: 查询类型（平台定义，可选）
            status: 订单状态（可选）
            page_size: 每页数量（可选）
            page_num: 页码（可选）
            buyer_open_id: 买家 openId（可选）
            uid: 用户ID（可选）

        Returns:
            ServiceMarketOrderListResponse: 服务订单列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = ServiceMarketOrderListRequest(
            access_token=access_token,
            uid=uid,
            param=ServiceMarketOrderListParam(
                start_time=start_time,
                end_time=end_time,
                query_type=query_type,
                status=status,
                page_size=page_size,
                page_num=page_num,
                buyer_open_id=buyer_open_id,
            ),
            api_version="1",
        )
        return self._client.execute(request, ServiceMarketOrderListResponse)

    def get_service_order_detail(
        self, access_token: str, oid: int, uid: Optional[int] = None
    ) -> ServiceMarketOrderDetailResponse:
        """获取服务订单详情（同步）。

        OpenAPI: `open.service.market.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.servicemarket.OpenServiceMarketOrderDetailRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/servicemarket/OpenServiceMarketOrderDetailRequest.java`)

        Args:
            access_token: 访问令牌
            oid: 服务订单ID
            uid: 用户ID（可选）

        Returns:
            ServiceMarketOrderDetailResponse: 服务订单详情

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = ServiceMarketOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=ServiceMarketOrderDetailParam(oid=oid),
            api_version="1",
        )
        return self._client.execute(request, ServiceMarketOrderDetailResponse)

    def get_buyer_service_info(
        self, access_token: str, buyer_open_id: str, uid: Optional[int] = None
    ) -> ServiceMarketBuyerServiceInfoResponse:
        """获取买家服务信息（同步）。

        OpenAPI: `open.service.market.buyer.service.info` (GET)
        Java: `com.kuaishou.merchant.open.api.request.servicemarket.OpenServiceMarketBuyerServiceInfoRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/servicemarket/OpenServiceMarketBuyerServiceInfoRequest.java`)

        Args:
            access_token: 访问令牌
            buyer_open_id: 买家 openId
            uid: 用户ID（可选）

        Returns:
            ServiceMarketBuyerServiceInfoResponse: 买家服务信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = ServiceMarketBuyerServiceInfoRequest(
            access_token=access_token,
            uid=uid,
            param=ServiceMarketBuyerServiceInfoParam(buyer_open_id=buyer_open_id),
            api_version="1",
        )
        return self._client.execute(request, ServiceMarketBuyerServiceInfoResponse)
