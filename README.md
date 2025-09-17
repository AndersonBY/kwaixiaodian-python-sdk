# 快手小店开放平台 Python SDK

[![PyPI](https://img.shields.io/pypi/v/kwaixiaodian.svg)](https://pypi.org/project/kwaixiaodian/)
[![Python](https://img.shields.io/pypi/pyversions/kwaixiaodian.svg)](https://pypi.org/project/kwaixiaodian/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Lint & Typecheck](https://github.com/AndersonBY/kwaixiaodian-python-sdk/actions/workflows/lint-typecheck.yml/badge.svg)](https://github.com/AndersonBY/kwaixiaodian-python-sdk/actions/workflows/lint-typecheck.yml)
[![Tests](https://github.com/AndersonBY/kwaixiaodian-python-sdk/actions/workflows/tests.yml/badge.svg)](https://github.com/AndersonBY/kwaixiaodian-python-sdk/actions/workflows/tests.yml)
[![Docs](https://github.com/AndersonBY/kwaixiaodian-python-sdk/actions/workflows/docs.yml/badge.svg)](https://github.com/AndersonBY/kwaixiaodian-python-sdk/actions/workflows/docs.yml)

快手小店开放平台的现代化Python SDK，提供完整的异步API支持。

## ✨ 特性

- 🚀 **异步优先** - 基于 `httpx` 的高性能异步HTTP客户端
- 🔄 **同步支持** - 提供同步版本客户端，满足不同场景需求
- 🔐 **完整认证** - 支持OAuth 2.0认证流程和签名验证
- 📦 **按Java参考对齐** - 仅实现 Java SDK 参考中存在的官方API
- 🎯 **类型安全** - 基于Pydantic v2的完整类型注解和数据验证
- ⚡ **高性能** - 连接池、自动重试、并发请求支持
- 📚 **完整文档** - 详细的API文档和丰富的使用示例
- 🛡️ **错误处理** - 全面的异常处理和错误码映射
- 🔄 **自动重试** - 网络异常和令牌过期自动重试机制

## 📦 安装

```bash
# 基础安装
pip install kwaixiaodian

# 或使用PDM
pdm add kwaixiaodian

# 开发环境安装
pip install "kwaixiaodian[dev,test,docs]"
```

## 🚀 快速开始

SDK提供了异步和同步两个版本的客户端，您可以根据需求选择使用：

### 🔥 异步版本（推荐用于高并发场景）

```python
import asyncio
from kwaixiaodian import KwaixiaodianClient

# 初始化异步客户端
async def main():
    async with KwaixiaodianClient(
        app_key="your_app_key",           # 应用AppKey
        app_secret="your_app_secret",     # 应用AppSecret  
        sign_secret="your_sign_secret",   # 签名密钥
    ) as client:
        # 使用异步客户端进行API调用
        orders = await client.order.list(...)
        
asyncio.run(main())
```

### 🔧 同步版本（适合脚本和简单场景）

```python
from kwaixiaodian import SyncKwaixiaodianClient

# 初始化同步客户端
with SyncKwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret",
) as client:
    # 使用同步客户端进行API调用
    orders = client.order.list(...)
```

### 2. OAuth认证

#### 异步版本

```python
from kwaixiaodian import OAuthClient

async with OAuthClient(
    app_key="your_app_key",
    app_secret="your_app_secret"
) as oauth_client:
    # 获取授权URL
    auth_url = oauth_client.get_authorize_url(
        redirect_uri="your_redirect_uri",
        scope=["merchant_order", "merchant_item"]
    )
    print(f"请访问授权链接: {auth_url}")
    
    # 授权回调后，使用code获取token
    token_response = await oauth_client.get_access_token(
        code="authorization_code_from_callback"
    )
    
    access_token = token_response.access_token
    refresh_token = token_response.refresh_token
```

#### 同步版本

```python
from kwaixiaodian import SyncOAuthClient

with SyncOAuthClient(
    app_key="your_app_key",
    app_secret="your_app_secret"
) as oauth_client:
    # 获取授权URL
    auth_url = oauth_client.get_authorize_url(
        redirect_uri="your_redirect_uri",
        scope=["merchant_order", "merchant_item"]
    )
    print(f"请访问授权链接: {auth_url}")
    
    # 授权回调后，使用code获取token（同步调用）
    token_response = oauth_client.get_access_token(
        code="authorization_code_from_callback"
    )
    
    access_token = token_response.access_token
    refresh_token = token_response.refresh_token
```

### 3. API调用示例

#### 异步版本示例

```python
# 订单管理
async with KwaixiaodianClient(app_key, app_secret, sign_secret) as client:
    # 获取订单列表
    orders = await client.order.list(
        access_token=access_token,
        seller_id=123456,
        begin_time="2024-01-01T00:00:00",
        end_time="2024-01-31T23:59:59",
        page_size=100
    )

    # 获取订单详情
    order_detail = await client.order.get(
        access_token=access_token,
        order_id="202401010001"
    )
    
    # 商品管理
    items = await client.item.list(
        access_token=access_token,
        page_size=50,
        status=1  # 1-在售，2-下架
    )

    # 新建商品（简化示例）
    # from kwaixiaodian.models.item import OpenApiAddSkuDTO
    # new_item = await client.item.new(
    #     access_token=access_token,
    #     title="新商品标题",
    #     category_id=12345,
    #     image_urls=["https://example.com/main.jpg"],
    #     sku_list=[OpenApiAddSkuDTO(rel_sku_id=1, sku_stock=100, sku_sale_price=9999)],
    # )
```

#### 同步版本示例

```python
# 订单管理
with SyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
    # 获取订单列表（无需await）
    orders = client.order.list(
        access_token=access_token,
        seller_id=123456,
        begin_time="2024-01-01T00:00:00",
        end_time="2024-01-31T23:59:59",
        page_size=100
    )

    # 获取订单详情
    order_detail = client.order.get(
        access_token=access_token,
        order_id="202401010001"
    )
    
    # 商品管理
    items = client.item.list(
        access_token=access_token,
        page_size=50,
        status=1  # 1-在售，2-下架
    )

    # 新建商品（简化示例）
    # from kwaixiaodian.models.item import OpenApiAddSkuDTO
    # new_item = client.item.new(
    #     access_token=access_token,
    #     title="新商品标题",
    #     category_id=12345,
    #     image_urls=["https://example.com/main.jpg"],
    #     sku_list=[OpenApiAddSkuDTO(rel_sku_id=1, sku_stock=100, sku_sale_price=9999)],
    # )
```

#### 物流发货

```python
# 订单发货
ship_result = await client.logistics.ship(
    access_token=access_token,
    order_id="202401010001",
    logistics_company="SF",  # 顺丰
    tracking_number="SF123456789",
    ship_time="2024-01-15T10:30:00"
)

# 注：物流轨迹查询与物流公司列表接口以 Java 参考为准，当前未提供
```

#### 售后处理

```python
# 获取退款单列表
refunds = await client.refund.list(
    access_token=access_token,
    begin_time="2024-01-01T00:00:00",
    end_time="2024-01-31T23:59:59"
)

# 同意退款
await client.refund.agree(
    access_token=access_token,
    refund_id="RF202401010001",
    refund_amount=9999  # 分为单位
)
```

### 4. 批量操作

```python
# 并发调用多个API
async def fetch_order_details(order_ids):
    tasks = [
        client.order.get(access_token=access_token, order_id=oid)
        for oid in order_ids
    ]
    return await asyncio.gather(*tasks)

order_details = await fetch_order_details([
    "202401010001", "202401010002", "202401010003"
])
```

### 5. 错误处理

```python
from kwaixiaodian import KwaixiaodianAPIError, KwaixiaodianAuthError

try:
    orders = await client.order.list(
        access_token=access_token,
        seller_id=123456,
        begin_time="2024-01-01T00:00:00",
        end_time="2024-01-31T23:59:59"
    )
except KwaixiaodianAuthError as e:
    print(f"认证失败: {e.message}")
    # 自动刷新token逻辑
    new_token = await oauth_client.refresh_access_token(refresh_token)
    # 重试API调用
except KwaixiaodianAPIError as e:
    print(f"API调用失败: {e.error_code} - {e.message}")
    if e.error_code == "ITEM_NOT_FOUND":
        print("商品不存在")
except Exception as e:
    print(f"未知错误: {e}")
```

## 🏗️ 支持的业务领域

| 业务域                   | 功能描述                   | 主要API                                       |
| ------------------------ | -------------------------- | --------------------------------------------- |
| **订单管理** (order)     | 订单查询、状态更新、发货等 | `list`, `get`, `update_status`, `ship`        |
| **商品管理** (item)      | 商品CRUD、库存、规格等     | `list`, `get`, `create`, `update`, `delete`   |
| **售后管理** (refund)    | 退款退货、协商处理等       | `list`, `get`, `agree`, `reject`, `negotiate` |
| **营销推广** (promotion) | 优惠券、活动、分销等       | `coupon_*`, `activity_*`, `distribution_*`    |
| **物流快递** (logistics) | 发货、跟踪、地址管理等     | `ship`, `track`, `companies`, `addresses`     |
| **用户管理** (user)      | 用户信息、授权管理等       | `info`, `shops`, `permissions`                |
| **评价管理** (comment)   | 商品评价、回复等           | `list`, `reply`, `appeal`                     |
| **资金管理** (funds)     | 账单、提现、流水等         | `balance`, `bills`, `withdraw`                |
| **店铺管理** (shop)      | 店铺信息、设置等           | `info`, `update`, `settings`                  |
| **直播带货** (shoplive)  | 直播商品、数据等           | `items`, `data`, `settings`                   |

[查看完整API列表](docs/api-reference.md)

## 🔧 高级功能

### 自定义HTTP配置

```python
import httpx

# 自定义HTTP客户端配置
custom_client = KwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret",
    http_config={
        "timeout": 30.0,
        "limits": httpx.Limits(max_connections=100, max_keepalive_connections=20),
        "proxies": "http://proxy.example.com:8080",
        "verify": True  # SSL验证
    }
)
```

### 自动重试配置

```python
# 配置重试策略
client = KwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret", 
    sign_secret="your_sign_secret",
    retry_config={
        "max_retries": 3,
        "backoff_factor": 1.0,
        "retry_on_status": [429, 500, 502, 503, 504],
        "retry_on_auth_error": True  # token过期自动重试
    }
)
```

### 日志配置

```python
import logging

# 开启调试日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("kwaixiaodian")

client = KwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret",
    enable_logging=True,
    log_level="DEBUG"
)
```

## ⚡ 异步 vs 同步版本选择

### 何时使用异步版本 (推荐)

- ✅ **高并发场景** - 需要同时处理多个API请求
- ✅ **Web应用** - FastAPI、Sanic等异步框架
- ✅ **I/O密集型任务** - 大量网络请求、文件操作
- ✅ **现代Python应用** - 充分利用async/await语法

```python
# 异步版本支持并发调用，性能更优
import asyncio
from kwaixiaodian import KwaixiaodianClient

async def process_orders():
    async with KwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        # 并发获取多个订单的详情
        tasks = [
            client.order.get(access_token, order_id) 
            for order_id in order_ids
        ]
        order_details = await asyncio.gather(*tasks)
```

### 何时使用同步版本

- ✅ **脚本和工具** - 批处理脚本、命令行工具
- ✅ **简单集成** - 不需要异步复杂性的场景
- ✅ **遗留系统** - 与同步代码库集成
- ✅ **学习和原型** - 更简单的调试和理解

```python
# 同步版本更适合顺序处理
from kwaixiaodian import SyncKwaixiaodianClient

def process_orders():
    with SyncKwaixiaodianClient(app_key, app_secret, sign_secret) as client:
        for order_id in order_ids:
            # 顺序处理每个订单
            order_detail = client.order.get(access_token, order_id)
            process_single_order(order_detail)
```

### 性能对比

| 场景              | 异步版本           | 同步版本    |
| ----------------- | ------------------ | ----------- |
| **单个API调用**   | ≈相同              | ≈相同       |
| **10个并发调用**  | ~2-3x 更快         | 基准        |
| **100个并发调用** | ~5-10x 更快        | 基准        |
| **内存使用**      | 较低 (协程)        | 较高 (线程) |
| **代码复杂度**    | 中等 (async/await) | 简单        |

### 接口兼容性

两个版本提供完全相同的API接口，只是调用方式不同：

```python
# 异步版本
orders = await client.order.list(access_token, seller_id, ...)

# 同步版本  
orders = client.order.list(access_token, seller_id, ...)
```

## 📖 文档

- [完整API文档](docs/api-reference.md)
- [认证指南](docs/authentication.md)  
- [错误处理](docs/error-handling.md)
- [最佳实践](docs/best-practices.md)
- [更新日志](CHANGELOG.md)

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

### 开发环境设置

```bash
# 克隆项目
git clone https://github.com/AndersonBY/kwaixiaodian-python-sdk.git
cd kwaixiaodian-python-sdk

# 安装PDM
pip install pdm

# 安装依赖
pdm install

# 运行测试
pdm run test

# 代码格式化
pdm run format

# 类型检查  
pdm run typecheck
```

## 📄 许可证

本项目采用 [MIT License](LICENSE) 许可证。

## 🙋‍♂️ 支持

- 📧 邮箱: support@kwaixiaodian.com
- 🐛 Issue: [GitHub Issues](https://github.com/AndersonBY/kwaixiaodian-python-sdk/issues)
- 📖 文档: [在线文档](https://kwaixiaodian-python-sdk.readthedocs.io)

---

⭐ 如果这个项目对您有帮助，请给我们一个Star！
