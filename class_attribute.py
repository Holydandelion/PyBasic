
class TestClass:
    # class attributes, the variable exists in the class's namespace
    # for an object, such as a list, each instance and the class  copy the reference.
    # for an number, each instance and the class  copy the value.

    L = [123]
    i = 0
    def __init__(self, arg1: int):
        # instance attributes, exists in the instance's namespace
        self.j = arg1
        self.data  = []

        # local varible, exists in the function's namespace
        # can not be referenced by a instance
        k = arg1

obj1 = TestClass(1)
obj1.i = 111
obj1.L[0] = 456
obj2 = TestClass(2)
obj2.L[0] = 789
obj2.i = 222

print("obj1.L:{0}, obj1.i:{1:d}, obj1.j:{1:d}".format(obj1.L, obj1.i, obj1.j))
print("obj2.L:{0}, obj2.i:{1:d}, obj2.j:{1:d}".format(obj2.L, obj2.i, obj2.j))
print("TestClass.L:{0} TestClass.i:{1}".format(TestClass.L, TestClass.i))