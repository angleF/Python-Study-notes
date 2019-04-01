# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析 遍历全部可能，把有重复的剃掉。
def fn():
    total = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (j != k) and (k != i):
                    print(i, j, k)
                    total += 1
    print(total)


def fn2():
    import itertools
    sum = 0
    a = [1, 2, 3, 4]
    # itertools.permutations 返回可迭代对象的所有数学全排列方式。
    for i in itertools.permutations(a, 3):
        print(i)
        sum += 1
    print(sum)




if __name__ == "__main__":
    fn2()
