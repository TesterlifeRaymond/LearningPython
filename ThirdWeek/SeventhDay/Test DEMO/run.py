"""
@Name: run.py
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/1
"""

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests/baidu', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
    
# def suite():
#     loader = unittest.TestLoader()
#     suite = loader.discover(r'tests\login', pattern='test_*.py')
#     return suite
#
#
# if __name__ == '__main__':
#     suite = suite()
#     print(suite)
#     unittest.main(defaultTest='suite')

"""
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    return suite
"""