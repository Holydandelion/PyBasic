
def print_max(x, y):
    '''Print the max number of tow numbers

    The tow numbers must be integer'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x)
    else:
        print(y)

print_max(3.1, 5.4)
#print(print_max.__doc__)
help(print_max)