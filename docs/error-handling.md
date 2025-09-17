# 错误处理

快手小店SDK提供了完整的异常层次结构和错误处理机制，帮助你优雅地处理各种异常情况。

## 异常层次结构

SDK定义了以下异常类：

```
KwaixiaodianSDKError (基础异常)
├── KwaixiaodianAPIError (API业务错误)
├── KwaixiaodianAuthError (认证错误)
├── KwaixiaodianNetworkError (网络错误)
└── KwaixiaodianSignatureError (签名错误)
```

### 异常类详解

#### KwaixiaodianSDKError

所有SDK异常的基类：

```python
from kwaixiaodian import KwaixiaodianSDKError

try:
    # SDK相关操作
    pass
except KwaixiaodianSDKError as e:
    print(f"SDK错误: {e}")
```

#### KwaixiaodianAPIError

API业务逻辑错误，包含详细的错误码和消息：

```python
from kwaixiaodian import KwaixiaodianAPIError

try:
    response = await client.order.list(...)
except KwaixiaodianAPIError as e:
    print(f"API错误码: {e.code}")
    print(f"错误消息: {e.message}")
    print(f"请求ID: {e.request_id}")
    print(f"响应详情: {e.response}")
```

常见API错误码：

| 错误码  | 说明         | 处理建议               |
| ------- | ------------ | ---------------------- |
| `40001` | 缺少必要参数 | 检查请求参数完整性     |
| `40002` | 参数格式错误 | 验证参数格式和类型     |
| `40003` | 权限不足     | 检查授权范围和令牌权限 |
| `40004` | 访问频率超限 | 实施请求限流和重试     |
| `50001` | 系统内部错误 | 稍后重试或联系技术支持 |

#### KwaixiaodianAuthError

认证相关错误：

```python
from kwaixiaodian import KwaixiaodianAuthError

try:
    response = await client.order.list(...)
except KwaixiaodianAuthError as e:
    if e.code == "INVALID_TOKEN":
        # 令牌无效，需要重新授权
        print("令牌无效，请重新授权")
    elif e.code == "TOKEN_EXPIRED":
        # 令牌过期，尝试刷新
        print("令牌过期，尝试刷新")
    elif e.code == "AUTHORIZATION_REVOKED":
        # 授权被撤销
        print("授权被撤销，需要重新授权")
```

#### KwaixiaodianNetworkError

网络连接错误：

```python
from kwaixiaodian import KwaixiaodianNetworkError

try:
    response = await client.order.list(...)
except KwaixiaodianNetworkError as e:
    print(f"网络错误: {e}")
    # 可以实施重试逻辑
```

#### KwaixiaodianSignatureError

签名验证错误：

```python
from kwaixiaodian import KwaixiaodianSignatureError

try:
    response = await client.order.list(...)
except KwaixiaodianSignatureError as e:
    print(f"签名错误: {e}")
    # 检查签名密钥和算法配置
```

## 错误处理最佳实践

### 1. 分层异常处理

```python
import asyncio
import logging
from kwaixiaodian import (
    AsyncKwaixiaodianClient,
    KwaixiaodianAPIError,
    KwaixiaodianAuthError,
    KwaixiaodianNetworkError,
    KwaixiaodianSignatureError
)

logger = logging.getLogger(__name__)

async def handle_order_query(client, access_token, seller_id):
    """处理订单查询，包含完整错误处理"""
    try:
        response = await client.order.list(
            access_token=access_token,
            seller_id=seller_id,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )

        return response.result

    except KwaixiaodianAuthError as e:
        logger.error(f"认证错误: {e.code} - {e.message}")
        if e.code == "TOKEN_EXPIRED":
            # 尝试刷新令牌
            raise TokenRefreshRequired()
        elif e.code == "AUTHORIZATION_REVOKED":
            # 需要重新授权
            raise ReauthorizationRequired()
        else:
            raise

    except KwaixiaodianAPIError as e:
        logger.error(f"API错误: {e.code} - {e.message}")
        if e.code == "40004":  # 频率限制
            # 实施退避重试
            await asyncio.sleep(1)
            raise RateLimitExceeded()
        elif e.code.startswith("50"):  # 服务器错误
            # 可以重试的错误
            raise RetryableError(str(e))
        else:
            # 客户端错误，不应重试
            raise

    except KwaixiaodianNetworkError as e:
        logger.error(f"网络错误: {e}")
        # 网络错误通常可以重试
        raise RetryableError(str(e))

    except KwaixiaodianSignatureError as e:
        logger.error(f"签名错误: {e}")
        # 签名错误通常是配置问题，不应重试
        raise ConfigurationError(str(e))

    except Exception as e:
        logger.error(f"未知错误: {e}")
        raise
```

