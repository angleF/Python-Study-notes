# Python捕获异常语法
"""
    try:
        可能异常语句

    except 异常类 as ex:
        异常处理
    finally:

"""


# 捕获异常满足多个 except块时，优先先定义的
# try:
#     print(10 / 0)
#
# except ZeroDivisionError as ex:
#     print("除0异常：", ex)
# except Exception as ex:
#     print("Exception：", ex)
# finally:
#     print("......")

class MyException(Exception):
    pass


# 手动抛出异常
def fn(a, b):
    if a == 0 or b == 0:
        raise MyException("自定义异常抛出")
    return a / b


print(fn(1, 0))
