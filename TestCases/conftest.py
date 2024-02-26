import pytest
import allure
from src.Utilities.RequestUtilities import RequestAPIUtilities
from src.dao.products_dao import ProductsDAO


@pytest.fixture(scope="module")
def get_product_id_fromDB():
    prod_dao = ProductsDAO()
    product = prod_dao.fetch_random_product(1)
    product_id = product[0]['ID']
    return product_id

####### pytest HTML REPORT ######
def pytest_configure(config):
    config._metadata['PROJECT NAME'] = "WOO COMMERCE"
    config._metadata['MODULE NAME'] = "MY STORE"
    config._metadata['TESTER'] = "RAJA"
    config._metadata['ENVIRONMENT'] = f"{RequestAPIUtilities().env}"


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME")
    metadata.pop("Packages")
    metadata.pop("Platform")
    metadata.pop("Plugins")
    metadata.pop("Python")

####### pytest ALLURE REPORT ######
def test_environment_details():
    allure.environment(operating_system="Windows 10")

def test_project_and_tester_name():
    allure.dynamic.project(name="My Store")
    allure.dynamic.tester(name="Raja")
