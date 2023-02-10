import random

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):   # constructor
        self._dealer = dealer
        self._make_deck()

    @property
    def dealer_name(self):  # getter property
        return self._dealer

    @dealer_name.setter
    def dealer_name(self, dealer_name):  # setter property
        if isinstance(dealer_name, str):
            self._dealer = dealer_name
        else:
            raise TypeError("Dealer must be a string")


    @property  # public variable implemented by a method
    def cards(self):  # getter property
        return self._cards


    def _make_deck(self):
        self._cards = []  # store the cards here
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # make a tuple
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)


    def draw(self):
        return self._cards.pop()  # return 1 card

    def __str__(self):  # implement str(obj)
        return "CardDeck"



