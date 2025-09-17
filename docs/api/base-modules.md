# 基础模块

SDK的核心基础组件和通用模块，提供异常处理机制、基础数据模型定义、通用数据结构等核心功能。这些模块为整个SDK的稳定运行提供基础支撑，确保API调用的可靠性和数据的一致性。

## 异常处理

::: kwaixiaodian.exceptions
    options:
      show_source: true
      show_bases: true
      heading_level: 3
      members_order: source
      group_by_category: true
      show_category_heading: true
      show_root_heading: true
      show_object_full_path: false
      summary: true

## 基础数据模型

::: kwaixiaodian.models.base
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

## 通用数据模型

::: kwaixiaodian.models.common
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