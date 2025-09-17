# 示例代码

本页面提供了快手小店Python SDK的丰富使用示例，涵盖各种常见业务场景。

## 基础使用示例

### 异步客户端基础用法

```python
import asyncio
from kwaixiaodian import AsyncKwaixiaodianClient

async def basic_example():
    """基础异步客户端使用示例"""
    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret"
    ) as client:

        # 获取订单列表
        orders = await client.order.list(
            access_token="your_access_token",
            seller_id=123456,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59",
            page=1,
            size=20
        )

        print(f"获取到 {len(orders.result)} 个订单")
        for order in orders.result:
            print(f"订单ID: {order.order_id}, 状态: {order.order_status}")

if __name__ == "__main__":
    asyncio.run(basic_example())
```

### 同步客户端基础用法

```python
from kwaixiaodian import SyncKwaixiaodianClient

def sync_basic_example():
    """同步客户端使用示例"""
    with SyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret"
    ) as client:

        # 获取商品列表
        items = client.item.list(
            access_token="your_access_token",
            seller_id=123456,
            page=1,
            size=50
        )

        print(f"获取到 {len(items.result)} 个商品")
        for item in items.result:
            print(f"商品ID: {item.product_id}, 标题: {item.title}")

sync_basic_example()
```

## OAuth认证示例

### 完整OAuth流程

```python
import asyncio
from kwaixiaodian import AsyncOAuthClient

async def oauth_flow_example():
    """完整OAuth认证流程示例"""

    oauth_client = AsyncOAuthClient(
        app_key="your_app_key",
        app_secret="your_app_secret"
    )

    # 1. 获取授权URL
    auth_url = oauth_client.get_authorize_url(
        redirect_uri="https://your-app.com/callback",
        scope=["merchant_order", "merchant_item", "merchant_refund"],
        state="random_state_string"
    )

    print(f"请访问授权URL: {auth_url}")
    print("授权后获取code参数...")

    # 2. 模拟获取authorization_code
    authorization_code = input("请输入授权码: ")

    # 3. 获取访问令牌
    token_response = await oauth_client.get_access_token(
        code=authorization_code,
        redirect_uri="https://your-app.com/callback"
    )

    print(f"访问令牌: {token_response.access_token}")
    print(f"刷新令牌: {token_response.refresh_token}")
    print(f"过期时间: {token_response.expires_in}秒")

    # 4. 使用访问令牌调用API
    from kwaixiaodian import AsyncKwaixiaodianClient

    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret"
    ) as client:

        orders = await client.order.list(
            access_token=token_response.access_token,
            seller_id=123456,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )

        print(f"使用新令牌获取到 {len(orders.result)} 个订单")

asyncio.run(oauth_flow_example())
```

### 令牌刷新示例

```python
async def token_refresh_example():
    """令牌刷新示例"""

    oauth_client = AsyncOAuthClient(
        app_key="your_app_key",
        app_secret="your_app_secret"
    )

    # 使用刷新令牌获取新的访问令牌
    refresh_token = "your_refresh_token"

    try:
        new_token_response = await oauth_client.refresh_access_token(
            refresh_token=refresh_token
        )

        print(f"新访问令牌: {new_token_response.access_token}")
        print(f"新刷新令牌: {new_token_response.refresh_token}")

        # 保存新令牌以供后续使用
        save_tokens(
            new_token_response.access_token,
            new_token_response.refresh_token
        )

    except Exception as e:
        print(f"令牌刷新失败: {e}")
        # 需要重新授权

def save_tokens(access_token, refresh_token):
    """保存令牌到安全存储"""
    # 实现令牌存储逻辑
    pass

asyncio.run(token_refresh_example())
```

## 业务场景示例

### 订单管理

