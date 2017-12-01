"""
@Name: __init__.py
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/12/1
"""


class Config:
    enum = {
        'login': {
            'url': 'https://testerhome.com/account/sign_in',
            'username': '2839889878@qq.com',
            'password': 'abcd1234',
            'xpath': [
                '//input[@id="user_login"]',   # input username
                '//input[@id="user_password"]',   # input password
                '//input[@value="登录"]'   # click login button
            ],
            'assert_xpath': [
                '/html/body/div[1]/nav/div/ul[1]/li/ul/li[1]/a/text()'
            ]
        }
    }