# K0008 - 错误信息：refreshToken.discarded

> **文档ID**: 85189  
> **页面标识**: e62738fd59e01aae65ed2577a46f00151636685473087  
> **更新时间**: 1636685478701  
> **浏览量**: 19934

---

**问题现象：**

错误信息：**{"result":100200102,"error":"access\_denied","error\_msg":"refreshToken.discarded"}**

#### 

#### 问题原因：

重复使用了refresh\_token，refresh\_token使用一次即失效。

#### 解决方案：

每次刷新后会下发一个新的token，再次使用须用新的token进行刷新。
