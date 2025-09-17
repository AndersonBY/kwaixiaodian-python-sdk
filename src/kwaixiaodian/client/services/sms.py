"""短信服务（对齐 Java SDK 与开放平台）。

- OpenAPI 范围：`open.sms.*`
- Java 对应包：`com.kuaishou.merchant.open.api.request.merchant_sms`
- 故障与规则参考：`docs/开发者支持文档/开放平台/业务咨询/K6002 - 短信发送失败.md`
"""

from typing import List, Optional

from ...models.sms import (
    SmsBatchSendParam,
    SmsBatchSendRequest,
    SmsBatchSendResponse,
    SmsExpressSendParam,
    SmsExpressSendRequest,
    SmsExpressSendResponse,
    SmsGenericResponse,
    SmsItemRequest,
    SmsSendParam,
    SmsSendRequest,
    SmsSendResponse,
    SmsSendResultParam,
    SmsSendResultRequest,
    SmsSendResultResponse,
    SmsSignApplyCreateParam,
    SmsSignApplyCreateRequest,
    SmsSignDeleteParam,
    SmsSignDeleteRequest,
    SmsSignViewParam,
    SmsSignViewRequest,
    SmsTemplateApplyCreateParam,
    SmsTemplateApplyCreateRequest,
    SmsTemplateDeleteParam,
    SmsTemplateDeleteRequest,
    SmsTemplateViewParam,
    SmsTemplateViewRequest,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncSmsService:
    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def create_sign(
        self, access_token: str, sign: str, uid: Optional[int] = None
    ):
        """创建短信签名。

        OpenAPI: `open.sms.sign.apply.create` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSignApplyCreateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSignApplyCreateRequest.java`)

        Args:
            access_token: 访问令牌
            sign: 签名内容（需符合平台规范）
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 签名申请结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSignApplyCreateRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSignApplyCreateParam(sign=sign),
            api_version="1"
        )
        return await self._client.execute(req, SmsGenericResponse)

    async def delete_sign(
        self, access_token: str, sign_id: int, uid: Optional[int] = None
    ):
        """删除短信签名。

        OpenAPI: `open.sms.sign.delete` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSignDeleteRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSignDeleteRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSignDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSignDeleteParam(sign_id=sign_id),
            api_version="1",
        )
        return await self._client.execute(req, SmsGenericResponse)

    async def view_signs(
        self,
        access_token: str,
        sign_like: Optional[str] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        sign_id: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """查询短信签名列表。

        OpenAPI: `open.sms.sign.view` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSignViewRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSignViewRequest.java`)

        Args:
            access_token: 访问令牌
            sign_like: 模糊匹配的签名内容（可选）
            page_num: 页码（可选）
            page_size: 每页数量（可选）
            sign_id: 指定签名ID（可选）
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 签名查询结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSignViewRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSignViewParam(
                sign_like=sign_like,
                page_num=page_num,
                page_size=page_size,
                sign_id=sign_id,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsGenericResponse)

    async def create_template(
        self,
        access_token: str,
        template_name: str,
        template_content: str,
        template_type: int,
        uid: Optional[int] = None,
    ):
        """创建短信模板。

        OpenAPI: `open.sms.template.apply.create` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsTemplateApplyCreateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsTemplateApplyCreateRequest.java`)

        Args:
            access_token: 访问令牌
            template_name: 模板名称
            template_content: 模板内容
            template_type: 模板类型（平台定义）
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 模板申请结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsTemplateApplyCreateRequest(
            access_token=access_token,
            uid=uid,
            param=SmsTemplateApplyCreateParam(
                template_name=template_name,
                template_content=template_content,
                template_type=template_type,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsGenericResponse)

    async def delete_template(
        self, access_token: str, template_id: int, uid: Optional[int] = None
    ):
        """删除短信模板。

        OpenAPI: `open.sms.template.delete` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsTemplateDeleteRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsTemplateDeleteRequest.java`)

        Args:
            access_token: 访问令牌
            template_id: 模板ID
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsTemplateDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=SmsTemplateDeleteParam(template_id=template_id),
            api_version="1",
        )
        return await self._client.execute(req, SmsGenericResponse)

    async def view_templates(
        self,
        access_token: str,
        template_id: Optional[int] = None,
        template_name: Optional[str] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """查询短信模板。

        OpenAPI: `open.sms.template.view` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsTemplateViewRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsTemplateViewRequest.java`)

        Args:
            access_token: 访问令牌
            template_id: 模板ID（可选）
            template_name: 模板名称（可选）
            page_num: 页码（可选）
            page_size: 每页数量（可选）
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 模板查询结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsTemplateViewRequest(
            access_token=access_token,
            uid=uid,
            param=SmsTemplateViewParam(
                template_id=template_id,
                template_name=template_name,
                page_num=page_num,
                page_size=page_size,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsGenericResponse)

    async def send(
        self,
        access_token: str,
        sign_id: int,
        template_id: int,
        template_param: str,
        mobile: str,
        extra: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SmsSendResponse:
        """发送单条短信。

        注意：若发送失败或审核失败，请参考
        `docs/开发者支持文档/开放平台/业务咨询/K6002 - 短信发送失败.md`。

        OpenAPI: `open.sms.send` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSendRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSendRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            template_id: 模板ID
            template_param: 模板变量（JSON 字符串）
            mobile: 接收手机号
            extra: 扩展字段（可选）
            uid: 用户ID（可选）

        Returns:
            SmsSendResponse: 短信发送结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSendRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSendParam(
                sign_id=sign_id,
                template_id=template_id,
                template_param=template_param,
                mobile=mobile,
                extra=extra,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsSendResponse)

    async def batch_send(
        self,
        access_token: str,
        sign_id: int,
        template_param: str,
        template_id: int,
        item_request: Optional[List[SmsItemRequest]] = None,
        uid: Optional[int] = None,
    ) -> SmsBatchSendResponse:
        """批量发送短信。

        OpenAPI: `open.sms.batch.send` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsBatchSendRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsBatchSendRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            template_param: 模板变量（JSON 字符串）
            template_id: 模板ID
            item_request: 批量手机号与变量配置（可选）
            uid: 用户ID（可选）

        Returns:
            SmsBatchSendResponse: 批量发送结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsBatchSendRequest(
            access_token=access_token,
            uid=uid,
            param=SmsBatchSendParam(
                sign_id=sign_id,
                template_param=template_param,
                template_id=template_id,
                item_request=item_request,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsBatchSendResponse)

    async def express_send(
        self,
        access_token: str,
        sign_id: int,
        template_id: int,
        template_param: str,
        waybill_code: str,
        extra: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SmsExpressSendResponse:
        """发送快递类短信（按运单号）。

        OpenAPI: `open.sms.express.send` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsExpressSendRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsExpressSendRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            template_id: 模板ID
            template_param: 模板变量（JSON 字符串）
            waybill_code: 运单号
            extra: 扩展字段（可选）
            uid: 用户ID（可选）

        Returns:
            SmsExpressSendResponse: 快递短信发送结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsExpressSendRequest(
            access_token=access_token,
            uid=uid,
            param=SmsExpressSendParam(
                sign_id=sign_id,
                template_id=template_id,
                template_param=template_param,
                waybill_code=waybill_code,
                extra=extra,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsExpressSendResponse)

    async def send_result(
        self,
        access_token: str,
        message_id: Optional[int] = None,
        template_id: Optional[int] = None,
        sign_id: Optional[int] = None,
        mobile: Optional[str] = None,
        status: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SmsSendResultResponse:
        """查询短信发送结果。

        OpenAPI: `open.sms.send.result` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSendResultRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSendResultRequest.java`)

        Args:
            access_token: 访问令牌
            message_id: 短信ID（可选）
            template_id: 模板ID（可选）
            sign_id: 签名ID（可选）
            mobile: 手机号（可选）
            status: 短信状态（可选）
            start_time: 查询开始时间（毫秒，可选）
            end_time: 查询结束时间（毫秒，可选）
            page_num: 页码（可选）
            page_size: 每页数量（可选）
            uid: 用户ID（可选）

        Returns:
            SmsSendResultResponse: 发送结果列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSendResultRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSendResultParam(
                message_id=message_id,
                template_id=template_id,
                sign_id=sign_id,
                mobile=mobile,
                status=status,
                start_time=start_time,
                end_time=end_time,
                page_num=page_num,
                page_size=page_size,
            ),
            api_version="1",
        )
        return await self._client.execute(req, SmsSendResultResponse)


class SyncSmsService:
    def __init__(self, client: SyncBaseClient):
        self._client = client

    def create_sign(self, access_token: str, sign: str, uid: Optional[int] = None):
        """创建短信签名（同步）。

        OpenAPI: `open.sms.sign.apply.create` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSignApplyCreateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSignApplyCreateRequest.java`)

        Args:
            access_token: 访问令牌
            sign: 签名内容
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 签名申请结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSignApplyCreateRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSignApplyCreateParam(sign=sign),
            api_version="1"
        )
        return self._client.execute(req, SmsGenericResponse)

    def delete_sign(self, access_token: str, sign_id: int, uid: Optional[int] = None):
        """删除短信签名（同步）。

        OpenAPI: `open.sms.sign.delete` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSignDeleteRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSignDeleteRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSignDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSignDeleteParam(sign_id=sign_id),
            api_version="1",
        )
        return self._client.execute(req, SmsGenericResponse)

    def view_signs(
        self,
        access_token: str,
        sign_like: Optional[str] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        sign_id: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """查询短信签名列表（同步）。

        OpenAPI: `open.sms.sign.view` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSignViewRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSignViewRequest.java`)

        Args:
            access_token: 访问令牌
            sign_like: 模糊匹配的签名（可选）
            page_num: 页码（可选）
            page_size: 每页数量（可选）
            sign_id: 指定签名ID（可选）
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 签名查询结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSignViewRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSignViewParam(
                sign_like=sign_like,
                page_num=page_num,
                page_size=page_size,
                sign_id=sign_id,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsGenericResponse)

    def create_template(
        self,
        access_token: str,
        template_name: str,
        template_content: str,
        template_type: int,
        uid: Optional[int] = None,
    ):
        """创建短信模板（同步）。

        OpenAPI: `open.sms.template.apply.create` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsTemplateApplyCreateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsTemplateApplyCreateRequest.java`)

        Args:
            access_token: 访问令牌
            template_name: 模板名称
            template_content: 模板内容
            template_type: 模板类型
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 模板申请结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsTemplateApplyCreateRequest(
            access_token=access_token,
            uid=uid,
            param=SmsTemplateApplyCreateParam(
                template_name=template_name,
                template_content=template_content,
                template_type=template_type,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsGenericResponse)

    def delete_template(
        self, access_token: str, template_id: int, uid: Optional[int] = None
    ):
        """删除短信模板（同步）。

        OpenAPI: `open.sms.template.delete` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsTemplateDeleteRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsTemplateDeleteRequest.java`)

        Args:
            access_token: 访问令牌
            template_id: 模板ID
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsTemplateDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=SmsTemplateDeleteParam(template_id=template_id),
            api_version="1",
        )
        return self._client.execute(req, SmsGenericResponse)

    def view_templates(
        self,
        access_token: str,
        template_id: Optional[int] = None,
        template_name: Optional[str] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ):
        """查询短信模板（同步）。

        OpenAPI: `open.sms.template.view` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsTemplateViewRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsTemplateViewRequest.java`)

        Args:
            access_token: 访问令牌
            template_id: 模板ID（可选）
            template_name: 模板名称（可选）
            page_num: 页码（可选）
            page_size: 每页数量（可选）
            uid: 用户ID（可选）

        Returns:
            SmsGenericResponse: 模板查询结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsTemplateViewRequest(
            access_token=access_token,
            uid=uid,
            param=SmsTemplateViewParam(
                template_id=template_id,
                template_name=template_name,
                page_num=page_num,
                page_size=page_size,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsGenericResponse)

    def send(
        self,
        access_token: str,
        sign_id: int,
        template_id: int,
        template_param: str,
        mobile: str,
        extra: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SmsSendResponse:
        """发送单条短信（同步）。

        OpenAPI: `open.sms.send` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSendRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSendRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            template_id: 模板ID
            template_param: 模板变量（JSON 字符串）
            mobile: 接收手机号
            extra: 扩展字段（可选）
            uid: 用户ID（可选）

        Returns:
            SmsSendResponse: 短信发送结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSendRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSendParam(
                sign_id=sign_id,
                template_id=template_id,
                template_param=template_param,
                mobile=mobile,
                extra=extra,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsSendResponse)

    def batch_send(
        self,
        access_token: str,
        sign_id: int,
        template_param: str,
        template_id: int,
        item_request: Optional[List[SmsItemRequest]] = None,
        uid: Optional[int] = None,
    ) -> SmsBatchSendResponse:
        """批量发送短信（同步）。

        OpenAPI: `open.sms.batch.send` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsBatchSendRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsBatchSendRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            template_param: 模板变量（JSON 字符串）
            template_id: 模板ID
            item_request: 批量手机号与变量配置（可选）
            uid: 用户ID（可选）

        Returns:
            SmsBatchSendResponse: 批量发送结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsBatchSendRequest(
            access_token=access_token,
            uid=uid,
            param=SmsBatchSendParam(
                sign_id=sign_id,
                template_param=template_param,
                template_id=template_id,
                item_request=item_request,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsBatchSendResponse)

    def express_send(
        self,
        access_token: str,
        sign_id: int,
        template_id: int,
        template_param: str,
        waybill_code: str,
        extra: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> SmsExpressSendResponse:
        """发送快递类短信（同步）。

        OpenAPI: `open.sms.express.send` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsExpressSendRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsExpressSendRequest.java`)

        Args:
            access_token: 访问令牌
            sign_id: 签名ID
            template_id: 模板ID
            template_param: 模板变量（JSON 字符串）
            waybill_code: 运单号
            extra: 扩展字段（可选）
            uid: 用户ID（可选）

        Returns:
            SmsExpressSendResponse: 快递短信发送结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsExpressSendRequest(
            access_token=access_token,
            uid=uid,
            param=SmsExpressSendParam(
                sign_id=sign_id,
                template_id=template_id,
                template_param=template_param,
                waybill_code=waybill_code,
                extra=extra,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsExpressSendResponse)

    def send_result(
        self,
        access_token: str,
        message_id: Optional[int] = None,
        template_id: Optional[int] = None,
        sign_id: Optional[int] = None,
        mobile: Optional[str] = None,
        status: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> SmsSendResultResponse:
        """查询短信发送结果（同步）。

        OpenAPI: `open.sms.send.result` (GET)
        Java: `com.kuaishou.merchant.open.api.request.merchant_sms.OpenSmsSendResultRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/merchant_sms/OpenSmsSendResultRequest.java`)

        Args:
            access_token: 访问令牌
            message_id: 短信ID（可选）
            template_id: 模板ID（可选）
            sign_id: 签名ID（可选）
            mobile: 手机号（可选）
            status: 短信状态（可选）
            start_time: 查询开始时间（毫秒，可选）
            end_time: 查询结束时间（毫秒，可选）
            page_num: 页码（可选）
            page_size: 每页数量（可选）
            uid: 用户ID（可选）

        Returns:
            SmsSendResultResponse: 发送结果列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        req = SmsSendResultRequest(
            access_token=access_token,
            uid=uid,
            param=SmsSendResultParam(
                message_id=message_id,
                template_id=template_id,
                sign_id=sign_id,
                mobile=mobile,
                status=status,
                start_time=start_time,
                end_time=end_time,
                page_num=page_num,
                page_size=page_size,
            ),
            api_version="1",
        )
        return self._client.execute(req, SmsSendResultResponse)
