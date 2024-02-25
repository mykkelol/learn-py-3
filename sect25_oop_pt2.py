""" 
Implement two classes, Card and Deck:
- each instance of Card should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
- each instance of Card should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
- Card's __repr__ method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

- each instance of Deck should have a cards attribute with all 52 possible instances of Card.
- Deck should have an instance method called count which returns a count of how many cards remain in the deck.
- Deck's __repr__ method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
- Deck should have an instance method called _deal which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should raise a ValueError with the message "All cards have been dealt".
- Deck should have an instance method called shuffle which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
- Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck and return that single card.
- Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a list of cards from the deck and return that list of cards.
- Deck should allow us to iterate over cards without accessing Deck.cards directly by converting it into an iterator

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
    
    def __iter__(self):
        return iter(self.cards)

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
