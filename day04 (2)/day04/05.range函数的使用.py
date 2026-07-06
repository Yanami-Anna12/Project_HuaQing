"""
range函数是一个序列的数据，可以指定数字范围
    range(n) => 从0开始，到n-1的数字
    range(n,m) => 从n开始，到m-1结束
    range(n,m,step) => 从n开始，到m-1结束,每次变化step幅度的值

    特点：包含头，不包含尾部的值
"""

num1=range(5) # 0，1，2，3，4
# print(num1)
for item in num1:
    print(item)

print('===========')

num2=range(5,10) # 5,6,7,8,9
for item in num2:
    print(item)
print('===========')

# 每次增加2 => 从5开始 5,7,9
num2=range(5,10,2) # 5,7,9
for item in num2:
    print(item)