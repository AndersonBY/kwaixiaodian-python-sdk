"""Shop service tests aligned with Java SDK reference.

Covers:
- GET vs POST usage for shop endpoints
- Alias mapping in ParamDTO JSON (e.g., pageNum/pageSize, brandList)
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.shop import AsyncShopService, SyncShopService
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_shop_brand_page_get_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncShopService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": []})

    async def _mock_post(url, data):
        raise AssertionError("Shop brand page must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.brand_page_get(access_token="t", page_num=2, page_size=50, uid=None)

    assert captured["params"]["method"] == "open.shop.brand.page.get"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["pageNum"] == 2
    assert payload["pageSize"] == 50


@pytest.mark.unit
def test_sync_shop_brand_batch_add_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncShopService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {"ok": True}})

    def _mock_get(url, params):
        raise AssertionError("Shop brand batch add must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    brands = [{"name": "A"}, {"name": "B"}]
    resp = svc.brand_batch_add(access_token="t", brand_list=brands, uid=None)

    assert captured["data"]["method"] == "open.shop.brand.batch.add"
    p = captured["data"].get("param")
    assert isinstance(p, str)
    payload = orjson.loads(p)
    assert isinstance(payload.get("brandList"), list)
    assert len(payload["brandList"]) == 2
    assert resp.is_success


@pytest.mark.unit
def test_sync_shop_info_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncShopService(client)

    def _mock_get(url, params):
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.info(access_token="t", uid=None)
