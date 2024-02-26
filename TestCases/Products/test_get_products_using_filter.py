import pytest
from datetime import datetime,timedelta
from src.Helpers.product_helper import ProductHelper
from src.dao.products_dao import ProductsDAO
import pprint

pytestmark = [pytest.mark.products,pytest.mark.smoke]

@pytest.mark.regression
class Test_getproductsfilter():

    @pytest.mark.tc07
    def test_get_products_by_filter_after(self):
        # create payload for filter
        x_days = 5
        # tmp_date = datetime.now().replace(microsecond=0) - timedelta(x_days)
        # expected_date = tmp_date.isoformat()
        tmp_date = datetime.now() - timedelta(x_days)
        after_date = tmp_date.strftime("%Y-%m-%dT%H:%M:%S")
        payload = dict()
        payload['after'] = after_date
        #call the request
        prod_utils = ProductHelper()
        res = prod_utils.list_products("products",payload=payload)
        assert res ,f"List should not be empty : {res}"
        #get the data from DB
        pd = ProductsDAO()
        ressql = pd.fetch_product_by_date(after_date)
        # verify the Date between API and DB
        db_date = (ressql[0]['post_date']).strftime("%Y-%m-%dT%H:%M:%S")
        assert db_date > after_date , f"expected_date :{after_date} , DB_DATE : {db_date}"
        #verify the count between API and DB
        assert len(res) == len(ressql), f"Count not matched API count :{len(res)} , DB count :{ len(ressql)}"
        # verify the ID between API and DB
        res_id_list = sorted([ i['id'] for i in res])
        ressql_id_list = sorted([ i['ID'] for i in ressql])
        #import pdb;pdb.set_trace()
        assert res_id_list == ressql_id_list , f"ID list not matched API ID : {res_id_list} , DB ID :{ressql_id_list}"







