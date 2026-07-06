# x = int(input("请输入数字x:"))
# y = int(input("请输入数字y:"))
# print(x + y, '\n', x - y, sep='')
# if (a > b and a > c):
#     print("a更大")
# elif (a < b and c < b):
#     print("b更大")
# elif (c > a and c > b):
#     print("c更大")
"""
x=int(input("请输入数字x:"))
y=int(input("请输入数字y:"))

y =
"""
judgement = True
while (judgement):
    a = int(input("请输入边长a:"))
    b = int(input("请输入边长b:"))
    c = int(input("请输入边长c:"))
    if (a + b > c and a + c > b and b + c > a):
        judgement = False
        if (a == b == c):
            print("这是等边三角形")
        elif (a == b != c or a == c != b or b == c != a):
            print("这是等腰三角形")
        elif (a != b != c):
            print("这是普通三角形")
    else:
        print("这不是三角形,请重新输入")
