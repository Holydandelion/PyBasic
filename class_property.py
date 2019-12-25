

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size, fdel=None, doc="Rectangle's property")

#test code
r = Rectangle()
print(r.size)
r.size = (150, 100)
print(r.size)
print("r.size is:\n", r.size.__doc__)