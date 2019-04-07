"""


"""
import re


def replace():
    file_obj = open("str.log", "r", encoding="utf-8")

    # 替换yyyy-MM-dd为yyyy-MM-dd
    # ?P<year> 表示为该组起别名，使用 \g<year> 引用
    sub = re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "\g<year>/\g<month>/\g<day>", file_obj.read())
    print(sub)


def join():
    # join相较于使用+符号直接连接的方式在性能和空间上都有优势
    print(''.join(["A", 's', 's', 'sd', 'f', 'd', 'g', 'h']))

    str_ = [1, 2, 4, 0.4, 'q', 'w', 'e']
    print(''.join((str(x) for x in str_)))


if __name__ == "__main__":
    join()
