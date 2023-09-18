# 标准答案：
# print("欢迎来到支配剧场")
# height = int(input("请输入你的身高(cm)："))
# if height > 120:
#     print("您的身高超出120cm，游玩需要购票10元")
# else:
#     print("您的身高未超出120cm，可以免费游玩")
# print("祝您游玩愉快！")

# 加强版：
print("欢迎来到支配剧场")
if int(input("请输入你的身高(cm)：")) < 120:
    print("您的身高未超出120cm，可以免费游玩")
elif int(input("请输入你的VIP等级：")) > 3:
    print("您的VIP等级大于3，可以免费游玩")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，可以免费游玩")
else:
    print("不好意思，您未满足免费游玩的任一条件，需购票10元")
print("祝您游玩愉快！")
