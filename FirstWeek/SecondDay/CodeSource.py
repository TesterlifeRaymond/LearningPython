"""
@Name: CodeSource
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/12
"""

# 下标取值
# 切片
# 数据类型的相关操作

# print
# print 作用是打印一行数据， 输出在标准输出环境
# 基础数据类型
# str, int, bool, float, list, dict, set, tuple
# str = '' or "" or ''''''
# string = "True"  str 而不是一个bool
# string = 'print'  <class 'str'>
# int = 所有的整型数字
# integer = 123 or 0 or -123 or 999999999999999999999999999999999999999999
# float = 123.456 or 0.0 or -123.456 or 99999999.99999999999999999999
# bool = True or False
# list = [1, 2, '3', abs, True， True]
# tuple = (1, 2, '3', abs, True, True)
# tuple 类型的数据是不可以被改变的，而list类型是可以被任意改变的
# set = set(), 交集/并集/差集
# dict = {}, dict()
# dict类型特点是 存储结构为key=value的键值对形式
# userinfo = {'港': '二期', '期盼': '三期'}
# dict中， 不能存储相同key的数据，key不能重复，key是唯一的


# type or isinstance
# type
#   print(type(123)) ==> <class 'int'>
#   print(type('1234')) ==> <class 'str'>

# isinstance
#   print(isinstance(123, int)) ==> True
#   print(isinstance(123, str)) ==> False


# 变量与常量

# 变量与常量最大的区别在于， 变量有可能随着程序的运行而发生状态或值的改变， 但是常量不会
# python中， 定义常量，常量名为全部大写，如果有多个单词，可用下划线分割
# name = '狗子'
# name = '期盼'

# PYTHON_CLASS = '三期课程'


if __name__ == '__main__':
    user_list = ['狗子', '港', '期盼', '思', 'DAYDREAM']
    # print(type(user_list))
    # print(isinstance(user_list, list))
    # # index
    # # user_list 默认索引
    # # 所有的list 或可迭代的对象， 第一位索引值都是0
    # print(user_list[0])
    # print(user_list[1])
    # print(user_list[-1])
    # print(user_list[-3])
    # print(user_list[4])
    # print(user_list[-5])
    #
    # user_string_text = '0123456789'
    # print(user_string_text[2])
    # print(user_string_text[-5])
    # print(user_string_text[5])
    #
    # user_tuple = ('狗子', '港', '期盼', '思', 'DAYDREAM')
    # print(user_tuple[2], user_tuple[4], user_tuple[-2])
    # # 所有的str / list / tuple 默认索引的第一位是0， 最后一位是-1
    # print(user_list)
    # user_list[2] = '牛仔很忙'
    # print(user_list)
    #
    # # dir python中查看一个对象他包含哪些可用方法
    # print(dir(user_list))
    user_list.append('今晚打老虎')  # 在一个列表的最后位置，新增一个元素
    # user_list.append('今晚打老虎')  # 在一个列表的最后位置，新增一个元素
    # print(user_list)
    # user_list.append('有点随便')
    # print(user_list)
    # # user_list.clear()   # clear方法， 是清空一个列表
    # # print(user_list)
    # print(user_list.count('今晚打老虎'))  # count 是取出list中有几个输入进来的元素， 如果没有返回0
    # print(user_list.index('牛仔很忙'))  # index 获取list中第一个碰到的输入的元素， 并返回元素位置， 如果没有没有会报错
    # print(user_list.index('今晚打老虎'))
    # user_list.insert(0, '一凡')  # 在user_list这个列表0号index位置， 增减一个元素=一凡
    # print(user_list)
    # user_list.insert(0, '十一')
    # print(user_list)
    # user_list.insert(-1, '唐李民')
    # print(user_list)
    #
    # last_item = user_list.pop()  # 删除一个列表中最后一位， 并把这个元素返回回来
    # print(last_item)
    # print(user_list.pop())
    # print(user_list)
    #
    # user_list.remove('一凡')  # remove 是移除list中的该元素
    # print(user_list)
    #
    # # a_list = [1, 2, 2, 3, 4, 5, 2]
    # # for i in a_list:
    # #     if i == 2:
    # #         a_list.remove(i)
    # # print(a_list)
    #
    # print(user_list)
    # print(user_list.index('牛仔很忙'))
    # user_list.reverse()  # 逆序一个列表， 并改变列表原有的index值
    # print(user_list)
    # print(user_list.index('牛仔很忙'))
    #
    # # sort
    # user_list.sort()
    # print(user_list)  # 对列表进行升序排序， 并改变列表原有的index
    # print(sorted(user_list))  # python内置的sorted 是不会改变原有的listindex位置的
    # print(user_list)
    
    # 取出user_list中的第2到第4个元素的全部的值
    # 在user_list列表中， 每2个index位置取值一次
    print(user_list)
    user_tuple = ('狗子', '港', '期盼', '思', 'DAYDREAM', '今晚打老虎')
    print(user_list[2:5])
    # 从第二个元素开始，包含第二个元素， 到第5个元素结束，不包含第5个元素，返回这个列表切片的值
    print(user_tuple[1:4])
    # 切片中，第一个元素是包含的， 第二个元素是不包含的
    user_string_text = 'Raymond is good man!'
    print(user_string_text[4:7])

    print(user_string_text[0::2])
    # step
    # 切片中的步长
    number_list = [item for item in range(0, 100)]
    # print(number_list)
    # print(number_list[0:50:2])
    # # 切片的理解
    # # list[起点：终点：每一步走多长]
    # print(number_list[::5])
    print(number_list)
    print(number_list[2:10:2])
    print(number_list[-2:-10:-2])
    # print(number_list[-1:-50:-2])

    a_list = sorted([1, 2, 2, 3, 4, 5, 2])
    # b_list = sorted(list(set(a_list)))
    # print(a_list)
    # b_list.remove(2)
    # print(b_list)

    uniq_a_list = set(a_list)
    print(uniq_a_list, type(uniq_a_list))
    b_list = list(uniq_a_list)
    print(b_list, type(b_list))
    new_b_list = sorted(b_list)
    # sorted(b_list).remove(2)

    new_b_list.remove(2)
    print(b_list)
    print(new_b_list)

    # list.sort 是操作原有list并改变index顺序， 始终操作的是list本身
    # sorted(list) 是一个新的list，如果需要操作新的list 需要把这个新的list进行变量赋值
    # import requests
    # pip install requests
    dict_dir_list = dir(dict)
    dict_module = [item for item in dict_dir_list if '__' not in item]    # 列表推导式
    print(dict_module)
    keys = ('狗子', '港', 'DAYDREAM')
    values = ('dog', 'gang', 'day')
    # print(dict.fromkeys(keys))
    user_dict = {key: value for key, value in zip(keys, values)}   # 字典推导式
    # dict hashmap
    # 是一个无序的， 且key唯一
    # python3.6之后 字典是有序的
    print(list(user_dict.keys())[2])   # dict.keys 和dict.values并不能直接通过下标取值的形式直接取值
    print(list(user_dict.values())[2])    # 我们需要先把dict.keys的数据类型转换成list类型， 再做取值行为
