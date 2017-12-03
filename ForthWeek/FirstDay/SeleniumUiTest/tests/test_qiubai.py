"""
@Name: test_qiubai
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/3
"""
import unittest
import time
from lib.Business import BusinessApi
from config import Config


class TestBaiDu(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('baidu')
        cls.assert_xpath = cls.config.get('home_page').get('assert_info')[0]
        
    def setUp(self):
        self.lib = BusinessApi(self.config)
        self.driver = self.lib.driver
        
    def tearDown(self):
        self.driver.quit()
    
    def test_baidu_home_page(self):
        """[百度][主页] 测试主页请求正确"""
        self.lib.baidu_search()
        self.assertIsNotNone(self.lib.check(self.assert_xpath))
        self.assertEqual(self.lib.check(self.assert_xpath), True)
    
    def test_click_baike(self):
        """[百度][主页] 从百度主页点击按钮进入百度百科"""
        self.lib.baidu_search()
        self.lib.click(self.lib.baike_xpath)
        time.sleep(2)
        self.lib.switch_tabs()
        self.assertEqual(self.lib.parse(self.assert_xpath)[0], '{}_百度百科'.format(self.lib.keywords))

    def test_get_baike_appname(self):
        """[百度][百科] 从百科页面直接进入，查询app名字正确"""
        self.lib.baidu_baike()
        self.assertEqual(self.lib.parse(self.lib.baike_assert)[0].strip(), self.lib.keywords)
    
    