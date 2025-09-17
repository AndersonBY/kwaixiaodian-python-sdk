"""行业特化服务
基于 Java 参考实现，提供虚拟商品订单管理、二手商品用户档案查询等功能。

文档规范
- OpenAPI: 展示方法名与 HTTP 动词（来自模型 `api_method`/`http_method`）
- Java: 对应 Java Request 类与源码路径（用于交叉校验）
- Raises: `KwaixiaodianAPIError`、`KwaixiaodianValidationError`
"""

from typing import Optional

from ...models.industry import (
    SecondhandUserProfileQueryParam,
    SecondhandUserProfileQueryRequest,
    SecondhandUserProfileQueryResponse,
    VirtualOrderDecryptParam,
    VirtualOrderDecryptRequest,
    VirtualOrderDecryptResponse,
    VirtualOrderDetailParam,
    VirtualOrderDetailRequest,
    VirtualOrderDetailResponse,
    VirtualOrderReviewParam,
    VirtualOrderReviewRequest,
    VirtualOrderReviewResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncIndustryService:
    """异步行业特化服务

    提供垂直行业特化功能：
    - 虚拟商品订单详情查询
    - 虚拟商品订单审核
    - 虚拟商品订单解密
    - 二手商品用户档案查询
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化行业特化服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 虚拟商品订单管理相关 ====================

    async def get_virtual_order_detail(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> VirtualOrderDetailResponse:
        """获取虚拟商品订单详情。

        OpenAPI: `open.industry.virtual.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenIndustryVirtualOrderDetailRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenIndustryVirtualOrderDetailRequest.java`

        Args:
            access_token: 访问令牌
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            VirtualOrderDetailResponse: 虚拟商品订单详情查询响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误

        Examples:
            ```python
            resp = await industry.get_virtual_order_detail(
                access_token="your_token", order_id=123456
            )
            ```
        """
        request = VirtualOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=VirtualOrderDetailParam(order_id=order_id),
        )
        return await self._client.execute(request, VirtualOrderDetailResponse)

    async def review_virtual_order(
        self,
        access_token: str,
        review_code: int,
        order_id: int,
        uid: Optional[int] = None,
    ) -> VirtualOrderReviewResponse:
        """审核虚拟商品订单。

        OpenAPI: `open.industry.virtual.order.review` (POST)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenIndustryVirtualOrderReviewRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenIndustryVirtualOrderReviewRequest.java`

        Args:
            access_token: 访问令牌
            review_code: 审核状态码
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            VirtualOrderReviewResponse: 虚拟商品订单审核响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = VirtualOrderReviewRequest(
            access_token=access_token,
            uid=uid,
            param=VirtualOrderReviewParam(review_code=review_code, order_id=order_id),
        )
        return await self._client.execute(request, VirtualOrderReviewResponse)

    async def decrypt_virtual_order(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> VirtualOrderDecryptResponse:
        """解密虚拟商品订单。

        OpenAPI: `open.industry.virtual.order.decrypt` (POST)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenIndustryVirtualOrderDecryptRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenIndustryVirtualOrderDecryptRequest.java`

        Args:
            access_token: 访问令牌
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            VirtualOrderDecryptResponse: 虚拟商品订单解密响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = VirtualOrderDecryptRequest(
            access_token=access_token,
            uid=uid,
            param=VirtualOrderDecryptParam(order_id=order_id),
        )
        return await self._client.execute(request, VirtualOrderDecryptResponse)

    # ==================== 二手商品相关 ====================

    async def query_secondhand_user_profile(
        self, access_token: str, open_id: str, uid: Optional[int] = None
    ) -> SecondhandUserProfileQueryResponse:
        """查询二手用户档案。

        OpenAPI: `open.secondhand.wwdz.user.profile.query` (GET)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenSecondhandWwdzUserProfileQueryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenSecondhandWwdzUserProfileQueryRequest.java`

        Args:
            access_token: 访问令牌
            open_id: 用户开放ID
            uid: 用户ID（可选）

        Returns:
            SecondhandUserProfileQueryResponse: 二手用户档案查询响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = SecondhandUserProfileQueryRequest(
            access_token=access_token,
            uid=uid,
            param=SecondhandUserProfileQueryParam(open_id=open_id),
        )
        return await self._client.execute(request, SecondhandUserProfileQueryResponse)


class SyncIndustryService:
    """同步行业特化服务

    提供垂直行业特化功能的同步版本。
    """

    def __init__(self, client: SyncBaseClient):
        """初始化同步行业特化服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    # ==================== 虚拟商品订单管理相关 ====================

    def get_virtual_order_detail(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> VirtualOrderDetailResponse:
        """获取虚拟商品订单详情 (同步)。

        OpenAPI: `open.industry.virtual.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenIndustryVirtualOrderDetailRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenIndustryVirtualOrderDetailRequest.java`

        Args:
            access_token: 访问令牌
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            VirtualOrderDetailResponse: 虚拟商品订单详情查询响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = VirtualOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=VirtualOrderDetailParam(order_id=order_id),
        )
        return self._client.execute(request, VirtualOrderDetailResponse)

    def review_virtual_order(
        self,
        access_token: str,
        review_code: int,
        order_id: int,
        uid: Optional[int] = None,
    ) -> VirtualOrderReviewResponse:
        """审核虚拟商品订单 (同步)。

        OpenAPI: `open.industry.virtual.order.review` (POST)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenIndustryVirtualOrderReviewRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenIndustryVirtualOrderReviewRequest.java`

        Args:
            access_token: 访问令牌
            review_code: 审核状态码
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            VirtualOrderReviewResponse: 虚拟商品订单审核响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = VirtualOrderReviewRequest(
            access_token=access_token,
            uid=uid,
            param=VirtualOrderReviewParam(review_code=review_code, order_id=order_id),
        )
        return self._client.execute(request, VirtualOrderReviewResponse)

    def decrypt_virtual_order(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> VirtualOrderDecryptResponse:
        """解密虚拟商品订单 (同步)。

        OpenAPI: `open.industry.virtual.order.decrypt` (POST)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenIndustryVirtualOrderDecryptRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenIndustryVirtualOrderDecryptRequest.java`

        Args:
            access_token: 访问令牌
            order_id: 订单ID
            uid: 用户ID（可选）

        Returns:
            VirtualOrderDecryptResponse: 虚拟商品订单解密响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = VirtualOrderDecryptRequest(
            access_token=access_token,
            uid=uid,
            param=VirtualOrderDecryptParam(order_id=order_id),
        )
        return self._client.execute(request, VirtualOrderDecryptResponse)

    # ==================== 二手商品相关 ====================

    def query_secondhand_user_profile(
        self, access_token: str, open_id: str, uid: Optional[int] = None
    ) -> SecondhandUserProfileQueryResponse:
        """查询二手用户档案 (同步)。

        OpenAPI: `open.secondhand.wwdz.user.profile.query` (GET)
        Java: `com.kuaishou.merchant.open.api.request.industry.OpenSecondhandWwdzUserProfileQueryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/industry/OpenSecondhandWwdzUserProfileQueryRequest.java`

        Args:
            access_token: 访问令牌
            open_id: 用户开放ID
            uid: 用户ID（可选）

        Returns:
            SecondhandUserProfileQueryResponse: 二手用户档案查询响应

        Raises:
            KwaixiaodianValidationError: 参数缺失或非法
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = SecondhandUserProfileQueryRequest(
            access_token=access_token,
            uid=uid,
            param=SecondhandUserProfileQueryParam(open_id=open_id),
        )
        return self._client.execute(request, SecondhandUserProfileQueryResponse)
