#!/usr/bin/env python3
"""
快手SDK同步客户端使用示例

本示例演示如何使用快手SDK的同步版本进行API调用，
包括订单管理、商品管理和OAuth认证等功能。
"""

import os
import sys
from datetime import datetime, timedelta

# 添加父目录到Python路径，以便导入SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from kwaixiaodian import SyncKwaixiaodianClient, SyncOAuthClient
from kwaixiaodian.exceptions import KwaixiaodianAPIError, KwaixiaodianAuthError
from kwaixiaodian.models.common import ItemStatus, OrderStatus


def oauth_example():
    """OAuth认证流程示例"""
    print("=== OAuth认证流程示例 ===")

    # 初始化OAuth客户端
    oauth_client = SyncOAuthClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        server_url="https://openapi.kwaixiaodian.com",
    )

    try:
        # 1. 获取授权URL
        auth_url = oauth_client.get_authorize_url(
            redirect_uri="https://your-app.com/callback",
            scope=["merchant_order", "merchant_item", "merchant_refund"],
            state="random_state_string_123",
        )
        print(f"授权URL: {auth_url}")
        print("请用户访问此URL进行授权...")

        # 2. 模拟用户授权后获得授权码（实际应用中从回调URL获取）
        authorization_code = "mock_authorization_code"

        # 3. 使用授权码获取访问令牌
        try:
            token_response = oauth_client.get_access_token(authorization_code)
            print(f"访问令牌: {token_response.access_token}")
            print(f"刷新令牌: {token_response.refresh_token}")
            print(f"过期时间: {token_response.expires_in}秒")

            return token_response.access_token

        except KwaixiaodianAuthError as e:
            print(f"获取令牌失败: {e}")
            return None

    finally:
        oauth_client.close()


def order_management_example(access_token: str):
    """订单管理示例"""
    print("=== 订单管理示例 ===")

    # 使用上下文管理器确保资源正确释放
    with SyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret",
        enable_logging=True,  # 启用调试日志
    ) as client:
        try:
            # 1. 获取订单列表
            print("1. 获取最近30天的订单...")
            end_time = datetime.now()
            begin_time = end_time - timedelta(days=30)

            orders_response = client.order.list(
                access_token=access_token,
                seller_id=123456,  # 替换为实际的商家ID
                begin_time=begin_time.strftime("%Y-%m-%d %H:%M:%S"),
                end_time=end_time.strftime("%Y-%m-%d %H:%M:%S"),
                order_status=OrderStatus.WAIT_DELIVER,  # 只获取待发货订单
                page_size=50,
            )

            if orders_response.result:
                print(f"获取到 {len(orders_response.result)} 个待发货订单")

                # 2. 处理每个订单
                for order in orders_response.result[:3]:  # 只处理前3个订单作为示例
                    print(f"\n处理订单: {order.order_id}")

                    # 获取订单详情
                    order_detail = client.order.get(
                        access_token=access_token, order_id=order.order_id
                    )

                    if order_detail.result:
                        print(f"  订单金额: {order_detail.result.total_yuan}元")
                        if order_detail.result.address:
                            print(f"  收货人: {order_detail.result.address.receiver}")
                            print(f"  收货地址: {order_detail.result.address.detail}")

                # 更新商家备注
                client.order.update_remark(
                    access_token=access_token,
                    order_id=order.order_id,
                    note=f"已确认订单，准备发货 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                )
                print("  已更新订单备注")

                # 模拟发货（实际应用中需要真实的物流信息）
                if False:  # 设置为True来执行发货操作
                    ship_response = client.order.ship(
                        access_token=access_token,
                        order_id=order.order_id,
                        express_code=1,  # 快递公司代码
                        express_no="SF1234567890",
                    )
                    if ship_response.is_success:
                        print("  订单发货成功")

        except KwaixiaodianAPIError as e:
            print(f"订单操作失败: {e}")
            if e.error_code:
                print(f"错误代码: {e.error_code}")
            if e.sub_code:
                print(f"子错误代码: {e.sub_code}")


def item_management_example(access_token: str):
    """商品管理示例"""
    print("=== 商品管理示例 ===")

    with SyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret",
    ) as client:
        try:
            # 1. 获取在售商品列表
            print("1. 获取在售商品列表...")
            items_response = client.item.list(
                access_token=access_token,
                item_status=ItemStatus.ON_SALE,
                page_size=20,
            )

            if items_response.result:
                print(f"获取到 {len(items_response.result)} 个在售商品")

                # 2. 查看前几个商品的详情
                for item in items_response.result[:3]:
                    print(f"\n商品: {item.title}")

                    # 获取商品详情
                    item_detail = client.item.get(
                        access_token=access_token, item_id=item.item_id
                    )

                    if item_detail.result:
                        print(f"  ID: {item_detail.result.item_id}")
                        print(f"  价格: {item_detail.result.price_yuan}元")
                        print(f"  原价: {item_detail.result.original_price_yuan}元")
                        print(f"  库存: {item_detail.result.stock}")
                        print(f"  状态: {item_detail.result.status}")

                        # 如果库存较低，补充库存
                        # 示例：更新SKU库存需要提供具体的 sku_id
                        # if item_detail.result.stock < 10 and item_detail.result.skus:
                        #     print("  库存较低，补充库存...")
                        #     client.item.update_stock(
                        #         access_token=access_token,
                        #         item_id=item.item_id,
                        #         sku_id=item_detail.result.skus[0].sku_id,
                        #         stock=50,
                        #     )
                        #     print("  已补充SKU库存到50个")

            # 3. 新建商品示例（注释掉，避免实际创建）
            if False:  # 设置为True来创建新商品
                print("\n3. 新建商品...")
                from kwaixiaodian.models.item import OpenApiAddSkuDTO

                new_item = client.item.new(
                    access_token=access_token,
                    title="测试商品 - Python SDK",
                    category_id=12345,  # 替换为实际的类目ID
                    image_urls=["https://example.com/main.jpg"],
                    sku_list=[
                        OpenApiAddSkuDTO(
                            rel_sku_id=1, sku_stock=100, sku_sale_price=9999
                        )
                    ],
                )

                if new_item.is_success:
                    print("商品新建成功")

        except KwaixiaodianAPIError as e:
            print(f"商品操作失败: {e}")


