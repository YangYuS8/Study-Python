import random

num = random.randint(1, 100)
time = 0
guess = int(input("猜一个1-100的随机数："))
while guess != num:
    if guess > num:
        print("不对，你猜的有点大了\n")
        time += 1
        guess = int(input("再猜一次试试："))
    else:
        print("不对，你猜的有点小了\n")
        time += 1
        guess = int(input("再猜一次试试："))
print("捏麻麻滴，终于猜中了")
print(f"狠人，你一共猜了{time}次！")
