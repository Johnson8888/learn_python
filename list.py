'''
Author: 弗拉德
Date: 2020-11-24 20:16:23
LastEditTime: 2020-11-24 20:53:04
Support: http://fulade.me
'''

# 题目地址：https://www.fulade.me/python-list-7.html


if __name__ == "__main__":

    #### 7-1 将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
    names = ['Steve Jobs','Elon Musk','Zuckerberg']
    print('My friends {} 、{} 、 {}'.format(names[0],names[1],names[2]))

    #### 7-2 如果你可以邀请任何人一起共进晚餐(无论是在世的还是故去的)，你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人， 然后，打印列表。
    invite_list = ['Bob','Petter','James']
    print(invite_list)
    #### 7-3 修改嘉宾名单:你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。然后再一次打印这个列表。
    invite_list[0] = 'Tim Cook'
    print(invite_list)

    ### 7-4 添加嘉宾:你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
    ### 使用 insert()将一位新嘉宾添加到名单开头。
    ### 使用 insert()将另一位新嘉宾添加到名单中间。
    ### 使用 append()将最后一位新嘉宾添加到名单末尾。
    invite_list.insert(0,'Kobe')
    invite_list.insert(2,'Johnson')
    invite_list.append('Heisenberg')
    print(invite_list)

    #### 7-5 缩减名单:你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。 使用 pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一下.
    poped_1 = invite_list.pop()
    print(poped_1)
    poped_2 = invite_list.pop()
    print(poped_2)
    poped_3 = invite_list.pop()
    print(poped_3)
    poped_4 = invite_list.pop()
    print(poped_4)
    print(invite_list)

    #### 7-7 放眼世界: 想出至少 5 个你渴望去旅游的地方。将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python 列表。
    #### 使用 sorted()按字母顺序打印这个列表，同时不要修改它。再次打印该列表，核实排列顺序未变。
    #### 使用 sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。再次打印该列表，核实排列顺序未变。
    #### 使用 reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
    #### 使用 reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
    #### 使用 sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
    #### 使用 sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
    cisties = ['hawaii','beijing','sanPaulo','tokyo','shanghai']
    print(sorted(cisties))
    print(cisties)
    print(sorted(cisties,reverse=True))
    print(cisties)
    cisties.reverse()
    print(cisties)
    cisties.reverse()
    print(cisties)
    cisties.sort()
    print(cisties)
    cisties.sort(reverse=True)
    print(cisties)