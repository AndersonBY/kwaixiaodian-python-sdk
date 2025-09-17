"""
本地生活服务示例（Java对齐）

演示 Local Life 域的显式参数便捷方法（异步/同步）。

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


async def async_example(order_id: Optional[str] = None):
    async with AsyncKwaixiaodianClient(APP_KEY, APP_SECRET, SIGN_SECRET) as client:
        # 订单详情（显式参数，uid 可选，置于最后）
        if order_id:
            detail = await client.local_life.get_order_detail(
                access_token=ACCESS_TOKEN, order_id=order_id
            )
            print("detail.is_success:", detail.is_success)

        # 订单分页（显式参数）
        page = await client.local_life.get_order_page(
            access_token=ACCESS_TOKEN,
            item_id_list=None,  # type: Optional[List[int]]
            create_time_start=None,
            create_time_end=None,
            page_num=1,
            page_size=20,
        )
        print("page.is_success:", page.is_success)


def sync_example(order_id: Optional[str] = None):
    with SyncKwaixiaodianClient(APP_KEY, APP_SECRET, SIGN_SECRET) as client:
        if order_id:
            detail = client.local_life.get_order_detail(
                access_token=ACCESS_TOKEN, order_id=order_id
            )
            print("detail.is_success:", detail.is_success)

        page = client.local_life.get_order_page(
            access_token=ACCESS_TOKEN, page_num=1, page_size=20
        )
        print("page.is_success:", page.is_success)


if __name__ == "__main__":
    # 可传入一个真实的 order_id 验证详情查询
    asyncio.run(async_example(order_id=None))
    sync_example(order_id=None)
