import random
import string



def generate_random_username_emailid(username=None,emailid=None):

    if not username:
        user_length = 8
        username  = ''.join(random.choices(string.ascii_letters , k=user_length))
    if not emailid:
        email_length = 10
        email = ''.join(random.choices(string.ascii_lowercase , k=email_length))
        emailid = email + '@test.com'

    user_details = { 'username' : username , 'emailid' : emailid  }

    return user_details


def generate_random_product_name(product_name = None ):

    if not product_name:
        prefix = "az_"
        product_name = prefix + "".join(random.choices(string.ascii_lowercase , k = 10))

    return product_name

