"""
1、某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，
同时迭代三个列表，计算每个学生的总分（并行）

2、某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，
一次迭代每个列表，统计全学年成绩高与90分的总分（串行）

解决方案：
1.并行：使用内置函数zip,将多个可迭代对象合并，每次迭代返回一个元组
2.串行：使用标准库中的itertools.chain，将多个可迭代对象连接
"""
from random import randint
from itertools import chain

range_A = [randint(20, 100) for i in range(40)]
range_B = [randint(20, 100) for i in range(40)]
range_C = [randint(20, 100) for i in range(40)]
range_D = [randint(20, 100) for i in range(40)]

# 1.并行
total = []
for stu_a, stu_b, stu_c in zip(range_A, range_B, range_C):
    total.append((stu_a+stu_b+stu_c))

print("总和：", total)

# 2.串行
x_list = [x for x in chain(range_A, range_B, range_C, range_D) if x > 90]
print(x_list)
print(sum(x_list))

