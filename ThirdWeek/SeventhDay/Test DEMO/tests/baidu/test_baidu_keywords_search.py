"""
@Name: test_baidu_keywords_search
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/2
"""
import lib
from config import Config
import unittest
from BeautifulReport import BeautifulReport

# 原子化层级， WebdDiverClient, Config
# 业务封装层级， page object ， Business， 封装了多个业务方法
# 测试方法层级， 他只调用业务层级的逻辑关系， 除非业务逻辑和顺序发生变化， 否则不做修改


class BaiDuTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('baidu')
    
    def setUp(self):
        self.lib = lib.BusinessApi(self.config)
        self.driver = self.lib.driver
    
    def tearDown(self):
        self.driver.quit()
    
    def test_config_enum_is_ok(self):
        """[百度][Config] 验证百度config文件是否正确"""
        print('test start with test_config_enum_is_ok')
        self.assertIsNotNone(self.lib.config)
        self.assertIsNotNone(self.lib.keywords)
        self.assertIsNotNone(self.lib.url)
        self.assertIsNotNone(self.lib.assert_title)
        print('断言所有配置文件不为None')

    def test_baidu_search_is_ok(self):
        """[百度][TEST] 在百度首页输入搜索关键字，确认返回结果正确"""
        print('在百度搜索中输入{}关键字进行查询并跳转到查询结果页面')
        self.lib.baidu_search(self.lib.url, self.lib.keywords)
        print('断言测试结果 {} 不为None'.format(self.lib.parse(self.lib.assert_title)))
        # self.go_to_some_path_and_click_elments(xxxx)
        self.assertIsNotNone(self.lib.parse(self.lib.assert_title))
        self.assertEqual(self.lib.parse(self.lib.assert_title)[0], '{}_百度搜索'.format(self.lib.keywords))
    
    @BeautifulReport.add_test_img('test')
    def test_baidu_tieba(self):
        """[百度][TEST] 测试搜索后，跳转到贴吧中的title与预期结果一致"""
        print('在百度搜索中输入{}关键字进行查询并跳转到查询结果页面'.format(self.lib.keywords))
        self.lib.baidu_search(self.lib.url, self.lib.keywords)
        print('跳转到结果页面中的贴吧页面')
        # self.lib.driver.get_screenshot_as_file('img/test.png')
        print('将当前页面进行图片存储')
        self.lib.click(self.lib.tieba_button)
        print('断言页面中的内容与我们的预期结果一致')
        self.assertEqual(str(self.lib.parse(self.lib.assert_tieba_title)[0]).strip(), '淘宝网吧')
