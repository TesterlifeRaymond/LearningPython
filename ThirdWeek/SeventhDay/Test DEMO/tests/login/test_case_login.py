"""
@Name: test_case_login
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/1
"""
# root path 是TestDemo这个文件夹下的路径
# 如果需要引入packages 或module中的工具类或者模块， 引入层级的第一级为root path
# 我们当前项目 root path中包含1个run文件 和3个文件夹

import lib
import os
import time
from config import Config
import unittest
from BeautifulReport import BeautifulReport


class TestHomeCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('login')
        cls.img_path = 'img/'
        cls.url = cls.config.get('url')
        cls.username = cls.config.get('username')
        cls.password = cls.config.get('password')
        cls.inpu_username, cls.input_password, cls.click_login_button = \
            cls.config.get('xpath')
        cls.assert_info = cls.config.get('assert_xpath')[0]
    
    def setUp(self):
        self.lib = lib.WebDriver()
        self.driver = self.lib.driver
    
    def tearDown(self):
        self.driver.quit()

    def test_config_enum_is_ok(self):
        print('test start with test_config_enum_is_ok')
        self.assertIsNotNone(self.config)
        self.assertIsNotNone(self.username)
        self.assertIsNotNone(self.url)
        self.assertIsNotNone(self.password)

    # def test_testerhome_login(self):
    #     self.lib.get(self.url)
    #     self.lib.send_keys(self.inpu_username, self.username)
    #     self.lib.send_keys(self.input_password, self.password)
    #     self.lib.click(self.click_login_button)
    #     time.sleep(5)
    #     assert_info = self.lib.parse(self.assert_info)[0]
    #     self.assertEqual(assert_info, self.password)
    #
    # @BeautifulReport.add_test_img('testerlife')
    # def test_testerhome_page(self):
    #     self.lib.get('http://testerlife.com')
    #     time.sleep(3)
    #     path = os.path.abspath(self.img_path + 'testerlife.png')
    
    @BeautifulReport.add_test_img('testerlife')
    def test_show_img_in_report(self):
        """ 展示截图在report.html中"""
        print('测试完成')

# __main__是告诉你， 你的文件入口是谁
if __name__ == '__main__':
    unittest.main()