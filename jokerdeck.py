from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call parent method
        for _ in range(2):
            self._cards.append(("***Joker***", "Joker"))

