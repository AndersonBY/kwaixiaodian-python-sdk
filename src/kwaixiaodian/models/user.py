"""用户管理相关数据模型（严格对齐 Java SDK）"""

from typing import ClassVar, List, Optional

from pydantic import Field

from .base import BaseModel, BaseRequest, BaseResponse, HttpMethod

# ==================== Java: domain.user ====================


class UserInfoData(BaseModel):
    """对齐 Java: UserInfoData"""

    name: str = Field(description="用户名")
    sex: str = Field(description="性别")
    head: str = Field(description="头像URL")
    big_head: str = Field(description="大头像URL", alias="bigHead")
    open_id: str = Field(description="开放ID", alias="openId")


class OpenStaffInfoParam(BaseModel):
    """对齐 Java: OpenStaffInfoParam"""

    staff_id: int = Field(description="员工ID", alias="staffId")
    open_id: str = Field(description="员工开放ID", alias="openId")
    name: str = Field(description="员工姓名")


class GetSellerInfoResponseParam(BaseModel):
    """对齐 Java: GetSellerInfoResponseParam"""

    name: str = Field(description="用户名")
    sex: str = Field(description="性别")
    head: str = Field(description="头像URL")
    big_head: str = Field(description="大头像URL", alias="bigHead")
    seller_id: int = Field(description="卖家ID", alias="sellerId")
    open_id: str = Field(description="开放ID", alias="openId")
    staff_info: Optional[OpenStaffInfoParam] = Field(
        default=None, description="员工信息", alias="staffInfo"
    )


class RoleInfo(BaseModel):
    """对齐 Java: RoleInfo"""

    role_name: str = Field(description="角色名称", alias="roleName")
    role_id: int = Field(description="角色ID", alias="roleId")
    role_desc: Optional[str] = Field(
        default=None, description="角色描述", alias="roleDesc"
    )


class UserViewInfo(BaseModel):
    """对齐 Java: UserViewInfo"""

    update_time: int = Field(description="更新时间戳", alias="updateTime")
    deleted: bool = Field(description="是否删除")
    staff_user_id: int = Field(description="员工用户ID", alias="staffUserId")
    contact_phone: Optional[str] = Field(
        default=None, description="联系电话", alias="contactPhone"
    )
    login_type: Optional[str] = Field(
        default=None, description="登录类型", alias="loginType"
    )
    phone: Optional[str] = Field(default=None, description="绑定手机", alias="phone")
    role_info: List[RoleInfo] = Field(
        default_factory=list, description="角色信息", alias="roleInfo"
    )
    nick_name: Optional[str] = Field(default=None, description="昵称", alias="nickName")
    disabled: bool = Field(description="是否停用")
    shop_name: Optional[str] = Field(
        default=None, description="店铺名称", alias="shopName"
    )
    remarks: Optional[str] = Field(default=None, description="备注", alias="remarks")


class Staffs(BaseModel):
    """对齐 Java: Staffs"""

    staffs: List[UserViewInfo] = Field(default_factory=list, description="员工列表")
    deleted_count: Optional[int] = Field(
        default=None, description="已删除数量", alias="deletedCount"
    )
    disabled_count: Optional[int] = Field(
        default=None, description="已停用数量", alias="disabledCount"
    )
    normal_count: Optional[int] = Field(
        default=None, description="正常数量", alias="normalCount"
    )
    total_count: Optional[int] = Field(
        default=None, description="总数量", alias="totalCount"
    )


class CreateStaffData(BaseModel):
    """对齐 Java: CreateStaffData"""

    staff_userid: int = Field(description="创建的员工用户ID", alias="staffUserid")


class UpdateStaffResp(BaseModel):
    """对齐 Java: UpdateStaffResp"""

    success: bool = Field(description="是否成功")


class RemoveStaffResp(BaseModel):
    """对齐 Java: RemoveStaffResp"""

    success: bool = Field(description="是否成功")


class UpdateStaffStatusResp(BaseModel):
    """对齐 Java: UpdateStaffStatusResp"""

    success: bool = Field(description="是否成功")


class SubAccountRoleListData(BaseModel):
    """对齐 Java: Data (role list)"""

    roles: List[RoleInfo] = Field(default_factory=list, description="角色列表")


# ==================== Java: request.user ====================


