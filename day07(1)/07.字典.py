"""
    字典也是一种数据类型，但是字典里面存储的是key_value值(键值对)的形式
    列表 => []
    元祖 => ()
    字典 => {}
"""
# 定义一个字典
# 语法：
# {"键名1"："键值1"，"键名2"："键值2",...}
info={"name":"张三","age":18,"addr":"长沙"}
print(info)
info2={
    "name":"李四",
    "age":20,
    "addr":"广州"
}
# 给info字典添加一个键值对
info["gender"]="男"
print(info)
print("="*80)
# 修改字典中的键值
info["name"]="张三丰"
print(info)
print("="*80)
# 获取字典中的值
print(info2["name"])
print("="*80)
# 删除字典中的成员
del info["name"]
print(info)