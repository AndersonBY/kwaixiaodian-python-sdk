"""代发服务相关模型

基于 Java SDK 参考实现：
- com.kuaishou.merchant.open.api.request.dropshipping.*
- com.kuaishou.merchant.open.api.response.dropshipping.*
- com.kuaishou.merchant.open.api.domain.dropshipping.*
"""

from typing import List, Optional

from pydantic import Field

from .base import BaseRequest, BaseResponse, HttpMethod


# 域对象模型
class AddressInfo(BaseResponse):
    """地址信息"""

    province: Optional[str] = Field(None, description="省份")
    city: Optional[str] = Field(None, description="城市")
    district: Optional[str] = Field(None, description="区县")
    detail: Optional[str] = Field(None, description="详细地址")
    name: Optional[str] = Field(None, description="收件人姓名")
    phone: Optional[str] = Field(None, description="联系电话")


class ItemInfo(BaseResponse):
    """商品信息"""

    item_id: Optional[int] = Field(None, description="商品ID")
    item_name: Optional[str] = Field(None, description="商品名称")
    quantity: Optional[int] = Field(None, description="数量")
    price: Optional[int] = Field(None, description="价格（分）")


class WarehouseInfo(BaseResponse):
    """仓库信息"""

    warehouse_id: Optional[int] = Field(None, description="仓库ID")
    warehouse_name: Optional[str] = Field(None, description="仓库名称")
    warehouse_code: Optional[str] = Field(None, description="仓库编码")


class ContractInfo(BaseResponse):
    """合同信息"""

    contract_name: Optional[str] = Field(None, description="合同名称")
    contract_phone: Optional[str] = Field(None, description="合同电话")


class ExpressServiceInfo(BaseResponse):
    """快递服务信息"""

    service_code: Optional[str] = Field(None, description="服务编码")
    service_name: Optional[str] = Field(None, description="服务名称")


class DsOrderGetRequest(BaseResponse):
    """代发订单获取请求（域对象）"""

    reserve_end_time: Optional[int] = Field(None, description="预约截止时间")
    total_package_quantity: Optional[int] = Field(None, description="总包裹数量")
    user_name: Optional[str] = Field(None, description="用户名")
    allocate_order_code: Optional[str] = Field(None, description="分配订单编码")
    goods_description: Optional[str] = Field(None, description="商品描述")
    packaging_description: Optional[str] = Field(None, description="包装描述")
    total_package_length: Optional[float] = Field(None, description="总包裹长度")
    package_code: Optional[str] = Field(None, description="包裹编码")
    express_product_code: Optional[str] = Field(None, description="快递产品编码")
    user_code: Optional[str] = Field(None, description="用户编码")
    item_list: Optional[List[ItemInfo]] = Field(None, description="商品列表")
    ext_data: Optional[str] = Field(None, description="扩展数据")
    has_freight_insurance: Optional[bool] = Field(None, description="是否有运费险")
    net_site_name: Optional[str] = Field(None, description="网点名称")
    express_company_code: Optional[str] = Field(None, description="快递公司编码")
    total_package_width: Optional[float] = Field(None, description="总包裹宽度")
    order_channel: Optional[str] = Field(None, description="订单渠道")
    pod_model_address: Optional[AddressInfo] = Field(None, description="收件人地址")
    sender_contract: Optional[ContractInfo] = Field(None, description="发件人合同信息")
    total_package_weight: Optional[float] = Field(None, description="总包裹重量")
    trade_order_remark: Optional[str] = Field(None, description="交易订单备注")
    total_package_volume: Optional[float] = Field(None, description="总包裹体积")
    is_sign_back: Optional[bool] = Field(None, description="是否签回")
    pay_amount: Optional[int] = Field(None, description="支付金额（分）")
    settle_account: Optional[str] = Field(None, description="结算账户")
    pay_method: Optional[int] = Field(None, description="支付方式")
    warehouse: Optional[WarehouseInfo] = Field(None, description="仓库信息")
    total_package_height: Optional[float] = Field(None, description="总包裹高度")
    net_site_code: Optional[str] = Field(None, description="网点编码")
    sender_address: Optional[AddressInfo] = Field(None, description="发件人地址")
    template_url: Optional[str] = Field(None, description="模板URL")
    reserve_time: Optional[int] = Field(None, description="预约时间")
    request_id: Optional[str] = Field(None, description="请求ID")
    express_services: Optional[List[ExpressServiceInfo]] = Field(
        None, description="快递服务列表"
    )


