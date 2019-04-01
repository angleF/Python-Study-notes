# 元组是一个不可变的序列
# 它和列表的操作方式基本一致
# 创建元组使用()
my_tuple = ()  # 创建了一个空元组
print(my_tuple, ",", type(my_tuple))  # <class 'tuple'>

# 当元组不是一个空元组是，括号可以省略
# 如果元组不是空元组，它需要包含至少一个元素
my_tuple = 1, 2, 3, 4, 5, 6, 7  # 定义一个包含多个元素的元组
# print(my_tuple)
# my_tuple = 40,  # 定义一个只包含一个元素的元组
# print(my_tuple)

# 序列的解包（解构）
# 将序列中的元素依次按顺序赋值给a,d,f等三个元素，f前带*表示将序列中除前两个以外的所有元素组成一个列表赋值给f
a, d, *f = my_tuple
print("a:", a)
print("d:", d)
print("f:", f)

q = 100
w = 200
# 通过解包来将q、w 两个变量的值进行交换，而不需要一个临时变量接收
q, w = w, q
print("q:", q, ",w:", w)

my_list = [11, 22, 33, 44, 55, 66, 77]
z, *x, c = my_list
print("z:", z, ",x:", x, ",c:", c)
