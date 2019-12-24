age = 28
name = 'chen'

# use f tag
print(f'programer: {name:}')

# use format method location parameter
print('{0} is {1} years when he begin to learn python'.format(name, age))


# use format method key word parameter
print("programer:{name}".format(name='chen'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))