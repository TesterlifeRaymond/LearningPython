"""
@Name: client
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/6
"""

import json
from jsonschema import validate
from requests import Session
from user_agent import generate_user_agent
from .recursion import GetDictParam
import random, string


class HttpHandler(GetDictParam):
    def __init__(self):
        super(HttpHandler, self).__init__()
        self.session = Session()
        self.headers = {
            'User-Agent': generate_user_agent()
        }
    
    def mobile(self):
        pattern = ['138', '139', '140', '155', '158', '147', '131', '132']
        mobile = random.choice(pattern) + ''.join(random.sample(string.digits, 8))
        return mobile
    
    def get(self, url):
        resp = self.session.get(url, headers=self.headers).text
        return resp
    
    def post(self, url, data=None, json=None):
        if json:
            return self.session.post(url, json=json).text
        return self.session.post(url, data=data).text
    
    @classmethod
    def valid_json(cls, myjson, class_name, schname):
        """ 按照jsonSchema格式校验jsonkey、jsonkeyType、jsonCount """
        # get(self, url): ==> self代表的是类实例对象
        # http = HttpHandler() ==> http == self
        
        # valid_json(cls, *args) ==> cls 代表类对象本身
        # HttpHandler.valid_json(*args) == cls
        # HttpHandler().get() ==> self

        schfile = 'schema/%s/%s.json' % (class_name, schname)
        with open(schfile, 'r', encoding='utf-8') as f:
            mysch = json.load(f)
        try:
            validate(myjson, mysch)
        except Exception as e:
            print(e)
            return e
        else:
            return True
        finally:
            pass