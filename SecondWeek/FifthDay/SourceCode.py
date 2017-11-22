"""
@Name: SourceCode
@Version: 
@Project: PyCharm Community Edition
@Author: liujinjia
@Data: 2017/11/22
"""
import json
import random
import string
import time

"""
实现一个构造测试数据的类
# 这个类能生成指定号段的手机号码
# 这个类能生成随机中文名字， 可指定生成名字的姓氏和长度
# 这个类可以生成一共用户信息的字典， 该用户信息字典包含 用户中文名 密码 邮箱 手机号 创建这条数据的时间
# 将用户信息存储到用户文件夹下
# 定义repr 查看对应类实例对象的基础信息
"""

FIRST_NAME_ENUM = '赵钱孙李周吴郑王'
LAST_NAME_ENUM = '与玉鱼汪千苗喵'


class Datas:
    """ 这是一个构造测试数据的类"""
    def __init__(self, mobile_number_head=None, first_name_head=None, name_lenth=None):
        """
        初始化Datas类并接受必要的入参
        :param mobile_number_head: 指定的手机号段
        :param first_name_head: 指定的姓
        :param name_lenth: 指定用户名的长度
        """
        self.mobile_head = mobile_number_head
        self.first_name = first_name_head
        self.name_lenth = name_lenth
        self.save_json_file_path = 'Users'
        self.return_title = 'Datas<{}>'
        self.func_args = [item for item in dir(self) if not item.startswith('__') and callable(getattr(self, item))]

    def write_file(self, file_name, data):
        """ 讲文件写入Users路径"""
        file_name = '{}/{}.json'.format(self.save_json_file_path, file_name)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(data)
    
    def make_user_json_and_write_file(self):
        """
            将随机生成的用户信息， 存储进文件
        :return:
        """
        titles = ('中文名', '密码', '手机号', '邮箱','创建时间')
        name = self.make_user_name()
        
        infos = (
            name,
            self.make_random_password(),
            self.mobile(),
            self.make_user_email(),
            time.strftime('%Y-%m-%d %H:%M:%S')
        )
        data = json.dumps({key: value for key, value in zip(titles, infos)}, ensure_ascii=False, indent=4)
        self.write_file(name, data)

    def make_random_password(self):
        """
            创建一个随机的用户密码
        :return:
        """
        return ''.join(random.sample(string.digits + string.ascii_letters + string.punctuation, 8))

    def make_user_email(self):
        """
        :return:
        """
        buf = ['@163.com', '@qq.com', '@gmail.com', '@yahoo.com']
        head = random.sample(string.ascii_letters + string.digits, 8)
        email = ''.join(head) + random.choice(buf)
        return email

    def make_user_name(self) -> str:
        """
            生成一个随机的用户名
        :return:
        """
        if not self.first_name:
            self.first_name = random.choice(list(FIRST_NAME_ENUM))
        if not self.name_lenth:
            self.name_lenth = 2 if random.randint(1, 100) > 50 else 1

        last_name = ''.join(random.sample(list(LAST_NAME_ENUM), self.name_lenth))
        print('用户名是 ：{}'.format(self.first_name + last_name))
        return self.first_name + last_name
        
    def mobile(self):
        """ 生成一个指定号段的手机号， 如果没有指定则随机返回一个号段的手机号"""
        if self.mobile_head:
            try:
                int(self.mobile_head)
            except Exception as err:
                return err
    
        if self.mobile_head and len(list(self.mobile_head)) == 3:
            return self.mobile_head + ''.join(random.sample(list(string.digits), 8))
        mobile = ['137', '138', '139', '131', '140', '150', '177']
        return random.choice(mobile) + ''.join(random.sample(list(string.digits), 8))

    def __repr__(self):
         """
            pass
         :return:
         """
         return 'Datas(<{}>)'.format(self.func_args)


class FruitsMarket:
    """ 这是一个水果市场"""
    def __init__(self, mkname, create_time=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.mkname = mkname
        self.create_time = create_time
        self.all_fruits_count = 100
    
    def buy_some_fruits(self, fruits_count):
        """ 水果市场进货功能 """
        self.all_fruits_count += fruits_count
    
    def cell_some_fruits(self, fruits_count):
        self.all_fruits_count -= fruits_count
    
    def throw_some_fruits(self):
        self.all_fruits_count -= 2
    
    def __repr__(self):
        return str(self.all_fruits_count)


class InterfaceTest(Datas):
    def __init__(self):
        super(InterfaceTest, self).__init__()
        print(self.mobile())
        print(self.make_user_name())


if __name__ == '__main__':
    # datas = Datas()
    # datas.make_user_json_and_write_file()
    # print(datas)
    # market = FruitsMarket('上海贸易中心')
    # print(market)
    # market.cell_some_fruits(21)
    # print(market)
    # market.throw_some_fruits()
    # print(market)
    # market.cell_some_fruits(50)
    # print(market)
    interface = InterfaceTest()

