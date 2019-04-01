# 列表相当于Java中的数组 区别在于长度为可变并且不限制存储类型
# Python中列表可以保存任意对象，也就是说一个列表中可以保存数值、字符串、bool、浮点数、列表、函数以及自定义对象
my_list = [1, 2, 3.2, "hello", True, None, print];
print(my_list)

print(len(my_list))  # len()获取列表的长度
print(my_list[0])  # 获取列表首个元素
print(my_list[-1])  # 获取列表最后一个元素

# 切片 也就是截取出一个子列表
stus = ["张三", "李四", "王五", "赵六", "田七", "刘八", "麻子"]

print(stus[0:3])  # 截取列表前三个到新列表中，索引值包头不包尾
print(stus[:])  # 相当于全拷贝了一个新的列表
print(stus[:4:2])
print(stus[::-1])  # 从列表尾部开始截取  第三个参数为步长，表示获取上个元素后跳过（指定步长-1）个元素，步长默认为1，不能为0

list0_ = [1, 2, 3]
list1_ = [4, 5, 6]
list_ = list0_ + list1_  # 拼接列表
print(list_)
l = (list0_ + list1_) * 5  # 将拼接合并后的列表复制5遍（包括自身一遍）
print(l)

# in、not in 检查数组的元素
print("中" in stus)  # 检查指定元素在列表中是否存在
print("张三" not in stus)  # 指定元素在列表中是否不存在

print(max(l))  # 获取列表中最大的元素
print(min(l))  # 获取列表中最小的元素

print(stus.index("王五"))  # 获取指定元素在列表中的索引，当元素不存在时报错
print(l.count(1))  # 统计指定元素在列表中的个数

for s in stus:
    print(s)
