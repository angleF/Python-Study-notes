# 封装是面向对象三大特性之一
# 封装是为了隐藏对象中一些不希望被外部所访问的属性和方法
# 为属性提供setter和getter方法

# 可以为对象的属性使用双下划线开头，__xxx
# 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问
# 其实隐藏属性只不过是Python自动为属性改了一个名字
#   实际上是将名字修改为了，_类名__属性名 比如 __name -> _Person__name
# class Person:
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self , name):
#         self.__name = name

# 使用Python的property装饰器
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 对外将getter方法定义和属性名一致
    # 并且加上 @property
    @property
    def name(self):
        print("name的getter方法执行了.....")
        return self._name

    @name.setter
    def name(self, name):
        print("name的setter方法执行了.....")
        self._name = name

    @property
    def age(self):
        print("age的getter方法执行了.....")
        return self._age

    @age.setter
    def age(self, age):
        print("age的setter方法执行了.....")
        self._age = age


# 调用属性装饰后getter方法
person = Person("张三",18)
print(person.name)
person.name = '李四'
print(person.name)

print(person.age)
person.age = 29
print(person.age)
