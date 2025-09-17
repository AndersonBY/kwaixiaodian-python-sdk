# 最佳实践

本指南总结了使用快手小店Python SDK的最佳实践，帮助你构建稳定、高效、安全的应用程序。

## 客户端配置

### 1. 连接池配置

```python
from kwaixiaodian import AsyncKwaixiaodianClient
from kwaixiaodian.http import HTTPConfig

# 生产环境推荐配置
http_config = HTTPConfig(
    timeout=30.0,  # 30秒超时
    max_connections=100,  # 最大连接数
    max_keepalive_connections=20,  # 保持连接数
    keepalive_expiry=30.0  # 连接保持时间
)

async with AsyncKwaixiaodianClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    sign_secret="your_sign_secret",
    http_config=http_config
) as client:
    # 使用配置优化的客户端
    pass
```

### 2. 重试策略配置

```python
from kwaixiaodian.http import RetryConfig

# 自定义重试配置
retry_config = RetryConfig(
    max_retries=3,  # 最大重试次数
    backoff_factor=0.5,  # 退避因子
    status_codes=[429, 500, 502, 503, 504],  # 重试的HTTP状态码
    max_backoff=30.0  # 最大退避时间
)

async with AsyncKwaixiaodianClient(
    # ... 其他配置
    retry_config=retry_config
) as client:
    pass
```

### 3. 环境配置管理

```python
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class KuaishouConfig:
    app_key: str
    app_secret: str
    sign_secret: str
    base_url: Optional[str] = None
    timeout: float = 30.0
    max_connections: int = 100

    @classmethod
    def from_env(cls):
        """从环境变量创建配置"""
        return cls(
            app_key=os.environ["KUAISHOU_APP_KEY"],
            app_secret=os.environ["KUAISHOU_APP_SECRET"],
            sign_secret=os.environ["KUAISHOU_SIGN_SECRET"],
            base_url=os.environ.get("KUAISHOU_BASE_URL"),
            timeout=float(os.environ.get("KUAISHOU_TIMEOUT", "30.0")),
            max_connections=int(os.environ.get("KUAISHOU_MAX_CONNECTIONS", "100"))
        )

    def create_client(self):
        """创建客户端实例"""
        http_config = HTTPConfig(
            timeout=self.timeout,
            max_connections=self.max_connections,
            base_url=self.base_url
        )

        return AsyncKwaixiaodianClient(
            app_key=self.app_key,
            app_secret=self.app_secret,
            sign_secret=self.sign_secret,
            http_config=http_config
        )

# 使用示例
config = KuaishouConfig.from_env()
async with config.create_client() as client:
    pass
```

## 性能优化

### 1. 并发请求处理

```python
import asyncio
from typing import List, Dict, Any

async def batch_order_query(
    client: AsyncKwaixiaodianClient,
    access_token: str,
    seller_ids: List[int],
    begin_time: str,
    end_time: str
) -> Dict[int, List[Any]]:
    """并发查询多个商家的订单"""

    async def query_seller_orders(seller_id: int):
        try:
            response = await client.order.list(
                access_token=access_token,
                seller_id=seller_id,
                begin_time=begin_time,
                end_time=end_time
            )
            return seller_id, response.result
        except Exception as e:
            logger.error(f"查询商家{seller_id}订单失败: {e}")
            return seller_id, []

    # 并发执行查询
    tasks = [query_seller_orders(seller_id) for seller_id in seller_ids]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # 处理结果
    order_data = {}
    for result in results:
        if isinstance(result, Exception):
            logger.error(f"批量查询出错: {result}")
            continue

        seller_id, orders = result
        order_data[seller_id] = orders

    return order_data

# 使用示例
async def main():
    async with AsyncKwaixiaodianClient(...) as client:
        seller_ids = [123456, 123457, 123458]
        orders = await batch_order_query(
            client, access_token, seller_ids,
            "2024-01-01T00:00:00", "2024-01-31T23:59:59"
        )
```

