
class MyClass:
    @staticmethod
    def func_s():
        print("call func_s()")

    def func(self):
        print("call func()")

print("MyClass.func_s is {0}".format(MyClass.func_s))
print("MyClass.func is {0}".format(MyClass.func))
print(MyClass.func_s())
print(MyClass.func("a"))

print()
obj_a = MyClass()
# use the same function object
print("obj_a.func_s is {0}".format(obj_a.func_s))

# have its own method object
print("obj_a.func is {0}".format(obj_a.func))


print()
obj_b = MyClass()
# use the same function object
print("obj_b.func is {0}".format(obj_b.func_s))

# have its own method object
print("obj_b.func is {0}".format(obj_b.func))
