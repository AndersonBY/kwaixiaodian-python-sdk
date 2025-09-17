"""Utils helper tests"""

import pendulum
import pytest

from kwaixiaodian.exceptions import KwaixiaodianValidationError
from kwaixiaodian.utils.helpers import (
    build_api_url,
    chunk_list,
    clean_dict,
    format_timestamp,
    parse_timestamp,
    safe_get,
    validate_required_params,
)


def test_format_timestamp_with_string():
    ts = format_timestamp("2024-01-01 00:00:00")
    # 2024-01-01 00:00:00 UTC -> 1704067200000 ms
    assert ts.isdigit()
    assert len(ts) >= 10


def test_format_timestamp_invalid_string_raises():
    import pendulum

    with pytest.raises(pendulum.parsing.ParserError):
        format_timestamp("not-a-date")


def test_format_timestamp_with_datetime():
    dt = pendulum.datetime(2024, 1, 1, 0, 0, 0)
    ts = format_timestamp(dt)
    assert ts.isdigit()


def test_format_timestamp_with_int():
    ts = format_timestamp(1704067200000)
    assert ts == "1704067200000"


def test_parse_timestamp_from_string():
    dt = parse_timestamp("1704067200000")
    assert isinstance(dt, pendulum.DateTime)
    assert dt.year == 2024


def test_parse_timestamp_from_int():
    dt = parse_timestamp(1704067200000)
    assert dt.year == 2024


def test_build_api_url():
    url = build_api_url("https://openapi.kwaixiaodian.com", "open.item.get")
    assert url.endswith("/open/open/item/get")


def test_validate_required_params_ok():
    validate_required_params({"a": 1, "b": 2}, ["a", "b"])  # no exception


def test_validate_required_params_missing():
    with pytest.raises(KwaixiaodianValidationError) as ei:
        validate_required_params({"a": 1}, ["a", "b"])  # missing b
    assert "缺少必需参数" in str(ei.value)


def test_clean_dict_removes_none():
    out = clean_dict({"a": 1, "b": None, "c": 0})
    assert out == {"a": 1, "c": 0}


def test_clean_dict_keep_none():
    out = clean_dict({"a": None}, remove_none=False)
    assert out == {"a": None}


def test_safe_get_direct_and_nested():
    data = {"a": 1, "b": {"c": {"d": 4}}}
    assert safe_get(data, "a") == 1
    assert safe_get(data, "b.c.d") == 4
    assert safe_get(data, "b.c.x", default=42) == 42


def test_chunk_list():
    items = list(range(10))
    chunks = list(chunk_list(items, 3))
    assert chunks == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
