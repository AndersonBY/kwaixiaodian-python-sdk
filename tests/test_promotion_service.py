from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.promotion import (
    AsyncPromotionService,
    SyncPromotionService,
)


@pytest.mark.unit
def test_sync_promotion_coupon_statistic_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncPromotionService(client)

    captured = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {"total": 0}})

    def _mock_post(url, data):
        raise AssertionError("open.promotion.coupon.statistic must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    svc.get_coupon_statistic(access_token="t", coupon_id=12345, business_line=2)

    assert captured["params"]["method"] == "open.promotion.coupon.statistic"
    p = orjson.loads(captured["params"].get("param"))
    assert p["couponId"] == 12345
    assert p["businessLine"] == 2


@pytest.mark.unit
async def test_async_promotion_crowd_list_post_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncPromotionService(client)

    captured = {}

    async def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {"items": []}})

    async def _mock_get(url, params):
        raise AssertionError("open.promotion.crowd.list must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    await svc.list_crowds(access_token="t", crowd_type=1, page_num=1, page_size=10)

    assert captured["data"]["method"] == "open.promotion.crowd.list"
    p = orjson.loads(captured["data"].get("param"))
    assert p["crowdType"] == 1
    assert p["pageNum"] == 1
    assert p["pageSize"] == 10