class AppendDropshippingOrderRequest(BaseResponse):
    """追加代发订单请求（域对象）"""

    request_id: Optional[str] = Field(None, description="请求ID")
    dropshipping_order_code: Optional[str] = Field(None, description="代发订单编码")
    order_type: Optional[int] = Field(None, description="订单类型")
    order_item_list: Optional[List["DropshippingItemInfo"]] = Field(
        None, description="订单商品列表"
    )
    seller_note: Optional[str] = Field(None, description="卖家备注")
    receiver_address: Optional[AddressInfo] = Field(None, description="收件人地址")
    receiver_contact: Optional["ContactInfo"] = Field(
        None, description="收件人联系方式"
    )


# 批量获取电子面单
class EbillBatchGetRequest(BaseRequest):
    """批量获取电子面单请求"""

    api_method: str = "open.dropshipping.ebill.batch.get"
    http_method: HttpMethod = HttpMethod.POST

    ds_order_get_req: Optional[List[DsOrderGetRequest]] = Field(
        None, description="代发订单获取请求列表", alias="dsOrderGetReq"
    )


class EbillBatchGetResponse(BaseResponse):
    """批量获取电子面单响应"""

    pass


# 取消电子面单
class EbillCancelRequest(BaseRequest):
    """取消电子面单请求"""

    api_method: str = "open.dropshipping.ebill.cancel"
    http_method: HttpMethod = HttpMethod.POST

    waybill_code: Optional[str] = Field(None, description="运单号", alias="waybillCode")
    express_company_code: Optional[str] = Field(
        None, description="快递公司编码", alias="expressCompanyCode"
    )
    user_code: Optional[str] = Field(None, description="用户编码", alias="userCode")


class EbillCancelResponse(BaseResponse):
    """取消电子面单响应"""

    pass


# 批量分配订单
class OrderBatchAllocateRequest(BaseRequest):
    """批量分配订单请求"""

    api_method: str = "open.dropshipping.order.batch.allocate"
    http_method: HttpMethod = HttpMethod.POST

    dropshipping_order_code_list: Optional[List[str]] = Field(
        None, description="代发订单编码列表", alias="dropshippingOrderCodeList"
    )
    factory_code: Optional[str] = Field(
        None, description="工厂编码", alias="factoryCode"
    )


class OrderBatchAllocateResponse(BaseResponse):
    """批量分配订单响应"""

    pass


# 取消批量分配订单
class OrderBatchAllocateCancelRequest(BaseRequest):
    """取消批量分配订单请求"""

    api_method: str = "open.dropshipping.order.batch.allocate.cancel"
    http_method: HttpMethod = HttpMethod.POST

    dropshipping_order_code_list: Optional[List[str]] = Field(
        None, description="代发订单编码列表", alias="dropshippingOrderCodeList"
    )
    cancel_allocate_reason: Optional[str] = Field(
        None, description="取消分配原因", alias="cancelAllocateReason"
    )


class OrderBatchAllocateCancelResponse(BaseResponse):
    """取消批量分配订单响应"""

    pass


# 批量追加订单
class OrderBatchAppendRequest(BaseRequest):
    """批量追加订单请求"""

    api_method: str = "open.dropshipping.order.batch.append"
    http_method: HttpMethod = HttpMethod.POST

    append_request_list: Optional[List[AppendDropshippingOrderRequest]] = Field(
        None, description="追加请求列表", alias="appendRequestList"
    )


class OrderBatchAppendResponse(BaseResponse):
    """批量追加订单响应"""

    pass


# 批量删除订单
class OrderBatchDeleteRequest(BaseRequest):
    """批量删除订单请求"""

    api_method: str = "open.dropshipping.order.batch.delete"
    http_method: HttpMethod = HttpMethod.POST

    dropshipping_order_code_list: Optional[List[str]] = Field(
        None, description="代发订单编码列表", alias="dropshippingOrderCodeList"
    )


