"""SMS domain models (aligned with Java reference)

Java package: com.kuaishou.merchant.open.api.request.merchant_sms
Endpoints cover sign/template/send/result families, e.g.:
- open.sms.sign.apply.create (GET)
- open.sms.sign.delete (GET)
- open.sms.sign.view (GET)
- open.sms.template.apply.create (GET)
- open.sms.template.delete (GET)
- open.sms.template.view (GET)
- open.sms.send (POST)
- open.sms.batch.send (POST)
- open.sms.express.send (POST)
- open.sms.send.result (POST)
"""

from typing import ClassVar, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# -------------------- Domain models --------------------


class SmsItemRequest(BaseModel):
    extra: Optional[str] = Field(None, alias="extra")
    mobile: Optional[str] = Field(None, alias="mobile")


# -------------------- Params --------------------


class SmsSignApplyCreateParam(BaseModel):
    sign: str = Field(..., alias="sign")


class SmsSignDeleteParam(BaseModel):
    sign_id: int = Field(..., alias="signId")


class SmsSignViewParam(BaseModel):
    sign_like: Optional[str] = Field(None, alias="signLike")
    page_num: Optional[int] = Field(None, alias="pageNum")
    page_size: Optional[int] = Field(None, alias="pageSize")
    sign_id: Optional[int] = Field(None, alias="signId")


class SmsTemplateApplyCreateParam(BaseModel):
    template_name: str = Field(..., alias="templateName")
    template_content: str = Field(..., alias="templateContent")
    template_type: int = Field(..., alias="templateType")


class SmsTemplateDeleteParam(BaseModel):
    template_id: int = Field(..., alias="templateId")


class SmsTemplateViewParam(BaseModel):
    template_id: Optional[int] = Field(None, alias="templateId")
    template_name: Optional[str] = Field(None, alias="templateName")
    page_num: Optional[int] = Field(None, alias="pageNum")
    page_size: Optional[int] = Field(None, alias="pageSize")


class SmsSendParam(BaseModel):
    sign_id: int = Field(..., alias="signId")
    template_id: int = Field(..., alias="templateId")
    template_param: str = Field(..., alias="templateParam")
    mobile: str = Field(..., alias="mobile")
    extra: Optional[str] = Field(None, alias="extra")


class SmsCrowdSendParam(BaseModel):
    sign_id: int = Field(..., alias="signId")
    template_id: int = Field(..., alias="templateId")
    template_param: str = Field(..., alias="templateParam")
    crowd_id: int = Field(..., alias="crowdId")
    extra: Optional[str] = Field(None, alias="extra")


class SmsExpressSendParam(BaseModel):
    sign_id: int = Field(..., alias="signId")
    template_id: int = Field(..., alias="templateId")
    template_param: str = Field(..., alias="templateParam")
    waybill_code: str = Field(..., alias="waybillCode")
    extra: Optional[str] = Field(None, alias="extra")


class SmsBatchSendParam(BaseModel):
    sign_id: int = Field(..., alias="signId")
    template_param: str = Field(..., alias="templateParam")
    template_id: int = Field(..., alias="templateId")
    item_request: Optional[List[SmsItemRequest]] = Field(None, alias="itemRequest")


class SmsSendResultParam(BaseModel):
    message_id: Optional[int] = Field(None, alias="messageId")
    template_id: Optional[int] = Field(None, alias="templateId")
    sign_id: Optional[int] = Field(None, alias="signId")
    mobile: Optional[str] = Field(None, alias="mobile")
    status: Optional[int] = Field(None, alias="status")
    start_time: Optional[int] = Field(None, alias="startTime")
    end_time: Optional[int] = Field(None, alias="endTime")
    page_num: Optional[int] = Field(None, alias="pageNum")
    page_size: Optional[int] = Field(None, alias="pageSize")


# -------------------- Requests --------------------


class SmsSignApplyCreateRequest(BaseRequest):
    param: SmsSignApplyCreateParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.sign.apply.create"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SmsSignDeleteRequest(BaseRequest):
    param: SmsSignDeleteParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.sign.delete"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SmsSignViewRequest(BaseRequest):
    param: SmsSignViewParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.sign.view"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SmsTemplateApplyCreateRequest(BaseRequest):
    param: SmsTemplateApplyCreateParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.template.apply.create"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SmsTemplateDeleteRequest(BaseRequest):
    param: SmsTemplateDeleteParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.template.delete"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SmsTemplateViewRequest(BaseRequest):
    param: SmsTemplateViewParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.template.view"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SmsSendRequest(BaseRequest):
    param: SmsSendParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.send"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SmsBatchSendRequest(BaseRequest):
    param: SmsBatchSendParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.batch.send"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SmsExpressSendRequest(BaseRequest):
    param: SmsExpressSendParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.express.send"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class SmsSendResultRequest(BaseRequest):
    param: SmsSendResultParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.sms.send.result"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


# -------------------- Responses --------------------


class SmsGenericResponse(BaseResponse[dict]):
    pass


class SmsSendResponse(BaseResponse[dict]):
    pass


class SmsBatchSendResponse(BaseResponse[dict]):
    pass


class SmsExpressSendResponse(BaseResponse[dict]):
    pass


class SmsSendResultResponse(BaseResponse[dict]):
    pass