### 2. 分页数据批量处理

```python
from typing import AsyncGenerator, Any

async def get_all_orders(
    client: AsyncKwaixiaodianClient,
    access_token: str,
    seller_id: int,
    begin_time: str,
    end_time: str,
    page_size: int = 100
) -> AsyncGenerator[Any, None]:
    """分页获取所有订单数据"""
    page = 1

    while True:
        try:
            response = await client.order.list(
                access_token=access_token,
                seller_id=seller_id,
                begin_time=begin_time,
                end_time=end_time,
                page=page,
                size=page_size
            )

            if not response.result:
                break

            for order in response.result:
                yield order

            # 检查是否还有更多数据
            if len(response.result) < page_size:
                break

            page += 1

        except Exception as e:
            logger.error(f"获取第{page}页数据失败: {e}")
            break

# 使用示例
async def process_all_orders():
    async with AsyncKwaixiaodianClient(...) as client:
        order_count = 0

        async for order in get_all_orders(
            client, access_token, seller_id,
            "2024-01-01T00:00:00", "2024-01-31T23:59:59"
        ):
            # 处理每个订单
            await process_order(order)
            order_count += 1

            if order_count % 1000 == 0:
                logger.info(f"已处理 {order_count} 个订单")
```

### 3. 连接复用

```python
class KuaishouClientManager:
    """客户端连接管理器"""

    def __init__(self, config: KuaishouConfig):
        self.config = config
        self._client = None

    async def __aenter__(self):
        self._client = self.config.create_client()
        await self._client.__aenter__()
        return self._client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.__aexit__(exc_type, exc_val, exc_tb)

# 在应用生命周期内复用连接
class OrderService:
    def __init__(self, client_manager: KuaishouClientManager):
        self.client_manager = client_manager

    async def get_orders(self, access_token: str, seller_id: int):
        async with self.client_manager as client:
            return await client.order.list(
                access_token=access_token,
                seller_id=seller_id,
                begin_time="2024-01-01T00:00:00",
                end_time="2024-01-31T23:59:59"
            )

    async def ship_order(self, access_token: str, seller_id: int, order_id: str):
        async with self.client_manager as client:
            return await client.logistics.ship(
                access_token=access_token,
                seller_id=seller_id,
                order_id=order_id,
                logistics_id=1,
                waybill_code="SF1234567890"
            )
```

## 安全实践

### 1. 敏感信息处理

```python
import hashlib
import logging

class SensitiveDataFilter(logging.Filter):
    """过滤日志中的敏感信息"""

    SENSITIVE_FIELDS = ['access_token', 'app_secret', 'sign_secret', 'refresh_token']

    def filter(self, record):
        if hasattr(record, 'msg'):
            for field in self.SENSITIVE_FIELDS:
                if field in str(record.msg):
                    # 用星号替换敏感信息
                    record.msg = str(record.msg).replace(
                        getattr(record, field, ''),
                        '*' * 8
                    )
        return True

# 配置日志过滤器
logger = logging.getLogger('kwaixiaodian')
logger.addFilter(SensitiveDataFilter())

def mask_sensitive_data(data: str, show_prefix: int = 4) -> str:
    """遮掩敏感数据"""
    if len(data) <= show_prefix:
        return '*' * len(data)
    return data[:show_prefix] + '*' * (len(data) - show_prefix)

# 使用示例
masked_token = mask_sensitive_data(access_token)
logger.info(f"使用令牌: {masked_token}")
```

### 2. 请求签名验证

