"""Tests for AsyncBaseClient and SyncBaseClient execute and validation paths"""

import asyncio

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.exceptions import KwaixiaodianAPIError, KwaixiaodianValidationError
from kwaixiaodian.models.base import BaseRequest, BaseResponse
from kwaixiaodian.models.comment import CommentListRequest


class _DummyReq(BaseRequest):
    # Simple request with constant method
    @property
    def api_method(self) -> str:  # type: ignore[override]
        return "open.ping"


class _DummyResp(BaseResponse[dict]):
    pass


async def test_async_execute_success(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)

    # Prepare request (GET) and mock HTTP client
    req = CommentListRequest(access_token="t")

    async def _mock_get(url, params):
        return httpx.Response(200, json={"result": {"items": [], "total": 0}})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    # Use a generic response type to validate client parsing, independent of domain models
    resp = await client.execute(req, _DummyResp)
    assert resp.is_success
    assert resp.result is not None


async def test_async_execute_http_error(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    req = _DummyReq(access_token="t")

    async def _mock_post(url, data):
        return httpx.Response(500, text="boom")

    monkeypatch.setattr(client.http_client, "post", _mock_post)

    with pytest.raises(KwaixiaodianAPIError):
        await client.execute(req, _DummyResp)


async def test_async_execute_api_error(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    req = _DummyReq(access_token="t")

    async def _mock_post(url, data):
        return httpx.Response(
            200, json={"error_code": "INVALID_REQUEST", "error_msg": "bad"}
        )

    monkeypatch.setattr(client.http_client, "post", _mock_post)

    with pytest.raises(KwaixiaodianAPIError):
        await client.execute(req, _DummyResp)


def test_async_execute_validation_error():
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    req = _DummyReq(access_token="")

    with pytest.raises(KwaixiaodianValidationError):
        asyncio.run(client.execute(req, _DummyResp))


def test_sync_execute_success(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    req = _DummyReq(access_token="t")

    def _mock_post(url, data):
        return httpx.Response(200, json={"result": {}})

    monkeypatch.setattr(client.http_client, "post", _mock_post)

    resp = client.execute(req, _DummyResp)
    assert resp.is_success


def test_sync_execute_api_error(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    req = _DummyReq(access_token="t")

    def _mock_post(url, data):
        return httpx.Response(200, json={"error_code": "INVALID", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "post", _mock_post)

    with pytest.raises(KwaixiaodianAPIError):
        client.execute(req, _DummyResp)


async def test_async_execute_get_branch(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)

    from kwaixiaodian.models.base import HttpMethod  # local import to avoid cycle

    class _GetReq(BaseRequest):
        @property
        def api_method(self) -> str:  # type: ignore[override]
            return "open.ping"

        @property
        def http_method(self) -> HttpMethod:  # type: ignore[override]
            return HttpMethod.GET

    async def _mock_get(url, params):
        return httpx.Response(200, json={"result": {"pong": True}})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    res = await client.execute(_GetReq(access_token="t"), _DummyResp)
    assert res.is_success


def test_sync_execute_json_decode_error(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)

    class DummyResp:
        status_code = 200
        text = "invalid"

        def json(self):
            # Simulate orjson decode error path
            raise orjson.JSONDecodeError("x", b"x", 0)  # type: ignore[arg-type]

    def _mock_post(url, data):
        return DummyResp()

    monkeypatch.setattr(client.http_client, "post", _mock_post)

    with pytest.raises(KwaixiaodianAPIError):
        client.execute(_DummyReq(access_token="t"), _DummyResp)


def test_sync_execute_wraps_non_sdk_error(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)

    # cause a non-SDK exception inside execute try-block
    def _boom(*args, **kwargs):
        raise ValueError("boom")

    monkeypatch.setattr(client.signature_manager, "build_signed_params", _boom)

    with pytest.raises(KwaixiaodianAPIError):
        client.execute(_DummyReq(access_token="t"), _DummyResp)
