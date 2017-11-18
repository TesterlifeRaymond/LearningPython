"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/18
"""
import json

# python中的类
# python中是通过class关键字， 来定义一个类


class MyFirstClass:
    """ 这是一个测试类 """
    # object = MyFirstClass(name, age, city)
    def __init__(self, name, age, city):
        """ init class
        __init__默认第一位接受的参数为self，self代表着类的实例对象本身
        # python中常用的类方法有三种
        # 一种是我们今天讲到的instance类， 也就实例类
        # 另一种是我们明天要将的 class类对象, 也就是类方法中的@classmethod装饰器
        # 第三种是静态类对象，用@staticemethod装饰器
        
        # 如果这个类需要接受参数， 则需要在这个类下面定义一个 def __init__(self, *args, **kwargs)的方法
        """
        self.log = True   # 这是一个可以直接在外部读取的实例类属性
        self.__name = name   # 在python的class属性定义中 双下划线开头的属性， 属于私有属性，在class外部是不可以直接读取和操作的
        self.__age = age   # 如果你一定要在外部调用他 可以用dir() ==> 获取到被重命名之后的类实例属性名，例如：_MyFirstClass__age
        self.__city = city
        # self.__name 是实例类属性
        # 带有双下划线的实例类属性属于私有属性， 是说这个类中的私有属性不建议在外部直接调用或访问
    
    def __repr__(self):
        """
            返回这个对象的基础信息
            自定义一个返回结果，替换掉默认的返回内存地址的信息
            __str__ or __repr__
        :return:
        """
        if '_MyFirstClass__name' in dir(self):
            return '我的名字：{}， 我的年龄{}， 我在{}城市。 当前的log信息状态为：{}'.format(
                self.__name, self.__age, self.__city, self.log)
        return 'user info is not define ...'

    def reset_name(self, new_name):
        """
            对这个name这个类属性进行重新赋值
        :return:
        """
        self.__name = new_name
    
    def del_all_info(self):
        """
            函数：在python中是不需要绑定任何对象就可以直接使用的
            方法：在python中类方法包含三种，instance类，class类方法和静态类方法(statice)
        :return:
        """
        del self.__name, self.__age, self.__city, self.log


class PythonStudent:
    """ 这个类是python学员信息的存储类"""
    def __init__(self, name, age, city):
        """
            这个类接受3个参数
        :param name: user name
        :param age: user age
        :param city: user city
        """
        self.name = name
        self.age = age
        self.city = city
        self.titles = ('用户名', '年龄', '城市')
    
    def __repr__(self):
        """
            save userinfo
        :return:
        """
        userinfo = (self.name, self.age, self.city)
        user_dict = {key: value for key, value in zip(self.titles, userinfo)}
        user_json = json.dumps(user_dict, ensure_ascii=False, indent=4)

        with open('Users/{}.json'.format(self.name), 'wb') as file:
            file.write(user_json.encode())
        return '数据存储完成'


class Crawl:
    """这是一个userinfo的展示类"""
    def __init__(self, url, xpath, craw_name):
        """
            初始化这个类， 接受三个参数
        :param url: 需要请求的url
        :param xpath: 需要解析这个url的xpath
        :param craw_name: 爬虫的名字
        """
        self.info = url, xpath, craw_name
    
    def __repr__(self):
        """
            repr
        :return:
        """
        print('需要请求的url: {}, 对应的解析xpath:{}, 爬虫对应的名字{}'.format(*self.info))

if __name__ == '__main__':
    # 我们定义了一个类
    # 这个类的名字是MyFirstClass
    # 这个类在实例化的过程中接受3个参数， name/age/city
    # 当这个类接收到这3个入参的时候，初始化3个self.x的属性 .self.name, self.age, self.city
    # 这个类的实例对象如果直接打印， 则返回一个repr的标准输出
    # MyFirstClass 是一个类对象
    # MyFirstClass(name, age, city) 这个对象是一个实例对象
    user_infos = [
        ('Gang', 18, '上海'),
        ('随便', 30, '俄罗斯'),
        ('Raymon', 20, '北京'),
        ('狗子', 5, '新加坡')
    ]
    for user in user_infos:
        print(PythonStudent(*user))
        break
