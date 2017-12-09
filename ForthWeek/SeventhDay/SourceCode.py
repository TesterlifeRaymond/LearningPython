"""
@Version: 1.0
@Project: LearningPython
@Author: Raymond
@Data: 2017/12/9 21:08
@File: SourceCode.py
@License: MIT
"""
# python web
# django, tornado, flask

# django ==> 大部分组件化已经完成， 只需要直接引用就可以了
# tornado ==> python web的异步web框架
# flask ==> 微服务web框架，但是他的功能和插件一点都不微

from flask import Flask, request

app = Flask(__name__)


@app.route('/gang')
def index():
  args = dict(request.args)
  print(args)
  return '<h1>Hello ! {} , your password is {} </h1>'.format(args.get('name')[0], args.get('password')[0])


if __name__ == '__main__':
    app.run()


# import random
# import string
# import unittest
# from BeautifulReport import BeautifulReport
#
# class BaseDataClass:
#     def mobile(self, head=None):
#         if not head:
#             head = random.choice(['130', '131', '132', '133', '134', '135', '136', '137', '138'])
#         return head + ''.join(random.sample(string.digits, 8))
#
#     def password(self, lenth=None, small_letters='lower', digits=None, punctuation=None):
#         if not lenth:
#             lenth = random.randint(6, 12)
#         if not digits:
#             digits = ''
#         ascii_info = {
#             'lower': string.ascii_lowercase,
#             'upper': string.ascii_uppercase,
#             'all': string.ascii_letters
#         }.get(small_letters)
#         if not ascii_info:
#             raise AttributeError('没有找到定义， 当前定义包含["lower", "upper", "all"]')
#
#         if not punctuation:
#             punctuation = ''
#         result = ''.join(random.sample(ascii_info + digits + punctuation, lenth))
#         return result
#
#     def email(self, foot=None):
#         if not foot:
#             foot = random.choice(['@163.com', '@qq.com', '@soho.com', '@aliyun.com'])
#         return self.password(lenth=8) + foot
#
#
# class TestBase(unittest.TestCase):
#     """ utx : ==> github  jianbing"""
#     @classmethod
#     def setUpClass(cls):
#         cls.base = BaseDataClass()
#         cls.base_head = ['130', '131', '132', '133', '134', '135', '136', '137', '138']
#
#     def test_mobile(self):
#         self.assertTrue(self.base.mobile()[:3] in self.base_head)
#
#
#
# if __name__ == '__main__':
#     suite = unittest.defaultTestLoader.discover('.', 'SourceCode.py')
#     report = BeautifulReport(suite)
#     report.report(description='基础的测试报告')
    # base = BaseDataClass()
    # # print(base.password(lenth=8, small_letters='111', digits=string.digits))
    # print(base.email())

# import json
# from collections import namedtuple
# from random import shuffle
# from itertools import zip_longest
#
# n_groups = lambda seq, n: zip_longest(*[iter(seq)]*n)
#
# Card = namedtuple('Poker', ['Color', 'Number'])
#
#
# class Cards:
#         ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
#         colors = ['黑桃', '红桃', '方片', '草花']
#         lasts = None
#
#         def __init__(self):
#             self._cards = [Card(color, rank)
#                            for color in self.colors
#                            for rank in self.ranks] \
#                           + [['King', 'Big'], ['King', 'Samll']]
#
#         def __len__(self):
#             return len(self._cards)
#
#         def __repr__(self):
#             result = self._cards.copy()
#             shuffle(result)
#             self.lasts = [result.pop() for _ in range(3)]
#             return json.dumps(result, ensure_ascii=False)
#
#         def get_hand(self):
#             return self.lasts
#
#
# if __name__ == '__main__':
#     card = Cards()
#     result = list(n_groups(json.loads(str(card)), 17))
#     user_a, user_b, user_c = result
#     print(user_a)
#     print(user_b)
#     print(user_c)
#     print('++++++++++++++')
#     print(card.get_hand())
#     for item in card.get_hand():
#         print(item.Color, item.Number)