```python
import hmac
import hashlib
import time
from urllib.parse import urlencode

def verify_webhook_signature(
    payload: bytes,
    signature: str,
    secret: str,
    timestamp: str,
    tolerance: int = 300
) -> bool:
    """验证webhook签名"""

    # 检查时间戳
    try:
        request_time = int(timestamp)
        current_time = int(time.time())

        if abs(current_time - request_time) > tolerance:
            return False
    except ValueError:
        return False

    # 构建签名字符串
    sign_string = f"{timestamp}.{payload.decode('utf-8')}"

    # 计算期望签名
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        sign_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    # 安全比较
    return hmac.compare_digest(signature, expected_signature)

# 在webhook处理中使用
def handle_webhook(request):
    payload = request.body
    signature = request.headers.get('X-Kuaishou-Signature')
    timestamp = request.headers.get('X-Kuaishou-Timestamp')

    if not verify_webhook_signature(payload, signature, webhook_secret, timestamp):
        return {"error": "Invalid signature"}, 401

    # 处理webhook
    return {"status": "ok"}, 200
```

### 3. 访问控制

```python
import jwt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

class AccessTokenManager:
    """访问令牌管理器"""

    def __init__(self, secret: str):
        self.secret = secret

    def create_token(self, user_id: str, permissions: list, expires_in: int = 3600) -> str:
        """创建内部访问令牌"""
        payload = {
            'user_id': user_id,
            'permissions': permissions,
            'exp': datetime.utcnow() + timedelta(seconds=expires_in),
            'iat': datetime.utcnow()
        }

        return jwt.encode(payload, self.secret, algorithm='HS256')

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """验证令牌"""
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def check_permission(self, token: str, required_permission: str) -> bool:
        """检查权限"""
        payload = self.verify_token(token)
        if not payload:
            return False

        permissions = payload.get('permissions', [])
        return required_permission in permissions

# 权限装饰器
def require_permission(permission: str):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            # 从请求中获取令牌
            token = kwargs.get('internal_token')
            if not token_manager.check_permission(token, permission):
                raise PermissionError(f"需要权限: {permission}")

            return await func(*args, **kwargs)
        return wrapper
    return decorator

# 使用示例
@require_permission('order:read')
async def get_orders(access_token: str, seller_id: int, internal_token: str):
    async with AsyncKwaixiaodianClient(...) as client:
        return await client.order.list(
            access_token=access_token,
            seller_id=seller_id,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )
```

## 监控和观测

### 1. 性能监控

```python
import time
import asyncio
from functools import wraps
from typing import Dict, List
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class MetricData:
    count: int = 0
    total_time: float = 0.0
    errors: int = 0

class PerformanceMonitor:
    """性能监控器"""

    def __init__(self):
        self.metrics: Dict[str, MetricData] = defaultdict(MetricData)

    def record_request(self, endpoint: str, duration: float, success: bool = True):
        """记录请求指标"""
        metric = self.metrics[endpoint]
        metric.count += 1
        metric.total_time += duration

        if not success:
            metric.errors += 1

    def get_stats(self, endpoint: str = None) -> Dict[str, Any]:
        """获取统计信息"""
        if endpoint:
            metric = self.metrics[endpoint]
            avg_time = metric.total_time / metric.count if metric.count > 0 else 0
            error_rate = metric.errors / metric.count if metric.count > 0 else 0

            return {
                'endpoint': endpoint,
                'count': metric.count,
                'avg_time': avg_time,
                'error_rate': error_rate
            }
        else:
            return {
                endpoint: self.get_stats(endpoint)
                for endpoint in self.metrics.keys()
            }

# 性能监控装饰器
monitor = PerformanceMonitor()

def monitor_performance(endpoint: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            success = True

            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                raise
            finally:
                duration = time.time() - start_time
                monitor.record_request(endpoint, duration, success)

        return wrapper
    return decorator

# 使用示例
@monitor_performance('order.list')
async def get_orders():
    async with AsyncKwaixiaodianClient(...) as client:
        return await client.order.list(...)

# 定期输出统计信息
async def report_stats():
    while True:
        await asyncio.sleep(60)  # 每分钟报告一次
        stats = monitor.get_stats()
        logger.info(f"性能统计: {stats}")
```

### 2. 健康检查