class OrderBatchDeleteResponse(BaseResponse):
    """批量删除订单响应"""

    pass


# 发货
class OrderDeliverRequest(BaseRequest):
    """订单发货请求"""

    api_method: str = "open.dropshipping.order.deliver"
    http_method: HttpMethod = HttpMethod.POST

    return_address_id: Optional[int] = Field(
        None, description="退货地址ID", alias="returnAddressId"
    )
    waybill_code: Optional[str] = Field(None, description="运单号", alias="waybillCode")
    user_code: Optional[str] = Field(None, description="用户编码", alias="userCode")
    allocate_order_code: Optional[str] = Field(
        None, description="分配订单编码", alias="allocateOrderCode"
    )
    express_company_code: Optional[str] = Field(
        None, description="快递公司编码", alias="expressCompanyCode"
    )
    serial_number_list: Optional[List[str]] = Field(
        None, description="序列号列表", alias="serialNumberList"
    )
    imei_list: Optional[List[str]] = Field(
        None, description="IMEI列表", alias="imeiList"
    )


class OrderDeliverResponse(BaseResponse):
    """订单发货响应"""

    pass


# 查询订单详情
class OrderDetailQueryRequest(BaseRequest):
    """查询订单详情请求"""

    api_method: str = "open.dropshipping.order.detail.query"
    http_method: HttpMethod = HttpMethod.POST

    allocate_order_code: Optional[str] = Field(
        None, description="分配订单编码", alias="allocateOrderCode"
    )
    user_code: Optional[str] = Field(None, description="用户编码", alias="userCode")


class OrderDetailQueryResponse(BaseResponse):
    """查询订单详情响应"""

    pass


# 查询订单列表
class OrderListRequest(BaseRequest):
    """查询订单列表请求"""

    api_method: str = "open.dropshipping.order.list"
    http_method: HttpMethod = HttpMethod.POST

    page_size: Optional[int] = Field(None, description="页面大小", alias="pageSize")
    begin_time: Optional[int] = Field(None, description="开始时间", alias="beginTime")
    end_time: Optional[int] = Field(None, description="结束时间", alias="endTime")
    query_type: Optional[int] = Field(None, description="查询类型", alias="queryType")
    sort: Optional[int] = Field(None, description="排序", alias="sort")
    allocate_status: Optional[int] = Field(
        None, description="分配状态", alias="allocateStatus"
    )
    cursor: Optional[str] = Field(None, description="游标", alias="cursor")


class OrderListResponse(BaseResponse):
    """查询订单列表响应"""

    pass


# 更新物流信息
class OrderLogisticsUpdateRequest(BaseRequest):
    """更新订单物流信息请求"""

    api_method: str = "open.dropshipping.order.logistics.update"
    http_method: HttpMethod = HttpMethod.POST

    waybill_code: Optional[str] = Field(None, description="运单号", alias="waybillCode")
    express_company_code: Optional[str] = Field(
        None, description="快递公司编码", alias="expressCompanyCode"
    )
    user_code: Optional[str] = Field(None, description="用户编码", alias="userCode")
    allocate_order_code: Optional[str] = Field(
        None, description="分配订单编码", alias="allocateOrderCode"
    )


class OrderLogisticsUpdateResponse(BaseResponse):
    """更新订单物流信息响应"""

    pass


# 查询商家详情
class OrderMerchantDetailRequest(BaseRequest):
    """查询订单商家详情请求"""

    api_method: str = "open.dropshipping.order.merchant.detail"
    http_method: HttpMethod = HttpMethod.POST

    dropshipping_order_code: Optional[str] = Field(
        None, description="代发订单编码", alias="dropshippingOrderCode"
    )


class OrderMerchantDetailResponse(BaseResponse):
    """查询订单商家详情响应"""

    pass


