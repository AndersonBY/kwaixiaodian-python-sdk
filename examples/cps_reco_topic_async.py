"""Minimal async example: CPS promotion recommended topics

Fetches CPS promotion recommended topics via the main distribution service.

Environment variables:
- KS_APP_KEY
- KS_APP_SECRET
- KS_SIGN_SECRET
- KS_ACCESS_TOKEN
- KS_SERVER_URL (optional, defaults to production)
"""

import asyncio
import os
from typing import Optional

from kwaixiaodian.client.main import AsyncKwaixiaodianClient


def _get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)


async def main() -> None:
    app_key = _get_env("KS_APP_KEY")
    app_secret = _get_env("KS_APP_SECRET")
    sign_secret = _get_env("KS_SIGN_SECRET")
    access_token = _get_env("KS_ACCESS_TOKEN")
    server_url = _get_env("KS_SERVER_URL", "https://openapi.kwaixiaodian.com")

    if not all([app_key, app_secret, sign_secret, access_token]):
        print(
            "Missing env vars: KS_APP_KEY/KS_APP_SECRET/KS_SIGN_SECRET/KS_ACCESS_TOKEN"
        )
        return

    async with AsyncKwaixiaodianClient(
        app_key=app_key or "",
        app_secret=app_secret or "",
        sign_secret=sign_secret or "",
        server_url=server_url or "https://openapi.kwaixiaodian.com",
        enable_logging=False,
    ) as client:
        resp = await client.distribution.get_cps_promotion_reco_topic_list(
            access_token=access_token or ""
        )
        print(
            "CPS recommended topics:",
            getattr(resp, "data", None) or getattr(resp, "result", None),
        )


if __name__ == "__main__":
    asyncio.run(main())
