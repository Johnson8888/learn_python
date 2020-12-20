'''
Author: 弗拉德
Date: 2020-11-30 11:11:36
LastEditTime: 2020-11-30 11:35:24
Support: http://fulade.me
'''


# 题目地址:http://fulade.me/python-handle-list-1-8.html

if __name__ == "__main__":


    # 8-1 动物:想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for循环将每种动物的名称都打印出来。
    # 修改这个程序，使其针对每种动物都打印一个句子，如"A dog would make a great pet"。
    # 在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如"Any of these animals would make a great pet!"这样的句子。
    animal_list = ['dog','cat','pig','sheep']
    for animal in animal_list:
        print(animal)
        print('A {} would make a great pet'.format(animal))
    print('Any of these animals would make a great pet!')


    # 8-2  数到 20:使用一个 for 循环打印数字 1~20(含)。
    for i in range(1,21):
        print(i)
    
    # 8-3 计算 1~ 1000000 的总和:创建一个列表，其中包含数字1~1000000，再使用min()和max()核实该列表确实是从1开始，到1000000 结束的。
    # 另外，对这个列表调用函数sum()，体会一下Python将一百万个数字相加需要多长时间。
    number_list = range(1,1000001)
    print(min(number_list))
    print(max(number_list))
    print(sum(number_list))


    # 8-4 3的倍数:创建一个列表，其中包含 3~30 内能被3整除的数字;再使用一个for循环将这个列表中的数字都打印出来。
    number_list_2 = range(3,30,3)
    for number in number_list_2:
        print(number)

    # 8-5 切片:修改8-1的代码，在末尾添加几行代码，以完成如下任务。 
    # 打印消息"The first three items in the list are:"，再使用切片来打印列表的前三个元素。
    # 打印消息"Three items from the middle of the list are:"，再使用切片来打印列表中间的三个元素。
    # 打印消息"The last three items in the list are:"，再使用切片来打印列表末尾的三个元素。
    print('The first three items in the list are:')
    first_three_items = animal_list[:3]
    print(first_three_items)
    print('Three items from the middle of the list are:')
    print(first_three_items[1])
    print('The last three items in the list are:')
    print(animal_list[-3:])
    