# 1.三种定义方式
# 单引号定义法
name = "黑马程序员"
print(type(name))
# 双引号定义法
name = "黑马程序员"
print(type(name))
# 三引号定义法，与多行注释相同
name = """
黑马
程序
员
"""
print(type(name))

# 2.字符串的引号嵌套
# 在字符串内包含双引号
name = '"黑马程序员"'
print(name)
# 在字符串内包含单引号
name = "'黑马程序员'"
print(name)
# 使用转义字符 \ 解除引号的效用
name = '"黑马程序员"'
print(name)
name = "'黑马程序员'"
print(name)

# 3.字符串拼接
# 字面量之间的拼接
print("学IT来黑马" + "月薪过万")
# 字面量与变量之间的拼接
name = "黑马程序员"
address = "建材城东路9号院"
tel = 4006189090
# print("我是：" + name + "我的地址是：" + address + "我的电话是：" + tel)

# 4.字符串格式化
# 通过占位的方式，完成拼接
name = "黑马程序员"
message = "学IT来：%s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s元" % (class_num, avg_salary)
print(message)

# 5.字符串的精度控制
num1 = 11
num2 = 11.415
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.415宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.415宽度不限制，小数精度2，结果是：%.2f" % num2)

# 6.快速格式化
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
# f:format
print(f"我是{name}，我成立于{set_up_year}年，我今天的股价是：{stock_price}")

# 7.表达式的格式化
print("1 * 1的结果为：%d" % (1 * 1))
print(f"1 * 2的结果为：{1 * 2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))
