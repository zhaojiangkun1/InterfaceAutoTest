"""
首先有一个类
"""
class Person():
    pass

print(Person)
p = Person
print(p)
p.name = "张三"
print(p.name)

def func(p):
    print(p.name)

func(p)

# 动态的创建一个类

def get_class(name):
    if name == "dog":
        class Dog():
            def run(self):
                print("dog run")
        return Dog   # 这里返回的是类，而不是类的实例
    else:
        class Cat():
            def run(self):
                print("cat run")
        return Cat

c = get_class("dog")
print(c)
c.run(c)
c = get_class("c")
print(c)
c.run(c)

# type
print(type(1))
print(type("aaa"))

# 使用type来动态的构造一个类
print(type(c))

Person2 = type('Person2', (), {})
print(Person2)
p2 = Person2()
print(p2)

# 增加属性
class Person3():
    name = "张三"


Person3 = type('Person3', (), {'name': '李四'})
print(Person3.name)

# 继承
Person4 = type('Person4', (Person3,), {})
print(Person4.name)


# 增加方法
def person4_run(self):
    print("person4 run")


Person4 = type('Person4', (Person3,), {'person4_run': person4_run})
p = Person4()
p.person4_run()

# 元类
# 类创造实例
# 元类是用来创造类的
# Person4 = type('Person4', (Person3), {'person4_run': person4_run})
# p = Person4()
# p.person4_run()

class MyMetaClass(type):

    def __new__(cls, name, bases, attrs):
        print("元类new方法运行")
        print(name)
        print(bases)
        attrs['add'] = lambda self, value: value + value
        print(attrs)
        # 下边这一行调用type方法来动态的构建类
        return type.__new__(cls, name, bases, attrs)

class MyClass(Person4, metaclass=MyMetaClass):
    # 上边的 metaclass=MyMetaClass 就指定了使用MyMetaClass来定制类
    # 就是通过type.__new__来创建的
    pass


my_class = MyClass()
r = my_class.add(2)
print(r)


