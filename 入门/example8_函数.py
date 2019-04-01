# 给函数形参设置默认值，调用函数时该参数不传默认值就会生效
def fn(a=5, s=4):
    return a * s


print(fn())

# 函数的参数传递有两种方式，分别为位置传递和关键字传递
# 位置传递：顾名思义就是按照形参的顺序传入实参
# 关键字传递：在调用时指定参数名如：fn(s=22,a=10)
# 这两种方式可以混合使用，但是在使用时必须将位置传递写在前面
print(fn(s=22, a=10))


# 函数在调用时解析器不会检查实参的类型，实参可以传递任意类型对象


# 不定长参数
# *nums会将所有实参保存在一个元组中
# 带*符号的形参只能有一个
def my_sum(*nums):
    print(type(nums))  # <class 'tuple'>
    sum_ = 0
    for num in nums:
        sum_ += num

    return sum_


print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 第一个参数给a，第二个参数给b，剩下的都保存到c的元组中
def fn2(a, b, *c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


# 可变参数不是必须写在最后，但是注意，带*的参数后的所有参数，必须以关键字参数的形式传递
# 第一个参数给a，剩下的位置参数给b的元组，c必须使用关键字参数
def fn3(a, *b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


#  如果在形参的开头直接写一个*符号，则表示在调用时必须使用关键字方式传递参数
def fn4(*, a, c):
    return a * c


# print(fn4(1, 2)) # TypeError: fn4() takes 0 positional arguments but 2 were given
print(fn4(a=5, c=15))


# **形参表示接收所有其他的关键字参数，它将这些参数统一保存在一个字典里,该参数在调用时可以省略，但是传递时必须为关键字传递
# 字典的key就是参数名称，相应的value就是实参
# **形参只能有一个，并且必须写在所有参数的最后
def fn5(a, b, **my_dict):
    print("a=:", a, "\ttype:", type(a))
    print("b=:", b, "\ttype:", type(b))
    print("my_dict=:", my_dict, "\ttype:", type(my_dict))


fn5(123, "撒大声地", first="Fu", lastName="ZhaoLiang")


def fn6(**my_dict):
    print("-" * 20)
    print("my_dict=:", my_dict, "\ttype:", type(my_dict))


fn6()

print("*" * 60)


# 参数的解包（拆包）
def fn7(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


# 创建一个元组
t = (10, 20, 30)

# 传递实参时，也可以在序列类型的参数前添加星号，这样他会自动将序列中的元素依次作为参数传递
# 这里要求序列中元素的个数必须和形参的个数的一致
fn7(*t)

# 创建一个字典
d = {"a": "参数a", "b": "参数b", "c": "参数c"}
# 通过在实参前加上**符号对字典进行解包操作,该方式要求字典中的key名称和数量必须和函数形参一致
fn7(**d)


# 函数的文档描述

def fn8(a: int, b: int) -> int:  # 形参后面的：int表示该参数接收一个整型，参数括号后面的->int 表示返回一个整型  这些都只是对函数的描述，并不会起到校验作用
    """
     这里是对函数描述
     自定义格式
    :param a: ...
    :param b: ...
    :return: 返回值...
    """
    pass


# 使用 help(fn) 获取指定函数的文档
help(len)

all_a = 100


# 作用域
def fn9():
    #     在函数中操作修改变量默认都是局部变量
    # 如果希望在函数内部操作全局变量,需要使用 global 关键字，先声明变量
    global all_a
    all_a = 20
    print(all_a)


fn9()

# 命名空间(namespace)
# 命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间中
# 每一个作用域都会有一个对应的命名空间
# 全局命名空间,用来保存全局变量.函数命名空间用来保存函数中定义使用的变量
# 命名空间的结构就是一个字典，是一个专门用来存储变量的字典

# locals()用来获取当前作用域的命名空间
print(locals())


def fn10():
    # 在函数中使用locals()获取的是函数的命名空间
    # 使用globals()获取到全局的命名空间
    d = globals()
    print("全局命名空间：", d)
    print("当前函数命名空间：", locals())


fn10()


# 高阶函数
# 接收函数作为参数、或者将函数作为返回值的函数就是高阶函数
# 将一个函数作物参数时，实际上就是将指定的函数代码传递给了目标函数
def fn11(i):
    return i % 2 == 0


def fn12(i):
    return i % 2 != 0


def invoke_(func, lst):
    new_list = []
    for i in lst:
        if func(i):
            new_list.append(i)

    return new_list


print(invoke_(fn12, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# 匿名函数 lambda 函数表达式（语法糖）
# lambda 函数表达式用来创建一些简单地函数
# 语法： lambda 参数列表 ： 返回值

filer_result = filter(lambda i: i % 2 == 0, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 123})
print(list(filer_result))

# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数 ， key
#   key需要一个函数作为参数，当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l = ['bb','aaaa','c','ddddddddd','fff']
# l.sort(key=len)

l = [2,5,'1',3,'6','4']
l.sort(key=int)
# print(l)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意的序列进行排序
#   并且使用sorted()排序不会影响原来的对象，而是返回一个新对象

l = [2,5,'1',3,'6','4']
# l = "123765816742634781"

print('排序前:',l)
print(sorted(l,key=int))
print('排序后:',l)
