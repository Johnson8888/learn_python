'''
Author: 弗拉德
Date: 2020-12-10 13:38:33
LastEditTime: 2020-12-10 13:56:27
Support: http://fulade.me
'''

# 题目地址:http://fulade.me/python-dict-1-11.html


if __name__ == "__main__":


    # 11-1 请想出5个人的名字，并将这些名字用作字典中的键，想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。
    name_dict = {'Kobe':24,'James':23,'Bob':21,'John':14,'White':1}
    for key, value in name_dict.items():
        print(key + ' like ' + str(value))

    # 11-2 创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile':'egypt'。使用循环为每条河流打印一条消息，如"The Nile runs through Egypt."。
    # 使用循环将该字典中每条河流的名字都打印出来。使用循环将该字典包含的每个国家的名字都打印出来。   
    river_dict = {'nile':'egypt','Changjiang':'china','Amazon':'Brazil'}
    for key, value in river_dict.items():
        print('The {} runs through {}.'.format(key,value))
    for key in river_dict.keys():
        print(key)
    for value in river_dict.values():
        print(value)

    # 11-3 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名;在每个字典中
    # 包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。

    pet_0 = {'breed':'Golden Retriever','boss':'kobe'}
    pet_1 = {'breed':'Husky','boss':'James'}
    pet_2 = {'breed':'Pomeranian','boss':'Bob'}
    pets = [pet_0,pet_1,pet_2]
    for pet in pets:
        print('Breed is {} and boss is {} .'.format(pet['breed'],pet['boss']))
