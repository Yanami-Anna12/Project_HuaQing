"""
    正常使用for循环，是没有下标的，那么我们可以给要被遍历套上enumerate()
    还可以修改起始下标
    
    使用方法：index指的是下标
    for index,item inumerate(被遍历的数据)：
        print(index,item)
"""
s1="AI人工智能"
#   01 2345
for index,item in enumerate(s1):
    print(index,item)

print("=================")

# 指定下标的起始位置从10开始
for index,item in enumerate(s1,start=10):
    print(index,item)