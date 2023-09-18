# 定义变量
num = 5
# 判断语句
if num == int(input("请输入第一次猜想的数字：")):
    print("恭喜，第一次就猜对了！")
elif num == int(input("不对，再猜一次：")):
    print("还不错，两次就猜对了")
elif num == int(input("不对，再猜最后一次：")):
    print("嚯哟！绝地反击？！居然猜对了！")
else:
    print(f"Sorry，全部猜错啦，我想的是：{num}")
