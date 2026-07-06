"""
什么是三元运算符(三目运算符)
    其实就是简化版的if-else语句
语法：
    条件为真时返回的结果 if 判断条件 else 条件为假时返回的结果
"""
a=10
b=20
# 条件为true
c=a if a<b else b
print(f"c = {c}")

# 条件为false
d=a if a>b else b
print(f"d = {d}")