```python
async def order_management_example():
    """订单管理示例"""

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_id = 123456

        # 1. 获取待发货订单
        pending_orders = await client.order.list(
            access_token=access_token,
            seller_id=seller_id,
            order_status="PAID",  # 已付款待发货
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )

        print(f"待发货订单数量: {len(pending_orders.result)}")

        # 2. 批量发货
        for order in pending_orders.result:
            try:
                # 发货
                ship_response = await client.logistics.ship(
                    access_token=access_token,
                    seller_id=seller_id,
                    order_id=order.order_id,
                    logistics_id=1,  # 顺丰快递
                    waybill_code=f"SF{order.order_id[-8:]}"  # 模拟快递单号
                )

                print(f"订单 {order.order_id} 发货成功")

            except Exception as e:
                print(f"订单 {order.order_id} 发货失败: {e}")

        # 3. 查询物流状态
        for order in pending_orders.result[:5]:  # 查询前5个订单
            try:
                logistics_info = await client.logistics.query(
                    access_token=access_token,
                    seller_id=seller_id,
                    order_id=order.order_id
                )

                print(f"订单 {order.order_id} 物流状态: {logistics_info.status}")

            except Exception as e:
                print(f"查询订单 {order.order_id} 物流失败: {e}")

asyncio.run(order_management_example())
```

## 分销示例

以下示例演示如何使用主客户端调用分销领域的只读接口。运行前请设置环境变量：

- `KS_APP_KEY`、`KS_APP_SECRET`、`KS_SIGN_SECRET`、`KS_ACCESS_TOKEN`
- 可选：`KS_SERVER_URL`（默认 `https://openapi.kwaixiaodian.com`）

示例脚本位于 `examples/` 目录，可直接运行。

### 异步：获取分销公开分类列表

```bash
python examples/distribution_public_category_async.py
```

核心调用：

```python
async with AsyncKwaixiaodianClient(app_key=..., app_secret=..., sign_secret=...) as client:
    resp = await client.distribution.get_distribution_public_category_list(
        access_token=os.getenv("KS_ACCESS_TOKEN", "")
    )
```

### 同步：获取分销公开分类列表

```bash
python examples/distribution_public_category_sync.py
```

### 异步：获取 CPS 推荐话题

```bash
python examples/cps_reco_topic_async.py
```

核心调用：

```python
async with AsyncKwaixiaodianClient(app_key=..., app_secret=..., sign_secret=...) as client:
    resp = await client.distribution.get_cps_promotion_reco_topic_list(
        access_token=os.getenv("KS_ACCESS_TOKEN", "")
    )
```

### 同步：获取 CPS 推荐话题

```bash
python examples/cps_reco_topic_sync.py
```

### 异步：获取 二级分销 投资活动列表（标准）

```bash
python examples/second_investment_activity_list_async.py
```

### 同步：获取 二级分销 投资活动列表（标准）

```bash
python examples/second_investment_activity_list_sync.py
```

### 物流模板管理

```python
async def logistics_template_example():
    """物流模板管理示例（异步）"""

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"

        # 1. 创建快递模板
        await client.logistics.template_create(
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

        # 2. 查询模板列表
        await client.logistics.template_list(access_token)

        # 3. 更新快递模板（仅传需要更新的字段）
        await client.logistics.template_update(
            access_token=access_token,
            template_id=123,  # 替换为实际模板ID
            name="更新后的模板名称",
        )

asyncio.run(logistics_template_example())
```

### 商品管理

```python
async def item_management_example():
    """商品管理示例"""

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_id = 123456

        # 1. 创建新商品
        new_item = await client.item.create(
            access_token=access_token,
            seller_id=seller_id,
            title="测试商品",
            price=9999,  # 价格单位为分
            market_price=12999,
            category_id=1001,
            description="这是一个测试商品",
            images=["https://example.com/image1.jpg"],
            stock=100
        )

        print(f"创建商品成功，商品ID: {new_item.product_id}")

        # 2. 更新商品信息
        updated_item = await client.item.update(
            access_token=access_token,
            seller_id=seller_id,
            product_id=new_item.product_id,
            title="更新后的商品标题",
            price=8999,  # 降价
            stock=150   # 增加库存
        )

        print(f"更新商品成功: {updated_item.title}")

        # 3. 批量获取商品信息
        item_ids = [new_item.product_id, "other_product_id"]
        items = await client.item.batch_get(
            access_token=access_token,
            seller_id=seller_id,
            product_ids=item_ids
        )

        for item in items.result:
            print(f"商品: {item.title}, 价格: {item.price/100}元, 库存: {item.stock}")

        # 4. 更新库存
        await client.item.update_stock(
            access_token=access_token,
            seller_id=seller_id,
            product_id=new_item.product_id,
            stock=200
        )

        print(f"商品 {new_item.product_id} 库存更新为200")

        # 5. 商品上下架
        await client.item.update_status(
            access_token=access_token,
            seller_id=seller_id,
            product_id=new_item.product_id,
            status="OFFLINE"  # 下架
        )

        print(f"商品 {new_item.product_id} 已下架")

asyncio.run(item_management_example())
```

