class vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x};{self.y})"
    def __add__(self, other):
        return vektor(self.x + other.x, self.y + other.y)

v = vektor(3,1)
v1 = vektor(4, 1)
v2 = vektor(2, 6)
print(v+v1)