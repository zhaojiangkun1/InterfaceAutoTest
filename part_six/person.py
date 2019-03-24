
class Person():
    def __init__(self, name):
        print("构造函数运行")


    def __call__(self, *args, **kwargs):
        print("call方法运行")

    # 挂羊头卖狗肉
    def __new__(cls, *args, **kwargs):
        print("new方法运行")
        return object.__new__(Person)
        # return Dog()

    def __del__(self):
        print("析构函数 del方法运行")

class Dog():
    def run(self):
        print("dog run")


Person(1)(2)
# p = Person()
# p(1)
# print(type(p))
# p.run()
