"""
某软件要求，从网络抓取各个城市气温信息，并依次显示：
北京：25~20
天津：17~22
长春：12~18
...
如果依次抓取所有城市田七在显示，显示第一个城市气温时，有很高的延时，
并且浪费存储空间。我们期望以‘用时访问’的策略，并且能把所有城市气温封装到一个对象里，
可用for语句进行迭代，如何解决？

解决方案：
1、实现一个迭代器对象WeatherIterator,next方法每次返回一个城市气温
2、实现一个可迭代对象WeatherIterable,__iter__方法返回一个迭代器对象
"""

import requests
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    """
        自定义迭代器
    """

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return WeatherIterator.get_weather(city)

    @staticmethod
    def get_weather(city):
        response = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=%s" % city)
        data = response.json()["data"]["forecast"][0]
        return "%s: %s , %s" % (city, data["low"], data["high"])


class WeatherIterable:

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        """
            实现自定义迭代器
        :return:  返回一个可迭代的自定义迭代器
        """
        return WeatherIterator(self.cities)


for i in WeatherIterable(["上海", "长沙", "邵阳"]):
    print(i)
