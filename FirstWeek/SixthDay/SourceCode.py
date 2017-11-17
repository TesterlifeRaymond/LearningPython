# """
# @Name: SourceCode
# @Version:
# @Project: PyCharm Community Edition
# @Author: liujinjia
# @Data: 2017/11/16
# """
#
# import random
# import string
# # from FirstWeek.ForthDay import SouceCode   # import module
# # import FirstWeek    # import packages
#
# # module: python中，每个单独的文件， 代表一个module
# # packages : pip install requests  python site-packages/requests/， 每个文件夹代表packages
#
# # numbers = list(range(1, 100))
# # print(random.choice(numbers))   # random.choice 接受一个可迭代的对象， 从对象中随机取出一个元素， 并返回
# # print(random.randint(1, 99))   # random.randint 接受2个参数，一个是起始点， 一个是结束点， 从这两个点之间(包含这两点)随机返回一个int类型的值
# # print(random.sample(numbers, 8))   # random.sample 接受2个参数， 第一个参数为可迭代的对象，第二个参数为返回这个对象中的几个元素，返回列表类型
# # print([item for item in dir(string) if not item.startswith('__')])
# #
# # print(numbers)
# # random.shuffle(numbers)   # random.shuffle 接受一个列表，并把这个列表中全部的元素位置打乱， 返回None, 会改变原有的列表index
# # print(numbers)
# #
# # print(string.ascii_letters)   # string.ascii_letters 打印a-z,A-Z 全部的大小写的26个英文字符的一个字符串
# # print(string.digits)   # string.digits 返回一个0-9的全部数据的字符串
# # print(string.ascii_lowercase)   # 26个小写的英文字母的字符串
# # print(string.ascii_uppercase)   # 26个大写的英文字符
#
#
# # numbers = list(string.digits)
# # random.shuffle(numbers)
# # headers = ['138', '139', '140', '131', '155', '157']
# # mobile_number = random.choice(headers) + ''.join(random.sample(numbers, 8))  # 随机生成一个手机号
# # print(mobile_number)
# #
# #
# # num = 8   # 生成几位邮箱前缀
# # footer = ['@163.com', '@qq.com', '@yahoo.com', '@126.com']
# # header = ''.join(random.sample(list(string.digits + string.ascii_letters), num))
# # email = header + random.choice(footer)
# # print(email)
# #
# # # 生成一个随机的8位密码，包含大小写，不包含特殊符号
# # numbers = list(string.digits + string.ascii_letters + string.punctuation)
# # random.shuffle(numbers)
# # print(numbers)
# # print(''.join(random.sample(numbers, 8)))
#
#
# # 生成一个随机的四位数， 四位数字不想等
#
# # 然后让用户猜， 猜对3次， 则退出游戏
# # 如果持续猜错， 则累加错误次数， 当错误次数达到10次， 退出游戏
#
# # number = random.sample(string.digits, 4)
# # # set()
# # print(number)
# # success_number = 0
# # fail_number = 0
# # while 1:
# #     if success_number == 3 or fail_number == 10:
# #         print('退出游戏！')
# #         break
# #     user = list(input('请输入这不相同的4个数字：'))
# #     if user == number:
# #         success_number += 1
# #         print('恭喜你！回答正确')
# #     else:
# #         print('真糟糕！猜错了！')
# #         fail_number += 1
#
#
# if __name__ == '__main__':
#     # python中的函数
#     # function 代表函数， method代表方法
#     # function不需要与任何类或实例类对象绑定
#     # method 一定会绑定一个对象cls or self
#
#     def make_a_mobile():
#         """
#             doc string, 函数的注释内容
#         :return:
#         """
#         # print('numbers {}'.format(st))
#         numbers = list(string.digits)
#         random.shuffle(numbers)
#         headers = ['138', '139', '140', '131', '155', '157']
#         mobile_number = random.choice(headers) + ''.join(random.sample(numbers, 8))  # 随机生成一个手机号
#         print(mobile_number)
#         return mobile_number
#
#     def hi(name):
#         """
#             这个函数接受一个必填参数
#         :param name: 这是一个用户名
#         :return:
#         """
#         print('Hi {}'.format(name))
#         # ’{}‘.format(name) 代表将一个字符串格式化，{}部分由format中的参数来替代
#         # format 主要用于字符串格式化
#         return name
#
#
#     def give_me_apple(apple: str) -> str:
#         """
#             让这个函数给我一个苹果
#         :param apple:
#         :return:
#         """
#         if apple:
#             return apple
#         # print(apple)   # 说：我要给你一个苹果， 但是并没有给我， 只是说了给我
#         return apple * 2  # 给： 我什么都没有说， 但是我给你苹果
#         print(apple)   # 每个函数中，只会出发一个return， return后面的代码将不会被执行
#
#     # 函数的定义，是通过def关键字来定义的
#     # def 后面接函数名
#     # 函数名后面的括号可以为空， 如果要给这个函数传递参数， 则输入参数名
#     # 函数中的参数分为3种
#     # 第一种 必传参数 func(a, b) 说明func这个函数默认接受2个必传参数， a和b, 一定要按照正确的顺序写入
#     # 第二种 关键字参数 func(a=1, b=2) 说明func函数接受两个keywords参数，可以直接用key=value的形式对参数进行修改, 当前默认值为a=1, b=2
#     # apple = give_me_apple('apple')   # None
#     # print(apple)
#
#     def number_sum(a=1, b=2):
#         """
#             number = a + b
#         :param a:
#         :param b:
#         :return:
#         """
#         print('a + b', a + b)
#
#     number_sum()
#
#     def print_user_info(name, age, work):
#         """
#             这个函数，接受三个必传参数，把他们拼接成一句话，不错返回
#         :param name: 用户名
#         :param age: 用户年龄
#         :param work: 用户的工作
#         :return: None
#         """
#         print('我是{}，我今年{}，我的工作是{}'.format(name, age, work))
#
#     user_info = ('Raymond', 20, 'IT')
#     user_info = dict(name='Raymond', age=20, work='IT')
#     print_user_info(**user_info)
#     # 把这个字典中的每一个key=value 传递给这个函数作为他的keywords参数
#     user_info = ['港', 15, 'student']
#     print_user_info(*user_info)   # 是说把这个列表中的每一位元素，拆分开传递给这个函数的必传参数
#
#     def print_user_info_kwargs(name=None, age=None, work=None):
#         """
#             这个函数只有一个必填参数 name
#             age 和 work可以为空
#         :param name:
#         :param age:
#         :param work:
#         :return:
#         """
#         if not name:
#             name = '路人甲'
#         if not age:
#             age = 20
#         if not work:
#             work = '待业'
#         print('我是{}，我今年{}，我的工作是{}'.format(name, age, work))
#
#     def print_user_info(*args, **kwargs):
#         """
#             * args ：args类型是一个元组， 他接受不确定个数的非keywords类型参数
#             ** kwargs kwargs类型是dict， 他接受不确定个数的keywords的类型的参数
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         if kwargs.get('city'):
#             print('城市的名字是{}'.format(kwargs['city']))
#         # print(name)
#         # print(args, type(args), len(args))
#         print(kwargs, type(kwargs))
#
#
#     name = 'Raymond'
#     age = 20
#     work = 'IT'
#     # name = 'gang'
#     # age = 15
#     # work = '教师'
#     # print_user_info(name, age, work, 1, 2, 3, 4, 5, 6, 7, a=1, b=2, c=3, cc=100, city='上海')
#     # print_user_info_kwargs(work=work, age=age, name=name)
#
#     def get_city_dict():
#         city_code = [100000, 210000, 457000]
#         city_name = ['北京', '上海', '平顶山']
#         return {key: value for key, value in zip(city_code, city_name)}
#
#     def get_city_code(code: int) -> str:
#         """
#             这是一个通过邮编查询城市的函数，接受一个邮编，返回城市信息
#         :param code:
#         :return:
#         """
#         city_dict = get_city_dict()   # 通过调用get_city_dict() 函数将返回的city_dict赋值给一个变量
#         print(city_dict)
#         return city_dict.get(code, '我也不知道这个城市是哪？')
#
#     # print(get_city_code(1234))
#
#
#     def get_user_info() -> tuple:
#         user_mobile = make_a_mobile()
#         num = 8   # 生成几位邮箱前缀
#         footer = ['@163.com', '@qq.com', '@yahoo.com', '@126.com']
#         header = ''.join(random.sample(list(string.digits + string.ascii_letters), num))
#         user_email = header + random.choice(footer)
#         user_password = ''.join(random.sample(string.digits + string.ascii_letters + string.punctuation, 8))
#         return user_mobile, user_email, user_password
#
#     def print_user_info() -> None:
#         """
#          打印用户信息
#         :return:
#         """
#         user_mobile, user_email, user_password = get_user_info()
#         print('当前用户的手机号码是: {}, 邮箱是: {}, 密码是: {}'.format(user_mobile, user_email, user_password))
#
#     def save_user_info() -> None:
#         result = []
#         text = ('mobile', 'email', 'password')
#         for num in range(10):
#             userinfo = get_user_info()
#             result.append({key: value for key, value in zip(text, userinfo)})
#         print(result)
#
#         # map, reduce
#         # map 不支持继续使用
#         # python更推崇 推导式概念
#         # [item for item in text]  # 列表推导式
#         # {key: value for key, value in zip(text, userinfo)}   字典推导式
#
#     save_user_info()
#
#     # 写一个函数
#     # 这个函数要自动生成中文用户名
#     # 可以指定姓氏， 如果没有指定则随机姓氏
#     # 并返回一个2-3位的随机中文名字
#
#
import random
FIRST_NAME_ENUM = '赵钱孙李周吴郑王'
LAST_NAME_ENUM = '与玉鱼汪千苗喵'


def make_user_name(first_name=None) -> str:
    """
        生成一个随机的用户名
    :return:
    """
    if not first_name:
        first_name = random.choice(list(FIRST_NAME_ENUM))
    
    rand = 2 if random.randint(1, 100) > 50 else 1
    last_name = ''.join(random.sample(list(LAST_NAME_ENUM), rand))
    print('用户名是 ：{}'.format(first_name + last_name))
    return first_name + last_name


make_user_name('独孤')



