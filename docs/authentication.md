# 认证指南

快手小店SDK支持完整的OAuth 2.0认证流程，本指南将详细介绍如何配置和使用认证功能。

## OAuth 2.0认证流程

### 1. 创建OAuth客户端

```python
from kwaixiaodian import AsyncOAuthClient, SyncOAuthClient

# 异步OAuth客户端
oauth_client = AsyncOAuthClient(
    app_key="your_app_key",
    app_secret="your_app_secret"
)

# 同步OAuth客户端
oauth_client = SyncOAuthClient(
    app_key="your_app_key",
    app_secret="your_app_secret"
)
```

### 2. 获取授权URL

```python
# 构建授权URL
auth_url = oauth_client.get_authorize_url(
    redirect_uri="https://your-app.com/callback",
    scope=["merchant_order", "merchant_item", "merchant_refund"],
    state="random_state_string"
)

print(f"请访问以下URL进行授权: {auth_url}")
```

### 3. 处理授权回调

用户在快手授权后，会重定向到你的`redirect_uri`，携带授权码：

```
https://your-app.com/callback?code=AUTHORIZATION_CODE&state=random_state_string
```

### 4. 获取访问令牌

```python
# 异步方式
async def get_token(authorization_code):
    token_response = await oauth_client.get_access_token(
        code=authorization_code,
        redirect_uri="https://your-app.com/callback"
    )

    access_token = token_response.access_token
    refresh_token = token_response.refresh_token
    expires_in = token_response.expires_in

    return access_token, refresh_token, expires_in

# 同步方式
def get_token_sync(authorization_code):
    token_response = oauth_client.get_access_token(
        code=authorization_code,
        redirect_uri="https://your-app.com/callback"
    )

    return token_response.access_token, token_response.refresh_token
```

### 5. 刷新访问令牌

访问令牌有效期通常为24小时，需要使用刷新令牌获取新的访问令牌：

```python
# 异步刷新
async def refresh_access_token(refresh_token):
    token_response = await oauth_client.refresh_access_token(
        refresh_token=refresh_token
    )

    new_access_token = token_response.access_token
    new_refresh_token = token_response.refresh_token  # 可能更新

    return new_access_token, new_refresh_token

# 同步刷新
def refresh_access_token_sync(refresh_token):
    token_response = oauth_client.refresh_access_token(
        refresh_token=refresh_token
    )

    return token_response.access_token, token_response.refresh_token
```

## 权限范围 (Scope)

快手开放平台支持以下权限范围：

| Scope                       | 说明     | 包含权限                 |
| --------------------------- | -------- | ------------------------ |
| `merchant_basic`            | 基础信息 | 店铺基本信息查询         |
| `merchant_order`            | 订单管理 | 订单查询、发货、状态更新 |
| `merchant_item`             | 商品管理 | 商品增删改查、库存管理   |
| `merchant_refund`           | 售后管理 | 退款退货处理             |
| `merchant_logistics`        | 物流管理 | 物流查询、发货管理       |
| `merchant_promotion`        | 营销推广 | 优惠券、活动管理         |
| `merchant_finance`          | 财务管理 | 资金查询、结算管理       |
| `merchant_customer_service` | 客服管理 | 客服消息、工单管理       |

### 申请多个权限

```python
auth_url = oauth_client.get_authorize_url(
    redirect_uri="https://your-app.com/callback",
    scope=[
        "merchant_basic",
        "merchant_order",
        "merchant_item",
        "merchant_refund",
        "merchant_logistics"
    ],
    state="random_state_string"
)
```

## 签名验证

快手API使用HMAC-SHA256或MD5进行签名验证，SDK会自动处理签名计算。

### 配置签名方法

```python
from kwaixiaodian import AsyncKwaixiaodianClient
from kwaixiaodian.auth import SignMethod

async with AsyncKwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret",
    sign_method=SignMethod.HMAC_SHA256  # 或 SignMethod.MD5
) as client:
    # 客户端会自动处理签名
    pass
```

### 签名算法详解

#### HMAC-SHA256签名 (推荐)

1. 按参数名排序所有请求参数
2. 构建查询字符串格式：`key1=value1&key2=value2`
3. 使用HMAC-SHA256算法和sign_secret计算签名
4. 将签名添加到请求参数中

#### MD5签名

1. 按参数名排序所有请求参数
2. 构建字符串：`key1value1key2value2sign_secret`
3. 计算MD5哈希值
4. 将签名添加到请求参数中

## 令牌管理最佳实践

### 1. 安全存储令牌

```python
import os
import json
from cryptography.fernet import Fernet

class TokenStorage:
    def __init__(self, encryption_key=None):
        self.key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def save_token(self, user_id, access_token, refresh_token):
        """安全存储令牌"""
        token_data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user_id": user_id
        }

        encrypted_data = self.cipher.encrypt(
            json.dumps(token_data).encode()
        )

        # 存储到数据库或文件
        with open(f"tokens/{user_id}.token", "wb") as f:
            f.write(encrypted_data)

    def load_token(self, user_id):
        """加载令牌"""
        try:
            with open(f"tokens/{user_id}.token", "rb") as f:
                encrypted_data = f.read()

            decrypted_data = self.cipher.decrypt(encrypted_data)
            token_data = json.loads(decrypted_data.decode())

            return token_data["access_token"], token_data["refresh_token"]
        except FileNotFoundError:
            return None, None
```

