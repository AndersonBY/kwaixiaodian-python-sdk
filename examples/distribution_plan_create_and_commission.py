"""
Distribution plan create + commission query examples.

This script demonstrates how to:
- Create a distribution plan (POST): open.distribution.plan.create
- Query plan commission (GET): open.distribution.plan.commission.query

Notes
- Use environment variables for credentials/tokens/ids.
- Parameter structures for plan creation vary by business type; fill according
  to Kuaishou OpenAPI docs and Java SDK request models.
- Network calls require valid credentials. This example is safe to run but
  will only succeed with proper access_token and configured params.

Env vars
- KS_APP_KEY, KS_APP_SECRET, KS_SIGN_SECRET
- KS_ACCESS_TOKEN
- KS_PLAN_CREATE_TYPE (e.g., "NORMAL" or business-specific)
- KS_PLAN_ID (optional, for commission query)

Run
  python examples/distribution_plan_create_and_commission.py
"""

from __future__ import annotations

import asyncio
import os
from typing import Any

from kwaixiaodian import AsyncKwaixiaodianClient


def _env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)


async def main() -> None:
    app_key = _env("KS_APP_KEY", "your_app_key")
    app_secret = _env("KS_APP_SECRET", "your_app_secret")
    sign_secret = _env("KS_SIGN_SECRET", "your_sign_secret")
    access_token = _env("KS_ACCESS_TOKEN", "your_token")

    plan_create_type = _env("KS_PLAN_CREATE_TYPE", "NORMAL")
    plan_id_str = _env("KS_PLAN_ID")
    plan_id = int(plan_id_str) if plan_id_str else None

    # Example param stubs. Replace with real fields per OpenAPI/Java docs.
    # See: java_sdk_reference/.../distribution/OpenDistributionPlanCreateRequest.java
    normal_plan_param: dict[str, Any] = {
        # "itemId": 123456,  # 商品ID
        # "commissionRate": 10,  # 佣金比（举例）
    }

    async with AsyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # 1) Create distribution plan (POST)
        create_resp = await client.distribution.create_distribute_plan(
            access_token=access_token,
            plan_create_type=plan_create_type,
            normal_plan_param=normal_plan_param or None,
            exclusive_plan_param=None,
            orientation_plan_param=None,
        )
        print("plan.create.is_success =", create_resp.is_success)
        print("plan.create.raw =", create_resp.raw)

        # 2) Query plan commission (GET) if plan_id is provided
        if plan_id is not None:
            commission_resp = await client.distribution.query_plan_commission(
                access_token=access_token,
                plan_id=plan_id,
                pcursor=None,
            )
            print("plan.commission.query.is_success =", commission_resp.is_success)
            print("plan.commission.query.raw =", commission_resp.raw)


if __name__ == "__main__":
    asyncio.run(main())