### 售后处理

```python
async def refund_management_example():
    """售后管理示例"""

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_id = 123456

        # 1. 获取待处理退款单
        refunds = await client.refund.list(
            access_token=access_token,
            seller_id=seller_id,
            status="WAITING_SELLER_AGREE",  # 等待商家同意
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )

        print(f"待处理退款单数量: {len(refunds.result)}")

        # 2. 处理退款单
        for refund in refunds.result:
            try:
                # 获取退款详情
                refund_detail = await client.refund.get_detail(
                    access_token=access_token,
                    seller_id=seller_id,
                    refund_id=refund.refund_id
                )

                print(f"退款单 {refund.refund_id}:")
                print(f"  订单ID: {refund_detail.order_id}")
                print(f"  退款金额: {refund_detail.refund_amount/100}元")
                print(f"  退款原因: {refund_detail.refund_reason}")

                # 根据退款金额决定是否同意
                if refund_detail.refund_amount <= 5000:  # 50元以下自动同意
                    await client.refund.agree(
                        access_token=access_token,
                        seller_id=seller_id,
                        refund_id=refund.refund_id
                    )
                    print(f"  自动同意退款")

                else:
                    # 大金额退款需要人工审核
                    print(f"  需要人工审核")

            except Exception as e:
                print(f"处理退款单 {refund.refund_id} 失败: {e}")

        # 3. 查询退款统计
        refund_stats = await client.refund.get_statistics(
            access_token=access_token,
            seller_id=seller_id,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )

        print(f"本月退款统计:")
        print(f"  退款单数: {refund_stats.total_count}")
        print(f"  退款金额: {refund_stats.total_amount/100}元")
        print(f"  退款率: {refund_stats.refund_rate}%")

asyncio.run(refund_management_example())
```

## 高级用法示例

### 并发处理

```python
import asyncio
from typing import List, Dict, Any

async def concurrent_processing_example():
    """并发处理示例"""

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_ids = [123456, 123457, 123458, 123459, 123460]

        # 并发获取多个商家的订单
        async def get_seller_orders(seller_id: int) -> Dict[str, Any]:
            try:
                orders = await client.order.list(
                    access_token=access_token,
                    seller_id=seller_id,
                    begin_time="2024-01-01T00:00:00",
                    end_time="2024-01-31T23:59:59"
                )

                return {
                    "seller_id": seller_id,
                    "order_count": len(orders.result),
                    "orders": orders.result,
                    "success": True
                }

            except Exception as e:
                return {
                    "seller_id": seller_id,
                    "error": str(e),
                    "success": False
                }

        # 创建并发任务
        tasks = [get_seller_orders(seller_id) for seller_id in seller_ids]

        # 等待所有任务完成
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # 处理结果
        total_orders = 0
        successful_sellers = 0

        for result in results:
            if isinstance(result, dict) and result.get("success"):
                seller_id = result["seller_id"]
                order_count = result["order_count"]
                total_orders += order_count
                successful_sellers += 1

                print(f"商家 {seller_id}: {order_count} 个订单")
            else:
                print(f"获取商家订单失败: {result}")

        print(f"\n总计: {successful_sellers} 个商家, {total_orders} 个订单")

asyncio.run(concurrent_processing_example())
```

### 分页数据处理

```python
async def pagination_example():
    """分页数据处理示例"""

    async def get_all_orders(client, access_token, seller_id):
        """获取所有订单数据"""
        all_orders = []
        page = 1
        page_size = 100

        while True:
            try:
                response = await client.order.list(
                    access_token=access_token,
                    seller_id=seller_id,
                    begin_time="2024-01-01T00:00:00",
                    end_time="2024-01-31T23:59:59",
                    page=page,
                    size=page_size
                )

                if not response.result:
                    break

                all_orders.extend(response.result)
                print(f"已获取 {len(all_orders)} 个订单")

                # 如果返回的数据少于页面大小，说明已经是最后一页
                if len(response.result) < page_size:
                    break

                page += 1

                # 添加延迟避免频率限制
                await asyncio.sleep(0.1)

            except Exception as e:
                print(f"获取第 {page} 页数据失败: {e}")
                break

        return all_orders

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_id = 123456

        orders = await get_all_orders(client, access_token, seller_id)
        print(f"总共获取到 {len(orders)} 个订单")

        # 统计订单状态
        status_count = {}
        for order in orders:
            status = order.order_status
            status_count[status] = status_count.get(status, 0) + 1

        print("订单状态统计:")
        for status, count in status_count.items():
            print(f"  {status}: {count}")

asyncio.run(pagination_example())
```

