"""Refund service tests aligned with Java SDK reference.

Covers:
- GET vs POST usage for refund endpoints
- Alias mapping in ParamDTO JSON (e.g., refundId, reasonCode)
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.refund import AsyncRefundService, SyncRefundService
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_refund_detail_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncRefundService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("Refund detail must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get(access_token="t", refund_id=123)

    assert captured["params"]["method"] == "open.seller.order.refund.detail"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["refundId"] == 123


@pytest.mark.unit
def test_sync_refund_reject_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncRefundService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("Refund reject must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.reject(access_token="t", refund_id=11, reason_code=5, reject_desc="no")

    assert captured["data"]["method"] == "open.refund.reject"
    param_json = captured["data"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["refundId"] == 11
    assert payload["reasonCode"] == 5
    assert payload["rejectDesc"] == "no"


@pytest.mark.unit
async def test_async_refund_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncRefundService(client)

    async def _mock_get(url, params):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        await svc.get(access_token="t", refund_id=999)
