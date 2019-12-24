
with open('testfile.txt', 'br+') as f:
    for line in f:
        print(line)

with open('testfile.txt', 'r+') as f:
    buf = f.read(5)
    print(buf)
    print(f.write('after end'))

f = open('testfile.txt', 'rb+')
f.write(b'0123456789')
f.seek(5)
print('index:{0:d}'.format(f.tell()))
buf = f.read(2)
print(buf)
f.flush()
f.close()
