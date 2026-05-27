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
                self.cards.append(Card(symbol=s, value=v))
    
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

    def draw(self)->Card:
        c = self.cards[0]
        self.cards = self.cards[1:]
        return c


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def value(self):
        v = 0
        a_count = 0
        for card in self.cards:
            if card.value in ('A'):
                v += 11
                a_count += 1
            elif card.value in ('J', 'Q', 'K'):
                v += 10
            else:
                v += int(card.value)

        sub_a = min(
            (v-12)//10,
            a_count
        )
        return v - sub_a*10 if sub_a > 0 else v

    def __repr__(self) -> str:
        return f"{self.name}: {self.value()} pont {self.cards}"


d = Deck()
d.shuffle()


player = Hand(name='Joe')
player.add_card(card=d.draw())
player.add_card(card=d.draw())

dealer = Hand(name='Dealer')
dealer.add_card(card=d.draw())
dealer.add_card(card=d.draw())

print(player)
print(dealer)

player_draws = input('\nKérsz még lapot (i/n): ')
while player_draws == 'i':
    player.add_card(card=d.draw())
    print(player)
    player_draws = input('\nKérsz még lapot (i/n): ')

winner = None
if player.value() > 21:
    winner = dealer
else:
    while dealer.value() < 17:
        dealer.add_card(card=d.draw())
        print(dealer)

    if player.value() > dealer.value() or dealer.value() > 21:
        winner = player
    elif player.value() < dealer.value():
        winner = dealer

print('A játéknak vége.')
if winner:
    print(f"A győztes: {winner.name}")
else:
    print('Döntetlen')
