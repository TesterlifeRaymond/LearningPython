"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/15
"""

user_dict = {}

beijng = user_dict.get('beijing', '北京')
# print(beijng)   # ==> 北京

# print(user_dict['beijing'])

# dict.items()

user_dict = dict(beijing='北京', shanghai='上海', tianjin='天津')
print(type(user_dict.keys()))
# print(user_dict.keys()[1])    # 我们不能直接对dict.keys() 和 dict.values()返回的类型进行下标取值
print(type(list(user_dict.keys())))
print(list(user_dict.keys())[0])   # 如果我们需要通过下标取出dict.keys or dict.values中对应index的元素， 可以用list(dict.keys())
# 转换一次类型之后再做取值行为

# for key, value in user_dict.items():
#     print(key, value)

# for key in user_dict.keys():
#     print(key, user_dict[key])

userinfo = ('Raymond', '牛仔', 'gang', '老虎')
userdict = dict.fromkeys(userinfo, 0)
# print(userdict.pop('Raymond'))
# pop输入一个key 然后删除掉字典中这个key所对应的键值对 key=value， 并返回value的值

# popitem

# print(userdict.popitem())   # pop只返回value,但是popitem返回的是key和value的一个元组
#
# userdict['Raymond'] = 1
# userdict.update(gang=10)
# userdict.setdefault('随便', 100)
#
# print(userdict)
#
#
# print(bool(userdict))
# print(bool(0))


if __name__ == '__main__':
    # try ... catch
    # try ... except
    
    # random
    # try 在python中用于捕获异常
    # 如果不分类型，捕获全部异常，则直接使用Exception
    # 如果需要指定异常类型， 则可以使用 NameError KeyError等python的异常类型
    import sys
    userdict = {}
    try:
        print(userdict['dog'])
    # except KeyError as ex:
    #     print('捕获key error异常， 他的错误信息是：', ex)
    # except NameError as ex:
    #     print('捕获name error 异常， 他的错误消息是：', ex)
    # except ValueError as ex:
    #     print('value error 异常， 他的错误消息是：', ex)
    except KeyError as msg:
        print(str(msg) + ' is  not in dict')
    except (NameError, ValueError, KeyError) as err:
        t, v, _ = sys.exc_info()
        print(t, v)
    #     print('捕获到key error 或 value error的相关错误, 错误信息为：', err)
    except Exception as ex:
        print('捕获未知异常， 异常消息为：', ex)
    #
    
    # raise , 主动抛出异常的关键字
    from time import sleep
    
    num = 0
    while num < 100:
        num += 1
        try:
            if num == 100:
                raise ValueError('num == 100 , so except')
        except ValueError as ex:
            print(num)
            print(ex)
    print(num)
    # redis = ''
    # while 1:
    #     print(num)
    #     if True:   # ==> 我们重复的尝试请求并返回错误
    #         num += 1
    #         sleep(1)
    #     if num == 3:
    #         try:
    #             raise TimeoutError('异常失败处理，重复尝试3次请求依然失败')
    #         except TimeoutError:
    #             redis.set('error_random', url)
    #

    # class ValideJsonError(Exception):
    #     """ pass """
    #     def __init__(self, msg):
    #         self.msg = msg
    #
    #     def __repr__(self):
    #         return self.msg
    #
    # raise ValideJsonError('错误的json结构体')
    #
    
    import random
    # import string
    #
    # print([item for item in dir(random) if not item.startswith('__')])
    # # baidu ==> python3 random函数详解
    #
    # print(random.randint(1, 5))
    # # 整型的伪随机数
    # print(string.ascii_letters)
    # print(string.digits)
    #
    # buf = ['@163.com', '@qq.com', '@gmail.com', '@yahoo.com']
    # head = random.sample(string.ascii_letters + string.digits, 8)
    # print(head)
    # email = ''.join(head) + random.choice(buf)
    # # print('join: 将一个列表转换成一个字符串：', ''.join(head))
    # # '分隔符'.join 快速的把一个列表转换成字符串
    # # '元素/分隔符/元素/分隔符....
    #
    # print(email)
    #
    # mobile = ['137', '138', '139', '131', '140', '150', '177']
    # print(random.choice(mobile) + str(random.randint(10000000, 99999999)))
    
    
    # class Usage(Exception):
    #     """ pass """
    #     def __init__(self, msg):
    #         self.msg = msg
    #
    #     def __repr__(self):
    #         return self.msg
    #
    #
    # raise Usage('Usage error')
    #
    
    # user_input = input('请输入一个数字:')
    # print('用户输入的数字是:', user_input)
    # input接受的类型 是一个字符串
    # input的作用是接受用户输入的一个参数, 传递给一个变量
    
    # 随机出一个数字
    # 让用户去猜
    # 如果用户持续猜错 可以选择继续猜，或者通过ctrl + c的方式结束游戏
    # 如果用户猜对了， 则自动退出
    # 如果错误， 则重新猜
    # import sys
    #
    # user_input_list = []
    # while 1:
    #     rand = random.randint(1, 11)
    #     user = input('请输入一个数字:')
    #     try:
    #         user = int(user)
    #         if user_input_list.count(user) >= 5:
    #             print('该数字输入5次，不可继续输入啦！')
    #             continue
    #         if rand == int(user):
    #             print('恭喜你，猜对了！游戏退出')
    #             break
    #         else:
    #             user_input_list.append(user)
    #             print('user : {}'.format(user), 'comp :{}'.format(rand))
    #             print('猜错了哦， 继续加油， 或者 CTRL+C退出游戏！')
    #     except KeyboardInterrupt:
    #         sys.exit(0)
    #     except ValueError:
    #         print('输入类型错误， 只接受int类型的参数')
