"""
@Name: run.py
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/1
"""

import unittest


def suite():
    loader = unittest.TestLoader()
    suite = loader.discover(r'tests\login', pattern='test_*.py')
    return suite


if __name__ == '__main__':
    suite = suite()
    print(suite)
    unittest.main(defaultTest='suite')

"""
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    return suite
"""