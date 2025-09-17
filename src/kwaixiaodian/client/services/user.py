"""用户管理服务（严格对齐 Java SDK）"""

from typing import List, Optional

from ...models.user import (
    UserFansCheckRequest,
    UserFansCheckResponse,
    UserInfoRequest,
    UserInfoResponse,
    UserSellerGetRequest,
    UserSellerGetResponse,
    UserSubAccountCreateRequest,
    UserSubAccountCreateResponse,
    UserSubAccountListRequest,
    UserSubAccountListResponse,
    UserSubAccountRemoveRequest,
    UserSubAccountRemoveResponse,
    UserSubAccountRoleListRequest,
    UserSubAccountRoleListResponse,
    UserSubAccountStatusUpdateRequest,
    UserSubAccountStatusUpdateResponse,
    UserSubAccountUpdateRequest,
    UserSubAccountUpdateResponse,
)
from ..base import AsyncBaseClient, SyncBaseClient


class AsyncUserService:
    """异步用户管理服务（对齐 Java SDK 与开放平台）。

    - OpenAPI 范围：`open.user.*`
    - Java 包：`com.kuaishou.merchant.open.api.request.user`
    - 规则与协议：参考 `docs/开发指南和规则协议/`
    """

    def __init__(self, client: AsyncBaseClient):
        self._client = client

    async def get_info(
        self, access_token: str, uid: Optional[int] = None
    ) -> UserInfoResponse:
        """获取用户基本信息。

        OpenAPI: `open.user.info.get` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserInfoGetRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserInfoGetRequest.java`)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选，默认从令牌解析）

        Returns:
            UserInfoResponse: 用户基本资料（头像、昵称等）

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserInfoRequest(access_token=access_token, uid=uid, api_version="1")
        return await self._client.execute(request, UserInfoResponse)

    async def get_seller_info(
        self, access_token: str, uid: Optional[int] = None
    ) -> UserSellerGetResponse:
        """获取卖家信息。

        OpenAPI: `open.user.seller.get` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSellerGetRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSellerGetRequest.java`)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选，默认从令牌解析）

        Returns:
            UserSellerGetResponse: 卖家基础信息及员工信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSellerGetRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return await self._client.execute(request, UserSellerGetResponse)

    async def check_fans(
        self, access_token: str, from_open_id: str, uid: Optional[int] = None
    ) -> UserFansCheckResponse:
        """粉丝关系检查。

        OpenAPI: `open.user.fans.check` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserFansCheckRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserFansCheckRequest.java`)

        Args:
            access_token: 访问令牌
            from_open_id: 来源用户的开放ID
            uid: 商家用户ID（可选）

        Returns:
            UserFansCheckResponse: 是否存在粉丝关系

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserFansCheckRequest(
            access_token=access_token,
            uid=uid,
            from_open_id=from_open_id,
            api_version="1",
        )
        return await self._client.execute(request, UserFansCheckResponse)

    async def create_sub_account(
        self,
        access_token: str,
        contact_phone: str,
        role_ids: List[int],
        nick_name: str,
        phone: Optional[str] = None,
        remarks: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> UserSubAccountCreateResponse:
        """创建子账号。

        OpenAPI: `open.user.sub.account.create` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountCreateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountCreateRequest.java`)

        Args:
            access_token: 访问令牌
            contact_phone: 联系电话
            role_ids: 子账号绑定的角色ID列表
            nick_name: 子账号昵称
            phone: 登录手机号（可选）
            remarks: 备注信息（可选）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountCreateResponse: 新建子账号结果（含 staff_userid）

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountCreateRequest(
            access_token=access_token,
            uid=uid,
            contact_phone=contact_phone,
            role_ids=role_ids,
            phone=phone,
            nick_name=nick_name,
            remarks=remarks,
            api_version="1",
        )
        return await self._client.execute(request, UserSubAccountCreateResponse)

    async def list_sub_accounts(
        self,
        access_token: str,
        user_name: Optional[str] = None,
        count: Optional[int] = 20,
        page: Optional[int] = 1,
        include_deleted: Optional[bool] = False,
        include_disabled: Optional[bool] = False,
        uid: Optional[int] = None,
    ) -> UserSubAccountListResponse:
        """查询子账号列表。

        OpenAPI: `open.user.sub.account.list` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountListRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountListRequest.java`)

        Args:
            access_token: 访问令牌
            user_name: 账号搜索关键字（可选）
            count: 单页数量（默认 20）
            page: 页码（默认 1）
            include_deleted: 是否包含已删除账号（默认 False）
            include_disabled: 是否包含已停用账号（默认 False）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountListResponse: 子账号分页数据

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountListRequest(
            access_token=access_token,
            uid=uid,
            user_name=user_name,
            count=count,
            page=page,
            include_deleted=include_deleted,
            include_disabled=include_disabled,
            api_version="1",
        )
        return await self._client.execute(request, UserSubAccountListResponse)

    async def update_sub_account(
        self,
        access_token: str,
        staff_user_id: int,
        contact_phone: Optional[str] = None,
        role_ids: Optional[List[int]] = None,
        remarks: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> UserSubAccountUpdateResponse:
        """更新子账号信息。

        OpenAPI: `open.user.sub.account.update` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountUpdateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountUpdateRequest.java`)

        Args:
            access_token: 访问令牌
            staff_user_id: 子账号ID
            contact_phone: 联系电话（可选）
            role_ids: 角色ID列表（可选）
            remarks: 备注信息（可选）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountUpdateResponse: 更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountUpdateRequest(
            access_token=access_token,
            uid=uid,
            staff_user_id=staff_user_id,
            contact_phone=contact_phone,
            role_ids=role_ids,
            remarks=remarks,
            api_version="1",
        )
        return await self._client.execute(request, UserSubAccountUpdateResponse)

    async def remove_sub_account(
        self, access_token: str, staff_user_id: int, uid: Optional[int] = None
    ) -> UserSubAccountRemoveResponse:
        """删除子账号。

        OpenAPI: `open.user.sub.account.remove` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountRemoveRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountRemoveRequest.java`)

        Args:
            access_token: 访问令牌
            staff_user_id: 子账号ID
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountRemoveResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountRemoveRequest(
            access_token=access_token,
            uid=uid,
            staff_user_id=staff_user_id,
            api_version="1",
        )
        return await self._client.execute(request, UserSubAccountRemoveResponse)

    async def update_sub_account_status(
        self,
        access_token: str,
        staff_user_id: int,
        stop: bool,
        uid: Optional[int] = None,
    ) -> UserSubAccountStatusUpdateResponse:
        """启用或停用子账号。

        OpenAPI: `open.user.sub.account.status.update` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountStatusUpdateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountStatusUpdateRequest.java`)

        Args:
            access_token: 访问令牌
            staff_user_id: 子账号ID
            stop: 是否停用（True 停用，False 启用）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountStatusUpdateResponse: 状态变更结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountStatusUpdateRequest(
            access_token=access_token,
            uid=uid,
            staff_user_id=staff_user_id,
            stop=stop,
            api_version="1",
        )
        return await self._client.execute(request, UserSubAccountStatusUpdateResponse)

    async def list_sub_account_roles(
        self, access_token: str, uid: Optional[int] = None
    ) -> UserSubAccountRoleListResponse:
        """获取子账号角色列表。

        OpenAPI: `open.user.sub.account.role.list` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountRoleListRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountRoleListRequest.java`)

        Args:
            access_token: 访问令牌
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountRoleListResponse: 角色列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountRoleListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return await self._client.execute(request, UserSubAccountRoleListResponse)


