# input语句演示
name = input("请告诉我你是谁？")
print("我知道了，你是%s" % name)

# 输入数字类型
num = input("请告诉我你的银行卡密码：")
# 数据类型转换
num = int(num)
print("你的银行卡密码的类型是：", type(num))
