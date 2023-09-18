# 1.布尔类型演示及比较运算符的应用
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型是{type(bool_2)}")

# 比较运算符的使用
# == , != , > , < , >= , <=
# 比较运算符演示
num1 = 10
num2 = 10
num3 = 15
print(f"10 == 10的结果是：{num1 == num2}")
print(f"10 != 15的结果是：{num1 != num3}")
name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima的结果是：{name1 == name2}")
num4 = 5
print(f"10 > 5的结果是：{num1 > num4}")
print(f"10 < 5的结果是：{num1 < num4}")
print(f"10 >= 10的结果是：{num1 >= num2}")
print(f"10 <= 10的结果是：{num1 <= num2}")


# 2.判断语句if elif else演示
# age = 30
age = 16
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
elif age < 12:
    print("小学生担心过头了")
else:
    print("我还未成年")
    print("救救孩子")
print("时间过得真快啊")

# 3.判断语句的嵌套
# 参考C++的判断语句嵌套
