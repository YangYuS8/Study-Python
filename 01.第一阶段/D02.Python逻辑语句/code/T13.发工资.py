import random

money = 10000
for x in range(1, 21):
    worker_mark = random.randint(1, 10)
    if worker_mark < 5:
        print(f"{x}号员工，绩效分为{worker_mark}，低于5，不发工资，下一位")
        continue
    elif money == 0:
        print("工资发完了，下个月再领取吧")
        break
    else:
        money -= 1000
        print(f"{x}号员工，发放工资1000元，账户余额剩余{money}元")
