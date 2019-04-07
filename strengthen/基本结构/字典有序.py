"""
如何让字典保存有序

方案：
使用collections.OrderedDict代替内置Dict,依次将选手成绩存入OrderedDict

"""
from collections import OrderedDict

# 根据key添加的顺序排序

ordered_dict = OrderedDict()
ordered_dict["B"] = "b"
ordered_dict["A"] = "a"
ordered_dict["Q"] = "q"
ordered_dict["D"] = "d"
ordered_dict["X"] = "x"

for k in ordered_dict.keys():
    print(k)
