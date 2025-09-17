"""相册素材服务（对齐 Java SDK 与开放平台）。

- OpenAPI 范围：`open.photo.*`
- Java 包：`com.kuaishou.merchant.open.api.request.video`
"""

from typing import Optional

from ...models.photo import (
    PhotoCountRequest,
    PhotoCountResponse,
    PhotoDeleteRequest,
    PhotoDeleteResponse,
    PhotoIdParam,
    PhotoInfoRequest,
    PhotoInfoResponse,
    PhotoListParam,
    PhotoListRequest,
    PhotoListResponse,
    PhotoPublishParam,
    PhotoPublishRequest,
    PhotoPublishResponse,
    PhotoStartUploadRequest,
    PhotoStartUploadResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncPhotoService:
    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def get_count(
        self, access_token: str, uid: Optional[int] = None
    ) -> PhotoCountResponse:
        """获取相册图片数量

        OpenAPI: `open.photo.count` (GET)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoCountRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoCountRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoCountResponse: 相册图片数量信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoCountRequest(access_token=access_token, uid=uid, api_version="1")
        return await self._client.execute(request, PhotoCountResponse)

    async def list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> PhotoListResponse:
        """分页获取相册图片列表

        OpenAPI: `open.photo.list` (GET)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoListRequest.java)

        Args:
            access_token: 访问令牌。
            cursor: 分页游标（可选）。
            count: 返回条数（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoListResponse: 相册图片列表及分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoListRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoListParam(cursor=cursor, count=count),
            api_version="1",
        )
        return await self._client.execute(request, PhotoListResponse)

    async def start_upload(
        self, access_token: str, uid: Optional[int] = None
    ) -> PhotoStartUploadResponse:
        """获取上传令牌

        OpenAPI: `open.photo.start.upload` (POST)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoStartUploadRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoStartUploadRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoStartUploadResponse: 上传令牌与上传地址信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoStartUploadRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return await self._client.execute(request, PhotoStartUploadResponse)

    async def publish(
        self, access_token: str, upload_token: str, uid: Optional[int] = None
    ) -> PhotoPublishResponse:
        """发布上传的图片

        OpenAPI: `open.photo.publish` (POST)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoPublishRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoPublishRequest.java)

        Args:
            access_token: 访问令牌。
            upload_token: 上传完成后返回的令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoPublishResponse: 发布结果与素材ID等信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoPublishRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoPublishParam(upload_token=upload_token),
            api_version="1",
        )
        return await self._client.execute(request, PhotoPublishResponse)

    async def delete(
        self, access_token: str, photo_id: str, uid: Optional[int] = None
    ) -> PhotoDeleteResponse:
        """删除相册图片

        OpenAPI: `open.photo.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoDeleteRequest.java)

        Args:
            access_token: 访问令牌。
            photo_id: 图片ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoIdParam(photo_id=photo_id),
            api_version="1",
        )
        return await self._client.execute(request, PhotoDeleteResponse)

    async def info(
        self, access_token: str, photo_id: str, uid: Optional[int] = None
    ) -> PhotoInfoResponse:
        """查询图片详情

        OpenAPI: `open.photo.info` (GET)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoInfoRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoInfoRequest.java)

        Args:
            access_token: 访问令牌。
            photo_id: 图片ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoInfoResponse: 图片详细信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoInfoRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoIdParam(photo_id=photo_id),
            api_version="1",
        )
        return await self._client.execute(request, PhotoInfoResponse)


class SyncPhotoService:
    def __init__(self, client: SyncBaseClient):
        self._client = client

    def get_count(
        self, access_token: str, uid: Optional[int] = None
    ) -> PhotoCountResponse:
        """获取相册图片数量（同步）

        OpenAPI: `open.photo.count` (GET)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoCountRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoCountRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoCountResponse: 相册图片数量信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoCountRequest(access_token=access_token, uid=uid, api_version="1")
        return self._client.execute(request, PhotoCountResponse)

    def list(
        self,
        access_token: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        uid: Optional[int] = None,
    ) -> PhotoListResponse:
        """分页获取相册图片列表（同步）

        OpenAPI: `open.photo.list` (GET)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoListRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoListRequest.java)

        Args:
            access_token: 访问令牌。
            cursor: 分页游标（可选）。
            count: 返回条数（可选）。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoListResponse: 相册图片列表及分页信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoListRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoListParam(cursor=cursor, count=count),
            api_version="1",
        )
        return self._client.execute(request, PhotoListResponse)

    def start_upload(
        self, access_token: str, uid: Optional[int] = None
    ) -> PhotoStartUploadResponse:
        """获取上传令牌（同步）

        OpenAPI: `open.photo.start.upload` (POST)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoStartUploadRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoStartUploadRequest.java)

        Args:
            access_token: 访问令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoStartUploadResponse: 上传令牌与上传地址信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoStartUploadRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return self._client.execute(request, PhotoStartUploadResponse)

    def publish(
        self, access_token: str, upload_token: str, uid: Optional[int] = None
    ) -> PhotoPublishResponse:
        """发布上传的图片（同步）

        OpenAPI: `open.photo.publish` (POST)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoPublishRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoPublishRequest.java)

        Args:
            access_token: 访问令牌。
            upload_token: 上传完成后返回的令牌。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoPublishResponse: 发布结果与素材ID等信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoPublishRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoPublishParam(upload_token=upload_token),
            api_version="1",
        )
        return self._client.execute(request, PhotoPublishResponse)

    def delete(
        self, access_token: str, photo_id: str, uid: Optional[int] = None
    ) -> PhotoDeleteResponse:
        """删除相册图片（同步）

        OpenAPI: `open.photo.delete` (POST)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoDeleteRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoDeleteRequest.java)

        Args:
            access_token: 访问令牌。
            photo_id: 图片ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoDeleteResponse: 删除结果。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoDeleteRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoIdParam(photo_id=photo_id),
            api_version="1",
        )
        return self._client.execute(request, PhotoDeleteResponse)

    def info(
        self, access_token: str, photo_id: str, uid: Optional[int] = None
    ) -> PhotoInfoResponse:
        """查询图片详情（同步）

        OpenAPI: `open.photo.info` (GET)
        Java: `com.kuaishou.merchant.open.api.request.video.OpenPhotoInfoRequest`
            (java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/video/OpenPhotoInfoRequest.java)

        Args:
            access_token: 访问令牌。
            photo_id: 图片ID。
            uid: 可选用户ID（最后一个可选参数）。

        Returns:
            PhotoInfoResponse: 图片详细信息。

        Raises:
            KwaixiaodianAPIError: 平台返回错误或响应解析失败。
        """
        request = PhotoInfoRequest(
            access_token=access_token,
            uid=uid,
            param=PhotoIdParam(photo_id=photo_id),
            api_version="1",
        )
        return self._client.execute(request, PhotoInfoResponse)
