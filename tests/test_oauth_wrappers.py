"""Cover client.oauth thin wrappers for both sync and async"""

import asyncio

from kwaixiaodian import AsyncOAuthClient, SyncOAuthClient
from kwaixiaodian.auth.types import TokenResponse


def test_sync_oauth_wrappers(monkeypatch):
    client = SyncOAuthClient("id", "secret")

    tr = TokenResponse(access_token="a", expires_in=3600, refresh_token="r")

    monkeypatch.setattr(client._oauth_manager, "refresh_access_token", lambda rt: tr)
    monkeypatch.setattr(
        client._oauth_manager, "get_client_credentials_token", lambda: tr
    )
    monkeypatch.setattr(client._oauth_manager, "revoke_token", lambda t, tt: True)

    assert client.refresh_access_token("r").access_token == "a"
    assert client.get_client_credentials_token().token_type == "Bearer"
    assert client.revoke_token("a") is True


def test_async_oauth_wrappers(monkeypatch):
    client = AsyncOAuthClient("id", "secret")

    tr = TokenResponse(access_token="a", expires_in=3600, refresh_token="r")

    async def _refresh(rt):
        return tr

    async def _client_token():
        return tr

    async def _revoke(t, tt):
        return True

    monkeypatch.setattr(client._oauth_manager, "refresh_access_token", _refresh)
    monkeypatch.setattr(
        client._oauth_manager, "get_client_credentials_token", _client_token
    )
    monkeypatch.setattr(client._oauth_manager, "revoke_token", _revoke)

    async def _run():
        assert (await client.refresh_access_token("r")).access_token == "a"
        assert (await client.get_client_credentials_token()).token_type == "Bearer"
        assert (await client.revoke_token("a")) is True
        await client.close()

    asyncio.run(_run())
