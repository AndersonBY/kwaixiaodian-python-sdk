"""
Minimal Distribution examples (aligned with Java reference).

This script demonstrates:
- Query Plan (GET): open.distribution.plan.query
- Query Plan Commission (GET): open.distribution.plan.commission.query
- Update Kwaimoney PID (POST): open.distribution.cps.kwaimoney.pid.update
- Seller Activity Promotion Effect Summary (GET): open.distribution.seller.activity.promotion.effect.summary

Use environment variables for secrets/tokens and ids:
- KS_APP_KEY, KS_APP_SECRET, KS_SIGN_SECRET
- KS_ACCESS_TOKEN
- KS_ITEM_ID, KS_PLAN_ID, KS_ACTIVITY_ID, KS_CPS_PID, KS_PROMOTION_BIT_NAME
"""

from __future__ import annotations

import asyncio
import os

from kwaixiaodian import AsyncKwaixiaodianClient, SyncKwaixiaodianClient


def _read_env(name: str, default: str | None = None) -> str | None:
    val = os.getenv(name, default)
    return val


async def async_examples() -> None:
    app_key = _read_env("KS_APP_KEY", "your_app_key")
    app_secret = _read_env("KS_APP_SECRET", "your_app_secret")
    sign_secret = _read_env("KS_SIGN_SECRET", "your_sign_secret")
    access_token = _read_env("KS_ACCESS_TOKEN", "your_token")

    item_id_str = _read_env("KS_ITEM_ID")
    plan_id_str = _read_env("KS_PLAN_ID")
    activity_id_str = _read_env("KS_ACTIVITY_ID")
    cps_pid = _read_env("KS_CPS_PID", "pid_xxx")
    promotion_bit_name = _read_env("KS_PROMOTION_BIT_NAME", "my_slot")

    item_id = int(item_id_str) if item_id_str else None
    plan_id = int(plan_id_str) if plan_id_str else None
    activity_id = int(activity_id_str) if activity_id_str else None

    async with AsyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # Query Plan (GET) — alias: itemId
        plan_resp = await client.distribution.query_plan(
            access_token=access_token, item_id=item_id
        )
        print("query_plan.is_success =", plan_resp.is_success)

        # Query Plan Commission (GET) — alias: planId, pcursor
        if plan_id is not None:
            commission_resp = await client.distribution.query_plan_commission(
                access_token=access_token, plan_id=plan_id, pcursor=None
            )
            print("query_plan_commission.is_success =", commission_resp.is_success)

        # Update Kwaimoney PID (POST) — alias: cpsPid, promotionBitName
        pid_update_resp = await client.distribution.update_cps_kwaimoney_pid(
            access_token=access_token,
            cps_pid=cps_pid or "pid_demo",
            promotion_bit_name=promotion_bit_name or "demo_slot",
        )
        print("update_cps_kwaimoney_pid.is_success =", pid_update_resp.is_success)

        # Seller Activity Promotion Effect Summary (GET) — alias: activityId, endTime
        if activity_id is not None:
            effect_summary_resp = (
                await client.distribution.get_seller_activity_promotion_effect_summary(
                    access_token=access_token, activity_id=activity_id, end_time=None
                )
            )
            print(
                "seller_activity_promotion_effect_summary.is_success =",
                effect_summary_resp.is_success,
            )


def sync_examples() -> None:
    app_key = _read_env("KS_APP_KEY", "your_app_key")
    app_secret = _read_env("KS_APP_SECRET", "your_app_secret")
    sign_secret = _read_env("KS_SIGN_SECRET", "your_sign_secret")
    access_token = _read_env("KS_ACCESS_TOKEN", "your_token")
    activity_id_str = _read_env("KS_ACTIVITY_ID")
    activity_id = int(activity_id_str) if activity_id_str else None

    with SyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        if activity_id is not None:
            resp = client.distribution.get_seller_activity_promotion_effect_summary(
                access_token=access_token, activity_id=activity_id, end_time=None
            )
            print("sync effect summary is_success =", resp.is_success)


if __name__ == "__main__":
    # Run async examples; then a small sync example
    asyncio.run(async_examples())
    sync_examples()
