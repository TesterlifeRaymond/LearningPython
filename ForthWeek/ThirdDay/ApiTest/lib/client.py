"""
@Name: client
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/5
"""
import json
from jsonschema import validate
from requests import Session
from user_agent import generate_user_agent
from .recursion import GetDictParam


class HttpHandler(GetDictParam):
    def __init__(self):
        super(HttpHandler, self).__init__()
        self.session = Session()
        self.headers = {
            'User-Agent': generate_user_agent()
        }
    
    def get(self, url):
        resp = self.session.get(url, headers=self.headers).json()
        return resp

    
    def post(self, url, data=None, json=None):
        if json:
            return self.session.post(url, json=json).json()
        return self.session.post(url, data=data).json()

    @classmethod
    def valid_json(cls, myjson, class_name, schname):
        """ 按照jsonSchema格式校验jsonkey、jsonkeyType、jsonCount """
        schfile = 'schema/%s/%s.json' % (class_name, schname)
        with open(schfile, 'r', encoding='utf-8') as f:
            mysch = json.load(f)
        try:
            validate(myjson, mysch)
        except Exception as e:
            return e
        else:
            return True
        finally:
            pass