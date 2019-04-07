"""
有个文本文件，我们想读取其中某个范围的内容，
如100-300行之间的内容，Python中文本文件是可迭代对象，
我们是否可以使用类似列表切片的方式得到一个100-300行的文件内容的生成器？
例如：
f = open("/var/log/dmesg)
f[100:300]

解决方案：
使用标准库中itertools.islice，返回一个迭代对象切片的生成器
"""
from itertools import islice


t = open("test.log")
lice_list = islice(t, 10, 20)
for x in lice_list:
    print(x)
