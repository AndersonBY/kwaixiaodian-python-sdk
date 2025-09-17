"""
行业特化服务示例（Java对齐）

演示 Industry 域的显式参数便捷方法（异步/同步）。

安全提示：使用环境变量注入敏感信息；示例不会输出敏感令牌。
"""

import asyncio
import os
from typing import Optional

from kwaixiaodian import AsyncKwaixiaodianClient, SyncKwaixiaodianClient

APP_KEY = os.getenv("KUAISHOU_APP_KEY", "your_app_key")
APP_SECRET = os.getenv("KUAISHOU_APP_SECRET", "your_app_secret")
SIGN_SECRET = os.getenv("KUAISHOU_SIGN_SECRET", "your_sign_secret")
ACCESS_TOKEN = os.getenv("KUAISHOU_ACCESS_TOKEN", "your_access_token")


async def async_example(order_id: Optional[int] = None, open_id: Optional[str] = None):
    async with AsyncKwaixiaodianClient(APP_KEY, APP_SECRET, SIGN_SECRET) as client:
        if order_id is not None:
            detail = await client.industry.get_virtual_order_detail(
                access_token=ACCESS_TOKEN, order_id=order_id
            )
            print("virtual detail:", detail.is_success)

            # 审核/解密操作通常需要真实订单和权限，示例保留但不默认执行
            # review = await client.industry.review_virtual_order(
            #     access_token=ACCESS_TOKEN, review_code=1, order_id=order_id
            # )
            # print("virtual review:", review.is_success)

            # decrypt = await client.industry.decrypt_virtual_order(
            #     access_token=ACCESS_TOKEN, order_id=order_id
            # )
            # print("virtual decrypt:", decrypt.is_success)

        if open_id is not None:
            profile = await client.industry.query_secondhand_user_profile(
                access_token=ACCESS_TOKEN, open_id=open_id
            )
            print("secondhand profile:", profile.is_success)


def sync_example(order_id: Optional[int] = None, open_id: Optional[str] = None):
    with SyncKwaixiaodianClient(APP_KEY, APP_SECRET, SIGN_SECRET) as client:
        if order_id is not None:
            detail = client.industry.get_virtual_order_detail(
                access_token=ACCESS_TOKEN, order_id=order_id
            )
            print("virtual detail:", detail.is_success)

            # 同步版审核/解密示例（默认不执行）
            # review = client.industry.review_virtual_order(
            #     access_token=ACCESS_TOKEN, review_code=1, order_id=order_id
            # )
            # print("virtual review:", review.is_success)

            # decrypt = client.industry.decrypt_virtual_order(
            #     access_token=ACCESS_TOKEN, order_id=order_id
            # )
            # print("virtual decrypt:", decrypt.is_success)

        if open_id is not None:
            profile = client.industry.query_secondhand_user_profile(
                access_token=ACCESS_TOKEN, open_id=open_id
            )
            print("secondhand profile:", profile.is_success)


if __name__ == "__main__":
    # 可传入真实 order_id/open_id 验证
    asyncio.run(async_example(order_id=None, open_id=None))
    sync_example(order_id=None, open_id=None)
