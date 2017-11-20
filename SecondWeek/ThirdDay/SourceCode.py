"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/20
"""

# oop 面向对象编程的三大特性
# 封装 把重复的代码整合成一个通过不同参数而返回相同操作的过程 买水果这个过程中， 买可以封装为一个类方法
# 多态 多态是写一个父类， 抽象类不做实现， 只做定义
# 继承 首先我们写了一个Fruits类， Apple -> 脆的， 面的， 青苹果， 红苹果

import json
from abc import ABCMeta
from abc import abstractmethod

# 定义一个抽象类，需要在这个类的继承中继承metaclass=ABCMeta
# 定义一个抽象类方法， 需要在这个类方法上挂一个abstractmethod装饰器
# 定义好的抽象类，不能直接实例化， 否则会抛出TypeError的异常
# 如果你需要实现这个抽象类的类方法， 可以让子类继承父类后， 用子类的类方法override父类的对应方法


class Fruits(metaclass=ABCMeta):
    """ 这是一个水果的父类 """
    
    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def throw(self):
        pass

    @abstractmethod
    def sell(self):
        pass
    
    def param(self):
        pass

class Apple(Fruits):
    def buy(self):
        print('购买一个苹果')
    
    def sell(self):
        print('卖掉一个苹果')
    
    def throw(self):
        print('这个苹果坏了， 仍掉它')
        

class Banana(Fruits):
    def buy(self):
        print('购买一个香蕉')
    
    def sell(self):
        print('卖掉一个香蕉')
    
    def throw(self):
        print('这个香蕉坏了， 仍掉它')


class People:
    def __init__(self, name, age, city, work):
        self.users = name, age, city, work
        self.title = ('name', 'age', 'city', 'work')

    def get_user_info(self):
        return json.dumps({key: value for key, value in zip(self.title, self.users)}, indent=4, ensure_ascii=False)


class Teacher(People):
    def __init__(self, name, age, city):
        self.work = 'teacher'
        super(Teacher, self).__init__(name, age, city, self.work)
        # super 初始化父类


class Student(People):
    def __init__(self, name, age, city):
        self.work = 'student'
        super(Student, self).__init__(name, age, city, self.work)


class Worker(People):
    """ 这是一个工人的类"""
    def __init__(self):
        self.users = 'Raymond', 20, '北京', '工人'
        super(Worker, self).__init__(*self.users)
        

class Duck:
    """ pass """
    def __init__(self, _quack, _fly):
        self._quack = _quack
        self._fly = _fly
        self.type = '真'
    
    def swim(self):
        print('swiming ...!')

    def display(self):
        print(self._quack)
        print(self._fly)
        self.swim()
        return '我是一只{}的鸭子'.format(self.type)


class GreenDuck(Duck):
    def __init__(self):
        super(GreenDuck, self).__init__(None, None)
        self._quack = '我会叫'
        self._fly = '我会飞'
        self.type = '绿头'
    
    def green_quack(self):
        return 'gua gua gua'


class RubberDuck(Duck):
    """ 橡皮鸭子 """
    def __init__(self):
        self._quack = '我不会叫'
        self._fly = '我不会飞'
        super(RubberDuck, self).__init__(self._quack, self._fly)
        self.type = '橡皮'
    
    def swim(self):
        print('橡皮鸭漏气了， 不会游泳了')
        return '我不能游泳了'


class DecoyDuck(RubberDuck):
    """ 诱饵鸭子"""
    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.type = '诱饵'


if __name__ == '__main__':
    green = GreenDuck()
    print(green.display())   # display 是由父类来实现的
    green.swim()    # swim和green_qucak 是由子类来实现的
    print(green.green_quack())
    # duck = Duck('我会叫', '我会飞')
    # print(duck.display())
    print('================')
    rubber = RubberDuck()
    print(rubber.display())     # display 是由父类实现
    print(rubber.swim())    # 是由子类override之后实现的
    # decoy = DecoyDuck()
    # print(decoy.display())
    # worker = Worker()
    # print(worker.get_user_info())
    # teacher = Teacher('茶茶', 35, '上海')
    # print(teacher.get_user_info())
    # students = [
    #     ('gang', 18, 'chengdu'),
    #     ('老虎', 22, '平顶山'),
    #     ('随便', 19, 'xiamen')
    # ]
    # for student in students:
    #     st = Student(*student)
    #     print(st.get_user_info())
    # fruits = Fruits()
    # apple = Apple()
    # apple.buy()
    # apple.throw()
    # apple.sell()
    # user = Teacher('Raymond', 20, '北京')
    # user1 = Student('gang', 20, 'shanghai')
    # print(user.get_user_info())
    # print(user1.get_user_info())