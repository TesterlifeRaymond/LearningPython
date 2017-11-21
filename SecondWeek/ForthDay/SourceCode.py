
"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/21
"""
from abc import ABCMeta
from abc import abstractmethod


def return_sum_number(*args, **kwargs):
    # *args 代表不确定个数的非keywords关键字 接收到的数据类型是tuple
    # **kwargs 代表接受不确定个数的键值对入参，接受到的数据类型是dict

    if kwargs.get('param'):
        args = kwargs.get('param')
    return sum(args)


class Animal(metaclass=ABCMeta):
    """ 这是动物的抽象类 """
    def __init__(self, animal_name, animal_age, animal_color, **kwargs: dict):
        self.animal_info = [animal_name, animal_age, animal_color]
        if kwargs:
            # 如果初始化参数中出现kw关键字姓氏的入参， 则把关键字形式的参数提取出来
            # kwargs 是一个dict 类型， 所以kwargs.keys() 或kwargs.values()
            self.animal_info.append(kwargs)

    @abstractmethod
    def call(self):
        """ 这是动物的叫声的抽象类方法 """
        raise NotImplemented
    @abstractmethod
    def swim(self):
        """这是动物的游泳的抽象类方法"""
        raise NotImplemented

    @abstractmethod
    def fly(self):
        """这是动物的飞行的抽象类方法"""
        raise NotImplemented

    @abstractmethod
    def run(self):
        """ 这是动物的跑的抽象类方法"""
        raise NotImplemented

    def display(self):
        if len(self.animal_info) == 3:
            # self.animal_info[0], self.animal_info[1], self.animal_info[2] <== *self.animal_info
            print("这是一只{}动物, 它今年{}岁了, 他有一身漂亮的{}颜色".format(*self.animal_info))
        else:
            print("这是一只{}动物, 它今年{}岁了, 他有一身漂亮的{}颜色,".format(*self.animal_info[0:3]))
            info = ''
            for key, value in self.animal_info[-1].items():
                info += key + ',' + value + '.'
            print('他还有一些特殊的属性呢：{}'.format(info))

    def __repr__(self):
        """ pass """
        result = self.display()
        return '' if not result else result
        # if not result:
        #   return ''
        # return result


class Dog(Animal):
    def __init__(self, name, age, color, **kwargs):
        super(Dog, self).__init__(name, age, color, **kwargs)
    
    def call(self):
        """ pass """
        print('汪汪汪！')
    
    def swim(self):
        """ pass """
        print('狗子会游泳')
    
    def fly(self):
        """ pass """
        print('狗子不会飞')
        
    def run(self):
        print('狗子跑得快')


class Duck(Animal):
    def __init__(self, name, age, color, **kwargs):
        super(Duck, self).__init__(name, age, color, **kwargs)

    def call(self):
        """ pass """
        print('Quack！Quack！Quack！')

    def swim(self):
        """ pass """
        print('鸭子会游泳')

    def fly(self):
        """ pass """
        print('鸭子还会飞')

    def run(self):
        print('鸭子没有狗子跑的快！')


class 搞事情:
    """ 这是一个用来搞事情类"""
    # 搞 = 搞事情(1, 2, 3, 4, 5, 6, abc=123, bcd=456, abcd=1234)
    # print(dir(搞)) print(dir(self))
    def __init__(实例对象, *搞事情的不确定参数, **搞事情的关键字参数):
        实例对象.不确定参数元组 = 搞事情的不确定参数
        实例对象.不确定关键字字典 = 搞事情的关键字参数
        实例对象.打印 = print

    def 遍历不确定参数元组(实例对象):
        """
            pass
        :return:
        """
        for 参数 in 实例对象.不确定参数元组:
            实例对象.打印(参数)
    
    def 将字典中的元素全部打印出来(实例对象):
        """ pass """
        for 关键字, 值 in 实例对象.不确定关键字字典.items():
            # for key, value in [(key, value), (key, value), (key, value)]:
            print(关键字, 值)

if __name__ == '__main__':
    搞 = 搞事情(1, 2, 3, 4, 5, 6, abc=123, bcd=456, abcd=1234)
    搞.将字典中的元素全部打印出来()
    搞.遍历不确定参数元组()
    black_dog = Dog('狗子', 5, '黑色的')
    fat = Dog('狗子', 18, '斑点', eat='特别能吃！', fly='跑的快了还能飞起来！')
    print(black_dog)
    print(fat)
    yellow_duck = Duck('小黄鸭', 2, '黄色')
    print(yellow_duck)
    green_duck = Duck('绿头鸭', 2, '彩色', hair='一头绿色的长发', fly='迎风就飞起来')
    print(green_duck)
