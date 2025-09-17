"""Invoice service tests aligned with Java SDK reference.

Covers:
- GET method usage for invoice endpoints
- Alias mapping in ParamDTO JSON (fromType, toType, toId, orderId)
- Error path raises KwaixiaodianAPIError
"""

from __future__ import annotations

import httpx
import orjson
import pytest

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient, SyncBaseClient
from kwaixiaodian.client.services.invoice import AsyncInvoiceService, SyncInvoiceService
from kwaixiaodian.exceptions import KwaixiaodianAPIError


@pytest.mark.unit
async def test_async_invoice_amount_get_uses_get_and_aliases(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncInvoiceService(client)

    captured = {}

    async def _mock_get(url, params):
        captured.update({"url": url, "params": params})
        return httpx.Response(200, json={"result": {}})

    async def _mock_post(url, data):
        raise AssertionError("Invoice.amount_get must use GET, not POST")

    monkeypatch.setattr(client.http_client, "get", _mock_get)
    monkeypatch.setattr(client.http_client, "post", _mock_post)

    await svc.amount_get(
        access_token="t",
        from_type="ORDER",
        to_type="BUYER",
        to_id=1001,
        order_id=2002,
        uid=None,
    )

    # Ensure signed GET params include correct method and alias-mapped ParamDTO JSON
    assert captured["params"]["method"] == "open.invoice.amount.get"
    param_json = captured["params"].get("param")
    assert isinstance(param_json, str)
    payload = orjson.loads(param_json)
    assert payload["fromType"] == "ORDER"
    assert payload["toType"] == "BUYER"
    assert payload["toId"] == 1001
    assert payload["orderId"] == 2002


@pytest.mark.unit
async def test_async_invoice_subsidy_audit_info_response_parsing(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncInvoiceService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "oid": "O123",
                    "amount": "10.00",
                    "subSidyAmount": "2.00",
                    "userPayAmount": "8.00",
                    "city": "SZ",
                    "barCode": "B1",
                    "channelSeqNo": "CSEQ",
                    "openInvoiceSubjectProto": {"t": 1},
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.subsidy_audit_info(access_token="t", oid="O123", uid=None)

    assert resp.is_success
    assert resp.result is not None
    assert resp.result.oid == "O123"


@pytest.mark.unit
def test_sync_invoice_amount_get_error_path_raises(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = SyncBaseClient(cfg)
    svc = SyncInvoiceService(client)

    def _mock_get(url, params):
        # Simulate API error payload
        return httpx.Response(200, json={"error_code": "E", "error_msg": "bad"})

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    with pytest.raises(KwaixiaodianAPIError):
        svc.amount_get(
            access_token="t",
            from_type="ORDER",
            to_type="BUYER",
            to_id=1,
            order_id=2,
            uid=None,
        )
