"""
@Name: SouceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/14
"""

# dir(dict)

# dir用来查看入参的全部方法
# [dict.modules, clear, fromkeys, keys, values, pop, popitem]

# dict_moduemailles = [item for item in dir(dict) if not '__' in item]
# print(dict_modules)
# clear 是清空字典中的所有键值对， key=value
# copy  是复制一个字典全部的key value
# fromkeys 是接受一个列表或元组， 并把元组中的所有元素作为key， 默认赋值key的value为None

userinfo = ('Raymond', '牛仔', 'gang', '老虎')
userdict = dict.fromkeys(userinfo, 0)
# print(userdict)

# dict 的取值方式有两种，第一种是.get(key, default)， 第二种是dict['key']
# dict.get(key, default) 当key在字典中不存在的时候， 默认返回None，如果定义default的参数， 则返回default
# dict['key'] 的取值方式中， 如果key不存在与字典中， 则直接抛出KeyError的异常

# print("userdict.get('suibian')", userdict.get('suibian'))
# print("userdict.get('suibian', '有点随便')", userdict.get('suibian', '有点随便'))
# print(userdict['suibian'])

# dict.items , 他会返回一个dict_items的类型，一般使用场景是在for循环的时候，同时取出key 和对应的value

# for key in userdict.keys():
#     print(key, userdict[key])

# print(userdict.items())
# for key, value in userdict.items():
#     print(key, value)

# dict.keys : 取出字典中全部的key， 他的默认类型是dict_keys, 如果想转换成list ==》 list(dict.keys())
# dict.values: ....

# pop : dict.pop(param), 删除指定param的key和value， 并返回value

# print(userdict.pop('Raymond'))
# print(userdict)

# popitem ： dict.popitem 删除一个默认的key=value的键值对， 并返回这个键值对的key=value
# print(userdict.popitem())
# print(userdict)

# dict.setdefault : 可以在一个字典中增加一个值, 并返回他的value， 默认返回为None
# print(userdict.setdefault('suibian'))
# print(userdict)

# dict.update
# userdict.setdefault('suibian', 0)
# userdict.update(suibian='1')
# userdict.update(panwang=1)
# userdict['11'] = '十一'
# userdict.update({'11': 1})
# dict.update 如果key不存在， 则新增一个key并新增对应的value
# dict.default 如果key不存在， 则新增， 如果key存在， 则不做任何修改
# dict[key] = new_value， 这样写法可以直接新增或修改对应的key的value
# print(userdict)


if True:
    print(True)

# 所有数据类型的bool值何时为空
integer = 0
string = ''
f_list = []
f_tuple = ()
f_set = set()
f_dict = dict()
f_bool = False
f_none = None

# {}   ==> type({}) dict
# set() ==> type(set()) set

# class.__bool__


# python中，一个空的数据类型(string, list tuple, set) 或 0 或 None 或False bool值都为False
#
# print(bool(integer))
# print(bool(string))
# print(bool(f_bool))
#
f_list.append('Raymond')
t_list = f_list.copy()
t_list = ['Raymond']

if t_list and len(t_list) > 2:
    print(len(t_list))
elif not t_list:
    print('True list is empty')
elif t_list.count('Raymond') != 0:
    print("t_list.count('Raymond') != 0")
elif len(t_list) * 2 == 4:
    print("len(t_list) * 2 == 4")
else:
    print('normal')

# if elif 都是判断表达式为真时，才会被执行下一个缩进段的代码
# 如果if 和elif 全部未命中， 则直接进入else


if __name__ == '__main__':
    # for循环
    # while 循环
    # break continue
    # pass
    userinfo = ['Raymond', 'gang', 'dog', 'devan', '牛仔']
    string_text = 'Hi Raymond'
    # 下标取值是对可迭代的对象进行index取值
    for user in userinfo:
        print(user)

    for text in string_text:
        print(text)

    for key in list(userdict.keys()):
        print(key)

    for param in userinfo:
        print(param)

    # # while 1
    # # while True
    # # while num < 5
    #
    while len(userinfo) <= 10:
        print(len(userinfo))
        userinfo.append('Raymond')
    
    for item in userinfo:
        if item == 'dog':
            break   # 跳出一个循环
        print(item)

    # while 1:
    #     num = 0
    #     for _ in range(10):
    #         if num == 5:
    #             break
    #         num += 1
    #         print(num)
    # while 如果用的不恰当， 他会进入一个死循环无法跳出
    # break 只跳出最近一层循环 不管是for 或是while
    
    # print(list(range(10)))
    #
    # for _ in range(5):
    #     userinfo.pop()
    #     print(userinfo)
    
    # numbers = []
    # for num in range(10):
    #     numbers.append(num)
    # print(numbers)
    
    # userinfo = ['Raymond', 'gang', 'dog', 'devan', '牛仔']

    for item in userinfo:
        if 'dog' == item:
            continue  # 当触发continue时，会跳出当前循环，进入下一次循环
        elif 'Raymond' == item:
            pass  # pass 留出空行，但是什么都不做
        elif item == 'devan':
            break  # 结束掉所有的循环
        print(item)
    # range(10) ==> 0-9
    # range(10) list(range(10)) ==> 0-9
    # list(range(1, 11)) ==> 从1开始 到11结束但不包含11 也就是1-10
    # range(start, end, step)
    for number in range(3, 11, 2):
        # number = 1
        print(number)
        if number == 3:  # number == 3 is False
            pass
        elif number == 5:  # number == 5 is False
            continue
        elif number == 7:  # number == 7 is False
            continue
        else:
            break
    #
    # userinfo = ['Raymond', 'gang', 'dog', 'devan', '牛仔']

    for item in userinfo:
        if 'Raymond' == item:
            continue
        elif 'dog' == item:
            pass
        print(item)
    
    userinfo = ['刘德华', '黎明', 'Raymond', 'dog', '随便', '牛仔']
    username = 'dog'
    # print(username in userinfo)
    if bool(userinfo.count('dog')):
        print(True)
    else:
        print(False)

    num = 0
    for user in userinfo:
        if user == username:
            print('username 在 userinfo中')
            break
        elif num == len(userinfo):
            print('不存在userinfo中')
        num += 1

