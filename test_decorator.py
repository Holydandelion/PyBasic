

class MyClass:
    _count = 0  # class variable

    @classmethod
    def add_count(cls):
        print("cls:{0}".format(cls))
        cls._count += 1
        print("_count:{}".format(cls._count))  # reference class variable by cls.
        return "done"

print("MyClass.add_count: {0} \nMyClass.add_count(): {1} \n".format(MyClass.add_count, MyClass.add_count()))

A = MyClass()
print("A.add_count:{} \nA.add_count():{}".format(A.add_count, A.add_count()))