def logistics_template_example(access_token: str):
    """物流模板管理示例（同步）"""
    print("=== 物流模板管理示例（同步） ===")

    with SyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret",
        enable_logging=True,
    ) as client:
        try:
            # 创建快递模板
            create_resp = client.logistics.template_create(
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
            client.logistics.template_list(access_token)
            print("模板列表查询完成")

            # 更新快递模板（示例ID，替换为真实模板ID）
            template_id = 123
            update_resp = client.logistics.template_update(
                access_token=access_token,
                template_id=template_id,
                name="更新后的模板名称",
            )
            if update_resp.is_success:
                print("更新快递模板成功")

        except KwaixiaodianAPIError as e:
            print(f"物流模板操作失败: {e}")


def error_handling_example():
    """错误处理示例"""
    print("=== 错误处理示例 ===")

    with SyncKwaixiaodianClient(
        app_key="invalid_key", app_secret="invalid_secret", sign_secret="invalid_sign"
    ) as client:
        try:
            # 使用无效的令牌调用API
            client.order.list(
                access_token="invalid_token",
                seller_id=123456,
                begin_time="2024-01-01 00:00:00",
                end_time="2024-01-31 23:59:59",
            )

        except KwaixiaodianAPIError as e:
            print("捕获到API错误:")
            print(f"  错误消息: {e.message}")
            print(f"  错误代码: {e.error_code}")
            print(f"  子错误代码: {e.sub_code}")
            print(f"  请求ID: {e.request_id}")

        except Exception as e:
            print(f"捕获到其他异常: {e}")


def performance_comparison():
    """性能对比示例（同步 vs 异步）"""
    print("=== 性能对比示例 ===")

    import time

    # 同步调用示例
    print("同步调用性能测试...")
    start_time = time.time()

    with SyncKwaixiaodianClient(
        app_key="test_key", app_secret="test_secret", sign_secret="test_sign"
    ) as sync_client:
        # 模拟多个API调用
        for _ in range(5):
            try:
                # 注意：这里会因为无效参数而失败，但可以测试调用开销
                sync_client.order.list(
                    access_token="test_token",
                    seller_id=123456,
                    begin_time="2024-01-01 00:00:00",
                    end_time="2024-01-31 23:59:59",
                )
            except Exception:
                pass  # 忽略错误，只测试调用开销

    sync_time = time.time() - start_time
    print(f"同步调用耗时: {sync_time:.3f}秒")

    print("\n注意：异步版本在并发场景下性能更优")
    print("同步版本适合简单的顺序操作和脚本场景")


def main():
    """主函数"""
    print("快手SDK同步客户端使用示例")
    print("=" * 50)

    # 注意：请替换为实际的应用凭证
    print("请先在快手开放平台申请应用凭证，并替换示例中的占位符\n")

    # 1. OAuth认证示例
    access_token = oauth_example()

    if not access_token:
        print("未获取到有效的访问令牌，使用模拟令牌继续演示...")
        access_token = "mock_access_token"

    print("\n" + "=" * 50)

    # 2. 订单管理示例
    order_management_example(access_token)

    print("\n" + "=" * 50)

    # 3. 商品管理示例
    item_management_example(access_token)

    print("\n" + "=" * 50)

    # 4. 错误处理示例
    error_handling_example()

    print("\n" + "=" * 50)

    # 5. 性能对比示例
    performance_comparison()

    print("\n示例执行完成!")
    print("\n使用建议:")
    print("- 生产环境中请妥善保管应用凭证")
    print("- 建议使用上下文管理器确保资源正确释放")
    print("- 对于高并发场景，推荐使用异步版本客户端")
    print("- 同步版本适合脚本和简单的顺序操作场景")


if __name__ == "__main__":
    main()
