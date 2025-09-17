# SDK使用说明

> **文档ID**: 266057  
> **页面标识**: 2cb0d14623549774e8c8e06994bbcadb1614263973792  
> **更新时间**: 1648882624130  
> **浏览量**: 23018

---

### **1. 概述**

为了提高开发者的效率，快手电商开放平台SDK提供了用户授权、接口访问等功能。

### **2.环境依赖**

JAVA SDK 需要依赖Jave SE/EE 1.6及以上

目前官方仅支持JAVA版本SDK

### **3.如何下载**

JAVA\_SDK\_版本**- [点击下载](https://open.kwaixiaodian.com/rest/open/platform/sdk/api/download)**

注意：

此版本sdk中AccessTokenKsMerchantClient构造函数不兼容，

原构造函数（入参为serverRestUrl和appKey）：AccessTokenKsMerchantClient(String serverRestUrl, String appKey)

改为新构造函数（入参为appKey和signSecret）：AccessTokenKsMerchantClient(String appKey, String signSecret)

并且删除构造函数：AccessTokenKsMerchantClient(String appKey）

请各位开发者注意修改原有构造函数

### **4.使用示例**

官方JAVA SDK的安全扫描报告 - [点击下载](https://p4-ec.ecukwai.com/kos/nlav10684/open/file/Kuaishou-Open-Platform-SDK-scan-report.pdf)

根据平台安全侧的扫描规则，SDK无安全风险

### **5.使用示例**

#### **5.1 授权相关**

**OAuth2的code授权方式:**

```
String appKey = "your app key";
String appSecret = "your app secret";
String grantCode = "your oauth grant code";
//服务器地址
String  serverRestUrl = "server rest url";

//指定服务器地址
OauthAccessTokenKsClient oauthAccessTokenKsClient 
                  = new OauthAccessTokenKsClient(appKey, appSecret, serverRestUrl);
//不指定服务器地址，服务器地址默认为线上
OauthAccessTokenKsClient oauthAccessTokenKsClient 
                  = new OauthAccessTokenKsClient(appKey, appSecret);

// 生成AccessToken
try {
	KsAccessTokenResponse response 
	             = oauthAccessTokenKsClient.getAccessToken(grantCode);
    System.out.println(JSON.toJSONString(response));
} catch (KsMerchantApiException e) {
	e.printStackTrace();
}

String refreshToken = "your app refreshToken";

// 刷新AccessToken
try {
    KsAccessTokenResponse response 
                 = oauthAccessTokenKsClient.refreshAccessToken(refreshToken);
    System.out.println(JSON.toJSONString(response));
} catch (KsMerchantApiException e) {
    e.printStackTrace();
}
```

**OAuth2的client\_credentials** **授权方式**

```
String appKey = "your app key"; 
String appSecret = "your app secret"; 
OauthCredentialKsClient  oauthCredentialKsClient = new OauthCredentialKsClient(appKey, appSecret); 

// 生成AccessToken 
try { 
    KsCredentialResponse response = oauthAccessTokenKsClient.getAccessToken(); System.out.println(JSON.toJSONString(response)); 
} catch (KsMerchantApiException e) { 
    e.printStackTrace(); 
}
```

#### **5.2 接口访问**

##### **5.2.1 一般用法**

以订单拉取接口为例

```
String appKey = "your app key";
String accessToken = "your app accessToken";
String signSecret = "your app signSecret";

//服务器地址为空时，默认是线上环境地址
String  serverRestUrl = "";
// 对应授权商家快手账号
long sellerId = 1L;

AccessTokenKsMerchantClient tokenKsMerchantClient 
                     = new AccessTokenKsMerchantClient(serverRestUrl, appKey, signSecret);

OpenSellerOrderPcursorListRequest openSellerOrderPcursorListRequest 
                     = new OpenSellerOrderPcursorListRequest();
// common param 
openSellerOrderPcursorListRequest.setAccessToken(accessToken); 
openSellerOrderPcursorListRequest.setUid(sellerId); 
openSellerOrderPcursorListRequest.setApiMethodVersion(1);

// business param 
openSellerOrderPcursorListRequest.setType(1); 
openSellerOrderPcursorListRequest.setQueryType(2); 
openSellerOrderPcursorListRequest.setSellerId(sellerId); 
openSellerOrderPcursorListRequest.setPageSize(100); 
openSellerOrderPcursorListRequest.setBeginTime(1581350280000L); 
openSellerOrderPcursorListRequest.setEndTime(1581350400018L); 
openSellerOrderPcursorListRequest.setPcursor("");

// api invoke
try {
    OpenSellerOrderPcursorListResponse response 
                       = tokenKsMerchantClient.execute(openSellerOrderPcursorListRequest);
    System.out.println(JSON.toJSONString(response));
} catch (KsMerchantApiException e) {
    e.printStackTrace();
}
```

##### **5.2.2 自定义方式**

自定义request和response，继承指定对象，并实现指定方法

request继承类：AbstractAccessTokenRequest

例：

```
public class DemoRequest implements AbstractAccessTokenRequest<DemoResponse> {

        public Map<String, Object> getBizParams() {
            // 业务参数
            Map<String, Object> map = new HashMap<String, Object>();
            map.put("itemId", 12312321);
            return map;
        }

        public String getApiMethodName() {
            // api名称
            return "open.item.get";
        }

        public Class<DemoResponse> getResponseClass() {
            // 响应对象
            return DemoResponse.clazz;
        }

        public HttpRequestMethod getHttpRequestMethod() {
            // http method
            return HttpRequestMethod.POST;
        }
}
```

response继承类：KsMerchantResponse

例：

```
public class DemoResponse extends KsMerchantResponse {
        // 业务参数
       private String itemName;
  
       public String getItemName() {
           return itemName;
       }
  
      public void setItemName(String itemName) {
          this.itemName = itemName;
      }
}
```

访问示例：

```
String appKey = "your app key";
String accessToken = "your app accessToken";
String signSecret = "your app signSecret";

//服务器地址为空时，默认是线上环境地址
String  serverRestUrl = "";
DemoRequest request = new DemoRequest();
 
AccessTokenKsMerchantClient tokenKsMerchantClient = new AccessTokenKsMerchantClient(serverRestUrl, appKey, signSecret);

try {
    DemoResponse response = tokenKsMerchantClient.execute(request);
    System.out.println(response.getErrorMsg());
    System.out.println(response.getResult());
    System.out.println(GsonUtils.toJSON(response));
} catch (KsMerchantApiException e) {
    e.printStackTrace();
}
```

##### **5.2.3 泛化方式**

API变更不需要重新生成SDK，request和response使用通用对象

```
String appKey = "your app key";
String accessToken = "your app accessToken";
String signSecret = "your app signSecret";

//服务器地址为空时，默认是线上环境地址
String  serverRestUrl = "";
 
KsCommonRequest request = new KsCommonRequest("open.item.get"/**api名称*/, accessToken, params/**业务参数map*/, HttpRequestMethod.GET);
 
AccessTokenKsMerchantClient tokenKsMerchantClient = new AccessTokenKsMerchantClient(serverRestUrl, appKey, signSecret);

try {
    KsResponseDTO response = tokenKsMerchantClient.execute(request);
    System.out.println(response.getResponse());
    System.out.println(response.getResponseObj(xxxx.class/**结果对象*/));
} catch (KsMerchantApiException e) {
    e.printStackTrace();
}
```
