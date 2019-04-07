a = [1, 2, 3, 4, 5, 6, 7, 8]

# 列表推导
d = [i ** 2 for i in a]

# 集合推导
e = {i ** 2 for i in a}

# 元组推导
f = (i ** 2 for i in a)

print("列表:", type(d), "   ", d)
print("集合:", type(e), "   ", e)
print("元组:", type(f), "   ", list(f))
print()
# 使用条件
d = [i ** 2 for i in a if i > 3]
# 过滤掉小于3的
print("列表:", type(d), "   ", d)

print()
# 推导表达式中使用函数
a = [1, 2, 3, 4, 5, 6, 7, 8]


def conpute(x):
    if (x >= 6):
        return x ** 2
    return x ** 3


d = (conpute(i) for i in a)
x = []
for n in d:
    x.append(n)
print(x)
"""
输出：
列表: <class 'list'>     [1, 4, 9, 16, 25, 36, 49, 64]
集合: <class 'set'>     {64, 1, 4, 36, 9, 16, 49, 25}
生成器表达式: <class 'generator'>     [1, 4, 9, 16, 25, 36, 49, 64]

列表: <class 'list'>     [16, 25, 36, 49, 64]

[1, 8, 27, 64, 125, 36, 49, 64]
"""