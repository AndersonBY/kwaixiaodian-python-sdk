from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.funds import SyncFundsService
from kwaixiaodian.client.services.order import AsyncOrderService, SyncOrderService


@pytest.mark.unit
def test_sync_order_seller_detail_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    captured = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    def _mock_post(url, data):
        raise AssertionError("open.seller.order.detail must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    svc.get_seller_detail(access_token="t", order_id=12345)

    assert captured["params"]["method"] == "open.seller.order.detail"
    p = orjson.loads(captured["params"].get("param"))
    assert p["orderId"] == 12345


@pytest.mark.unit
def test_sync_order_external_order_relation_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    captured = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.get_external_order_relation(access_token="t", order_id=777)

    assert captured["params"]["method"] == "open.external.order.relation"
    p = orjson.loads(captured["params"].get("param"))
    assert p["orderId"] == 777


@pytest.mark.unit
async def test_async_order_seller_pcursor_list_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncOrderService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {"items": []}})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    await svc.seller_pcursor_list(
        access_token="t",
        begin_time=1704067200000,
        end_time=1706745599000,
        page_size=50,
        pcursor="NEXT",
    )

    assert captured["params"]["method"] == "open.seller.order.pcursor.list"
    p = orjson.loads(captured["params"].get("param"))
    # time aliases
    assert p["beginTime"] == 1704067200000
    assert p["endTime"] == 1706745599000
    # pagination aliases
    assert p["pageSize"] == 50
    assert p["pcursor"] == "NEXT"


@pytest.mark.unit
def test_sync_order_query_kspay_promo_detail_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncOrderService(client)

    captured = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    def _mock_post(url, data):
        raise AssertionError(
            "open.query.order.kspay.promo.detail must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    svc.query_kspay_promo_detail(
        access_token="t",
        order_id=999,
        buyer_open_id="B",
        seller_open_id="S",
        query_source="SRC",
    )

    assert captured["params"]["method"] == "open.query.order.kspay.promo.detail"
    p = orjson.loads(captured["params"].get("param"))
    assert p["orderId"] == 999
    assert p["buyerOpenId"] == "B"
    assert p["sellerOpenId"] == "S"
    assert p["querySource"] == "SRC"


@pytest.mark.unit
def test_sync_funds_financial_query_bill_list_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncFundsService(client)

    captured = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    def _mock_post(url, data):
        raise AssertionError(
            "open.funds.financial.query.bill.list must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    svc.query_financial_bill_list(
        access_token="t",
        start_time=1704067200000,
        end_time=1706745599000,
        bill_type="ORDER",
        account_channel=["WX", "ALI"],
        scroll_id="SCROLL",
    )

    assert captured["params"]["method"] == "open.funds.financial.query.bill.list"
    p = orjson.loads(captured["params"].get("param"))
    assert p["startTime"] == 1704067200000
    assert p["endTime"] == 1706745599000
    assert p["billType"] == "ORDER"
    assert p["accountChannel"] == ["WX", "ALI"]
    assert p["scrollId"] == "SCROLL"
