"""Tests for models.base utilities and properties"""

import orjson
import pytest

from kwaixiaodian.models.base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    HttpMethod,
    PagedData,
)


class _ReqNoApi(BaseRequest):
    # intentionally no api_method override
    pass


def test_base_model_json_roundtrip():
    class M(BaseModel):
        a: int
        b: int | None = None

    m = M(a=1)
    d = m.to_dict()
    assert d == {"a": 1}
    js = m.to_json()
    assert orjson.loads(js) == {"a": 1}
    m2 = M.from_json(js)
    assert m2.a == 1 and m2.b is None


def test_base_response_error_message_composition():
    r = BaseResponse(
        result=None, error_code="E", error_msg="oops", sub_code="S", sub_msg="detail"
    )
    em = r.error_message
    assert "[E]" in em and "oops" in em and "Sub: [S]" in em and "detail" in em


def test_paged_data_total_pages():
    p = PagedData(items=[], total=101, page_size=20)
    assert p.total_pages == 6
    p2 = PagedData(items=[], total=None, page_size=None)
    assert p2.total_pages is None


def test_base_request_defaults_and_errors():
    # default http_method is POST
    class R(BaseRequest):
        @property
        def api_method(self) -> str:  # type: ignore[override]
            return "open.echo"

    r = R(access_token="t")
    assert r.http_method == HttpMethod.POST
    with pytest.raises(NotImplementedError):
        _ReqNoApi(access_token="t").api_method  # unresolved api_method

    # override http_method by subclassing
    class R2(BaseRequest):
        @property
        def api_method(self) -> str:  # type: ignore[override]
            return "open.echo"

        @property
        def http_method(self) -> HttpMethod:  # type: ignore[override]
            return HttpMethod.DELETE

    r2 = R2(access_token="t")
    assert r2.http_method == HttpMethod.DELETE
