"""
历史记录

使用标准库collections中deque，它是一个双端循环队列
在程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入

"""
from collections import deque
from random import randint
import pickle
import os

num_rand = randint(0, 100)

history = deque([], 5)  # 队列最大长度


def guess(k):
    if k == num_rand:
        print("猜中了!!!")
        return True

    if k < num_rand:
        print("%s is less-than N" % k)
    else:
        print("%s is greater-than N" % k)
    return False


flag = True
while True:
    line = input("请输入一个数字：")
    if flag and os.path.exists("history"):
        load_history = pickle.load(open('history', "rb"))
        if load_history:
            history = load_history
            flag = False
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'h?':
        print(list(history))
    elif line == 'exit':
        pickle.dump(history, open('history', "wb"))
        print("程序退出中.....")
        break
    else:
        print("'%s' 不是一个数字" % line)
