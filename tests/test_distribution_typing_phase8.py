from __future__ import annotations

import httpx

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient
from kwaixiaodian.client.services.distribution import AsyncDistributionService


async def test_brand_theme_item_list_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "itemList": [
                        {"goodsId": 100, "goodsTitle": "G1"},
                        {"goodsId": 200, "goodsTitle": "G2"},
                    ],
                    "orderType": [{"name": "销量", "type": 1}],
                    "pcursor": "bti-next",
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_brand_theme_item_list(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.pcursor == "bti-next"
    assert resp.result.item_list and resp.result.item_list[0].goods_id == 100


async def test_brand_theme_shop_list_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "shopList": [{"shopId": 9, "shopName": "ShopA", "itemNum": 3}],
                    "pcursor": "bts-next",
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_brand_theme_shop_list(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.pcursor == "bts-next"
    assert resp.result.shop_list and resp.result.shop_list[0].shop_id == 9


async def test_reco_topic_seller_list_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "sellerList": [
                        {"shopId": 123, "shopName": "S1", "shopStar": "4.9"}
                    ],
                    "pcursor": "rt-next",
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_reco_topic_seller_list(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.pcursor == "rt-next"
    assert resp.result.seller_list and resp.result.seller_list[0].shop_id == 123
