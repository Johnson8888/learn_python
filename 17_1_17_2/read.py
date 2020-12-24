'''
Author: 弗拉德
Date: 2020-12-24 20:36:55
LastEditTime: 2020-12-24 20:45:42
Support: http://fulade.me
'''
import os
if __name__ == "__main__":


    #17-1 在文本编辑器中新建一个文件，写几句话来总结一下你至
    #此学到的Python知识。将这个文件命名为 learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，读取整个文件，并打印。
    folder_path = os.path.join(os.getcwd(),"17_1_17_2")
    file_path = os.path.join(folder_path,"learning_python.txt")
    with open(file_path) as f:
        content = f.read()
        print(content)



    # 17-2 访客:编写一个程序，提示用户输入其名字;用户作出响应后，将其名字写 入到文件 guest.txt中。
    username_file_path = os.path.join(folder_path,"user_name.txt")
    message = input("please input user name: ")
    with open(username_file_path, 'a') as file_object:
        print_message = "welcome " + message + "\n"
        file_object.write(print_message)
        print(print_message)
        file_object.close()