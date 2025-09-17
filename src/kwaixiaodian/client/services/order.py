"""订单服务类（严格对齐 Java 参考）"""

from typing import Any, Dict, List, Optional

from ...models.order import (
    DecryptBaseMetaInfo,
    DesensitiseBaseMetaInfo,
    EncryptBaseMetaInfo,
    ExternalOrderRelationRequest,
    ExternalOrderRelationResponse,
    IndexParamData,
    KsSellerOrderAddressUpdateRequest,
    KsSellerOrderAddressUpdateResponse,
    OrderAddressAuditApproveRequest,
    OrderAddressAuditRejectRequest,
    OrderAddressAuditResponse,
    OrderAddressUpdateRequest,
    OrderAddressUpdateResponse,
    OrderBuyerOrderListRequest,
    OrderBuyerOrderListResponse,
    OrderCloseRequest,
    OrderCloseResponse,
    OrderDecryptBatchRequest,
    OrderDecryptBatchResponse,
    OrderDesensitiseBatchRequest,
    OrderDesensitiseBatchResponse,
    OrderEncryptBatchRequest,
    OrderEncryptBatchResponse,
    OrderFeeDetailRequest,
    OrderFeeDetailResponse,
    OrderGetRequest,
    OrderGetResponse,
    OrderGoodsLogisticsAppendRequest,
    OrderGoodsLogisticsAppendResponse,
    OrderGoodsSplitDeliverRequest,
    OrderGoodsSplitDeliverResponse,
    OrderListEncryptParamTestRequest,
    OrderListEncryptParamTestResponse,
    OrderListRequest,
    OrderListResponse,
    OrderLogisticsUpdateRequest,
    OrderLogisticsUpdateResponse,
    OrderSearchIndexBatchRequest,
    OrderSearchIndexBatchResponse,
    OrderShipRequest,
    OrderShipResponse,
    OrderSkuUpdateRequest,
    OrderSkuUpdateResponse,
    OrderTagFlagRequest,
    OrderTagFlagResponse,
    OrderTakerateInquiryRequest,
    OrderTakerateInquiryResponse,
    OrderTokenVerifyRequest,
    OrderTokenVerifyResponse,
    OrderUpdateRemarkRequest,
    OrderUpdateRemarkResponse,
    QueryOrderKspayPromoDetailRequest,
    QueryOrderKspayPromoDetailResponse,
    SellerOrderDetailRequest,
    SellerOrderDetailResponse,
    SellerOrderPcursorListRequest,
    SellerOrderPcursorListResponse,
    SplitDeliveryGoodsPackageItemDTO,
    SplitDeliveryGoodsStatusRequest,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncOrderService:
    """异步订单服务（仅保留 Java 存在的 API）。

    - OpenAPI 范围：`open.order.*`, `open.seller.order.*`
    - Java 包：`com.kuaishou.merchant.open.api.request.order` 及 `...request`
    - 平台规则参考：`docs/开发指南和规则协议/`
    """

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def list(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        page_size: int = 20,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> OrderListResponse:
        """分页获取订单列表（游标）。

        Args:
            access_token: 访问令牌。
            begin_time: 开始时间（秒级时间戳）。
            end_time: 结束时间（秒级时间戳）。
            page_size: 每页数量。
            pcursor: 下一页游标。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderListResponse: 订单列表和下一页游标。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.cursor.list` (GET)
        Java: `OpenOrderCursorListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderCursorListRequest.java`
        """
        request = OrderListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            page_size=page_size,
            cursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, OrderListResponse)

    async def get(
        self, access_token: str, order_id: str, uid: Optional[int] = None
    ) -> OrderGetResponse:
        """获取订单详情。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID（字符串）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderGetResponse: 订单详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.detail` (GET)
        Java: `OpenOrderDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderDetailRequest.java`
        """
        request = OrderGetRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, OrderGetResponse)

    async def ship(
        self,
        access_token: str,
        order_id: int,
        express_code: int,
        express_no: str,
        return_address_id: Optional[int] = None,
        quality_param: Optional[str] = None,
        serial_number_list: Optional[List[str]] = None,
        imei_list: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> OrderShipResponse:
        """发货（更新订单发货信息）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            express_code: 快递公司编码。
            express_no: 运单号。
            return_address_id: 退货地址 ID（可选）。
            quality_param: 质检参数（可选）。
            serial_number_list: 序列号列表（可选）。
            imei_list: IMEI 列表（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderShipResponse: 发货结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.goods.deliver` (POST)
        Java: `OpenSellerOrderGoodsDeliverRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderGoodsDeliverRequest.java`
        """
        request = OrderShipRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            express_code=express_code,
            express_no=express_no,
            return_address_id=return_address_id,
            quality_param=quality_param,
            serial_number_list=serial_number_list,
            imei_list=imei_list,
            api_version="1",
        )
        return await self._client.execute(request, OrderShipResponse)

    async def update_remark(
        self,
        access_token: str,
        order_id: int,
        note: str,
        staff_id: Optional[int] = None,
        flag: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> OrderUpdateRemarkResponse:
        """新增订单备注/旗标。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            note: 备注内容（最长 500 字）。
            staff_id: 员工 ID（可选）。
            flag: 备注标记（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderUpdateRemarkResponse: 备注/旗标更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.note.add` (POST)
        Java: `OpenSellerOrderNoteAddRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderNoteAddRequest.java`
        """
        request = OrderUpdateRemarkRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            note=note,
            staff_id=staff_id,
            flag=flag,
            api_version="1",
        )
        return await self._client.execute(request, OrderUpdateRemarkResponse)

    async def close(
        self,
        access_token: str,
        order_id: int,
        uid: Optional[int] = None,
    ) -> OrderCloseResponse:
        """关闭订单。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderCloseResponse: 订单关闭结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.close` (POST)
        Java: `OpenSellerOrderCloseRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderCloseRequest.java`
        """
        request = OrderCloseRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, OrderCloseResponse)

    async def update_logistics(
        self,
        access_token: str,
        order_id: int,
        express_code: int,
        express_no: str,
        logistics_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> OrderLogisticsUpdateResponse:
        """更新订单物流信息。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            express_code: 快递公司编码。
            express_no: 运单号。
            logistics_id: 物流 ID（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderLogisticsUpdateResponse: 物流更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.logistics.update` (POST)
        Java: `KsMerchantOrderLogisticsUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantOrderLogisticsUpdateRequest.java`
        """
        request = OrderLogisticsUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            express_code=express_code,
            express_no=express_no,
            logistics_id=logistics_id,
            api_version="1",
        )
        return await self._client.execute(request, OrderLogisticsUpdateResponse)

    async def get_fee_detail(
        self, access_token: str, order_id: str, uid: Optional[int] = None
    ) -> OrderFeeDetailResponse:
        """获取订单费用明细。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID（字符串）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderFeeDetailResponse: 费用明细列表及总金额。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.fee.detail` (GET)
        Java: `OpenSellerOrderFeeDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderFeeDetailRequest.java`
        """
        request = OrderFeeDetailRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, OrderFeeDetailResponse)

    async def update_sku(
        self,
        access_token: str,
        order_id: int,
        item_id: int,
        old_sku_id: int,
        new_sku_id: int,
        uid: Optional[int] = None,
    ) -> OrderSkuUpdateResponse:
        """更换订单 SKU。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            item_id: 商品 ID。
            old_sku_id: 原 SKU ID。
            new_sku_id: 新 SKU ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderSkuUpdateResponse: SKU 更换结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.sku.update` (POST)
        Java: `OpenSellerOrderSkuUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderSkuUpdateRequest.java`
        """
        request = OrderSkuUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            item_id=item_id,
            old_sku_id=old_sku_id,
            new_sku_id=new_sku_id,
            api_version="1",
        )
        return await self._client.execute(request, OrderSkuUpdateResponse)

    async def verify_token(
        self, access_token: str, token: str, uid: Optional[int] = None
    ) -> OrderTokenVerifyResponse:
        """核验订单 token。

        Args:
            access_token: 访问令牌。
            token: 待核验的订单 token。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderTokenVerifyResponse: 令牌校验结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.token.verify` (GET)
        Java: `OpenSellerOrderTokenVerifyRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderTokenVerifyRequest.java`
        """
        request = OrderTokenVerifyRequest(
            access_token=access_token, uid=uid, token=token, api_version="1"
        )
        return await self._client.execute(request, OrderTokenVerifyResponse)

    async def address_update(
        self,
        access_token: str,
        order_id: int,
        consignee: str,
        mobile: str,
        province_code: int,
        province: str,
        city_code: int,
        city: str,
        district_code: int,
        district: str,
        address: str,
        town_code: Optional[int] = None,
        town: Optional[str] = None,
        is_partial_update: Optional[bool] = False,
        uid: Optional[int] = None,
    ) -> OrderAddressUpdateResponse:
        """更新订单收货地址。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            consignee: 收货人姓名。
            mobile: 手机号码。
            province_code: 省份代码。
            province: 省份名称。
            city_code: 城市代码。
            city: 城市名称。
            district_code: 区县代码。
            district: 区县名称。
            address: 详细地址。
            town_code: 乡镇代码（可选）。
            town: 乡镇名称（可选）。
            is_partial_update: 是否部分更新（可选，默认 False）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderAddressUpdateResponse: 地址更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.address.update` (POST)
        Java: `OpenOrderAddressUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderAddressUpdateRequest.java`
        """
        request = OrderAddressUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            consignee=consignee,
            mobile=mobile,
            province_code=province_code,
            province=province,
            city_code=city_code,
            city=city,
            district_code=district_code,
            district=district,
            address=address,
            town_code=town_code,
            town=town,
            is_partial_update=is_partial_update,
            api_version="1",
        )
        return await self._client.execute(request, OrderAddressUpdateResponse)

    async def address_audit_approve(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> OrderAddressAuditResponse:
        """审批通过地址修改。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderAddressAuditResponse: 审批结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.address.audit.approve` (GET)
        Java: `OpenOrderAddressAuditApproveRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderAddressAuditApproveRequest.java`
        """
        request = OrderAddressAuditApproveRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, OrderAddressAuditResponse)

    async def address_audit_reject(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> OrderAddressAuditResponse:
        """驳回地址修改申请。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderAddressAuditResponse: 审批结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.address.audit.reject` (GET)
        Java: `OpenOrderAddressAuditRejectRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderAddressAuditRejectRequest.java`
        """
        request = OrderAddressAuditRejectRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, OrderAddressAuditResponse)

    async def ks_seller_order_address_update(
        self,
        access_token: str,
        order_id: int,
        consignee: str,
        mobile: str,
        province_code: int,
        province: str,
        city_code: int,
        city: str,
        district_code: int,
        district: str,
        address: str,
        uid: Optional[int] = None,
    ) -> KsSellerOrderAddressUpdateResponse:
        """商家订单地址更新（KS 专用）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            consignee: 收货人姓名。
            mobile: 手机号码。
            province_code: 省份代码。
            province: 省份名称。
            city_code: 城市代码。
            city: 城市名称。
            district_code: 区域代码。
            district: 区域名称。
            address: 详细地址。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            KsSellerOrderAddressUpdateResponse: KS 卖家订单地址更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.ks.seller.order.address.update` (POST)
        Java: `OpenOrderKsSellerOrderAddressUpdateRequest`（KS 专用）
        """
        request = KsSellerOrderAddressUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            consignee=consignee,
            mobile=mobile,
            province_code=province_code,
            province=province,
            city_code=city_code,
            city=city,
            district_code=district_code,
            district=district,
            address=address,
            api_version="1",
        )
        return await self._client.execute(request, KsSellerOrderAddressUpdateResponse)

    async def decrypt_batch(
        self,
        access_token: str,
        batch_decrypt_list: List[DecryptBaseMetaInfo],
        uid: Optional[int] = None,
    ) -> OrderDecryptBatchResponse:
        """批量解密订单敏感字段。

        Args:
            access_token: 访问令牌。
            batch_decrypt_list: 批量解密请求列表。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderDecryptBatchResponse: 批量解密结果集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.decrypt.batch` (POST)
        Java: `OpenOrderDecryptBatchRequest`（模型对齐）
        """
        request = OrderDecryptBatchRequest(
            access_token=access_token,
            uid=uid,
            batch_decrypt_list=batch_decrypt_list,
            api_version="1",
        )
        return await self._client.execute(request, OrderDecryptBatchResponse)

    async def encrypt_batch(
        self,
        access_token: str,
        batch_encrypt_list: List[EncryptBaseMetaInfo],
        uid: Optional[int] = None,
    ) -> OrderEncryptBatchResponse:
        """批量加密订单敏感字段。

        Args:
            access_token: 访问令牌。
            batch_encrypt_list: 批量加密请求列表。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderEncryptBatchResponse: 批量加密结果集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.encrypt.batch` (POST)
        Java: `OpenOrderEncryptBatchRequest`（模型对齐）
        """
        request = OrderEncryptBatchRequest(
            access_token=access_token,
            uid=uid,
            batch_encrypt_list=batch_encrypt_list,
            api_version="1",
        )
        return await self._client.execute(request, OrderEncryptBatchResponse)

    async def desensitise_batch(
        self,
        access_token: str,
        batch_desensitise_list: List[DesensitiseBaseMetaInfo],
        uid: Optional[int] = None,
    ) -> OrderDesensitiseBatchResponse:
        """批量脱敏订单敏感字段。

        Args:
            access_token: 访问令牌。
            batch_desensitise_list: 批量脱敏请求列表。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderDesensitiseBatchResponse: 批量脱敏结果集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.desensitise.batch` (POST)
        Java: `OpenOrderDesensitiseBatchRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderDesensitiseBatchRequest.java`
        """
        request = OrderDesensitiseBatchRequest(
            access_token=access_token,
            uid=uid,
            batch_desensitise_list=batch_desensitise_list,
            api_version="1",
        )
        return await self._client.execute(request, OrderDesensitiseBatchResponse)

    async def search_index_batch(
        self,
        access_token: str,
        index_param_list: List[IndexParamData],
        uid: Optional[int] = None,
    ) -> OrderSearchIndexBatchResponse:
        """批量搜索订单索引。

        Args:
            access_token: 访问令牌。
            index_param_list: 索引参数列表（明文与类型）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderSearchIndexBatchResponse: 批量索引结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.search.index.batch` (POST)
        Java: `OpenOrderSearchIndexBatchRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderSearchIndexBatchRequest.java`
        """
        request = OrderSearchIndexBatchRequest(
            access_token=access_token,
            uid=uid,
            index_param_list=index_param_list,
            api_version="1",
        )
        return await self._client.execute(request, OrderSearchIndexBatchResponse)

    async def tag_flag(
        self,
        access_token: str,
        order_view_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        cps_type: Optional[int] = None,
        cursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> OrderTagFlagResponse:
        """订单标签标记查询。

        Args:
            access_token: 访问令牌。
            order_view_status: 订单查看状态（可选）。
            page_size: 每页数量（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间戳（可选）。
            end_time: 结束时间戳（可选）。
            cps_type: CPS 类型（可选）。
            cursor: 游标（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderTagFlagResponse: 订单列表、是否有更多、下一游标。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.tag.flag` (GET)
        Java: `OpenOrderTagFlagRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderTagFlagRequest.java`
        """
        request = OrderTagFlagRequest(
            access_token=access_token,
            uid=uid,
            order_view_status=order_view_status,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            cps_type=cps_type,
            cursor=cursor,
            api_version="1",
        )
        return await self._client.execute(request, OrderTagFlagResponse)

    async def takerate_inquiry(
        self,
        access_token: str,
        order_time: int,
        params: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> OrderTakerateInquiryResponse:
        """订单佣金费率查询。

        Args:
            access_token: 访问令牌。
            order_time: 订单时间戳（秒）。
            params: 附加参数映射（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderTakerateInquiryResponse: 佣金费率及详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.takerate.inquiry` (GET)
        Java: `OpenOrderTakerateInquiryRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderTakerateInquiryRequest.java`
        """
        request = OrderTakerateInquiryRequest(
            access_token=access_token,
            uid=uid,
            order_time=order_time,
            params=params,
            api_version="1",
        )
        return await self._client.execute(request, OrderTakerateInquiryResponse)

    async def goods_split_deliver(
        self,
        access_token: str,
        main_order_id: int,
        delivery_item_info_list: List[SplitDeliveryGoodsPackageItemDTO],
        delivery_status: List[SplitDeliveryGoodsStatusRequest],
        uid: Optional[int] = None,
    ) -> OrderGoodsSplitDeliverResponse:
        """拆分发货。

        Args:
            access_token: 访问令牌。
            main_order_id: 主订单 ID。
            delivery_item_info_list: 包裹与订单项发货信息列表。
            delivery_status: 发货状态列表。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderGoodsSplitDeliverResponse: 拆分发货处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.goods.split.deliver` (POST)
        Java: `OpenOrderGoodsSplitDeliverRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderGoodsSplitDeliverRequest.java`
        """
        request = OrderGoodsSplitDeliverRequest(
            access_token=access_token,
            uid=uid,
            main_order_id=main_order_id,
            delivery_item_info_list=delivery_item_info_list,
            delivery_status=delivery_status,
            api_version="1",
        )
        return await self._client.execute(request, OrderGoodsSplitDeliverResponse)

    async def list_encrypt_param_test(
        self,
        access_token: str,
        order_view_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        cps_type: Optional[int] = None,
        cursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> OrderListEncryptParamTestResponse:
        """订单列表加密参数测试。

        Args:
            access_token: 访问令牌。
            order_view_status: 订单查看状态（可选）。
            page_size: 每页数量（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间戳（可选）。
            end_time: 结束时间戳（可选）。
            cps_type: CPS 类型（可选）。
            cursor: 游标（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderListEncryptParamTestResponse: 测试响应。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.list.encrypt.param.test` (GET)
        Java: `OpenOrderListEncryptParamTestRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderListEncryptParamTestRequest.java`
        """
        request = OrderListEncryptParamTestRequest(
            access_token=access_token,
            uid=uid,
            order_view_status=order_view_status,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            cps_type=cps_type,
            cursor=cursor,
            api_version="1",
        )
        return await self._client.execute(request, OrderListEncryptParamTestResponse)

    async def append_goods_logistics(
        self,
        access_token: str,
        order_id: int,
        express_code: int,
        express_no: str,
        uid: Optional[int] = None,
    ) -> OrderGoodsLogisticsAppendResponse:
        """追加包裹物流。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            express_code: 快递公司编码。
            express_no: 运单号。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderGoodsLogisticsAppendResponse: 追加包裹物流的处理结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.goods.logistics.append` (POST)
        Java: `OpenSellerOrderGoodsLogisticsAppendRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderGoodsLogisticsAppendRequest.java`
        """
        request = OrderGoodsLogisticsAppendRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            express_code=express_code,
            express_no=express_no,
            api_version="1",
        )
        return await self._client.execute(request, OrderGoodsLogisticsAppendResponse)

    async def buyer_order_list(
        self,
        access_token: str,
        buyer_open_id: str,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        order_status: Optional[List[int]] = None,
        order_source_type: Optional[List[int]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> OrderBuyerOrderListResponse:
        """买家订单列表。

        Args:
            access_token: 访问令牌。
            buyer_open_id: 买家 openId。
            cursor: 游标（可选）。
            limit: 返回条数限制（可选）。
            order_status: 订单状态列表（可选）。
            order_source_type: 订单来源类型列表（可选）。
            start_time: 开始时间（秒级时间戳，可选）。
            end_time: 结束时间（秒级时间戳，可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderBuyerOrderListResponse: 买家订单列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.buyer.order.list` (GET)
        Java: `OpenOrderBuyerOrderListRequest`
        """
        request = OrderBuyerOrderListRequest(
            access_token=access_token,
            uid=uid,
            buyer_open_id=buyer_open_id,
            cursor=cursor,
            limit=limit,
            order_status=order_status,
            order_source_type=order_source_type,
            start_time=start_time,
            end_time=end_time,
            api_version="1",
        )
        return await self._client.execute(request, OrderBuyerOrderListResponse)

    async def get_seller_detail(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> SellerOrderDetailResponse:
        """商家订单详情。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            SellerOrderDetailResponse: 商家订单详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.detail` (GET)
        Java: `SellerOrderDetailRequest`
        """
        request = SellerOrderDetailRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, SellerOrderDetailResponse)

    async def seller_pcursor_list(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        type: Optional[int] = None,
        current_page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        cps_type: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderPcursorListResponse:
        """商家订单游标列表。

        Args:
            access_token: 访问令牌。
            begin_time: 开始时间（秒级时间戳）。
            end_time: 结束时间（秒级时间戳）。
            type: 订单类型（可选）。
            current_page: 当前页码（可选）。
            page_size: 每页数量（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            cps_type: CPS 类型（可选）。
            pcursor: 下一页游标（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            SellerOrderPcursorListResponse: 商家订单游标列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.pcursor.list` (GET)
        Java: `KsMerchantOrderListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantOrderListRequest.java`
        """
        request = SellerOrderPcursorListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            type=type,
            current_page=current_page,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            cps_type=cps_type,
            pcursor=pcursor,
            api_version="1",
        )
        return await self._client.execute(request, SellerOrderPcursorListResponse)

    async def query_kspay_promo_detail(
        self,
        access_token: str,
        order_id: Optional[int] = None,
        query_source: Optional[str] = None,
        buyer_open_id: Optional[str] = None,
        seller_open_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> QueryOrderKspayPromoDetailResponse:
        """KS 支付订单优惠详情。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID（可选）。
            query_source: 查询来源（可选）。
            buyer_open_id: 买家 openId（可选）。
            seller_open_id: 卖家 openId（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            QueryOrderKspayPromoDetailResponse: 优惠详情结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.query.order.kspay.promo.detail` (GET)
        Java: `OpenQueryOrderKspayPromoDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/kwaishop_pay/OpenQueryOrderKspayPromoDetailRequest.java`
        """
        request = QueryOrderKspayPromoDetailRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            query_source=query_source,
            buyer_open_id=buyer_open_id,
            seller_open_id=seller_open_id,
            api_version="1",
        )
        return await self._client.execute(request, QueryOrderKspayPromoDetailResponse)

    async def get_external_order_relation(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> ExternalOrderRelationResponse:
        """外部订单关系。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            ExternalOrderRelationResponse: 外部订单关系数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.external.order.relation` (GET)
        Java: `KsMerchantExternalOrderRelationRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantExternalOrderRelationRequest.java`
        """
        request = ExternalOrderRelationRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return await self._client.execute(request, ExternalOrderRelationResponse)


class SyncOrderService:
    """同步订单服务（与异步版语义一致，保留 Java 存在的 API）。"""

    def __init__(self, client: SyncBaseClient):
        self._client = client

    def list(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        page_size: int = 20,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> OrderListResponse:
        """分页获取订单列表（同步）。

        Args:
            access_token: 访问令牌。
            begin_time: 开始时间（秒级时间戳）。
            end_time: 结束时间（秒级时间戳）。
            page_size: 每页数量。
            pcursor: 下一页游标。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderListResponse: 订单列表和下一页游标。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.cursor.list` (GET)
        Java: `OpenOrderCursorListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderCursorListRequest.java`
        """
        request = OrderListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            page_size=page_size,
            cursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, OrderListResponse)

    def get(
        self, access_token: str, order_id: str, uid: Optional[int] = None
    ) -> OrderGetResponse:
        """获取订单详情（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID（字符串）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderGetResponse: 订单详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.detail` (GET)
        Java: `OpenOrderDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderDetailRequest.java`
        """
        request = OrderGetRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, OrderGetResponse)

    def ship(
        self,
        access_token: str,
        order_id: int,
        express_code: int,
        express_no: str,
        return_address_id: Optional[int] = None,
        quality_param: Optional[str] = None,
        serial_number_list: Optional[List[str]] = None,
        imei_list: Optional[List[str]] = None,
        uid: Optional[int] = None,
    ) -> OrderShipResponse:
        """发货（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            express_code: 快递公司编码。
            express_no: 运单号。
            return_address_id: 退货地址 ID（可选）。
            quality_param: 质检参数（可选）。
            serial_number_list: 序列号列表（可选）。
            imei_list: IMEI 列表（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderShipResponse: 发货结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.goods.deliver` (POST)
        Java: `OpenSellerOrderGoodsDeliverRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderGoodsDeliverRequest.java`
        """
        request = OrderShipRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            express_code=express_code,
            express_no=express_no,
            return_address_id=return_address_id,
            quality_param=quality_param,
            serial_number_list=serial_number_list,
            imei_list=imei_list,
            api_version="1",
        )
        return self._client.execute(request, OrderShipResponse)

    def update_remark(
        self,
        access_token: str,
        order_id: int,
        note: str,
        staff_id: Optional[int] = None,
        flag: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> OrderUpdateRemarkResponse:
        """新增订单备注/旗标（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            note: 备注内容（最长 500 字）。
            staff_id: 员工 ID（可选）。
            flag: 备注标记（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderUpdateRemarkResponse: 备注/旗标更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.note.add` (POST)
        Java: `OpenSellerOrderNoteAddRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderNoteAddRequest.java`
        """
        request = OrderUpdateRemarkRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            note=note,
            staff_id=staff_id,
            flag=flag,
            api_version="1",
        )
        return self._client.execute(request, OrderUpdateRemarkResponse)

    def close(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> OrderCloseResponse:
        """关闭订单（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderCloseResponse: 订单关闭结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.close` (POST)
        Java: `OpenSellerOrderCloseRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderCloseRequest.java`
        """
        request = OrderCloseRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, OrderCloseResponse)

    def update_logistics(
        self,
        access_token: str,
        order_id: int,
        express_code: int,
        express_no: str,
        logistics_id: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> OrderLogisticsUpdateResponse:
        """更新订单物流信息（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            express_code: 快递公司编码。
            express_no: 运单号。
            logistics_id: 物流 ID（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderLogisticsUpdateResponse: 物流更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.logistics.update` (POST)
        Java: `KsMerchantOrderLogisticsUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantOrderLogisticsUpdateRequest.java`
        """
        request = OrderLogisticsUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            express_code=express_code,
            express_no=express_no,
            logistics_id=logistics_id,
            api_version="1",
        )
        return self._client.execute(request, OrderLogisticsUpdateResponse)

    def get_fee_detail(
        self, access_token: str, order_id: str, uid: Optional[int] = None
    ) -> OrderFeeDetailResponse:
        """获取订单费用明细（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID（字符串）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderFeeDetailResponse: 费用明细列表及总金额。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.fee.detail` (GET)
        Java: `OpenSellerOrderFeeDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderFeeDetailRequest.java`
        """
        request = OrderFeeDetailRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, OrderFeeDetailResponse)

    def update_sku(
        self,
        access_token: str,
        order_id: int,
        item_id: int,
        old_sku_id: int,
        new_sku_id: int,
        uid: Optional[int] = None,
    ) -> OrderSkuUpdateResponse:
        """更换订单 SKU（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            item_id: 商品 ID。
            old_sku_id: 原 SKU ID。
            new_sku_id: 新 SKU ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderSkuUpdateResponse: SKU 更换结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.sku.update` (POST)
        Java: `OpenSellerOrderSkuUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderSkuUpdateRequest.java`
        """
        request = OrderSkuUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            item_id=item_id,
            old_sku_id=old_sku_id,
            new_sku_id=new_sku_id,
            api_version="1",
        )
        return self._client.execute(request, OrderSkuUpdateResponse)

    def verify_token(
        self, access_token: str, token: str, uid: Optional[int] = None
    ) -> OrderTokenVerifyResponse:
        """核验订单 token（同步）。

        Args:
            access_token: 访问令牌。
            token: 待核验的订单 token。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderTokenVerifyResponse: 令牌校验结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.token.verify` (GET)
        Java: `OpenSellerOrderTokenVerifyRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderTokenVerifyRequest.java`
        """
        request = OrderTokenVerifyRequest(
            access_token=access_token, uid=uid, token=token, api_version="1"
        )
        return self._client.execute(request, OrderTokenVerifyResponse)

    def address_update(
        self,
        access_token: str,
        order_id: int,
        consignee: str,
        mobile: str,
        province_code: int,
        province: str,
        city_code: int,
        city: str,
        district_code: int,
        district: str,
        address: str,
        town_code: Optional[int] = None,
        town: Optional[str] = None,
        is_partial_update: Optional[bool] = False,
        uid: Optional[int] = None,
    ) -> OrderAddressUpdateResponse:
        """更新订单收货地址（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            consignee: 收货人姓名。
            mobile: 手机号码。
            province_code: 省份代码。
            province: 省份名称。
            city_code: 城市代码。
            city: 城市名称。
            district_code: 区县代码。
            district: 区县名称。
            address: 详细地址。
            town_code: 乡镇代码（可选）。
            town: 乡镇名称（可选）。
            is_partial_update: 是否部分更新（可选，默认 False）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderAddressUpdateResponse: 地址更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.address.update` (POST)
        Java: `OpenOrderAddressUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderAddressUpdateRequest.java`
        """
        request = OrderAddressUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            consignee=consignee,
            mobile=mobile,
            province_code=province_code,
            province=province,
            city_code=city_code,
            city=city,
            district_code=district_code,
            district=district,
            address=address,
            town_code=town_code,
            town=town,
            is_partial_update=is_partial_update,
            api_version="1",
        )
        return self._client.execute(request, OrderAddressUpdateResponse)

    def address_audit_approve(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> OrderAddressAuditResponse:
        """审批通过地址修改（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderAddressAuditResponse: 审批结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.address.audit.approve` (GET)
        Java: `OpenOrderAddressAuditApproveRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderAddressAuditApproveRequest.java`
        """
        request = OrderAddressAuditApproveRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, OrderAddressAuditResponse)

    def address_audit_reject(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> OrderAddressAuditResponse:
        """驳回地址修改申请（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderAddressAuditResponse: 审批结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.address.audit.reject` (GET)
        Java: `OpenOrderAddressAuditRejectRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderAddressAuditRejectRequest.java`
        """
        request = OrderAddressAuditRejectRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, OrderAddressAuditResponse)

    def ks_seller_order_address_update(
        self,
        access_token: str,
        order_id: int,
        consignee: str,
        mobile: str,
        province_code: int,
        province: str,
        city_code: int,
        city: str,
        district_code: int,
        district: str,
        address: str,
        uid: Optional[int] = None,
    ) -> KsSellerOrderAddressUpdateResponse:
        """商家订单地址更新（KS 专用，同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            consignee: 收货人姓名。
            mobile: 手机号码。
            province_code: 省份代码。
            province: 省份名称。
            city_code: 城市代码。
            city: 城市名称。
            district_code: 区域代码。
            district: 区域名称。
            address: 详细地址。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            KsSellerOrderAddressUpdateResponse: KS 卖家订单地址更新结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.ks.seller.order.address.update` (POST)
        Java: `OpenOrderKsSellerOrderAddressUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderKsSellerOrderAddressUpdateRequest.java`
        """
        request = KsSellerOrderAddressUpdateRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            consignee=consignee,
            mobile=mobile,
            province_code=province_code,
            province=province,
            city_code=city_code,
            city=city,
            district_code=district_code,
            district=district,
            address=address,
            api_version="1",
        )
        return self._client.execute(request, KsSellerOrderAddressUpdateResponse)

    def decrypt_batch(
        self,
        access_token: str,
        batch_decrypt_list: List[DecryptBaseMetaInfo],
        uid: Optional[int] = None,
    ) -> OrderDecryptBatchResponse:
        """批量解密订单敏感字段（同步）

        OpenAPI: `open.order.decrypt.batch` (POST)
        Java: `com.kuaishou.merchant.open.api.request.order.OpenOrderDecryptBatchRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderDecryptBatchRequest.java)

        Args:
            access_token: 访问令牌。
            batch_decrypt_list: 批量解密请求列表（包含 `bizId` 与密文）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderDecryptBatchResponse: 批量解密结果集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = OrderDecryptBatchRequest(
            access_token=access_token,
            uid=uid,
            batch_decrypt_list=batch_decrypt_list,
            api_version="1",
        )
        return self._client.execute(request, OrderDecryptBatchResponse)

    def encrypt_batch(
        self,
        access_token: str,
        batch_encrypt_list: List[EncryptBaseMetaInfo],
        uid: Optional[int] = None,
    ) -> OrderEncryptBatchResponse:
        """批量加密订单敏感字段（同步）

        OpenAPI: `open.order.encrypt.batch` (POST)
        Java: `com.kuaishou.merchant.open.api.request.order.OpenOrderEncryptBatchRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderEncryptBatchRequest.java)

        Args:
            access_token: 访问令牌。
            batch_encrypt_list: 批量加密请求列表（包含 `bizId` 与明文）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderEncryptBatchResponse: 批量加密结果集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = OrderEncryptBatchRequest(
            access_token=access_token,
            uid=uid,
            batch_encrypt_list=batch_encrypt_list,
            api_version="1",
        )
        return self._client.execute(request, OrderEncryptBatchResponse)

    def desensitise_batch(
        self,
        access_token: str,
        batch_desensitise_list: List[DesensitiseBaseMetaInfo],
        uid: Optional[int] = None,
    ) -> OrderDesensitiseBatchResponse:
        """批量脱敏订单敏感字段（同步）。

        Args:
            access_token: 访问令牌。
            batch_desensitise_list: 批量脱敏请求列表。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderDesensitiseBatchResponse: 批量脱敏结果集合。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.desensitise.batch` (POST)
        Java: `OpenOrderDesensitiseBatchRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderDesensitiseBatchRequest.java`
        """
        request = OrderDesensitiseBatchRequest(
            access_token=access_token,
            uid=uid,
            batch_desensitise_list=batch_desensitise_list,
            api_version="1",
        )
        return self._client.execute(request, OrderDesensitiseBatchResponse)

    def search_index_batch(
        self,
        access_token: str,
        index_param_list: List[IndexParamData],
        uid: Optional[int] = None,
    ) -> OrderSearchIndexBatchResponse:
        """批量搜索订单索引（同步）。

        Args:
            access_token: 访问令牌。
            index_param_list: 索引参数列表（明文与类型）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderSearchIndexBatchResponse: 批量索引结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.search.index.batch` (POST)
        Java: `OpenOrderSearchIndexBatchRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderSearchIndexBatchRequest.java`
        """
        request = OrderSearchIndexBatchRequest(
            access_token=access_token,
            uid=uid,
            index_param_list=index_param_list,
            api_version="1",
        )
        return self._client.execute(request, OrderSearchIndexBatchResponse)

    def tag_flag(
        self,
        access_token: str,
        order_view_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        cps_type: Optional[int] = None,
        cursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> OrderTagFlagResponse:
        """订单标签标记查询（同步）。

        Args:
            access_token: 访问令牌。
            order_view_status: 订单查看状态（可选）。
            page_size: 每页数量（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间戳（可选）。
            end_time: 结束时间戳（可选）。
            cps_type: CPS 类型（可选）。
            cursor: 游标（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderTagFlagResponse: 订单列表、是否有更多、下一游标。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.tag.flag` (GET)
        Java: `OpenOrderTagFlagRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderTagFlagRequest.java`
        """
        request = OrderTagFlagRequest(
            access_token=access_token,
            uid=uid,
            order_view_status=order_view_status,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            cps_type=cps_type,
            cursor=cursor,
            api_version="1",
        )
        return self._client.execute(request, OrderTagFlagResponse)

    def takerate_inquiry(
        self,
        access_token: str,
        order_time: int,
        params: Optional[Dict[str, Any]] = None,
        uid: Optional[int] = None,
    ) -> OrderTakerateInquiryResponse:
        """订单佣金费率查询（同步）。

        Args:
            access_token: 访问令牌。
            order_time: 订单时间戳（秒）。
            params: 附加参数映射（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderTakerateInquiryResponse: 佣金费率及详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.takerate.inquiry` (GET)
        Java: `OpenOrderTakerateInquiryRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderTakerateInquiryRequest.java`
        """
        request = OrderTakerateInquiryRequest(
            access_token=access_token,
            uid=uid,
            order_time=order_time,
            params=params,
            api_version="1",
        )
        return self._client.execute(request, OrderTakerateInquiryResponse)

    def goods_split_deliver(
        self,
        access_token: str,
        main_order_id: int,
        delivery_item_info_list: List[SplitDeliveryGoodsPackageItemDTO],
        delivery_status: List[SplitDeliveryGoodsStatusRequest],
        uid: Optional[int] = None,
    ) -> OrderGoodsSplitDeliverResponse:
        """一单多包裹拆分发货（同步）

        OpenAPI: `open.order.goods.split.deliver` (POST)
        Java: `com.kuaishou.merchant.open.api.request.order.OpenOrderGoodsSplitDeliverRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderGoodsSplitDeliverRequest.java)

        Args:
            access_token: 访问令牌。
            main_order_id: 主订单 ID。
            delivery_item_info_list: 拆分包裹的明细列表。
            delivery_status: 包裹对应的发货状态集合。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderGoodsSplitDeliverResponse: 拆分发货结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。
        """
        request = OrderGoodsSplitDeliverRequest(
            access_token=access_token,
            uid=uid,
            main_order_id=main_order_id,
            delivery_item_info_list=delivery_item_info_list,
            delivery_status=delivery_status,
            api_version="1",
        )
        return self._client.execute(request, OrderGoodsSplitDeliverResponse)

    def list_encrypt_param_test(
        self,
        access_token: str,
        order_view_status: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        cps_type: Optional[int] = None,
        cursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> OrderListEncryptParamTestResponse:
        """订单列表加密参数测试（同步）。

        Args:
            access_token: 访问令牌。
            order_view_status: 订单查看状态（可选）。
            page_size: 每页数量（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            begin_time: 开始时间戳（可选）。
            end_time: 结束时间戳（可选）。
            cps_type: CPS 类型（可选）。
            cursor: 游标（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderListEncryptParamTestResponse: 测试响应。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.list.encrypt.param.test` (GET)
        Java: `OpenOrderListEncryptParamTestRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderListEncryptParamTestRequest.java`
        """
        request = OrderListEncryptParamTestRequest(
            access_token=access_token,
            uid=uid,
            order_view_status=order_view_status,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            cps_type=cps_type,
            cursor=cursor,
            api_version="1",
        )
        return self._client.execute(request, OrderListEncryptParamTestResponse)

    def append_goods_logistics(
        self,
        access_token: str,
        order_id: int,
        express_code: int,
        express_no: str,
        uid: Optional[int] = None,
    ) -> OrderGoodsLogisticsAppendResponse:
        """追加包裹物流（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            express_code: 快递公司编码。
            express_no: 运单号。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderGoodsLogisticsAppendResponse: 追加包裹物流结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.goods.logistics.append` (POST)
        Java: `OpenSellerOrderGoodsLogisticsAppendRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenSellerOrderGoodsLogisticsAppendRequest.java`
        """
        request = OrderGoodsLogisticsAppendRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            express_code=express_code,
            express_no=express_no,
            api_version="1",
        )
        return self._client.execute(request, OrderGoodsLogisticsAppendResponse)

    def buyer_order_list(
        self,
        access_token: str,
        buyer_open_id: str,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        order_status: Optional[List[int]] = None,
        order_source_type: Optional[List[int]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> OrderBuyerOrderListResponse:
        """买家订单列表（同步）。

        Args:
            access_token: 访问令牌。
            buyer_open_id: 买家 openId。
            cursor: 游标（可选）。
            limit: 返回条数限制（可选）。
            order_status: 订单状态列表（可选）。
            order_source_type: 订单来源类型列表（可选）。
            start_time: 开始时间（秒级时间戳，可选）。
            end_time: 结束时间（秒级时间戳，可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            OrderBuyerOrderListResponse: 买家订单列表与分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.order.buyer.order.list` (GET)
        Java: `com.kuaishou.merchant.open.api.request.order.OpenOrderBuyerOrderListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/order/OpenOrderBuyerOrderListRequest.java)
        """
        request = OrderBuyerOrderListRequest(
            access_token=access_token,
            uid=uid,
            buyer_open_id=buyer_open_id,
            cursor=cursor,
            limit=limit,
            order_status=order_status,
            order_source_type=order_source_type,
            start_time=start_time,
            end_time=end_time,
            api_version="1",
        )
        return self._client.execute(request, OrderBuyerOrderListResponse)

    def get_seller_detail(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> SellerOrderDetailResponse:
        """商家订单详情（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            SellerOrderDetailResponse: 商家订单详情。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.detail` (GET)
        Java: `com.kuaishou.merchant.open.api.request.KsMerchantOrderDetailRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantOrderDetailRequest.java)
        """
        request = SellerOrderDetailRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, SellerOrderDetailResponse)

    def seller_pcursor_list(
        self,
        access_token: str,
        begin_time: int,
        end_time: int,
        type: Optional[int] = None,
        current_page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[int] = None,
        query_type: Optional[int] = None,
        cps_type: Optional[int] = None,
        pcursor: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SellerOrderPcursorListResponse:
        """商家订单游标列表（同步）。

        Args:
            access_token: 访问令牌。
            begin_time: 开始时间（秒级时间戳）。
            end_time: 结束时间（秒级时间戳）。
            type: 订单类型（可选）。
            current_page: 当前页码（可选）。
            page_size: 每页数量（可选）。
            sort: 排序方式（可选）。
            query_type: 查询类型（可选）。
            cps_type: CPS 类型（可选）。
            pcursor: 下一页游标（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            SellerOrderPcursorListResponse: 商家订单游标列表。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.seller.order.pcursor.list` (GET)
        Java: `KsMerchantOrderListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantOrderListRequest.java`
        """
        request = SellerOrderPcursorListRequest(
            access_token=access_token,
            uid=uid,
            begin_time=begin_time,
            end_time=end_time,
            type=type,
            current_page=current_page,
            page_size=page_size,
            sort=sort,
            query_type=query_type,
            cps_type=cps_type,
            pcursor=pcursor,
            api_version="1",
        )
        return self._client.execute(request, SellerOrderPcursorListResponse)

    def query_kspay_promo_detail(
        self,
        access_token: str,
        order_id: Optional[int] = None,
        query_source: Optional[str] = None,
        buyer_open_id: Optional[str] = None,
        seller_open_id: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> QueryOrderKspayPromoDetailResponse:
        """KS 支付订单优惠详情（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID（可选）。
            query_source: 查询来源（可选）。
            buyer_open_id: 买家 openId（可选）。
            seller_open_id: 卖家 openId（可选）。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            QueryOrderKspayPromoDetailResponse: 优惠详情结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.query.order.kspay.promo.detail` (GET)
        Java: `OpenQueryOrderKspayPromoDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/kwaishop_pay/OpenQueryOrderKspayPromoDetailRequest.java`
        """
        request = QueryOrderKspayPromoDetailRequest(
            access_token=access_token,
            uid=uid,
            order_id=order_id,
            query_source=query_source,
            buyer_open_id=buyer_open_id,
            seller_open_id=seller_open_id,
            api_version="1",
        )
        return self._client.execute(request, QueryOrderKspayPromoDetailResponse)

    def get_external_order_relation(
        self, access_token: str, order_id: int, uid: Optional[int] = None
    ) -> ExternalOrderRelationResponse:
        """外部订单关系（同步）。

        Args:
            access_token: 访问令牌。
            order_id: 订单 ID。
            uid: 可选用户 ID（最后一个可选参数）。

        Returns:
            ExternalOrderRelationResponse: 外部订单关系数据。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或解析失败。

        OpenAPI: `open.external.order.relation` (GET)
        Java: `KsMerchantExternalOrderRelationRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantExternalOrderRelationRequest.java`
        """
        request = ExternalOrderRelationRequest(
            access_token=access_token, uid=uid, order_id=order_id, api_version="1"
        )
        return self._client.execute(request, ExternalOrderRelationResponse)