class SyncUserService:
    """同步用户管理服务（与异步版本等价的能力集合）。"""

    def __init__(self, client: SyncBaseClient):
        self._client = client

    def get_info(
        self, access_token: str, uid: Optional[int] = None
    ) -> UserInfoResponse:
        """获取用户基本信息（同步）。

        OpenAPI: `open.user.info.get` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserInfoGetRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserInfoGetRequest.java`)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选）

        Returns:
            UserInfoResponse: 用户基础资料

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserInfoRequest(access_token=access_token, uid=uid, api_version="1")
        return self._client.execute(request, UserInfoResponse)

    def get_seller_info(
        self, access_token: str, uid: Optional[int] = None
    ) -> UserSellerGetResponse:
        """获取卖家信息（同步）。

        OpenAPI: `open.user.seller.get` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSellerGetRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSellerGetRequest.java`)

        Args:
            access_token: 访问令牌
            uid: 用户ID（可选）

        Returns:
            UserSellerGetResponse: 卖家信息

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSellerGetRequest(
            access_token=access_token, uid=uid, api_version="1"
        )
        return self._client.execute(request, UserSellerGetResponse)

    def check_fans(
        self, access_token: str, from_open_id: str, uid: Optional[int] = None
    ) -> UserFansCheckResponse:
        """粉丝关系检查（同步）。

        OpenAPI: `open.user.fans.check` (GET)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserFansCheckRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserFansCheckRequest.java`)

        Args:
            access_token: 访问令牌
            from_open_id: 来源用户开放ID
            uid: 商家用户ID（可选）

        Returns:
            UserFansCheckResponse: 粉丝关系校验结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserFansCheckRequest(
            access_token=access_token,
            uid=uid,
            from_open_id=from_open_id,
            api_version="1",
        )
        return self._client.execute(request, UserFansCheckResponse)

    def create_sub_account(
        self,
        access_token: str,
        contact_phone: str,
        role_ids: List[int],
        nick_name: str,
        phone: Optional[str] = None,
        remarks: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> UserSubAccountCreateResponse:
        """创建子账号（同步）。

        OpenAPI: `open.user.sub.account.create` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountCreateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountCreateRequest.java`)

        Args:
            access_token: 访问令牌
            contact_phone: 联系电话
            role_ids: 角色ID列表
            nick_name: 子账号昵称
            phone: 登录手机号（可选）
            remarks: 备注信息（可选）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountCreateResponse: 创建结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountCreateRequest(
            access_token=access_token,
            uid=uid,
            contact_phone=contact_phone,
            role_ids=role_ids,
            phone=phone,
            nick_name=nick_name,
            remarks=remarks,
            api_version="1",
        )
        return self._client.execute(request, UserSubAccountCreateResponse)

    def list_sub_accounts(
        self,
        access_token: str,
        user_name: Optional[str] = None,
        count: Optional[int] = 20,
        page: Optional[int] = 1,
        include_deleted: Optional[bool] = False,
        include_disabled: Optional[bool] = False,
        uid: Optional[int] = None,
    ) -> UserSubAccountListResponse:
        """查询子账号列表（同步）。

        OpenAPI: `open.user.sub.account.list` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountListRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountListRequest.java`)

        Args:
            access_token: 访问令牌
            user_name: 搜索关键字（可选）
            count: 单页数量（默认 20）
            page: 页码（默认 1）
            include_deleted: 是否包含已删除账号
            include_disabled: 是否包含已停用账号
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountListResponse: 子账号分页数据

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountListRequest(
            access_token=access_token,
            uid=uid,
            user_name=user_name,
            count=count,
            page=page,
            include_deleted=include_deleted,
            include_disabled=include_disabled,
            api_version="1",
        )
        return self._client.execute(request, UserSubAccountListResponse)

    def update_sub_account(
        self,
        access_token: str,
        staff_user_id: int,
        contact_phone: Optional[str] = None,
        role_ids: Optional[List[int]] = None,
        remarks: Optional[str] = None,
        uid: Optional[int] = None,
    ) -> UserSubAccountUpdateResponse:
        """更新子账号信息（同步）。

        OpenAPI: `open.user.sub.account.update` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountUpdateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountUpdateRequest.java`)

        Args:
            access_token: 访问令牌
            staff_user_id: 子账号ID
            contact_phone: 联系电话（可选）
            role_ids: 角色ID列表（可选）
            remarks: 备注信息（可选）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountUpdateResponse: 更新结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountUpdateRequest(
            access_token=access_token,
            uid=uid,
            staff_user_id=staff_user_id,
            contact_phone=contact_phone,
            role_ids=role_ids,
            remarks=remarks,
            api_version="1",
        )
        return self._client.execute(request, UserSubAccountUpdateResponse)

    def remove_sub_account(
        self, access_token: str, staff_user_id: int, uid: Optional[int] = None
    ) -> UserSubAccountRemoveResponse:
        """删除子账号（同步）。

        OpenAPI: `open.user.sub.account.remove` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountRemoveRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountRemoveRequest.java`)

        Args:
            access_token: 访问令牌
            staff_user_id: 子账号ID
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountRemoveResponse: 删除结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountRemoveRequest(
            access_token=access_token,
            uid=uid,
            staff_user_id=staff_user_id,
            api_version="1",
        )
        return self._client.execute(request, UserSubAccountRemoveResponse)

    def update_sub_account_status(
        self,
        access_token: str,
        staff_user_id: int,
        stop: bool,
        uid: Optional[int] = None,
    ) -> UserSubAccountStatusUpdateResponse:
        """启用或停用子账号（同步）。

        OpenAPI: `open.user.sub.account.status.update` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountStatusUpdateRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountStatusUpdateRequest.java`)

        Args:
            access_token: 访问令牌
            staff_user_id: 子账号ID
            stop: 是否停用（True 停用，False 启用）
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountStatusUpdateResponse: 状态变更结果

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountStatusUpdateRequest(
            access_token=access_token,
            uid=uid,
            staff_user_id=staff_user_id,
            stop=stop,
            api_version="1",
        )
        return self._client.execute(request, UserSubAccountStatusUpdateResponse)

    def list_sub_account_roles(
        self, access_token: str, uid: Optional[int] = None
    ) -> UserSubAccountRoleListResponse:
        """获取子账号角色列表（同步）。

        OpenAPI: `open.user.sub.account.role.list` (POST)
        Java:
            `com.kuaishou.merchant.open.api.request.user.OpenUserSubAccountRoleListRequest`
            (`java_sdk_reference/decompiled_source/com/kuaishou/merchant/open/api/request/user/OpenUserSubAccountRoleListRequest.java`)

        Args:
            access_token: 访问令牌
            uid: 商家用户ID（可选）

        Returns:
            UserSubAccountRoleListResponse: 角色列表

        Raises:
            KwaixiaodianAPIError: 当开放平台返回错误码或解析失败时抛出。
        """
        request = UserSubAccountRoleListRequest(
            access_token=access_token,
            uid=uid,
            api_version="1",
        )
        return self._client.execute(request, UserSubAccountRoleListResponse)
