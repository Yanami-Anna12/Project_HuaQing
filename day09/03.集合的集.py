"""
集合有并集，交集，差集
    并集 => | union             表示两个集合合并元素
    交集 => & intersection      表示两个集合中共有的元素
    差集 => - difference        表示两个集合中第一个集合减去第二个集合中的内容后存在的不同元素
"""
s1={"a","b","c"}
s2={1,2,3,"a"}
# 使用并集
# s3=s1 | s2
# print(s3)

# 使用交集
# s4 = s1 & s2
# print(s4)

# 使用差集
# s5=s1-s2
# print(s5)

# 集合的推导式
# s6={i for i in range(11) if i%2==0}
# print(s6)

# 将列表中的元素去重后再求平方
# list=[1,3,5,7,3,5]
# s7={i**2 for i in list}
# print(s7)

# 字典推导式
s8={i:i**2 for i in range(6)}
print(s8)