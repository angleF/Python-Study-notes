# help(open)
# 打开文件，内置函数
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# open函数默认以全量读取文本文件,返回类型：_io.TextIOWrapper
# 参数：
# file：文件路径
# mode：打开文件的模式
# buffering：设置缓冲策略，0:关闭缓存（仅在二进制模式下有效）,1:选择行缓冲（仅在文本模式下可用）
# encoding ：编码
# errors：errors是一个可选字符串，用于指定如何处理编码错误

# 手动开启关闭文件
# text_io = open("file/dome.txt", encoding="utf-8")
# print(text_io)
# print(text_io.read())
# text_io.close()

# 借助finally语句关闭io
# text_io2 = None
# try:
#     text_io2 = open("file/dome.txt", encoding="utf-8")
#     print(text_io2.read())
# # except Exception as ex:
# #     print("操作文件异常...", ex)
# finally:
#     text_io2.close()

# 使用with ... as .. 语法将在代码块执行完后自动关闭
# with open("file/dome.txt", encoding="utf-8") as text_io1:
#     print(text_io1.read())
#
# file_name = 'hello'
#
# try:
#     with open(file_name) as file_obj:
#         print(file_obj.read())
# except FileNotFoundError:
#     print(f'{file_name} 文件不存在~~')

# _io.TextIOWrapper.read函数 限制每次读取大小，文本模式下为字符大小，二进制模式下为字节大小
# try:
#     with open("file/dome.txt", encoding="utf-8") as dome_io:
#         read = dome_io.read(100)
#         print(read)
#         print("字符长度:", len(read))
# except IOError as ex:
#     print("文件操作异常：", ex)

# readlines()
# 该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回
# with open("file/dome.txt" , encoding='utf-8') as file_obj:
#     readlines = file_obj.readlines()
#     print(readlines)

# 读取大文件是为避免read函数全量读取导致内存溢出，限制每次读取一部分处理后继续读取
# try:
#     with open("file/dome.txt", encoding="utf-8") as dome_io:
#         read=None
#         while True :
#             read = dome_io.read(100)
#             if not read:
#                 break;
#             print(read, "\t\t字符长度:", len(read))
#
# except IOError as ex:
#     print("文件操作异常：", ex)

# 写入文本文件
# try:
#     with open("file/dome_write1.txt", "r+", encoding="utf-8") as dome_write1_io:
#         # 文件存在则覆盖文件中内容，不存在则创建
#         dome_write1_io.write("创建了一个新的文本文件")
#         print(dome_write1_io.read())
#         dome_write1_io.write("创建了一个新的文本文件")
# except IOError as ex:
#     print("操作文件异常：", ex)

# try:
#     with open("file/dome_write2.txt", "a+", encoding="utf-8") as dome_write2_io:
#         # 文件存在则追加文件中内容，不存在则创建
#         dome_write2_io.write("创建了一个新的文本文件")
#         print(dome_write2_io.read())
#         # dome_write1_io.write("创建了一个新的文本文件")
# except IOError as ex:
#     print("操作文件异常：", ex)

# 二进制文件
# try:
#     with open("file/截图.jpg", "rb") as b_read:
#         print(b_read.read(100))
# except IOError as e:
#     print("异常：", e)

# 文件拷贝
# try:
#     with open("file/截图.jpg", "rb") as b_read:
#         with open("file/截图1.jpg", "wb") as w_read:
#             while True:
#                 b_read_ = b_read.read(2048)
#                 if not b_read_:
#                     break
#                 w_read.write(b_read_)
# except IOError as e:
#     print("异常：", e)

# seek() 可以修改当前读取的位置
# seek()需要两个参数
#   第一个 是要切换到的位置
#   第二个 计算位置方式
#       可选值：
#           0 从头计算，默认值
#           1 从当前位置计算
#           2 从最后位置开始计算
with open("file/dome.txt", encoding="utf-8") as text_io1:
    print(text_io1.seek(200, 0))
    print(text_io1.read(100))
# seek() 可以修改当前读取的位置
# seek()需要两个参数
#   第一个 是要切换到的位置
#   第二个 计算位置方式
#       可选值：
#           0 从头计算，默认值
#           1 从当前位置计算
#           2 从最后位置开始计算


import os
from pprint import pprint

# os.listdir() 获取指定目录的目录结构
# 需要一个路径作为参数，会获取到该路径下的目录结构，默认路径为 . 当前目录
# 该方法会返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素
r = os.listdir()

# os.getcwd() 获取当前所在的目录
r = os.getcwd()

# os.chdir() 切换当前所在的目录 作用相当于 cd
# os.chdir('c:/')

# r = os.getcwd()

# 创建目录
# os.mkdir("aaa") # 在当前目录下创建一个名字为 aaa 的目录

# 删除目录
# os.rmdir('abc')

# open('aa.txt','w')
# 删除文件
# os.remove('aa.txt')

# os.rename('旧名字','新名字') 可以对一个文件进行重命名，也可以用来移动一个文件
# os.rename('aa.txt','bb.txt')
os.rename('bb.txt', 'file/bb.txt')

pprint(r)
