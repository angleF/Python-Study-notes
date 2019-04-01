# 输入三个整数x,y,z，请把这三个数由小到大输出。

# 冒泡
raw = []
for i in range(3):
    x = int(input("int%d:" % i))
    raw.append(x)
for i in range(len(raw)):
    for j in range(i, len(raw)-1):
        if raw[j] > raw[j + 1]:
            raw[j + 1], raw[j] = raw[j], raw[j + 1]
print(raw)

# 调用内置函数
raw = []
for i in range(3):
    x = int(input("int%d:" % i))
    raw.append(x)

print(sorted(raw))
