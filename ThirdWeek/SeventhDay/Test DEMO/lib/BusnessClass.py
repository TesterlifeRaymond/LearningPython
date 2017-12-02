"""
@Name: BusnessClass
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/2
"""
import time
from .WebDriverClient import WebDriver


class BusinessApi(WebDriver):
    """"""
    def __init__(self, config):
        """ pass """
        super(BusinessApi, self).__init__()
        self.config = config
        self.img_path = 'img/'
        self.url = self.config.get('url')
        self.keywords = self.config.get('keywords')
        self.search_input_element, self.click_search_button, self.tieba_button = \
            self.config.get('xpath')
        self.assert_title, self.assert_tieba_title = self.config.get('assert_xpath')

    def baidu_search(self, url, keywords):
        self.get(url)
        self.send_keys(self.search_input_element, keywords)
        # self.click('some xpath')
        self.click(self.click_search_button)
        time.sleep(1)