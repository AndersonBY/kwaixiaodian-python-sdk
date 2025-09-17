# K0003 - 调用API时报错 “token中无scope权限”

> **文档ID**: 208070  
> **页面标识**: 0fadf84ba78049e96f4bb94ea37b69351618228070897  
> **更新时间**: 1646036083000  
> **浏览量**: 4915

---

#### 问题分类：

API调用类-商品API/订单API/用户API/退款API/分销API/物流API/客服API/评价API/服务市场API-所有接口

#### 问题现象：

调用API时报错“token中无scope权限”

#### 问题原因：

用户对APP进行授权时，并未授权API所属的权限/应用无该权限  
如预期：APP可以获取到用户的商品信息授权

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646033767278.png)

实际：在授权信息中并没有对商品信息授权，因此拿不到当前授权用户的商品信息，也就无法调用商品类目的API  
![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646033826811.png)

#### 解决方案：

1.首先确认APP是否有了调用这个API权限，再确认是否用户已经授权允许APP获取了这个权限

2.确认API归属的权限组，在API详情页下方有权限说明，确认调用报错的API所属权限是哪个

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646033999252.png)

3.查看APP是否有API的所属权限，在"控制台-应用中心"中找到调用报错的APP，点进APP应用详情页面，查看是否有了API所属类目的权限，如没有则需要申请

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/daitianao/gravity-open-editor-1618228927350.png)

4.在APP已获取API所属类目的权限包后，对用户重新发起授权调用，让用户完成对APP的授权

未上线的APP，可以在测试列表中加上测试用户，点击“发起授权”，将链接发给用户完成授权

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646034323992.png)

复制第一个链接，发送给用户

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646034448660.png)

用户打开授权页面，确认在授权页面左侧的APP和API所属的权限包，让用户完成这个权限对APP的授权，例如商品信息授权

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646033767278.png)

已上线的APP，若是商家后台类应用，则可以在授权列表中加上正式授权用户，点击发起授权，将链接发给用户，完成授权，后续步骤同上

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646035001928.png)

复制第一个链接，发送给用户

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646034448660.png)

用户打开授权页面，确认在授权页面左侧的APP和API所属的权限包，让用户完成这个权限对APP的授权，例如商品信息授权

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646033767278.png)

检查线上状态为已建立授权和永久有效

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1646035995622.png)

#### 注意：

1、APP申请增加新的应用权限之后，商家旧的token并不会自动追加新权限，必须要商家再次授权里包含这个新的权限才可以。  
2、测试用户列表中的用户，天调用量次数和授权期限均有限制，商家后台类应用正式使用时，必须要上线，并将正式商家添加到授权用户列表中，完成授权。

#### 关键字：

token

权限

授权

报错
