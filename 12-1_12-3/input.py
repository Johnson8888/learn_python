'''
Author: 弗拉德
Date: 2020-12-20 15:28:23
LastEditTime: 2020-12-20 15:44:49
Support: http://fulade.me
'''


### 题目地址： http://fulade.me/python-input-12.html

if __name__ == "__main__":
    

    #12.1 编写一个程序，询问用户要咨询什么样的汽车，并打印一条消息，如"Let me see if I can find you a Subaru"。
    #car_name = input("Tell me a name of the car:")
    #print("Let me see if I can find you a " + car_name)  
    
############################################################################################################################################

    #12.2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一条消息，指出没有空桌；否则指出有空桌。
    #user_count = input("How many users? ")
    #user_count = int(user_count)
    #if user_count > 8:
    #    print("没有空桌了")
    #else:
    #    print("有空桌")

############################################################################################################################################

    #12.3 让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
    number_str = input("Input a number:")
    number = int(number_str)
    if number % 10 == 0:
        print("是10的整数倍")
    else:
        print("不是10的整数倍")
