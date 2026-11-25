import os
os.system('cls')

class Pont:
    x:float
    y:float


    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    
    def __sub__(self, other):
        return Pont(self.x - other.x, self.y-other.y)

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
     
    def __repr__(self):
        return f'({self.x};{self.y})'


class Haromszog:
    A: Pont
    B: Pont
    C: Pont
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C


    def oldal(self, n):
        if n == C:
            return(abs(A-B))
        if n == B:
            return(abs(A-C))
        if n == A:
            return(abs(B-C))


    def k(self):
        return self.oldal(C)+self.oldal(B)+self.oldal(A)

    def t(self):
        return (K/2*(K/2*h.oldal(A))*(K/2*h.oldal(B))*(K/2*h.oldal(C)))**0.5




    
    def __repr__(self):
        return(f'{A},{B},{C}')


A = Pont(-5,2)
B = Pont(5,2)
C = Pont(0,10)
h = Haromszog(A,B,C)
K = h.k()
print(h.t())
