"""
python中的列表类似于一个容器，可以用来保存多个不同类型的值，他有下标
语法：
list=[元素1，元素2，元素3，...元素n]
可以通过下标来访问列表中的某个元素
可以通过下标来修改列表中的某个元素
可以通过下标来添加列表中的某个元素
可以通过下标来删除列表中的某个元素
"""
list=[10,20,30,"Hello World",True,12.5]
# 通过下标来访问
print(list[0])
# 通过下标来修改
list[0]=100
print(list)
# 通过下标来删除元素
del list[0]
print(list)
# 通过下标来添加列表成员
# list[6]="Hello EveryOne!"
# 在指定的下标位置，插入新的元素 100
list.insert(2,100)
list.append("Hello EveryOne!")
print(list)
print("="*80)

# 遍历列表成员
for item in list:
    print(item)

print("="*80)

# enumerate 可以使用下标
for (index,item) in enumerate(list):
    print(index,item)

