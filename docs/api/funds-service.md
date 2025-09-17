# 资金服务

快手小店资金管理API，提供完整的财务处理功能。支持账户余额查询、资金流水查询、提现管理、账单下载、保证金管理等核心功能，帮助商家全面掌控资金状况和财务流水。

## 异步资金服务

::: kwaixiaodian.client.services.funds.AsyncFundsService
    options:
      show_source: false
      show_bases: true
      heading_level: 3
      members_order: source
      group_by_category: true
      show_category_heading: true
      show_root_heading: true
      show_object_full_path: false
      summary: true

## 同步资金服务

::: kwaixiaodian.client.services.funds.SyncFundsService
    options:
      show_source: false
      show_bases: true
      heading_level: 3
      members_order: source
      group_by_category: true
      show_category_heading: true
      show_root_heading: true
      show_object_full_path: false
      summary: true

## 资金数据模型

::: kwaixiaodian.models.funds
    options:
      show_source: false
      show_bases: true
      heading_level: 3
      members_order: source
      group_by_category: true
      show_category_heading: true
      show_root_heading: true
      show_object_full_path: false
      summary: true
      filters: ["!^_", "!^__"]