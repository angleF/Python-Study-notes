# 闭包就是能够读取其他函数内部变量的函数

# 形成闭包的条件
#   1、函数嵌套
#   2、将内部函数作为返回值返回
#   3、内部函数必须要使用到外部函数的变量

def make_averager():
    # 创建一个列表，用来保存数值
    nums = []

    # 创建一个内部函数,用于计算平均值
    def averager(n):
        # 将n添加到列表中
        nums.append(n)
        print(nums)
        # 求平均值
        return sum(nums) / len(nums)

    return averager;


# 调用外部函数
averager = make_averager()

print(averager(10))  # 10.0
print(averager(20))  # 15.0
print(averager(30))  # 20.0
print(averager(40))  # 25.0
print(averager(50))  # 30.0


# 使用 nonlocal 声明变量为父函数变量
def fn():
    a = 10

    def fn1(x):
        nonlocal a
        a = 20

        def fn2():
            nonlocal a
            a = 30
            return a * x

        return fn2()

    return fn1


f = fn()
print(f(20))
print(f(20))
