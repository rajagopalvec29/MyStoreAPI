import pytest
from src.Helpers.product_helper import ProductHelper
import random
import pprint



@pytest.mark.tc15
def test_update_product_price(get_product_id_fromDB):
    products = ProductHelper()
    res = products.list_products("products")
    for i in res :
        product_id = i['id']
        if i['on_sale']:
            continue
        else:
            break
    else:
        product_id = get_product_id_fromDB

    #update price
    new_price = str(random.randint(10,100)) + "." + str(random.randint(11,99))
    info = {"regular_price":new_price}

    #get current price
    res = products.list_product_by_id("products/"+ str(product_id))
    current_price = res["regular_price"]

    # update regular price
    res = products.update_product_price("products/"+ str(product_id), payload=info)
    resjson = res.json()

    #verify the res
    pprint.pprint(resjson)
    assert  resjson["regular_price"] == info["regular_price"] , f"current price not updated {current_price} , API price { resjson['regular_price']}"
    print(f"current price : {current_price} is updated to { resjson['regular_price']}")


@pytest.mark.tc16
def test_update_product_on_sale():
    products = ProductHelper()
    prod_list = products.list_products("products")
    for prod in prod_list:
        product_id = prod['id']
        if prod["regular_price"] != "" :
            if prod['on_sale'] and prod["sale_price"] :
                continue
            else:
                break
    else:
        print("no id present")

    # update the onsale
    apires = products.list_product_by_id("products/"+str(product_id))
    print(apires['on_sale'])

    info = {'sale_price' : "10.99"}
    apires = products.update_product_price("products/"+str(product_id),payload=info)
    resjson = apires.json()
    assert resjson['on_sale'] == 1 , f"on sale field not updated {resjson['on_sale'] }"
    print(f"On Sale : {resjson['on_sale']}, Sale_price : {resjson['sale_price']} ")

    #update sale price as empty and veriyf the onsale set to False
    info = {'sale_price': ""}
    apires = products.update_product_price("products/" + str(product_id), payload=info)
    resjson = apires.json()
    assert resjson['on_sale'] == 0, f"on sale field not updated {resjson['on_sale']}"
    print(f"On Sale : {resjson['on_sale']}, Sale_price : {resjson['sale_price']} ")









