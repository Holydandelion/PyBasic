

def add_count(cls):
    print("cls:{0}".format(cls))
    cls._count += 1
    print("_count:{}".format(cls._count))  # reference class variable by cls.
    return "done"

class MyClass:
    _count = 0  # class variable
    foo = classmethod(add_count)

print("MyClass.foo: {0} \nMyClass.foo(): {1} \n".format(MyClass.foo, MyClass.foo()))

A = MyClass()
print("A.foo:{} \nA.foo():{}".format(A.foo, A.foo()))