import pytest
import logging as logger
import pprint
import json
from src.data.order_data import *
from src.Helpers.order_helper import OrderHelper
from src.dao.products_dao import ProductsDAO
from src.dao.order_dao import OrderDao
from src.Helpers.customers_helper import CustomerHelper

pytestmark = [pytest.mark.orders]


@pytest.mark.tc08
def test_createorders(get_product_id_fromDB):
     #retrive data from json file
     # order_jsonfile = open("src/data/orderPayload.json")
     # payload = json.load(order_jsonfile)
     #call payload
     # payload = create_order()
     # pprint.pprint(payload)

     #get product id from db
     product_id = get_product_id_fromDB

     # update payload with above product id
     payload = { "line_items":  [
                                  { "product_id": product_id,
                                    "quantity": 2 }
                                 ]
                }

     #call create order method and raise req
     order = OrderHelper()
     res  = order.create_order("orders",payload)
     resjson = res.json()

     # verify the created order
     order.verify_created_order(resjson, product_id)


@pytest.mark.tc09
def test_createorders_for_new_customer(get_product_id_fromDB):
     # get product id from db
     product_id = get_product_id_fromDB
     #get new customer id
     cust = CustomerHelper()
     res = cust.create_customer("customers")
     customer_id = res['id']

     # update payload with above product_id and customer_id
     info = { "line_items":  [
                                  { "product_id": product_id,
                                    "quantity": 2 }
                                 ],
                   "customer_id": customer_id
                }

     order = OrderHelper()
     apires = order.create_order("orders",payload=info)
     resjson = apires.json()
     #verify the created order
     order.verify_created_order(resjson, product_id,customer_id)
















