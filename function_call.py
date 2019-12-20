
def story(**kwd):
    return ('%(job)s called %(name)s' % kwd)

def power(x, y, *others):
    if others:
        print('received reduntant parameters:', others)
    return pow(x, y)

def interVal(start, stop=None, step = 1):
    if stop is None:
        start, stop = 0, start

    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step;

    return result

dict = {'job':'player', 'name':'Chen'}
tuple1 = ('one', 'two')

print(story(job = 'king', name = 'Chen'))
print(story(**dict))
print(power(2, 3, 'oh what'))
print(power(3, 2, *tuple1))
print(interVal(10))


