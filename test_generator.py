
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

obj = reverse('abcdef')
print(obj)

print("next(obj):", next(obj))
print("next(obj):", next(obj))

for e in obj:
    print(e, end = ' ')
print()
# raise StopIteration
# print(next(obj))


def list_cube(size):
    """
    :param size:int, max size of cube
    :return: generator objcet, each iteraton return a list of cubes
    """

    result = [] # saved after each call
    for i in range(size+1):
        result.append(i**3)
        yield  result

for e in list_cube(10):
    print(e)


def fun(c):
    L = []
    L.append(c)
    yield L


obj = fun(1)
print(obj)
print(next(obj))
# print(next(obj))  raise StopIteration, because the function is finished.


def get_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = get_fibonacci()

for i in range(9):
    print(' next(f):', next(f))