### 2. 自动重试机制

```python
import asyncio
import random
from typing import Callable, Any

class RetryableError(Exception):
    pass

class ExponentialBackoffRetry:
    def __init__(self, max_retries=3, base_delay=1.0, max_delay=60.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay

    async def execute(self, func: Callable, *args, **kwargs) -> Any:
        """执行函数，遇到可重试错误时自动重试"""
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                return await func(*args, **kwargs)

            except (KwaixiaodianNetworkError, RetryableError) as e:
                last_exception = e

                if attempt < self.max_retries:
                    # 计算退避延迟
                    delay = min(
                        self.base_delay * (2 ** attempt) + random.uniform(0, 1),
                        self.max_delay
                    )

                    logger.warning(
                        f"第{attempt + 1}次尝试失败，{delay:.2f}秒后重试: {e}"
                    )
                    await asyncio.sleep(delay)
                else:
                    logger.error(f"重试{self.max_retries}次后仍然失败")

            except (KwaixiaodianAuthError, KwaixiaodianSignatureError, KwaixiaodianAPIError) as e:
                # 这些错误通常不应重试
                if isinstance(e, KwaixiaodianAPIError) and e.code.startswith("50"):
                    # 服务器错误可以重试
                    last_exception = e
                    continue
                else:
                    raise

        # 所有重试都失败
        raise last_exception

# 使用示例
retry_helper = ExponentialBackoffRetry(max_retries=3)

async def resilient_api_call():
    async def api_operation():
        async with AsyncKwaixiaodianClient(...) as client:
            return await handle_order_query(client, access_token, seller_id)

    try:
        return await retry_helper.execute(api_operation)
    except Exception as e:
        logger.error(f"API调用最终失败: {e}")
        raise
```

### 3. 令牌自动刷新

```python
class TokenManager:
    def __init__(self, oauth_client):
        self.oauth_client = oauth_client
        self.access_token = None
        self.refresh_token = None

    async def execute_with_auto_refresh(self, func, *args, **kwargs):
        """执行API调用，自动处理令牌刷新"""
        try:
            return await func(*args, **kwargs)

        except KwaixiaodianAuthError as e:
            if e.code == "TOKEN_EXPIRED" and self.refresh_token:
                logger.info("令牌过期，尝试刷新")

                try:
                    # 刷新令牌
                    token_response = await self.oauth_client.refresh_access_token(
                        refresh_token=self.refresh_token
                    )

                    self.access_token = token_response.access_token
                    self.refresh_token = token_response.refresh_token

                    # 更新函数参数中的访问令牌
                    if 'access_token' in kwargs:
                        kwargs['access_token'] = self.access_token

                    logger.info("令牌刷新成功，重试API调用")
                    return await func(*args, **kwargs)

                except Exception as refresh_error:
                    logger.error(f"令牌刷新失败: {refresh_error}")
                    raise ReauthorizationRequired() from refresh_error
            else:
                raise

# 使用示例
token_manager = TokenManager(oauth_client)

async def api_call_with_refresh():
    async def order_operation():
        async with AsyncKwaixiaodianClient(...) as client:
            return await client.order.list(
                access_token=token_manager.access_token,
                seller_id=seller_id,
                begin_time="2024-01-01T00:00:00",
                end_time="2024-01-31T23:59:59"
            )

    return await token_manager.execute_with_auto_refresh(order_operation)
```

### 4. 统一错误处理装饰器