```python
import asyncio
from enum import Enum
from typing import Dict, Any

class HealthStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

class HealthChecker:
    """健康检查器"""

    def __init__(self, client: AsyncKwaixiaodianClient):
        self.client = client

    async def check_api_connectivity(self) -> Dict[str, Any]:
        """检查API连通性"""
        try:
            start_time = time.time()

            # 尝试调用一个轻量级API
            await self.client.shop.get_shop_info(
                access_token="test_token",  # 测试令牌
                seller_id=1
            )

            duration = time.time() - start_time

            return {
                'status': HealthStatus.HEALTHY.value,
                'response_time': duration,
                'message': 'API连接正常'
            }

        except KwaixiaodianNetworkError:
            return {
                'status': HealthStatus.UNHEALTHY.value,
                'message': '网络连接失败'
            }
        except KwaixiaodianAuthError:
            # 认证错误说明连接正常，只是令牌问题
            return {
                'status': HealthStatus.DEGRADED.value,
                'message': '连接正常，但认证失败'
            }
        except Exception as e:
            return {
                'status': HealthStatus.UNHEALTHY.value,
                'message': f'未知错误: {str(e)}'
            }

    async def comprehensive_health_check(self) -> Dict[str, Any]:
        """综合健康检查"""
        checks = {}

        # API连通性检查
        checks['api_connectivity'] = await self.check_api_connectivity()

        # 连接池状态检查
        if hasattr(self.client._http_client, '_pool'):
            pool = self.client._http_client._pool
            checks['connection_pool'] = {
                'status': HealthStatus.HEALTHY.value,
                'active_connections': len(getattr(pool, '_connections', [])),
                'message': '连接池正常'
            }

        # 确定整体状态
        statuses = [check['status'] for check in checks.values()]
        if any(status == HealthStatus.UNHEALTHY.value for status in statuses):
            overall_status = HealthStatus.UNHEALTHY.value
        elif any(status == HealthStatus.DEGRADED.value for status in statuses):
            overall_status = HealthStatus.DEGRADED.value
        else:
            overall_status = HealthStatus.HEALTHY.value

        return {
            'overall_status': overall_status,
            'checks': checks,
            'timestamp': datetime.now().isoformat()
        }

# Web框架健康检查端点示例（FastAPI）
from fastapi import FastAPI

app = FastAPI()
health_checker = HealthChecker(client)

@app.get("/health")
async def health_check():
    return await health_checker.comprehensive_health_check()
```

## 测试策略

### 1. 单元测试

```python
import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock
from kwaixiaodian import AsyncKwaixiaodianClient, KwaixiaodianAPIError

@pytest.fixture
async def mock_client():
    """模拟客户端"""
    client = AsyncMock(spec=AsyncKwaixiaodianClient)
    return client

@pytest.mark.asyncio
async def test_order_query_success(mock_client):
    """测试订单查询成功场景"""
    # 设置模拟响应
    mock_response = MagicMock()
    mock_response.result = [
        MagicMock(order_id="123", order_status="PAID"),
        MagicMock(order_id="124", order_status="SHIPPED")
    ]
    mock_client.order.list.return_value = mock_response

    # 执行测试
    orders = await get_orders_service(mock_client, "token", 12345)

    # 验证结果
    assert len(orders) == 2
    assert orders[0].order_id == "123"
    mock_client.order.list.assert_called_once()

@pytest.mark.asyncio
async def test_order_query_api_error(mock_client):
    """测试API错误场景"""
    # 设置模拟异常
    mock_client.order.list.side_effect = KwaixiaodianAPIError(
        code="40001",
        message="参数错误",
        request_id="req-123"
    )

    # 验证异常抛出
    with pytest.raises(KwaixiaodianAPIError) as exc_info:
        await get_orders_service(mock_client, "token", 12345)

    assert exc_info.value.code == "40001"

async def get_orders_service(client, access_token, seller_id):
    """被测试的服务函数"""
    response = await client.order.list(
        access_token=access_token,
        seller_id=seller_id,
        begin_time="2024-01-01T00:00:00",
        end_time="2024-01-31T23:59:59"
    )
    return response.result
```

