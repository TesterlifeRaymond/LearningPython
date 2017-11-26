"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/25
"""
import os
from requests import Session
from lxml import etree
from user_agent import generate_user_agent

# 写一个简单的爬虫 爬取妹子图的所有图片


class BaseCrawl:
    """ 父类 """
    def __init__(self):
        headers = {}
        headers['User-Agent'] = generate_user_agent()
        self.session = Session()
        self.session.headers = headers

    def request(self, url, encoding='utf-8'):
        response = self.session.get(url)
        if response.encoding != encoding:
            response.encoding = encoding
        return response.content
    
    def parse(self, html, xpaths):
        selector = etree.HTML(html)
        if isinstance(xpaths, (tuple, list)):
            return [selector.xpath(xpath) for xpath in xpaths]
        return selector.xpath(xpaths)
    
    def output(self, url, xpaths, encoding='utf-8'):
        html = self.request(url, encoding=encoding)
        return self.parse(html, xpaths)


class MeiZiTu(BaseCrawl):
    def __init__(self):
        super(MeiZiTu, self).__init__()
        self.start_url = 'http://www.meizitu.com/a/more_{}.html'
        self.base_url = 'http://www.meizitu.com/'
        self.home_page_html = self.request(self.base_url)
        self.page_number = self.get_all_page_number()
    
    def get_all_page_number(self):
        text = self.parse(self.home_page_html, '//*[@id="wp_page_numbers"]/ul/li[14]/a/@href')[0]
        page_number = int(text.split('_')[1].split('.')[0])
        return page_number
    
    def get_page_info(self, page_number, xpath):
        if page_number > self.page_number:
            page_number = self.page_number
        resp = self.output(self.start_url.format(page_number), xpath, encoding='gbk')
        return resp
    
    def get_all_page_info(self, xpaths, page_number=None):
        if not page_number or page_number > self.page_number:
            page_number = self.page_number
        result = []
        for page_num in range(1, page_number + 1):
            resp = self.get_page_info(page_num, xpaths)
            result.append(resp)
        return result

    def get_img_urls(self, all_page_info_xpaths, xpath, page_number=1, encoding='utf-8'):
        for name, url in zip(*self.get_all_page_info(all_page_info_xpaths, page_number=page_number)[0]):
            for name, pic_url in zip(*self.output(url, xpath, encoding=encoding)):
                self.download_imgs(name, pic_url)
    
    def download_imgs(self, pic_name, url):
        partten= pic_name.split('，')
        pic_name = pic_name.replace('，', '_')
        *name, _ = partten
        name = '_'.join(name)
        if not os.path.exists('imgs/{}'.format(name)):
            os.mkdir('imgs/{}'.format(name))
        print(url)
        contents = self.request(url, encoding='gbk')

        with open('imgs/{}/{}.jpg'.format(name, pic_name), 'wb') as img:
            img.write(contents)
        

if __name__ == '__main__':
    mm = MeiZiTu()
    xpaths = [
        '//*[@class="pic"]/a/img/@alt',
        '//*[@class="pic"]/a/@href',
    ]
    # titles, urls = mm.get_page_info(5, xpaths)
    # for title, url in zip(titles, urls):
    #     print(title, url)
    pic_xpaths = [
        '//*[@id="picture"]/p/img/@alt',
        '//*[@id="picture"]/p/img/@src'
    ]
    # mmjpg
    mm.get_img_urls(xpaths, pic_xpaths, encoding='gbk')
