"""
@Name: wether
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/6
"""

import json
import unittest
from lib.client import HttpHandler


class JuHeWeChat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://v.juhe.cn/weixin/query'
        cls.http = HttpHandler()
    
    def test_wether_api_methos_post(self):
        """[JuHe][WeChat] 测试聚合wechatApi请求结果正确"""
        data = {
            'key': '4beb9d77d2b95ce9bec6d8363ee5a620',
            'ps': 40
        }
        result = json.loads(self.http.post(self.url, data=data))
        list_info = self.http.get_value(result, 'list')
        for item in list_info:
            print(self.http.get_value(item, 'title'))
            self.assertIsNotNone(self.http.get_value(item, 'title'))
        self.assertEqual(result.get('reason'), '请求成功')
        self.assertEqual(self.http.get_value(result, 'ps'), data.get('ps'))
        self.assertEqual(result.get('error_code'), 0)
        self.assertIsNotNone(result.get('result'))
