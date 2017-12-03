"""
@Name: Business
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/3
"""
import time
from .WebDriverClient import WebDriver


class BusinessApi(WebDriver):
    def __init__(self, config):
        super(BusinessApi, self).__init__()
        try:
            self.config = config.get('home_page')
            self.url = self.config.get('start_url')
            self.kw_xpath, self.button_xpath, self.baike_xpath = self.config.get('xpath')
            self.keywords = self.config.get('keyword')
            self.baike_url = config.get('baike').get('start_url')
            self.baike_assert = config.get('baike').get('assert_xpath')[0]
        except:
            pass

    def baidu_search(self, keyword=None):
        self.get(self.url)
        if not keyword:
            keyword = self.keywords
        self.send_keys(self.kw_xpath, keyword)
        self.click(self.button_xpath)
        time.sleep(1)
    
    def baidu_baike(self):
        self.get(self.baike_url)
