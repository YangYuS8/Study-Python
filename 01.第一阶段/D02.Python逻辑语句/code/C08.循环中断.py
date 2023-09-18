# 演示continue
for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")

# continue嵌套
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

# 演示break
for i in range(1, 101):
    print("语句1")
    break
    print("语句2")
print("语句3")

# break嵌套
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        break
        print("语句3")
    print("语句4")
