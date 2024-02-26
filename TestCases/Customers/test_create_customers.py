import logging as logger
import pytest
import pprint
from src.data.customer_data import *
from src.Helpers.customers_helper import CustomerHelper
from src.Utilities.GenericUtilities import *
from src.dao.customer_dao import Customer_DAO

@pytest.mark.customers
@pytest.mark.tc01
def test_createnewcustomer():
    logger.info("<<<<This is create data>>>>>")
    #Assign username and email via random
    userdetails = generate_random_username_emailid()
    username = userdetails['username']
    emailid = userdetails['emailid']
    #raising customer request
    cust = CustomerHelper()
    res = cust.create_customer("customers", username=username, emailid=emailid)
    #verify the API Response
    assert username == res['username'] , f"expected user name :{username} Actual user name : {res['username']}"
    #verify the DB entry
    custdao = Customer_DAO()
    ressql = custdao.get_customer_by_email(emailid)
    sql_user_id = ressql[0]['user_id']
    logger.info(f"Data Created in Database DB user id :{sql_user_id} ")
    assert sql_user_id == res['id'] , f"DB user id :{sql_user_id} not matched with API user id : {res['id']}"


@pytest.mark.customers
@pytest.mark.tc03
def test_create_customer_fail_existing_user():
    #get random existing user name
    custdao = Customer_DAO()
    ressql = custdao.get_random_customer()
    existing_user = ressql[0]['username']

    #raise request using existing username
    cust = CustomerHelper()
    res = cust.create_customer_using_existing_user("customers", username=existing_user)
    assert  res['message'] == 'An account is already registered with that username. Please choose another.', f"actual message : { res['message']}"









