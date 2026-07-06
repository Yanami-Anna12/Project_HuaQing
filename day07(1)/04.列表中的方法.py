# 列表中的方法
list1=['a','b','c','d','e']
list2=["f","a","b"]
list3=list1+list2 # 列表合并/拼接
list4=[42,12,66,3]
print(list3)
print("="*80)

# 把list1复制3分
# print(list1*3)
# count统计列表中元素出现的 次数
print(list3.count('a'))
print("="*80)
# index 获取index中的内容中列表中对应的下标
print(list1.index("e"))
print("="*80)
# 移除列表中的元素
list1.remove("c")
print(list1)
print("="*80)
# 将列表内容翻转
list1.reverse()
print(list1)
print("="*80)
# 清空列表中的元素内容
list1.clear()
print(list1)
print("="*80)
# 获取列表中的最大值max、最小值min、列表的长度
# 注意：针对列表中都是数字成员
print(max(list4))
print(min(list4))
print(len(list4))
print("="*80)
# 列表中的成员排序 返回一个新的列表
print(sorted(list4)) # 默认是升序排列
print(sorted(list4,reverse=True)) # reverse=True 按降序排列
print(sorted(list2)) # 默认是升序排列，可以对字母排序 a-z