class UserInfoRequest(BaseRequest):
    """open.user.info.get (GET)"""

    @property
    def api_method(self) -> str:
        return "open.user.info.get"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class UserInfoResponse(BaseResponse[UserInfoData]):
    """用户基本信息响应"""

    pass


class UserSellerGetRequest(BaseRequest):
    """open.user.seller.get (GET)"""

    @property
    def api_method(self) -> str:
        return "open.user.seller.get"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class UserSellerGetResponse(BaseResponse[GetSellerInfoResponseParam]):
    """卖家信息响应"""

    pass


class UserFansCheckRequest(BaseRequest):
    """open.user.fans.check (GET)"""

    from_open_id: str = Field(description="来源用户开放ID", alias="fromOpenId")

    @property
    def api_method(self) -> str:
        return "open.user.fans.check"

    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class UserFansCheckResponse(BaseResponse[bool]):
    """是否粉丝 (true/false)"""

    pass


class UserSubAccountCreateRequest(BaseRequest):
    """open.user.sub.account.create (POST)"""

    contact_phone: str = Field(description="联系电话", alias="contactPhone")
    role_ids: List[int] = Field(description="角色ID列表", alias="roleIds")
    phone: Optional[str] = Field(default=None, description="绑定手机", alias="phone")
    nick_name: str = Field(description="昵称", alias="nickName")
    remarks: Optional[str] = Field(default=None, description="备注", alias="remarks")

    @property
    def api_method(self) -> str:
        return "open.user.sub.account.create"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UserSubAccountCreateResponse(BaseResponse[CreateStaffData]):
    """创建子账号响应"""

    pass


class UserSubAccountListRequest(BaseRequest):
    """open.user.sub.account.list (POST)"""

    user_name: Optional[str] = Field(
        default=None, description="用户名筛选", alias="userName"
    )
    count: Optional[int] = Field(default=20, description="每页数量", alias="count")
    page: Optional[int] = Field(default=1, description="页码", alias="page")
    include_deleted: Optional[bool] = Field(
        default=False, description="是否包含已删除", alias="includeDeleted"
    )
    include_disabled: Optional[bool] = Field(
        default=False, description="是否包含已停用", alias="includeDisabled"
    )

    @property
    def api_method(self) -> str:
        return "open.user.sub.account.list"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UserSubAccountListResponse(BaseResponse[Staffs]):
    """子账号列表响应"""

    pass


class UserSubAccountUpdateRequest(BaseRequest):
    """open.user.sub.account.update (POST)"""

    staff_user_id: int = Field(description="员工用户ID", alias="staffUserId")
    contact_phone: Optional[str] = Field(
        default=None, description="联系电话", alias="contactPhone"
    )
    role_ids: Optional[List[int]] = Field(
        default=None, description="角色ID列表", alias="roleIds"
    )
    remarks: Optional[str] = Field(default=None, description="备注", alias="remarks")

    @property
    def api_method(self) -> str:
        return "open.user.sub.account.update"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UserSubAccountUpdateResponse(BaseResponse[UpdateStaffResp]):
    """更新子账号响应"""

    pass


class UserSubAccountRemoveRequest(BaseRequest):
    """open.user.sub.account.remove (POST)"""

    staff_user_id: int = Field(description="员工用户ID", alias="staffUserId")

    @property
    def api_method(self) -> str:
        return "open.user.sub.account.remove"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UserSubAccountRemoveResponse(BaseResponse[RemoveStaffResp]):
    """删除子账号响应"""

    pass


class UserSubAccountStatusUpdateRequest(BaseRequest):
    """open.user.sub.account.status.update (POST)"""

    staff_user_id: int = Field(description="员工用户ID", alias="staffUserId")
    stop: bool = Field(description="是否停用", alias="stop")

    @property
    def api_method(self) -> str:
        return "open.user.sub.account.status.update"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UserSubAccountStatusUpdateResponse(BaseResponse[UpdateStaffStatusResp]):
    """更新子账号状态响应"""

    pass


class UserSubAccountRoleListRequest(BaseRequest):
    """open.user.sub.account.role.list (POST)"""

    @property
    def api_method(self) -> str:
        return "open.user.sub.account.role.list"

    http_method: ClassVar[HttpMethod] = HttpMethod.POST


class UserSubAccountRoleListResponse(BaseResponse[SubAccountRoleListData]):
    """子账号角色列表响应"""

    pass
