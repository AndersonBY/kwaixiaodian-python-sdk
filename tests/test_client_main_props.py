"""Tests for client.main service properties and context managers"""

import asyncio

from kwaixiaodian import AsyncKwaixiaodianClient, SyncKwaixiaodianClient


def test_async_client_properties_and_close():
    client = AsyncKwaixiaodianClient(app_key="k", app_secret="s", sign_secret="x")

    # Access all service properties to exercise getters
    assert client.order is not None
    assert client.item is not None
    assert client.refund is not None
    assert client.logistics is not None
    assert client.funds is not None
    assert client.industry is not None
    assert client.service_market is not None
    assert client.local_life is not None
    assert client.comment is not None
    assert client.customer_service is not None
    assert client.dropshipping is not None
    assert client.shop is not None
    assert client.user is not None
    assert client.security is not None
    assert client.invoice is not None
    assert client.live is not None
    assert client.distribution is not None
    assert client.supply is not None

    asyncio.run(client.close())


def test_async_client_context_manager():
    async def _run():
        async with AsyncKwaixiaodianClient("k", "s", "x") as client:
            assert client.item is not None
            # Exercise async scm() as method
            assert await asyncio.to_thread(lambda: client.scm()) is not None

    asyncio.run(_run())


def test_sync_client_properties_and_close():
    client = SyncKwaixiaodianClient(app_key="k", app_secret="s", sign_secret="x")

    assert client.order is not None
    assert client.item is not None
    assert client.refund is not None
    assert client.logistics is not None
    assert client.funds is not None
    assert client.industry is not None
    assert client.service_market is not None
    assert client.local_life is not None
    assert client.comment is not None
    assert client.customer_service is not None
    assert client.dropshipping is not None
    assert client.shop is not None
    assert client.user is not None
    assert client.security is not None
    assert client.invoice is not None
    assert client.live is not None
    assert client.distribution is not None
    assert client.supply is not None

    # Exercise scm() methods (not properties)
    assert client.scm() is not None

    client.close()
