"""
实现一个连续浮点数发生器FloatRange(类似range),
根据你给定范围和步长值产生一个列连续浮点数。
如：迭代FloatRange(2.0,4.0,0.2)可产生序列：

正向：3.0 -> 3.2 -> 3.4 -> 3.6 -> 3.8 -> 4.0
反向：4.0 -> 3.8 -> 3.6 -> 3.4 -> 3.2 -> 3.0
"""


class FloatRange:

    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        """
        实现正向迭代器
        :return: 生成器
        """
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        """
        实现反向迭代
        :return: 生成器
        """
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


# 正向
for x in FloatRange(2.0, 4.0, 0.2):
    print(x)

print("—" * 20)
# 反向
for x in reversed(FloatRange(2.0, 4.0, 0.2)):
    print(x)
