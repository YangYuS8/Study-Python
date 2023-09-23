# 1.演示嵌套调用函数
# 定义函数func_b
def func_b():
    print("---2---")


# 定义函数func_a,并在内部调用func_b
def func_a():
    print("---1---")
    # 嵌套调用func_b
    func_b()
    print("---3---")


# 调用函数func_a
func_a()


# 2.变量的作用域
# 演示局部变量
def test_a():
    num = 100
    print(f"test_a:{num}")


test_a()
# 演示全局变量
num = 200


def test_b():
    print(f"test_b:{num}")


def test_c():
    global num
    num = 300
    print(f"test_c:{num}")


test_b()
test_c()
print(num)
