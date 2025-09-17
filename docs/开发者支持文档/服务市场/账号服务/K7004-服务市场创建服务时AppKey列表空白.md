# K7004-服务市场创建服务时AppKey列表空白

> **文档ID**: 401743  
> **页面标识**: 12281831b8e9b85e177012be52f5ed2b1635926531026  
> **更新时间**: 1724740868472  
> **浏览量**: 2355

---

#### 问题分类：

服务市场-创建服务

#### 问题现象：

服务市场创建服务时，appkey打开无选项

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1636007826624.png)

#### 

#### 问题原因：

可能有以下四个原因

**1、确认服务市场绑定的开发者账号邮箱和应用所属开放平台账号邮箱是否一致**

进入服务市场服务商后台-资质管理-店铺信息，查看开发者账号关联的邮箱是否已经绑定

（1）若未绑定，请登录到开放平台-[应用中心](https://open.kwaixiaodian.com/console/zone/new/home/application/appList)，确认应用appKey已存在，进入到账户中心-[基本信息](https://open.kwaixiaodian.com/console/zone/new/home/info/basic/basicInfo)确认当前的开发者账号的关联邮箱，并进行绑定验证；

（2）若已绑定，请使用邮箱所属的开发者账号登录开放平台，再开放平台-[应用中心](https://open.kwaixiaodian.com/console/zone/new/home/application/appList)中确认账号下是否有所需appKey。

**![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683863834216.png)**

上图中服务商管理后台-资质管理-[店铺信息](https://fuwu.kwaixiaodian.com/shop)中的开发者账号邮箱，下图中应用所属的开放平台控制台-个人中心-账户中心-[基本信息](https://open.kwaixiaodian.com/console/zone/new/home/info/basic/basicInfo)中的邮箱，需要两者保持一致

**![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683871218190.png)**

**2、确认开放平台和服务市场认证的公司名称及统一社会信用码一致**

开放平台：个人中心-企业信息

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683863174187.png)

服务市场：服务商控制台-资质管理-企业信息

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683863430297.png)

**3、确认关联的开发者账号为第三方开发者**

只有开放平台第三方开发者类型及该类型下的三方类目应用，才可以在服务市场上架服务

**![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683863583019.png)**

第三方类型应用才可以进行上架

**![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683864201504.png)**

**4、确认开放平台的应用类目与服务市场的服务类目一致**

**![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1683863583019.png)**

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1636007888125.png)

#### 解决方案：

首先校验一致性

1、服务市场账号下关联的开发者邮箱，和应用appKey所属的开发者账号邮箱一致；

2、服务市场的企业资质主体和开发者账号的企业资质主体一致（账号入驻时绑定的企业资质主体提交后不可以进行更改）；

3、服务市场创建服务的类目，和应用appKey的类目一致（应用创建后类目不可更改）；

4、确认开放平台应用类目为第三方类目，且状态为已上线；

5、仅第三方开发者创建的应用可以上架到服务市场。

若不一致，解决方案如下

1、如存在不一致情况请重新注册相同信息账号，如存在困难，请提工单说明具体情况，我们评估是否有有效途径解决；

2、商家后台应用无法上架到服务市场，需要删除原有应用并将开放平台账号修改第三方开发者类型，再重新创建应用，具体操作方案见：<https://open.kwaixiaodian.com/zone/new/faq/detail?cateId=all&pageSign=ad1902ed2da7ba13cb70374625fa4ba31618580306776>

3、建议在绑定的开放平台账号里创建应用并上线，即可关联到现有服务市场；

4、类目不同时请选择与开放平台相同类目即可成功。

#### 关键字：

创建服务

appkey为空

appkey不展示
