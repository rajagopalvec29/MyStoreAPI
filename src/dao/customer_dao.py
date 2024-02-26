from src.Utilities.DBUtilities import DB_Utilities
import random

class Customer_DAO:

    def __init__(self):
        self.db_util = DB_Utilities()

    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM local.wp_wc_customer_lookup where email = '{email}';"
        res = self.db_util.execute_select(sql)
        return res

    def get_random_customer(self):

        sql = "SELECT * FROM local.wp_wc_customer_lookup order by username desc  limit 10;"
        res = self.db_util.execute_select(sql)
        rand_cust = random.choices(res, k=1)
        return rand_cust



