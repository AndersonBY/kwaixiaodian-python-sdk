"""Customer Service HTTP + alias tests aligned with Java SDK reference.

Covers:
- POST verb usage for CS endpoints
- Alias mapping in ParamDTO JSON (e.g., groupName, groupId)
- Nested alias serialization (nickName, contentType)
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.customer_service import (
    AsyncCustomerServiceService,
    SyncCustomerServiceService,
)
from kwaixiaodian.exceptions import KwaixiaodianAPIError
from kwaixiaodian.models.customer_service import CsUser, MessageContent


@pytest.mark.unit
def test_sync_cs_dispatch_group_add_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("Dispatch group add must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.add_dispatch_group(access_token="t", group_name="VIP组", uid=None)

    assert captured["data"]["method"] == "open.cs.dispatching.group.add"
    param_json = captured["data"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["groupName"] == "VIP组"


@pytest.mark.unit
def test_sync_cs_dispatch_group_query_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("Dispatch group query must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.query_dispatch_group(access_token="t", group_id=123, uid=None)

    assert captured["data"]["method"] == "open.cs.dispatching.group.query"
    param_json = captured["data"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["groupId"] == 123


@pytest.mark.unit
async def test_async_cs_intelligent_message_send_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncCustomerServiceService(client)

    captured = {}

    async def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    async def _mock_get(url, params):
        raise AssertionError("Intelligent message send must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    to_user = CsUser(nick_name="nick", role=1)
    message_list = [MessageContent(content_type=1, content="hello")]

    await svc.send_intelligent_message(
        access_token="t",
        to_user=to_user,
        message_list=message_list,
        uid=None,
    )

    assert captured["data"]["method"] == "open.cs.intelligent.message.send"
    param_json = captured["data"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    # Nested alias keys
    assert payload["toUser"]["nickName"] == "nick"
    assert payload["toUser"]["role"] == 1
    assert isinstance(payload["messageList"], list) and payload["messageList"]
    assert payload["messageList"][0]["contentType"] == 1
    assert payload["messageList"][0]["content"] == "hello"


@pytest.mark.unit
def test_sync_cs_negative_path_raises_api_error(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    def _mock_post(url, data):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "post", _mock_post)

    with pytest.raises(KwaixiaodianAPIError):
        svc.query_dispatch_group(access_token="t", group_id=999, uid=None)


@pytest.mark.unit
def test_sync_cs_logistics_session_create_callback_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("logistics.session.create.callback must use POST")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.create_logistics_session_callback(
        access_token="t",
        assistant_id="a1",
        ks_session_id="ks1",
        session_id="s1",
        session_type=2,
        uid=None,
    )

    assert captured["data"]["method"] == "open.cs.logistics.session.create.callback"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["assistantId"] == "a1"
    assert payload["ksSessionId"] == "ks1"
    assert payload["sessionId"] == "s1"
    assert payload["sessionType"] == 2


@pytest.mark.unit
def test_sync_cs_mapping_add_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("dispatching.mapping.commodity.add must use POST")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.add_commodity_mapping(
        access_token="t", commodity_id=123456, group_id=789, uid=None
    )

    assert captured["data"]["method"] == "open.cs.dispatching.mapping.commodity.add"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["commodityId"] == 123456
    assert payload["groupId"] == 789


@pytest.mark.unit
def test_sync_cs_mapping_del_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("dispatching.mapping.commodity.del must use POST")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.delete_commodity_mapping(
        access_token="t", commodity_id=654321, group_id=321, uid=None
    )

    assert captured["data"]["method"] == "open.cs.dispatching.mapping.commodity.del"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["commodityId"] == 654321
    assert payload["groupId"] == 321


@pytest.mark.unit
def test_sync_cs_mapping_query_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("dispatching.mapping.commodity.query must use POST")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.query_commodity_mapping(access_token="t", commodity_id=777, uid=None)

    assert captured["data"]["method"] == "open.cs.dispatching.mapping.commodity.query"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["commodityId"] == 777


@pytest.mark.unit
def test_sync_cs_mapping_query_default_uses_post_and_no_param(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError(
            "dispatching.mapping.commodity.query_default must use POST"
        )

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.query_default_commodity_mapping(access_token="t", uid=None)

    assert (
        captured["data"]["method"]
        == "open.cs.dispatching.mapping.commodity.query_default"
    )
    # No ParamDTO fields; param should be omitted entirely
    assert "param" not in captured["data"]


@pytest.mark.unit
def test_sync_cs_intelligent_evaluation_message_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncCustomerServiceService(client)

    captured = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("intelligent.evaluation.message must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    svc.send_intelligent_evaluation_message(
        access_token="t", to_user_id="UID_123", uid=None
    )

    assert captured["data"]["method"] == "open.cs.intelligent.evaluation.message"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["toUserId"] == "UID_123"
