"""
@Version: 1.0
@Project: LearningPython
@Author: Raymond
@Data: 2017/12/10 21:03
@File: CodeReview.py
@License: MIT
"""
import time
from selenium import webdriver
from lxml.html import fromstring
from requests import Session

ALL_PAGE_COUNT = 80

SEARCH_INPUT_KEY_XPATH = '//*[@id="key"]'
CHECK_ALL_IMG_BUTTON_XPATH = '//*[@class="ch all"]'
IMAGE_HREF_IN_PAGE_XPATH = '//*[@class="pic"]/ul/li/a/@href'
ALL_IMAGES_SRC_XPATH = '//*[@class="content"]/img/@src'
IMAGES_TITLE_XPATH = '//*[@class="article"]/h2/text()'


class WebdriverClient:
    """ 基础的selenium api 封装类"""
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.session = Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Upgrade-Insecure-Requests': '1'
        }
    
    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    
    def get(self, url):
        self.driver.get(url)
    
    def switch_to_windows(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != self.get_now_windows():
                self.driver.switch_to.window(handle)

    def get_now_windows(self):
        return self.driver.current_window_handle
    
    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)
    
    def parse(self, xpath):
        selector = fromstring(self.driver.page_source)
        if isinstance(xpath, (tuple, list)):
            return [selector.xpath(item) for item in xpath]
        return selector.xpath(xpath)

    def check(self, xpath, num=5):
        while num:
            pattern = self.parse(xpath)
            if pattern:
                return True
            num -= 1
        return False

    def request(self, url):
        print(url)
        response = self.session.get(url, headers=self.headers)
        if response.status_code == 404:
            raise AttributeError('访问404， 请重试')
        return response.content


class MMJpgCrawl(WebdriverClient):
    def __init__(self):
        super(MMJpgCrawl, self).__init__()
        self.start_url = 'http://www.mmjpg.com/'
        self.all_page_url = ['http://www.mmjpg.com/home/{num}'.format(num=num) for num in range(2, 81)]
    
    def get_index_page_all_images(self):
        self.get(self.start_url)
        redirect_urls = self.parse(IMAGE_HREF_IN_PAGE_XPATH)
        for url in redirect_urls:
            self.get(url)
            if self.check(CHECK_ALL_IMG_BUTTON_XPATH):
                self.click(CHECK_ALL_IMG_BUTTON_XPATH)
                if self.check(ALL_IMAGES_SRC_XPATH):
                    filename = self.parse(IMAGES_TITLE_XPATH)[0]
                    all_imgs = self.parse(ALL_IMAGES_SRC_XPATH)
                    for index, img in enumerate(all_imgs):
                        self.get(img)
                        with open('img/{}.html'.format(filename + '_{}'.format(index)), 'wb') as file:
                            file.write(self.driver.page_source.encode())
                        self.get(url)
                        if not self.check(ALL_IMAGES_SRC_XPATH):
                            time.sleep(1)
                        self.click(CHECK_ALL_IMG_BUTTON_XPATH)
                        time.sleep(3)
        self.driver.close()


if __name__ == '__main__':
    mm = MMJpgCrawl()
    mm.get_index_page_all_images()
