# 分销服务

分销相关的API服务，包含分销主服务（聚合各子服务能力）以及其余核心接口。

子服务页面（完整接口文档）：

- [CPS 子服务](distribution-cps.md)
- [投资活动 子服务](distribution-investment.md)
- [卖家活动 子服务](distribution-seller.md)
- [二级分销 子服务](distribution-second.md)

> 说明：为避免文档冗长，以下主服务文档隐藏了大部分“委托方法”（即简单转发到子服务的方法）。
> 如需查看完整子服务接口，请参考源码中的 `kwaixiaodian.client.services.distribution.*` 模块。

## 异步分销服务

::: kwaixiaodian.client.services.distribution.main.AsyncDistributionService
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
      filters:
        # 隐藏委托到 CPS 子服务的方法
        - "!^get_cps_.*"
        - "!^create_cps_.*"
        - "!^update_cps_.*"
        - "!^query_cps_.*"
        - "!^parse_cps_.*"
        - "!^transfer_cps_.*"
        # 隐藏委托到 Investment 子服务的方法
        - "!^get_investment_.*"
        - "!^create_investment_.*"
        - "!^audit_investment_.*"
        - "!^delete_investment_.*"
        - "!^close_investment_.*"
        - "!^query_investment_.*"
        - "!^adjust_investment_.*"
        # 隐藏委托到 Seller 子服务的方法
        - "!^get_seller_.*"
        - "!^cancel_seller_.*"
        - "!^apply_seller_.*"
        - "!^query_seller_.*"
        # 隐藏委托到 Second 子服务的方法
        - "!^get_second_.*"
        - "!^apply_again_second_.*"
        - "!^apply_second_.*"
        - "!^edit_apply_second_.*"
        - "!^cancel_second_.*"
        - "!^handle_second_.*"

## 同步分销服务

::: kwaixiaodian.client.services.distribution.main.SyncDistributionService
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
      filters:
        # 隐藏委托到 CPS 子服务的方法
        - "!^get_cps_.*"
        - "!^create_cps_.*"
        - "!^update_cps_.*"
        - "!^query_cps_.*"
        - "!^parse_cps_.*"
        - "!^transfer_cps_.*"
        # 隐藏委托到 Investment 子服务的方法
        - "!^get_investment_.*"
        - "!^create_investment_.*"
        - "!^audit_investment_.*"
        - "!^delete_investment_.*"
        - "!^close_investment_.*"
        - "!^query_investment_.*"
        - "!^adjust_investment_.*"
        # 隐藏委托到 Seller 子服务的方法
        - "!^get_seller_.*"
        - "!^cancel_seller_.*"
        - "!^apply_seller_.*"
        - "!^query_seller_.*"
        # 隐藏委托到 Second 子服务的方法
        - "!^get_second_.*"
        - "!^apply_again_second_.*"
        - "!^apply_second_.*"
        - "!^edit_apply_second_.*"
        - "!^cancel_second_.*"
        - "!^handle_second_.*"
