zz = "####################################################"
print(zz)

aa = "Deck Class"
bb = "- Instantiate a new deck"
cc = "-- Create all 52 card objects"
dd = "-- Hold as a list of Card objects"
ee = "- Shuffle a Deck through a method call"
ff = "--Random library shuffle() function"
gg = "- Deal cards from the Deck object"
hh = "-- Pop method from cards list"
ii = "- We will see that that Deck class holds a list of Card objects"
jj = "- This means that the Deck class will return Card class object instances"
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)
print(gg)
print(hh)
print(ii)
print(jj)
print(zz)

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
new_deck = Deck()
new_deck.shuffle()
#print(new_deck.all_cards)
first_card = new_deck.all_cards[0]
print(first_card)
last_card = new_deck.all_cards[-1]
print(last_card)
print(zz)

mycard = new_deck.deal_one()
print(type(mycard))
print(mycard)
print(len((new_deck.all_cards)))
print(zz)