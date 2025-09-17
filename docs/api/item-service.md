# 商品服务

商品管理相关的API服务，包括商品CRUD、库存管理、规格管理等功能。

## 异步商品服务

::: kwaixiaodian.client.services.item.AsyncItemService
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

## 同步商品服务

::: kwaixiaodian.client.services.item.SyncItemService
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

## 商品数据模型

::: kwaixiaodian.models.item
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