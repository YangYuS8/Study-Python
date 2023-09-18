# for的基础语法
name = "helloworld"
for x in name:
    print(x)

# range语法1 range(num)
for x in range(10):
    print(x)

# range语法2 range(num1, num2)
for x in range(5, 10):
    # 从5开始，到10结束(不包含10本身)的一个数字序列
    print(x)

# range语法3 range(num1, num2, step)
for x in range(5, 10, 2):
    # 从5开始，到10结束(不包含10本身)的一个数字序列，且数字之间的间隔为2
    print(x)

# for循环的变量作用域
i = 0
for i in range(5):
    print(i)
print(i)

# for嵌套：一个道理，不记录了
