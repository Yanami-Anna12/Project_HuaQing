import random

num = random.randint(1,100)
while 1:
    a = int(input("请输入数字"))
    if a > num:
        print("太大了!")
    elif a < num:
        print("太小了!")
    else:
        print("恭喜你，猜对了!")
        break