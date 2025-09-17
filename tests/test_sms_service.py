from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.sms import AsyncSmsService, SyncSmsService


@pytest.mark.unit
def test_sync_sms_send_post_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncSmsService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {"ok": True}})

    def _mock_get(url, params):
        raise AssertionError("open.sms.send must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.send(
        access_token="t",
        sign_id=1,
        template_id=2,
        template_param='{"code":"1234"}',
        mobile="13800000000",
        extra="x",
    )

    assert captured["data"]["method"] == "open.sms.send"
    p = orjson.loads(captured["data"].get("param"))
    assert p["signId"] == 1
    assert p["templateId"] == 2
    assert p["templateParam"].startswith("{")
    assert p["mobile"] == "13800000000"


@pytest.mark.unit
async def test_async_sms_template_view_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncSmsService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("open.sms.template.view must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.view_templates(access_token="t", template_id=100)

    assert captured["params"]["method"] == "open.sms.template.view"
    p = orjson.loads(captured["params"].get("param"))
    assert p["templateId"] == 100
