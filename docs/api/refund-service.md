# 售后服务

快手小店售后服务API，提供完整的退款退货处理功能。支持退款申请、退货处理、售后订单查询、争议处理等核心业务场景，帮助商家高效处理售后相关事务。

## 异步售后服务

::: kwaixiaodian.client.services.refund.AsyncRefundService
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

## 同步售后服务

::: kwaixiaodian.client.services.refund.SyncRefundService
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

## 售后数据模型

::: kwaixiaodian.models.refund
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