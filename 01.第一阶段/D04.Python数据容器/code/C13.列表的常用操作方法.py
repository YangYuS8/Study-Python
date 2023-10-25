# 数据容器演示：list列表的常用操作
mylist = ["itcast", "itheima", "python"]

# 1.1查找某元素的下标索引
index = mylist.index("itheima")
print(f"itheima的下标索引是{index}")
# 1.2如果查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"hello的下标索引是{index}")

# 2.修改特定下标索引的元素
mylist[0] = "传智教育"
print(f"修改后的列表是{mylist}")

# 3.在指定下标索引位置插入新元素
mylist.insert(1, "best")
print(f"插入后的列表是{mylist}")

# 4.在列表末尾追加"单个"新元素
mylist.append("黑马程序员")
print(f"追加后的列表是{mylist}")

# 5.在列表末尾追加"多个"新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"追加后的列表是{mylist}")

# 6.删除指定下标索引的元素
mylist = ["itcast", "itheima", "python"]
# 6.1方法1：使用del关键字
del mylist[2]
print(f"del删除后的列表是{mylist}")
# 6.2方法2：使用pop()方法
mylist = ["itcast", "itheima", "python"]
element = mylist.pop(2)
print(f"pop删除后的列表是{mylist}，被删除的元素是{element}")
# 6.3方法3：使用remove()方法
mylist = ["itcast", "itheima", "python"]
mylist.remove("python")
print(f"remove删除后的列表是{mylist}")
