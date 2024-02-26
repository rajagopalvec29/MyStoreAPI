
API_HOSTS = {
    'test' : " http://localhost:10004/wp-json/wc/v3/",
    'prod' : " ",
    'consumer_key' : "ck_ced88d5026129fafb79aa8b1f5f5a3e2d5a8ed13",
     'consumer_secret' : "cs_07db1e7fe0bc1205fa8bd46e6d5e73f5745e7ce6"
}

DB_HOSTS = { "machine1" : {"test" : {"host": "localhost",
                                     "database" : "local",
                                     "port": 10005
                                     } ,
                            "prod" : {"host": "localhost",
                                     "database" : "local",
                                     "port": 10005
                                     }
                           }
             }