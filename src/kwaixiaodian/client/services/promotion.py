"""Promotion service (aligned with Java reference).

Exposes open.promotion.* endpoints for coupon/crowd/seller/shop and order detail.
"""

from typing import List, Optional

from ...models.promotion import (
    PromotionCouponCreateParam,
    PromotionCouponCreateRequest,
    PromotionCouponDeleteRequest,
    PromotionCouponIdParam,
    PromotionCouponIdsParam,
    PromotionCouponOverRequest,
    PromotionCouponPageListParam,
    PromotionCouponPageListRequest,
    PromotionCouponQueryRequest,
    PromotionCouponSendParam,
    PromotionCouponSendRequest,
    PromotionCouponStatisticParam,
    PromotionCouponStatisticRequest,
    PromotionCouponStockAddParam,
    PromotionCouponStockAddRequest,
    PromotionCrowdCreateParam,
    PromotionCrowdCreateRequest,
    PromotionCrowdDetailParam,
    PromotionCrowdDetailRequest,
    PromotionCrowdEditParam,
    PromotionCrowdEditRequest,
    PromotionCrowdListParam,
    PromotionCrowdListRequest,
    PromotionCrowdPredictParam,
    PromotionCrowdPredictRequest,
    PromotionCrowdUpdateParam,
    PromotionCrowdUpdateRequest,
    PromotionGenericResponse,
    PromotionOrderDetailParam,
    PromotionOrderDetailRequest,
    PromotionSellerStatisticParam,
    PromotionSellerStatisticRequest,
    PromotionShopNewbieCreateParam,
    PromotionShopNewbieCreateRequest,
    TagCondition,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncPromotionService:
    """营销推广服务（对齐 Java 参考）

    范围
    - 优惠券：open.promotion.coupon.*
    - 人群：open.promotion.crowd.*
    - 统计：open.promotion.seller.statistic
    - 新客：open.promotion.shop.newbie.create
    - 订单：open.promotion.order.detail

    说明
    - OpenAPI 对齐：以 `src/kwaixiaodian/models/promotion.py` 请求模型的
      `api_method` 与 `http_method` 为准，并与 Java 参考严格映射。
    - Java 参考路径：`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/promotion/` 等。
    - 异常：请求失败或平台返回错误码时，底层会抛出 `KwaixiaodianAPIError`。
    """

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    # -------------------- Coupon --------------------
    async def create_coupon(
        self, access_token: str, uid: Optional[int] = None, **kwargs
    ):
        """创建优惠券

        OpenAPI: open.promotion.coupon.create (POST)
        Java: PromotionCouponCreateRequest
            (java_sdk_reference/.../request/promotion/PromotionCouponCreateRequest.java)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选；保持为最后一个可选参数）
            **kwargs: 透传至 `PromotionCouponCreateParam` 的各字段

        Returns:
            PromotionGenericResponse: 创建结果

        Raises:
            KwaixiaodianAPIError: 当平台返回错误码或解析失败。
        """
        req = PromotionCouponCreateRequest(
            access_token=access_token, uid=uid, param=PromotionCouponCreateParam(**kwargs), api_version="1"
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def delete_coupon(
        self, access_token: str, coupon_id: int, uid: Optional[int] = None
    ):
        """删除优惠券

        OpenAPI: open.promotion.coupon.delete (POST)
        Java: PromotionCouponDeleteRequest

        Args:
            access_token: 访问令牌
            coupon_id: 优惠券ID
            uid: 用户ID（可选）

        Returns:
            PromotionGenericResponse: 删除结果
        """
        req = PromotionCouponDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponIdParam(coupon_id=coupon_id),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def over_coupon(
        self, access_token: str, coupon_id: int, uid: Optional[int] = None
    ):
        """结束优惠券投放

        OpenAPI: `open.promotion.coupon.over` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponOverRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponOverRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 结束投放结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponOverRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponIdParam(coupon_id=coupon_id),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def page_list_coupons(
        self,
        access_token: str,
        coupon_target_type: Optional[int] = None,
        page_no: Optional[int] = None,
        seller_coupon_status: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """分页查询优惠券

        OpenAPI: `open.promotion.coupon.page.list` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponPageListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponPageListRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_target_type: 优惠券目标类型（可选）。
            page_no: 页码（可选）。
            seller_coupon_status: 优惠券状态（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 分页数据与统计信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponPageListRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponPageListParam(
                coupon_target_type=coupon_target_type,
                page_no=page_no,
                seller_coupon_status=seller_coupon_status,
                page_size=page_size,
            ),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def query_coupons(
        self, access_token: str, coupon_ids: List[int], uid: Optional[int] = None
    ):
        """批量查询优惠券详情

        OpenAPI: `open.promotion.coupon.query` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponQueryRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponQueryRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_ids: 优惠券ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 优惠券详情集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponQueryRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponIdsParam(coupon_id=coupon_ids),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def send_coupon(
        self,
        access_token: str,
        coupon_config_id: int,
        outer_id: Optional[str] = None,
        receive_channel: Optional[int] = None,
        user_open_id: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """发放优惠券

        OpenAPI: `open.promotion.coupon.send` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponSendRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponSendRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_config_id: 优惠券配置ID。
            outer_id: 外部业务ID（可选）。
            receive_channel: 领取渠道（可选）。
            user_open_id: 用户OpenId（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 发放结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponSendRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponSendParam(
                coupon_config_id=coupon_config_id,
                outer_id=outer_id,
                receive_channel=receive_channel,
                user_open_id=user_open_id,
            ),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def get_coupon_statistic(
        self,
        access_token: str,
        coupon_id: int,
        business_line: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """获取优惠券统计

        OpenAPI: `open.promotion.coupon.statistic` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponStatisticRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponStatisticRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            business_line: 业务线（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 统计结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponStatisticRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponStatisticParam(coupon_id=coupon_id, business_line=business_line),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def add_coupon_stock(
        self,
        access_token: str,
        coupon_id: int,
        increment_num: int,
        uid: Optional[int] = None,
    ):
        """追加优惠券库存

        OpenAPI: `open.promotion.coupon.stock.add` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponStockAddRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponStockAddRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            increment_num: 增加库存数量。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 增加库存处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponStockAddRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponStockAddParam(coupon_id=coupon_id, increment_num=increment_num),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    # -------------------- Crowd --------------------
    async def create_crowd(
        self,
        access_token: str,
        crowd_name: str,
        crowd_desc: Optional[str] = None,
        tag_condition: Optional[List[TagCondition]] = None,
        ext_json: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """创建人群

        OpenAPI: `open.promotion.crowd.create` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdCreateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdCreateRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_name: 人群名称。
            crowd_desc: 人群描述（可选）。
            tag_condition: 标签条件集合（可选）。
            ext_json: 扩展JSON（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdCreateRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdCreateParam(
                crowd_name=crowd_name,
                crowd_desc=crowd_desc,
                tag_condition=tag_condition,
                ext_json=ext_json,
            ),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def update_crowd(
        self,
        access_token: str,
        crowd_id: int,
        ext_json: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """更新人群扩展信息

        OpenAPI: `open.promotion.crowd.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdUpdateRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_id: 人群ID。
            ext_json: 扩展JSON（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdUpdateRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdUpdateParam(crowd_id=crowd_id, ext_json=ext_json),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def edit_crowd(
        self,
        access_token: str,
        crowd_id: int,
        crowd_name: str,
        crowd_desc: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """编辑人群基础信息

        OpenAPI: `open.promotion.crowd.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdEditRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_id: 人群ID。
            crowd_name: 人群名称。
            crowd_desc: 人群描述（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 编辑结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdEditRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdEditParam(
                crowd_id=crowd_id,
                crowd_name=crowd_name,
                crowd_desc=crowd_desc,
            ),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def get_crowd_detail(
        self, access_token: str, crowd_id: int, uid: Optional[int] = None
    ):
        """查询人群详情

        OpenAPI: `open.promotion.crowd.detail` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdDetailRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_id: 人群ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 人群详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdDetailRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdDetailParam(crowd_id=crowd_id),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def list_crowds(
        self,
        access_token: str,
        crowd_type: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """分页查询人群

        OpenAPI: `open.promotion.crowd.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdListRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_type: 人群类型（可选）。
            page_num: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 人群分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdListRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdListParam(crowd_type=crowd_type, page_num=page_num, page_size=page_size),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def predict_crowd(
        self,
        access_token: str,
        tag_condition: Optional[List[TagCondition]] = None,
        ext_json: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """预估人群规模

        OpenAPI: `open.promotion.crowd.predict` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdPredictRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdPredictRequest.java)

        Args:
            access_token: 访问令牌。
            tag_condition: 标签条件集合（可选）。
            ext_json: 扩展JSON（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 规模预估结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdPredictRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdPredictParam(tag_condition=tag_condition, ext_json=ext_json),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    # -------------------- Stats/Shop/Order --------------------
    async def seller_statistic(
        self,
        access_token: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        business_line: Optional[int] = None,
        coupon_target: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """商家优惠券统计

        OpenAPI: `open.promotion.seller.statistic` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionSellerStatisticRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionSellerStatisticRequest.java)

        Args:
            access_token: 访问令牌。
            start_time: 开始时间（毫秒，可选）。
            end_time: 结束时间（毫秒，可选）。
            business_line: 业务线（可选）。
            coupon_target: 优惠券目标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 统计数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionSellerStatisticRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionSellerStatisticParam(
                start_time=start_time,
                end_time=end_time,
                business_line=business_line,
                coupon_target=coupon_target,
            ),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def shop_newbie_create(
        self,
        access_token: str,
        coupon_target_type: int,
        item_id: List[int],
        coupon_price: int,
        coupon_end: int,
        coupon_front_type: int,
        coupon_base: int,
        status: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """创建店铺新客优惠配置

        OpenAPI: `open.promotion.shop.newbie.create` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionShopNewbieCreateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionShopNewbieCreateRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_target_type: 优惠券目标类型。
            item_id: 商品ID列表。
            coupon_price: 优惠券面额（分）。
            coupon_end: 结束时间（毫秒）。
            coupon_front_type: 展示类型。
            coupon_base: 使用门槛（分）。
            status: 状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionShopNewbieCreateRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionShopNewbieCreateParam(
                coupon_target_type=coupon_target_type,
                item_id=item_id,
                coupon_price=coupon_price,
                coupon_end=coupon_end,
                coupon_front_type=coupon_front_type,
                coupon_base=coupon_base,
                status=status,
            ),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)

    async def order_detail(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ):
        """查询订单推广明细

        OpenAPI: `open.promotion.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.KsMerchantPromotionDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantPromotionDetailRequest.java)

        Args:
            access_token: 访问令牌。
            order_id: 订单ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 推广明细数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionOrderDetailParam(order_id=order_id),
            api_version="1",
        )
        return await self._client.execute(req, PromotionGenericResponse)


class SyncPromotionService:
    """营销推广服务（同步版）

    文档风格与异步版一致，API 与 Java 映射一致。
    """

    def __init__(self, client: SyncBaseClient):
        self._client = client

    # The sync versions mirror the async implementations
    def create_coupon(self, access_token: str, uid: Optional[int] = None, **kwargs):
        """创建优惠券

        OpenAPI: open.promotion.coupon.create (POST)
        Java: PromotionCouponCreateRequest
        """
        req = PromotionCouponCreateRequest(
            access_token=access_token, uid=uid, param=PromotionCouponCreateParam(**kwargs), api_version="1"
        )
        return self._client.execute(req, PromotionGenericResponse)

    def delete_coupon(
        self, access_token: str, coupon_id: int, uid: Optional[int] = None
    ):
        """删除优惠券（同步）

        OpenAPI: `open.promotion.coupon.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponDeleteRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponIdParam(coupon_id=coupon_id),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def over_coupon(self, access_token: str, coupon_id: int, uid: Optional[int] = None):
        """结束优惠券投放（同步）

        OpenAPI: `open.promotion.coupon.over` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponOverRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponOverRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 结束投放结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponOverRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponIdParam(coupon_id=coupon_id),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def page_list_coupons(
        self,
        access_token: str,
        coupon_target_type: Optional[int] = None,
        page_no: Optional[int] = None,
        seller_coupon_status: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """分页查询优惠券（同步）

        OpenAPI: `open.promotion.coupon.page.list` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponPageListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponPageListRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_target_type: 优惠券目标类型（可选）。
            page_no: 页码（可选）。
            seller_coupon_status: 优惠券状态（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 分页数据与统计信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponPageListRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponPageListParam(
                coupon_target_type=coupon_target_type,
                page_no=page_no,
                seller_coupon_status=seller_coupon_status,
                page_size=page_size,
            ),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def query_coupons(
        self, access_token: str, coupon_ids: List[int], uid: Optional[int] = None
    ):
        """批量查询优惠券（同步）

        OpenAPI: `open.promotion.coupon.query` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponQueryRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponQueryRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_ids: 优惠券ID列表。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 优惠券详情集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponQueryRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponIdsParam(coupon_id=coupon_ids),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def send_coupon(
        self,
        access_token: str,
        coupon_config_id: int,
        outer_id: Optional[str] = None,
        receive_channel: Optional[int] = None,
        user_open_id: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """发放优惠券（同步）

        OpenAPI: `open.promotion.coupon.send` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponSendRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponSendRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_config_id: 优惠券配置ID。
            outer_id: 外部业务ID（可选）。
            receive_channel: 领取渠道（可选）。
            user_open_id: 用户OpenId（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 发放结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponSendRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponSendParam(
                coupon_config_id=coupon_config_id,
                outer_id=outer_id,
                receive_channel=receive_channel,
                user_open_id=user_open_id,
            ),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def get_coupon_statistic(
        self,
        access_token: str,
        coupon_id: int,
        business_line: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """获取优惠券统计（同步）

        OpenAPI: `open.promotion.coupon.statistic` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponStatisticRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponStatisticRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            business_line: 业务线（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 统计结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponStatisticRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponStatisticParam(coupon_id=coupon_id, business_line=business_line),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def add_coupon_stock(
        self,
        access_token: str,
        coupon_id: int,
        increment_num: int,
        uid: Optional[int] = None,
    ):
        """追加优惠券库存（同步）

        OpenAPI: `open.promotion.coupon.stock.add` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCouponStockAddRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCouponStockAddRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_id: 优惠券ID。
            increment_num: 增加库存数量。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 增加库存处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCouponStockAddRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCouponStockAddParam(coupon_id=coupon_id, increment_num=increment_num),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def create_crowd(
        self,
        access_token: str,
        crowd_name: str,
        crowd_desc: Optional[str] = None,
        tag_condition: Optional[List[TagCondition]] = None,
        ext_json: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """创建人群（同步）

        OpenAPI: `open.promotion.crowd.create` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdCreateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdCreateRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_name: 人群名称。
            crowd_desc: 人群描述（可选）。
            tag_condition: 标签条件集合（可选）。
            ext_json: 扩展JSON（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdCreateRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdCreateParam(
                crowd_name=crowd_name,
                crowd_desc=crowd_desc,
                tag_condition=tag_condition,
                ext_json=ext_json,
            ),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def update_crowd(
        self,
        access_token: str,
        crowd_id: int,
        ext_json: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """更新人群扩展信息（同步）

        OpenAPI: `open.promotion.crowd.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdUpdateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdUpdateRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_id: 人群ID。
            ext_json: 扩展JSON（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdUpdateRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdUpdateParam(crowd_id=crowd_id, ext_json=ext_json),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def edit_crowd(
        self,
        access_token: str,
        crowd_id: int,
        crowd_name: str,
        crowd_desc: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """编辑人群（同步）

        OpenAPI: `open.promotion.crowd.edit` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdEditRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdEditRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_id: 人群ID。
            crowd_name: 人群名称。
            crowd_desc: 人群描述（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 编辑结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdEditRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdEditParam(
                crowd_id=crowd_id,
                crowd_name=crowd_name,
                crowd_desc=crowd_desc,
            ),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def get_crowd_detail(
        self, access_token: str, crowd_id: int, uid: Optional[int] = None
    ):
        """查询人群详情（同步）

        OpenAPI: `open.promotion.crowd.detail` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdDetailRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_id: 人群ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 人群详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdDetailRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdDetailParam(crowd_id=crowd_id),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def list_crowds(
        self,
        access_token: str,
        crowd_type: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """分页查询人群（同步）

        OpenAPI: `open.promotion.crowd.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdListRequest.java)

        Args:
            access_token: 访问令牌。
            crowd_type: 人群类型（可选）。
            page_num: 页码（可选）。
            page_size: 页面大小（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 人群分页数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdListRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdListParam(crowd_type=crowd_type, page_num=page_num, page_size=page_size),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def predict_crowd(
        self,
        access_token: str,
        tag_condition: Optional[List[TagCondition]] = None,
        ext_json: Optional[str] = None,
        uid: Optional[int] = None,
    ):
        """预估人群规模（同步）

        OpenAPI: `open.promotion.crowd.predict` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionCrowdPredictRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionCrowdPredictRequest.java)

        Args:
            access_token: 访问令牌。
            tag_condition: 标签条件集合（可选）。
            ext_json: 扩展JSON（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 规模预估结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionCrowdPredictRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionCrowdPredictParam(tag_condition=tag_condition, ext_json=ext_json),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def seller_statistic(
        self,
        access_token: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        business_line: Optional[int] = None,
        coupon_target: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """商家优惠券统计（同步）

        OpenAPI: `open.promotion.seller.statistic` (GET)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionSellerStatisticRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionSellerStatisticRequest.java)

        Args:
            access_token: 访问令牌。
            start_time: 开始时间（毫秒，可选）。
            end_time: 结束时间（毫秒，可选）。
            business_line: 业务线（可选）。
            coupon_target: 优惠券目标（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 统计数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionSellerStatisticRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionSellerStatisticParam(
                start_time=start_time,
                end_time=end_time,
                business_line=business_line,
                coupon_target=coupon_target,
            ),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def shop_newbie_create(
        self,
        access_token: str,
        coupon_target_type: int,
        item_id: List[int],
        coupon_price: int,
        coupon_end: int,
        coupon_front_type: int,
        coupon_base: int,
        status: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """创建店铺新客优惠配置（同步）

        OpenAPI: `open.promotion.shop.newbie.create` (POST)
        Java: `com.kuaishou.merchant.open.api.request.OpenPromotionShopNewbieCreateRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/OpenPromotionShopNewbieCreateRequest.java)

        Args:
            access_token: 访问令牌。
            coupon_target_type: 优惠券目标类型。
            item_id: 商品ID列表。
            coupon_price: 优惠券面额（分）。
            coupon_end: 结束时间（毫秒）。
            coupon_front_type: 展示类型。
            coupon_base: 使用门槛（分）。
            status: 状态（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 创建结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionShopNewbieCreateRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionShopNewbieCreateParam(
                coupon_target_type=coupon_target_type,
                item_id=item_id,
                coupon_price=coupon_price,
                coupon_end=coupon_end,
                coupon_front_type=coupon_front_type,
                coupon_base=coupon_base,
                status=status,
            ),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)

    def order_detail(self, access_token: str, order_id: int, uid: Optional[int] = None):
        """查询订单推广明细（同步）

        OpenAPI: `open.promotion.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.KsMerchantPromotionDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantPromotionDetailRequest.java)

        Args:
            access_token: 访问令牌。
            order_id: 订单ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PromotionGenericResponse: 推广明细数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        req = PromotionOrderDetailRequest(
            access_token=access_token,
            uid=uid,
            param=PromotionOrderDetailParam(order_id=order_id),
            api_version="1",
        )
        return self._client.execute(req, PromotionGenericResponse)
