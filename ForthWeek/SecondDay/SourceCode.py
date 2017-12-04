"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/4
"""
import requests
import json
from lxml import etree
# douban search book api
# https://api.douban.com/v2/book/search
# 这是接口的请求地址
# 如果想要把一个参数传递给一个get请求， 那么我们需要在这个接口最后的位置增加一个?
# url?param_key=param_value&param_b=param
# get方法中传递的入参 以&符号分割
# baidu.com?q=三国演义


# api_url = 'https://api.douban.com/v2/book/search?q={}'
# # ?q={}
# book_name = '三国演义'
# result = requests.get(api_url.format(book_name)).json()
# response.json() 返回的是一个字典类型的数据结构
# json.dumps 是将一个字典类型的数据转换成string类型
url = 'https://api.douban.com/v2/movie/search?tag={}'
keyword = '喜剧'
print(json.dumps(requests.get(url.format(keyword)).json(), ensure_ascii=False, indent=4))

#
# data = result.get('books')
#
# for item in data:
#     print(json.dumps(item, ensure_ascii=False, indent=4))
#     print('======================')
#
# key = 'e53c5f18346ba5e40309fdf7574ee25b'
# url = 'http://op.juhe.cn/onebox/news/query?key={}&q={}'
#
# url = url.format(key, '红黄蓝')
# result = requests.get(url).text
# print(result)
#
#
# url = 'http://v.juhe.cn/weather/index?format=2&cityname={}&key={}'
# city_name = '北京'
# key = '8914a2e03dc4cbed5178b9b5464496fc'
#
# url = url.format(city_name, key)
#
# result = requests.get(url).json()
# print(result.keys())
# print(result.get('result').keys())
#
#
# url = 'http://v.juhe.cn/movie/index?key=e37f646f17ef5d6e6d0c37037263e9f6&title={}'
# # title = '战狼2'
# title = '美国队长'
# result = requests.get(url.format(title)).json()
# data = json.dumps(result, ensure_ascii=False, indent=4)
# print(data)
#
#
# for item in result.get('result').get('future'):
#     print(item)
# print(result.get('result').get('sk'))
# print(result.get('result').get('today'))
# # future 是一周的天气预报的列表
# # tody 是今天的天气预报的信息
# # sk 代表的风向和风的级数
#
#
# assert result.get('reason') == 'successed!'
# assert result.get('error_code') == 0
# print(result)
# string_result = json.dumps(result, indent=4, ensure_ascii=False)
# print(string_result)
#
#
# api_url = 'https://api.douban.com/v2/book/search?tag={}'
# tag = 'Python'
#
# result = json.dumps(requests.get(api_url.format(tag)).json(), indent=4, ensure_ascii=False)
# print(result)
# # http 在接口测试中 我们常用的是get 和post
# # put delete
#

url = 'http://v.juhe.cn/weixin/query?key={}'
key = '4beb9d77d2b95ce9bec6d8363ee5a620'
result = requests.get(url.format(key)).json()
data = result.get('result').get('list')
# data ==> [{}, {}, {}, {}]
# for item in data:
#    type(item) ==> dict
for item in data:
    print(json.dumps(item, indent=4, ensure_ascii=False))
    print('=================')
#
#
url = 'https://testerhome.com/account/sign_in'

session = requests.Session()
result = session.get(url).text
csrf = etree.HTML(result).xpath('//*[@name="csrf-token"]/@content')[0]
print(csrf)

headers = {}
headers['X-CSRF-Token'] = csrf

data = {
    'utf8': '✓',
    'user[login]': '2839889878@qq.com',
    'user[password]': 'abcd1234',
    'user[remember_me]':1,
    'commit': '登录'
}

result = session.post(url, data=data, headers=headers).text
print(etree.HTML(result).xpath('//*[@href="/abcd1234"]/text()'))
print(result)
#
#
# url = 'http://apis.juhe.cn/cook/query'
# data = {
#     'menu': '鱼香肉丝',
#     'key': '338ce1ecb756bf7ca4772fbb9f11cd75',
# }
# # http://apis.juhe.cn/cook/query?menu=鱼香肉丝&key=338ce1ecb756bf7ca4772fbb9f11cd75
# # get url
#
#
#
# result = requests.post(url, data=data).json()
# data = result.get('result').get('data')
# for item in data:
#     # print(json.dumps(item, ensure_ascii=False, indent=4))
#     print(json.dumps(item.get('id'), ensure_ascii=False, indent=4))
#     print(json.dumps(item.get('tags'), ensure_ascii=False, indent=4))
#     print('========================')
