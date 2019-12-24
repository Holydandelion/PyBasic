

# iterate a dict
D1 = {'name':'John', 'number':'001', 'job':'unkown'}
for item in D1.items():
    print(item)

# iterate a list
L1 = ['a', 'bbb', 'ccc']
for item in enumerate(L1):
    print(item)

# reverse iterate a sequence
L2 = [1, 2, 3, 4, 5]
for i in reversed(L2):
    print(i)

print(L2)   # L2 is not changed.

#  iterate a soreted sequence copy
L3 = [6, 2, 1, 3, 4, 5]
for i in sorted(L3, reverse=True):
    print(i)

print(L3)   # L3 is not changed.