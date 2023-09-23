# 演示对函数进行文档说明
# 定义函数并用文档说明
def add(x, y):
    """
    add函数可以接收2个参数,进行2数相加的功能
    Args:
        x (int): 表示相加的其中一个数字
        y (int): 表示相加的另一个数字

    Returns:
        int: 返回值是两数相加的结果
    """
    result = x + y
    print(f"两数相加的结果是:{result}")
    return result


add(5, 6)
