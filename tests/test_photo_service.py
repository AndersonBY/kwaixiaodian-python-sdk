from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.photo import AsyncPhotoService, SyncPhotoService


@pytest.mark.unit
async def test_async_photo_info_get_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncPhotoService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {"ok": True}})

    async def _mock_post(url, data):
        raise AssertionError("open.photo.info must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.info(access_token="t", photo_id="P123")

    assert captured["params"]["method"] == "open.photo.info"
    p = captured["params"].get("param")
    payload = orjson.loads(p)
    assert payload["photoId"] == "P123"


@pytest.mark.unit
def test_sync_photo_publish_post_and_alias(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncPhotoService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {"ok": True}})

    def _mock_get(url, params):
        raise AssertionError("open.photo.publish must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.publish(access_token="t", upload_token="UT-1")

    assert captured["data"]["method"] == "open.photo.publish"
    p = orjson.loads(captured["data"].get("param"))
    assert p["uploadToken"] == "UT-1"
