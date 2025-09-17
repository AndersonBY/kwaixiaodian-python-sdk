"""示例：类型化订单视图与金额助手使用

运行方式：

    pdm run python examples/order_money_helpers.py

注意：示例仅演示序列化与调用方式，请在真实环境中提供有效的 access_token。
"""

import asyncio
import os

from kwaixiaodian import KwaixiaodianClient


async def main() -> None:
    access_token = os.getenv("KS_ACCESS_TOKEN", "test_token")

    async with KwaixiaodianClient(
        app_key=os.getenv("KS_APP_KEY", "app_key"),
        app_secret=os.getenv("KS_APP_SECRET", "app_secret"),
        sign_secret=os.getenv("KS_SIGN_SECRET", "sign_secret"),
    ) as client:
        # 仅作演示：在真实环境下使用有效的时间范围
        resp = await client.order.seller_pcursor_list(
            access_token=access_token,
            begin_time="2024-01-01 00:00:00",
            end_time="2024-01-02 00:00:00",
            page_size=10,
        )

        if resp.result and resp.result.order_info_list:
            for info in resp.result.order_info_list:
                print("订单ID:", info.oid, "总金额(元):", info.total_fee_yuan)
                for p in info.order_product_info_list or []:
                    print("  ", p.item_title, "单价(元):", p.price_yuan)


if __name__ == "__main__":
    asyncio.run(main())
