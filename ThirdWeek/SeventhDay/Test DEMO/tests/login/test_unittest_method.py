"""
@Name: test_unittest_method
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/1
"""

import unittest


class MethodTest(unittest.TestCase):
    def test_equal(self):
        """ 测试1=1 为真"""
        self.assertEqual(1, 1)

    def test_not_null(self):
        """测试我们传递的信息不为None"""
        self.assertIsNotNone('text')
    
    def test_null(self):
        """测试我们传递的信息为None"""
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main()