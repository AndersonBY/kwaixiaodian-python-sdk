"""基础数据模型定义"""

from abc import ABC
from enum import Enum
from typing import TYPE_CHECKING, Any, Dict, Generic, List, Optional, TypeVar

if TYPE_CHECKING:
    pass

import orjson
from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, Field

# 响应数据类型变量
T = TypeVar("T")


class BaseModel(PydanticBaseModel):
    """基础数据模型

    使用Pydantic v2作为基础，提供数据验证和序列化功能。
    """

    model_config = ConfigDict(
        # 允许额外字段
        extra="allow",
        # 使用枚举值而非名称
        use_enum_values=True,
        # 验证赋值
        validate_assignment=True,
        # 允许使用字段名填充（而不仅是别名）
        populate_by_name=True,
        # 字段别名生成器
        alias_generator=None,
    )

    def to_dict(self, exclude_none: bool = True) -> Dict[str, Any]:
        """转换为字典

        Args:
            exclude_none: 是否排除None值

        Returns:
            字典表示
        """
        return self.model_dump(exclude_none=exclude_none, by_alias=True)

    def to_json(self, exclude_none: bool = True) -> str:
        """转换为JSON字符串

        Args:
            exclude_none: 是否排除None值

        Returns:
            JSON字符串
        """
        data = self.to_dict(exclude_none=exclude_none)
        return orjson.dumps(data).decode()

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseModel":
        """从字典创建实例

        Args:
            data: 字典数据

        Returns:
            模型实例
        """
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "BaseModel":
        """从JSON字符串创建实例

        Args:
            json_str: JSON字符串

        Returns:
            模型实例
        """
        data = orjson.loads(json_str)
        return cls.from_dict(data)


class HttpMethod(str, Enum):
    """HTTP方法枚举"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class BaseRequest(BaseModel, ABC):
    """基础请求模型"""

    # 公共参数
    access_token: str = Field(description="访问令牌")
    uid: Optional[int] = Field(default=None, description="用户ID")
    api_version: str = Field("1", description="API版本")

    @property
    def api_method(self) -> str:
        """API方法名

        优先从实例字段或子类类属性中读取，兼容部分子类以字段方式声明 api_method 的写法。
        子类也可以显式覆写为 @property 以返回常量字符串。
        """
        # Prefer instance field if present (for subclasses that declared api_method as a field)
        if "api_method" in self.__dict__:
            val = self.__dict__["api_method"]
            if isinstance(val, str) and val:
                return val
        # Next, look up class attribute if it's a plain string constant
        cls_attr = getattr(type(self), "api_method", None)
        if isinstance(cls_attr, str) and cls_attr:
            return cls_attr
        # Not provided — subclasses should override via @property
        raise NotImplementedError("api_method not implemented for request class")

    @property
    def http_method(self) -> HttpMethod:
        """HTTP方法，默认为POST

        兼容子类以字段方式声明 http_method 的写法。
        """
        if "http_method" in self.__dict__:
            val = self.__dict__["http_method"]
            if isinstance(val, HttpMethod):
                return val
            # tolerate raw string
            if isinstance(val, str):
                try:
                    return HttpMethod(val)
                except Exception:
                    pass
        cls_attr = getattr(type(self), "http_method", None)
        if isinstance(cls_attr, HttpMethod):
            return cls_attr
        if isinstance(cls_attr, str):
            try:
                return HttpMethod(cls_attr)
            except Exception:
                pass
        return HttpMethod.POST

    def get_business_params(self) -> Dict[str, Any]:
        """获取业务参数

        返回排除公共参数后的业务参数字典
        """
        exclude_fields = {"access_token", "uid", "api_version"}
        data = self.model_dump(exclude=exclude_fields, exclude_none=True, by_alias=True)
        # Java SDK 约定：所有业务字段包裹在 ParamDTO 后，通过 key="param" 传递
        # 我们在签名层会对 business_params 做一次整体 JSON 序列化并放入 param
        # 因此如果请求类仅包含一个名为 "param" 的字段，这里需要“拆箱”，返回其内部内容，
        # 以避免生成形如 param={"param":{...}} 的嵌套结构。
        if set(data.keys()) == {"param"}:
            inner = data.get("param")
            if isinstance(inner, dict):
                return inner
        return data


class BaseResponse(BaseModel, Generic[T]):
    """基础响应模型"""

    result: Optional[T] = Field(default=None, description="响应结果")
    error_code: Optional[str] = Field(default=None, description="错误码")
    error_msg: Optional[str] = Field(default=None, description="错误消息")
    sub_code: Optional[str] = Field(default=None, description="子错误码")
    sub_msg: Optional[str] = Field(default=None, description="子错误消息")
    request_id: Optional[str] = Field(default=None, description="请求ID")

    @property
    def is_success(self) -> bool:
        """请求是否成功"""
        return not self.error_code

    @property
    def error_message(self) -> str:
        """完整错误信息"""
        parts: List[str] = []
        if self.error_code:
            parts.append(f"[{self.error_code}]")
        if self.error_msg:
            parts.append(self.error_msg)
        if self.sub_code:
            parts.append(f"Sub: [{self.sub_code}]")
        if self.sub_msg:
            parts.append(self.sub_msg)
        return " ".join(parts) if parts else ""


class PagedData(BaseModel, Generic[T]):
    """分页数据模型"""

    items: List[T] = Field(default_factory=lambda: [], description="数据列表")
    total: Optional[int] = Field(default=None, description="总数量")
    page_size: Optional[int] = Field(default=None, description="页面大小")
    page_num: Optional[int] = Field(default=None, description="页码")
    has_more: Optional[bool] = Field(default=None, description="是否有更多数据")
    pcursor: Optional[str] = Field(default=None, description="游标分页标识")

    @property
    def total_pages(self) -> Optional[int]:
        """总页数"""
        if self.total is not None and self.page_size is not None and self.page_size > 0:
            return (self.total + self.page_size - 1) // self.page_size
        return None


class PagedResponse(BaseResponse[PagedData[T]]):
    """分页响应模型"""

    def __init__(self, **data):
        super().__init__(**data)
        if self.result is None:
            self.result = PagedData()


# 常用的响应类型别名
SimpleResponse = BaseResponse[Dict[str, Any]]
ListResponse = BaseResponse[List[Dict[str, Any]]]
