"""评价管理服务（对齐 Java SDK 与开放平台）

- OpenAPI 范围：`open.comment.*`
- 设计依据：`java_sdk_reference/decompiled_source/com/kuaishou/` 下的同名 Java 请求类

文档说明：
- 若参数或行为存在不明确之处，均以 Java 参考与本仓库 `models/comment.py` 的实现为准；
- 相关平台规则与指引，参考 `docs/开发指南和规则协议/` 与 `docs/开发者支持文档/`；
- 每个函数的 docstring 末尾尽量标注 Java 源路径与 API method 便于检索与校验。
"""

from typing import Any, Dict, List, Optional

from ...models.comment import (
    CommentListParam,
    CommentListRequest,
    CommentListResponse,
    CommentReplyRequest,
    CommentReplyResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncCommentService:
    """异步评价管理服务（严格对齐 Java 参考与 OpenAPI）

    对应 Java 包大致位置：`com.kuaishou.merchant.open.api.request` 中的评论相关请求类。
    """

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def list_comments(
        self,
        access_token: str,
        out_order_no: Optional[str] = None,
        service_score: Optional[List[int]] = None,
        quality_score: Optional[List[int]] = None,
        logistics_score: Optional[List[int]] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        create_time_from: Optional[int] = None,
        create_time_to: Optional[int] = None,
        classify_type: Optional[int] = None,
        out_item_id: Optional[int] = None,
        item_title: Optional[str] = None,
        root_comment_tag: Optional[List[int]] = None,
        complain_status: Optional[int] = None,
    ) -> CommentListResponse:
        """获取评价列表。

        Args:
            access_token: 访问令牌。
            out_order_no: 外部订单号筛选。
            service_score: 服务评分筛选，取值范围参考 Java `serviceScore` 列表。
            quality_score: 质量评分筛选，参考 Java `qualityScore` 列表。
            logistics_score: 物流评分筛选，参考 Java `logisticsScore` 列表。
            offset: 偏移量，配合 `limit` 用于分页。
            limit: 返回数量上限。
            create_time_from: 创建时间起（秒级时间戳）。
            create_time_to: 创建时间止（秒级时间戳）。
            classify_type: 分类类型，参考 Java `ClassifyType` 定义。
            out_item_id: 外部商品 ID。
            item_title: 商品标题关键词。
            root_comment_tag: 根评价标签列表。
            complain_status: 投诉状态，参考 Java `ComplainStatus` 定义。

        Returns:
            CommentListResponse: 评价列表响应数据。

        Raises:
            KuaishouAPIError: 当开放平台返回非 0 错误码时抛出。

        OpenAPI:
            - method: `open.comment.list.get`
            - http: GET

        Java:
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantCommentQueryRequest.java`
            - class: `KsMerchantCommentQueryRequest`
        """
        request = CommentListRequest(
            access_token=access_token,
            param=CommentListParam(
                out_order_no=out_order_no,
                service_score=service_score,
                quality_score=quality_score,
                logistics_score=logistics_score,
                offset=offset,
                limit=limit,
                create_time_from=create_time_from,
                create_time_to=create_time_to,
                classify_type=classify_type,
                out_item_id=out_item_id,
                item_title=item_title,
                root_comment_tag=root_comment_tag,
                complain_status=complain_status,
            ),
            api_version="1",
        )
        return await self._client.execute(request, CommentListResponse)

    async def reply_comment(
        self,
        access_token: str,
        comment_id: str,
        reply_content: str,
        is_official: Optional[bool] = True,
        out_info: Optional[Dict[str, Any]] = None,
    ) -> CommentReplyResponse:
        """新增评价/回复。

        Args:
            access_token: 访问令牌。
            comment_id: 被回复的评价 ID（`replyToCommentId`）。
            reply_content: 回复内容，长度限制参考 Java 校验逻辑与平台规则。
            is_official: 是否以“官方”身份回复（将透传到 `option.official`）。
            out_info: 业务外部信息透传，见 Java `ItemCommentOutInfo` 对象。

        Returns:
            CommentReplyResponse: 回复提交结果。

        Raises:
            KuaishouAPIError: 当开放平台返回非 0 错误码时抛出。

        OpenAPI:
            - method: `open.comment.add`
            - http: POST

        Java:
            - path: `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantCommentReplyRequest.java`
            - class: `KsMerchantCommentReplyRequest`
        """

        request = CommentReplyRequest(
            access_token=access_token,
            reply_to_comment_id=int(comment_id) if comment_id.isdigit() else None,
            content=reply_content,
            out_info=out_info,
            option={"official": is_official} if is_official is not None else None,
            api_version="1",
        )
        return await self._client.execute(request, CommentReplyResponse)


class SyncCommentService:
    """同步评价管理服务（严格对齐 Java 参考与 OpenAPI）"""

    def __init__(self, client: SyncBaseClient):
        self._client = client

    def list_comments(
        self,
        access_token: str,
        out_order_no: Optional[str] = None,
        service_score: Optional[List[int]] = None,
        quality_score: Optional[List[int]] = None,
        logistics_score: Optional[List[int]] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        create_time_from: Optional[int] = None,
        create_time_to: Optional[int] = None,
        classify_type: Optional[int] = None,
        out_item_id: Optional[int] = None,
        item_title: Optional[str] = None,
        root_comment_tag: Optional[List[int]] = None,
        complain_status: Optional[int] = None,
    ) -> CommentListResponse:
        """获取评价列表（同步）。

        OpenAPI: `open.comment.list.get` (GET)
        Java: `KsMerchantCommentQueryRequest` —
        `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantCommentQueryRequest.java`
        """
        request = CommentListRequest(
            access_token=access_token,
            param=CommentListParam(
                out_order_no=out_order_no,
                service_score=service_score,
                quality_score=quality_score,
                logistics_score=logistics_score,
                offset=offset,
                limit=limit,
                create_time_from=create_time_from,
                create_time_to=create_time_to,
                classify_type=classify_type,
                out_item_id=out_item_id,
                item_title=item_title,
                root_comment_tag=root_comment_tag,
                complain_status=complain_status,
            ),
            api_version="1",
        )
        return self._client.execute(request, CommentListResponse)

    def reply_comment(
        self,
        access_token: str,
        comment_id: str,
        reply_content: str,
        is_official: Optional[bool] = True,
        out_info: Optional[Dict[str, Any]] = None,
    ) -> CommentReplyResponse:
        """新增评价/回复（同步）。

        OpenAPI: `open.comment.add` (POST)
        Java: `KsMerchantCommentReplyRequest` —
        `java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/KsMerchantCommentReplyRequest.java`
        """

        request = CommentReplyRequest(
            access_token=access_token,
            reply_to_comment_id=int(comment_id) if comment_id.isdigit() else None,
            content=reply_content,
            out_info=out_info,
            option={"official": is_official} if is_official is not None else None,
            api_version="1",
        )
        return self._client.execute(request, CommentReplyResponse)
