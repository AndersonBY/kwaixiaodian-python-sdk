"""Minimal async example: Distribution public category list

Reads credentials and access token from environment variables and fetches
the distribution public category list. This example does not mask or print
secrets and will only run with valid credentials.

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
    value = os.getenv(name, default)
    return value


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
        resp = await client.distribution.get_distribution_public_category_list(
            access_token=access_token or ""
        )
        # Print a concise summary without leaking secrets
        print(
            "Public categories fetched:",
            getattr(resp, "data", None) or getattr(resp, "result", None),
        )


if __name__ == "__main__":
    asyncio.run(main())
