"""代发服务客户端

基于 Java SDK 参考实现的代发服务API封装，支持异步和同步调用。
"""

from typing import List, Optional

from kwaixiaodian.models.dropshipping import (
    AppendDropshippingOrderRequest,
    ApplyBindFactoryInfo,
    DsOrderGetRequest,
    EbillBatchGetRequest,
    EbillBatchGetResponse,
    EbillCancelRequest,
    EbillCancelResponse,
    OrderBatchAllocateCancelRequest,
    OrderBatchAllocateCancelResponse,
    OrderBatchAllocateRequest,
    OrderBatchAllocateResponse,
    OrderBatchAppendRequest,
    OrderBatchAppendResponse,
    OrderBatchDeleteRequest,
    OrderBatchDeleteResponse,
    OrderDeliverRequest,
    OrderDeliverResponse,
    OrderDetailQueryRequest,
    OrderDetailQueryResponse,
    OrderListRequest,
    OrderListResponse,
    OrderLogisticsUpdateRequest,
    OrderLogisticsUpdateResponse,
    OrderMerchantDetailRequest,
    OrderMerchantDetailResponse,
    OrderMerchantListRequest,
    OrderMerchantListResponse,
    RelationListRequest,
    RelationListResponse,
    RelationMerchantBatchApplyRequest,
    RelationMerchantBatchApplyResponse,
    RelationMerchantBatchUnbindRequest,
    RelationMerchantBatchUnbindResponse,
    RoleQueryRequest,
    RoleQueryResponse,
    UnbindFactoryInfo,
)


