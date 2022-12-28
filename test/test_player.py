import unittest
from src.deck import Deck
from src.card import Card
from src.player import Player


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.player = Player(self.deck)
        

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards_after_deal(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 50)
        self.assertEqual(len(self.player.hand), 2)

    def test_scenario_2(self):  # Given I have a valid hand of cards, When I choose to ‘hit’, Then I receive another card, And my score is updated
        number_of_cards = len(self.deck.cards)
        init_score = self.player.score
        self.player.hit(1, self.deck)
        self.assertEqual(len(self.player.hand), 3) 
        print(self.player.score)
        for i in range(len(self.player.hand)):
            print(self.player.hand[i].rank)
            print(self.player.hand[i].suit)






if __name__ == '__main__':
    unittest.main()
