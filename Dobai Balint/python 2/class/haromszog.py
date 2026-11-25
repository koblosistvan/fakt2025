class Pont:
    x:float
    y:float
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def __sub__(self,other):
        return Pont(self.x-other.x , self.y-other.y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

class Haromszog:
    a: Pont
    b: Pont
    c: Pont

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 

    def __repr__(self):
        return f'{self.a} , {self.b} , {self.c}'


    def hossz(self,oldal):
        if oldal == 'a':
            return abs (self.b-self.c)
        elif oldal == 'b':
            return abs (self.c-self.a)
        elif oldal == 'c':
            return abs (self.b-self.a)
        else:
            return -1
        
    def terulet(self):
        a = self.hossz('a')
        b = self.hossz('b')
        c = self.hossz('c')
        return 0.25* ((a + b + c)*(-a + b + c)*(a-b+c)*(a+b-c))**0.5
    def kerulet(self):
        a = self.hossz('a')
        b = self.hossz('b')
        c = self.hossz('c')
        return (a+b+c)





h = Haromszog(Pont(0,0), Pont(4,3), Pont(3,2))
print(h.terulet())
print(h.kerulet())



