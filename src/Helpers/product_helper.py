from src.Utilities.RequestUtilities import RequestAPIUtilities
from src.Utilities.GenericUtilities import *
import pprint


class ProductHelper:

    def __init__(self):
        self.requtils = RequestAPIUtilities()
        pass


    # def list_all_products(self,endpoint):
    #     res = self.requtils.get(endpoint)
    #     pprint.pprint(res.json())
    #     return res.json()

    def list_product_by_id(self,endpoint,payload=None):
        res = self.requtils.get(endpoint, payload=payload)
        return res.json()

    def list_products(self,endpoint,payload=None):

        if not payload:
            payload = dict()

        max_page = 100
        all_products = []
        for i in range(1, max_page+1):
            payload['page'] = i
            res = self.requtils.get(endpoint, payload=payload)

            if not res.json():
                break
            else:
                all_products.extend(res.json())
        else:
            raise Exception(f"Unable to fetch all products more than page : {max_page}")

        return all_products

    def create_single_product(self,endpoint,product_name=None,**kwargs):

        if not product_name:
            product_name = generate_random_product_name()

        payload = dict()
        payload['name'] = product_name
        payload['type'] = "simple"
        payload['regular_price'] = "21.36"
        payload.update(kwargs)
        res = self.requtils.post(endpoint,payload=payload)
        return res.json()


    def update_product_price(self, endpoint , payload ):
        res = self.requtils.put(endpoint,payload=payload)
        return res



