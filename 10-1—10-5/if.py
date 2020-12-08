'''
Author: 弗拉德
Date: 2020-12-08 16:34:37
LastEditTime: 2020-12-08 16:42:59
Support: http://fulade.me
'''


# 题目地址:http://fulade.me/python-if-control-1-10.html


if __name__ == "__main__":
    
    # 10-1 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
    n1 = 10
    n2 = 20
    print(n1 == n2)
    print(n1 != n2)
    print(n1 > n2)
    print(n1 < n2)
    print(n1 >= n2)
    print(n1 <= n2)
    
    # 10-2 请创建一个名为 brush_color 的画笔变量，并将其设置为'green'、'yellow'或'red'。编写一条if语句，检查画笔是否是绿色的，如果是，就打印一条消息。
    brush_color = 'green'
    if brush_color == 'green':
        print('this color is ' + brush_color)
    else:
    # 10-3 像练习 10-2 那样设置画笔的颜色，并编写一个if-else结构。如果画笔是绿色的，就打印一条消息。如果画笔不是绿色的，就打印另一条消息。
        print('this is other color')


    # 10-4 将练习 10-3 中的 if-else 结构改为 if-elif-else 结构。实现以下逻辑
    # 如果画笔是绿色的，就打印一条消息，这是绿色。
    # 如果画笔是黄色的，就打印一条消息，这是黄色。
    # 如果画笔是红色的，就打印一条消息，这是红色。
    brush_color_1 = 'red'
    if brush_color_1 == 'green':
        print('this color is green')
    elif brush_color_1 == 'yellow':
        print('this color is yellow')
    else:
        print('this color is red')
    # 10-5 人生的不同阶段:设置变量 age 的值，再编写一个if-elif-else 结构，根据 age的值判断处于人生的哪个阶段。
    # 如果一个人的年龄小于 2 岁，就打印一条消息，指出他是婴儿。
    # 如果一个人的年龄为 2(含)~4 岁，就打印一条消息，指出他正蹒跚学步。
    # 如果一个人的年龄为 4(含)~13 岁，就打印一条消息，指出他是儿童。
    # 如果一个人的年龄为 13(含)~20 岁，就打印一条消息，指出他是青少年。
    # 如果一个人的年龄为 20(含)~65 岁，就打印一条消息，指出他是成年人。  
    # 如果一个人的年龄超过 65(含)岁，就打印一条消息，指出他是老年人。
    age = 10
    if age < 2:
        print('婴儿')
    if age >= 2 and age < 4:
        print('蹒跚学步')
    if age >= 4 and age < 13:
        print('儿童')
    if age >= 13 and age < 20:
        print('青少年')
    if age >= 20 and age < 65:
        print('成年人')
    if age > 65:
        print('老年人')