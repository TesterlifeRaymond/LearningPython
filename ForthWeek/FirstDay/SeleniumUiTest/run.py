"""
@Name: run
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/3
"""
import unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
    # test_baidu.py
    # test_sogou.py
    # test_soho.py
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
