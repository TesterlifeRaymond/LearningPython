"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/1
"""

import unittest
# unittest 是python中的单元测试框架
# pytest, nosetest 都是python中非常优秀的自动化测试框架
# htmltestrunner， bstestrunner
# BeautifulReport


# python module, packages 两个概念
# module 是单个python文件的模块
# packages 是一个python的文件夹路径， 里面可能包含多个py的模块


class TestDemo(unittest.TestCase):
    def setUp(self):
        # 是指每次测试方法在被执行前都会调用的方法
        print('测试方法开始被执行')
    
    def tearDown(self):
        # 是每个测试方法执行后都会被调用的方法
        print('测试方法执行完成')
    
    @classmethod
    def setUpClass(cls):
        # 每个testcase的class 在执行前， 会运行一次
        print('TestDemo setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        # 每个testcase的class 在执行后， 会运行一次
        print('TestDemo tearDownClass')
    
    def test_equale_type(self):
        # self.assertEqual 他接受两个必传参数， 第三个参数为msg
        # 判断前两个参数是否相等
        print('正在调用test_equal_type测试方法')
        self.assertEqual(type(dict()), dict)
    
    def test_text_is_not_null(self):
        print('正在调用test_text_is_not_null测试方法')
        self.assertIsNone(None, True)

if __name__ == '__main__':
    unittest.main()