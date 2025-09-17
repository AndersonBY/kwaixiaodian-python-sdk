# 订单服务

订单管理相关的API服务，包括订单查询、发货、状态更新等功能。

## 异步订单服务

::: kwaixiaodian.client.services.order.AsyncOrderService
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

## 同步订单服务

::: kwaixiaodian.client.services.order.SyncOrderService
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

## 订单数据模型

::: kwaixiaodian.models.order
    options:
      show_source: false
      show_bases: true
      heading_level: 3
      members_order: source
      group_by_category: true
      show_category_heading: true
      filters:
        - "!^_"
        - "!^__"
      summary: true