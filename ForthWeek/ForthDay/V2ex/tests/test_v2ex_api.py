"""
@Name: test_v2ex_api
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/6
"""

import json
import unittest
from lib.client import HttpHandler


class V2exApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.top_url = 'https://www.v2ex.com/api/topics/hot.json'
        cls.show_url = 'https://www.v2ex.com/api/nodes/show.json?name='
        cls.userinfo_url = 'https://www.v2ex.com/api/members/show.json?username='
        cls.laster_url = 'https://www.v2ex.com/api/topics/latest.json'
        cls.http = HttpHandler()
        
    def test_top_api_is_ok(self):
        """[V2ex][HOT] 测试hot接口返回正确"""
        result = json.loads(self.http.get(self.top_url))
        for item in result:
            self.assertIsNotNone(self.http.get_value(item, 'title'))
            base = self.http.get_value(item, 'node')
            laster_url = self.http.get_value(base, 'url').split('/')[-1]
            self.assertEqual(self.http.get_value(base, 'name') == laster_url, True)
            print('{} == {} is True'.format(laster_url, self.http.get_value(base, 'name')))
        
    def test_show_url_is_ok(self):
        """[V2ex][SHOW] 测试show node url is ok"""
        tags = 'Python'
        result = json.loads(self.http.get(self.show_url + tags))
        print(json.dumps(result, indent=4, ensure_ascii=False))
        self.assertEqual(self.http.get_value(result, 'title_alternative'), tags)
        self.assertEqual(self.http.get_value(result, 'id'), 90)
    
    def test_show_url_is_false(self):
        """[V2ex][SHOW] 测试show node url is False"""
        message = 'Object Not Found'
        status = 'error'
        result = json.loads(self.http.get(self.show_url))
        print(json.dumps(result, indent=4, ensure_ascii=False))
        self.assertEqual(self.http.get_value(result, 'status'), status)
        self.assertEqual(self.http.get_value(result, 'message'), message)

    def test_userinfo_is_ok(self):
        """[V2ex][USERINFO] 测试userinfo url is ok"""
        username = 'Raymond'
        user_url = 'http://www.v2ex.com/member/' + username
        result = json.loads(self.http.get(self.userinfo_url + username))
        print(json.dumps(result, indent=4, ensure_ascii=False))
        self.assertEqual(self.http.get_value(result, 'status'), 'found')
        self.assertEqual(self.http.get_value(result, 'username'), username)
        self.assertEqual(self.http.get_value(result, 'url'), user_url)

    def test_userinfo_is_false(self):
        """[V2ex][USERINFO] 测试userinfo url is false"""
        result = json.loads(self.http.get(self.userinfo_url))
        print(json.dumps(result, indent=4, ensure_ascii=False))
        status = 'notfound'
        self.assertEqual(status, self.http.get_value(result, 'status'))

    def test_laster_api_is_ok(self):
        """[V2ex][LASTER] test_laster_api_is_ok"""
        result = json.loads(self.http.get(self.laster_url))
        for item in result:
            self.assertIsNotNone(self.http.get_value(item, 'title'))
            base = self.http.get_value(item, 'node')
            laster_url = self.http.get_value(base, 'url').split('/')[-1]
            self.assertEqual(self.http.get_value(base, 'name') == laster_url, True)
            print('{} == {} is True'.format(laster_url, self.http.get_value(base, 'name')))