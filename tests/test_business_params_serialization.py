import pytest

from kwaixiaodian.models.order import OrderGetRequest
from kwaixiaodian.models.service_market import (
    ServiceMarketOrderDetailParam,
    ServiceMarketOrderDetailRequest,
)


@pytest.mark.unit
def test_business_params_uses_aliases_order_get():
    req = OrderGetRequest(access_token="token", order_id=123)
    params = req.get_business_params()

    # Should use alias 'oid' and not expose snake_case 'order_id'
    assert "oid" in params
    assert params["oid"] == 123
    assert "order_id" not in params


@pytest.mark.unit
def test_business_params_param_unwrap_service_market_detail():
    req = ServiceMarketOrderDetailRequest(
        access_token="token",
        param=ServiceMarketOrderDetailParam(oid=456),
    )
    params = req.get_business_params()

    # Only 'param' is present in the request payload; it should be unwrapped
    assert params == {"oid": 456}