```python
from functools import wraps
import asyncio

def handle_kuaishou_errors(max_retries=3, auto_refresh=True):
    """快手API错误处理装饰器"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            retry_count = 0

            while retry_count <= max_retries:
                try:
                    return await func(*args, **kwargs)

                except KwaixiaodianAuthError as e:
                    if auto_refresh and e.code == "TOKEN_EXPIRED":
                        # 尝试刷新令牌（需要实现token_manager）
                        logger.info("尝试刷新令牌")
                        # 刷新逻辑...
                        retry_count += 1
                        continue
                    else:
                        raise

                except KwaixiaodianNetworkError as e:
                    if retry_count < max_retries:
                        delay = 2 ** retry_count
                        logger.warning(f"网络错误，{delay}秒后重试: {e}")
                        await asyncio.sleep(delay)
                        retry_count += 1
                        continue
                    else:
                        raise

                except KwaixiaodianAPIError as e:
                    if e.code == "40004" and retry_count < max_retries:  # 频率限制
                        delay = 2 ** retry_count
                        logger.warning(f"频率限制，{delay}秒后重试")
                        await asyncio.sleep(delay)
                        retry_count += 1
                        continue
                    else:
                        raise

                except Exception as e:
                    logger.error(f"未知错误: {e}")
                    raise

            # 重试次数用完
            raise Exception(f"重试{max_retries}次后仍然失败")

        return wrapper
    return decorator

# 使用示例
@handle_kuaishou_errors(max_retries=3, auto_refresh=True)
async def get_orders():
    async with AsyncKwaixiaodianClient(...) as client:
        return await client.order.list(...)
```

## 日志记录

### 配置SDK日志

```python
import logging

# 配置SDK日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 调整SDK日志级别
kuaishou_logger = logging.getLogger('kwaixiaodian')
kuaishou_logger.setLevel(logging.DEBUG)

# 禁用敏感信息日志
sensitive_logger = logging.getLogger('kwaixiaodian.auth')
sensitive_logger.setLevel(logging.WARNING)
```

### 自定义错误日志

```python
import json
from datetime import datetime

class ErrorLogger:
    def __init__(self, log_file="kuaishou_errors.log"):
        self.log_file = log_file

    def log_error(self, error, context=None):
        """记录错误详情"""
        error_info = {
            "timestamp": datetime.now().isoformat(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context or {}
        }

        if isinstance(error, KwaixiaodianAPIError):
            error_info.update({
                "api_code": error.code,
                "api_message": error.message,
                "request_id": error.request_id
            })

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(error_info, ensure_ascii=False) + "\n")

# 使用示例
error_logger = ErrorLogger()

try:
    response = await client.order.list(...)
except KwaixiaodianAPIError as e:
    error_logger.log_error(e, {
        "function": "get_orders",
        "seller_id": seller_id,
        "access_token": access_token[:10] + "..."  # 部分隐藏
    })
    raise
```

## 监控和告警

### 错误率监控

```python
import time
from collections import defaultdict, deque

class ErrorMonitor:
    def __init__(self, window_size=300):  # 5分钟窗口
        self.window_size = window_size
        self.error_counts = defaultdict(deque)
        self.request_counts = deque()

    def record_request(self):
        """记录请求"""
        now = time.time()
        self.request_counts.append(now)
        self._cleanup_old_records(now)

    def record_error(self, error_type):
        """记录错误"""
        now = time.time()
        self.error_counts[error_type].append(now)
        self._cleanup_old_records(now)

    def _cleanup_old_records(self, now):
        """清理过期记录"""
        cutoff = now - self.window_size

        # 清理请求记录
        while self.request_counts and self.request_counts[0] < cutoff:
            self.request_counts.popleft()

        # 清理错误记录
        for error_type in list(self.error_counts.keys()):
            error_queue = self.error_counts[error_type]
            while error_queue and error_queue[0] < cutoff:
                error_queue.popleft()

    def get_error_rate(self, error_type=None):
        """获取错误率"""
        total_requests = len(self.request_counts)
        if total_requests == 0:
            return 0.0

        if error_type:
            error_count = len(self.error_counts[error_type])
        else:
            error_count = sum(len(queue) for queue in self.error_counts.values())

        return error_count / total_requests

    def should_alert(self, threshold=0.1):
        """检查是否应该告警"""
        return self.get_error_rate() > threshold

# 使用示例
monitor = ErrorMonitor()

async def monitored_api_call():
    monitor.record_request()

    try:
        result = await client.order.list(...)
        return result
    except Exception as e:
        monitor.record_error(type(e).__name__)

        if monitor.should_alert():
            # 发送告警
            send_alert(f"API错误率过高: {monitor.get_error_rate():.2%}")

        raise
```

## 总结

有效的错误处理是构建稳定应用的关键：

1. **理解异常层次** - 针对不同类型的错误采用不同的处理策略
2. **实施重试机制** - 对于瞬时错误自动重试
3. **令牌管理** - 自动处理令牌刷新和重新授权
4. **日志记录** - 记录详细的错误信息用于调试
5. **监控告警** - 实时监控错误率和异常模式
6. **优雅降级** - 在服务不可用时提供备选方案

通过遵循这些最佳实践，你可以构建出健壮且用户友好的应用程序。