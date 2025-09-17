"""Async OAuth client light tests"""

import asyncio

from kwaixiaodian import AsyncOAuthClient


def test_async_oauth_get_authorize_url():
    client = AsyncOAuthClient(
        app_key="id", app_secret="secret", server_url="https://srv"
    )
    url = client.get_authorize_url(
        redirect_uri="https://cb", scope=["merchant_order"], state="st"
    )
    assert url.startswith("https://srv/oauth2/authorize?")
    assert "client_id=id" in url
    assert "redirect_uri=https%3A%2F%2Fcb" in url
    asyncio.run(client.close())
