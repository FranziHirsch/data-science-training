# OOP Exercise

# Create a class "Card"

class Card:

    # Class attributes: Each instance of Card should have one of these suits & values
    suits=["Hearts", "Diamonds", "Clubs", "Spades"]
    values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value): # Each instance of card should have a suit and a value
        # If an instance is created where the suit/ value is not included in the lists above,
        # raise a ValueError
        if suit not in Card.suits or value not in Card.values:
            raise ValueError("Not a valid card")
        self.suit=suit
        self.value=value

    def  __repr__(self): # This is to set out how each instance of Card should appear
        rep=f"{self.value} of {self.suit}"
        return rep

