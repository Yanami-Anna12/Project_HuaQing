# # 输入一个字符串,输出所有偶数的索引位置的字符串
# s=input("请输入一段字符串内容：")
# print(s[::2])

# # 编写一个程序,查找输入的字符串当中是否包含"python"字符串
# s=input("请输入一段文本内容：")
# if "python" in s:
#     print("文本中包含python文字内容！")
# else:
#     print("文本中不包含python文字内容！")

# 编写一个字符串的分析程序
#     计算字符串的长度
#     翻转字符串
#     统计各个字符出现的次数

# s=input("请输入一段文本内容：")
# print(f"字符串内容长度是：{len(s)}")
# print(f"翻转后的内容是：{s[::-1]}")
# 统计各个字符出现的次数    hello everyone!

# {"h":1,"e":4,...}

# a=tuple(s)
# b={}
# # print(a)
# for i in a: # 循环遍历元祖
#     # 判断键名在字典中是否存在，如果不存在就添加进去，并设置值为1，如果存在就取出这个键名对应的值，并将值+1
#     if b.get(i)==None:
#         b[i]=1
#     else:
#         b[i]=b.get(i)+1
# print(b)


# 编写一个程序,定义一个列表,将列表里面所有的元素去重
# list1=[1,12,3,13,32,123,12,43]
# list2=[1,1,3,12,32,13,12,53]
# # 合并两个列表，列表中会出现很多重复的内容
# list3=list1+list2 # [1, 12, 3, 13, 32, 123, 12, 43, 1, 1, 3, 12, 32, 13, 12, 53]
# print(list3)

# # 定义一个空列表
# list4=[]
# for i in list3: # 循环遍历list3
#     # 取出list3中的每个成员，判断当前的成员在list4中是否出现过，如果没有出现过才添加到list4中去
#     if i not in list4:
#         list4.append(i)

# print(list4)

# """
# 使用字典做一个简单的学生管理系统
# 1. 定义一个空的字典 => students = {}
# 2. 当我们输入 => 
#     1 的时候,表示添加学生
#     2 的时候,表示查询学生
#     3 的时候,表示修改学生
#     4 的时候,表示删除学生
#     5 的时候,表示退出系统
# 3. 一定要使用死循环
# """
# 定义一个学生字典
s={}


while True:
    # 打印菜单选项
    print("\n==========学生成绩管理系统=========")
    print("1.添加学生")
    print("2.查询学生")
    print("3.查询所有学生")
    print("4.修改学生")
    print("5.删除学生")
    print("6.退出系统")
    # 接收用户输入的内容
    c=input("请选择对应的操作：【1～6】").strip()
    if c=="1":
        # TODO 添加学生
        name=input("请输入要添加的学生姓名：")
        if name in s:
            print("该学生已存在，不能重复添加")
        else:
            s[name]=name
            try: # try中的代码是尝试运行，如果出现错误我们就执行except中的内容
                score=float(input("请输入成绩："))
                if score>100 or score<0:
                    print("成绩输入超出范围！")
                else:
                    s[name]=score
            except ValueError:
                print("成绩输入有误！")
    elif c=="2":
        # TODO 查询学生
        name=input("请输入要查询的学生姓名：")
        if name in s:
            print(f"{name} => 查询的成绩为：{s.get(name)}")
        else:
            print("要查询的学生不存在！")
    elif c=="3":
        # TODO 查询所有学生
        print("系统中的所有学生信息如下：")
        for k in s.keys():
            print(f"{k} ==> {s[k]}")
    elif c=="4":
        # TODO 修改学生
        # 判断要修改的学生姓名是否存在
        name=input("请输入要修改的学生姓名：")
        if name in s:
            score=float(input("请输入修改后的成绩："))
            # 判断输入的成绩是否符合0～100
            if score>100 or score<0:
                print("输入的成绩有误！")
            else:
                s[name]=score
                print("修改成功！")
        else:
            print("修改失败，要修改的学生不存在！")
    elif c=="5":
        # TODO 删除学生
        # 判断要删除的学生姓名是否存在
        name=input("请输入要删除的学生姓名：")
        if name in s:
            if "y"==input(f"确认删除{name}这个同学信息吗？【y/n】"):
                # 确定删除该学生吗？
                del(s[name])
        else:
            print("删除失败，要删除的学生不存在！")
    elif c=="6":
        # TODO 退出系统学生
        print("感谢使用学生成绩管理系统，再见！")
        break # 退出循环
    else:
        print("输入有误，请重新输入！")
