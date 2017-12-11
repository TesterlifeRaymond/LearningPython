"""
@Version: 1.0
@Project: LearningPython
@Author: Raymond
@Data: 2017/12/11 21:06
@File: CodeReviewSecond.py
@License: MIT
"""

from selenium import webdriver
from lxml.html import fromstring
import time, random


class WebDriverClient:
    """ pass """
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    
    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)
    
    def parse(self, xpath):
        html = self.driver.page_source.replace('<em>', '').replace('</em>', '')
        return fromstring(html).xpath(xpath)

    def check(self, xpath):
        return bool(self.parse(xpath))
    
    def get(self, url):
        self.driver.get(url)


class JanDan(WebDriverClient):
    def __init__(self):
        super(JanDan, self).__init__()
        self.all_img_urls = 'http://baidu.com'
        self.input_xpath = '//*[@id="kw"]'
        self.click_xpath = '//*[@id="su"]'
        self.titles_xpath = '//h3[@class="t"]/a'

    def run(self):
        """ for key in keys:
                jd.run(key)
        """
        n = 0
        self.get(self.all_img_urls)
        self.send_keys(self.input_xpath, '妹子图')
        self.click(self.click_xpath)
        while n < 11:
            n += 1
            time.sleep(1)
            for item in self.parse(self.titles_xpath):
                print(item.xpath('text()'), item.xpath('@href'))
            self.click('//a[text()="下一页>"]')
        self.driver.close()

    def meizitu(self):
        urls = ['http://jandan.net/ooxx/page-{}#comments'.format(num) for num in range(1, 378)]
        for url in urls:
            self.get(url)
            time.sleep(random.randint(2, 5))
            print(self.parse('//p/img/@src'))


if __name__ == '__main__':
    jd = JanDan()
    jd.meizitu()
