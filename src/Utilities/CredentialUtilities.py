import os

class CreadentialsAPIUtilities:

    def __init__(self):
        pass

    def get_env_api_keys(self):
        wc_key = "ck_ced88d5026129fafb79aa8b1f5f5a3e2d5a8ed13" #os.environ.get('WC_KEY')
        wc_secret = "cs_07db1e7fe0bc1205fa8bd46e6d5e73f5745e7ce6" # os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("WC_KEY and WC_SECRET should be in Env Variables")
        else:
            return {'wc_key':wc_key ,'wc_secret':wc_secret }

    def get_env_db_cred(self):
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")

        if not db_user or not db_password:
            raise Exception("DB_USER and DB_PASSWORD should be in Env Variables")
        else:
            return {'db_user':db_user,'db_password':db_password}