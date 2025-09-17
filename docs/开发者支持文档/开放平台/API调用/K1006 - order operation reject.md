# K1006 - order operation reject

> **文档ID**: 53513  
> **页面标识**: 965270fd6dd34b36725789d755c9098f1631504421466  
> **更新时间**: 1631517552302  
> **浏览量**: 9630

---

#### 问题分类：

API调用类-订单API- 订单详情

#### 问题现象：

https://open.kwaixiaodian.com/open/seller/order/detail?method=open.seller.order.detail&version=1&signMethod=MD5&appkey=\*\*\*&access\_token=\*\*\*\*\*&timestamp=\*\*&param=\*\*\*&sign=\*\*\*

{"result":21,"error\_msg":"order operation reject","requestId":"\*\*\*\*\*\*"}

#### 问题原因：

原因为查询的订单所属商家与授权token所在商家并非同一商家

#### 解决方案：

服务商方：可以通过开放平台-支持工具/常用工具/授权查询工具/access token 信息查询页面，输入access token，点击查询获取token相关信息；除openid外还可以获取token是否到期，token所有scope等

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1631517382521.png)

商家方：登陆对应openid商家后台，确认订单列表可以搜索到对应订单

通过工单反馈发现存在另一种情况：授权商家为达人身份，此时请调用好物联盟API获取相关订单信息

#### 关键字：

获取订单详情报错

order operation reject

查不到订单
