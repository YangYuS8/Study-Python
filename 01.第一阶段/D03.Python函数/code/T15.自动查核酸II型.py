print("欢迎来到支配剧场！\n请出示您的健康码及72小时核酸证明，并配合测量体温！")


def autocheck_II(temperature):
    print(f"体温测量中...\n您的体温为：{temperature}度，", end="")
    if temperature > 37.5:
        print("需要隔离！")
    elif temperature > 27:
        print("体温正常，请进！")
    else:
        print("出错了，请重新测量！")


autocheck_II(35)
autocheck_II(37)
autocheck_II(39)
