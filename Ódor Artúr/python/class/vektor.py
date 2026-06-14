import math
class vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f"({self.x};{self.y})"
    

    def __add__(self, other):
        return vektor(self.x + other.x, self.y + other.y)
    

    def __sub__(self, other):
        return vektor(self.x - other.x, self.y - other.y)
    

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vektor(self.x * other, self.y * other)
        elif isinstance(other,(vektor)):
            return self.x * other.x + self.y*other.y
    

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return vektor(self.x * other, self.y * other)
        elif isinstance(other,(vektor)):
            return self.x * other.x + self.y*other.y
        

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5    
    

    def angle(self,other):
        szorzat = self*other
        cosalfa = szorzat/(abs(self)*abs(other))
        alfa = math.acos(cosalfa)
        return math.degrees(alfa)


v = vektor(3,1)
v1 = vektor(4, 1)
v2 = vektor(2, 6)
n = 2
print(v2*v1)
print(v1.angle(v2))