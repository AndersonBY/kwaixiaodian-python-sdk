"""User service tests aligned with Java SDK reference.

Covers:
- GET vs POST usage for user endpoints
- Alias mapping in ParamDTO JSON (e.g., fromOpenId, userName, count)
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.user import AsyncUserService, SyncUserService
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_user_fans_check_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncUserService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("open.user.fans.check must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.check_fans(access_token="t", from_open_id="FOO_OPEN_ID", uid=None)

    assert captured["params"]["method"] == "open.user.fans.check"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["fromOpenId"] == "FOO_OPEN_ID"


@pytest.mark.unit
def test_sync_user_sub_account_list_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncUserService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        # Minimal successful payload consistent with Staffs model
        return httpx.Response(200, json={"result": {"staffs": [], "totalCount": 0}})

    def _mock_get(url, params):
        raise AssertionError("open.user.sub.account.list must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.list_sub_accounts(
        access_token="t",
        user_name="alice",
        count=10,
        page=2,
        include_deleted=True,
        include_disabled=True,
        uid=None,
    )

    # Ensure signed POST params include correct method and alias-mapped ParamDTO JSON
    assert captured["data"]["method"] == "open.user.sub.account.list"
    param_json = captured["data"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["userName"] == "alice"
    assert payload["count"] == 10
    assert payload["page"] == 2
    assert payload["includeDeleted"] is True
    assert payload["includeDisabled"] is True

    # Response parsing sanity
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.total_count == 0
    assert isinstance(resp.result.staffs, list)


@pytest.mark.unit
def test_sync_user_info_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncUserService(client)

    def _mock_get(url, params):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.get_info(access_token="t", uid=None)
