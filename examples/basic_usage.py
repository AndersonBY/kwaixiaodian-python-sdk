"""
快手小店SDK基础使用示例

演示如何使用快手小店Python SDK进行基本的API操作。
"""

import asyncio
import logging

from kwaixiaodian import AsyncKwaixiaodianClient, AsyncOAuthClient
from kwaixiaodian.models.common import ItemStatus, OrderStatus

# 启用调试日志
logging.basicConfig(level=logging.INFO)


async def oauth_example():
    """OAuth认证示例"""
    print("=== OAuth认证示例 ===")

    # 创建OAuth客户端
    oauth_client = AsyncOAuthClient(
        app_key="your_app_key", app_secret="your_app_secret"
    )

    # 1. 获取授权URL
    auth_url = oauth_client.get_authorize_url(
        redirect_uri="https://your-app.com/callback",
        scope=["merchant_order", "merchant_item", "merchant_refund"],
        state="random_state_string",
    )

    print(f"授权链接: {auth_url}")
    print("请复制链接到浏览器中完成授权，获取authorization_code")

    # 模拟获取到的授权码
    # authorization_code = "your_authorization_code_from_callback"

    # 2. 使用授权码获取访问令牌
    # async with oauth_client:
    #     token_response = await oauth_client.get_access_token(authorization_code)
    #
    #     print(f"访问令牌: {token_response.access_token}")
    #     print(f"刷新令牌: {token_response.refresh_token}")
    #     print(f"过期时间: {token_response.expires_in}秒")
    #     print(f"授权范围: {token_response.scopes}")
    #
    #     # 3. 刷新访问令牌
    #     if token_response.refresh_token:
    #         new_token = await oauth_client.refresh_access_token(
    #             token_response.refresh_token
    #         )
    #         print(f"新访问令牌: {new_token.access_token}")


async def order_management_example():
    """订单管理示例"""
    print("\n=== 订单管理示例 ===")

    # 创建SDK客户端
    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret",
        enable_logging=True,
    ) as client:
        access_token = "your_access_token"
        seller_id = 123456  # 你的商家ID

        try:
            # 1. 获取订单列表
            print("1. 获取待发货订单...")
            orders_response = await client.order.list(
                access_token=access_token,
                seller_id=seller_id,
                begin_time="2024-01-01 00:00:00",
                end_time="2024-01-31 23:59:59",
                order_status=OrderStatus.WAIT_DELIVER,  # 待发货状态
                page_size=50,
            )

            if orders_response.is_success:
                orders = orders_response.result
                if orders:
                    print(f"找到 {len(orders)} 个待发货订单")

                    for order in orders[:5]:  # 显示前5个订单
                        print(f"  订单ID: {order.order_id}")
                        print(f"  订单金额: {order.total_yuan}元")
                        print(f"  创建时间: {order.create_time}")
                        print(f"  商品数量: {len(order.items) if order.items else 0}")
                        print("  ---")

            # 2. 获取订单详情
            if orders_response.is_success and orders_response.result:
                first_order = orders_response.result[0]
                print(f"\n2. 获取订单详情: {first_order.order_id}")

                order_detail = await client.order.get(
                    access_token=access_token, order_id=first_order.order_id
                )

                if order_detail.is_success:
                    order = order_detail.result
                    if order:
                        print(
                            f"  买家信息: {order.buyer_info.nickname if order.buyer_info else 'N/A'}"
                        )
                        print(
                            f"  收货地址: {order.address.detail if order.address else 'N/A'}"
                        )
                        print("  商品列表:")
                        if order.items:
                            for item in order.items:
                                print(
                                    f"    - {item.title}: {item.quantity}件 x {item.unit_yuan}元"
                                )

            # 3. 模拟订单发货
            print("\n3. 模拟订单发货...")
            # ship_result = await client.order.ship(
            #     access_token=access_token,
            #     order_id=20240101001,
            #     express_code=1,
            #     express_no="SF123456789"
            # )
            #
            # if ship_result.is_success:
            #     print("发货成功!")
            # else:
            #     print(f"发货失败: {ship_result.error_message}")
            print("发货功能已注释（需要真实订单ID）")

            # 4. 更新订单备注
            print("\n4. 模拟更新订单备注...")
            # remark_result = await client.order.update_remark(
            #     access_token=access_token,
            #     order_id=20240101001,
            #     note="客户要求尽快发货，已安排优先处理"
            # )
            #
            # if remark_result.is_success:
            #     print("备注更新成功!")
            print("备注更新功能已注释（需要真实订单ID）")

        except Exception as e:
            print(f"订单管理操作失败: {e}")


