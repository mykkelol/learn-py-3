""" 


"""


from random import shuffle as s

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'
    
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)
    
    def _deal(self, number_of_cards):
        count = self.count()
        if count == 0:
            raise ValueError('All cards have been dealt')
        actual_to_remove = min(count, number_of_cards) # need to know which is lesser to deal whatever's remaining or the requested num
        dealt_cards = self.cards[-actual_to_remove:] # to return cards dealt and will be removed since we're removing from the end of deck
        self.cards = self.cards[:-actual_to_remove] # update deck by removing cards dealt
        return dealt_cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            s(self.cards)
            return self.cards
        
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)
