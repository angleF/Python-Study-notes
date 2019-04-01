# 占位符 %s:表示任意字符串 %f:表示浮点数  %d:整数占位符
a = 'hello %s' % '那个谁'
# 多个占位符
b = 'hello %s , 还有 %s' % ('张三', "李四")
# 限制最小字符长度为3
c = 'hello %3s' % 'ss'
# 限制最小字符长度为1 最大最大字符长度为3   使用英文.分隔
d = 'hello %1.3s' % "Wrole"
# 保留两位小数
e = 'hello %1.2f' % 123.456
print(a)
print(b)
print(c)
print(d)
print(e)

# 格式化字符串，可以通过在字符串前添加一个f来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
z = '张三'
s = '李四'
c = f"hello {z} {s}"
print(c)

# 字符串复制（将字符串与数字相乘）
# 字符串乘以几表示复制几次（包括本身）
old = "abd,"
copy_str = old * 9
print(copy_str)

# Python中布尔值（bool）为大写开头True/False
# None 相当于java中的null

# 检查获取值类型 type()

print(type(123))  # <class 'int'>
print(type(123.21))  # <class 'float'>
print(type("123"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
print(type(type(None)))

# 类型转换
# int()、float()、str()、bool()
a = None
print(bool(a))

# 算术运算符
# + 加
# - 减
# * 乘
# ** 求幂次方
# / 除
# // 整除
# % 取模
f = 11 % 2
print(f)
print(16 ** 0.5)

# 关系运算
# > 大于
# >= 大于等于
# <= 小于等于
# < 小于
# == 是否相等，比较的是对象的值
# != 是否不相等，比较的是对象的值
# is 是不是一个对象，比较的是对象的地址
# is not 是否不是一个对象，比较的是对象的地址
print('32' > '2')  # （>、>=、<、<=比较的是字符串时 比较的是从左开始逐个字符的Unicode编码索引  多个字符比较就相当于使用 or）

# 逻辑运算
# not 非 ,可以对右侧的值进行非运算，
# 			对于布尔值，非运算会对其进行取反操作，True变False,False变True
# 			对于非布尔值,非运算会现将其转换为布尔值，然后再取反
# and 与
#       在程序设计中，and称为逻辑与运算，也称布尔运算；
#        1.and是在布尔上下文中从左到右计算表达式的值；
#        2.0、''、[]、()、{}、None、False在布尔上下文中为假；其它任何东西都为真；
#        3.如果布尔上下文中的某个值为假，则返回第一个假值；
#        4.所有值都为真，则返回最后一个真值。
# or 或

print("None转bool：", bool(None))
print("空字符转bool：", bool(None))

print(4 and 3, "=4 and 3")
result = 1 < 2 < 3  # 相当于 1<2 and 2<3

# 三元运算
# 语法： 语句1  if 条件表达式  else 语句2
print("周末") if True else print("工作日")
# 多重三元运算
print("周末") if False else (print("周末1") if True else print("工作日"))

