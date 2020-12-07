'''
Author: 弗拉德
Date: 2020-12-07 20:51:28
LastEditTime: 2020-12-07 20:54:35
Support: http://fulade.me
'''

# 题目地址:http://fulade.me/python-tuple-1-9.html


if __name__ == "__main__":
    

    # 9-1 有一个菜摊，提供五种蔬菜。请想出五种简单的蔬菜，并将其存储在一个元组中。
    vegetables = ('ginger','cabbage','celery','spinach','potato')
    # 9-2 使用一个 for 循环将该菜摊提供的五种蔬菜都打印出来。
    for v in vegetables:
        print(v)
    # 9-3给元组变量赋值，修改其中一种蔬菜为新品种，并使用一个 for 循环将新元组的每个元素都打印出来。
    vegetables = ('ginger','cabbage','celery','spinach','corn')
    for v in vegetables:
        print(v)
    # 9-4尝试修改其中的一个元素，核实 运行时会报错。
    vegetables[0] = 'taro'