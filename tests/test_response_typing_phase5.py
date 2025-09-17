from __future__ import annotations

import httpx

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient
from kwaixiaodian.client.services.distribution import AsyncDistributionService
from kwaixiaodian.client.services.funds import AsyncFundsService


async def test_funds_settled_bill_detail_typed_response(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncFundsService(client)

    async def _mock_get(url, params):
        # Mimic Java-aligned data shape: OpenApiQueryOrderBillDetailResponse
        return httpx.Response(
            200,
            json={
                "result": {
                    "orders": [
                        {
                            "orderNo": 123,
                            "productId": "P1",
                            "productName": "商品1",
                            "productNum": 2,
                            "orderCreateTime": "2024-01-02 03:04:05",
                            "actualPayAmount": "199.00",
                            "platformAllowanceAmount": "10.00",
                            "totalIncome": "189.00",
                            "totalRefundAmount": "0.00",
                            "platformCommissionAmount": "5.00",
                            "distributorId": "D001",
                            "distributorCommissionAmount": "3.00",
                            "settlementStatus": "DONE",
                            "settlementAmount": "181.00",
                            "settlementTime": "2024-01-03 01:02:03",
                            "accountChannel": "WX",
                            "accountName": "WeChat",
                            "refundInfo": [
                                {
                                    "platformAllowanceRefund": 0,
                                    "actualPayRefund": 0,
                                    "refundId": 0,
                                    "platformPayMarketAllowanceRefund": 0,
                                }
                            ],
                        }
                    ],
                    "cursor": "next-cursor",
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_settled_bill_detail(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.cursor == "next-cursor"
    assert resp.result.orders is not None
    assert resp.result.orders[0].order_no == 123
    assert resp.result.orders[0].product_name == "商品1"
    assert resp.result.orders[0].account_channel == "WX"
    # String money fields preserved (Java-aligned)
    assert resp.result.orders[0].actual_pay_amount == "199.00"


async def test_distribution_kwaimoney_promotion_trend_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": [
                    {"date": "2024-01-01", "totalUv": 10},
                    {"date": "2024-01-02", "totalUv": 20},
                ]
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_kwaimoney_promotion_effect_trend(
        access_token="t", begin_time=1, end_time=2
    )
    assert resp.is_success
    assert isinstance(resp.result, list)
    assert resp.result[0].date == "2024-01-01"
    assert resp.result[1].total_uv == 20


async def test_distribution_kwaimoney_promotion_effect_detail_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "detailList": [
                        {
                            "date": "2024-01-01",
                            "itemId": 111,
                            "itemName": "X",
                            "itemPrice": 12345,
                            "promoterId": 222,
                            "promoterName": "Alice",
                            "cpsPid": "pid1",
                            "uv": 99,
                            "orderId": 333,
                            "virtualDeviceId": "vdid",
                        }
                    ],
                    "total": 1,
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_effect_detail(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.total == 1
    assert resp.result.detail_list is not None
    d0 = resp.result.detail_list[0]
    assert d0.item_id == 111
    assert d0.promoter_name == "Alice"
    assert d0.cps_pid == "pid1"
