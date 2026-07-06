"""
字符串的属性和方法
+           字符串拼接
*           将字符串复制几遍
upper       将字符串中的小写字母转换成大写字母
lower       将字符串中的大写字母转换成小写字母
split       切割字符串，切割得到的结果是一个列表
strip       去除字符串两边的空格
count       统计字符串里面的字符
len         统计字符串的长度
startswith  判断字符串是否以某某开头
index()     查看某个字符串内容是否存在，如果存在就返回对应所在的下标，如果没查到就会报错
"""

s="Hello World"
# 字符串的属性
print(s+" python!")
print(s*3)
# 字符串的函数/方法 调用函数 => 函数名()
print(s.upper()) # 调用字符串的转换成大写方法
print(s.lower()) # 调用字符串的转换成小写方法
print(s.split("l")) # ["he","","o Wor","d"]
print(s.index("l")) # 找到第一次出现的下标位置  2
print(s.count(" ")) # 统计指定内容在字符串中出现的次数
print(len(s)) # 打印字符串的长度
print(s.startswith("Hel")) # 判断是否以Hel开头，返回一个布尔值
print(s.endswith("rld")) # 判断是否以rld结尾，返回一个布尔值
print(s.replace("l","a")) # 替换字符串中的内容
