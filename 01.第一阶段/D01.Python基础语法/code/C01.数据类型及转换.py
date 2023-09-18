# 1.查询数据类型的方法：
# 方法1：使用print直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(114.514))

# 方法2：使用变量存储type()语句的结果
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(114.514)
print(string_type)
print(int_type)
print(float_type)

# 方法3：使用type()语句，查看变量中存储的数据类型信息
name = "黑马程序员"
name_type = type(name)
print(name_type)

# 2.转换数据类型的方法：
# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)
float_str = str(114.514)
print(type(float_str), float_str)

# 将字符串转换成数字
num = int("11")
print(type(num), num)
num2 = float("114.514")
print(type(num2), num2)

# 错误示例：想要将字符串转换成数字，必须要求字符串内的内容都是数字
# num3 = int("黑马程序员")
# print(type(num3), num3)

# 将整数转换成浮点数
float_num = float(11)
print(type(float_num), float_num)

# 将浮点数转换成整数
int_num = int(114.514)
print(type(int_num), int_num)

# 补充：取消print输出换行
print("Hello, ", end="")
print("World")

# 补充：制表符 \t
# 效果等同于在键盘上按下tab键
# 作用：使多行字符串对齐
print("Genshin\tImpact")
print("Star\tRail")
