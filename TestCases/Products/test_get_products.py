import pytest
from src.Helpers.product_helper import ProductHelper
from src.dao.products_dao import ProductsDAO
import logging as logger
import pprint

pytestmark = [pytest.mark.products,pytest.mark.smoke]

@pytest.mark.tc04
def test_list_all_products():
    logger.info("***List All products***")
    prods = ProductHelper()
    res = prods.list_products("products")
    assert res != None , f"List should not be empty : {res}"


@pytest.mark.tc05
def test_get_product_by_id():
    logger.info("***List Product by ID****")
    #get rand productid
    prod_dao = ProductsDAO()
    rand_product = prod_dao.fetch_random_product()
    rand_product_id = rand_product[0]['ID']
    #list product by id
    prods = ProductHelper()
    res = prods.list_product_by_id(f"products/{rand_product_id}")
    print("RES ID  :", res['id'])
    pprint.pprint(res)
    assert res['id'] == rand_product_id ,f"product id is not in DB , expected id : {rand_product_id} but actual id :{res['id']}"

