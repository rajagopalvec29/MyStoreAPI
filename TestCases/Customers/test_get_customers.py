import logging as logger
import pytest
import pprint
from src.Helpers.customers_helper import CustomerHelper
from src.Utilities.GenericUtilities import *
from src.dao.customer_dao import Customer_DAO



@pytest.mark.customers
@pytest.mark.tc02
def test_list_all_customer():
    logger.info("***List All Customers***")
    # raising get customer list request
    cust = CustomerHelper()
    res = cust.list_customers("customers")
    assert res != None ,f"API RES is Empty : {res}"
