# 定义一个类
class A(object):
    #       类属性
    #       实例属性
    #       类方法
    #       实例方法
    #       静态方法

    # 类属性
    #     类属性可以通过类或者实例访问
    #     但是类属性只能通过类对象来修改，无法使用实例对象修改
    count = 0

    def __init__(self, name):
        #         生成一个实例属性
        self._name = name

    # 实例方法
    # 在类中定义,以self为第一个传入的参数的方法都是实例方法
    # 实例方法在调用时，Python会自动传入调用对象为第一个实参
    # 实例方法可以通过类对象和实例对象调用，使用类对象调用时不会自动传入第一个self参数，需要手动传入
    def test(self):
        print("这是一个实例方法....")

    # 类方法
    # 在类中使用@classmethon修饰的方法
    # 类方法的第一个参数为cls，解释器会自动传入当前的类对象
    # 类方法也可以通过实例对象调用，cls参数也会自动传入
    @classmethod
    def cls_method(cls):
        print("这是一个类方法.....")

    # 静态方法
    # 在类中使用@staticmethod修饰的属于静态方法
    # 静态方法不需要指定必须的默认参数，可以使用类对象和实例对象调用
    @staticmethod
    def static_method():
        print("这是一个静态方法......")
