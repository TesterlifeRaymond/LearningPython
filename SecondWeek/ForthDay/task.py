"""
@Name: task
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/21
"""

# 第二个作业
class Dog:
    def __init__(self,weight,height,hair,type):
        self.weight = weight
        self.height = height
        self.hair = hair
        self.type = type
        type = '狗'
        # type 没有被用到
        # 第二个 覆盖了buildin module中的type

    def bark(self):
        print('汪汪汪')

    def display(self):
        print(self.weight)
        print(self.height)
        print(self.hair)
        self.bark()
        return '我是一只{}，我非常忠心。'.format(self.type)


class mole_cricket(Dog):
    def __init__(self):
        self.weight = '我很轻'
        self.height = '我很高'
        self.hair = '我的毛发不长'
        self.type = '土狗'
        super(mole_cricket,self).__init__(self.weight,self.height,self.hair,self.type)


class big_dog(Dog):
    def __init__(self):
        self.weight = '我很重'
        self.height = '我很高'
        self.hair = '我的毛发很长'
        self.type = '大型犬'
        super(big_dog,self).__init__(self.weight,self.height,self.hair,self.type)


class little_dog(Dog):
    def __init__(self):
        self.weight ='我很轻'
        self.height ='我不高'
        self.hair = '我毛发长'
        self.type = '小型犬'
        super(little_dog,self).__init__(self.weight,self.height,self.hair,self.type)

# 第一个作业
from abc import ABCMeta
from abc import abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def call(self):
        """
        叫声
        :return:
        """
    @abstractmethod
    def fly(self):
        """
        是否会飞
        :return:
        """
    @abstractmethod
    def swim(self):
        """
        是否会游泳
        :return:
        """


class DOG(Animal):
    def call(self):
        print('这是一只会汪汪汪叫的狗')
    def fly(self):
        print('这是一只不会飞的狗')
    def swim(self):
        print('狗会游泳')


class CAT(Animal):
    def call(self):
        print('这是一只会喵喵喵叫的猫')
    def fly(self):
        print('这是一只不会飞的猫')
    def swim(self):
        print('猫不会游泳')


class DUCK(Animal):
    def call(self):
        print('这是一只会嘎嘎嘎叫的鸭子')
    def fly(self):
        print('这是一只不会飞的鸭子')
    def swim(self):
        print('鸭子会游泳')


class BIRD(Animal):
    def call(self):
        print('这是一只会喳喳叫的鸟')
    def fly(self):
        print('这是一只会飞的小鸟')
    def swim(self):
        print('会游泳的鸟')