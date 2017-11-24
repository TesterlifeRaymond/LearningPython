"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/23
"""

# http

# 我们打开网页， http://testerlife.com?a=123&b=345   get
# request.url = http://testerlife.com
# args = {'a': '123', 'b': '456'}
# 接口测试中，或者调用服务器接口的时候。  post
# request.url = http://testerlife.com
# body = {'a': '123', 'b': '456'}
# put, delete, head, OPTIONS


# http code
# 200 成功
# 302 重定向
# 400 参数错误
# 404  not define
# 500 服务器错误

import requests
import json
from lxml import etree


html = requests.get('http://testerlife.com').text
#
#
# element = etree.HTML(html).xpath('//title/text()')
# print(etree.HTML(html).xpath('//*[@id="post-tester_4"]/div[2]/header/h1/a/text()'))
# print(etree.HTML(html).xpath('//*[@id="header"]/nav[1]/ul/li[3]/a/text()'))
# print(etree.HTML(html).xpath('//*[@id="post-tester_4"]/div[2]/div[1]/blockquote/p/text()'))
# # img src='http://xxxx.png'  //img/@src
# # a href='http://xxxxx.com'  //a/@href
#
# print(element)
# response.text ==> 这个返回中的 字符串
# method = list(filter(lambda x: not x.startswith('__'), dir(resp)))
# print(resp.status_code == 200)  # ==> 查看返回结果的status_code是否正确
# print(resp.text)
# mode='wb' ==> bytes
# response.content ==> 这个返回中的content 是一个字节流类型， bytes


class TesterlifeCrawl:
    """ 这是一个爬虫类 """
    def __init__(self):
        """ pass """
        self.page_url = 'http://testerlife.com'
        self.__name = 'testerlife'
        self.__modify_xpath = None
        self.html = self.get_page_html()
    
    def get_page_html(self):
        """ pass """
        resp = requests.get(self.page_url)
        # print resp ==> Response
        # method = list(filter(lambda x: not x.startswith('__'), dir(resp)))
        # encoding ==> 默认的编码
        # text 返回这个response的字符串类型的返回结果
        if resp.encoding != 'utf-8':
            resp.encoding = 'utf-8'
        return resp.text
    
    def parse(self, xpath):
        """
            接受一个html 和一个xpath路径， 并返回html解析后的结果
        :param html: 一个html
        :param xpath: 一个xpath路径
        :return: 返回lxml解析html后的指定的xpath路径的数据
        """
        result = etree.HTML(self.html).xpath(xpath)
        self.__modify_xpath = None
        return result
    
    def set_xpaths(self, xpath):
        """ 接受一个xpath参数 """
        self.__modify_xpath = xpath
    
    def __repr__(self):
        if self.__modify_xpath:
            return json.dumps(self.parse(self.__modify_xpath), ensure_ascii=False, indent=4)
        return '没有指定xpaths属性， 请使用set_xpaths方法 指定需要获取数据的位置'


class TesterHome(TesterlifeCrawl):
    """ pass """
    def __init__(self):
        """ pass """
        super(TesterHome, self).__init__()
        self.page_url = 'http://testerhome.com'
        self.__name = 'testerhome'
        self.html = self.get_page_html()


class QiuBai(TesterlifeCrawl):
    def __init__(self):
        super(QiuBai, self).__init__()
        self.page_url = 'https://www.qiushibaike.com/'
        self.__name = 'qiushibaike'
        self.html = self.get_page_html()


class Crawl:
    """ pass """
    def __init__(self, url, name):
        self.url, self.name = url, name
    
    def request(self, url):
        resp = requests.get(url)
        if resp.encoding != 'utf-8':
            resp.encoding = 'utf-8'
        return resp.text
    
    def parse(self, html, xpaths):
        element = etree.HTML(html)
        if isinstance(xpaths, (tuple, list)):
            # return list(filter(lambda x: element.xpath(x), xpaths))
            return [element.xpath(xpath) for xpath in xpaths]
        return element.xpath(xpaths)
    
    def output(self, url, xpath):
        html = self.request(url)
        return self.parse(html, xpath)


class QiuShiBaiKe(Crawl):
    def __init__(self, url, name):
        super(QiuShiBaiKe, self).__init__(url, name)
    
    def allinfo(self, xpaths):
        return json.dumps(self.output(self.url, xpaths), ensure_ascii=False, indent=4)
        

if __name__ == '__main__':
    qb = QiuShiBaiKe('https://www.qiushibaike.com/', 'qb')
    xpaths = [
        '//h2/text()',
        '//*[@class="content"]/span/text()',
        '//*[@class="stats"]/span/i/text()'
    ]
    print(qb.allinfo(xpaths))
    # crawl = TesterlifeCrawl()
    # xpaths = [
    #     '//*[@id="post-tester_4"]/div[2]/div[1]/blockquote/p/text()',
    #     '//a[@class="article-title"]/text()',
    #     '//a[@class="article-title"]/@href',
    #     '//*[@class="article-date"]/time/@datetime'
    # ]
    # for item in xpaths:
    #     crawl.set_xpaths(item)
    #     print(crawl)
    # crawl.set_xpaths('//*[@id="post-tester_4"]/div[2]/div[1]/blockquote/p/text()')
    # print(crawl)
    # crawl.set_xpaths('//a[@class="article-title"]/text()')
    # print(crawl)
    # crawl.set_xpaths('//a[@class="article-title"]/@href')
    # print(crawl)
    # crawl.set_xpaths('//*[@class="article-date"]/time/@datetime')
    # # print(crawl)
    # # print(crawl)
    #
    # for xpath in xpaths:
    #     crawl.set_xpaths(xpath)
    #     print(crawl)
    # testerhome = TesterHome()
    # xpaths = [
    #     '//*[@class="title media-heading"]/a/@title',
    #     '//*[@class="info"]/a/@data-name',
    #     '//*[@class="title media-heading"]/a/@href',
    #
    # ]
    # for xpath in xpaths:
    #     testerhome.set_xpaths(xpath)
    #     print(testerhome)
    #
