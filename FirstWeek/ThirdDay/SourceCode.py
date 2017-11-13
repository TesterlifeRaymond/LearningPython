"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/13
"""


# 下标取值
# 可迭代的对象可以通过指定的index位置，获取对应的值
# str/list/tuple
# string_text = 'hello world!'
# string_text[1] ==> e
# string_text[6] ==> w

# user_list = ['Raymond', '狗子', 'gang']
# user_list[0] ==> Raymond
# user_list[-1] ==> gang

# user_tuple ...

# 下标取值，第一位index是0
# 最后一位是-1


# dir()
# dir可以获取到对象的全部方法
# 如果对一个不了解的对象， 进行方法的查询， 可以通过dir

# 完整的list方法的讲解
# list.append : 我们对一个列表追加一个元尿素，在最后一位
# userinfo = ['Raymond']
# userinfo.append('今晚打松鼠')
# userinfo ==> ['Raymond', '今晚打松鼠']

# list.clear : 清空一个列表
# userinfo ==> ['Raymond', '今晚打松鼠']
# userinfo.clear()
# userinfo ==> []
# userinfo = []

# list.copy : 复制一个列表
# userinfo = ['Raymond', '今晚打松鼠']
# new_userinfo = userinfo.copy()

# list.count : 他接受一个参数， 并返回这个参数在列表中的个数, 如果传递进来的参数不存在， 则返回0
# userinfo = ['Raymond', '今晚打松鼠']

# list.extend : 接受一个列表， 并把接受的列表与原列表合并为一个
# userinfo = ['Raymond', '今晚打松鼠']
# teacherinfo = ['小甲鱼', '茶茶']
# userinfo.extend(teacherinfo)

# list.index : 接受一个参数， 如果这个参数在列表中存在， 则返回列表中该元素第一个出现位置的index, 如果该元素不存在，则会报错
# userinfo = ['Raymond', '今晚打松鼠']
# userinfo.index('Raymond') ==> 0
# userinfo.index('小甲鱼') ==> Exception indexError

# list.insert : insert接受2个参数， 第一个参数是index位置， 第二个参数，是需要insert的值
# userinfo = ['Raymond', '今晚打松鼠']
# userinfo.insert(0, '思')
# userinfo ==> ['思', 'Raymond', '今晚打松鼠']
# userinfo.insert(-1, '茶茶')
# ['思', 'Raymond', '茶茶', '今晚打松鼠']
# insert不能再最后一位插入元素，如果index输入为-1 则在列表的-2位置插入一个元素
# 如果需要在list最后一位增加一个元素， 可以直接使用append

# list.pop : 删除最后一位，并返回被删除的元素
# userinfo = ['思', 'Raymond', '今晚打松鼠']
# userinfo.pop() ==> 今晚打松鼠
# print(userinfo) ==> ['思', 'Raymond']
# last_userinfo_param = userinfo.pop()
# print(last_userinfo_param) ==> 'Raymond'

# list.remove : 接受一个参数， 并在列表中移除这个参数， 如果列表中存在多个， 则优先删除第一个元素
# userinfo = ['思', 'Raymond', '今晚打松鼠']
# userinfo.remove('Raymond')
# userinfo ==> ['思', '今晚打松鼠']
# userinfo.remove('思') ==> None

# list.reverse : 他会逆序一个list原有的index， 并改变这个列表
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.reverse()
# numbers ==> [7, 6, 5, 4, 3, 2, 1]
# numbers = numbers.reverse() ==> None

# list.sort : 对列表进行升序排序， 并改变列表原有结构
# numbers = [2, 1, 6, 4, 5, 3, 7]
# numbers.sort()
# numbers ==> [1, 2, 3, 4, 5, 6, 7]
# numbers = sorted(numbers)
# number ==> [1, 2, 3, 4, 5, 6, 7]


if __name__ == '__main__':
    # dict_module = dir(dict)
    # dict_funcs = [item for item in dict_module if '__' not in item]
    # print(dict_funcs)
    # # dict 是字典
    # # 字典的特点是什么呢？
    # # python3.6以前的版本，字典是无序的
    # # 字典是一个hash类型， 因为是hash类型所以操作字典会非常快， 但是key是唯一的
    # # 字典的存储结构是key=value
    # # dict(a=1, b=2, c=3)
    # # dict ==> {'a': 1, 'b': 2, 'c': 3}
    #
    # test_dict = {'a': 1, 'b': 2, 'c': 3}
    # # test_dict.clear()
    # # test_dict.clear(): 清空这个字典中所有的元素
    # # test_dict = {}
    # # print(test_dict)
    # # new_dict = test_dict.copy()
    # # print(new_dict)
    # #
    # # test_dict.copy : 复制一个字典
    # # new_dict = test_dict.copy()
    # # new_dict ==> test_dict
    #
    # users = ('Raymond', 'gang', '打老虎', 'maas')
    # values = ('a', 'b', 'c', 'd')
    # print('test_dict.fromkeys(users, values)', test_dict.fromkeys(users, values))
    # # dict.fromkeys() : 是从一个列表或元祖中取出对应的元素，赋值给一个新的字典中的每一个key
    #
    # news = dict(beijing='北京', shanghai='上海', shenzhen='深圳')
    # # print(news.get('shanghai'), news['shanghai'])
    # # print(news.get('beijing'), news['beijing'])
    # # print(news.get('shenzhen'), news['shenzhen'])
    #
    # print(news.get('chengdu', '成都'))
    # print(news.get('xiamen', '厦门'))
    # print(news['chengdu'])
    # #
    # # dict.get() : 输入一个key， 并返回这个key对应的value， 如果这个key不存在， 则默认返回None, 也可以传递给它一个默认值
    # # dict['key'] : 如果这个key存在， 则返回key的value， 如果这个key不存在， 则抛出KeyError的异常
    #
    # print(news)
    # news['shanghai'] = '上海滩'
    # print(news)
    # news['xiamen'] = '厦门'
    # print(news)
    # # 如果我们需要修改一个字典对应key的value 我们可以用 dict['key'] = new_value的这种方式
    # # dict() {}
    #
    # # dict.update() : update接受一个kwargs参数， 并更新字典中对应key的value
    # news = {'beijing': '北京', 'shenzhen': '深圳', 'shanghai': '上海滩', 'xiamen': '厦门'}
    # news.update(beijing='首都')
    # news['shanghai'] = '上海'
    # print(news.items())
    #
    # # dict.items() : 会返回一个字典对应的key value的全部结构体, 每一个元祖中，存储着对应的key， value
    #
    # # for key, value in news.items():
    # #     print(key, value)
    #
    # # dict.keys() : 返回一个字典中全部的key， 返回的结构是dict_keys类型， 不能直接用index取值， 如果需要用index取值
    # # 需要做一步转换 ： keys = list(dict.keys())
    # # dict.values(): 返回一个字典中全部的value, 返回的结构是dict_values类型， 不能直接index取值， 如果需要用index取值
    # # 需要做一步转换 ： keys = list(dict.values())
    #
    # print(news.pop('beijing'))
    # print(news)
    # print(news.pop('xiamen'))
    # print(news)
    #
    # # list.pop() 不需要入参， list.pop删除的是列表中的最后一个元素
    # # dict.pop() 需要要给入参 key， dict中的pop是制定key删除
    # print(news)
    # print(news.popitem())
    # print(news)
    # # dict.pop 不一样的点在于， dict.popitem返回的是一个(key, value) 而pop只返回value
    #
    # news.setdefault('chengdu', '成都')
    # print(news)
    # dict.setdefault ：可以通过传递一个key 来给字典增加一个key value， 默认的value 为None
    # dict.setdefault(key, value)
    
    # bool True or False
    
    if True:    # if判断的内容永远为真， if not 判断的永远为假
        print('hello world !')
    else:
        print(False)
    num = 0
    print(bool(num))
    f_list = []
    f_string = ''
    f_dict = {}
    f_set = set()
    f_none = None
    f_tuple = ()

    print('f_list', bool(f_list))
    print('f_string', bool(f_string))
    print('f_dict', bool(f_dict))
    print('f_set', bool(f_set))

    if num == 0:    # num 为True, num != 0
        # num == 0 ==> True
        # if True
        print('num != 0')
    else:
        print('num == 0')
    
    news = {'beijing': '北京'}

    if news.get('tianjin'):
        print('天津唐山')
    else:
        print('天津不在字典中')
    # dict_module = dir(dict)
    # dict_funcs = [item for item in dict_module if '__' not in item]
    num = ''

    if num == 0:
        print('num is 0')
    elif isinstance(num, (str, dict)):
        print('num is str object or dict object')
    else:
        print('我也不知道num是什么类型')
