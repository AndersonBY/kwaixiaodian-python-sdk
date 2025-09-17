"""物流服务（对齐 Java SDK 与开放平台）

- OpenAPI 范围：`open.address.*`, `open.logistics.*`, `open.express.*`
- Java 对应包：`com.kuaishou.merchant.open.api.request.logistics`、`...request.express`
- 规则与指引：参考 `docs/开发指南和规则协议/` 与 `docs/开发者支持文档/`

说明：若某接口在 Java 参考中不存在或标注为回调/内部接口，已在本服务中移除或以回调形式保留。各方法 docstring 附带 OpenAPI method、HTTP 动词与 Java 源路径，便于校验。
"""

from typing import List, Optional

from ...models.logistics import (
    # 电子面单
    AddressDTO,
    BaseAddressInfo,
    Contract,
    # 地址管理
    DistrictListRequest,
    DistrictListResponse,
    # 快递服务
    ExpressCustomTemplateQueryRequest,
    ExpressCustomTemplateQueryResponse,
    ExpressEbillAppendRequest,
    ExpressEbillAppendResponse,
    ExpressEbillCancelRequest,
    ExpressEbillCancelResponse,
    ExpressEbillGetRequest,
    ExpressEbillGetResponse,
    ExpressEbillUpdateRequest,
    ExpressEbillUpdateResponse,
    ExpressPrinterElementQueryRequest,
    ExpressPrinterElementQueryResponse,
    ExpressReachableQueryRequest,
    ExpressReachableQueryResponse,
    ExpressStandardTemplateListRequest,
    ExpressStandardTemplateListResponse,
    ExpressSubscribeQueryRequest,
    ExpressSubscribeQueryResponse,
    ExpressTemplateAddParam,
    # Express Template APIs
    ExpressTemplateAddRequest,
    ExpressTemplateAddResponse,
    ExpressTemplateDetailParam,
    ExpressTemplateDetailRequest,
    ExpressTemplateDetailResponse,
    ExpressTemplateListParam,
    ExpressTemplateListRequest,
    ExpressTemplateListResponse,
    ExpressTemplateUpdateParam,
    ExpressTemplateUpdateRequest,
    ExpressTemplateUpdateResponse,
    GetEbillOrderRequest,
    ItemDTO,
    # 基础模型
    LogisticsTraceNotifyRequest,
    LogisticsTraceNotifyResponse,
    QueryRoutingReachableRequest,
    # 订单物流更新属于订单模块（此处已移除调用）
    SellerAddressCreateRequest,
    SellerAddressCreateResponse,
    SellerAddressDeleteRequest,
    SellerAddressDeleteResponse,
    SellerAddressGetRequest,
    SellerAddressGetResponse,
    SellerAddressListRequest,
    SellerAddressListResponse,
    SellerAddressUpdateRequest,
    SellerAddressUpdateResponse,
    TraceNotifyDetailDTO,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncLogisticsService:
    """异步物流服务。

    提供地址管理、快递模板、电子面单、物流轨迹回调等能力，严格对齐 Java SDK。
    """

    def __init__(self, client: AsyncBaseClient):
        """初始化物流服务

        Args:
            client: 基础客户端实例
        """
        self._client = client

    async def template_list(
        self,
        access_token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        search_used: Optional[bool] = None,
    ) -> ExpressTemplateListResponse:
        """获取快递模板列表。

        Args:
            access_token: 访问令牌。
            offset: 分页偏移量。
            limit: 返回条数。
            search_used: 是否只查询使用中的模板。

        Returns:
            ExpressTemplateListResponse: 模板列表。

        OpenAPI:
            - method: `open.logistics.express.template.list`
            - http: GET

        Java:
            - class: `OpenLogisticsExpressTemplateListRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateListRequest.java`
        """
        request = ExpressTemplateListRequest(
            access_token=access_token,
            param=ExpressTemplateListParam(
                offset=offset, limit=limit, search_used=search_used
            ),
        )
        return await self._client.execute(request, ExpressTemplateListResponse)

    async def template_create(
        self,
        access_token: str,
        send_province_name: str,
        send_district_code: int,
        send_time: int,
        send_city_name: str,
        cal_type: int,
        name: str,
        source_type: int,
        send_province_code: int,
        send_city_code: int,
        config: str,
        send_district_name: str,
        uid: Optional[int] = None,
    ) -> ExpressTemplateAddResponse:
        """创建快递模板。

        Args:
            access_token: 访问令牌。
            send_province_name: 发货省份名称。
            send_district_code: 发货区县行政编码。
            send_time: 发货时效配置（分钟）。
            send_city_name: 发货城市名称。
            cal_type: 计费类型。
            name: 模板名称。
            source_type: 来源类型。
            send_province_code: 发货省份行政编码。
            send_city_code: 发货城市行政编码。
            config: 模板配置（JSON 字符串）。
            send_district_name: 发货区县名称。
            uid: 可选用户 ID。

        Returns:
            ExpressTemplateAddResponse: 创建结果。

        OpenAPI:
            - method: `open.logistics.express.template.add`
            - http: POST

        Java:
            - class: `OpenLogisticsExpressTemplateAddRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateAddRequest.java`
        """
        param = ExpressTemplateAddParam(
            send_province_name=send_province_name,
            send_district_code=send_district_code,
            send_time=send_time,
            send_city_name=send_city_name,
            cal_type=cal_type,
            name=name,
            source_type=source_type,
            send_province_code=send_province_code,
            send_city_code=send_city_code,
            config=config,
            send_district_name=send_district_name,
        )
        request = ExpressTemplateAddRequest(
            access_token=access_token, param=param, uid=uid, api_version="1"
        )
        return await self._client.execute(request, ExpressTemplateAddResponse)

    async def template_update(
        self,
        access_token: str,
        template_id: int,
        send_province_name: Optional[str] = None,
        send_district_code: Optional[int] = None,
        send_time: Optional[int] = None,
        send_city_name: Optional[str] = None,
        cal_type: Optional[int] = None,
        name: Optional[str] = None,
        source_type: Optional[int] = None,
        send_province_code: Optional[int] = None,
        send_city_code: Optional[int] = None,
        config: Optional[str] = None,
        send_district_name: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ExpressTemplateUpdateResponse:
        """更新快递模板（仅提供需要修改的字段）。

        Args:
            access_token: 访问令牌。
            template_id: 模板 ID。
            send_province_name: 发货省份名称。
            send_district_code: 发货区县行政编码。
            send_time: 发货时效配置（分钟）。
            send_city_name: 发货城市名称。
            cal_type: 计费类型。
            name: 模板名称。
            source_type: 来源类型。
            send_province_code: 发货省份行政编码。
            send_city_code: 发货城市行政编码。
            config: 模板配置（JSON 字符串）。
            send_district_name: 发货区县名称。
            uid: 可选用户 ID。

        Returns:
            ExpressTemplateUpdateResponse: 更新结果。

        OpenAPI:
            - method: `open.logistics.express.template.update`
            - http: POST

        Java:
            - class: `OpenLogisticsExpressTemplateUpdateRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateUpdateRequest.java`
        """
        param = ExpressTemplateUpdateParam(
            id=template_id,
            send_province_name=send_province_name,
            send_district_code=send_district_code,
            send_time=send_time,
            send_city_name=send_city_name,
            cal_type=cal_type,
            name=name,
            source_type=source_type,
            send_province_code=send_province_code,
            send_city_code=send_city_code,
            config=config,
            send_district_name=send_district_name,
        )
        request = ExpressTemplateUpdateRequest(
            access_token=access_token, param=param, uid=uid, api_version="1"
        )
        return await self._client.execute(request, ExpressTemplateUpdateResponse)

    # ==================== 地址管理相关 ====================

    async def district_list(
        self,
        access_token: str,
        district_version: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> DistrictListResponse:
        """获取地区列表。

        Args:
            access_token: 访问令牌。
            district_version: 地区版本（可选）。
            uid: 可选用户 ID。

        Returns:
            DistrictListResponse: 地区列表。

        OpenAPI:
            - method: `open.address.district.list`
            - http: GET

        Java:
            - class: `OpenAddressDistrictListRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressDistrictListRequest.java`
        """
        request = DistrictListRequest(
            access_token=access_token,
            district_version=district_version,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, DistrictListResponse)

    async def seller_address_create(
        self,
        access_token: str,
        base_info: BaseAddressInfo,
        default_address: Optional[bool] = None,
        address_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerAddressCreateResponse:
        """创建商家地址。

        Args:
            access_token: 访问令牌。
            base_info: 地址基本信息（参考 Java `BaseAddressInfo`）。
            default_address: 是否设为默认地址。
            address_type: 地址类型（平台定义）。
            uid: 可选用户 ID。

        Returns:
            SellerAddressCreateResponse: 创建结果。

        OpenAPI:
            - method: `open.address.seller.create`
            - http: GET

        Java:
            - class: `OpenAddressSellerCreateRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerCreateRequest.java`
        """
        request = SellerAddressCreateRequest(
            access_token=access_token,
            base_info=base_info,  # BaseAddressInfo
            default_address=default_address,
            address_type=address_type,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, SellerAddressCreateResponse)

    async def seller_address_list(
        self,
        access_token: str,
        address_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerAddressListResponse:
        """获取商家地址列表。

        Args:
            access_token: 访问令牌。
            address_type: 地址类型（可选）。
            uid: 可选用户 ID。

        Returns:
            SellerAddressListResponse: 地址列表。

        OpenAPI:
            - method: `open.address.seller.list`
            - http: GET

        Java:
            - class: `OpenAddressSellerListRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerListRequest.java`
        """
        request = SellerAddressListRequest(
            access_token=access_token,
            address_type=address_type,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, SellerAddressListResponse)

    async def seller_address_get(
        self,
        access_token: str,
        address_id: int,
        uid: Optional[int] = None,
    ) -> SellerAddressGetResponse:
        """获取商家地址详情。

        Args:
            access_token: 访问令牌。
            address_id: 地址 ID。
            uid: 可选用户 ID。

        Returns:
            SellerAddressGetResponse: 地址详情。

        OpenAPI:
            - method: `open.address.seller.get`
            - http: GET

        Java:
            - class: `OpenAddressSellerGetRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerGetRequest.java`
        """
        request = SellerAddressGetRequest(
            access_token=access_token,
            address_id=address_id,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, SellerAddressGetResponse)

    async def seller_address_update(
        self,
        access_token: str,
        address_id: int,
        base_info: BaseAddressInfo,
        default_address: Optional[bool] = None,
        uid: Optional[int] = None,
    ) -> SellerAddressUpdateResponse:
        """更新商家地址。

        Args:
            access_token: 访问令牌。
            address_id: 地址 ID。
            base_info: 地址基本信息（Java `BaseAddressInfo`）。
            default_address: 是否设为默认地址。
            uid: 可选用户 ID。

        Returns:
            SellerAddressUpdateResponse: 更新结果。

        OpenAPI:
            - method: `open.address.seller.update`
            - http: GET

        Java:
            - class: `OpenAddressSellerUpdateRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerUpdateRequest.java`
        """
        request = SellerAddressUpdateRequest(
            access_token=access_token,
            address_id=address_id,
            base_info=base_info,
            default_address=default_address,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, SellerAddressUpdateResponse)

    async def seller_address_delete(
        self,
        access_token: str,
        address_id: int,
        uid: Optional[int] = None,
    ) -> SellerAddressDeleteResponse:
        """删除商家地址。

        Args:
            access_token: 访问令牌。
            address_id: 地址 ID。
            uid: 可选用户 ID。

        Returns:
            SellerAddressDeleteResponse: 删除结果。

        OpenAPI:
            - method: `open.address.seller.delete`
            - http: GET

        Java:
            - class: `OpenAddressSellerDeleteRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerDeleteRequest.java`
        """
        request = SellerAddressDeleteRequest(
            access_token=access_token,
            address_id=address_id,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, SellerAddressDeleteResponse)

    # ==================== 电子面单相关 ====================

    async def express_subscribe_query(
        self,
        access_token: str,
        express_company_code: str,
        uid: Optional[int] = None,
    ) -> ExpressSubscribeQueryResponse:
        """查询快递订阅状态。

        Args:
            access_token: 访问令牌。
            express_company_code: 快递公司编码。
            uid: 可选用户 ID。

        Returns:
            ExpressSubscribeQueryResponse: 订阅状态结果。

        OpenAPI:
            - method: `open.express.subscribe.query`
            - http: GET/POST 以平台为准（Java SDK 为 AccessToken Request，详情见参考）。

        Java:
            - class: `OpenExpressSubscribeQueryRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressSubscribeQueryRequest.java`
        """
        request = ExpressSubscribeQueryRequest(
            access_token=access_token,
            express_company_code=express_company_code,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressSubscribeQueryResponse)

    async def express_ebill_get(
        self,
        access_token: str,
        get_ebill_order_request: List[GetEbillOrderRequest],
        uid: Optional[int] = None,
    ) -> ExpressEbillGetResponse:
        """获取电子面单信息。

        Args:
            access_token: 访问令牌。
            get_ebill_order_request: 电子面单下单请求项列表。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillGetResponse: 面单信息列表。

        OpenAPI:
            - method: `open.express.ebill.get`
            - http: POST

        Java:
            - class: `OpenExpressEbillGetRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillGetRequest.java`
        """
        request = ExpressEbillGetRequest(
            access_token=access_token,
            get_ebill_order_request=get_ebill_order_request,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressEbillGetResponse)

    async def express_ebill_cancel(
        self,
        access_token: str,
        express_company_code: str,
        waybill_code: str,
        uid: Optional[int] = None,
    ) -> ExpressEbillCancelResponse:
        """取消电子面单。

        Args:
            access_token: 访问令牌。
            express_company_code: 快递公司编码。
            waybill_code: 运单号。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillCancelResponse: 取消结果。

        OpenAPI:
            - method: `open.express.ebill.cancel`
            - http: GET

        Java:
            - class: `OpenExpressEbillCancelRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillCancelRequest.java`
        """
        request = ExpressEbillCancelRequest(
            access_token=access_token,
            express_company_code=express_company_code,
            waybill_code=waybill_code,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressEbillCancelResponse)

    async def express_ebill_update(
        self,
        access_token: str,
        goods_description: Optional[str] = None,
        packaging_description: Optional[str] = None,
        total_package_length: Optional[float] = None,
        item_list: Optional[List[ItemDTO]] = None,
        ext_data: Optional[str] = None,
        receiver_contract: Optional[Contract] = None,
        sender_contract: Optional[Contract] = None,
        express_company_code: Optional[str] = None,
        total_package_width: Optional[float] = None,
        total_package_weight: Optional[float] = None,
        trade_order_remark: Optional[str] = None,
        total_package_volume: Optional[float] = None,
        total_package_height: Optional[float] = None,
        receiver_address: Optional[AddressDTO] = None,
        waybill_code: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ExpressEbillUpdateResponse:
        """更新电子面单信息（仅填写需要更新的字段）。

        Args:
            access_token: 访问令牌。
            goods_description: 货品描述。
            packaging_description: 包装描述。
            total_package_length: 包裹总长（cm）。
            item_list: 货品列表。
            ext_data: 扩展数据。
            receiver_contract: 收件人信息。
            sender_contract: 寄件人信息。
            express_company_code: 快递公司编码。
            total_package_width: 包裹总宽（cm）。
            total_package_weight: 包裹总重（kg）。
            trade_order_remark: 交易备注。
            total_package_volume: 包裹总体积。
            total_package_height: 包裹总高（cm）。
            receiver_address: 收件地址。
            waybill_code: 运单号。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillUpdateResponse: 更新结果。

        OpenAPI:
            - method: `open.express.ebill.update`
            - http: POST

        Java:
            - class: `OpenExpressEbillUpdateRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillUpdateRequest.java`
        """
        request = ExpressEbillUpdateRequest(
            access_token=access_token,
            goods_description=goods_description,
            packaging_description=packaging_description,
            total_package_length=total_package_length,
            item_list=item_list,
            ext_data=ext_data,
            receiver_contract=receiver_contract,
            sender_contract=sender_contract,
            express_company_code=express_company_code,
            total_package_width=total_package_width,
            total_package_weight=total_package_weight,
            trade_order_remark=trade_order_remark,
            total_package_volume=total_package_volume,
            total_package_height=total_package_height,
            receiver_address=receiver_address,
            waybill_code=waybill_code,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressEbillUpdateResponse)

    async def express_ebill_append(
        self,
        access_token: str,
        parent_waybill_code: str,
        express_company_code: str,
        add_package_quantity: int,
        uid: Optional[int] = None,
    ) -> ExpressEbillAppendResponse:
        """电子面单追加包裹

        Args:
            access_token: 访问令牌
            parent_waybill_code: 主运单号
            express_company_code: 快递公司编码
            add_package_quantity: 追加包裹数量（>=1）
            uid: 可选用户ID

        Returns:
            电子面单追加包裹响应
        """
        request = ExpressEbillAppendRequest(
            access_token=access_token,
            parent_waybill_code=parent_waybill_code,
            express_company_code=express_company_code,
            add_package_quantity=add_package_quantity,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressEbillAppendResponse)

    # ==================== 快递服务查询相关 ====================

    async def express_reachable_query(
        self,
        access_token: str,
        reachable_requests: List[QueryRoutingReachableRequest],
        uid: Optional[int] = None,
    ) -> ExpressReachableQueryResponse:
        """查询快递可达性（open.express.reachable.query, POST）"""
        request = ExpressReachableQueryRequest(
            access_token=access_token,
            reachable_requests=reachable_requests,  # List[QueryRoutingReachableRequest]
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressReachableQueryResponse)

    async def express_standard_template_list(
        self,
        access_token: str,
        express_company_code: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ExpressStandardTemplateListResponse:
        """获取标准模板列表

        Args:
            access_token: 访问令牌
            express_company_code: 快递公司编码
            uid: 可选用户ID

        Returns:
            获取标准模板列表响应
        """
        request = ExpressStandardTemplateListRequest(
            access_token=access_token,
            express_company_code=express_company_code,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressStandardTemplateListResponse)

    async def express_custom_template_query(
        self,
        access_token: str,
        standard_template_code: Optional[str] = None,
        type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ExpressCustomTemplateQueryResponse:
        """查询自定义模板列表

        Args:
            access_token: 访问令牌
            standard_template_code: 标准模板编码
            type: 模板类型
            uid: 可选用户ID

        Returns:
            查询自定义模板列表响应
        """
        request = ExpressCustomTemplateQueryRequest(
            access_token=access_token,
            standard_template_code=standard_template_code,
            type=type,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, ExpressCustomTemplateQueryResponse)

    async def express_printer_element_query(
        self, access_token: str, uid: Optional[int] = None
    ) -> ExpressPrinterElementQueryResponse:
        """查询打印元素（open.express.printer.element.query, GET）"""
        request = ExpressPrinterElementQueryRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return await self._client.execute(request, ExpressPrinterElementQueryResponse)

    # 订单物流更新相关接口属于订单模块，已移至 OrderService

    # ==================== 物流轨迹回调相关 ====================

    async def logistics_trace_notify(
        self,
        access_token: str,
        traces: List[TraceNotifyDetailDTO],
        uid: Optional[int] = None,
    ) -> LogisticsTraceNotifyResponse:
        """物流轨迹通知回调（open.logistics.trace.notify, POST）"""
        request = LogisticsTraceNotifyRequest(
            access_token=access_token,
            traces=traces,  # List[TraceNotifyDetailDTO]
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, LogisticsTraceNotifyResponse)

    # ==================== Express Template APIs ====================

    async def template_detail(
        self,
        access_token: str,
        template_id: int,
    ) -> ExpressTemplateDetailResponse:
        """获取快递模板详情

        Args:
            access_token: 访问令牌
            template_id: 模板ID

        Returns:
            快递模板详情查询响应
        """
        request = ExpressTemplateDetailRequest(
            access_token=access_token,
            param=ExpressTemplateDetailParam(id=template_id),
        )
        return await self._client.execute(request, ExpressTemplateDetailResponse)


class SyncLogisticsService:
    """同步物流服务（与异步版语义一致，OpenAPI 与 Java 参考相同）。"""

    def __init__(self, client: SyncBaseClient):
        """初始化物流服务

        Args:
            client: 同步基础客户端实例
        """
        self._client = client

    def template_list(
        self,
        access_token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        search_used: Optional[bool] = None,
    ) -> ExpressTemplateListResponse:
        """获取快递模板列表（同步）。

        Args:
            access_token: 访问令牌。
            offset: 分页偏移量。
            limit: 返回条数。
            search_used: 是否仅查询使用中的模板。

        Returns:
            ExpressTemplateListResponse: 模板列表。

        OpenAPI:
            - method: `open.logistics.express.template.list`
            - http: GET

        Java:
            - class: `OpenLogisticsExpressTemplateListRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateListRequest.java`
        """
        request = ExpressTemplateListRequest(
            access_token=access_token,
            param=ExpressTemplateListParam(
                offset=offset, limit=limit, search_used=search_used
            ),
        )
        return self._client.execute(request, ExpressTemplateListResponse)

    def template_create(
        self,
        access_token: str,
        send_province_name: str,
        send_district_code: int,
        send_time: int,
        send_city_name: str,
        cal_type: int,
        name: str,
        source_type: int,
        send_province_code: int,
        send_city_code: int,
        config: str,
        send_district_name: str,
        uid: Optional[int] = None,
    ) -> ExpressTemplateAddResponse:
        """创建快递模板（同步）。

        Args:
            access_token: 访问令牌。
            send_province_name: 发货省份名称。
            send_district_code: 发货区县行政编码。
            send_time: 发货时效配置（分钟）。
            send_city_name: 发货城市名称。
            cal_type: 计费类型。
            name: 模板名称。
            source_type: 来源类型。
            send_province_code: 发货省份行政编码。
            send_city_code: 发货城市行政编码。
            config: 模板配置（JSON 字符串）。
            send_district_name: 发货区县名称。
            uid: 可选用户 ID。

        Returns:
            ExpressTemplateAddResponse: 创建结果。

        OpenAPI:
            - method: `open.logistics.express.template.add`
            - http: POST

        Java:
            - class: `OpenLogisticsExpressTemplateAddRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateAddRequest.java`
        """
        param = ExpressTemplateAddParam(
            send_province_name=send_province_name,
            send_district_code=send_district_code,
            send_time=send_time,
            send_city_name=send_city_name,
            cal_type=cal_type,
            name=name,
            source_type=source_type,
            send_province_code=send_province_code,
            send_city_code=send_city_code,
            config=config,
            send_district_name=send_district_name,
        )
        request = ExpressTemplateAddRequest(
            access_token=access_token, param=param, uid=uid, api_version="1"
        )
        return self._client.execute(request, ExpressTemplateAddResponse)

    def template_update(
        self,
        access_token: str,
        template_id: int,
        send_province_name: Optional[str] = None,
        send_district_code: Optional[int] = None,
        send_time: Optional[int] = None,
        send_city_name: Optional[str] = None,
        cal_type: Optional[int] = None,
        name: Optional[str] = None,
        source_type: Optional[int] = None,
        send_province_code: Optional[int] = None,
        send_city_code: Optional[int] = None,
        config: Optional[str] = None,
        send_district_name: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ExpressTemplateUpdateResponse:
        """更新快递模板（同步）。仅提供需要修改的字段。

        Args:
            access_token: 访问令牌。
            template_id: 模板 ID。
            send_province_name: 发货省份名称。
            send_district_code: 发货区县行政编码。
            send_time: 发货时效配置（分钟）。
            send_city_name: 发货城市名称。
            cal_type: 计费类型。
            name: 模板名称。
            source_type: 来源类型。
            send_province_code: 发货省份行政编码。
            send_city_code: 发货城市行政编码。
            config: 模板配置（JSON 字符串）。
            send_district_name: 发货区县名称。
            uid: 可选用户 ID。

        Returns:
            ExpressTemplateUpdateResponse: 更新结果。

        OpenAPI:
            - method: `open.logistics.express.template.update`
            - http: POST

        Java:
            - class: `OpenLogisticsExpressTemplateUpdateRequest`
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateUpdateRequest.java`
        """
        param = ExpressTemplateUpdateParam(
            id=template_id,
            send_province_name=send_province_name,
            send_district_code=send_district_code,
            send_time=send_time,
            send_city_name=send_city_name,
            cal_type=cal_type,
            name=name,
            source_type=source_type,
            send_province_code=send_province_code,
            send_city_code=send_city_code,
            config=config,
            send_district_name=send_district_name,
        )
        request = ExpressTemplateUpdateRequest(
            access_token=access_token, param=param, uid=uid, api_version="1"
        )
        return self._client.execute(request, ExpressTemplateUpdateResponse)

    # ==================== 地址管理相关 ====================

    def district_list(
        self,
        access_token: str,
        district_version: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> DistrictListResponse:
        """获取地区列表（同步）。

        Args:
            access_token: 访问令牌。
            district_version: 地区版本（可选）。
            uid: 可选用户 ID。

        Returns:
            DistrictListResponse: 地区列表。

        OpenAPI: `open.address.district.list` (GET)
        Java: `OpenAddressDistrictListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressDistrictListRequest.java`
        """
        request = DistrictListRequest(
            access_token=access_token,
            district_version=district_version,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, DistrictListResponse)

    def seller_address_create(
        self,
        access_token: str,
        base_info: BaseAddressInfo,
        default_address: Optional[bool] = None,
        address_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerAddressCreateResponse:
        """创建商家地址（同步）。

        Args:
            access_token: 访问令牌。
            base_info: 地址基本信息（Java: `BaseAddressInfo`）。
            default_address: 是否设为默认地址。
            address_type: 地址类型（平台定义）。
            uid: 可选用户 ID。

        Returns:
            SellerAddressCreateResponse: 创建结果。

        OpenAPI: `open.address.seller.create` (GET)
        Java: `OpenAddressSellerCreateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerCreateRequest.java`
        """
        request = SellerAddressCreateRequest(
            access_token=access_token,
            base_info=base_info,
            default_address=default_address,
            address_type=address_type,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SellerAddressCreateResponse)

    def seller_address_list(
        self,
        access_token: str,
        address_type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SellerAddressListResponse:
        """获取商家地址列表（同步）。

        Args:
            access_token: 访问令牌。
            address_type: 地址类型（可选）。
            uid: 可选用户 ID。

        Returns:
            SellerAddressListResponse: 地址列表。

        OpenAPI: `open.address.seller.list` (GET)
        Java: `OpenAddressSellerListRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerListRequest.java`
        """
        request = SellerAddressListRequest(
            access_token=access_token,
            address_type=address_type,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SellerAddressListResponse)

    def seller_address_get(
        self,
        access_token: str,
        address_id: int,
        uid: Optional[int] = None,
    ) -> SellerAddressGetResponse:
        """获取商家地址详情（同步）。

        Args:
            access_token: 访问令牌。
            address_id: 地址 ID。
            uid: 可选用户 ID。

        Returns:
            SellerAddressGetResponse: 地址详情。

        OpenAPI: `open.address.seller.get` (GET)
        Java: `OpenAddressSellerGetRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerGetRequest.java`
        """
        request = SellerAddressGetRequest(
            access_token=access_token,
            address_id=address_id,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SellerAddressGetResponse)

    def seller_address_update(
        self,
        access_token: str,
        address_id: int,
        base_info: BaseAddressInfo,
        default_address: Optional[bool] = None,
        uid: Optional[int] = None,
    ) -> SellerAddressUpdateResponse:
        """更新商家地址（同步）。

        Args:
            access_token: 访问令牌。
            address_id: 地址 ID。
            base_info: 地址基本信息（Java: `BaseAddressInfo`）。
            default_address: 是否设为默认地址。
            uid: 可选用户 ID。

        Returns:
            SellerAddressUpdateResponse: 更新结果。

        OpenAPI: `open.address.seller.update` (GET)
        Java: `OpenAddressSellerUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerUpdateRequest.java`
        """
        request = SellerAddressUpdateRequest(
            access_token=access_token,
            address_id=address_id,
            base_info=base_info,
            default_address=default_address,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SellerAddressUpdateResponse)

    def seller_address_delete(
        self,
        access_token: str,
        address_id: int,
        uid: Optional[int] = None,
    ) -> SellerAddressDeleteResponse:
        """删除商家地址（同步）。

        Args:
            access_token: 访问令牌。
            address_id: 地址 ID。
            uid: 可选用户 ID。

        Returns:
            SellerAddressDeleteResponse: 删除结果。

        OpenAPI: `open.address.seller.delete` (GET)
        Java: `OpenAddressSellerDeleteRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenAddressSellerDeleteRequest.java`
        """
        request = SellerAddressDeleteRequest(
            access_token=access_token,
            address_id=address_id,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, SellerAddressDeleteResponse)

    # ==================== 电子面单相关 ====================

    def express_subscribe_query(
        self,
        access_token: str,
        express_company_code: str,
        uid: Optional[int] = None,
    ) -> ExpressSubscribeQueryResponse:
        """查询快递订阅状态（同步）。

        Args:
            access_token: 访问令牌。
            express_company_code: 快递公司编码。
            uid: 可选用户 ID。

        Returns:
            ExpressSubscribeQueryResponse: 订阅状态结果。

        OpenAPI: `open.express.subscribe.query`
        Java: `OpenExpressSubscribeQueryRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressSubscribeQueryRequest.java`
        """
        request = ExpressSubscribeQueryRequest(
            access_token=access_token,
            express_company_code=express_company_code,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressSubscribeQueryResponse)

    def express_ebill_get(
        self,
        access_token: str,
        get_ebill_order_request: List[GetEbillOrderRequest],
        uid: Optional[int] = None,
    ) -> ExpressEbillGetResponse:
        """获取电子面单信息（同步）。

        Args:
            access_token: 访问令牌。
            get_ebill_order_request: 电子面单下单请求项列表。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillGetResponse: 面单信息列表。

        OpenAPI: `open.express.ebill.get` (POST)
        Java: `OpenExpressEbillGetRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillGetRequest.java`
        """
        request = ExpressEbillGetRequest(
            access_token=access_token,
            get_ebill_order_request=get_ebill_order_request,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressEbillGetResponse)

    def express_ebill_cancel(
        self,
        access_token: str,
        express_company_code: str,
        waybill_code: str,
        uid: Optional[int] = None,
    ) -> ExpressEbillCancelResponse:
        """取消电子面单（同步）。

        Args:
            access_token: 访问令牌。
            express_company_code: 快递公司编码。
            waybill_code: 运单号。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillCancelResponse: 取消结果。

        OpenAPI: `open.express.ebill.cancel` (GET)
        Java: `OpenExpressEbillCancelRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillCancelRequest.java`
        """
        request = ExpressEbillCancelRequest(
            access_token=access_token,
            express_company_code=express_company_code,
            waybill_code=waybill_code,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressEbillCancelResponse)

    def express_ebill_update(
        self,
        access_token: str,
        goods_description: Optional[str] = None,
        packaging_description: Optional[str] = None,
        total_package_length: Optional[float] = None,
        item_list: Optional[List[ItemDTO]] = None,
        ext_data: Optional[str] = None,
        receiver_contract: Optional[Contract] = None,
        sender_contract: Optional[Contract] = None,
        express_company_code: Optional[str] = None,
        total_package_width: Optional[float] = None,
        total_package_weight: Optional[float] = None,
        trade_order_remark: Optional[str] = None,
        total_package_volume: Optional[float] = None,
        total_package_height: Optional[float] = None,
        receiver_address: Optional[AddressDTO] = None,
        waybill_code: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ExpressEbillUpdateResponse:
        """更新电子面单信息（同步）。仅填写需要更新的字段。

        Args:
            access_token: 访问令牌。
            goods_description: 货品描述。
            packaging_description: 包装描述。
            total_package_length: 包裹总长（cm）。
            item_list: 货品列表。
            ext_data: 扩展数据。
            receiver_contract: 收件人信息。
            sender_contract: 寄件人信息。
            express_company_code: 快递公司编码。
            total_package_width: 包裹总宽（cm）。
            total_package_weight: 包裹总重（kg）。
            trade_order_remark: 交易备注。
            total_package_volume: 包裹总体积。
            total_package_height: 包裹总高（cm）。
            receiver_address: 收件地址。
            waybill_code: 运单号。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillUpdateResponse: 更新结果。

        OpenAPI: `open.express.ebill.update` (POST)
        Java: `OpenExpressEbillUpdateRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillUpdateRequest.java`
        """
        request = ExpressEbillUpdateRequest(
            access_token=access_token,
            goods_description=goods_description,
            packaging_description=packaging_description,
            total_package_length=total_package_length,
            item_list=item_list,
            ext_data=ext_data,
            receiver_contract=receiver_contract,
            sender_contract=sender_contract,
            express_company_code=express_company_code,
            total_package_width=total_package_width,
            total_package_weight=total_package_weight,
            trade_order_remark=trade_order_remark,
            total_package_volume=total_package_volume,
            total_package_height=total_package_height,
            receiver_address=receiver_address,
            waybill_code=waybill_code,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressEbillUpdateResponse)

    def express_ebill_append(
        self,
        access_token: str,
        parent_waybill_code: str,
        express_company_code: str,
        add_package_quantity: int,
        uid: Optional[int] = None,
    ) -> ExpressEbillAppendResponse:
        """电子面单追加包裹（同步）。

        Args:
            access_token: 访问令牌。
            parent_waybill_code: 主运单号。
            express_company_code: 快递公司编码。
            add_package_quantity: 追加包裹数量（>= 1）。
            uid: 可选用户 ID。

        Returns:
            ExpressEbillAppendResponse: 追加结果。

        OpenAPI: `open.express.ebill.append` (POST)
        Java: `OpenExpressEbillAppendRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressEbillAppendRequest.java`
        """
        request = ExpressEbillAppendRequest(
            access_token=access_token,
            parent_waybill_code=parent_waybill_code,
            express_company_code=express_company_code,
            add_package_quantity=add_package_quantity,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressEbillAppendResponse)

    # ==================== 快递服务查询相关 ====================

    def express_reachable_query(
        self,
        access_token: str,
        reachable_requests: List[QueryRoutingReachableRequest],
        uid: Optional[int] = None,
    ) -> ExpressReachableQueryResponse:
        """查询快递可达性（同步）。

        Args:
            access_token: 访问令牌。
            reachable_requests: 批量可达性查询请求列表。
            uid: 可选用户 ID。

        Returns:
            ExpressReachableQueryResponse: 可达性结果列表。

        OpenAPI: `open.express.reachable.query`
        Java: `OpenExpressReachableQueryRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressReachableQueryRequest.java`
        """
        request = ExpressReachableQueryRequest(
            access_token=access_token,
            reachable_requests=reachable_requests,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressReachableQueryResponse)

    def express_standard_template_list(
        self,
        access_token: str,
        express_company_code: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> ExpressStandardTemplateListResponse:
        """获取标准模板列表（同步）。

        Args:
            access_token: 访问令牌。
            express_company_code: 快递公司编码（可选）。
            uid: 可选用户 ID。

        Returns:
            ExpressStandardTemplateListResponse: 标准模板列表。

        OpenAPI: `open.express.standard.template.list.get` (POST)
        Java: `OpenExpressStandardTemplateListGetRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressStandardTemplateListGetRequest.java`
        """
        request = ExpressStandardTemplateListRequest(
            access_token=access_token,
            express_company_code=express_company_code,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressStandardTemplateListResponse)

    def express_custom_template_query(
        self,
        access_token: str,
        standard_template_code: Optional[str] = None,
        type: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> ExpressCustomTemplateQueryResponse:
        """查询自定义模板列表（同步）。

        Args:
            access_token: 访问令牌。
            standard_template_code: 标准模板编码。
            type: 模板类型（平台定义）。
            uid: 可选用户 ID。

        Returns:
            ExpressCustomTemplateQueryResponse: 自定义模板列表。

        OpenAPI: `open.express.custom.tempate.list.query` (GET)
        Java: `OpenExpressCustomTempateListQueryRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/express/OpenExpressCustomTempateListQueryRequest.java`
        """
        request = ExpressCustomTemplateQueryRequest(
            access_token=access_token,
            standard_template_code=standard_template_code,
            type=type,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, ExpressCustomTemplateQueryResponse)

    # 订单物流更新相关接口属于订单模块，已移至 OrderService

    # ==================== 物流轨迹回调相关 ====================

    def logistics_trace_notify(
        self,
        access_token: str,
        traces: List[TraceNotifyDetailDTO],
        uid: Optional[int] = None,
    ) -> LogisticsTraceNotifyResponse:
        """物流轨迹通知回调（同步）。

        Args:
            access_token: 访问令牌。
            traces: 轨迹明细列表。
            uid: 可选用户 ID。

        Returns:
            LogisticsTraceNotifyResponse: 回调结果。

        OpenAPI: `open.logistics.trace.notify` (POST)
        Java: `OpenLogisticsTraceNotifyRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsTraceNotifyRequest.java`
        """
        request = LogisticsTraceNotifyRequest(
            access_token=access_token, traces=traces, uid=uid, api_version="1"
        )
        return self._client.execute(request, LogisticsTraceNotifyResponse)

    # ==================== Express Template APIs ====================

    def template_detail(
        self,
        access_token: str,
        template_id: int,
    ) -> ExpressTemplateDetailResponse:
        """获取快递模板详情（同步）。

        Args:
            access_token: 访问令牌。
            template_id: 模板 ID。

        Returns:
            ExpressTemplateDetailResponse: 模板详情。

        OpenAPI: `open.logistics.express.template.detail` (GET)
        Java: `OpenLogisticsExpressTemplateDetailRequest` —
            `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/logistics/OpenLogisticsExpressTemplateDetailRequest.java`
        """
        request = ExpressTemplateDetailRequest(
            access_token=access_token, param=ExpressTemplateDetailParam(id=template_id)
        )
        return self._client.execute(request, ExpressTemplateDetailResponse)
