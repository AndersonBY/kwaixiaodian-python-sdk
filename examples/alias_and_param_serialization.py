"""
示例：字段别名与 param 拆箱的序列化行为

运行：
  pdm run python examples/alias_and_param_serialization.py
"""

from kwaixiaodian.models.order import OrderGetRequest
from kwaixiaodian.models.service_market import (
    ServiceMarketOrderDetailParam,
    ServiceMarketOrderDetailRequest,
)


def main() -> None:
    # 例1：直接字段 → 使用别名键（Java: oid）
    order_req = OrderGetRequest(access_token="TOKEN", order_id=123)
    print("OrderGetRequest business params:", order_req.get_business_params())

    # 例2：仅包含 param 字段的请求 → 自动拆箱
    svc_req = ServiceMarketOrderDetailRequest(
        access_token="TOKEN",
        param=ServiceMarketOrderDetailParam(oid=456),
    )
    print(
        "ServiceMarketOrderDetailRequest business params:",
        svc_req.get_business_params(),
    )


if __name__ == "__main__":
    main()
