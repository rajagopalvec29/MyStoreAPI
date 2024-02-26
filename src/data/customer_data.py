


def createdata(username, useremail):
    postdata = {
    "email": useremail,
    "password": "pass123",
    "first_name": "Raj",
    "last_name": "Dose",
    "username":username,
    "billing": {
        "first_name": "John",
        "last_name": "Doe"
    },
    "shipping": {
        "first_name": "John",
        "last_name": "Doe"
    }
    }

    return postdata

