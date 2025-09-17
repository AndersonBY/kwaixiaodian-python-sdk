import pytest

from kwaixiaodian.models.base import HttpMethod
from kwaixiaodian.models.logistics import (
    BaseAddressInfo,
    DistrictListRequest,
    ExpressCustomTemplateQueryRequest,
    ExpressPrinterElementQueryRequest,
    ExpressTemplateListParam,
    ExpressTemplateListRequest,
    SellerAddressCreateRequest,
)


@pytest.mark.unit
def test_district_list_request_http_method_and_aliases():
    req = DistrictListRequest(access_token="t", district_version="v1")
    assert req.http_method == HttpMethod.GET
    # ensure alias is respected in business params
    params = req.get_business_params()
    assert "districtVersion" in params
    assert params["districtVersion"] == "v1"


@pytest.mark.unit
def test_express_custom_template_query_http_method():
    req = ExpressCustomTemplateQueryRequest(access_token="t")
    assert req.http_method == HttpMethod.GET


@pytest.mark.unit
def test_express_printer_element_query_http_method():
    req = ExpressPrinterElementQueryRequest(access_token="t")
    assert req.http_method == HttpMethod.GET


@pytest.mark.unit
def test_express_template_list_request_http_method_and_payload():
    param = ExpressTemplateListParam(offset=1, limit=10, search_used=True)
    req = ExpressTemplateListRequest(access_token="t", param=param)
    assert req.http_method == HttpMethod.GET
    # get_business_params should unwrap single "param" field content
    params = req.get_business_params()
    assert params == {"offset": 1, "limit": 10, "searchUsed": True}


@pytest.mark.unit
def test_seller_address_create_request_http_method_and_alias():
    base = BaseAddressInfo(
        consignee="c",
        mobile="m",
        province_code=1,
        province="P",
        city_code=2,
        city="C",
        district_code=3,
        district="D",
        address="A",
    )
    req = SellerAddressCreateRequest(access_token="t", base_info=base)
    assert req.http_method == HttpMethod.GET
    params = req.get_business_params()
    assert "baseInfo" in params
    assert params["baseInfo"]["provinceCode"] == 1
