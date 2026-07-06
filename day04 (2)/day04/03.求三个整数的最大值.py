"""
求三个整数的最大值
a=10
b=5
c=8
比较三个变量，判断，输出最大值
思路：
    如果a与b比较，a比b大，那么在拿a和c比较，如果a比c也要大，那么a就是这三个数中最大的数字，
    否则a比c也要小，那么c就是这三个数字中的最大值
"""
# 求用户输入的三个数字中的最大值
# 接收用户输入的整数，并把数字字符串转换成整数
a=int(input("请输入一个整数"))
b=int(input("请输入一个整数"))
c=int(input("请输入一个整数"))
# max_val保存三个变量中的最大值
max_val=0

if a>=b: # 先判断a是否大于等于b
    if a>=c: # 再次判断a是否大于等于c
        max_val=a
    else: # 如果c大于a，那么就把c保存到max_val中
        max_val=c
elif b>=c: # 先判断b是否大于等于c
    if b>=a: # 再次判断b是否大于等于a
        max_val=b
    else: # 如果a大于b，那么就把a保存到max_val中
        max_val=a 
elif c>=a: # 先判断c是否大于等于a
    if c>=b: # 再次判断c是否大于等于b
        max_val=c
    else:# 如果b大于c，那么就把b保存到max_val中
        max_val=b
print(f"最大值是：{max_val}")