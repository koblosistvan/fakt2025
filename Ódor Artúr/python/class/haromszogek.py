import math

class Pont:
    x: float
    y: float
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def __repr__(self):
        return f"({self.x};{self.y})"


class Haromszog:
    a: Pont
    b: Pont
    c: Pont

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def oldal(self, z):
        if z == "a":
            return self.b - self.c
        elif z == "b":
            return self.a - self.c
        elif z == "c":
            return self.b - self.c

    def kerulet(self):
        return self.oldal("a") + self.oldal("b") + self.oldal("c")

    def terulet(self):
        s = self.kerulet()/2
        return (s*(s-self.oldal("a"))*(s-self.oldal("b"))*(s-self.oldal("c")))**0.5
    
    def magassag(self, w):
        t = self.terulet()*2
        if w == "a":
            return t/self.oldal("a")
        elif w == "b":
            return t/self.oldal("b")
        elif w == "c":
            return t/self.oldal("c")

    def szog(self, q):
        oa = self.oldal("a")
        ob = self.oldal("b")
        oc = self.oldal("c")
        if q == "a":
            return math.acos((ob**2 + oc**2 - oa**2)/(2*ob*oc))*(180/math.pi)
        if q == "b":
            return math.acos((oa**2 + oc**2 - ob**2)/(2*oa*oc))*(180/math.pi)
        if q == "c":
            return math.acos((ob**2 + oa**2 - oc**2)/(2*ob*oa))*(180/math.pi)

    def belsokor_sugar(self):
        return self.terulet()/(self.kerulet()/2)

    def kulsokor_sugar(self):
        return     

a = Pont(0,3)
b = Pont(1,5)
c = Pont(2,3)
haromszog = Haromszog(a, b, c)
print(haromszog.oldal("c"))
print(haromszog.terulet())
print(haromszog.magassag("a"))
print(haromszog.szog("c"))