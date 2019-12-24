class Complex:
    def __init__(myself, realpart, imagpart):
        myself.r = realpart
        myself.i = imagpart

    def f(self):
        print("hello world")

x = Complex(3.0, -4.5)

# assignment introduces a new attibute without declaration
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

print('x.f is :', x.f)
print('Complex.f is :', Complex.f)
x.f()