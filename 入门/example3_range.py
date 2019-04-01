# range()是一个函数，可用用来生成一个自然数的序列
r = range(5)  # 生成一个0-5的序列
r = range(0, 10, 2)  #
# 该函数需要三个参数
#   1.起始位置（可以省略）缺省为0
# 	2、结束位置
# 	3.步长（可以省略）缺省为1
# print(list(r))

# print(r)

# for i in r :
# 	print(i)

# 获取1-100相加的和
sum_ = 0
for i in range(101):
    print(i, end=" , ")
    sum_ += i
print(f"1-100的和：{sum_}")
