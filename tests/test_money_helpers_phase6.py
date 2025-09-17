from __future__ import annotations

from decimal import Decimal

from kwaixiaodian.models.funds import GeneralOrderBillDetail


def test_general_order_bill_detail_decimal_helpers():
    data = GeneralOrderBillDetail(
        order_no=1,
        actual_pay_amount="199.00",
        platform_allowance_amount="10.50",
        total_income="188.50",
        total_refund_amount="0.00",
        platform_commission_amount="5.00",
        distributor_commission_amount="3.00",
        service_amount="1.50",
        settlement_amount="180.00",
        total_outgoing_amount="8.50",
    )

    assert data.actual_pay_amount_decimal == Decimal("199.00")
    assert data.platform_allowance_amount_decimal == Decimal("10.50")
    assert data.total_income_decimal == Decimal("188.50")
    assert data.total_refund_amount_decimal == Decimal("0.00")
    assert data.platform_commission_amount_decimal == Decimal("5.00")
    assert data.distributor_commission_amount_decimal == Decimal("3.00")
    assert data.service_amount_decimal == Decimal("1.50")
    assert data.settlement_amount_decimal == Decimal("180.00")
    assert data.total_outgoing_amount_decimal == Decimal("8.50")
