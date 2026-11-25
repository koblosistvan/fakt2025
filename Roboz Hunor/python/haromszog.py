

class Pont:
    x: float
    y: float


    def __init__(self,x,y):
        self.x = x
        self.y = y

    
    def __sub__(self, other):
        return ((self.x-other.x)**2 + (self.y - other.y)**2)**0.5


    def __abs__(self):
        pass


    def __repr__(self):
        return f'({self.x};{self.y})'





class Haromszog:
    a: Pont
    b: Pont
    c: Pont

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def oldal(self, z):
        if z == 'a':
            return self.b-self.c
        elif z == 'b':
            return self.a-self.c
        elif z == 'c':
            return self.b-self.a