### 2. 自动令牌刷新

```python
import asyncio
from datetime import datetime, timedelta

class TokenManager:
    def __init__(self, oauth_client, token_storage):
        self.oauth_client = oauth_client
        self.token_storage = token_storage
        self.tokens = {}  # user_id -> token_info

    async def get_valid_token(self, user_id):
        """获取有效的访问令牌，自动刷新过期令牌"""
        if user_id not in self.tokens:
            # 从存储加载令牌
            access_token, refresh_token = self.token_storage.load_token(user_id)
            if not access_token:
                raise ValueError("用户未授权")

            self.tokens[user_id] = {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_at": datetime.now() + timedelta(hours=24)
            }

        token_info = self.tokens[user_id]

        # 检查是否需要刷新
        if datetime.now() >= token_info["expires_at"]:
            try:
                # 刷新令牌
                new_token_response = await self.oauth_client.refresh_access_token(
                    refresh_token=token_info["refresh_token"]
                )

                # 更新令牌信息
                token_info["access_token"] = new_token_response.access_token
                token_info["refresh_token"] = new_token_response.refresh_token
                token_info["expires_at"] = datetime.now() + timedelta(
                    seconds=new_token_response.expires_in
                )

                # 保存新令牌
                self.token_storage.save_token(
                    user_id,
                    new_token_response.access_token,
                    new_token_response.refresh_token
                )

            except Exception as e:
                # 刷新失败，清除令牌
                del self.tokens[user_id]
                raise ValueError(f"令牌刷新失败: {e}")

        return token_info["access_token"]

# 使用示例
token_manager = TokenManager(oauth_client, token_storage)

async def api_call_with_auto_refresh(user_id):
    access_token = await token_manager.get_valid_token(user_id)

    async with AsyncKwaixiaodianClient(...) as client:
        orders = await client.order.list(
            access_token=access_token,
            seller_id=user_id,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )

    return orders
```

### 3. 多租户令牌管理

```python
class MultiTenantTokenManager:
    def __init__(self):
        self.tenant_oauth_clients = {}  # tenant_id -> oauth_client
        self.tenant_tokens = {}  # tenant_id -> user_tokens

    def add_tenant(self, tenant_id, app_key, app_secret):
        """添加租户"""
        self.tenant_oauth_clients[tenant_id] = AsyncOAuthClient(
            app_key=app_key,
            app_secret=app_secret
        )
        self.tenant_tokens[tenant_id] = {}

    async def authorize_user(self, tenant_id, user_id, authorization_code):
        """为租户的用户进行授权"""
        oauth_client = self.tenant_oauth_clients[tenant_id]

        token_response = await oauth_client.get_access_token(
            code=authorization_code,
            redirect_uri=f"https://your-app.com/{tenant_id}/callback"
        )

        self.tenant_tokens[tenant_id][user_id] = {
            "access_token": token_response.access_token,
            "refresh_token": token_response.refresh_token,
            "expires_at": datetime.now() + timedelta(
                seconds=token_response.expires_in
            )
        }

    async def get_client_for_user(self, tenant_id, user_id):
        """获取特定租户用户的客户端"""
        token_info = self.tenant_tokens[tenant_id][user_id]
        access_token = token_info["access_token"]

        # 这里可以加入令牌刷新逻辑

        return AsyncKwaixiaodianClient(
            app_key=self.tenant_oauth_clients[tenant_id].app_key,
            app_secret=self.tenant_oauth_clients[tenant_id].app_secret,
            sign_secret="tenant_sign_secret"  # 每个租户可以有不同的签名密钥
        )
```

## 常见问题

### Q: 如何处理授权被撤销的情况？

A: 当用户撤销授权时，API调用会返回`AUTHORIZATION_REVOKED`错误。你需要重新引导用户进行授权：

```python
from kwaixiaodian import KwaixiaodianAuthError

try:
    response = await client.order.list(...)
except KwaixiaodianAuthError as e:
    if e.code == "AUTHORIZATION_REVOKED":
        # 重新引导用户授权
        auth_url = oauth_client.get_authorize_url(...)
        # 提示用户重新授权
```

### Q: 令牌过期如何处理？

A: SDK会自动检测令牌过期并抛出相应异常。建议使用令牌管理器自动处理刷新：

```python
try:
    response = await client.order.list(...)
except KwaixiaodianAuthError as e:
    if "token" in e.message.lower() and "expire" in e.message.lower():
        # 尝试刷新令牌
        new_token = await refresh_access_token(refresh_token)
        # 重试API调用
```

### Q: 如何在生产环境中管理多个应用的认证？

A: 建议使用配置文件或环境变量管理应用凭证：

```python
import os
from kwaixiaodian import AsyncKwaixiaodianClient

# 从环境变量读取配置
async with AsyncKwaixiaodianClient(
    app_key=os.getenv("KUAISHOU_APP_KEY"),
    app_secret=os.getenv("KUAISHOU_APP_SECRET"),
    sign_secret=os.getenv("KUAISHOU_SIGN_SECRET")
) as client:
    pass
```

## 安全建议

1. **永远不要在客户端代码中硬编码密钥**
2. **使用HTTPS传输所有认证相关数据**
3. **定期轮换app_secret和sign_secret**
4. **实施令牌的安全存储和传输**
5. **监控异常的认证请求和失败模式**
6. **实施适当的访问控制和权限验证**
