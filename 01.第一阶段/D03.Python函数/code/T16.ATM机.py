# 定义主菜单函数menu
def menu():
    print("----------------主菜单----------------")
    print(f"{name},您好,欢迎使用ATM机,请选择操作:")
    print("[1]\t查询余额")
    print("[2]\t存款")
    print("[3]\t取款")
    print("[0]\t退出")
    return input("请输入选项前的数字执行操作:")
    # choice = int(input("请输入选项前的数字执行操作:"))
    # while choice != 0 or 1 or 2 or 3:
    #     choice = int(input("您输入的内容不符合规范,请按规范执行操作:"))
    #     if choice == 0 or 1 or 2 or 3:
    #         break
    # if choice == 0:
    #     print("感谢您的使用,欢迎您下次再来!")
    # elif choice == 1:
    #     choice_1(True)
    # elif choice == 2:
    #     choice_2()
    # elif choice == 3:
    #     choice_3()


# 定义查询金额函数choice_1
def choice_1(show_header):
    if show_header:
        print("---------------查询余额---------------")
    print(f"{name},您好,您的余额为:{money}元")
    menu()


# 定义存款函数choice_2
def choice_2():
    print("-----------------存款-----------------")
    money_more = int(input("请输入您想要存入的金额:"))
    global money
    money += money_more
    print(f"存款成功!")
    choice_1(False)


# 定义取款函数choice_3
def choice_3():
    print("-----------------取款-----------------")
    money_less = int(input("请输入您想要取出的金额:"))
    global money
    money -= money_less
    print(f"取款成功!")
    choice_1(False)


# 程序运行
name = input("请输入用户名:")
money = 5000000
passwd = int(input("请输入密码:"))
while passwd != 123456:
    passwd = int(input("密码错误,请重新输入密码:"))
    if passwd == 123456:
        break
while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        choice_1(True)
        continue  # 通过continue继续下一次循环,一进来就回到主菜单
    elif keyboard_input == "2":
        choice_2()
        continue
    elif keyboard_input == "3":
        choice_3()
        continue
    else:
        print("感谢您的使用,欢迎您下次再来!")
        break
# menu()
