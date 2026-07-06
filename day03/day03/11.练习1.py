"""
看代码说结果
"""

index = 1 # 循环初始变量
while index < 4:
    print(f"小刘跑了第{index}圈")  
    index += 1 # index =idnex+1
    while index == 3:
        print("受伤了,送往医院")
        break
        # continue
print("程序结束")

# continue
#  小刘跑了第1圈  小刘跑了第2圈 受伤了,送往医院
# break
#  小刘跑了第1圈  小刘跑了第2圈 受伤了,送往医院 小刘跑了第3圈  程序结束