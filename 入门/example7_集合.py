# 集合中元素是唯一、无序、并且只能是不可变类型的
# 创建一个空集合
empty_set = set()
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}

# 交集运算
result_intersection = set_1 & set_2
print("交集：", result_intersection)  # {4, 5, 6}

# 并集运算
result_union = set_1 | set_2
print("并集：", result_union)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 差集运算
difference_set = set_1 - set_2
print("差集：", difference_set)  # {1, 2, 3}

# 异或集
xor_set = set_1 ^ set_2
print("异或集：", xor_set)  # {1, 2, 3, 7, 8, 9}

# <= 检查一个几个是否是另一个集合的子集
# 如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，而b集合时a集合的超集
a_set = {1, 2, 3}
b_set = {1, 2, 3, 5, 6}
print(a_set <= b_set)  # True

#  <检查一个集合是否是另一个集合的真子集
#  如果超集b中含有子集a中的所有元素，并且b中还有a中没有的元素，则b就是a的真超集，a是b的真子集（也可以理解为如果b是a的超集，并且同时b中的元素个数大于a的数量）
print({1, 2, 3} < {1, 2, 3, 5, 7})  # True
print({1, 2, 3} < {1, 2, 3})  # False

#  >、>=作用相反