### 错误处理和重试

```python
import asyncio
import random
from kwaixiaodian import (
    AsyncKwaixiaodianClient,
    KwaixiaodianAPIError,
    KwaixiaodianNetworkError,
    KwaixiaodianAuthError
)

async def retry_example():
    """错误处理和重试示例"""

    async def api_call_with_retry(func, max_retries=3, base_delay=1.0):
        """带重试的API调用"""
        for attempt in range(max_retries + 1):
            try:
                return await func()

            except KwaixiaodianNetworkError as e:
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    print(f"网络错误，{delay:.2f}秒后重试 (尝试 {attempt + 1}/{max_retries + 1}): {e}")
                    await asyncio.sleep(delay)
                else:
                    print(f"网络错误，重试 {max_retries} 次后仍然失败")
                    raise

            except KwaixiaodianAPIError as e:
                if e.code == "40004" and attempt < max_retries:  # 频率限制
                    delay = base_delay * (2 ** attempt)
                    print(f"频率限制，{delay:.2f}秒后重试")
                    await asyncio.sleep(delay)
                else:
                    print(f"API错误，不重试: {e.code} - {e.message}")
                    raise

            except KwaixiaodianAuthError as e:
                print(f"认证错误，不重试: {e.code} - {e.message}")
                raise

        return None

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_id = 123456

        # 定义API调用函数
        async def get_orders():
            return await client.order.list(
                access_token=access_token,
                seller_id=seller_id,
                begin_time="2024-01-01T00:00:00",
                end_time="2024-01-31T23:59:59"
            )

        try:
            orders = await api_call_with_retry(get_orders, max_retries=3)
            print(f"成功获取 {len(orders.result)} 个订单")

        except Exception as e:
            print(f"最终失败: {e}")

asyncio.run(retry_example())
```

### 数据导出

```python
import asyncio
import csv
import json
from datetime import datetime, timedelta

async def data_export_example():
    """数据导出示例"""

    async with AsyncKwaixiaodianClient(...) as client:
        access_token = "your_access_token"
        seller_id = 123456

        # 获取过去30天的订单数据
        end_time = datetime.now()
        start_time = end_time - timedelta(days=30)

        all_orders = []
        page = 1

        while True:
            try:
                response = await client.order.list(
                    access_token=access_token,
                    seller_id=seller_id,
                    begin_time=start_time.isoformat(),
                    end_time=end_time.isoformat(),
                    page=page,
                    size=100
                )

                if not response.result:
                    break

                all_orders.extend(response.result)
                page += 1

                print(f"已获取 {len(all_orders)} 个订单")

            except Exception as e:
                print(f"获取订单数据失败: {e}")
                break

        # 导出为CSV
        with open("orders_export.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "order_id", "order_status", "create_time", "pay_time",
                "total_amount", "buyer_id", "buyer_name"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for order in all_orders:
                writer.writerow({
                    "order_id": order.order_id,
                    "order_status": order.order_status,
                    "create_time": order.create_time,
                    "pay_time": getattr(order, "pay_time", ""),
                    "total_amount": order.total_amount / 100,  # 转换为元
                    "buyer_id": order.buyer_id,
                    "buyer_name": getattr(order, "buyer_name", "")
                })

        print(f"订单数据已导出到 orders_export.csv，共 {len(all_orders)} 条记录")

        # 导出为JSON
        with open("orders_export.json", "w", encoding="utf-8") as jsonfile:
            order_data = []
            for order in all_orders:
                order_dict = {
                    "order_id": order.order_id,
                    "order_status": order.order_status,
                    "create_time": order.create_time,
                    "total_amount": order.total_amount,
                    "buyer_id": order.buyer_id,
                    # 包含所有字段
                    **{k: v for k, v in order.__dict__.items() if not k.startswith('_')}
                }
                order_data.append(order_dict)

            json.dump(order_data, jsonfile, ensure_ascii=False, indent=2)

        print(f"订单数据已导出到 orders_export.json")

asyncio.run(data_export_example())
```

