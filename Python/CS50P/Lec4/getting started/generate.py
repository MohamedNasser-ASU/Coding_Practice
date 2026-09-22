import random
cards = [ "jack", "queen", "king"]

coin = random.choice(["heads","tails"])
number = random.randint(1,10)
print(f"{coin}, {number}")
random.shuffle(cards)
for card in cards:
    print(card, end = ", ")




print()
