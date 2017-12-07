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


class ChildrenApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.remote_ip = 'http://182.92.178.14/page'
        cls.register_url = 'http://182.92.178.14/api/v1/register'
        cls.login_url = 'http://182.92.178.14/api/v1/login'
        cls.userinfo_url = 'http://182.92.178.14/api/v1/userInfo'
        cls.history_task_url = 'http://182.92.178.14/api/v1/userQuestion'
        cls.score = 'http://182.92.178.14/api/v1/userScore'
        cls.http = HttpHandler()
    
    def test_remote_ip(self):
        """[Child][RemoteIp] 测试请求端ip正确"""
        result = json.loads(self.http.get(self.remote_ip))
        assert_info = {
            'origin': "118.247.186.155"
        }
        print(json.dumps(result, ensure_ascii=False, indent=4))
        self.assertEqual(result == assert_info, True)
        self.assertEqual(self.http.valid_json(result, 'child', 'remote_ip'), True)
    
    # orm
    def test_user_1_register_is_ok(self):
        """[Child][Register] 测试一个用户注册正确"""
        mobile = self.http.mobile()
        # print(self.http.mobile() != self.http.mobile())
        param = {"username": mobile, "password": "1234567"}
        print(mobile, '1234567')
        result = json.loads(self.http.post(self.register_url, data=param))
        print(result)
        self.assertEqual(result.get('message'), 'success')
        self.assertEqual(result.get('auth'), 'user')
        self.assertEqual(result.get('username'), mobile)
        self.assertEqual(self.http.valid_json(result, 'child', 'register_success'), True)

    def test_user_2_login_is_ok(self):
        """[Child][Login] 测试刚刚注册的用户登陆成功"""
        mobile = '13243286910'
        param = {"username": mobile, "password": "1234567"}
        result = json.loads(self.http.post(self.login_url, data=param))
        print(result)
        self.assertEqual(self.http.valid_json(result, 'child', 'login_success'), True)
        self.assertEqual(result.get('message'), 'success')
        self.assertEqual(result.get('auth'), 'user')
        self.assertEqual(result.get('username'), mobile)

    def test_get_user_info_is_ok(self):
        """[Child][UserInfo] 查询全部用户信息接口返回正确"""
        result = json.loads(self.http.get(self.userinfo_url))
        self.assertEqual(result.get('message'), 'success')
        self.assertIsNotNone(result.get('attribute'))
        for item in self.http.get_value(result, 'attribute')[0]:
            self.assertEqual(self.http.valid_json(item, 'child', 'item_info'), True)

    def test_get_history_tasks_is_ok(self):
        """[Child][HistoryTasks] 查询用户历史答题记录"""
        param = {'username': 'yy'}
        result = json.loads(self.http.post(self.history_task_url, json=param))
        print(result)
        result = json.loads(result)
        self.assertIsNotNone(result.get('response'))
        self.assertEqual(result.get('message'), 'success')
        self.assertEqual(self.http.valid_json(result, 'child', 'history'), True)

    def test_get_history_tasks_is_false(self):
        """[Child][HistoryTasks] 查询用户历史答题记录"""
        param = {'username': '13243286910'}
        result = json.loads(self.http.post(self.history_task_url, json=param))
        print(result)
        result = json.loads(result)
        self.assertIsNotNone(result.get('response'))
        self.assertEqual(result.get('message'), 'success')
        self.assertEqual(self.http.valid_json(result, 'child', 'history'), True)
    
    def test_user_score_info(self):
        """[Child][UserScore] 查询用户某次答题记录"""
        param = {'username': 'yy', 'score_id': 1}
        result = json.loads(self.http.post(self.score, json=param))
        print(result)
        for item in json.loads(self.http.get_value(result, 'question')):
            print(json.dumps(item), "<br></br>")
            self.assertEqual(self.http.valid_json(item, 'child', 'score'), True)
        self.assertEqual(result.get('titleNum'), '30')