info={"name":"张三","age":18,"gender":"男"}

# 使用字典的 items()方法
for key,value in info.items():
    print(f"{key}-->{value}")
print("-"*50)

# 直接遍历字典
for key in info:
    # print(f"{key} ===> {info.get(key)}")
    print(f"{key} ===> {info[key]}")
print("-"*50)

# 获取字典中所有的值
for index,value in enumerate(info.values()):
    print(f"{index} ==> {value}")