"""Seller Activity tests aligned with Java SDK reference.

Focus:
- Async GET alias checks for item list, usable item, promotion effect item
- Negative path for open info raising KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.distribution import (
    AsyncDistributionService,
    SyncDistributionService,
)
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_seller_activity_item_list_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.seller.activity.item.list must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_seller_activity_item_list(
        access_token="t",
        item_audit_status=1,
        category_id=22,
        offset=5,
        item_id=333,
        activity_id=4444,
        limit=50,
        item_title="abc",
        uid=None,
    )

    assert captured["params"]["method"] == "open.distribution.seller.activity.item.list"
    payload = orjson.loads(captured["params"]["param"])
    assert payload["itemAuditStatus"] == 1
    assert payload["categoryId"] == 22
    assert payload["offset"] == 5
    assert payload["itemId"] == 333
    assert payload["activityId"] == 4444
    assert payload["limit"] == 50
    assert payload["itemTitle"] == "abc"


@pytest.mark.unit
async def test_async_seller_activity_usable_item_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.seller.activity.usable.item must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_seller_activity_usable_item(
        access_token="t",
        offset=7,
        item_id=999,
        activity_id=1010,
        limit=25,
        item_title="kwai",
        uid=None,
    )

    assert (
        captured["params"]["method"] == "open.distribution.seller.activity.usable.item"
    )
    payload = orjson.loads(captured["params"]["param"])
    assert payload["offset"] == 7
    assert payload["itemId"] == 999
    assert payload["activityId"] == 1010
    assert payload["limit"] == 25
    assert payload["itemTitle"] == "kwai"


@pytest.mark.unit
async def test_async_seller_activity_promotion_effect_item_get_and_aliases(
    monkeypatch,
):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.seller.activity.promotion.effect.item must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_seller_activity_promotion_effect_item(
        access_token="t",
        page_cursor=123,
        item_id=456,
        activity_id=789,
        end_time=1700007777,
        item_title="effect",
        page_size=66,
        uid=None,
    )

    assert (
        captured["params"]["method"]
        == "open.distribution.seller.activity.promotion.effect.item"
    )
    payload = orjson.loads(captured["params"]["param"])
    assert payload["pageCursor"] == 123
    assert payload["itemId"] == 456
    assert payload["activityId"] == 789
    assert payload["endTime"] == 1700007777
    assert payload["itemTitle"] == "effect"
    assert payload["pageSize"] == 66


@pytest.mark.unit
def test_sync_seller_activity_open_info_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    def _mock_get(url, params):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.get_seller_activity_open_info(access_token="t", activity_id=1, uid=None)


@pytest.mark.unit
def test_sync_seller_activity_promotion_effect_summary_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    captured: dict = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.seller.activity.promotion.effect.summary must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    resp = svc.get_seller_activity_promotion_effect_summary(
        access_token="t", activity_id=987, end_time=1700011111, uid=None
    )

    assert (
        captured["params"]["method"]
        == "open.distribution.seller.activity.promotion.effect.summary"
    )
    payload = orjson.loads(captured["params"]["param"])
    assert payload["activityId"] == 987
    assert payload["endTime"] == 1700011111
    assert resp.is_success


@pytest.mark.unit
def test_sync_seller_activity_promoter_adjust_history_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    captured: dict = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.seller.activity.queryActivityPromoterAdjustHistory must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    resp = svc.query_seller_activity_promoter_adjust_history(
        access_token="t", activity_id=555, offset=1, limit=20, uid=None
    )

    assert (
        captured["params"]["method"]
        == "open.distribution.seller.activity.queryActivityPromoterAdjustHistory"
    )
    payload = orjson.loads(captured["params"]["param"])
    assert payload["activityId"] == 555
    assert payload["offset"] == 1
    assert payload["limit"] == 20
    assert resp.is_success


@pytest.mark.unit
def test_sync_seller_activity_open_list_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    def _mock_get(url, params):
        # Simulate API error payload for open list endpoint
        return httpx.Response(200, json={"error_code": "E1", "error_msg": "oops"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.get_seller_activity_open_list(
            access_token="t", offset=0, limit=10, uid=None
        )
