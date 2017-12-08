"""
@Version: 1.0
@Project: LearningPython
@Author: Raymond
@Data: 2017/12/8 21:28
@File: SourceCode.py
@License: MIT
"""

import random
import string
from abc import ABCMeta, abstractmethod


class Base:
    def __init__(self, *args):
        self.name, self.work, self.age, self.city = args

    def __repr__(self):
        return ','.join([self.name, self.work, self.age, self.city])


class People(Base):
    def __init__(self, *args):
        super(People, self).__init__(*args)


if __name__ == '__main__':
    print(People('Raymond', 'Teacher', '30', '北京'))
    print(People('Gang', 'student', '22', '上海'))
    print(People('随便', 'student', '18', '不知道'))



# # 当类中的metaclass=ABCMeta的时候 说明父类为抽象类
# # 当类方法中使用了absractmethod装饰器的时候， 说明类方法为抽象类方法
# # 抽象类方法如果在子类中不进行重新实现， 无法实例化新的对象
#
#
# class Human(metaclass=ABCMeta):
#     @abstractmethod
#     def city(self):
#         pass
#
#     @abstractmethod
#     def sex(self):
#         pass
#
#     @abstractmethod
#     def age(self):
#         pass
#
#     @abstractmethod
#     def name(self):
#         pass
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     def __repr__(self):
#         return 'my name is {}, i\'m a {}, i\'m in {}, 我今年{}， 我的工作是{}'.format(
#             self.name(), self.sex(), self.city(), self.age(), self.work()
#         )
#
#
# class Teacher(Human):
#     def name(self):
#         return 'Raymond'
#
#     def age(self):
#         return 30
#
#     def sex(self):
#         return 'man'
#
#     def work(self):
#         return 'Teacher'
#
#     def city(self):
#         return 'Beijing'
#
#
# class Student(Human):
#     def name(self):
#         return 'DayDream'
#
#     def age(self):
#         return 22
#
#     def sex(self):
#         return 'girl'
#
#     def work(self):
#         return 'student'
#
#     def city(self):
#         return '平顶山'
#
#
# if __name__ == '__main__':
#     print(Teacher())

# print(random.randint(1, 10))   # 随机一个包含1-10的整数
# print(random.choice('12345'))   # 随机从一个可迭代的对象中取出一个元素
# text = list(range(1, 20))
# print(text)
# random.shuffle(text)   # shuffle打乱一个列表的全部元素的顺序， 并且改变列表本身
# print(text)
# print(random.random())   # random.random 不接受任何参数， 并返回一个0-1之间的float类型的数据

# print(string.digits, type(string.digits))   # 全部数字组成的字符串类型 0-9
# print(int(string.digits))  # 我们把0123456789， str类型 -》 转换成int 类型， 数字变成123456789 的int类型
# print({000, 00, 0})   # 000 00 0是同一个对象
# print(id(000) == id(0))
# print(000 is 00 and 00 is 0)
# print(string.punctuation)   # punctuation存储的是一组特殊符号的字符串
# print(string.ascii_letters)  # A-Z and a-z
# print(string.ascii_uppercase)  # A-Z
# print(string.ascii_lowercase)  # a-z


# class Animal(metaclass=ABCMeta):
#     # 抽象类是定义好所有的类似java中的接口instance， 不做实现， 只做定义
#     # 当子类继承父类的时候， 可以通过子类实现父类的抽象方法
#     # 如果子类在实例化前没有实现抽象方法， 则会报错
#
#     @abstractmethod
#     def color(self):
#         pass
#
#     @abstractmethod
#     def cry(self):
#         pass
#
#     @abstractmethod
#     def fly(self):
#         pass
#
#     @abstractmethod
#     def running(self):
#         pass
#
#     def dispaly(self):
#         print(self)
#         self.color()
#         self.cry()
#         self.fly()
#         self.running()
#
#
# class Cat(Animal):
#     def __init__(self):
#         super(Cat, self).__init__()
#
#     def color(self):
#         print('cat color is orange')
#
#     def fly(self):
#         print('cat can not fly')
#
#     def running(self):
#         print('cat running ')
#
#     def cry(self):
#         print('cat :miao miao miao ')
#
#
# class Dog(Animal):
#     """pass """
#     def cry(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def running(self):
#         pass
#
#     def color(self):
#         pass
 


# if __name__ == '__main__':
    # cat = Cat()
    # cat.dispaly()
    # dog = Dog()
    # dog.dispaly()






# def mobile(head=None):
#     """
#         mobile is a function
#     :param head:
#     :return:
#     """
#     if not head:
#         head = random.choice(['131', '132', '133', '134', '135', '136', '137', '140', '155'])
#     return head + ''.join(random.sample(string.digits, 8))
#
#
# def city(instance):
#     print(instance.get)
#
#
# class TestCase:
#     """
#         cls: 代表class对象本身， 也就是TestCase.mobile()， 也可以通过实例化后进行调用
#         self: 代表实例对象本身， 也就是TestCase().mobile()
#         static: 代表一个静态的类方法， 他可以通过TestCase.mobile() 或 TestCase().mobile来调用
#     """
#
#     @classmethod
#     def mobile(cls):
#         """
#             mobile is a class method
#         :return:
#         """
#         return 111
#
#     def username(self):
#         """
#             username is a instance method
#         :return:
#         """
#         return '222'
#
#     @staticmethod
#     def city():
#         """
#             city is a static method
#         :return:
#         """
#
#
# class Method:
#     @classmethod
#     def get(cls, url):
#         print(url)
#
#     def post(self, url):
#         print(url)
#
#     @staticmethod
#     def parse():
#         print(None)
#
#
# if __name__ == '__main__':
#     # print(TestCase.mobile())   # 这是类对象方法的调用方式
#     # test = TestCase()
#     # # test == self
#     # print(test.username())  # 而这里是类实例对象的调用方式
#     # # TestCase.username(TestCase())
#     # # TestCase.username(self)
#     # # test.username() ==> self.mobile()
#     # print(TestCase.city)   # 这是一个静态方法的调用方式
#     # # TestCase().city
#     # print(mobile)   # 这是一个函数的调用方式
#     Method.get('http://testerlife.com')
#     Method().post('http://baidu.com')
#     Method.parse()
#     print(city(Method()))
