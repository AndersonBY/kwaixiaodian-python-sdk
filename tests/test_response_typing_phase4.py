from __future__ import annotations

import httpx
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import SyncBaseClient
from kwaixiaodian.client.services.funds import SyncFundsService
from kwaixiaodian.client.services.order import SyncOrderService
from kwaixiaodian.models.funds import FundsFinancialBillListData
from kwaixiaodian.models.order import ExternalOrderRelationData, MerchantOrderInfoView


@pytest.mark.unit
def test_sync_external_order_relation_response_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    payload = {
        "result": {
            "jdOrder": {
                "channelId": 1,
                "pin": "PIN",
                "orderId": 123,
                "jdOrderId": "JD-001",
            }
        }
    }

    def _mock_get(url, params):
        return httpx.Response(200, json=payload)

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.get_external_order_relation(access_token="t", order_id=42)
    assert isinstance(resp.result, ExternalOrderRelationData)
    assert resp.result.jd_order is not None
    assert resp.result.jd_order.channel_id == 1
    assert resp.result.jd_order.jd_order_id == "JD-001"


@pytest.mark.unit
def test_sync_funds_financial_query_bill_list_response_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncFundsService(client)

    payload = {
        "result": {
            "total": 2,
            "scrollId": "SCROLL-1",
            "distributorSettledOrderData": {
                "data": [
                    {
                        "orderNo": 111,
                        "productId": "P1",
                        "productName": "Item 1",
                        "actualPayAmount": "100.00",
                    }
                ]
            },
            "distributorUnSettledOrderData": {
                "data": [
                    {
                        "orderNo": 222,
                        "productId": "P2",
                        "productName": "Item 2",
                        "actualPayAmount": "200.00",
                    }
                ]
            },
        }
    }

    def _mock_get(url, params):
        return httpx.Response(200, json=payload)

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.query_financial_bill_list(access_token="t")
    assert isinstance(resp.result, FundsFinancialBillListData)
    assert resp.result.total == 2
    assert resp.result.scroll_id == "SCROLL-1"
    assert resp.result.distributor_settled_order_data is not None
    assert resp.result.distributor_settled_order_data.data is not None
    assert resp.result.distributor_settled_order_data.data[0].order_no == 111
    assert resp.result.distributor_unsettled_order_data is not None
    assert resp.result.distributor_unsettled_order_data.data is not None
    assert resp.result.distributor_unsettled_order_data.data[0].order_no == 222


@pytest.mark.unit
def test_order_money_helpers_from_seller_detail(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    payload = {
        "result": {
            "totalFee": 12345,
            "expressFee": 600,
            "discountFee": 45,
            "orderProductInfoList": [
                {"itemId": 1, "price": 200, "originalPrice": 300},
            ],
        }
    }

    def _mock_get(url, params):
        return httpx.Response(200, json=payload)

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.get_seller_detail(access_token="t", order_id=1)
    assert isinstance(resp.result, MerchantOrderInfoView)
    assert resp.result.total_fee_yuan == 123.45
    assert resp.result.express_fee_yuan == 6.0
    assert resp.result.discount_fee_yuan == 0.45
    p = resp.result.order_product_info_list[0]
    assert p.price_yuan == 2.0
    assert p.original_price_yuan == 3.0
