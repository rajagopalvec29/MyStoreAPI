from src.Utilities.DBUtilities import DB_Utilities
import random

class ProductsDAO:

    def __init__(self):
        self.db_utils = DB_Utilities()


    def fetch_random_product(self, qty=1):

        sql = f'SELECT * FROM local.wp_posts where post_type = "product" order by ID desc  limit 50;'
        res = self.db_utils.execute_select(sql)
        rand_product = random.sample(res, qty)
        # import pdb;pdb.set_trace()
        return rand_product


    def fetch_product_by_product_name(self,product_name):

        sql = f"SELECT * FROM local.wp_posts where post_type = 'product' and post_title = '{product_name}' ;"
        res = self.db_utils.execute_select(sql)
        return res

    def fetch_product_by_date(self,_date):

        sql = f"select * from local.wp_posts where post_type = 'product' and post_date > '{_date}';"
        res = self.db_utils.execute_select(sql)
        return res
