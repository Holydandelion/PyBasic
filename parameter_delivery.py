
def acc(i: int)-> int:
    i += 100
    return i


def change_obj(obj):
    obj[0] = 0


# for number, deliver value of parameter
i = 1
print(acc(i))
print(i)

# for list and other object type, deliver reference of parameter
L1 = [1, 2]
change_obj(L1)
print(L1)

""" Error: tuple is immutable
A1 = (1, 2)
change_obj(A1)
print(A1)
"""