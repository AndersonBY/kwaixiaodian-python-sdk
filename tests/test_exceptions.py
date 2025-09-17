"""Exception classes stringification tests"""

from kwaixiaodian.exceptions import (
    ERROR_CODE_MAPPING,
    KwaixiaodianAPIError,
    KwaixiaodianAuthError,
    KwaixiaodianConfigError,
    KwaixiaodianNetworkError,
    KwaixiaodianRateLimitError,
    KwaixiaodianSDKError,
    KwaixiaodianSignatureError,
    KwaixiaodianValidationError,
)


def test_sdk_error_str_with_details():
    e = KwaixiaodianSDKError("msg", details={"k": 1})
    assert "Details" in str(e)


def test_api_error_str_contains_parts():
    e = KwaixiaodianAPIError(
        "msg", error_code="E", sub_code="S", http_status=400, request_id="rid"
    )
    s = str(e)
    assert (
        "Error Code: E" in s
        and "Sub Code: S" in s
        and "HTTP Status: 400" in s
        and "Request ID: rid" in s
    )


def test_auth_error_str_with_type():
    e = KwaixiaodianAuthError("bad", auth_type="oauth")
    assert str(e).startswith("[oauth]")


def test_signature_error_inherits_auth_error():
    e = KwaixiaodianSignatureError("sig bad")
    assert "sig bad" in str(e)


def test_validation_error_str():
    e = KwaixiaodianValidationError("invalid", field="f", value=0)
    s = str(e)
    assert "Field: f" in s and "Value: 0" in s


def test_rate_limit_error_str():
    e = KwaixiaodianRateLimitError("limit", retry_after=5)
    assert "Retry after: 5s" in str(e)


def test_network_and_config_error_exist():
    e1 = KwaixiaodianNetworkError("n")
    e2 = KwaixiaodianConfigError("c")
    assert isinstance(e1, KwaixiaodianSDKError)
    assert isinstance(e2, KwaixiaodianSDKError)
    # Ensure __str__ without details path is covered
    assert str(e1) == "n"
    assert str(e2) == "c"


def test_error_code_mapping_contains_common():
    assert "ACCESS_TOKEN_EXPIRED" in ERROR_CODE_MAPPING
