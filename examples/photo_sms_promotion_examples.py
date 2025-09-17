"""Runnable snippets for Photo, SMS, and Promotion domains.

Set environment variables:
- KS_APP_KEY, KS_APP_SECRET, KS_SIGN_SECRET, KS_ACCESS_TOKEN
"""

import asyncio
import os

from kwaixiaodian.client.main import AsyncKwaixiaodianClient


async def main() -> None:
    app_key = os.environ.get("KS_APP_KEY", "app_key")
    app_secret = os.environ.get("KS_APP_SECRET", "app_secret")
    sign_secret = os.environ.get("KS_SIGN_SECRET", "sign_secret")
    access_token = os.environ.get("KS_ACCESS_TOKEN", "token")

    async with AsyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # Photo: start upload and publish (tokens are placeholders)
        await client.photo.start_upload(access_token)
        await client.photo.publish(
            access_token, upload_token="UPLOAD_TOKEN_PLACEHOLDER"
        )

        # SMS: view template (templateId=100 for demo)
        await client.sms.view_templates(access_token, template_id=100)

        # Promotion: fetch coupon statistics (couponId=12345 for demo)
        await client.promotion.seller_statistic(access_token)


if __name__ == "__main__":
    asyncio.run(main())
