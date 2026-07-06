"""
字符串内容是有下标的，我们可以使用下标来访问字符串的内容
    s="Hello World"
下标：  012345678910
语法：
    s[0]

还可以对字符串进行遍历

获取字符串的长度，可以使用len方法
举例 =>         s="Hello World"
打印字符串长度 => print(len(s))
"""
s="Hello World"
# 使用循环对字符串进行遍历
for i in s:
    print(i)

# 打印分隔符
print("="*50)
# 对字符串使用下标来访问
print(s[0])
# 字符串内容不允许修改
# s[0]="W"
print(s)

# 获取字符串的长度
print(len(s))