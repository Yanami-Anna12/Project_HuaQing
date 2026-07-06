s="今天星期三，天气好晴朗！"

if "晴朗" in s:
    print("晴朗 在字符串内容中")
else:
    print("晴朗 不在字符串内容中")

print("="*50)

# 某个内容不在字符串中，满足条件就进入到if中
if "篮球" not in s:
    print("篮球 不在字符串内容中")
else:
    print("篮球 在字符串内容中")