class vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x};{self.y})'

    def __add__(self, other):
        return vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vektor(self.x - other.x, self.y - other.y)

    def __abs__(self, other):
        return vektor()





v1 = vektor(3, 1)
v2 = vektor(4, -2)
v= v1 + v2
vm = v1-v2
vh
print(vm)