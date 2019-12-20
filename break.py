
for i in range(0, 10):
    print(i)
    if i == 8:
        break
else:
    print('not reach here.', end = ' ')


while True:
    s = input('enter something: \n')
    if s == 'quit':
        break

    print('length of s is :', len(s))

print('done')
