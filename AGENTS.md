# Repository Guidelines

## 项目目标与参考来源
- 以 `java_sdk_reference/` 与 `docs/` 的 API 文档为唯一业务真源；不得实现未在 Java 参考或文档中出现的“猜测接口”。
- 设计与架构遵循 `CLAUDE.md`（async‑first、类型安全、服务分层）；本文件补充贡献流程与规范。

## 项目结构与模块组织
- `src/kwaixiaodian/` — 核心包：`client/`、`auth/`、`http/`、`models/`、`utils/`、`services/`。
- `tests/` — pytest 测试（含 `pytest-asyncio`），文件命名 `test_*.py`。
- `examples/` — 可运行示例；演示同步/异步与常见场景。
- `docs/` — MkDocs 文档；增删 API 必须同步更新文档。
- `java_sdk_reference/` — Java 参考实现；按域映射到 Python services/models。

## 开发、构建与测试命令
- 安装：`pip install pdm` 与 `pdm install`
- 质量：`pdm run format`、`pdm run lint`、`pdm run typecheck`
- 测试：`pdm run test`（覆盖率≥90%），`pdm run test-fast`
- 文档：`pdm run docs`（本地预览），`pdm run build-docs`
- 清理：`pdm run clean`

## 代码风格与命名约定
- Python 3.8+；4 空格缩进；行宽 88；Ruff 负责格式化/排序/检查。
- 全量类型标注；公共 API 提供类型与文档字符串（Pydantic v2 模型）。
- 命名：模块/函数 `snake_case`，类 `PascalCase`，常量 `UPPER_SNAKE_CASE`。
- 映射规则：Java `OrderService.listOrders` → Python `order.list`；Java POJO → `models/order.py` 中的 Pydantic 模型，字段名遵循 API 文档。

## 测试规范
- 使用 `pytest`、`pytest-asyncio`、`respx`；覆盖率门线 90%（配置已强制）。
- 标记：`@pytest.mark.unit` / `@pytest.mark.integration`；避免手动事件循环管理。
- 每个新增/变更 API：补充正向与错误路径测试，必要时添加示例。

## 提交与 Pull Request
- 提交信息：祈使句、主题 ≤72 字符；正文说明「为何」，并链接 Issue（如 `Fixes #123`）。
- PR 必须：描述清晰、范围聚焦、链接所依据的 `java_sdk_reference/` 文件与 `docs/` 页面、更新 `docs/` 与 `examples/`、所有检查通过。
- 推送前本地运行：`pdm run format lint typecheck test`。

## 安全与其他
- 禁止提交密钥/证书；示例用环境变量占位并注意日志脱敏。
- 变更小而聚焦；避免无关重构。新增域/端点需同时补全 models、services、docs、示例。
