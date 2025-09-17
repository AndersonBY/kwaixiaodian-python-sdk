# API调用说明

> **文档ID**: 401853  
> **页面标识**: 8cca5d25ba0015e5045a7ebec6383b741614263875756  
> **更新时间**: 1728527311870  
> **浏览量**: 24989

---

**1.** **前期准备**
---------------

首先需要入驻快手电商开放平台成为开发者，并在开发者账号下创建应用，详情请看[《开放平台入驻指南》](https://open.kwaixiaodian.com/zone/new/docs/dev?pageSign=a068e6b0409a9ee55f5b6f5760ff9d391614263559910)

**2.API** **调用方式**
------------------

### 2.1 域名信息

### 2.2 OAUTH认证

      web端授权方式，商家/子账号员工/开发者可通过授权链接获取用户授权，授权通过后即可通过token调用授权API，详见[《授权说明》](https://open.kwaixiaodian.com/zone/new/docs/dev?pageSign=e1d9e229332f4f233a04b44833a5dfe71614263940720)

### 2.3 SDK下载

     快手电商开放平台提供了所有线上API和消息的SDK，目前支持java 1.6及以上版本，推荐广大开发者使用。

**3.API调用参数说明**
---------------

    请求url样例：https://openapi.kwaixiaodian.com/open/xxx/xxx/xxx?appkey=ksxxxxx&method=open.xxx.xxx.xxx&version=1&param=xxxxxxx&access\_token=xxxxxxxxxxxxxx&timestamp=158888888888&signMethod=MD5&sign=xxxxxx

    请求Content-type仅支持application/x-www-form-urlencoded，如果是post请求，请将param参数放到body里，防止url 过长导致请求失败

|  |  |  |
| --- | --- | --- |
| url字段 | 是否必须 | 描述 |
| https://openapi.kwaixiaodian.com | 是 | 开放平台环境的域名，对应2.1域名信息 |
| /open/xxx/xxx/xx | 是 | 请求的API，用/替换名称中的. |
| appkey=ksxxxxx | 是 | 平台分配的appkey，即client\_id即appId |
| method=open.xxx.xxx.xxx | 是 | 请求的API，详见各API名称 |
| version=1 | 是 | 请求的API版本号，目前版本都为1 |
| param=xxxxxxxx | 是 | 业务参数，详见各API的入参内容 |
| access\_token=xxxxxxxxxx | 是 | 授权API必填，详见开发指南的授权说明文档 |
| timestamp=1583271919000 | 是 | 发起请求的Unix时间戳，单位为毫秒 |
| signMethod=HMAC\_SHA256 | 是 | 签名算法，支持HMAC\_SHA256和MD5， 推荐使用HMAC\_SHA256 |
| sign=xxxxxxxx | 是 | API入参的签名计算结果（2020.10.16开始灰度，10.31正式生效） |

**4.签名算法说明**
------------

快手电商开放平台的所有开放API调用都需要进行加签，服务端会根据请求参数，对签名进行验证，签名不合法的请求将会被拒绝。目前支持的签名算法有两种：MD5(signMethod=MD5)，HMAC\_SHA256（signMethod=HMAC\_SHA256)，下面将以MD5算法为例详细介绍签名流程，使用HMAC\_SHA256算法直接替换即可：

注意：是先进行参数签名计算，然后再对参数进行url encode。如果参数是放在请求body里的，那么url encode是非必须的。

* 保留=符号，用&符号将多个参数及其值组装在一起，根据上面的示例得到的排序结果为：access\_token=xxx&appkey=ks123&method=open.xxx.xxx&param={"title":"短袖", "relItemId":123456, "categoryId":12}&signMethod=MD5&timestamp=1583271919000&version=1。
* 排序好参数后，在末尾加入signSecret（在应用创建审核通过后由平台分配，在“应用中心-应用列表-应用详情”中可见）进行对应算法的签名计算

  + 如果使用MD5算法，则MD5(access\_token=xxx&appkey=ks123&method=open.xxx.xxx.xxx&param={"title":"短袖", "relItemId":123456,      "categoryId":12}&signMethod=MD5&timestamp=1583271919000&version=1&signSecret=xxxxxx)=sign；如果使用HMAC\_SHA256算法，则HMAC\_SHA256(access\_token=xxx&appkey=ks123&method=open.xxx.xxx.xxx&param={"title":"短袖", "relItemId":123456,      "categoryId":12}&signMethod=HMAC\_SHA256&timestamp=1583271919000&version=1&signSecret=xxxxxx)=sign；

[https://openapi.kwaixiaodian.com/open/xxx/xxx?access\_token=xxx&appkey=ks123&method=open.xxx.xxx.xxx&param=%7B%22title%22%3A%22%E7%9F%AD%E8%A2%96%22%2C%20%22relItemId%22%3A123456%2C%20%22categoryId%22%3A12%7D&version=1&signMethod=MD5&timestamp=1583271919000&sign=af2d80958e77e17f1d973003b7b7aec2](https://open.kwaixiaodian.com/open/xxx/xxx/xxx?appkey=ksxxxxx&method=open.xxx.xxx.xxx&version=1&param=xxxxxxx&access_token=xxxxxxxxxxxxxx&timestamp=158888888888&signMethod=MD5&sign=66987CB115214E59E6EC978214934FB8)

```
//签名计算
public static String sign(String param, String signSecret, SignMethodEnum signMethod) {
   StringBuffer sb = new StringBuffer();
   sb.append(param).append("&").append(SIGN_SECRET).append("=").append(signSecret);
   String inputStr = sb.toString();
   switch (signMethod) {
        //HMAC_SHA256算法
       case HMAC_SHA256:
          return HMACSHA256SignUtils.sign(inputStr, signSecret);
       //默认md5算法
       case MD5:
       default:
           return org.apache.commons.codec.digest.DigestUtils.md5Hex(inputStr);
   }
}

// 加签方法
public static String sign(Map<String, String> requestParamMap, String signSecret, SignMethodEnum signMethod) {
   return sign(getSignParam(requestParamMap), signSecret, signMethod);
}
public static String getSignParam(Map<String, String> requestParamMap) {
   String method = checkAndGetParam(requestParamMap, METHOD);
   String appKey = checkAndGetParam(requestParamMap, APPKEY);
   String accessToken = checkAndGetParam(requestParamMap, ACCESS_TOKEN);
   String version = requestParamMap.get(VERSION);
   String signMethod = requestParamMap.get(SIGN_METHOD);
   String timestamp = requestParamMap.get(TIMESTAMP);
   String param = requestParamMap.get(PARAM);
   Map<String, String> signMap = new HashMap<String, String>();
    // 必传参数
   signMap.put(METHOD, method);
   signMap.put(APPKEY, appKey);
   signMap.put(ACCESS_TOKEN, accessToken);
    //可选参数
   if (signMethod != null) {
       signMap.put(SIGN_METHOD, signMethod);
   }
   if (version != null) {
       signMap.put(VERSION, version);
   }
   if (timestamp != null) {
       signMap.put(TIMESTAMP, timestamp);
   }
   if (param != null) {
       signMap.put(PARAM, param);
   }
   String signParam =sortAndJoin(signMap);
   return signParam;
}
public static String checkAndGetParam(Map<String, String> paramMap, String paramKey) {
   String value = paramMap.get(paramKey);
   if (StringUtils.isBlank(value)) {
       throw new IllegalArgumentException(paramKey + " not exist");
   }
   return value;
}
// 排序
public static String sortAndJoin(Map<String, String> params) {
   TreeMap<String, String> paramsTreeMap = new TreeMap();
   for (Map.Entry<String, String> entry : params.entrySet()) {
       if (entry.getValue() == null) {
           continue;
       }
       paramsTreeMap.put(entry.getKey(), entry.getValue());
   }
   String signCalc = "";
   for (Map.Entry<String, String> entry : paramsTreeMap.entrySet()) {
       signCalc = String.format("%s%s=%s&", signCalc, entry.getKey(), entry.getValue(), "&");
   }
   if (signCalc.length() > 0) {
       signCalc = signCalc.substring(0, signCalc.length() - 1);
   }
   return signCalc;
}

private class HMACSHA256SignUtils {
    protected static final Logger logger = Logger.getLogger(HMACSHA256SignUtils.class.getName());

    /**
     * hmac_sha256取hash Base64编码
     */
    public static String sign(String params, String secret) {
        String result = "";
        try {
            Mac sha256HMAC = Mac.getInstance("HmacSHA256");
            SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
            sha256HMAC.init(secretKey);
            byte[] sha256HMACBytes = sha256HMAC.doFinal(params.getBytes());
            String hash = Base64.encodeBase64String(sha256HMACBytes);
            return hash;
        } catch (Exception e) {
            logger.warning("HMACSHA256SignUtils sign failed, params=" + params + ", error=" + e.getMessage());
        }
        return result;
    }
}
```

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
| merchant\_servicemarket | 读取应用在服务市场的信息 | 服务市场API权限 |
| merchant\_comment | 读取或更新订单评价信息 | 评价API权限 |
| merchant\_cs | 读取或更新店铺的客服信息 | 客服API权限 |
