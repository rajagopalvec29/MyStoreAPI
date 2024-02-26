from src.Utilities.GenericUtilities import *
from src.Utilities.RequestUtilities import RequestAPIUtilities
import pprint


class CustomerHelper:

    def __init__(self):
        self.reqapi = RequestAPIUtilities()

    def create_customer(self, endpoint , username = None , emailid=None , **kwargs):

        users = generate_random_username_emailid()

        if not username:
            username = users['username']
        if not emailid:
            emailid = users['emailid']

        payload = dict()
        payload['username'] = username
        payload['email'] = emailid
        payload.update(**kwargs)
        res = self.reqapi.post(endpoint, payload)
        # import pdb; pdb.set_trace()
        return res.json()

    def create_customer_using_existing_user(self, endpoint , username = None , emailid=None , **kwargs):

        users = generate_random_username_emailid()

        if not emailid:
            emailid = users['emailid']

        payload = dict()
        payload['username'] = username
        payload['email'] = emailid
        payload.update(**kwargs)
        res = self.reqapi.post(endpoint, payload , expected_status_code=400)
        pprint.pprint(res.json())
        return res.json()


    def list_customers(self , endpoint):
         res = self.reqapi.get(endpoint)
         pprint.pprint(res.json())
         return res.json()




