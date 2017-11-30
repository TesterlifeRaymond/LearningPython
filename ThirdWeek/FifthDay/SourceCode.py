"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/30
"""
import time
import json
import selenium
from selenium import webdriver
from lxml.html import fromstring
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium

HOME_INPUT_SEARCH_XPAHT = '//*[@id="vue-index"]/section/article/div[2]/div/div/input'
HOME_SEARCH_BUTTON_XPATH = '//*[@id="vue-index"]/section/article/div[2]/div/a[2]'
SEARCH_APP_LIST_XPATH = '//*[@title="{}"]'
VERSION_SELECT_BUTTON_XPATH = '//*[@id="vue-version"]/div[2]/div[2]/div[5]/div[2]/div/div/div/button'
WANDOUJIA_VERSION_BUTTON = '//*[@id="vue-version"]/div[2]/div[2]/div[5]/div[2]/div/div/div/div/ul/li[4]/a'


def retry(func):
    def wrap(*args, **kwargs):
        num = 0
        result = None
        while 1:
            try:
                result = func(*args, **kwargs)
                break
            except Exception as err:
                print(err)
                num += 1
                time.sleep(1)
            if num == 5:
                raise AssertionError('元素未找到！')
        return result
    return wrap


class WebDriverClient:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def check_elements(self, xpaths):
        return bool(self.driver.find_element_by_xpath(xpaths))
    
    def parse(self, xpath):
        # page_source 是当前页面的html源码
        # fromstring(html).xpaht 的返回结果是xpath命中的元素的值
        return fromstring(self.driver.page_source).xpath(xpath)
    
    @retry
    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    
    @retry
    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def implicitly_wait(self, timeout=10):
        self.driver.implicitly_wait(timeout)
    
    def close(self):
        self.driver.close()


class AndroidCoolChuan(WebDriverClient):
    def __init__(self, package='com.tencent.mm', appname='微信'):
        super(AndroidCoolChuan, self).__init__()
        self.package = package
        self.appname = appname
        self.home_url = 'http://android.kuchuan.com/page/detail/index'
        self.all_data_url = 'http://android.kuchuan.com/dailydownload?packagename={}&status=-1&date={}'.format(
            self.package, int(time.time() * 1000))

    def get_appinfo_page(self):
        self.driver.get(self.home_url)
        self.send_keys(HOME_INPUT_SEARCH_XPAHT, self.appname)
        self.click(HOME_SEARCH_BUTTON_XPATH)
        self.click(SEARCH_APP_LIST_XPATH.format(self.appname))
        
    def get_all_datas(self):
        self.get_appinfo_page()
        time.sleep(3)
        self.driver.get(self.all_data_url)
        result = str(self.parse('//text()')[0])
        print(result, type(result))
        data_dict = json.loads(result)
        print(data_dict, type(data_dict))
    
        # json.loads 是把一个json结构体(是字符串类型的字典)转换成dict类型
        # str ==> dict

    def detail_version(self):
        time.sleep(5)
        self.driver.get('http://android.kuchuan.com/page/detail/v'
                        'ersion?package=com.tencent.mobileqq&infomarketid=1&site=0')
        self.click(VERSION_SELECT_BUTTON_XPATH)
        self.click(WANDOUJIA_VERSION_BUTTON)
        self.close()
        

if __name__ == '__main__':
    # wechat = AndroidCoolChuan('com.tencent.mobileqq', 'QQ')
    # wechat.detail_version()
    wechat = AndroidCoolChuan('com.tencent.tmgp.sgame', '王者荣耀（全心出击）')
    wechat.get_all_datas()
    wechat.detail_version()
    