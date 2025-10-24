zz = "##########################################"
print(zz)

aa = "- Player Class"
bb = "-- This class will hold the player's current list of cards"
cc = "-- The player should be able to add or remove cards from their 'hand' (list of Card objects)"
dd = "-- We will want the player to add a single or multiple cards to their list"
ee = "-- We need to be able to translate a Deck/Hand of cards with a top and bottom to a python list"
ff = "--- Player Class with a self.all_cards.list"
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)
print(zz)

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('02', '03', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'02':2, '03':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
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
print(new_deck.all_cards[0])
mycard = new_deck.deal_one()
print(mycard)
print(zz)

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
new_player = Player("Todd")
print(new_player)
new_player.add_cards(mycard)
print(new_player)
print(new_player.all_cards[0])
print(zz)