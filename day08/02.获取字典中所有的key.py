"""
    获取字典中所有的key,可以使用kes()
    语法： 字典名.keys()

    通过字典中的键名获取值的方法： 字典名.get("键名")

    # 获取字典中的所有值：  值点名.values()
"""
info={"name":"张三","age":18,"gender":"男"}
# 获取字典中的所有key
keys=info.keys()
# 循环遍历，取出字典中的每个key
for key in keys:
    print(f"{key} ===> {info.get(key)}")

print("="*50)

# 获取字典中所有的值
for index,value in enumerate(info.values()):
    print(f"{index} ==> {value}")