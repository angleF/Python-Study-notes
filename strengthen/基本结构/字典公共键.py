"""
如何找到多个字典中的公共键

西班牙足球甲级联赛，每轮球员进球统计：
    1.{'苏亚雷斯':1,'梅西':2,'本泽马':1,'C罗':3}
    1.{'苏亚雷斯':2,'C罗':1,'格里兹曼':2,'贝尔':3}
    1.{'苏亚雷斯':1,'托雷斯':2,'贝尔':1,'内马尔':1}

统计出前N轮，每场比赛都有进球的球员
"""
from random import randint, sample
from functools import reduce

# 随机生成数据
s1 = {x: randint(1, 4) for x in sample('qazmlptgb', randint(4, 6))}
s2 = {x: randint(1, 4) for x in sample('qazmlptgb', randint(4, 6))}
s3 = {x: randint(1, 4) for x in sample('qazmlptgb', randint(4, 6))}

print(s1)
print(s2)
print(s3)
# 方案1 使用循环遍历判断

# 方案2：使用集合获取交集
print(set(s1.keys()) & set(s2.keys()) & set(s3.keys()))

print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))
