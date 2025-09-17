"""Funds service tests aligned with Java SDK reference.

Covers:
- GET method usage for funds endpoints
- Alias mapping in ParamDTO JSON (e.g., withdrawMoney, withdrawNo)
- Basic response parsing for async/sync services
"""

from __future__ import annotations

import httpx
import orjson

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.funds import AsyncFundsService, SyncFundsService
from kwaixiaodian.models.funds import (
    FundsAccountInfoRequest,
    FundsWithdrawApplyRequest,
)


async def test_async_funds_apply_withdraw_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncFundsService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("Funds.apply_withdraw must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.apply_withdraw(
        access_token="t",
        withdraw_money=12345,
        withdraw_no="WD1",
        remark="r",
        account_channel=2,
        sub_merchant_id="sub",
    )

    # Ensure signed GET params include correct method and alias-mapped ParamDTO JSON
    assert captured["params"]["method"] == "open.funds.center.withdraw.apply"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["withdrawMoney"] == 12345
    assert payload["withdrawNo"] == "WD1"
    assert payload["remark"] == "r"
    assert payload["accountChannel"] == 2
    assert payload["subMerchantId"] == "sub"


async def test_async_funds_list_withdraw_records_aliases_and_response(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncFundsService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        # Return minimal paged structure
        return httpx.Response(200, json={"result": {"items": []}})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.list_withdraw_records(
        access_token="t",
        limit=50,
        page=2,
        create_time_start=1700000000,
        create_time_end=1700003600,
        account_channel=1,
        sub_merchant_id="sub",
    )

    assert resp.is_success
    assert resp.result is not None
    assert resp.result.items == []

    # Check alias names in ParamDTO JSON
    assert captured["params"]["method"] == "open.funds.center.wirhdraw.record.list"
    payload = orjson.loads(captured["params"]["param"])  # type: ignore[arg-type]
    assert payload["limit"] == 50
    assert payload["page"] == 2
    assert payload["createTimeStart"] == 1700000000
    assert payload["createTimeEnd"] == 1700003600
    assert payload["accountChannel"] == 1
    assert payload["subMerchantId"] == "sub"


async def test_async_funds_get_daily_bill_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncFundsService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(
            200,
            json={
                "result": {
                    "billDate": "2024-01-31",
                    "billType": "ALL",
                    "total_amount": 0,
                    "details": [],
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    await svc.get_daily_bill(access_token="t", uid=None, bill_date="2024-01-31")

    assert captured["params"]["method"] == "open.funds.center.get.daily.bill"
    payload = orjson.loads(captured["params"]["param"])  # type: ignore[arg-type]
    assert payload["billDate"] == "2024-01-31"


def test_sync_funds_apply_withdraw_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncFundsService(client)

    captured = {}

    def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    def _mock_post(url, data):
        raise AssertionError("Funds.apply_withdraw must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    svc.apply_withdraw(
        access_token="t",
        withdraw_money=999,
        withdraw_no="WD2",
        remark="note",
        account_channel=3,
        sub_merchant_id="sm",
    )

    assert captured["params"]["method"] == "open.funds.center.withdraw.apply"
    payload = orjson.loads(captured["params"]["param"])  # type: ignore[arg-type]
    assert payload["withdrawMoney"] == 999
    assert payload["withdrawNo"] == "WD2"
    assert payload["remark"] == "note"
    assert payload["accountChannel"] == 3
    assert payload["subMerchantId"] == "sm"


def test_funds_request_aliases_and_http_method():
    # Verify model alias mapping and GET method declaration
    req = FundsWithdrawApplyRequest(
        access_token="t",
        withdraw_money=100,
        withdraw_no="W0",
        remark="r",
        account_channel=1,
        sub_merchant_id="s",
    )
    dumped = req.model_dump(by_alias=True)
    assert "withdrawMoney" in dumped
    assert "withdrawNo" in dumped
    assert "accountChannel" in dumped
    assert "subMerchantId" in dumped

    # Also verify another request declares GET
    ainfo = FundsAccountInfoRequest(access_token="t")
    from kwaixiaodian.models.base import HttpMethod  # local import

    assert ainfo.http_method is HttpMethod.GET


def test_funds_model_alias_dump_various_requests():
    # Daily bill
    from kwaixiaodian.models.funds import (
        FundsDailyBillRequest,
        FundsPinganBillRequest,
        FundsPostSalesBillListRequest,
        FundsQueryAccountBillRequest,
    )

    dreq = FundsDailyBillRequest(access_token="t", bill_date="2024-01-01")
    d = dreq.model_dump(by_alias=True)
    assert "billDate" in d

    preq = FundsPostSalesBillListRequest(access_token="t")
    pd = preq.model_dump(by_alias=True)
    assert "startTime" in pd or "endTime" in pd or "cursor" in pd

    qreq = FundsQueryAccountBillRequest(access_token="t")
    _ = qreq.model_dump(by_alias=True)
    # any of the aliased fields should be present when set; ensure keys exist after setting
    qreq2 = FundsQueryAccountBillRequest(
        access_token="t",
        start_time=1,
        end_time=2,
        role_type="seller",
        biz_type=["x"],
        wallet_type="w",
        sub_mch_id="m",
    )
    qd2 = qreq2.model_dump(by_alias=True)
    assert {
        "startTime",
        "endTime",
        "roleType",
        "bizType",
        "walletType",
        "subMchId",
    }.issubset(qd2.keys())

    preq2 = FundsPinganBillRequest(access_token="t", sub_mch_id="sub")
    pd2 = preq2.model_dump(by_alias=True)
    assert "subMchId" in pd2
