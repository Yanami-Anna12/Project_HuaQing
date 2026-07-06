"""
元祖是一组不可以改变的列表
元祖使用()来表示
"""
t1=tuple("Hello EveryOne!")
t2=(10,20,30)
t3=(123,) # 如果元祖中只有一个元素，需要在后面加,号

print(t1,type(t1))
print(t1[3])
print(t2[1]) # 获取t2中下标为1的成员
print(t2+t3)
print("="*80)

# 元祖中的成员内容不能被修改
# t2[1]=100 # 会报错
# print(t2)

# 元祖的内容不能被删除
# del t2[1] # 会报错
# print(t2)

# 元祖的推导式
a=(i for i in range(1,10) if i%2==0)
print(a) # 此处打印的是元祖的地址
print(tuple(a))