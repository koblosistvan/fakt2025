import math


A='a'
B='b'
C='c'



class Pont:
    x:float
    y:float


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f'[{self.x},{self.y}]'
    
    
    def __sub__(self, other):
        return Pont(self.x - other.x, self.y - other.y)


    def __abs__(self):
        return (self.x**2+self.y**2)**0.5 


class Haromszog:
    a: Pont
    b: Pont
    c: Pont


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    

    def hossz(self, oldal):
        if oldal == A:
            return abs(self.b - self.a)
        elif oldal == B:
            return abs(self.c - self.b)
        elif oldal == C:
            return abs(self.a-self.c)
        else:
            return 'Error 418'

    def kerulet(self):
        return A+B+C

    def terulet(self):
        s = self.kerulet()/2
        return (s*(s-A)*(s-B)*(s-C))**0.5

    def magassag(self):
        (self.terulet()*2)/self.hossz()

    def szog(self, szog):
        if szog == 'alfa':
            math.asin(self.terulet()*2/(B*C))
        elif szog == 'beta':
            math.asin(self.terulet()*2/(A*C))
        elif szog == 'gamma':
            math.asin(self.terulet()*2/(B*A))
        else:
            return 'I am still a Teapot'


    def beirt_sugar(self,s):
        s = self.kerulet()/2
        return self.terulet()/s


    def koreirt_sugar(self):
        ((A*B*C)/(self.terulet()*4))
    
    def __repr__(self):
        return f'{self.hossz(A)},{self.hossz(B)},{self.hossz(C)}\n, {self.kerulet()}\n, {self.terulet()}\n, {self.magassag()}\n, {self.szog('alfa')},{self.szog('beta')},{self.szog('gamma')}\n, {self.beirt_sugar()} '

h= Haromszog(Pont(0,0), Pont(4,3), Pont(3,2))
#print(abs(Pont(5,4) - Pont(4,5)))

print()