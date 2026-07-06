# 预测孩子身高
faHeight = float(input("请输入父亲身高:"))
moHeight = float(input("请输入母亲身高:"))

# 判断孩子性别
sex = str(input("请输入孩子性别,b表示男孩,g表示女孩:"))
if sex == 'b':
    childHeight = (faHeight + moHeight) * 0.54
elif sex == 'g':
    childHeight = (faHeight * 0.932 + moHeight) / 2
else:
    print("输入错误")
    exit()

# 判断是否喜欢运动
sport = str(input("请输入孩子是否喜欢运动,y表示喜欢,n表示不喜欢:"))
if sport == 'y':
    childHeight *= 1.02
elif sport == 'n':
    childHeight *= 1
else:
    print("输入错误")
    exit()

# 判断是否拥有良好的卫生习惯
habit = str(input("请输入孩子是否拥有良好的卫生习惯,y表示喜欢,n表示不喜欢:"))
if habit == 'y':
    childHeight *= 1.015
elif habit == 'n':
    childHeight *= 1
else:
    print("输入错误")
    exit()

print(childHeight)