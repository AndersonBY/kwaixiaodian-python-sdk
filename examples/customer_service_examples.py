"""
Minimal Customer Service examples (aligned with Java reference).

This script demonstrates:
- Dispatch Group Add/Query (POST): open.cs.dispatching.group.add/query
- Intelligent Message Send (POST): open.cs.intelligent.message.send

Use environment variables for secrets/tokens:
- KS_APP_KEY, KS_APP_SECRET, KS_SIGN_SECRET
- KS_ACCESS_TOKEN

These examples are safe to run as-is; they print basic `is_success` flags
and do not assume specific data exists in your account.

# Note on logistics callback input mapping (POST):
#   open.cs.logistics.session.create.callback expects aliases
#   assistantId / ksSessionId / sessionId / sessionType
#   Example call:
#   client.customer_service.create_logistics_session_callback(
#       access_token=ACCESS_TOKEN,
#       assistant_id="a1", ks_session_id="ks1",
#       session_id="s1", session_type=2,
#   )
"""

from __future__ import annotations

import asyncio
import os

from kwaixiaodian import AsyncKwaixiaodianClient, SyncKwaixiaodianClient
from kwaixiaodian.models.customer_service import CsUser, MessageContent


def _read_env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)


async def async_examples() -> None:
    app_key = _read_env("KS_APP_KEY", "your_app_key")
    app_secret = _read_env("KS_APP_SECRET", "your_app_secret")
    sign_secret = _read_env("KS_SIGN_SECRET", "your_sign_secret")
    access_token = _read_env("KS_ACCESS_TOKEN", "your_token")

    async with AsyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # 1) Add Dispatch Group (POST) — alias: groupName
        add_resp = await client.customer_service.add_dispatch_group(
            access_token=access_token, group_name="VIP客服组"
        )
        print("add_dispatch_group.is_success =", add_resp.is_success)

        # 2) Query Dispatch Group (POST) — alias: groupId
        if add_resp.data and add_resp.data.group_id is not None:
            group_id = add_resp.data.group_id
        else:
            # Fallback to a sample number if API doesn't return id in your environment
            group_id = 1
        query_resp = await client.customer_service.query_dispatch_group(
            access_token=access_token, group_id=group_id
        )
        print("query_dispatch_group.is_success =", query_resp.is_success)

        # 3) Intelligent Message Send (POST) — nested alias: nickName, contentType
        to_user = CsUser(nick_name="nick", role=1)
        message_list = [MessageContent(content_type=1, content="hello")]
        send_resp = await client.customer_service.send_intelligent_message(
            access_token=access_token, to_user=to_user, message_list=message_list
        )
        print("send_intelligent_message.is_success =", send_resp.is_success)


def sync_examples() -> None:
    app_key = _read_env("KS_APP_KEY", "your_app_key")
    app_secret = _read_env("KS_APP_SECRET", "your_app_secret")
    sign_secret = _read_env("KS_SIGN_SECRET", "your_sign_secret")
    access_token = _read_env("KS_ACCESS_TOKEN", "your_token")

    with SyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # Query Dispatch Group (POST) — example with a sample group id
        resp = client.customer_service.query_dispatch_group(
            access_token=access_token, group_id=1
        )
        print("sync query_dispatch_group.is_success =", resp.is_success)


if __name__ == "__main__":
    asyncio.run(async_examples())
    sync_examples()