### 2. 集成测试

```python
import os
import pytest
from kwaixiaodian import AsyncKwaixiaodianClient

@pytest.mark.integration
@pytest.mark.asyncio
async def test_real_api_integration():
    """真实API集成测试"""
    # 仅在有真实凭证时运行
    if not all([
        os.getenv("KUAISHOU_APP_KEY"),
        os.getenv("KUAISHOU_APP_SECRET"),
        os.getenv("KUAISHOU_SIGN_SECRET"),
        os.getenv("KUAISHOU_ACCESS_TOKEN")
    ]):
        pytest.skip("缺少真实API凭证")

    async with AsyncKwaixiaodianClient(
        app_key=os.getenv("KUAISHOU_APP_KEY"),
        app_secret=os.getenv("KUAISHOU_APP_SECRET"),
        sign_secret=os.getenv("KUAISHOU_SIGN_SECRET")
    ) as client:

        # 执行真实API调用
        response = await client.order.list(
            access_token=os.getenv("KUAISHOU_ACCESS_TOKEN"),
            seller_id=int(os.getenv("KUAISHOU_SELLER_ID")),
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-01T23:59:59"
        )

        # 验证响应结构
        assert hasattr(response, 'result')
        assert hasattr(response, 'code')
        assert response.code == 1  # 成功响应
```

### 3. 性能测试

```python
import asyncio
import time
import statistics
from typing import List

async def performance_test_concurrent_requests():
    """并发请求性能测试"""

    async def single_request():
        start = time.time()
        async with AsyncKwaixiaodianClient(...) as client:
            await client.order.list(...)
        return time.time() - start

    # 测试不同并发级别
    concurrency_levels = [1, 5, 10, 20, 50]
    results = {}

    for concurrency in concurrency_levels:
        print(f"测试并发级别: {concurrency}")

        tasks = [single_request() for _ in range(concurrency)]
        durations = await asyncio.gather(*tasks)

        results[concurrency] = {
            'mean': statistics.mean(durations),
            'median': statistics.median(durations),
            'p95': sorted(durations)[int(0.95 * len(durations))],
            'p99': sorted(durations)[int(0.99 * len(durations))]
        }

    return results

# 运行性能测试
if __name__ == "__main__":
    results = asyncio.run(performance_test_concurrent_requests())
    for concurrency, stats in results.items():
        print(f"并发{concurrency}: 平均{stats['mean']:.3f}s, "
              f"P95={stats['p95']:.3f}s")
```

## 部署考虑

### 1. 容器化配置

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 设置环境变量
ENV PYTHONPATH=/app
ENV KUAISHOU_LOG_LEVEL=INFO

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import asyncio; from app.health import health_check; asyncio.run(health_check())"

CMD ["python", "-m", "app.main"]
```

### 2. Kubernetes部署

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kuaishou-api-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: kuaishou-api-service
  template:
    metadata:
      labels:
        app: kuaishou-api-service
    spec:
      containers:
      - name: api
        image: kuaishou-api:latest
        ports:
        - containerPort: 8000
        env:
        - name: KUAISHOU_APP_KEY
          valueFrom:
            secretKeyRef:
              name: kuaishou-secrets
              key: app-key
        - name: KUAISHOU_APP_SECRET
          valueFrom:
            secretKeyRef:
              name: kuaishou-secrets
              key: app-secret
        - name: KUAISHOU_SIGN_SECRET
          valueFrom:
            secretKeyRef:
              name: kuaishou-secrets
              key: sign-secret
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

## 总结

遵循这些最佳实践可以帮助你：

1. **提高性能** - 合理配置连接池和并发处理
2. **增强安全性** - 保护敏感信息和实施访问控制
3. **提升可观测性** - 监控性能和健康状态
4. **确保质量** - 完善的测试策略
5. **简化部署** - 容器化和云原生部署

记住，最佳实践会随着应用的发展而演进，定期审查和更新你的实践是很重要的。