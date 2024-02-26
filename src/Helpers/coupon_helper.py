from src.Utilities.RequestUtilities import RequestAPIUtilities


class Coupon_Helper:

    def __init__(self):
        self.rqutil = RequestAPIUtilities()

    def create_coupon(self,endpoint, payload = None , **kwargs):
        res = self.rqutil.post(endpoint=endpoint, payload=payload )
        return res

