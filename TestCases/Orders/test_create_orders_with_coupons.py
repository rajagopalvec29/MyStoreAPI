from src.Helpers.product_helper import ProductHelper
from src.Helpers.order_helper import OrderHelper
from src.Utilities.RequestUtilities import RequestAPIUtilities
import random
import pytest
import pprint



@pytest.mark.tc17
def test_creatorders_apply_coupons():

    resutil = RequestAPIUtilities()
    res = resutil.get("coupons")
    resjson = res.json()
    pprint.pprint(resjson, sort_dicts=False)



    # # hard code 50% coupon
    # coupon_code = 'xevfex50off'
    # discount_pct = '50.00'
    #
    # # get a random product for order
    # rand_products = ProductHelper().list_products("products")
    # rand_product = random.choice(rand_products)
    #
    # info = dict()
    # info['coupon_code'] = coupon_code
    # info['discount_pct'] = discount_pct
    # info['product_id'] = rand_product['id']
    # info['product_price'] = rand_product['price']
    #
    # order_payload_addition = {
    #     "line_items": [{"product_id": info['product_id'], "quantity": 1}],
    #     "coupon_lines": [{"code": info['coupon_code']}],
    #     "shipping_lines": [{"method_id": "flat_rate", "method_title": "Flat Rate", "total": "0.00"}]
    # }
    #
    # # create payload and make call to create order
    # order_helper = OrderHelper()
    # rs_order = order_helper.create_order("orders",payload=order_payload_addition)
    #
    # # calculate expected total price based on coupon and product price
    # expected_total = float(info['product_price']) * (float(info['discount_pct']) / 100)
    #
    # # get total from order response and verify
    # total = round(float(rs_order['total']), 2)
    # expected_total = round(expected_total, 2)
    #
    # assert total == expected_total, f"Order total is not reduced after applying 50% coupon. Expected cost: {expected_total}, Actual: {total}"
    #
