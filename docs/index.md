# 快手小店 Python SDK

[![PyPI version](https://badge.fury.io/py/kwaixiaodian.svg)](https://badge.fury.io/py/kwaixiaodian)
[![Python Support](https://img.shields.io/pypi/pyversions/kwaixiaodian.svg)](https://pypi.org/project/kwaixiaodian/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

快手小店开放平台的现代化Python SDK，提供完整的异步API支持。

## ✨ 主要特性

- **🚀 异步优先** - 基于 `httpx` 的高性能异步HTTP客户端
- **🔐 完整认证** - 支持OAuth 2.0认证流程和签名验证
- **📦 全面覆盖** - 支持896个官方API接口，涵盖25个业务领域
- **🎯 类型安全** - 基于Pydantic v2的完整类型注解和数据验证
- **⚡ 高性能** - 连接池、自动重试、并发请求支持
- **📚 完整文档** - 详细的API文档和丰富的使用示例

## 🚀 快速开始

### 安装

```bash
pip install kwaixiaodian
```

### 基础使用

```python
import asyncio
from kwaixiaodian import KwaixiaodianClient

async def main():
    async with KwaixiaodianClient(
        app_key="your_app_key",
        app_secret="your_app_secret", 
        sign_secret="your_sign_secret"
    ) as client:
        # 获取订单列表
        orders = await client.order.list(
            access_token="your_token",
            seller_id=123456,
            begin_time="2024-01-01T00:00:00",
            end_time="2024-01-31T23:59:59"
        )
        
        print(f"找到 {len(orders.result)} 个订单")

asyncio.run(main())
```

## 📖 文档导航

- [快速开始](quickstart.md) - 5分钟上手指南
- [API参考](api-reference.md) - 完整API文档
- [认证指南](authentication.md) - OAuth配置详解
- [最佳实践](best-practices.md) - 生产环境建议
- [示例代码](examples.md) - 丰富的代码示例

## 🤝 社区支持

- **GitHub Issues**: [报告问题](https://github.com/AndersonBY/kwaixiaodian-python-sdk/issues)
- **邮件支持**: support@kwaixiaodian.com
- **文档网站**: [在线文档](https://kwaixiaodian-python-sdk.readthedocs.io)

## 📄 许可证

本项目采用 [MIT License](https://github.com/AndersonBY/kwaixiaodian-python-sdk/blob/main/LICENSE) 许可证。