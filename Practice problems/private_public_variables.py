class Public(object):
    def __init__(self, a, b):
        self._a = a
        self.__b = b
    
    def __repr__(self):
        return (str(self._a) + " " + str(self.__b))

p = Public(10,20)
print(p)
print(p._a)
print(p._Public__b)
