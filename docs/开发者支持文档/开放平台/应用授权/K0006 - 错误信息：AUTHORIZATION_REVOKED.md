# K0006 - 错误信息：AUTHORIZATION_REVOKED

> **文档ID**: 401079  
> **页面标识**: b364ea3121bf4524118721248de7fb911618307135717  
> **更新时间**: 1697444754877  
> **浏览量**: 9944

---

#### 问题分类：

API调用类-订单API-发货

#### 问题现象：

请求发货接口时返回错误信息：AUTHORIZATION\_REVOKED

<https://open.kwaixiaodian.com/open/seller/order/goods/deliver>

param":"{\"orderId\":\*\*\*\*,\"expressNo\":\*\*\*\*\*,\"expressCode\":\*\*}",

"appkey":"ks\*\*\*\*",

"timestamp":1617245975,

"access\_token":\*\*\*,

"version":1,

"method":"open.seller.order.goods.deliver",

"signMethod":"MD5",

"sign":\*\*\*;

错误信息：**{"result":24,"error\_msg":"AUTHORIZATION\_REVOKED"}"**

#### 问题原因：

该报错的原因为：用户取消了对应用的授权

产生报错的操作包括：用户主动取消了对应用的授权、测试用户10天授权有效期到期自动取消对应用的授权授权、用户订购了该应用对应的服务市场服务到期

如需确认具体取消授权时间，请使用[常用工具-授权查询工具](https://open.kwaixiaodian.com/zone/tool/auth/access)自助查询

#### 解决方案：

请与商家确认并让重新对应用授权，完成授权后重新获取token并再次调用API

#### 关键字：

发货

24

AUTHORIZATION\_REVOKED
