"""
@Name: HelloWorld
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/11
"""

# python是一门脚本语言
# python是强类型语言
# python能做什么？为什么要学习python？
# 自动化测试/机器学习/爬虫/devops/自动化运维/科学计算等

from keyword import kwlist


# print(kwlist)

if __name__ == '__main__':
    print('hello world !')
    # print, 打印
    # print函数接收一个或多个参数， 并把他们打印出来

    print(123456)

    print('abcd1234', end='')

    print('a', 'b', 'c', end='+++++++++++++++')
    print(1, 2, 3, end='\t')
    print(1+2)
    print('a'+'b')
    print(True or False)
    print(123.456)
    print(print)

    # # , 在打印的过程中， 被转换为空格显示出来
    print('1')

    # 关于python中常用的数据类型
    string = '1234'
    integer = 1234
    _float = 123.456
    _bool = True
    func = print
    _list = ['1234', abs, 1234, True, 1234]
    # list类型是可以修改的, list代表列表，可以存储多个元素，并且保留元素顺序，且元素可以被修改
    _list[2] = 666

    _tuple = ('1234', abs, 1234, True, 1234)  # tuple类型是不可修改的！

    _set = {'1234', abs, 1234, True, 1234}    # set类型， 不会保留定义时的数据位置， 并且会自动去重

    _dict = {'key': 'value', '北京': '100000'}
    # _dict = dict(key=1, 北京=1)
    # map
    # dict hashmap

    # <class 'json'> is not define ....
    # <class 'str'>
    # import json
    # print('json', type(json.dumps(_dict)))
    # None
    # null X

    # string 类型， 是字符串类型, '' or "" or """ 包裹起来的任何字符。
    # type, isinstance
    new_string_text = "1" + '1' + """123456"""
    print(type(new_string_text))
    print(type("True"))
    print(type("print"))
    print('"1234"')
    print('\'1234\'')

    print(type(123456789))   # 所有的整数
    print(type(0))
    print(type(-55555))
    print(type(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    print(500 / 30 * 2)     # int类型可以作为数学运算进行处理
    print("500" * 2)    # string类型在操作乘法时，　会打印出这个字符串 *2 的结果

    print(type(1234.56789))
    print(type(0.0))
    print(type(-123.456))
    print(type(9999999999999.999999999999999999))
    # import decimal
    #
    print(True or False)    # or 是不管你有几个对比对象， 只要其中有一个是True， 则返回True
    # if True
    # if type(123) == int
    # if isinstance(123, int)
    print(type(True))
    print(type(False))

    print(type(_list), _list)
    print(type(_tuple), _tuple)
    print(type(_set), _set)
    print(type(_dict), _dict)

    # print(type(_dict))
    # print(isinstance(_dict, dict))
    # print(dict)
    # userinfo = dict(a='b', c='d')
    # print(userinfo)
    # kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
    #  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
    #  'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    
    print('我们群有个吉祥物', '他的名字叫狗子', end=', ')
    print('狗子今年18岁')
    print('狗子没有女朋友')
    print('好吧， 狗子每天都被权限')

    name = '我们群有个吉祥物, 他的名字叫狗子'
    # 变量
    # 赋值
    # =左边是变量的名字， =右边是变量的值
    age = '狗子今年18岁'
    is_girlfriend = '狗子没有女朋友'
    diss_dog = '好吧, 狗子每天都被权限'

    # 常量
    TAGS = 'Bad Dog !'
    # 常量只定义一次， 以后不会改变， 只会引用
    # 变量会随着业务场景的变化， 而改变
    age = '狗子今年17岁'
    print(name, age, is_girlfriend, diss_dog, sep=',')
    print('狗子在群成员中的标签：', TAGS)

    # 自动化测试中， 常量的应用场景
    # adb shell
    # command.py
    # ADB_DEVICES = 'adb devices'
    # INSTALL_APK = 'adb install -r xxx.apk'
    
    dog = ['港', 22, True, False, 'my name is gang.']
    print('我的名字是：', dog[0], '我今年', dog[1], '我', dog[2], '女朋友')
