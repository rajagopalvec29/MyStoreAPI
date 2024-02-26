import pytest
from src.Helpers.order_helper import OrderHelper
from src.dao.order_dao import OrderDao
from src.Utilities.RequestUtilities import RequestAPIUtilities
from src.Utilities.GenericUtilities import *
import pprint

@pytest.mark.regression
@pytest.mark.parametrize("new_status",
                         [
                            pytest.param("pending", marks=[pytest.mark.tc10, pytest.mark.smoke]),
                            pytest.param("processing", marks=pytest.mark.tc11),
                            pytest.param("cancelled", marks=pytest.mark.tc12)
                        ]
                         )
def test_update_order_status(new_status):

    #create new order
    order = OrderHelper()
    apires = order.create_order("orders")

    #get order id and current status
    resjson = apires.json()
    order_id =  str(resjson['id'])
    current_status = resjson["status"]

    #update order status and raise put request
    update_info = {"status" : new_status}
    apires = order.update_order("orders/"+order_id, payload=update_info)
    resjson = apires.json()

    #verify the order status in api res and db
    pprint.pprint(resjson, sort_dicts=False)
    assert update_info["status"] == resjson["status"] , f"Status not updated {resjson['status']}"
    orderdao = OrderDao()
    sqlres = orderdao.get_order_by_orderid(order_id)
    db_order_status = sqlres[0]['status']
    assert "wc-"+ update_info["status"] == db_order_status , f"DB order status not updated DB ORDER Status{db_order_status}"

@pytest.mark.tc13
def test_update_order_status_with_invalid_status(new_status="inprocess"):
    # create new order
    order = OrderHelper()
    apires = order.create_order("orders")

    # get order id
    resjson = apires.json()
    order_id = str(resjson['id'])

    # update order status and raise put request
    update_info = {"status": new_status}
    apires = RequestAPIUtilities().put("orders/" + order_id,payload=update_info,expected_status_code=400)
    resjson = apires.json()
    assert resjson["code"] == "rest_invalid_param"


@pytest.mark.tc14
def test_update_order_customer_note():
    # create new order
    order = OrderHelper()
    apires = order.create_order("orders")

    # get order id
    resjson = apires.json()
    order_id = str(resjson['id'])

    notes = generate_random_product_name()

    #update order status and raise put request
    update_info = {"customer_note" : notes}
    apires = order.update_order("orders/"+order_id, payload=update_info)
    resjson = apires.json()
    assert  resjson['customer_note'] == notes


