code = "123456"
n = 3
while n >= 1:
    code1 = input("请输入密码:")
    if code1 == code:
        print("登陆成功")
        break
    else:
        n -= 1
        print(f"密码错误,请重新尝试,还剩{n}次机会")
        if n == 0:
            print("账户锁定")
