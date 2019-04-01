# 类由属性和方法构成
# 类的基本结构
"""
class 类名([父类]):

    公共的属性....

    对象的初始化方法，类似于java中的构造函数
    def __init__(self,...):
        psss

    自定义函数
    def method_1(self,...):
        pass

    def method_2(self,...):
        pass

"""


# 类中方法的都必须至少定义一个参数,第一个参数为执行当前方法的实例对象，由python解释器传入
# 在方法中不可以直接使用类中的公共属性，需要通过实例对象调用
# 类中可以定义一些特殊方法，这些特殊方式不需要我们直接调用，python的某些函数或者操作符会进行调用
# 特殊方法名都是以两个下划线开始然后两个下划线结束，比如：__init__、__str__

class Dog:

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def call(self, str_):
        print("这只狗名字：%s,年龄：%f ,性别：%s ,身高：%f" % (self.name, self.age, self.gender, self.height))
        print(str_)


dog = Dog("小黑", 1, '雄', 40)
dog.call("叫唤......")

help(Dog)