class AsyncDropshippingService:
    """异步代发服务（严格对齐 Java SDK 与文档）。

    - 不新增臆测端点；以 `models.dropshipping` 的 `api_method` 与 `http_method` 为准
    - 每个方法提供 OpenAPI 方法名 + HTTP 动词，Java 请求类与反编译源码路径
    - Raises 统一说明可能出现的 `KwaixiaodianAPIError`
    """

    def __init__(self, client):
        self._client = client

    async def batch_get_ebill(
        self,
        access_token: str,
        ds_order_get_req: Optional[List[DsOrderGetRequest]] = None,
    ) -> EbillBatchGetResponse:
        """批量获取电子面单。

        OpenAPI: `open.dropshipping.ebill.batch.get` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingEbillBatchGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingEbillBatchGetRequest.java`

        Args:
            access_token: 访问令牌
            ds_order_get_req: 电子面单获取请求列表

        Returns:
            电子面单批量获取响应

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = EbillBatchGetRequest(
            access_token=access_token,
            ds_order_get_req=ds_order_get_req,
        )
        return await self._client.execute(request, EbillBatchGetResponse)

    async def cancel_ebill(
        self,
        access_token: str,
        waybill_code: Optional[str] = None,
        express_company_code: Optional[str] = None,
        user_code: Optional[str] = None,
    ) -> EbillCancelResponse:
        """取消电子面单。

        OpenAPI: `open.dropshipping.ebill.cancel` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingEbillCancelRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingEbillCancelRequest.java`

        Args:
            access_token: 访问令牌
            waybill_code: 运单号
            express_company_code: 快递公司编码
            user_code: 用户编码

        Returns:
            取消结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = EbillCancelRequest(
            access_token=access_token,
            waybill_code=waybill_code,
            express_company_code=express_company_code,
            user_code=user_code,
        )
        return await self._client.execute(request, EbillCancelResponse)

    async def batch_allocate_order(
        self,
        access_token: str,
        dropshipping_order_code_list: Optional[List[str]] = None,
        factory_code: Optional[str] = None,
    ) -> OrderBatchAllocateResponse:
        """批量分配订单。

        OpenAPI: `open.dropshipping.order.batch.allocate` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchAllocateRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchAllocateRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code_list: 代发订单编码列表
            factory_code: 工厂编码

        Returns:
            批量分配结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchAllocateRequest(
            access_token=access_token,
            dropshipping_order_code_list=dropshipping_order_code_list,
            factory_code=factory_code,
        )
        return await self._client.execute(request, OrderBatchAllocateResponse)

    async def cancel_batch_allocate_order(
        self,
        access_token: str,
        dropshipping_order_code_list: Optional[List[str]] = None,
        cancel_allocate_reason: Optional[str] = None,
    ) -> OrderBatchAllocateCancelResponse:
        """取消批量分配订单。

        OpenAPI: `open.dropshipping.order.batch.allocate.cancel` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchAllocateCancelRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchAllocateCancelRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code_list: 代发订单编码列表
            cancel_allocate_reason: 取消分配原因

        Returns:
            取消结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchAllocateCancelRequest(
            access_token=access_token,
            dropshipping_order_code_list=dropshipping_order_code_list,
            cancel_allocate_reason=cancel_allocate_reason,
        )
        return await self._client.execute(request, OrderBatchAllocateCancelResponse)

    async def batch_append_order(
        self,
        access_token: str,
        append_request_list: Optional[List[AppendDropshippingOrderRequest]] = None,
    ) -> OrderBatchAppendResponse:
        """批量追加订单。

        OpenAPI: `open.dropshipping.order.batch.append` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchAppendRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchAppendRequest.java`

        Args:
            access_token: 访问令牌
            append_request_list: 追加请求列表

        Returns:
            批量追加结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchAppendRequest(
            access_token=access_token,
            append_request_list=append_request_list,
        )
        return await self._client.execute(request, OrderBatchAppendResponse)

    async def batch_delete_order(
        self,
        access_token: str,
        dropshipping_order_code_list: Optional[List[str]] = None,
    ) -> OrderBatchDeleteResponse:
        """批量删除订单。

        OpenAPI: `open.dropshipping.order.batch.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchDeleteRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchDeleteRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code_list: 代发订单编码列表

        Returns:
            批量删除结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchDeleteRequest(
            access_token=access_token,
            dropshipping_order_code_list=dropshipping_order_code_list,
        )
        return await self._client.execute(request, OrderBatchDeleteResponse)

    async def deliver_order(
        self,
        access_token: str,
        return_address_id: Optional[int] = None,
        waybill_code: Optional[str] = None,
        user_code: Optional[str] = None,
        allocate_order_code: Optional[str] = None,
        express_company_code: Optional[str] = None,
        serial_number_list: Optional[List[str]] = None,
        imei_list: Optional[List[str]] = None,
    ) -> OrderDeliverResponse:
        """订单发货。

        OpenAPI: `open.dropshipping.order.deliver` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderDeliverRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderDeliverRequest.java`

        Args:
            access_token: 访问令牌
            return_address_id: 退货地址ID
            waybill_code: 运单号
            user_code: 用户编码
            allocate_order_code: 分配订单编码
            express_company_code: 快递公司编码
            serial_number_list: 序列号列表
            imei_list: IMEI 列表

        Returns:
            发货结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderDeliverRequest(
            access_token=access_token,
            return_address_id=return_address_id,
            waybill_code=waybill_code,
            user_code=user_code,
            allocate_order_code=allocate_order_code,
            express_company_code=express_company_code,
            serial_number_list=serial_number_list,
            imei_list=imei_list,
        )
        return await self._client.execute(request, OrderDeliverResponse)

    async def query_order_detail(
        self,
        access_token: str,
        allocate_order_code: Optional[str] = None,
        user_code: Optional[str] = None,
    ) -> OrderDetailQueryResponse:
        """查询订单详情。

        OpenAPI: `open.dropshipping.order.detail.query` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderDetailQueryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderDetailQueryRequest.java`

        Args:
            access_token: 访问令牌
            allocate_order_code: 分配订单编码
            user_code: 用户编码

        Returns:
            订单详情

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderDetailQueryRequest(
            access_token=access_token,
            allocate_order_code=allocate_order_code,
            user_code=user_code,
        )
        return await self._client.execute(request, OrderDetailQueryResponse)

    async def list_orders(
        self,
        access_token: str,
        page_size: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        query_type: Optional[int] = None,
        sort: Optional[int] = None,
        allocate_status: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> OrderListResponse:
        """查询订单列表。

        OpenAPI: `open.dropshipping.order.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderListRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderListRequest.java`

        Args:
            access_token: 访问令牌
            page_size: 页面大小
            begin_time: 开始时间（毫秒）
            end_time: 结束时间（毫秒）
            query_type: 查询类型
            sort: 排序
            allocate_status: 分配状态
            cursor: 游标

        Returns:
            订单列表

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderListRequest(
            access_token=access_token,
            page_size=page_size,
            begin_time=begin_time,
            end_time=end_time,
            query_type=query_type,
            sort=sort,
            allocate_status=allocate_status,
            cursor=cursor,
        )
        return await self._client.execute(request, OrderListResponse)

    async def update_order_logistics(
        self,
        access_token: str,
        waybill_code: Optional[str] = None,
        express_company_code: Optional[str] = None,
        user_code: Optional[str] = None,
        allocate_order_code: Optional[str] = None,
    ) -> OrderLogisticsUpdateResponse:
        """更新订单物流信息。

        OpenAPI: `open.dropshipping.order.logistics.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderLogisticsUpdateRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderLogisticsUpdateRequest.java`

        Args:
            access_token: 访问令牌
            waybill_code: 运单号
            express_company_code: 快递公司编码
            user_code: 用户编码
            allocate_order_code: 分配订单编码

        Returns:
            更新结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderLogisticsUpdateRequest(
            access_token=access_token,
            waybill_code=waybill_code,
            express_company_code=express_company_code,
            user_code=user_code,
            allocate_order_code=allocate_order_code,
        )
        return await self._client.execute(request, OrderLogisticsUpdateResponse)

    async def query_order_merchant_detail(
        self,
        access_token: str,
        dropshipping_order_code: Optional[str] = None,
    ) -> OrderMerchantDetailResponse:
        """查询订单商家详情。

        OpenAPI: `open.dropshipping.order.merchant.detail` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderMerchantDetailRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderMerchantDetailRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code: 代发订单编码

        Returns:
            商家详情

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderMerchantDetailRequest(
            access_token=access_token,
            dropshipping_order_code=dropshipping_order_code,
        )
        return await self._client.execute(request, OrderMerchantDetailResponse)

    async def list_order_merchants(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        page_size: Optional[int] = None,
        factory_code: Optional[str] = None,
        dropshipping_status: Optional[int] = None,
        order_status: Optional[int] = None,
        refund_status: Optional[int] = None,
        order_type: Optional[int] = None,
        query_type: Optional[str] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        sort: Optional[int] = None,
    ) -> OrderMerchantListResponse:
        """查询订单商家列表。

        OpenAPI: `open.dropshipping.order.merchant.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderMerchantListRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderMerchantListRequest.java`

        Args:
            access_token: 访问令牌
            cursor: 游标
            page_size: 页面大小
            factory_code: 工厂编码
            dropshipping_status: 代发状态
            order_status: 订单状态
            refund_status: 退款状态
            order_type: 订单类型
            query_type: 查询类型
            begin_time: 开始时间（毫秒）
            end_time: 结束时间（毫秒）
            sort: 排序

        Returns:
            商家列表

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderMerchantListRequest(
            access_token=access_token,
            cursor=cursor,
            page_size=page_size,
            factory_code=factory_code,
            dropshipping_status=dropshipping_status,
            order_status=order_status,
            refund_status=refund_status,
            order_type=order_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            sort=sort,
        )
        return await self._client.execute(request, OrderMerchantListResponse)

    async def list_relations(
        self,
        access_token: str,
        factory_code: Optional[str] = None,
        begin_apply_time: Optional[int] = None,
        end_apply_time: Optional[int] = None,
        page_index: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> RelationListResponse:
        """查询工厂-商家关系列表。

        OpenAPI: `open.dropshipping.relation.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRelationListRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRelationListRequest.java`

        Args:
            access_token: 访问令牌
            factory_code: 工厂编码
            begin_apply_time: 开始申请时间（毫秒）
            end_apply_time: 结束申请时间（毫秒）
            page_index: 页索引
            page_size: 页大小

        Returns:
            关系列表

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RelationListRequest(
            access_token=access_token,
            factory_code=factory_code,
            begin_apply_time=begin_apply_time,
            end_apply_time=end_apply_time,
            page_index=page_index,
            page_size=page_size,
        )
        return await self._client.execute(request, RelationListResponse)

    async def batch_apply_merchant_relation(
        self,
        access_token: str,
        apply_request_list: Optional[List[ApplyBindFactoryInfo]] = None,
    ) -> RelationMerchantBatchApplyResponse:
        """批量申请商家关系。

        OpenAPI: `open.dropshipping.relation.merchant.batch.apply` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRelationMerchantBatchApplyRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRelationMerchantBatchApplyRequest.java`

        Args:
            access_token: 访问令牌
            apply_request_list: 申请请求列表

        Returns:
            申请结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RelationMerchantBatchApplyRequest(
            access_token=access_token,
            apply_request_list=apply_request_list,
        )
        return await self._client.execute(request, RelationMerchantBatchApplyResponse)

    async def batch_unbind_merchant_relation(
        self,
        access_token: str,
        unbind_request_list: Optional[List[UnbindFactoryInfo]] = None,
    ) -> RelationMerchantBatchUnbindResponse:
        """批量解绑商家关系。

        OpenAPI: `open.dropshipping.relation.merchant.batch.unbind` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRelationMerchantBatchUnbindRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRelationMerchantBatchUnbindRequest.java`

        Args:
            access_token: 访问令牌
            unbind_request_list: 解绑请求列表

        Returns:
            解绑结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RelationMerchantBatchUnbindRequest(
            access_token=access_token,
            unbind_request_list=unbind_request_list,
        )
        return await self._client.execute(request, RelationMerchantBatchUnbindResponse)

    async def query_role(
        self,
        access_token: str,
    ) -> RoleQueryResponse:
        """查询当前账号的代发角色。

        OpenAPI: `open.dropshipping.role.query` (GET)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRoleQueryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRoleQueryRequest.java`

        Args:
            access_token: 访问令牌

        Returns:
            角色查询结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RoleQueryRequest(
            access_token=access_token,
        )
        return await self._client.execute(request, RoleQueryResponse)


class SyncDropshippingService:
    """同步代发服务（严格对齐 Java SDK 与文档）。"""

    def __init__(self, client):
        self._client = client

    def batch_get_ebill(
        self,
        access_token: str,
        ds_order_get_req: Optional[List[DsOrderGetRequest]] = None,
    ) -> EbillBatchGetResponse:
        """批量获取电子面单（同步）。

        OpenAPI: `open.dropshipping.ebill.batch.get` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingEbillBatchGetRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingEbillBatchGetRequest.java`

        Args:
            access_token: 访问令牌
            ds_order_get_req: 电子面单获取请求列表

        Returns:
            电子面单批量获取响应

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = EbillBatchGetRequest(
            access_token=access_token,
            ds_order_get_req=ds_order_get_req,
        )
        return self._client.execute(request, EbillBatchGetResponse)

    def cancel_ebill(
        self,
        access_token: str,
        waybill_code: Optional[str] = None,
        express_company_code: Optional[str] = None,
        user_code: Optional[str] = None,
    ) -> EbillCancelResponse:
        """取消电子面单（同步）。

        OpenAPI: `open.dropshipping.ebill.cancel` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingEbillCancelRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingEbillCancelRequest.java`

        Args:
            access_token: 访问令牌
            waybill_code: 运单号
            express_company_code: 快递公司编码
            user_code: 用户编码

        Returns:
            取消结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = EbillCancelRequest(
            access_token=access_token,
            waybill_code=waybill_code,
            express_company_code=express_company_code,
            user_code=user_code,
        )
        return self._client.execute(request, EbillCancelResponse)

    def batch_allocate_order(
        self,
        access_token: str,
        dropshipping_order_code_list: Optional[List[str]] = None,
        factory_code: Optional[str] = None,
    ) -> OrderBatchAllocateResponse:
        """批量分配订单（同步）。

        OpenAPI: `open.dropshipping.order.batch.allocate` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchAllocateRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchAllocateRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code_list: 代发订单编码列表
            factory_code: 工厂编码

        Returns:
            批量分配结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchAllocateRequest(
            access_token=access_token,
            dropshipping_order_code_list=dropshipping_order_code_list,
            factory_code=factory_code,
        )
        return self._client.execute(request, OrderBatchAllocateResponse)

    def cancel_batch_allocate_order(
        self,
        access_token: str,
        dropshipping_order_code_list: Optional[List[str]] = None,
        cancel_allocate_reason: Optional[str] = None,
    ) -> OrderBatchAllocateCancelResponse:
        """取消批量分配订单（同步）。

        OpenAPI: `open.dropshipping.order.batch.allocate.cancel` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchAllocateCancelRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchAllocateCancelRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code_list: 代发订单编码列表
            cancel_allocate_reason: 取消分配原因

        Returns:
            取消结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchAllocateCancelRequest(
            access_token=access_token,
            dropshipping_order_code_list=dropshipping_order_code_list,
            cancel_allocate_reason=cancel_allocate_reason,
        )
        return self._client.execute(request, OrderBatchAllocateCancelResponse)

    def batch_append_order(
        self,
        access_token: str,
        append_request_list: Optional[List[AppendDropshippingOrderRequest]] = None,
    ) -> OrderBatchAppendResponse:
        """批量追加订单（同步）。

        OpenAPI: `open.dropshipping.order.batch.append` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchAppendRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchAppendRequest.java`

        Args:
            access_token: 访问令牌
            append_request_list: 追加请求列表

        Returns:
            批量追加结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchAppendRequest(
            access_token=access_token,
            append_request_list=append_request_list,
        )
        return self._client.execute(request, OrderBatchAppendResponse)

    def batch_delete_order(
        self,
        access_token: str,
        dropshipping_order_code_list: Optional[List[str]] = None,
    ) -> OrderBatchDeleteResponse:
        """批量删除订单（同步）。

        OpenAPI: `open.dropshipping.order.batch.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderBatchDeleteRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderBatchDeleteRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code_list: 代发订单编码列表

        Returns:
            批量删除结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderBatchDeleteRequest(
            access_token=access_token,
            dropshipping_order_code_list=dropshipping_order_code_list,
        )
        return self._client.execute(request, OrderBatchDeleteResponse)

    def deliver_order(
        self,
        access_token: str,
        return_address_id: Optional[int] = None,
        waybill_code: Optional[str] = None,
        user_code: Optional[str] = None,
        allocate_order_code: Optional[str] = None,
        express_company_code: Optional[str] = None,
        serial_number_list: Optional[List[str]] = None,
        imei_list: Optional[List[str]] = None,
    ) -> OrderDeliverResponse:
        """订单发货（同步）。

        OpenAPI: `open.dropshipping.order.deliver` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderDeliverRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderDeliverRequest.java`

        Args:
            access_token: 访问令牌
            return_address_id: 退货地址ID
            waybill_code: 运单号
            user_code: 用户编码
            allocate_order_code: 分配订单编码
            express_company_code: 快递公司编码
            serial_number_list: 序列号列表
            imei_list: IMEI 列表

        Returns:
            发货结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderDeliverRequest(
            access_token=access_token,
            return_address_id=return_address_id,
            waybill_code=waybill_code,
            user_code=user_code,
            allocate_order_code=allocate_order_code,
            express_company_code=express_company_code,
            serial_number_list=serial_number_list,
            imei_list=imei_list,
        )
        return self._client.execute(request, OrderDeliverResponse)

    def query_order_detail(
        self,
        access_token: str,
        allocate_order_code: Optional[str] = None,
        user_code: Optional[str] = None,
    ) -> OrderDetailQueryResponse:
        """查询订单详情（同步）。

        OpenAPI: `open.dropshipping.order.detail.query` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderDetailQueryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderDetailQueryRequest.java`

        Args:
            access_token: 访问令牌
            allocate_order_code: 分配订单编码
            user_code: 用户编码

        Returns:
            订单详情

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderDetailQueryRequest(
            access_token=access_token,
            allocate_order_code=allocate_order_code,
            user_code=user_code,
        )
        return self._client.execute(request, OrderDetailQueryResponse)

    def list_orders(
        self,
        access_token: str,
        page_size: Optional[int] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        query_type: Optional[int] = None,
        sort: Optional[int] = None,
        allocate_status: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> OrderListResponse:
        """查询订单列表（同步）。

        OpenAPI: `open.dropshipping.order.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderListRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderListRequest.java`

        Args:
            access_token: 访问令牌
            page_size: 页面大小
            begin_time: 开始时间（毫秒）
            end_time: 结束时间（毫秒）
            query_type: 查询类型
            sort: 排序
            allocate_status: 分配状态
            cursor: 游标

        Returns:
            订单列表

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderListRequest(
            access_token=access_token,
            page_size=page_size,
            begin_time=begin_time,
            end_time=end_time,
            query_type=query_type,
            sort=sort,
            allocate_status=allocate_status,
            cursor=cursor,
        )
        return self._client.execute(request, OrderListResponse)

    def update_order_logistics(
        self,
        access_token: str,
        waybill_code: Optional[str] = None,
        express_company_code: Optional[str] = None,
        user_code: Optional[str] = None,
        allocate_order_code: Optional[str] = None,
    ) -> OrderLogisticsUpdateResponse:
        """更新订单物流信息（同步）。

        OpenAPI: `open.dropshipping.order.logistics.update` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderLogisticsUpdateRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderLogisticsUpdateRequest.java`

        Args:
            access_token: 访问令牌
            waybill_code: 运单号
            express_company_code: 快递公司编码
            user_code: 用户编码
            allocate_order_code: 分配订单编码

        Returns:
            更新结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderLogisticsUpdateRequest(
            access_token=access_token,
            waybill_code=waybill_code,
            express_company_code=express_company_code,
            user_code=user_code,
            allocate_order_code=allocate_order_code,
        )
        return self._client.execute(request, OrderLogisticsUpdateResponse)

    def query_order_merchant_detail(
        self,
        access_token: str,
        dropshipping_order_code: Optional[str] = None,
    ) -> OrderMerchantDetailResponse:
        """查询订单商家详情（同步）。

        OpenAPI: `open.dropshipping.order.merchant.detail` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderMerchantDetailRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderMerchantDetailRequest.java`

        Args:
            access_token: 访问令牌
            dropshipping_order_code: 代发订单编码

        Returns:
            商家详情

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderMerchantDetailRequest(
            access_token=access_token,
            dropshipping_order_code=dropshipping_order_code,
        )
        return self._client.execute(request, OrderMerchantDetailResponse)

    def list_order_merchants(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        page_size: Optional[int] = None,
        factory_code: Optional[str] = None,
        dropshipping_status: Optional[int] = None,
        order_status: Optional[int] = None,
        refund_status: Optional[int] = None,
        order_type: Optional[int] = None,
        query_type: Optional[str] = None,
        begin_time: Optional[int] = None,
        end_time: Optional[int] = None,
        sort: Optional[int] = None,
    ) -> OrderMerchantListResponse:
        """查询订单商家列表（同步）。

        OpenAPI: `open.dropshipping.order.merchant.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingOrderMerchantListRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingOrderMerchantListRequest.java`

        Args:
            access_token: 访问令牌
            cursor: 游标
            page_size: 页面大小
            factory_code: 工厂编码
            dropshipping_status: 代发状态
            order_status: 订单状态
            refund_status: 退款状态
            order_type: 订单类型
            query_type: 查询类型
            begin_time: 开始时间（毫秒）
            end_time: 结束时间（毫秒）
            sort: 排序

        Returns:
            商家列表

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = OrderMerchantListRequest(
            access_token=access_token,
            cursor=cursor,
            page_size=page_size,
            factory_code=factory_code,
            dropshipping_status=dropshipping_status,
            order_status=order_status,
            refund_status=refund_status,
            order_type=order_type,
            query_type=query_type,
            begin_time=begin_time,
            end_time=end_time,
            sort=sort,
        )
        return self._client.execute(request, OrderMerchantListResponse)

    def list_relations(
        self,
        access_token: str,
        factory_code: Optional[str] = None,
        begin_apply_time: Optional[int] = None,
        end_apply_time: Optional[int] = None,
        page_index: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> RelationListResponse:
        """查询工厂-商家关系列表（同步）。

        OpenAPI: `open.dropshipping.relation.list` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRelationListRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRelationListRequest.java`

        Args:
            access_token: 访问令牌
            factory_code: 工厂编码
            begin_apply_time: 开始申请时间（毫秒）
            end_apply_time: 结束申请时间（毫秒）
            page_index: 页索引
            page_size: 页大小

        Returns:
            关系列表

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RelationListRequest(
            access_token=access_token,
            factory_code=factory_code,
            begin_apply_time=begin_apply_time,
            end_apply_time=end_apply_time,
            page_index=page_index,
            page_size=page_size,
        )
        return self._client.execute(request, RelationListResponse)

    def batch_apply_merchant_relation(
        self,
        access_token: str,
        apply_request_list: Optional[List[ApplyBindFactoryInfo]] = None,
    ) -> RelationMerchantBatchApplyResponse:
        """批量申请商家关系（同步）。

        OpenAPI: `open.dropshipping.relation.merchant.batch.apply` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRelationMerchantBatchApplyRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRelationMerchantBatchApplyRequest.java`

        Args:
            access_token: 访问令牌
            apply_request_list: 申请请求列表

        Returns:
            申请结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RelationMerchantBatchApplyRequest(
            access_token=access_token,
            apply_request_list=apply_request_list,
        )
        return self._client.execute(request, RelationMerchantBatchApplyResponse)

    def batch_unbind_merchant_relation(
        self,
        access_token: str,
        unbind_request_list: Optional[List[UnbindFactoryInfo]] = None,
    ) -> RelationMerchantBatchUnbindResponse:
        """批量解绑商家关系（同步）。

        OpenAPI: `open.dropshipping.relation.merchant.batch.unbind` (POST)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRelationMerchantBatchUnbindRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRelationMerchantBatchUnbindRequest.java`

        Args:
            access_token: 访问令牌
            unbind_request_list: 解绑请求列表

        Returns:
            解绑结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RelationMerchantBatchUnbindRequest(
            access_token=access_token,
            unbind_request_list=unbind_request_list,
        )
        return self._client.execute(request, RelationMerchantBatchUnbindResponse)

    def query_role(
        self,
        access_token: str,
    ) -> RoleQueryResponse:
        """查询当前账号的代发角色（同步）。

        OpenAPI: `open.dropshipping.role.query` (GET)
        Java: `com.kuaishou.merchant.open.api.request.dropshipping.OpenDropshippingRoleQueryRequest`
        Java Source: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/dropshipping/OpenDropshippingRoleQueryRequest.java`

        Args:
            access_token: 访问令牌

        Returns:
            角色查询结果

        Raises:
            KwaixiaodianAPIError: API 调用失败或返回错误
        """
        request = RoleQueryRequest(
            access_token=access_token,
        )
        return self._client.execute(request, RoleQueryResponse)
