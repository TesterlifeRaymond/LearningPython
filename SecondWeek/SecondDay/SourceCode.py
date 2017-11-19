"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/19
"""
import json
import os


class Student:
    """ 他是一个学生信息管理的类 """
    def __init__(self, name, age, sex, classinfo):
        """
            类在初始化的时候接受三个必传参数
        :param name: 学生名
        :param age: 学生年龄
        :param sex: 学生的性别
        """
        self.user_info = name, age, sex, classinfo
        self.user_info_back = self.user_info
        self.users_path = 'Users'
        self.titles = ('用户名', '年龄', '性别', '班级')
        self.user_info_dict = {key: value for key, value in zip(self.titles, self.user_info)}

    def save_userinfo(self):
        """
            将用户信息存储到对应的路径下
        :return:
        """
        # Student('Raymond', '20', '男', '1')
        # self.userinfo = ('Raymond', '20', '男', '1')
        # self.userinfo[0] ==> Raymond
        # Raymond.json 这个json文件是否存在与Users这个文件夹中
        # 如果存在， 则返回用户信息已存在
        # 如果不存在， 则通过with 直接写入到Users这个文件夹中
        if '{}.json'.format(self.user_info_back[0]) in \
                os.listdir(os.path.abspath(self.users_path)):
            #   os.listdir返回一个指定路径下的所有文件名
            # os.path.abspath(path), 返回一个相对路径的绝对路径地址
            return '用户信息已存在'

        with open('{}/{}.json'.format(self.users_path, self.user_info_back[0]), 'wb') as file:
            file.write(json.dumps(self.user_info_dict, indent=4, ensure_ascii=False).encode())
    
    def get_userinfo(self):
        """
            查询用户信息的方法
        :return:
        """
        if '{}.json'.format(self.user_info_back[0]) not in \
                os.listdir(os.path.abspath(self.users_path)):
            enter = input('用户信息已删除, 是否重新存储？：Y/N')
            if enter == 'Y':
                self.save_userinfo()
            else:
                return '用户信息不存在请查询其他用户'
        print(json.dumps(self.user_info_dict, indent=4, ensure_ascii=False))
    
    def del_userinfo(self):
        """
            删除掉这个类实例保存的用户信息
        :return:
        """
        del self.user_info

    def __repr__(self):
        """
            返回这个类实例对象存储的是哪一个用户
        :return:
        """
        if 'user_info' not in dir(self):
            return '用户信息已删除'
        return '<Student "{}">'.format(self.user_info_back[0])
    

def func(*args, **kwargs):
    return args, kwargs


class Fruits:
    """ 这是一个水果的类 """
    
    def apple(self):
        """
            return apples
        :return:
        """
        print('这里有一个苹果')
    
    def banana(self):
        """
            return banana
        :return:
        """
        print('这里有一个香蕉')
    
    def orange(self):
        """
            return orange
        :return:
        """
        print('这里有一个橘子')
        
    def all_fruits(self):
        self.apple()
        self.banana()
        self.orange()


class Sum:
    """ pass """
    def __init__(self, num_a, num_b):
        self.numbers = [num_a, num_b]
    
    def return_sum(self):
        return sum(self.numbers)
    
    def modify_num(self, num_index: int, value):
        try:
            self.numbers[num_index] = value
        except IndexError:
            print('超过最大index， 请重新输入')
    
    def __repr__(self):
        return '<Sum ({} + {} : {})>'.format(*self.numbers, self.return_sum())


if __name__ == '__main__':
    aaa = Sum(10, 5)
    print(aaa)
    aaa.modify_num(0, 100)
    print(aaa)
    aaa.modify_num(1, 55)
    print(aaa)
    aaa.modify_num(2, 17)

    # fruits = Fruits()
    # fruits.apple()
    # fruits.banana()
    # fruits.orange()
    # userinfo = ('港', 20, '男', '二班')
    # userinfo = ('Raymond', 30, '男', '一班')
    # ray = Student(*userinfo)
    # ray.del_userinfo()
    # print(ray.save_userinfo())
    # ray.del_userinfo()
    # print(ray)
    # ray.get_userinfo()
    # print(ray.user_info)
    # print(dir(ray))
    # print('user_info' in dir(ray))
    # print(ray.user_info in dir(ray))
    # print(ray)
    # ray.get_userinfo()
