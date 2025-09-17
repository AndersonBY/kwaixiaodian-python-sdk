"""Photo domain models (aligned with Java reference)

Java package: com.kuaishou.merchant.open.api.request.video
Endpoints:
- open.photo.count (GET)
- open.photo.list (GET)
- open.photo.start.upload (POST)
- open.photo.publish (POST)
- open.photo.delete (POST)
- open.photo.info (GET)
"""

from typing import ClassVar, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# -------------------- Params --------------------


class PhotoListParam(BaseModel):
    cursor: Optional[str] = Field(None, alias="cursor")
    count: Optional[int] = Field(None, alias="count")


class PhotoPublishParam(BaseModel):
    upload_token: str = Field(..., alias="uploadToken")


class PhotoIdParam(BaseModel):
    photo_id: str = Field(..., alias="photoId")


class EmptyParam(BaseModel):
    pass


# -------------------- Requests --------------------


class PhotoCountRequest(BaseRequest):
    """open.photo.count (GET)"""

    param: EmptyParam = Field(default_factory=EmptyParam)

    @property
    def api_method(self) -> str:
        return "open.photo.count"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PhotoListRequest(BaseRequest):
    """open.photo.list (GET)"""

    param: PhotoListParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.photo.list"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class PhotoStartUploadRequest(BaseRequest):
    """open.photo.start.upload (POST)"""

    param: EmptyParam = Field(default_factory=EmptyParam)

    @property
    def api_method(self) -> str:
        return "open.photo.start.upload"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PhotoPublishRequest(BaseRequest):
    """open.photo.publish (POST)"""

    param: PhotoPublishParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.photo.publish"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PhotoDeleteRequest(BaseRequest):
    """open.photo.delete (POST)"""

    param: PhotoIdParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.photo.delete"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class PhotoInfoRequest(BaseRequest):
    """open.photo.info (GET)"""

    param: PhotoIdParam = Field(...)

    @property
    def api_method(self) -> str:
        return "open.photo.info"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


# -------------------- Responses --------------------


class PhotoCountResponse(BaseResponse[dict]):
    pass


class PhotoListResponse(BaseResponse[dict]):
    pass


class PhotoStartUploadResponse(BaseResponse[dict]):
    pass


class PhotoPublishResponse(BaseResponse[dict]):
    pass


class PhotoDeleteResponse(BaseResponse[dict]):
    pass


class PhotoInfoResponse(BaseResponse[dict]):
    pass
