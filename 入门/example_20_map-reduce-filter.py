print("-" * 20, "map", "-" * 20)
# map函数 类似于java8中Stream流的map方法
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 示例1、 使用map函数将列表中的字符串类型的数值全都转换为数字（int）类型
# map函数返回一个map对象（实际map就是一个内置Class）
int_list = map(int, num_list)
print(list(int_list))

# 示例2、
# 将列表中的字符串首字符转为大写字符
name_list = ["zhagsan", "lisi", "wangwu", "zhaoliu", "tianqi", "liuba"]


def first_up(name):
    return str.title(name)


# 使用自定义函数
name_up_customize = map(first_up, name_list)
print(list(name_up_customize))
# 使用lambda
name_up_lambda = map(lambda n: str.title(n), name_list)
print(list(name_up_lambda))

print("-" * 20, "reduce", "-" * 20)
# 使用reduce函数对一个数字列表进行求和
# 使用reduce需要引入functools包
from functools import reduce

num_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# reduce返回执行后的总结果
# 该执行流程为 ((((((1+2)+3)+4)+5)+6)+7)+8)+9,不指定初始值时x=1,y=2,第二次执行时x=1+2,y=3......
sum_list = reduce(lambda x, y: x + y, num_int_list)
print(sum_list)
# 指定初始值,区别于上面，第一次x=100,y=1,第二次x=101,y=2......
sum_list = reduce(lambda x, y: x + y, num_int_list, 100)
print(sum_list)

print("-" * 20, "filter", "-" * 20)
# filter用于过滤,返回一个迭代器
my_list = [1, 3, 4, "5", "3", "22"]
# 过滤所有字符串
ints_ = filter(lambda x: isinstance(x, int), my_list)
print(ints_)  # <filter object at 0x000001530A004128>
print(list(ints_))
