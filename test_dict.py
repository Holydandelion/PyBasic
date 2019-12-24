
D1 = {'chenruogeng':10000, 'jiayi':8000, 'haowei': 20000}

for item in D1.items():
    print('{:s} is {:d}'.format(item[0], item[1]))

L = [('chenruogeng', 10000), ('jiayi', 8000), ('haowei', 20000)]
D2 = dict(L)

for item in D2.items():
    print('{:s} is {:d}'.format(item[0], item[1]))

L = [('chenruogeng', 10000), ('jiayi', 8000), ('haowei', 20000)]
D3 = dict(chenruogeng=10000, jiayi=8000, haowei=20000)

for item in D3.items():
    print('{:s} is {:d}'.format(item[0], item[1]))


L = ('a', 'bb', 'ccc')

for item in enumerate(L):
    print(item)
