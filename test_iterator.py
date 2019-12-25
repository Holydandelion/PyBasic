

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)


    # can simply return the instance itself
    def __iter__(self):
        return self

    """
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
        
    """

obj = Reverse('abcded')
print("iter(obj) is:{0}".format(iter(obj)))

for element in obj:
    print(element)

s = 'abc'
it = iter(s)

print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # catch a StopIteration exception