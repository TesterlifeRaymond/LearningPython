"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/24
"""

import requests
import json
from lxml import etree


class BaseCrawl:
    def __init__(self):
        pass

    def request(self, url, encoding='utf-8'):
        response = requests.get(url)
        if response.encoding != 'utf-8':
            response.encoding = encoding
        return response.text

    def parse(self, html, xpaths):
        selector = etree.HTML(html)
        if isinstance(xpaths, (tuple, list)):
            return [selector.xpath(xpath) for xpath in xpaths]
        return selector.xpath(xpaths)

    def output(self, url, xpath):
        html = self.request(url)
        return self.parse(html, xpath)


class QiuBai(BaseCrawl):
    def __init__(self):
        super(QiuBai, self).__init__()
        self.home_page_url = 'https://www.qiushibaike.com/'
        self.html = self.request(self.home_page_url)
    
    def get_all_users(self):
        result = self.parse(self.html, '//h2/text()')
        # user_names = list(filter(lambda x: (x.replace('\n', '')), result))
        user_names = [item.strip() for item in result]
        return user_names

    def get_like_number(self):
        return self.parse(self.html, '//span[@class="stats-vote"]/i/text()')
    
    def get_user_content(self):
        selector = self.parse(self.html, '//div[@class="content"]')
        result = []
        for item in selector:
            result.append(','.join(item.xpath('span/text()')).strip())
        return result
        # return [','.join(item.xpath('span/text()')).strip() for item in selector]
        # print(selector)
        # return json.dumps(self.parse(self.html, '//div[@class="articleGender manIcon"]/text()'), indent=4)
    

class BaiSiBuDeJie(BaseCrawl):
    def __init__(self):
        super(BaiSiBuDeJie, self).__init__()
        self.home_page_url = 'http://www.budejie.com/text/'
        self.html = self.request(self.home_page_url)
    
    def get_all_users(self):
        result = self.parse(self.html, '//*[@class="u-txt"]/a/text()')
        return result
    
    def get_like_numbers(self):
        result = self.parse(self.html, '//*[@class="j-r-list-tool-l-up"]/span/text()')
        return result
    
    def get_user_contents(self):
        result = self.parse(self.html, '//*[@class="j-r-list-c-desc"]')
        return [','.join(item.xpath('a/text()')) for item in result]


if __name__ == '__main__':
    # bsbdj = BaiSiBuDeJie()
    # users = bsbdj.get_all_users()
    # likes = bsbdj.get_like_numbers()
    # contents = bsbdj.get_user_contents()
    # for user, like, content in zip(users, likes, contents):
    #     print('====' * 5)
    #     print('用户：{}发表了一个段子 \n 段子：{} \n有{}用户喜欢这个段子'.format(user, content.replace('\n', ',').strip(','), like))
    #     print('====' * 5)
    
    
    
    qb = QiuBai()
    # users = qb.get_all_users()
    # like_numbers = qb.get_like_number()
    user_contents = qb.get_user_content()
    #
    # for user, like, content in zip(users, like_numbers, user_contents):
    #     print('====' * 5)
    #     print('用户：{}发表了一个段子 \n 段子：{} \n有{}用户喜欢这个段子'.format(user, content.replace('\n', ',').strip(','), like))
    #     print('====' * 5)
    # crawl = BaseCrawl()
    # html = crawl.request('http://testerlife.com')
    # topic_tags_href = crawl.parse(html, '//*[@class="article-tag-list-item"]/a/@href')
    # topic_tags = crawl.parse(html, '//*[@class="article-tag-list-item"]/a/text()')
    # print(topic_tags_href)
    # print(topic_tags)
    # for tag, href in zip(topic_tags, topic_tags_href):
    #     print(tag, href)
        
    # topics = crawl.parse(html, '//*[@class="article-title"]/text()')
    # tags = crawl.parse(html, '//*[@class="switch-part switch-part1"]/nav[@class="header-menu"]/ul/li/a/text()')
    # hrefs = crawl.parse(html, '//*[@class="switch-part switch-part1"]/nav[@class="header-menu"]/ul/li/a/@href')
    #
    # # print(topics)
    # print(tags)
    # print(hrefs)
    # for tag, href in zip(tags, hrefs):
    #     print(tag, href)