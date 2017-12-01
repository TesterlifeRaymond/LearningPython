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
        self.assertEqual(1, 1)

    def test_not_null(self):
        self.assertIsNotNone('text')
    
    def test_null(self):
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main()