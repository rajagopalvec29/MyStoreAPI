from src.Utilities.RequestUtilities import RequestAPIUtilities
from src.dao.order_dao import OrderDao
import json

class OrderHelper:

    def __init__(self):
        self.reqapi = RequestAPIUtilities()


    def create_order(self, endpoint,payload = None , **kwarg):

        order_json = open ("src/data/orderPayload.json")
        order_payload  = json.load(order_json)

        if type(payload) == dict:
             order_payload.update(payload)

        res = self.reqapi.post(endpoint=endpoint,payload=order_payload)
        return res

    def update_order(self,endpoint,payload=None,**kwarg):
        res = self.reqapi.put(endpoint=endpoint,payload=payload)
        return res


    def verify_created_order(self,resjson,product_id,customer_id=None):
        if not customer_id:
            customer_id = 0

        # verify the res
        assert resjson[ 'customer_id'] == customer_id, f"customer id is not matching between API : {resjson['customer_id']}, custid :{customer_id}"

        # verify the product id
        api_product_id = resjson['line_items'][0]['product_id']
        assert product_id == api_product_id, f"API product id :{api_product_id} not matching with product id : {product_id}"

        # verify in Db
        order_id = resjson['id']
        orderdao = OrderDao()
        dbres = orderdao.get_order_by_orderid(order_id)
        assert order_id == dbres[0]['id'], f"API order id :{order_id} and DB order id:{dbres[0]['id']}not matching"

        # verify product id in db
        dbres = orderdao.get_lineitem_by_orderid(order_id)
        lineitem = [i for i in dbres if i['order_item_type'] == 'line_item']
        order_item_id = lineitem[0]['order_item_id']
        orderdetails = orderdao.get_order_details_by_itemid(order_item_id)
        # import pdb;pdb.set_trace()
        assert product_id == int(orderdetails['_product_id']), f"DB product id : {orderdetails[0]['meta_value']}" \
                                                               f"not matching with  Product id : {product_id}"



