# 输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析 特殊情况，闰年时需考虑二月多加一天：
def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


dofM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
res = 0
year = int(input("year:"))
month = int(input("Month:"))
day = int(input("day:"))
if is_leap_year(year):
    dofM[2] += 1
for i in range(month):
    res += dofM[i]
print(res + day)
