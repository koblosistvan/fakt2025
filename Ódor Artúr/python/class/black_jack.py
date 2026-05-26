import random


COLOR = ["pikk", "káró", "kör", "treff"]
VAULE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]


class Cards:
    def __init__(self, color, vaule):
        if color.lower() not in COLOR:
            raise Exception("Nem megfelelő szín")
        if vaule.upper() not in VAULE:
            raise Exception("Nem megfelelő érték")
        
        self.color = color
        self.vaule = vaule

    
    def __repr__(self):
        return f"{self.color} {self.vaule}"


class Deck:
    def __init__(self):
        for s in VAULE:
            for c in COLOR:
                self.cards.append(Cards(vaule = s, color = c))


    def __repr__(self):
        return 


    def shuffle(self):
        for _ in range(100):
            a = random.randint(0, len(self.cards)-1)
            b = random.randint(0, len(self.cards)-1)
            self.cards[a], self.cards[b] = self.cards[b], self.cards[a]

        
    def draw(self):
        c = self.cards[0]
        self.cards = self.cards[1:]
        return c


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    
    def add_cards(self, c: Cards):
        self.cards.append(c)


    def vaule(self):
        v = 0
        for c in self.cards:
            if c.vaule in ("A"):
                v +=11
            elif c.vaule in ("J", "D", "K", "10"):
                v += 10
            else:
                v += int(c.vaule)



kártya = Cards("kör","2")
print(kártya)

d = Deck()
print(d)
c = d.draw
print(c)