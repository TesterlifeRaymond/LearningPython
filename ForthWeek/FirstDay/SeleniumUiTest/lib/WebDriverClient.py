"""
@Name: WebDriverClient
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/3
"""

from selenium import webdriver
from lxml.html import fromstring


class WebDriver:
    def __init__(self):
        # lib = WebDriver()
        # init_driver => self.driver
        self.driver = self.init_driver()

    def init_driver(self):
        return webdriver.Firefox()
    
    def get(self, url):
        self.driver.get(url)

    def parse(self, xpath):
        return fromstring(self.driver.page_source).xpath(xpath)
    
    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    
    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)
    
    def check(self, xpath):
        return bool(self.parse(xpath))
    
    def switch_tabs(self):
        now_handle = self.driver.current_window_handle
        handlers = self.driver.window_handles
        for handler in handlers:
            if handler != now_handle:
                self.driver.switch_to_window(handler)
                
    

