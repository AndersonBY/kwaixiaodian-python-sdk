"""
Second-Distribution apply + list examples.

This script demonstrates how to:
- Apply for a second-level distribution investment activity (GET)
  - open.distribution.second.action.apply.investment.activity (standard)
- List applied second-level investment activities (GET)
  - open.distribution.second.apply.investment.activity.list

Notes
- Use environment variables; calls require valid credentials.
- For exact semantics, see Java SDK requests in java_sdk_reference and docs.

Env vars
- KS_APP_KEY, KS_APP_SECRET, KS_SIGN_SECRET
- KS_ACCESS_TOKEN

Run
  python examples/second_distribution_apply_and_list.py
"""

from __future__ import annotations

import asyncio
import os

from kwaixiaodian import AsyncKwaixiaodianClient


def _env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)


async def main() -> None:
    app_key = _env("KS_APP_KEY", "your_app_key")
    app_secret = _env("KS_APP_SECRET", "your_app_secret")
    sign_secret = _env("KS_SIGN_SECRET", "your_sign_secret")
    access_token = _env("KS_ACCESS_TOKEN", "your_token")

    async with AsyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # 1) Apply for a second-level investment activity (standard)
        apply_resp = (
            await client.distribution.second.apply_second_investment_activity_standard(
                access_token=access_token
            )
        )
        print("second.apply.investment.activity.is_success =", apply_resp.is_success)
        print("second.apply.investment.activity.raw =", apply_resp.raw)

        # 2) List my applied second-level investment activities
        list_resp = (
            await client.distribution.second.get_second_apply_investment_activity_list(
                access_token=access_token
            )
        )
        print(
            "second.apply.investment.activity.list.is_success =", list_resp.is_success
        )
        print("second.apply.investment.activity.list.raw =", list_resp.raw)


if __name__ == "__main__":
    asyncio.run(main())
