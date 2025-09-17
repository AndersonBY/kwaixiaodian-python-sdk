# 快速开始

本指南将帮助你在5分钟内开始使用快手小店Python SDK。

## 安装

### 环境要求

- Python 3.8+
- 支持异步编程 (asyncio)

### 使用pip安装

```bash
pip install kwaixiaodian
```

### 从源码安装 (开发版本)

```bash
git clone https://github.com/AndersonBY/kwaixiaodian-python-sdk.git
cd kwaixiaodian-python-sdk
pip install -e .
```

## 获取API凭证

在使用SDK之前，你需要在快手开放平台获取以下信息：

1. **App Key** - 应用标识
2. **App Secret** - 应用密钥
3. **Sign Secret** - 签名密钥
4. **Access Token** - 用户授权令牌

访问 [快手开放平台](https://open.kwaixiaodian.com/) 创建应用并获取这些凭证。

## 基础使用

### 创建客户端

```python
import asyncio
from kwaixiaodian import AsyncKwaixiaodianClient

async def main():
    # 创建异步客户端
    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret"
    ) as client:
        # 你的业务逻辑
        pass

# 运行异步函数
asyncio.run(main())
```

### 同步客户端

如果你的项目不支持异步，可以使用同步客户端：

```python
from kwaixiaodian import SyncKwaixiaodianClient

with SyncKwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret"
) as client:
    # 你的业务逻辑
    pass
```

## 第一个API调用

以查询订单为例：

```python
import asyncio
from kwaixiaodian import AsyncKwaixiaodianClient

async def get_orders():
    async with AsyncKwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret",
        sign_secret="your_sign_secret"
    ) as client:

        # 获取订单列表
        response = await client.order.list(
            access_token="your_access_token",
            seller_id=123456,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59",
            page=1,
            size=20
        )

        print(f"状态码: {response.code}")
        print(f"订单数量: {len(response.result)}")

        for order in response.result:
            print(f"订单号: {order.order_id}, 状态: {order.order_status}")

asyncio.run(get_orders())
```

## 常用业务场景

### 商品管理

```python
# 获取商品列表
items = await client.item.list(
    access_token=access_token,
    seller_id=seller_id,
    page=1,
    size=50
)

# 更新商品信息
await client.item.update(
    access_token=access_token,
    seller_id=seller_id,
    product_id=product_id,
    title="新商品标题",
    price=9999  # 价格单位为分
)
```

### 物流管理

```python
# 发货
await client.logistics.ship(
    access_token=access_token,
    seller_id=seller_id,
    order_id=order_id,
    logistics_id=1,  # 物流公司ID
    waybill_code="SF1234567890"
)

# 查询物流状态
logistics_info = await client.logistics.query(
    access_token=access_token,
    seller_id=seller_id,
    order_id=order_id
)
```

### 售后处理

```python
# 查询退款单
refunds = await client.refund.list(
    access_token=access_token,
    seller_id=seller_id,
    begin_time="2024-01-01T00:00:00",
    end_time="2024-01-31T23:59:59"
)

# 处理退款
await client.refund.agree(
    access_token=access_token,
    seller_id=seller_id,
    refund_id=refund_id
)
```

## 错误处理

SDK提供了完整的异常层次结构：

```python
from kwaixiaodian import (
    AsyncKwaixiaodianClient,
    KwaixiaodianAPIError,
    KwaixiaodianAuthError,
    KwaixiaodianNetworkError
)

async def handle_errors():
    try:
        async with AsyncKwaixiaodianClient(...) as client:
            response = await client.order.list(...)

    except KwaixiaodianAuthError as e:
        print(f"认证错误: {e}")
    except KwaixiaodianAPIError as e:
        print(f"API错误: {e.code} - {e.message}")
    except KwaixiaodianNetworkError as e:
        print(f"网络错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")
```

## 配置选项

### HTTP配置

```python
from kwaixiaodian import AsyncKwaixiaodianClient
from kwaixiaodian.http import HTTPConfig, RetryConfig

# 自定义HTTP配置
http_config = HTTPConfig(
    timeout=30.0,
    max_connections=100,
    max_keepalive_connections=20
)

# 自定义重试配置
retry_config = RetryConfig(
    max_retries=3,
    backoff_factor=0.5,
    status_codes=[429, 500, 502, 503, 504]
)

async with AsyncKwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret",
    http_config=http_config,
    retry_config=retry_config
) as client:
    # 使用自定义配置的客户端
    pass
```

### 日志配置

```python
import logging

# 启用SDK日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('kwaixiaodian')
logger.setLevel(logging.DEBUG)
```

## 下一步

- 查看 [API参考文档](api-reference.md) 了解所有可用接口
- 阅读 [认证指南](authentication.md) 了解OAuth流程
- 参考 [示例代码](examples.md) 查看更多使用场景
- 查看 [最佳实践](best-practices.md) 了解生产环境建议

## 获取帮助

如果遇到问题，可以：

- 查看 [GitHub Issues](https://github.com/AndersonBY/kwaixiaodian-python-sdk/issues)
- 发送邮件到 support@kwaixiaodian.com
- 查看在线文档获取更多信息