## 实用工具示例

### 配置管理

```python
import os
import yaml
from dataclasses import dataclass
from typing import Optional

@dataclass
class SDKConfig:
    """SDK配置类"""
    app_key: str
    app_secret: str
    sign_secret: str
    base_url: Optional[str] = None
    timeout: float = 30.0
    max_retries: int = 3

    @classmethod
    def from_env(cls):
        """从环境变量创建配置"""
        return cls(
            app_key=os.environ["KUAISHOU_APP_KEY"],
            app_secret=os.environ["KUAISHOU_APP_SECRET"],
            sign_secret=os.environ["KUAISHOU_SIGN_SECRET"],
            base_url=os.environ.get("KUAISHOU_BASE_URL"),
            timeout=float(os.environ.get("KUAISHOU_TIMEOUT", "30.0")),
            max_retries=int(os.environ.get("KUAISHOU_MAX_RETRIES", "3"))
        )

    @classmethod
    def from_file(cls, config_file: str):
        """从配置文件创建配置"""
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)

        return cls(**config_data['kuaishou'])

    def create_client(self):
        """创建客户端"""
        from kwaixiaodian import AsyncKwaixiaodianClient
        from kwaixiaodian.http import HTTPConfig, RetryConfig

        http_config = HTTPConfig(
            timeout=self.timeout,
            base_url=self.base_url
        )

        retry_config = RetryConfig(
            max_retries=self.max_retries
        )

        return AsyncKwaixiaodianClient(
            app_key=self.app_key,
            app_secret=self.app_secret,
            sign_secret=self.sign_secret,
            http_config=http_config,
            retry_config=retry_config
        )

# 使用示例
async def config_example():
    # 从环境变量加载配置
    config = SDKConfig.from_env()

    # 或从配置文件加载
    # config = SDKConfig.from_file("config.yaml")

    async with config.create_client() as client:
        # 使用客户端
        pass

# config.yaml 示例文件内容:
"""
kuaishou:
  app_key: "your_app_key"
  app_secret: "your_app_secret"
  sign_secret: "your_sign_secret"
  base_url: "https://api.kwaixiaodian.com"
  timeout: 30.0
  max_retries: 3
"""
```

### 日志配置

```python
import logging
import sys
from datetime import datetime

def setup_logging(level=logging.INFO, log_file=None):
    """配置日志"""

    # 创建日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 配置根日志记录器
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # 清除已有的处理器
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # 文件处理器（如果指定）
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    # 配置SDK日志
    sdk_logger = logging.getLogger('kwaixiaodian')
    sdk_logger.setLevel(level)

    # 隐藏敏感信息
    class SensitiveFilter(logging.Filter):
        def filter(self, record):
            sensitive_keys = ['access_token', 'app_secret', 'sign_secret']
            if hasattr(record, 'msg'):
                msg = str(record.msg)
                for key in sensitive_keys:
                    if key in msg:
                        record.msg = msg.replace(key, '***')
            return True

    sdk_logger.addFilter(SensitiveFilter())

# 使用示例
async def logging_example():
    # 配置日志
    setup_logging(
        level=logging.INFO,
        log_file=f"kwaixiaodian_{datetime.now().strftime('%Y%m%d')}.log"
    )

    logger = logging.getLogger(__name__)

    async with AsyncKwaixiaodianClient(...) as client:
        logger.info("开始获取订单数据")

        try:
            orders = await client.order.list(...)
            logger.info(f"成功获取 {len(orders.result)} 个订单")

        except Exception as e:
            logger.error(f"获取订单失败: {e}")

asyncio.run(logging_example())
```

这些示例涵盖了快手小店Python SDK的主要使用场景。你可以根据自己的需求选择合适的示例进行参考和修改。

## 分销示例（Distribution）

- 计划创建 + 佣金查询：参见代码 `examples/distribution_plan_create_and_commission.py`。
- 二级分销申请 + 列表：参见代码 `examples/second_distribution_apply_and_list.py`。
- 其他分销示例：参见 `examples/distribution_examples.py`（计划查询、佣金查询、PID 更新、卖家活动效果等）。
