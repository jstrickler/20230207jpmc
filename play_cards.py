from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nero")
d2 = CardDeck("Archie")
j1 = JokerDeck("Saul")

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"j1: {j1}")


d1.shuffle()
print(f"d1.cards: {d1.cards}")

print(f"d1.dealer_name: {d1.dealer_name}")
print(f"d2.dealer_name: {d2.dealer_name}")

d1.dealer_name = "Fritz"

print(f"d1.dealer_name: {d1.dealer_name}")

print(f"d1._cards: {d1._cards}")
print()

for _ in range(5):
    card = d1.draw()
    print(card)
print()

print('-' * 60)
j1.shuffle()
print(f"j1.cards: {j1.cards}")