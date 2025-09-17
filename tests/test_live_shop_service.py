"""Live shop (shoplive) service tests aligned with Java SDK reference.

Covers:
- GET method usage for shoplive endpoints
- Alias mapping in ParamDTO JSON (itemId, userOpenId, actionScene)
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.live import AsyncLiveService, SyncLiveService
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_user_car_action_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncLiveService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):  # pragma: no cover - should not be called
        raise AssertionError("shoplive.user.car.action must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_user_car_action(
        access_token="t", user_open_id="U1", action_scene=[1, 2], uid=None
    )

    # Ensure signed GET params include correct method and alias-mapped ParamDTO JSON
    assert captured["params"]["method"] == "open.live.shop.user.car.action"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["userOpenId"] == "U1"
    assert payload["actionScene"] == [1, 2]


@pytest.mark.unit
async def test_async_item_check_oncar_response_parsing(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncLiveService(client)

    async def _mock_get(url, params):
        return httpx.Response(200, json={"result": {"liveCarItem": True}})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.check_item_oncar(access_token="t", item_id=123, uid=None)

    assert resp.is_success
    assert resp.result is not None
    assert resp.result.liveCarItem is True


@pytest.mark.unit
def test_sync_seller_real_uv_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncLiveService(client)

    def _mock_get(url, params):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.get_seller_real_uv(access_token="t", uid=None)