# 查询商家列表
class OrderMerchantListRequest(BaseRequest):
    """查询订单商家列表请求"""

    api_method: str = "open.dropshipping.order.merchant.list"
    http_method: HttpMethod = HttpMethod.POST

    cursor: Optional[str] = Field(None, description="游标", alias="cursor")
    page_size: Optional[int] = Field(None, description="页面大小", alias="pageSize")
    factory_code: Optional[str] = Field(
        None, description="工厂编码", alias="factoryCode"
    )
    dropshipping_status: Optional[int] = Field(
        None, description="代发状态", alias="dropshippingStatus"
    )
    order_status: Optional[int] = Field(
        None, description="订单状态", alias="orderStatus"
    )
    refund_status: Optional[int] = Field(
        None, description="退款状态", alias="refundStatus"
    )
    order_type: Optional[int] = Field(None, description="订单类型", alias="orderType")
    query_type: Optional[str] = Field(None, description="查询类型", alias="queryType")
    begin_time: Optional[int] = Field(None, description="开始时间", alias="beginTime")
    end_time: Optional[int] = Field(None, description="结束时间", alias="endTime")
    sort: Optional[int] = Field(None, description="排序", alias="sort")


class OrderMerchantListResponse(BaseResponse):
    """查询订单商家列表响应"""

    pass


# 查询关系列表
class RelationListRequest(BaseRequest):
    """查询关系列表请求"""

    api_method: str = "open.dropshipping.relation.list"
    http_method: HttpMethod = HttpMethod.POST

    factory_code: Optional[str] = Field(
        None, description="工厂编码", alias="factoryCode"
    )
    begin_apply_time: Optional[int] = Field(
        None, description="开始申请时间", alias="beginApplyTime"
    )
    end_apply_time: Optional[int] = Field(
        None, description="结束申请时间", alias="endApplyTime"
    )
    page_index: Optional[int] = Field(None, description="页面索引", alias="pageIndex")
    page_size: Optional[int] = Field(None, description="页面大小", alias="pageSize")


class RelationListResponse(BaseResponse):
    """查询关系列表响应"""

    pass


# 申请绑定工厂信息
class ApplyBindFactoryInfo(BaseResponse):
    """申请绑定工厂信息"""

    request_id: Optional[str] = Field(None, description="请求ID")
    factory_code: Optional[str] = Field(None, description="工厂编码")
    apply_content: Optional[str] = Field(None, description="申请内容")


# 解绑工厂信息
class UnbindFactoryInfo(BaseResponse):
    """解绑工厂信息"""

    request_id: Optional[str] = Field(None, description="请求ID")
    factory_code: Optional[str] = Field(None, description="工厂编码")


# 代发商品信息
class DropshippingItemInfo(BaseResponse):
    """代发商品信息"""

    item_id: Optional[int] = Field(None, description="商品ID")
    item_name: Optional[str] = Field(None, description="商品名称")
    quantity: Optional[int] = Field(None, description="数量")


# 联系人信息
class ContactInfo(BaseResponse):
    """联系人信息"""

    name: Optional[str] = Field(None, description="姓名")
    phone: Optional[str] = Field(None, description="电话")


# 批量申请商家关系
class RelationMerchantBatchApplyRequest(BaseRequest):
    """批量申请商家关系请求"""

    api_method: str = "open.dropshipping.relation.merchant.batch.apply"
    http_method: HttpMethod = HttpMethod.POST

    apply_request_list: Optional[List[ApplyBindFactoryInfo]] = Field(
        None, description="申请请求列表", alias="applyRequestList"
    )


class RelationMerchantBatchApplyResponse(BaseResponse):
    """批量申请商家关系响应"""

    pass


# 批量解绑商家关系
class RelationMerchantBatchUnbindRequest(BaseRequest):
    """批量解绑商家关系请求"""

    api_method: str = "open.dropshipping.relation.merchant.batch.unbind"
    http_method: HttpMethod = HttpMethod.POST

    unbind_request_list: Optional[List[UnbindFactoryInfo]] = Field(
        None, description="解绑请求列表", alias="unbindRequestList"
    )


class RelationMerchantBatchUnbindResponse(BaseResponse):
    """批量解绑商家关系响应"""

    pass


# 查询角色
class RoleQueryRequest(BaseRequest):
    """查询角色请求"""

    api_method: str = "open.dropshipping.role.query"
    http_method: HttpMethod = HttpMethod.GET

    # 无参数 - 对应空的ParamDTO


class RoleQueryResponse(BaseResponse):
    """查询角色响应"""

    pass
