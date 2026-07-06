while 1:
    score = int(input("请输入成绩"))
    if 90 <= score <= 100:
        print("等级:A")
        break
    elif 80 <= score < 90:
        print("等级:B")
        break
    elif 70 <= score < 80:
        print("等级:C")
        break
    elif 60 <= score < 70:
        print("等级:D")
        break
    elif 0 <= score < 60:
        print("等级:E")
        break
    else:
        print("成绩无效,请重新输入")