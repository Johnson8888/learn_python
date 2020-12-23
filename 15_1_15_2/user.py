'''
Author: 弗拉德
Date: 2020-12-23 11:53:12
LastEditTime: 2020-12-23 12:05:47
Support: http://fulade.me
'''



class User(object):

    login_attempts = 0
    
    def __init__(self,first_name,last_name):
        """
        初始化方法
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """
        输出当前用户的信息
        """
        print("My name is {} {}".format(self.first_name,self.last_name))

    def increment_login_attempts(self):
        """
        login_attempts 自增 1
        """
        self.login_attempts = self.login_attempts + 1
        print("login_attempts = {}".format(str(self.login_attempts)))

    def reset_login_attempts(self):
        """
        login_attempts 重置为1
        """
        self.login_attempts = 0
        print("login_attempts = {}".format(str(self.login_attempts)))



### 题目地址： http://fulade.me/python-class-1-15.html

if __name__ == "__main__":

    ## 15-1 用户:创建一个名为 User 的类，其中包含属性 first_name 和 last_name。
    # 在类User中定义一个名为 describe_user()的方 法，它打印用户信息摘要，创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
    user1 = User("Fulade","Li")
    user1.describe_user()
    user2 = User("Long","Cheng")
    user2.describe_user()
    
    ## 15-2 在为完成练习 15-1 而编写的User类中，添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，它将属性login_attempts 的值加 1。再编写一个名为 reset_login_attempts()的方法，它将属性login_attempts的值重置为0。
    #根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增;然后，调用方法 reset_login_attempts()，并再次打印属性 login_attempts 的值，确认它被重置为0。

    user3 = User("Dehua","Liu")
    user3.increment_login_attempts()
    user3.increment_login_attempts()
    user3.increment_login_attempts()
    user3.reset_login_attempts()