# 输入一个年份,判断该年份是平年还是闰年,能被4整除且不能被100整除的,或能被400整除的是闰年
year = int(input("请输入一个年份:"))
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")