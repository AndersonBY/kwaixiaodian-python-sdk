# API参考概述

快手小店Python SDK提供了完整的API接口，支持异步和同步两种调用方式。

## 📋 业务模块导航

### 🏢 核心客户端
- [核心客户端](api/core-clients.md) - 主要的SDK客户端类和OAuth认证

### 💼 核心业务
- [订单服务](api/order-service.md) - 订单查询、发货、状态更新
- [商品服务](api/item-service.md) - 商品CRUD、库存、规格管理
- [售后服务](api/refund-service.md) - 退款退货、协商处理
- [物流服务](api/logistics-service.md) - 物流跟踪、发货管理

### 💰 财务管理
- [资金服务](api/funds-service.md) - 账户资金、财务结算、提现管理
- [发票服务](api/invoice-service.md) - 发票开具、发票查询

### 🏪 店铺管理
- [店铺服务](api/shop-service.md) - 店铺信息、装修配置

### 🔧 基础模块
- [基础模块](api/base-modules.md) - 异常处理、基础模型、通用组件

## 🚀 快速访问

### 常用客户端类
- `AsyncKwaixiaodianClient` - 异步主客户端
- `SyncKwaixiaodianClient` - 同步主客户端
- `AsyncOAuthClient` - 异步OAuth客户端
- `SyncOAuthClient` - 同步OAuth客户端

### 常用异常类
- `KwaixiaodianSDKError` - SDK基础异常
- `KwaixiaodianAPIError` - API业务错误
- `KwaixiaodianAuthError` - 认证错误
- `KwaixiaodianNetworkError` - 网络错误

## 📖 使用说明

所有API服务都支持异步和同步两种调用方式：

```python
# 异步调用
async with AsyncKwaixiaodianClient(...) as client:
    orders = await client.order.list(...)

# 同步调用
with SyncKwaixiaodianClient(...) as client:
    orders = client.order.list(...)
```

## 🎯 API设计原则

1. **异步优先** - 所有API都支持异步调用，提供更好的性能
2. **类型安全** - 完整的类型注解和Pydantic数据验证
3. **业务分组** - 按业务域组织API，便于查找和使用
4. **Java对齐** - 严格基于官方Java SDK实现，确保兼容性
5. **错误友好** - 详细的异常信息和错误码映射

选择左侧导航中的具体服务模块查看详细的API文档。