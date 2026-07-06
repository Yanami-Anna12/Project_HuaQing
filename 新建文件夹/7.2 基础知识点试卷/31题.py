# 用户输入一个字符串，程序统计该字符串中每个字符出现的次数，并以字典形式输出结果
s = input("请输入字符:")
dict1 = {}
for key in s:
    if key in dict1:
        dict1[key] += 1
    else:
        dict1[key] = 1

print(dict1)