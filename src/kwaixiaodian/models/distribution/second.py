"""二级分销相关数据模型（按 Java 参考严格对齐）"""

from typing import Any, ClassVar, Dict

from ..base import BaseRequest, BaseResponse, HttpMethod

# ==================== 二级分销相关 API ====================


class SecondAllowInvestmentActivityItemListRequest(BaseRequest):
    """二级允许投资活动商品列表请求"""

    # Based on Java SDK: OpenDistributionSecondAllowInvestmentActivityItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.allow.investment.activity.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondAllowInvestmentActivityItemListResponse(BaseResponse[Dict[str, Any]]):
    """二级允许投资活动商品列表响应"""

    pass


class SecondApplyInvestmentActivityListRequest(BaseRequest):
    """二级申请投资活动列表请求"""

    # Based on Java SDK: OpenDistributionSecondApplyInvestmentActicityListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.apply.investment.activity.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondApplyInvestmentActivityListResponse(BaseResponse[Dict[str, Any]]):
    """二级申请投资活动列表响应"""

    pass


class SecondActionCancelCooperationRequest(BaseRequest):
    """二级操作取消合作请求"""

    # Based on Java SDK: OpenDistributionSecondActionCancelCooperationRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.cancel.cooperation"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionCancelCooperationResponse(BaseResponse[Dict[str, Any]]):
    """二级操作取消合作响应"""

    pass


class SecondActionApplyAgainInvestmentActivityRequest(BaseRequest):
    """二级操作重新申请投资活动请求"""

    # Based on Java SDK: OpenDistributionSecondActionApplyAgainInvestmentActivityRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.apply.again.investment.activity"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionApplyAgainInvestmentActivityResponse(BaseResponse[Dict[str, Any]]):
    """二级操作重新申请投资活动响应"""

    pass


class SecondActionApplyAgainInvestmentActicityRequest(BaseRequest):
    """二级操作重新申请投资活动请求（Acticity 拼写变体）

    基于 Java SDK: OpenDistributionSecondActionApplyAgainInvestmentActicityRequest
    """

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.apply.again.investment.acticity"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionApplyAgainInvestmentActicityResponse(BaseResponse[Dict[str, Any]]):
    """二级操作重新申请投资活动响应（Acticity 拼写变体）"""

    pass


class SecondActionHandleCooperationRequest(BaseRequest):
    """二级操作处理合作请求"""

    # Based on Java SDK: OpenDistributionSecondActionHandleCooperationRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.handle.cooperation"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionHandleCooperationResponse(BaseResponse[Dict[str, Any]]):
    """二级操作处理合作响应"""

    pass


class SecondActionApplyInvestmentActivityRequest(BaseRequest):
    """二级分销申请投资活动请求"""

    # Based on Java SDK: OpenDistributionSecondActionApplyInvestmentActicityRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.apply.investment.acticity"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionApplyInvestmentActivityResponse(BaseResponse[Dict[str, Any]]):
    """二级分销申请投资活动响应"""

    pass


class SecondActionApplyInvestmentActivityStandardRequest(BaseRequest):
    """二级分销申请投资活动请求（标准版）"""

    # Based on Java SDK: OpenDistributionSecondActionApplyInvestmentActivityRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.apply.investment.activity"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionApplyInvestmentActivityStandardResponse(BaseResponse[Dict[str, Any]]):
    """二级分销申请投资活动响应（标准版）"""

    pass


class SecondActionEditApplyInvestmentActivityRequest(BaseRequest):
    """二级分销编辑申请投资活动请求"""

    # Based on Java SDK: OpenDistributionSecondActionEditApplyInvestmentActicityRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.edit.apply.investment.acticity"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionEditApplyInvestmentActivityResponse(BaseResponse[Dict[str, Any]]):
    """二级分销编辑申请投资活动响应"""

    pass


class SecondActionEditApplyInvestmentActivityStandardRequest(BaseRequest):
    """二级分销编辑申请投资活动请求（标准版）"""

    # Based on Java SDK: OpenDistributionSecondActionEditApplyInvestmentActivityRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.action.edit.apply.investment.activity"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondActionEditApplyInvestmentActivityStandardResponse(
    BaseResponse[Dict[str, Any]]
):
    """二级分销编辑申请投资活动响应（标准版）"""

    pass


class SecondAllowInvestmentActivityItemListAltRequest(BaseRequest):
    """二级分销允许投资活动商品列表请求（变体）"""

    # Based on Java SDK: OpenDistributionSecondAllowInvestmentActicityItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.allow.investment.acticity.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondAllowInvestmentActivityItemListAltResponse(BaseResponse[Dict[str, Any]]):
    """二级分销允许投资活动商品列表响应（变体）"""

    pass


class SecondApplyInvestmentActivityItemListAltRequest(BaseRequest):
    """二级分销申请投资活动商品列表请求（变体）"""

    # Based on Java SDK: OpenDistributionSecondApplyInvestmentActicityItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.apply.investment.acticity.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondApplyInvestmentActivityItemListAltResponse(BaseResponse[Dict[str, Any]]):
    """二级分销申请投资活动商品列表响应（变体）"""

    pass


class SecondApplyInvestmentActivityListAltRequest(BaseRequest):
    """二级分销申请投资活动列表请求（变体）"""

    # Based on Java SDK: OpenDistributionSecondApplyInvestmentActicityListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.apply.investment.acticity.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondApplyInvestmentActivityListAltResponse(BaseResponse[Dict[str, Any]]):
    """二级分销申请投资活动列表响应（变体）"""

    pass


class SecondApplyInvestmentActivityItemListStandardRequest(BaseRequest):
    """二级分销申请投资活动商品列表请求（标准版）"""

    # Based on Java SDK: OpenDistributionSecondApplyInvestmentActivityItemListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.apply.investment.activity.item.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondApplyInvestmentActivityItemListStandardResponse(
    BaseResponse[Dict[str, Any]]
):
    """二级分销申请投资活动商品列表响应（标准版）"""

    pass


class SecondInvestmentActivityListAltRequest(BaseRequest):
    """二级分销投资活动列表请求（变体）"""

    # Based on Java SDK: OpenDistributionSecondInvestmentActicityListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.investment.acticity.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondInvestmentActivityListAltResponse(BaseResponse[Dict[str, Any]]):
    """二级分销投资活动列表响应（变体）"""

    pass


class SecondInvestmentActivityListStandardRequest(BaseRequest):
    """二级分销投资活动列表请求（标准版）"""

    # Based on Java SDK: OpenDistributionSecondInvestmentActivityListRequest

    @property
    def api_method(self) -> str:
        return "open.distribution.second.investment.activity.list"

    # Java: HttpRequestMethod.GET
    http_method: ClassVar[HttpMethod] = HttpMethod.GET


class SecondInvestmentActivityListStandardResponse(BaseResponse[Dict[str, Any]]):
    """二级分销投资活动列表响应（标准版）"""

    pass
