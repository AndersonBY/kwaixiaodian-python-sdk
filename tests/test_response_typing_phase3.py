from __future__ import annotations

import httpx
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.order import AsyncOrderService, SyncOrderService
from kwaixiaodian.models.order import (
    MerchantOrderInfoView,
    MerchantOrderListData,
    OrderKspayPromoData,
)


@pytest.mark.unit
def test_sync_kspay_promo_detail_response_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    payload = {
        "result": {
            "orderBaseInfo": {
                "providerTradeNo": "PTN123",
                "payChannel": "WX",
                "allRefund": False,
                "actualPayFee": 12345,
            },
            "orderKspayPromoDetail": {
                "otherDiscountAmount": 200,
                "governmentSubsidyAmount": 300,
                "governmentSubsidy": True,
            },
        }
    }

    def _mock_get(url, params):
        return httpx.Response(200, json=payload)

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.query_kspay_promo_detail(access_token="t", order_id=1)
    assert isinstance(resp.result, OrderKspayPromoData)
    assert resp.result.order_base_info is not None
    assert resp.result.order_base_info.provider_trade_no == "PTN123"
    assert resp.result.order_base_info.pay_channel == "WX"
    assert resp.result.order_base_info.actual_pay_fee == 12345
    assert resp.result.order_base_info.actual_pay_yuan == 123.45
    assert resp.result.order_kspay_promo_detail is not None
    assert resp.result.order_kspay_promo_detail.government_subsidy is True


@pytest.mark.unit
def test_sync_seller_order_detail_response_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    payload = {
        "result": {
            "buyerNick": "Alice",
            "sellerId": 1001,
            "orderProductInfoList": [
                {
                    "itemId": 123456,
                    "skuId": 7890,
                    "num": 2,
                    "price": 9999,
                }
            ],
            "logisticsInfo": {"expressNo": "SF123", "expressCode": 1},
        }
    }

    def _mock_get(url, params):
        return httpx.Response(200, json=payload)

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.get_seller_detail(access_token="t", order_id=42)
    assert isinstance(resp.result, MerchantOrderInfoView)
    assert resp.result.buyer_nick == "Alice"
    assert resp.result.seller_id == 1001
    assert resp.result.logistics_info is not None
    assert resp.result.logistics_info.express_no == "SF123"
    assert resp.result.order_product_info_list is not None
    assert resp.result.order_product_info_list[0].item_id == 123456


@pytest.mark.unit
@pytest.mark.asyncio
async def test_async_seller_pcursor_list_response_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncOrderService(client)

    payload = {
        "result": {
            "currentPage": 1,
            "pageSize": 50,
            "totalPage": 10,
            "totalSize": 500,
            "beginTime": 1704067200000,
            "endTime": 1706745599000,
            "pcursor": "NXT",
            "orderInfoList": [
                {
                    "buyerNick": "Bob",
                    "sellerId": 1002,
                    "num": 1,
                    "totalFee": 1000,
                }
            ],
        }
    }

    async def _mock_get(url, params):
        return httpx.Response(200, json=payload)

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.seller_pcursor_list(
        access_token="t",
        begin_time=1704067200000,
        end_time=1706745599000,
        page_size=50,
    )
    assert isinstance(resp.result, MerchantOrderListData)
    assert resp.result.current_page == 1
    assert resp.result.page_size == 50
    assert resp.result.pcursor == "NXT"
    assert resp.result.order_info_list is not None
    assert resp.result.order_info_list[0].buyer_nick == "Bob"
