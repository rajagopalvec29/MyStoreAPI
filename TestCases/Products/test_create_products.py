import pytest
import pprint
import logging as logger
from src.Helpers.product_helper import ProductHelper
from src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products,pytest.mark.smoke]


@pytest.mark.tc06
def test_create_single_product():
    #create payload and raise request
    logger.info("***Create Single Product in Store***")
    product = ProductHelper()
    res = product.create_single_product("products",product_name="")
    #verify the response
    pprint.pprint(res)
    assert res , f"Product is not created {res}"
    #verify in DB
    product_name = res['name']
    prods = ProductsDAO()
    ressql = prods.fetch_product_by_product_name(product_name)
    pprint.pprint(ressql)
    assert ressql[0]['post_name'] == product_name ,f"Product name not matched API name : {product_name} , DB name :{ressql[0]['post_name'] }"



