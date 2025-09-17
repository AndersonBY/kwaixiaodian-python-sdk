# 发票服务

快手小店发票管理API，提供完整的电子发票处理功能。支持发票申请、发票查询、发票下载、发票状态管理、发票模板配置等核心功能，帮助商家规范化处理发票业务。

## 异步发票服务

::: kwaixiaodian.client.services.invoice.AsyncInvoiceService
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

## 同步发票服务

::: kwaixiaodian.client.services.invoice.SyncInvoiceService
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

## 发票数据模型

::: kwaixiaodian.models.invoice
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