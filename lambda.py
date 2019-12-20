def get_funcs():
    temp = [lambda x : i*x for i in range(4)]
    #lambda 表达式每次都返回 i*x， 而不是 0*x, 1*x等将i计算后的结果。全部返回后才计算。
    # temp 为保存了函数对象的列表， []里为列表推导式
    return temp


def lengthOfx(x):
    print('The length of {0} is {1}'.format(repr(x), len(x)))

if(__name__ == '__main__'):
    for func in get_funcs():
        print(func(2))

    lengthOfx('123')
    lengthOfx([1, 2, 3, 4, 5])
