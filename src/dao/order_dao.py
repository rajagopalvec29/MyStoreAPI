from src.Utilities.DBUtilities import DB_Utilities

class OrderDao:

    def __init__(self):
        self.dbutil = DB_Utilities()


    def get_order_by_orderid(self, orderid):
        sql = f"select * from local.wp_wc_orders where id = {orderid};"
        return self.dbutil.execute_select(sql)

    def get_lineitem_by_orderid(self,orderid):
        sql = f"select * from local.wp_woocommerce_order_items where order_id = {orderid};"
        return self.dbutil.execute_select(sql)

    def get_order_details_by_itemid(self,order_item_id):
        sql = f"SELECT * FROM local.wp_woocommerce_order_itemmeta where order_item_id = {order_item_id};"
        result =  self.dbutil.execute_select(sql)
        metadict = dict()
        for i in result:
            metadict[i['meta_key']] = i['meta_value']
        return metadict


