# 继承是面向对象三大特性之一
# 通过继承，子类可以使用父类的属性及方法
# Pyton中支持多继承

# 单继承
class Animal:

    def __init__(self, sound, age, name, gender):
        print("父类......")
        self._sound = sound
        self._age = age
        self._name = name
        self._gender = gender

    def run(self):
        print("动物跑......")

    def sleep(self):
        print("动物睡觉.....")


class Dog(Animal):

    def __init__(self, sound, age, name, gender, str):
        print("子类......")
        #  调用父类初始化方法
        # 父类初始化方法不会像java构造器一样自动调用
        super().__init__(sound, age, name, gender)
        self._str = str

    def kan_men(self):
        print("狗看门......")

    # 重写父类方法
    def run(self):
        print("狗跑.......")


dog = Dog("汪汪汪", 2, "小黑", '雄', "sssss")
dog.sleep()
dog.kan_men()
dog.run()


# 多继承
class A:

    def run(self):
        print("A.run()......")


class B(A):

    # def run(self):
    #     print("B.run()......")

    def sleep(self):
        print("B.sleep().......")


class C:

    def run(self):
        print("C.run()......")

    def jiao(self):
        print("C.jiao()......")


class D(B, C):
    pass


d = D()

d.run()
d.jiao()

"""
多继承时，执行顺序为 先在当前类中查找是否有该方法，没有则在
第一个继承的父类中查找，没有再找第一个父类的父类...一直往上查找，
直到object类，若是还没找到就找第二个父类，再没有就找其父类
(这里有一个流程就是若是哪个类已经查找过，则会跳过)

执行run方法，D->B->A
执行jiao方法，D->B->A->object,->C

"""