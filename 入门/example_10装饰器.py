# python装饰器用于扩展函数功能的一种函数

# 不使用用装饰器
def fn(a, b):
    return a * b


# 一般情况low有点的就是直接更改函数源码
# 稍微好一点就是重新定义个函数，在这个新函数中添加需要扩展的代码然后在调用源函数

def ex_fn(a, b):
    print("fn函数执行前....")
    result = fn(a, b)
    print("fn函数执行后....")
    return result


#  使用该方式比之上一种就是不需要每次都重新定义一个函数，只需要调用该函数并传入所需参数就可
def decoration(func, *args, **ex_args):
    print("fn函数执行前....")
    result = func(*args, **ex_args)
    print("fn函数执行后....返回值：", result)
    return result


# decoration(fn, 10, 20)


# 使用装饰器
def decoration_invoke1(func):
    def inner(*args, **ex_args):
        print("fn函数执行前....decoration_invoke1")
        result = func(*args, **ex_args)
        print("fn函数执行后....decoration_invoke1，返回值：", result)
        return result

    return inner


def decoration_invoke2(func):
    def inner(*args, **ex_args):
        print("func函数执行前....decoration_invoke2")
        result = func(*args, **ex_args)
        print("func函数执行后....decoration_invoke2，返回值：", result)
        return result

    return inner


# 在定义函数是，可以通过 @装饰器函数名 来对函数进行装饰
# 可以为函数添加多个装饰器


# 执行顺序就相当于先调用decoration_invoke1然后在decoration_invoke1中调用decoration_invoke2
# 也就是说将fn函数作为参数传递给了decoration_invoke2，而将decoration_invoke2函数作为参数传递给了decoration_invoke1
# decoration_invoke1对decoration_invoke2进行了装饰/扩展，而decoration_invoke2对fn进行了装饰/扩展
@decoration_invoke1
@decoration_invoke2
def fn1(a, b):
    return a + b


fn1(10, 20)
