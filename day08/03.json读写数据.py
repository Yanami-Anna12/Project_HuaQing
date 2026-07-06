"""
    什么是json数据？
    json数据主要是用于做前后端数据交互的，其实类似于我们学的字典

    写入到json数据
        里面存储的是json格式的文件
        将数据写入到json文件中
        步骤：
        导包 => import json
        with open("json数据的文件名","参数",encoding="utf-8") as f:
            json.dump(字典,参数,ensure_ascii=False)
        解释说明：
            with        => 固定写法
            open        => 打开JSON数据，打开JSON的文件
            参数：
                w       => write  写入文件
                r       => read   读取文件
                b       => binary 二进制
                encoding => "utf-8" 设置成通用编码格式
                as      => 起别名
                ensure_ascii => False 防止ascii转换成unicode码

    读取json格式的文件：
        with open("要读取的json文件","参数",encodid="utf-8") as f:
            data=json.load(f)
"""
# 导包
import json
# 准备json格式的数据，也就是python中的字典
info={"name":"张三","age":18,"gender":"男"}
# 向data.json文件中写入json数据
with open("data.json","w",encoding="utf-8") as f:
    json.dump(info,f,ensure_ascii=False)

print("数据写入完毕！")

print("-"*50)

#  读取data.json文件，在控制台打印数据
with open("data.json","r",encoding="utf-8") as f:
    data=json.load(f)
print(f"读取到的数据是：{data}")