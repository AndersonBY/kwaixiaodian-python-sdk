"""辅助工具函数"""

from typing import Any, Dict, Generator, List, Union
from urllib.parse import urljoin

import pendulum

from ..exceptions import KwaixiaodianValidationError


def format_timestamp(dt: Union[str, pendulum.DateTime, int]) -> str:
    """格式化时间戳

    Args:
        dt: 时间，支持字符串、DateTime对象或毫秒时间戳

    Returns:
        毫秒时间戳字符串
    """
    if isinstance(dt, str):
        # 尝试解析时间字符串
        parsed_dt = pendulum.parse(dt)
        if isinstance(parsed_dt, pendulum.DateTime):
            return str(int(float(parsed_dt.timestamp()) * 1000))
        else:
            raise KwaixiaodianValidationError(f"无法将字符串解析为DateTime对象: {dt}")
    elif isinstance(dt, pendulum.DateTime):
        return str(int(float(dt.timestamp()) * 1000))
    else:
        # 必须是 int 类型，假设已经是毫秒时间戳
        return str(dt)


def parse_timestamp(timestamp: Union[str, int]) -> pendulum.DateTime:
    """解析时间戳

    Args:
        timestamp: 毫秒时间戳

    Returns:
        DateTime对象
    """
    if isinstance(timestamp, str):
        timestamp = int(timestamp)

    # 转换为秒级时间戳
    return pendulum.from_timestamp(timestamp / 1000)


def build_api_url(base_url: str, method: str) -> str:
    """构建API URL

    Args:
        base_url: 基础URL
        method: API方法名，如 open.item.get

    Returns:
        完整的API URL
    """
    # 将方法名中的点替换为斜杠
    path = "/open/" + method.replace(".", "/")
    return urljoin(base_url, path)


def validate_required_params(params: Dict[str, Any], required: List[str]) -> None:
    """验证必需参数

    Args:
        params: 参数字典
        required: 必需参数列表

    Raises:
        KwaixiaodianValidationError: 必需参数缺失
    """
    missing: List[str] = []
    for param in required:
        if param not in params or params[param] is None:
            missing.append(param)

    if missing:
        raise KwaixiaodianValidationError(
            f"缺少必需参数: {', '.join(missing)}",
            details={"missing_params": missing, "provided_params": list(params.keys())},
        )


def clean_dict(data: Dict[str, Any], remove_none: bool = True) -> Dict[str, Any]:
    """清理字典，移除空值

    Args:
        data: 原始字典
        remove_none: 是否移除None值

    Returns:
        清理后的字典
    """
    result: Dict[str, Any] = {}
    for key, value in data.items():
        if remove_none and value is None:
            continue
        result[key] = value
    return result


def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """安全获取字典值

    Args:
        data: 数据字典
        key: 键名，支持点分隔的嵌套键
        default: 默认值

    Returns:
        键对应的值或默认值
    """
    if "." not in key:
        return data.get(key, default)

    keys = key.split(".")
    current = data

    for k in keys:
        if not isinstance(current, dict) or k not in current:
            return default
        current = current[k]

    return current


def chunk_list(items: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """将列表分块

    Args:
        items: 原始列表
        chunk_size: 块大小

    Returns:
        分块后的列表
    """
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]
