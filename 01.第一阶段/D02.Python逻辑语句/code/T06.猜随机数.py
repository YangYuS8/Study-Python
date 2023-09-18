import random

num = random.randint(1, 10)
guess_num = int(input("请输入你要猜测的数字："))
if guess_num == num:
    print("yes")
else:
    if guess_num > num:
        print("big")
    else:
        print("small")
    guess_num = int(input("请输入你要猜测的数字："))
    if guess_num == num:
        print("yes")
    else:
        if guess_num > num:
            print("big")
        else:
            print("small")
        guess_num = int(input("请输入你要猜测的数字："))
        if guess_num == num:
            print("yes")
        else:
            print(f"不好意思，全猜错啦~正确答案为：{num}")
