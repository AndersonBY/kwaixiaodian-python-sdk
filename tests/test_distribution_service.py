"""Distribution service tests aligned with Java SDK reference.

Focus:
- GET vs POST usage for distribution endpoints
- Alias mapping in ParamDTO JSON for representative endpoints
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.distribution import (
    AsyncDistributionService,
    SyncDistributionService,
)
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_cps_order_list_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("open.seller.order.cps.list must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_cps_order_list(
        access_token="t",
        current_page=3,
        page_size=20,
        sort=1,
        query_type=2,
        type=0,
        pcursor="CUR",
        distributor_id=12345,
        begin_time=1700000000,
        end_time=1700001000,
        uid=None,
    )

    assert captured["params"]["method"] == "open.seller.order.cps.list"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    # Alias checks
    assert payload["currentPage"] == 3
    assert payload["pageSize"] == 20
    assert payload["sort"] == 1
    assert payload["queryType"] == 2
    assert payload["type"] == 0
    assert payload["pcursor"] == "CUR"
    assert payload["distributorId"] == 12345
    assert payload["beginTime"] == 1700000000
    assert payload["endTime"] == 1700001000


@pytest.mark.unit
def test_sync_promote_update_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    captured: dict = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data, "verb": "POST"})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("open.distribution.promote.update must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.update_promote(
        access_token="t",
        commission_id=[111, 222],
        status=1,
        uid=None,
    )

    assert captured["data"]["method"] == "open.distribution.promote.update"
    param_json = captured["data"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    # Alias checks
    assert payload["commissionId"] == [111, 222]
    assert payload["status"] == 1
    # basic success path
    assert resp.is_success


@pytest.mark.unit
def test_sync_cps_order_list_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    def _mock_get(url, params):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.get_cps_order_list(access_token="t", page_size=10, uid=None)


@pytest.mark.unit
async def test_async_kwaimoney_order_list_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.cps.kwaimoney.order.list must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_cps_kwaimoney_order_list(
        access_token="t",
        cps_order_status=1,
        page_size=50,
        sort_type=2,
        query_type=3,
        begin_time=1700000000,
        end_time=1700009999,
        pcursor="CUR2",
        uid=None,
    )

    assert captured["params"]["method"] == "open.distribution.cps.kwaimoney.order.list"
    payload = orjson.loads(captured["params"]["param"])
    assert payload["cpsOrderStatus"] == 1
    assert payload["pageSize"] == 50
    assert payload["sortType"] == 2
    assert payload["queryType"] == 3
    assert payload["beginTime"] == 1700000000
    assert payload["endTime"] == 1700009999
    assert payload["pcursor"] == "CUR2"


@pytest.mark.unit
def test_sync_plan_create_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    captured: dict = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data, "verb": "POST"})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("open.distribution.plan.create must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.create_distribute_plan(
        access_token="t",
        plan_create_type="NORMAL",
        normal_plan_param={"foo": "bar"},
        uid=None,
    )

    assert captured["data"]["method"] == "open.distribution.plan.create"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["planCreateType"] == "NORMAL"
    assert payload["normalPlanParam"] == {"foo": "bar"}
    assert resp.is_success


@pytest.mark.unit
async def test_async_investment_open_info_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        await svc.get_investment_activity_open_info(
            access_token="t", activity_id=123, uid=None
        )


@pytest.mark.unit
async def test_async_kwaimoney_pid_list_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.cps.kwaimoney.pid.list must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.get_cps_kwaimoney_pid_list(
        access_token="t", page=2, page_size=30, uid=None
    )

    assert captured["params"]["method"] == "open.distribution.cps.kwaimoney.pid.list"
    payload = orjson.loads(captured["params"]["param"])
    assert payload["page"] == 2
    assert payload["pageSize"] == 30


@pytest.mark.unit
def test_sync_plan_update_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncDistributionService(client)

    captured: dict = {}

    def _mock_post(url, data):
        captured.update({"url": url, "data": data, "verb": "POST"})
        return httpx.Response(200, json={"result": {}})

    def _mock_get(url, params):
        raise AssertionError("open.distribution.plan.update must use POST, not GET")

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = svc.update_distribute_plan(
        access_token="t",
        plan_id=888,
        update_type="STATUS",
        update_plan_status_param={"status": "ENABLED"},
        uid=None,
    )

    assert captured["data"]["method"] == "open.distribution.plan.update"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["planId"] == 888
    assert payload["updateType"] == "STATUS"
    assert payload["updatePlanStatusParam"] == {"status": "ENABLED"}
    assert resp.is_success


@pytest.mark.unit
async def test_async_leader_order_cursor_list_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        await svc.get_cps_leader_order_cursor_list(
            access_token="t", page_size=10, uid=None
        )


@pytest.mark.unit
async def test_async_plan_query_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("open.distribution.plan.query must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.query_plan(access_token="t", item_id=123, uid=None)

    assert captured["params"]["method"] == "open.distribution.plan.query"
    payload = orjson.loads(captured["params"]["param"])
    assert payload["itemId"] == 123


@pytest.mark.unit
async def test_async_plan_commission_query_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params, "verb": "GET"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError(
            "open.distribution.plan.commission.query must use GET, not POST"
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.query_plan_commission(
        access_token="t", plan_id=456, pcursor="CUR", uid=None
    )

    assert captured["params"]["method"] == "open.distribution.plan.commission.query"
    payload = orjson.loads(captured["params"]["param"])
    assert payload["planId"] == 456
    assert payload["pcursor"] == "CUR"


@pytest.mark.unit
async def test_async_kwaimoney_pid_update_uses_post_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    captured: dict = {}

    async def _mock_post(url, data):
        captured.update({"url": url, "data": data, "verb": "POST"})
        return httpx.Response(200, json={"result": {}})

    async def _mock_get(url, params):
        raise AssertionError(
            "open.distribution.cps.kwaimoney.pid.update must use POST, not GET"
        )

    monkeypatch.setattr(client.http_client, "post", _mock_post)
    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.update_cps_kwaimoney_pid(
        access_token="t", cps_pid="PID123", promotion_bit_name="bit", uid=None
    )

    assert captured["data"]["method"] == "open.distribution.cps.kwaimoney.pid.update"
    payload = orjson.loads(captured["data"]["param"])
    assert payload["cpsPid"] == "PID123"
    assert payload["promotionBitName"] == "bit"
    assert resp.is_success


@pytest.mark.unit
async def test_async_seller_activity_open_list_error_path_raises(monkeypatch):
    pytest.skip("Skipped by instruction: no tests this round")
