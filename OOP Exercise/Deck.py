# OOP Exercise

# Import Card module from the Card folder in Github

# https://gist.github.com/MRobertEvers/55a989b4883ea8d7715d2e156627f034
import sys

# Navigate to the folder where the module is
sys.path.append("./Card")

# Import the module
from Card import Card

# Import random module
import random


# Create a class Deck

class Deck:

    # Class attributes: Each instance of Card should have one of these suits & values
    suits=["Hearts", "Diamonds", "Clubs", "Spades"]
    values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Set no of cards in the deck
    no_cards=0

    def __init__(self):
        self.cards=[] # each instance of Deck should contain a list of cards
        self.build() # when an instance is initiated, the "build" function should be called to build a new deck


    def build(self): # This is to build a new deck
        for s in Deck.suits:
            for v in Deck.values:
                self.cards.append(Card(s,v)) # append to the instance (cards list) a Card (from module "Card") for each suit/ value combo
                Deck.no_cards+=1 # add a card to the no of cards in the deck for every card appended



    def __repr__(self): # This should show the total no of cards in the deck (i.e. remain static even after a card is dealt)
        n=0
        for s in Deck.suits:
            for v in Deck.values:
                n+=1
        rep = f"Deck of {n} cards."
        return rep



    def show_deck(self):
        return print(self.cards)



    def count(self): # counts the no of cards remaining in the deck
        return print(f" There are {Deck.no_cards} cards remaining in the deck.")



    def _deal(self, x): # accepts a no & removes at most that no of cards from the deck (may need to remove fewer if there are not enough cards left in the deck)
       if Deck.no_cards >=x:
           Deck.no_cards-=x
       elif Deck.no_cards ==0: #if there are no cards in the deck, the method should return a ValueError "All cards have been dealt)
           raise ValueError("All cards have been dealt.")
       else:
           Deck.no_cards-=Deck.no_cards



    def shuffle(self): #This shuffles a full deck of cards
        if Deck.no_cards==52:
            return random.shuffle(self.cards)
        else:
            return print("Only full decks can be shuffled")



    def deal_card(self): #uses _deal method to deal a single card & returns that single card
        self._deal(1)
        card_dealt=self.cards.pop(0)
        return print(card_dealt)



    def deal_hand(self, x): #accepts a no & uses _deal method to deal a list of cards from the deck & returns that list of cards
        hand=[]
        self._deal(x)
        print(self.cards)
        for n in range(x):
            hand.append(self.cards.pop(0))
        return print(hand)


d1=Deck()

print(d1)

d1.show_deck()

d1.count()

d1.shuffle()

d1.show_deck()

d1.deal_hand(8)

d1.count()

d1.deal_card()

d1.count()

# d1._deal(39)
#
# d1.count()
#
# d1._deal(2)
#
# d1.count()
#
# d1._deal(1)


