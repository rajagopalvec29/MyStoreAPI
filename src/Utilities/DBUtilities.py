import pymysql
from src.Utilities.CredentialUtilities import CreadentialsAPIUtilities
from src.configs.host_configs import DB_HOSTS
import os

class DB_Utilities:

    def __init__(self):
        self.credobj = CreadentialsAPIUtilities()
        self.dbcreds = self.credobj.get_env_db_cred()
        self.machine = os.environ.get("MACHINE")
        self.env = os.environ.get("ENV","test")
        self.host = DB_HOSTS[self.machine][self.env]["host"]
        self.port = DB_HOSTS[self.machine][self.env]["port"]

    def create_connection(self):
        connection = pymysql.connect(host=self.host , user=self.dbcreds['db_user'] , password=self.dbcreds['db_password'] , port=self.port)
        return connection

    def execute_select(self,sql):
        conn = self.create_connection()

        try :
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"DB Error : {e}")
        finally:
            conn.close()

        return res


