from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import requests
import os
from src.configs.host_configs import API_HOSTS
import logging as logger
from src.Utilities.CredentialUtilities import CreadentialsAPIUtilities


class RequestAPIUtilities:

    def __init__(self):
        self.env = os.environ.get('ENV','test')
        self.baseurl = API_HOSTS[self.env]
        cred_util = CreadentialsAPIUtilities()
        self.creds = cred_util.get_env_api_keys()
        # self.consumer_key = API_HOSTS['consumer_key']
        # self.consumer_secret = API_HOSTS['consumer_secret']
        self.auth = OAuth1(self.creds['wc_key'], self.creds['wc_secret'])

    def assert_respose_status_code(self):
        assert self.expected_status_code == self.status_code, f"expected status code : {self.expected_status_code} , actual status code : {self.status_code}"\
        f"URL : {self.posturl } , Res : {self.resjson}"


    def post(self,endpoint, payload ,headers = None , expected_status_code = 201):
        if not headers:
            headers = {"Content-Type": "application/json"}

        logger.info(f"Payload = {payload}")
        logger.info(f"BaseUrl = {self.baseurl+endpoint} , consumerkey = {self.creds['wc_key']} , consumer_secret = {self.creds['wc_secret'] } ")
        self.posturl = self.baseurl+endpoint
        res = requests.post(self.posturl,json=payload , headers=headers, auth=self.auth)
        self.resjson = res.json()
        # import pdb;pdb.set_trace()
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.assert_respose_status_code()
        return res

    def get(self,endpoint,payload=None,headers = None,expected_status_code = 200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        logger.info(f"BaseUrl = {self.baseurl + endpoint} , consumerkey = {self.creds['wc_key']} , consumer_secret = {self.creds['wc_secret']} ")
        self.geturl = self.baseurl + endpoint

        try:
            res = requests.get(self.geturl,params=payload,headers=headers,auth=self.auth)
        except Exception as e:
            raise Exception(f"API Request Error : {e} , RES : {res.status_code}")
        finally:
            print(f"API Respose code : {res.status_code}")


        self.resjson = res.json()
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.assert_respose_status_code()
        return res



    def put(self,endpoint, payload=None ,headers = None,expected_status_code = 200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.geturl = self.baseurl + endpoint
        logger.info(f"Payload = {payload}")
        logger.info(f"BaseUrl = { self.geturl} , consumerkey = {self.creds['wc_key']} , consumer_secret = {self.creds['wc_secret']} ")

        try :
            res = requests.put(url=self.geturl, json=payload,headers=headers ,auth=self.auth)
        except Exception as e:
            raise Exception(f"API Error :{e} ,  RES : {res.status_code}")
        finally:
            print(f"API STATUS Code : {res.status_code}")

        self.resjson = res.json()
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.assert_respose_status_code()
        return  res





