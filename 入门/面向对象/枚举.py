# 枚举为不可变对象
from enum import Enum


class Nums(Enum):
    First = 1
    Two = 2
    Three = 3
    Four = 4

    @classmethod
    def num_str(cls, num):
        key_map = {
            cls.First: {
                're': '我是1'
            },
            cls.Two: {
                're': '我是2'
            },
            cls.Three: {
                're': '我是3'
            },
            cls.Four: {
                're': '我是4'
            }
        }
        return key_map[num]['re']


# 获取到枚举类
print(Nums(1))
# 获取到对应的 num_str
print(Nums.num_str(Nums(1)))
# 通过枚举类可以获取到值，这个值就保存在数据库
print(Nums.First.value)
