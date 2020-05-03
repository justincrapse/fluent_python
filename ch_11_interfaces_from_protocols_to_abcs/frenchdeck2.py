import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value

    # must implement these next 2 functions as they are abstract methods of the ABC collections.MutableSequence.
    # otherwise error thrown:"Can't instantiate abstract class FrenchDeck with abstract methods ______(abstract method)"
    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, position, value):
        self._cards.insert(position, value)
        

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    deck = FrenchDeck()
    print(f'randome card: {choice(deck)}')

    for card in sorted(deck, key=spades_high):
        print(card)

    print(Card('Q', 'hearts') in deck)
