# 编写一个程序，使用 `while` 循环计算用户输入的任意多个正整数之和。
print("请输入正整数,输入0停止输入:")
sum = 0
while 1:
    num = int(input())
    if num > 0:
        sum += num
    elif num == 0:
        break
    else:
        print("负数不计入总和，请重新输入")
        continue
print(sum)