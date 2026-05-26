import random

SYMBOLS = ['pikk', 'káró', 'kőr', 'treff']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
    def __init__(self, symbol, value):
        if symbol.lower() not in SYMBOLS:
            raise Exception('Nem megfelelő szín')
        if value.upper() not in VALUES:
            raise Exception('Nem megfelelő érték')
        
        self.symbol = symbol.lower()
        self.value = value.upper()
        
    def __repr__(self):
        return f"{self.symbol}-{self.value}"
    

class Deck:
    def __init__(self):
        self.cards = []
        for s in SYMBOLS:
            for v in VALUES:
                self.cards.append( Card(symbol=s, value=v) )
    

    def __repr__(self):
        return f"{len(self.cards)}/52 lap"
    

    def shuffle(self):
        for _ in range(100):
            a = random.randint(0, len(self.cards)-1)
            b = random.randint(0, len(self.cards)-1)
            self.cards[a], self.cards[b] = self.cards[b], self.cards[a]

    
    def cut(self):
        a = random.randint(0, len(self.cards)-1)
        self.cards = self.cards[a:] + self.cards[:a]


    def draw(self):
        c = self.cards[0]
        self.cards = self.cards[1:]
        return c

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = [Card]


    def add_card(self, c: Card):
        self.cards.append(c)


    def value(self):
        v = 0
        a_count = 0
        for c in self.cards:
            if c.value in ('A'):
                v += 11
            elif c.value in ('J', 'Q', 'K'):
                v += 10
            else:
                v += int(c.value)
        


c = Card('pikk', 'a')
print(c)

d = Deck()
print(d)
print(d.cards[5])
d.shuffle()
print(d.cards[5])
c = d.draw()
print(c)
print(d)