"""
实现一个可迭代对象的类，他能迭代出给定范围内的所有素数
 输入1,30
 输出：2,3,5,7,11,13,17,19,23,29

解决方案：
将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
"""


class PrimeNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime_num(self, k):
        if k < 2:
            return False

        for i in range(2, k):
            if k % i == 0:
                return False
            return True

    def __iter__(self):
        print("-" * 30)
        for j in range(self.start, self.end + 1):
            if self.is_prime_num(j):
                yield j


for x in PrimeNumbers(1, 10):
    print("*" * 30)
    print(x)
