# 对列表元素的遍历,获取列表中的每个成员
list1=['a','b','c','d','e']
# 获取列表的长度(列表中元素的个数)
# print(len(list1))

# 使用for循环来遍历列表中的元素
for item in list1:
    print(item)

print("="*80)

# 获取下标
for index,item in enumerate(list1):
    print(f"下标：{index},成员：{item}")