# 1.函数的定义
# 定义一个函数，输出相关信息
def say_hi():
    print("Hi")


# 调用函数
say_hi()


# 2.函数的传入参数
# 定义两数相加的函数，通过参数接收2个数字
def add(x, y):
    print(f"{x}+{y}={x+y}")


add(1, 2)


# 3.函数的返回值
def add2(a, b):
    result = a + b
    return result


r = add2(5, 6)
print(r)
# 返回空类型
result2 = say_hi()
print(f"无返回值函数返回的内容是:{result2}")
print(f"无返回值函数返回的内容类型是:{type(result2)}")


# 主动返回None的函数
def say_hi2():
    print("Hi")
    return None


result2 = say_hi2
print(f"无返回值,返回的内容为:{result2}")
print(f"无返回值,返回的内容类型为:{type(result2)}")


# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None


result2 = check_age(16)
if not result2:
    # 进入if表示result2是None,也就是False
    print("未成年,不可以进入")

# None用于声明无初始内容的变量
name = None
