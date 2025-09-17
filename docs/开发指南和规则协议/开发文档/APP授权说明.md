# APP授权说明

> **文档ID**: 401716  
> **页面标识**: e1d9e229332f4f233a04b44833a5dfe71614263940720  
> **更新时间**: 1724738358527  
> **浏览量**: 98085

---

1.授权简介
------

### **1.1 授权说明**

        快手开放平台是基于OAuth2协议的开放授权和鉴权服务，接入前需要了解标准的OAuth2的一些相关知识，可以参考文档 [THE OAUTH 2.0 AUTHORIZATION FRAMEWORK](https://tools.ietf.org/html/rfc6749)。开放平台提供了OAuth2的两种授权方式，授权码code和客户端凭证client\_credentials，分别适用于需要用户授权的授权API调用场景，以及不需要用户授权的非授权API调用场景。注：OAuth2相关知识是接入必备，建议提前阅读。

### **1.2 授权方式**

**OAuth是一种授权机制，数据所有者（快手用户）通过快手平台授予给第三方应用（ISV在开放平台创建的应用，包含appKey等证书信息）自己的部分数据（用户信息、商品发布权限、订单数据等），让第三方可以在某个时间段内通过为令牌（token）访问和使用自己的数据。**

对于标识了“需用户授权”的API，需要使用OAuth2的code授权方式，获取【APP+权限组+用户】的access\_token

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640178541271.png)  
对于未有授权标识的API，可使用OAuth2的client\_credentials授权方式，获取【APP+权限组】的access\_token

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640178622837.png)

### **1.3 获取权限组**

        开放平台开发者分为五种类型：第三方开发者、商家开发者、快分销团长开发者、快赚客开发者和平台合作伙伴，开发者最多可以创建10个应用即APP，一个应用可以拥有多个授权用户，一个授权用户也可以给多个APP授权。APP+权限组+授权用户，这三项唯一确定一个code授权模式的access\_token或refresh\_token，当出现token权限相关的错误时请确认token的值解析出来的三项内容是否当前用户相匹配。线上自助授权信息查询可以使用[【支持中心-常用工具-授权查询工具】](https://open.kwaixiaodian.com/zone/new/tool/auth/authStatus)

       确认API所属权限，开发者可根据业务范围确认需要调用哪些API进行应用开发，确认API所属的权限组是什么

![](https://p5-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652239725006.png)

         确认APP权限，进入“应用中心-应用管理-应用详情”中，查看是否已经拥有业务所需权限，每一个权限包对应一个类目的API的调用权限，可对需要的权限进行申请

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640245900115.png)

### **1.4 开发中建立授权**

      所有的APP在创建完成后、上线前都可以在左侧“授权管理-测试用户”中添加测试用户，用于开发期间的测试

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1650959794130.png)

进入“应用中心-授权管理-测试用户”，填写用户id将其添加到测试用户列表，点击“发起授权”  
  
![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240099636.png)

打开授权弹框，引导用户通过二维码扫码授权，或者PC端网页授权，即可建立授权关系

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240194141.png)

测试用户登录打开授权页面后进行登录，确认应用、权限组等信息，点击“授权并登陆”，会跳转到应用填写的回调地址页面，并带上授权成功后返回的code，若打开授权页面报错，可以查看[授权常见错误](https://open.kwaixiaodian.com/zone/new/faq/list?cateId=49) 自助排查

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240443173.png)

用户点击“授权并登陆”后，会跳转到应用填写的回调地址页面，并带上授权成功后返回的code。有以下两种方式可以获取到APP开发阶段中的token

**1.code换取token**

回调地址可以解析code内容，并使用本文第2点**OAuth2的code** **授权流程及接口简介** 查看code获取token的流程，通过返回的access\_token来调用API（推荐）

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240668650.png)

**2.复制token**

在测试阶段，也可以刷新测试用户页面，直接点击“复制token”获取到access\_token调用API，token有效期为48小时

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652241022422.png)

### **1.5 上线后建立授权**

#### （1）上架到服务市场

若APP详情中展示有第5步的上架流程，则需要到<https://fuwu.kwaixiaodian.com/> 用同一个公司主体完成服务商身份入驻，并在创建服务时关联appKey，将服务上架

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1650960159430.png)

服务上架后应用详情展示如下图，可查看服务详情跳转到服务市场

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1650960513106.png)

用户通过服务市场二维码扫码订购，或在PC端直接订购，完成用户对APP的授权

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1650960770565.png)

用户订购完成后，可到[已订购列表](https://fuwu.kwaixiaodian.com/toolService)查看已经订购的服务

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1654573011083.png)

用户点击“使用服务”后，会跳转到应用填写的回调地址页面，并带上授权成功后返回的code。回调地址可以解析code内容，并使用本文第2点**OAuth2的code** **授权流程及接口简介** 查看code获取token的流程，通过返回的access\_token来调用API

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240668650.png)

