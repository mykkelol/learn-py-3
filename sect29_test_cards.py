from sect25_oop_pt2 import Card, Deck
from random import shuffle
import unittest

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts', 'A')

    def test_init(self):
        """card must have a suit and a value"""
        self.assertEqual(self.card.suit, 'Hearts')
        self.assertEqual(self.card.value, 'A')
    
    def test_repr(self):
        """repr must return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), 'A of Hearts')

class DeckTest(unittest.TestCase):
    def setUp(self):
        # notice how with setUp, self.deck.cards refreshes to original state of 52 for every test
        self.deck = Deck()

    def test_init(self):
        """deck must have a list of 52 cards at initialization"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_count(self):
        """count must dynamically return count of cards after every hand dealt"""
        self.assertEqual(len(self.deck.cards), 52)
        self.deck.cards.pop()
        self.assertEqual(len(self.deck.cards), 51)

    def test_deal_sufficient_cards(self):
        """_deal must deal up to what is requested"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.cards, 42)
    
    def test_deal_sufficient_cards(self):
        """_deal must deal up to what is remaining but not more"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(len(self.deck.cards), 0)
    
    def test_deal_no_cards(self):
        """_deal must throw ValueError if deal is requested but there is no card remaining"""
        self.deck._deal(100)
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card must return one card at a time"""
        card = self.deck.cards[-1] # we're not popping it out so we're saving the last value that will be pop for validation
        dealt_card = self.deck._deal(1)[0]
        self.assertEqual(card, dealt_card)
        self.assertEqual(len(self.deck.cards), 51)
    
    def test_deal_hand(self):
        """deal_hand must deal the exact number of cards specified"""
        dealt_cards = self.deck._deal(10)
        self.assertEqual(len(dealt_cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_shuffle_full_deck(self):
        """shuffle must shuffle the cards randomly if the deck has not been drawn"""
        cards = self.deck.cards[:] # create full shallow copy
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)
    
    def test_shuffle_not_full_deck(self):
        """shuffle must not be shuffled if it is not a full deck"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

if __name__ == '__main__':
    unittest.main()