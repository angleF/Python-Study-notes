sum = 0


def f(n):
    global sum
    sum+=1
    if n == 1: return 1
    return f(n - 1) + n


print(f(500))
print(sum)
