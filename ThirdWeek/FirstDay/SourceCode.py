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
import time
# 写一个简单的爬虫 爬取妹子图的所有图片


class BaseCrawl:
    """ 父类 """
    def __init__(self):
        headers = {}
        headers['User-Agent'] = generate_user_agent()
        self.session = Session()
        self.session.headers = headers

    def request(self, url, encoding='utf-8', content=None):
        response = self.session.get(url)
        if response.encoding != encoding:
            response.encoding = encoding
        if content:
            return response.content
        return response.text
    
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
        self.base_url = 'http://www.meizitu.com/a/{}.html'
        self.home_page_html = self.request(self.base_url)
        # self.page_number = self.get_all_page_number()
    
    def get_all_urls(self):
        return [self.base_url.format(url) for url in range(1, 5586)]
    
    def down_load_imgs(self, xpaths, encoding='gbk'):
        for url in self.get_all_urls():
            
            name, url = self.output(url, xpaths, encoding=encoding)
            if not name or not url:
                continue
            # self.output(url, xpaths, encoding=encoding) ==》 [[name], [url]]
            # name 代表list中的第一个位置的元素
            # *url 代表除去name之后剩余在list中的全部元素的列表
            name = name[0].replace(' ', '').replace('，', '_').replace('（', '(').replace('）', ')')
            if not os.path.exists('imgs/{}'.format(name)):
                os.mkdir('imgs/{}'.format(name))

            # num = 0
            for index, pic_url in enumerate(url, 1):
                #     print(index, pic_url)
                # # for pic_url in url:
                #     num += 1
                #     print('imgs/{}/{}.jpg'.format(name, name + '_' + str(index)))
                if os.path.exists('imgs/{}/{}.jpg'.format(name, name + '_' + str(index))):
                    print('图片已经存在了！ 图片名为{}/{}.jpg'.format(name, name + '_' + str(index)))
                    continue
                print(pic_url)
                contents = self.request(pic_url, encoding='gbk', content=1)  # ==> content = 1 or content = True
                with open('imgs/{}/{}.jpg'.format(name, name + '_' + str(index)), 'wb') as img:
                    img.write(contents)
    # def get_all_page_number(self):
    #     text = self.parse(self.home_page_html, '//*[@id="wp_page_numbers"]/ul/li[14]/a/@href')[0]
    #     page_number = int(text.split('_')[1].split('.')[0])
    #     return page_number
    #
    # def get_page_info(self, page_number, xpath):
    #     if page_number > self.page_number:
    #         page_number = self.page_number
    #     resp = self.output(self.start_url.format(page_number), xpath, encoding='gbk')
    #     return resp
    #
    # def get_all_page_info(self, xpaths, page_number=None):
    #     if not page_number or page_number > self.page_number:
    #         page_number = self.page_number
    #     result = []
    #     for page_num in range(1, page_number + 1):
    #         resp = self.get_page_info(page_num, xpaths)
    #         result.append(resp)
    #     return result
    #
    # def get_img_urls(self, all_page_info_xpaths, xpath, page_number=1, encoding='utf-8'):
    #     all_result = self.get_all_page_info(all_page_info_xpaths, page_number=page_number)
    #     for item in all_result:
    #         for name, url in zip(*item):
    #             print(name, url)
    #             result = self.parse(self.request(url, encoding=encoding), xpath)
    #             for name, pic_url in zip(*result):
    #                 self.download_imgs(name, pic_url)
    #
    # def download_imgs(self, pic_name, url):
    #     partten= pic_name.split('，')
    #     pic_name = pic_name.replace('，', '_')
    #     *name, _ = partten
    #     name = '_'.join(name)
    #     if not os.path.exists('imgs/{}'.format(name)):
    #         os.mkdir('imgs/{}'.format(name))
    #     elif os.path.exists('imgs/{}/{}.jpg'.format(name, pic_name)):
    #         print('图片已经存在了！ 图片名为{}/{}.jpg'.format(name, pic_name))
    #         return
    #     contents = self.request(url, encoding='gbk')
    #
    #     with open('imgs/{}/{}.jpg'.format(name, pic_name), 'wb') as img:
    #         img.write(contents)
        

if __name__ == '__main__':
    mm = MeiZiTu()
    # xpaths = [
    #     '//*[@class="pic"]/a/img/@alt',
    #     '//*[@class="pic"]/a/@href',
    # ]
    # titles, urls = mm.get_page_info(5, xpaths)
    # for title, url in zip(titles, urls):
    #     print(title, url)
    # pic_xpaths = [
    #     '//*[@id="picture"]/p/img/@alt',
    #     '//*[@id="picture"]/p/img/@src'
    # ]
    pic_xpaths = [
        '//*[@id="maincontent"]/div[1]/div[1]/h2/a/text()',
        '//*[@class="postContent"]/p/img/@src'
    ]
    mm.down_load_imgs(pic_xpaths, encoding='gbk')
    # # mmjpg
    # mm.get_img_urls(xpaths, pic_xpaths, encoding='gbk', page_number=3)
