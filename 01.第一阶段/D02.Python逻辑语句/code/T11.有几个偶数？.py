num = 100
count = 0
for x in range(1, num):
    if x % 2 == 0:
        count += 1
print(f"1到{num}(不含{num}本身)的范围内有{count}个偶数")
