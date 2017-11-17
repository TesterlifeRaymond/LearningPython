"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/17
"""

# log

# python中如何去做文件的读写

# python写文件

# mode : r, rb, w, wb, a, a+
# file = open('log.txt', mode='w', encoding='utf-8')
# file.write('这是python写进来的log\n') # mode=w 如果这个文件在当前指定路径不存在， 则生成一个文件，并写入进去需要写入的信息
# file.write('好吧， 我要写很多个file.write')
# # w在操作的过程中会覆盖原有的文件
# file.close()
# print(file.closed)
#
# file = open('log.txt', mode='a', encoding='utf-8')
# file.write('mode=a的时候，我要在这个文件的最后位置新增一行信息')
# file.close()
#
# file = open('log.txt', mode='a', encoding='utf-8')
# file.writelines(['\n我是整行写入的', '\n我想在这行再加一些备注'])
# file.writelines(['\n我是第二个整行', '\n好吧我觉得我没什么写的了就是想在这里占一个位置'])
# file.close()
#
# # str => bytes
# # bytes => str
#
# string_text = '我是雷蒙德！'
# print('string text ', string_text, type(string_text))
# bytes_text = string_text.encode()
# print('bytes_text ', bytes_text, type(bytes_text))
#
# bytes2string = bytes_text.decode()
# print(bytes2string)

# with open('log.txt', mode='rb') as file:
#     data = file.read()
#     # print(file.read())   # 这里会返回一个空的bytes类型的数据，因为file.read()只会返回一次数据，返回后数据被消费掉
#
# file_text = data.decode()
# print(file_text)

# with open('log.txt', mode='r', encoding='utf-8') as file:
#     for item in file:
#         print(item)
#     # 如果我们便利一个file中的每一行数据, 可以通过for循环这个file对象， 也可以通过for循环去打开file.readline()获取数据

# with open('log.txt', mode='r', encoding='utf-8') as file:
#     print(file.readlines())  # file.readlines() 返回一个完整的文件内容的列表，每一行用’，‘分割


# my_logs = ['这是一个美好的下午\n', '非常适合吹牛\n', '如果给我一个冰棍那就更好了\n']

# def write_file(mode: str, logs: list) -> str:
#     """
#         接受一个log的列表，并把这个log的列表写入到一个文件中
#     :param mode:
#     :param logs:
#     :return: 写入成功
#     """
#     if 'w' in mode:
#         with open('log.txt', mode=mode, encoding='utf-8') as file:
#             file.writelines(logs)
#
#     if 'r' in mode:
#         with open('log.txt', mode=mode, encoding='utf-8') as file:
#             print(file.readlines())
#
#     if 'a' in mode:
#         with open('log.txt', mode=mode, encoding='utf-8') as file:
#             file.writelines(logs)
#     return '输入的mode是{}, 文件已经执行完成'.format(mode)
#
#
# print(write_file('r', my_logs))


# python中的匿名函数
# lambda
# lambda 关键字后面跟的是这个函数的入参
# lambda ：后面表达的是这个函数的返回结果

# sum = lambda a, b: a + b
# print(sum(1, 2))
#
recurstion = lambda a, b: {key: value for key, value in zip(a, b)}
# recurstion 是一个将两个元组或列表转换成字典的匿名函数

name = ['Raymond', '港', '狗子', '随便']  # a
city = ['北京', '上海', '重庆', '济南']  # b
print(recurstion(name, city))


def recurstion(a, b):
    """
        pass
    :param a:
    :param b:
    :return:
    """
    return {key: value for key, value in zip(a, b)}

def sum(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a + b

print(sum(3, 4))



# 写一个计算器
# 这个计算器接受不确定个数的参数
# 他接受一个seq参数， 这个参数代表 + - * /
# 通过seq参数 将所有输入进来的参数进行对应操作 / 不做处理返回错误信息


def 计算器(*args, seq='+'):
    """
        这是一个制作一种运算的计算器
    :param args:
    :param seq:
    :return:
    """
    if seq == '+':
        return sum(args)
    if seq == '-':
        head, foot = args[0], args[1::]
        for num in foot:
            head -= num
        return head
    if seq == '*':
        res = 1
        for num in args:
            res *= num
        return res
    return '除法暂时不做处理'


print(计算器(1, 2, 4, 100,seq='*'))