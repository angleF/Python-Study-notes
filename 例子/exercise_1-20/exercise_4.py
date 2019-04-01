# 斐波那契数列。
#
# 程序分析 斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和

target = int(input())
my_ = [1, 1]
while True:
    end = len(my_) - 1
    end_sum = my_[end - 1] + my_[end]
    if end_sum > target:
        break
    my_.append(end_sum)


print(my_)

def fn():
    a = 10

    def fn1(x):
        nonlocal a
        a = a * x
        return a

    return fn1


f = fn()
print(f(20))
print(f(20))
