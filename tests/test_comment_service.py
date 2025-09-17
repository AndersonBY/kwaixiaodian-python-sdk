"""Comment service tests aligned with Java SDK reference.

Covers:
- GET vs POST usage for comment endpoints
- Alias mapping in ParamDTO JSON
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.comment import AsyncCommentService, SyncCommentService
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_comment_list_get_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncCommentService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {"total": 0}})

    async def _mock_post(url, data):
        raise AssertionError("open.comment.list.get must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.list_comments(
        access_token="t", out_order_no="O-1", service_score=[5], limit=10
    )

    assert captured["params"]["method"] == "open.comment.list.get"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    # alias keys
    assert payload["outOrderNo"] == "O-1"
    assert payload["serviceScore"] == [5]
    assert payload["limit"] == 10


@pytest.mark.unit
def test_sync_comment_add_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCommentService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {"ok": True}})

    def _mock_get(url, params):
        raise AssertionError("open.comment.add must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.reply_comment(
        access_token="t",
        comment_id="12345",
        reply_content="Thanks",
        is_official=True,
        out_info={"k": "v"},
    )

    assert captured["data"]["method"] == "open.comment.add"
    p = captured["data"].get("param")
    assert isinstance(p, str)
    payload = orjson.loads(p)
    assert payload["replyToCommentId"] == 12345
    assert payload["content"] == "Thanks"
    assert payload["option"]["official"] is True
    assert payload["outInfo"]["k"] == "v"
    assert resp.is_success


@pytest.mark.unit
def test_sync_comment_list_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCommentService(client)

    def _mock_get(url, params):
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.list_comments(access_token="t", limit=1)
