import pytest
from src.Helpers.coupon_helper import Coupon_Helper
from src.Utilities.GenericUtilities import *
import random


@pytest.mark.coupons
@pytest.mark.parametrize("discount_type",[
                                            pytest.param("percent", marks= [pytest.mark.tc18]),
                                            pytest.param("fixed_cart",marks= [pytest.mark.tc19]),
                                             pytest.param("fixed_product",marks= [pytest.mark.tc20])
                                          ])
def test_create_coupons(discount_type):
    coupon = Coupon_Helper()
    code = generate_random_product_name() + "off"
    amount = str(random.randint(10, 100))

    payload = {
    "code": code,
    "discount_type": discount_type,
    "amount": amount,
    "individual_use": "true",
    "exclude_sale_items": "true"
        }

    resapi = coupon.create_coupon("coupons",payload=payload)
    resjson = resapi.json()
    assert resjson['id']
    print(resjson)


@pytest.mark.jenkins
def test_jenkins_test():
    pass