async def item_management_example():
    """商品管理示例"""
    print("\n=== 商品管理示例 ===")

    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret",
        enable_logging=True,
    ) as client:
        access_token = "your_access_token"

        try:
            # 1. 获取商品列表
            print("1. 获取在售商品列表...")
            items_response = await client.item.list(
                access_token=access_token,
                item_status=ItemStatus.ON_SALE,  # 在售商品
                page_size=20,
            )

            if items_response.is_success:
                items = items_response.result
                if items:
                    print(f"找到 {len(items)} 个在售商品")

                    for item in items[:5]:  # 显示前5个商品
                        print(f"  商品ID: {item.item_id}")
                        print(f"  标题: {item.title}")
                        print(f"  价格: {item.price_yuan}元")
                        print(f"  库存: {item.stock}")
                        print("  ---")

            # 2. 获取商品详情
            if items_response.is_success and items_response.result:
                first_item = items_response.result[0]
                print(f"\n2. 获取商品详情: {first_item.item_id}")

                item_detail = await client.item.get(
                    access_token=access_token, item_id=first_item.item_id
                )

                if item_detail.is_success:
                    item = item_detail.result
                    if item:
                        print(f"  商品标题: {item.title}")
                        print(
                            f"  商品描述: {item.description[:100] if item.description else 'N/A'}..."
                        )
                        print(f"  图片数量: {len(item.images) if item.images else 0}")
                        print(f"  SKU数量: {len(item.skus) if item.skus else 0}")
                        if item.skus:
                            print("  SKU信息:")
                            for sku in item.skus[:3]:  # 显示前3个SKU
                                print(
                                    f"    - SKU ID: {sku.sku_id}, 价格: {sku.price_yuan}元, 库存: {sku.stock}"
                                )

            # 3. 模拟新建商品
            print("\n3. 模拟新建商品...")
            # from kwaixiaodian.models.item import OpenApiAddSkuDTO
            # new_item_response = await client.item.new(
            #     access_token=access_token,
            #     title="iPhone 15 Pro 256GB 深空黑",
            #     category_id=12345,  # 需要真实类目ID
            #     image_urls=["https://example.com/main.jpg"],
            #     sku_list=[OpenApiAddSkuDTO(rel_sku_id=1, sku_stock=50, sku_sale_price=899900)],
            # )
            # if new_item_response.is_success:
            #     print("商品新建成功")
            print("商品新建功能已注释（需要真实类目ID和图片URL）")

            # 4. 模拟更新库存
            print("\n4. 模拟更新商品库存...")
            # if items_response.is_success and items_response.result:
            #     item_to_update = items_response.result[0]
            #     stock_result = await client.item.update_stock(
            #         access_token=access_token,
            #         item_id=item_to_update.item_id,
            #         sku_id=item_to_update.skus[0].sku_id,
            #         stock=200  # 更新SKU库存为200
            #     )
            #
            #     if stock_result.is_success:
            #         print(f"库存更新成功! 商品ID: {item_to_update.item_id}")
            #     else:
            #         print(f"库存更新失败: {stock_result.error_message}")
            print("库存更新功能已注释（需要真实商品ID）")

        except Exception as e:
            print(f"商品管理操作失败: {e}")


async def logistics_template_example():
    """物流模板管理示例（异步）"""
    print("\n=== 物流模板管理示例（异步） ===")

    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret",
        enable_logging=True,
    ) as client:
        access_token = "your_access_token"

        try:
            # 创建快递模板（演示参数，按实际需求填写）
            create_resp = await client.logistics.template_create(
                access_token=access_token,
                send_province_name="北京",
                send_district_code=110101,
                send_time=1,
                send_city_name="北京市",
                cal_type=1,
                name="默认模板",
                source_type=1,
                send_province_code=11,
                send_city_code=1101,
                config="{}",
                send_district_name="东城区",
            )
            if create_resp.is_success:
                print("创建快递模板成功")

            # 列表查询
            await client.logistics.template_list(access_token)
            print("模板列表查询完成")

            # 更新快递模板（示例ID，替换为真实模板ID）
            template_id = 123
            update_resp = await client.logistics.template_update(
                access_token=access_token,
                template_id=template_id,
                name="更新后的模板名称",
            )
            if update_resp.is_success:
                print("更新快递模板成功")

        except Exception as e:
            print(f"物流模板操作失败: {e}")


async def error_handling_example():
    """错误处理示例"""
    print("\n=== 错误处理示例 ===")

    async with AsyncKwaixiaodianClient(
        app_key="invalid_app_key",
        app_secret="invalid_app_secret",
        sign_secret="invalid_sign_secret",
    ) as client:
        try:
            # 使用无效的token尝试调用API
            orders_response = await client.order.list(
                access_token="invalid_token",
                seller_id=123456,
                begin_time="2024-01-01 00:00:00",
                end_time="2024-01-31 23:59:59",
            )

            if not orders_response.is_success:
                print("API调用失败:")
                print(f"  错误码: {orders_response.error_code}")
                print(f"  错误信息: {orders_response.error_msg}")
                if orders_response.sub_code:
                    print(f"  子错误码: {orders_response.sub_code}")
                if orders_response.request_id:
                    print(f"  请求ID: {orders_response.request_id}")

        except Exception as e:
            print(f"异常捕获: {type(e).__name__}: {e}")


async def main():
    """主函数"""
    print("快手小店Python SDK使用示例")
    print("=" * 50)

    # OAuth认证示例
    await oauth_example()

    # 注意：以下示例需要真实的访问令牌才能正常运行
    # 在实际使用中，请替换为你的真实凭证

    # 订单管理示例
    # await order_management_example()

    # 商品管理示例
    # await item_management_example()

    # 错误处理示例
    await error_handling_example()

    print("\n示例执行完成!")
    print("注意: 大部分功能示例已注释，需要真实的API凭证才能运行。")


if __name__ == "__main__":
    asyncio.run(main())
