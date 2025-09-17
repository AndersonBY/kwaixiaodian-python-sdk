# K0009 - 报错 Invalid url

> **文档ID**: 233348  
> **页面标识**: 61e77001e924b34c3d8b3180cd9648151647412312424  
> **更新时间**: 1647412317815  
> **浏览量**: 37443

---

#### 问题分类：

APP授权页面报错Invalid url

#### 问题现象：

打开授权页面报错Invalid url

![](https://p2-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1647401358466.png)

#### 问题原因：

1.当前授权页面中的app\_id的值不存在

2.当前授权页面中的redirect\_uri的值和当前app的回调地址的值不一致

#### 解决方案：

##### 1.获取正确的授权地址进行授权

进入"控制台-应用中心-应用管理-应用详情"，查看APP的基本信息，确认回调地址填写正确，格式以https://开头。回调网址为用户确认授权后跳转后的地址，授权完成后会将code拼接后跳转到该地址，请确保回调网址为开发者所有。

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1647411801254.png)

在当前应用下查看授权管理，点击"授权管理-测试用户"或"授权管理-授权用户"，添加用户后，点击"发起授权"

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1647412051318.png)

在发起授权弹框中，可选择PC端授权，复制PC端的授权地址

![](https://p4-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1647412118049.png)

将当前地址发送给已经添加到"授权管理-测试用户"或"授权管理-授权用户"中的用户，让用户登陆快手账号后打开，用户确认后即建立了授权关系

![](https://p5-ec.ecukwai.com/kos/nlav10684/gravity-open-editor/gravity-open-editor-1640245696443.png)
