"""
利用循环来求5~50之间的奇数和
思路：
    循环变量初始值 index=5和累加变量 sum=0
    判断条件 index<=50
    循环体  将5～50之间的偶数累加 
        如何判断循环变量是否是偶数？ 可以使用 index%2==0
"""
index=5
sum=0
while index<=50:
    if index%2: # 隐士转换，正常判断应该是 index%2==1  因为数字1转bool类型是true
        sum+=index
    index+=1
print(f"5～50之间所有奇数累加结果是：{sum}")