#### （2）上线

若APP详情中展示上线为最终流程，则可以通过授权管理添加正式的授权用户，点击左侧菜单栏“授权管理-授权用户”进去授权用户列表

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652248831873.png)

填写用户id将其添加到授权用户列表，点击“发起授权”

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652249330444.png)

打开授权弹框，引导用户通过二维码扫码授权，或者PC端网页授权

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240194141.png)

用户登录打开授权页面后进行登录，确认应用、权限组等信息，点击“授权并登陆”，会跳转到应用填写的回调地址页面，并带上授权成功后返回的code，若打开授权页面报错，可以查看[授权常见错误](https://open.kwaixiaodian.com/zone/new/faq/list?cateId=49) 自助排查

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240443173.png)

用户点击“授权并登陆”后，会跳转到应用填写的回调地址页面，并带上授权成功后返回的code。回调地址可以解析code内容，并使用本文第2点**OAuth2的code** **授权流程及接口简介** 查看code获取token的流程，通过返回的access\_token来调用API

![](https://p5-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1652240668650.png)

**2.OAuth2的code** **授权流程及接口简介**
-------------------------------

### **2.1 code** **授权流程**

![Oauth2.png](https://p4-ec.ecukwai.com/ufile/adsocial/abba4347-4840-40db-b1d2-0f74b05d76bb.jpg "Oauth2.png")

**授权流程可以简单归纳为：**   
**1.获取授权码code（步骤1234）；**   
**2.授权码code换取长时令牌refreshToken以及短时访问令牌accessToken（步骤56），使用accessToken调用电商授权API（步骤789）；**   
**3.若短时访问令牌accessToken过期，则使用长时令牌refreshToken刷新短时访问令牌accessToken，再使用新的accessToken进行调用。**

     下面将详细介绍每一步的调用过程及用到的接口

### **2.2** **获取授权码code**

授权页面地址示例：https://open.kwaixiaodian.com/oauth/authorize?app\_id=xxx&redirect\_uri=xxx&scope=xxx,xxx&response\_type=code&state=xxx

使用说明：  
1、若应用为”商家后台””快分销”“快赚客”自研应用，需要现在应用的测试用户或授权用户列表中添加用户后，用户打开授权页面完成授权；  
2、若应用为第三方ISV应用，需要上架到服务市场，用户需在服务市场订购了服务完成授权。

页面参数说明:

|  |  |  |
| --- | --- | --- |
| **参数名** | **是否必须** | **描述** |
| app\_id | 是 | 应用的 appKey |
| response\_type | 是 | 授权的类型，默认为"code" |
| scope | 是 | APP已经拥有且需要获取用户授权的权限包，多个用 “,” 连接，比如merchant\_item。可至“应用中心-APP详情页”查看APP已获得的权限包列表，平台所有权限包见下文 |
| redirect\_uri | 是 | 授权成功的回调uri，为APP在创建时填写的回调地址 |
| state | 否 | 状态值，成功授权后回调时会原样带回 |

      如果授权成功，授权服务器会将用户的浏览器重定向到应用 ：http(s)://redirect\_uri?code=CODE&state=STATE

|  |  |  |
| --- | --- | --- |
| **参数名** | **参数类型** | **是否必须** |
| code | string | 用来换取access\_token 的授权码，有效期为 2 分钟且只能使用一次，在用户首次允许授权时返回 |
| state | string | 如果请求时传递参数，会回传该参数 |

### **2.3** **用授权码code换取长时令牌refreshToken以及访问令牌accessToken**

      请求地址: https://openapi.kwaixiaodian.com/oauth2/access\_token  \*\* 此接口为后端接口\*\*

      请求方法: GET

      请求参数:

|  |  |  |
| --- | --- | --- |
| **参数名** | **是否必须** | **描述** |
| app\_id | 是 | 开发者appKey |
| grant\_type | 是 | 授权的类型，"code" |
| code | 是 | 2.2中获取到的code |
| app\_secret | 是 | 开发者的appSecret |

    正确返回值:

|  |  |
| --- | --- |
| **参数名** | **描述** |
| result | 返回结果类型，1为正确，其他为不正确 |
| access\_token | 临时访问令牌，作为调用授权API时的入参，过期时间为expires\_in值，授权用户、app和权限组范围唯一决定一个access\_token值 |
| refresh\_token | 长时访问令牌，默认为180天，授权用户、app和权限组范围唯一决定一个refresh\_token值 注意：refresh\_token值不需要存储固定值，因access\_token48小时过期时间内需要**用长时令牌refreshToken刷新访问令牌accessToken，每次刷新会换取新的refreshToken** |
| open\_id | 用户对该开发者的唯一身份标识 |
| expires\_in | access\_token过期时间，单位秒，默认为172800，即48小时 |
| scopes | 本次授权中，用户允许的授权权限范围，即access\_token和refresh\_token中包含的scopes |

    异常返回值：

|  |  |
| --- | --- |
| **参数名** | **描述** |
| result | 返回结果类型，详情查看本文错误码简介 |
| error | 错误类型 |
| error\_msg | 错误详情，用于提示具体的错误原因 |

### **2.4** **用长时令牌refreshToken刷新访问令牌accessToken**

       当access\_token 过期时，可以使用(在有效期内的) refresh\_token重新获取新的access\_token，不需要显式的用户授权过程，若refresh\_token也过期了，则需要再次经过用户授权，因此需要关注refresh\_token的时效（默认180天），需要在时效内用此接口再换取新的refresh\_token才不会出现用户授权频繁失效的情况。该接口只支持authorization\_code模式获取access\_token 刷新，刷新得到新的access\_token 和refresh\_token, **旧的refresh\_token 随即在5分钟内失效** 。

 使用子账号的refreshToken刷新accessToken时以下情况会报错：1、子账号被禁用、删除或状态不可用；2、子账号的主账号和APP不存在授权关系。

       当且仅当子账号状态可用，且子账号的主账号和APP存在授权关系时，才可正确获取到子账号的accessToken。

       请求地址: https://openapi.kwaixiaodian.com/oauth2/refresh\_token  \*\* 此接口为后端接口\*\*

       请求方法: POST

       请求参数:

|  |  |  |
| --- | --- | --- |
| **参数名** | **是否必须** | **描述** |
| grant\_type | 是 | 授权的类型，必须是"refresh\_token" |
| refresh\_token | 是 | 长时访问令牌，默认为180天，2.3接口中返回的值 |
| app\_id | 是 | 开发者 appId |
| app\_secret | 是 | 开发者的appSecret |

    正确返回值:

|  |  |
| --- | --- |
| **参数名** | **描述** |
| result | 返回结果类型，1为正确，其他为不正确 |
| access\_token | 临时访问令牌，作为调用授权API时的入参，过期时间为expires\_in值 |
| expires\_in | access\_token过期时间，单位秒，默认为172800，即48小时 |
| refresh\_token | 长时访问令牌，默认为180天，会返回新的refresh\_token，原有的refresh\_token即失效 注意：refresh\_token值不需要存储固定值，因access\_token48小时过期时间内需要**用长时令牌refreshToken刷新访问令牌accessToken，每次刷新会换取新的refreshToken** |
| refresh\_token\_expires\_in | refresh\_token 的过期时间，单位秒，默认为180天 |
| scopes | access\_token包含的scope |

    异常返回值：

|  |  |
| --- | --- |
| **参数名** | **描述** |
| result | 返回结果类型，详情查看本文错误码简介 |
| error | 错误类型 |
| error\_msg | 错误详情，用于提示具体的错误原因 |

**3.OAuth2的client\_credentials** **授权流程及接口简介**
----------------------------------------------

### **3.1 client\_credentials授权流程**

![image.png](https://p2-ec.ecukwai.com/ufile/adsocial/7677c288-f284-440c-9376-85739ab82845.jpg "image.png")

授权流程可以简单归纳为：   
        1.获取token（步骤12）；   
        2.使用accessToken调用电商非授权API（步骤3）；   
        3.若短时访问令牌accessToken过期，则再次获取新的accessToken进行调用。

     下面将详细介绍第1步获取token接口

### **3.2 获取token**

      请求地址: https://openapi.kwaixiaodian.com/oauth2/access\_token  \*\* 此接口为后端接口\*\*

      请求方法: GET

      请求参数:

|  |  |  |
| --- | --- | --- |
| **参数名** | **是否必须** | **描述** |
| app\_id | 是 | 开发者appKey |
| grant\_type | 是 | 授权的类型，"client\_credentials" |
| app\_secret | 是 | 开发者的appSecret |

    正确返回值:

|  |  |
| --- | --- |
| **参数名** | **描述** |
| result | 返回结果类型，1为正确，其他为不正确 |
| access\_token | 临时访问令牌，作为调用授权API时的入参，过期时间为expires\_in值 |
| token\_type | token类型 |
| expires\_in | access\_token过期时间，单位秒 |

**4.** **授权错误码简介**
------------------

|  |  |  |
| --- | --- | --- |
| result | error | 异常描述 |
| 100200100 | invalid\_request | 缺少必要的请求参数 |
| 100200101 | unauthorized\_client | app 非法，例如 开发者不存在，app 不存在或状态不正确等 |
| 100200102 | access\_denied | 请求被拒绝，授权和后续API，访问中出现任何的Token 错误都会返回这个异常，存在三种可能 invalid refresh\_token  无效token refreshToken.discarded  refreshToken已经用过，不能重复使用 refreshToken.revokedAuthorization 用户已经撤销授权 |
| 100200103 | unsupported\_response\_type | responseType 错误 |
| 100200104 | unsupported\_grant\_type | 换取accessToken 使用的grantType 错误 |
| 100200105 | invalid\_grant | 换取accessToken 使用的 code 错误 |
| 100200106 | invalid\_scope | 权限 scope 错误，或者用户取消了授权等 |
| 100200107 | invalid\_openid | 用户的 openid 无效 |
| 100200500 | server\_error | 服务器内部错误，开发者侧无法处理 |

**5.** **权限组列表**
----------------

    权限组用于控制APP调用API和接受消息的权限范围，只有当APP拥有该API所属的权限组才可以调用API，只有当APP拥有该消息所属的权限组才可以消费消息，列表中说明了现有的权限组以及对应的权限组的API和消息。快手电商开放平台会根据开发者创建的应用类型授予默认的权限组，若开发者需要申请额外的权限组，请发邮件到open@kuaishou.com并说明理由。

|  |  |  |
| --- | --- | --- |
| Scope | 描述 | 备注 |
| user\_base | 授权之后的默认权限 | 所有应用默认拥有此权限组 |
| user\_info | 用户基本信息 | 所有应用默认拥有此权限组 |
| merchant\_user | 商家用户信息 | 用户API权限 |
| merchant\_item | 读取或更新店铺的商品数据 | 商品API和商品消息权限 |
| merchant\_order | 读取或更新店铺的订单信息 | 订单API和订单消息权限 |
| merchant\_refund | 读取或更新店铺的售后信息 | 退款单API和退款单消息权限 |
| merchant\_distribution | 读取或更新分销信息 | 分销API权限 |
| merchant\_logistics | 读取或更新物流信息 | 物流API权限 |
| merchant\_promotion | 读取或更新营销信息 | 营销API权限 |
| merchant\_cs | 读取或更新店铺的客服信息 | 客服API权限 |
| merchant\_comment | 读取或更新店铺的评价信息 | 评价API权限 |
| merchant\_servicemarket | 获取应用在服务市场的订购信息 | 服务市场API权限 |

**6. 常见问题**
-----------

### **6.1 调用API返回-token中无scope的权限**

自查：请使用[【支持中心-常用工具-授权查询工具】](https://open.kwaixiaodian.com/zone/new/tool/auth/authStatus)自查token中拥有哪些权限包，token中的scope范围为“用户已确认授权给APP的权限包”，不等于APP在平台申请的权限包。  
原因：APP有scope权限不等于用户给了APP这个权限，还需要用户确认授权时包括这个权限。大部分原因都在用户在对APP授权后，APP又申请了新的权限包，但用户并没有对APP授权新的权限包，因此出现这个报错。按照隐私保护的规定，每一次要获取用户的权限，都必须清楚地让用户进行确认。  
解决办法：检查授权地址[https://open.kwaixiaodian.com/oauth/authorize?appId=xxx&redirect\_uri=xxx&scope=xxx](https://s.kwaixiaodian.com/oauth/authorize?appId=xxx&redirectUri=xxx&scope=xxx)&response\_type=code&state=xxx，将APP新加的权限包添加到scope参数中去，让用户打开授权地址后重新授权  
  
如示例：  
首先通过"支持中心-常用工具-授权查询工具“自查，自查后token中没有merchant\_logistics权限，代表openId所属的用户并没有将自己的物流信息权限授予给这个APP

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640248353303.png)  
检查应用中是否有这个权限，如"未获取"则进行申请，申请通过后状态为"已获取"  
![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640247555846.png)

拼接完整的带有该scope信息的授权地址给到用户，让用户确认授权时包括对应的权限组信息，授权地址可参考1.3自助拼接或从授权管理中获取

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640247726887.png)

### **6.2 Token 常见问题**

1. access\_token有效期说明：  
access\_token 有效期：通常为48小时，以接口返回时间为主，有变动可能。  
refresh\_token有效期：通常为180天，以接口返回时间为主，有变动可能。

2. 刷新access\_token后，旧的token是否还能使用？  
当access\_token失效之前或者之后，都可以使用有效的refresh\_token去获取一个新的access\_token。

新旧access\_token互不干扰，过期时间独立计算，可以同时有效。  
接口会同时返回一个refresh\_token，同时废弃掉老的refresh\_token。

3. 刷新accessToken后，新的refreshToken过期时间如何计算？  
特别注意：新的refresh\_token过期时间会继承上一个refresh\_token 的过期时间。因此返回值refresh\_token\_expires\_in会随时间逐渐递减。  
因此，当 refresh\_token过期之后，当用户再次使用时,需要第三方主动引导用户再次授权。
