import unittest
from src.Card import Card

class CardUTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_creating_cards(self):
    
        #Testing wrong card    
        card_wrong = Card('xxx', 'yyy')
        v = card_wrong.get_value()
        self.assertEqual(v, -1, "Should be -1")
        
        #Testing correct card: Ace of Spades
        ace_of_spades = Card('Spades', 'Ace')
        v = ace_of_spades.get_value()
        self.assertEqual(v, 14, "Should be 14")
        
        #Testing trump card functionality
        ace_of_spades.set_trump('Hearths')
        v = ace_of_spades.get_value()
        self.assertEqual(v, 14, "Not a trump, shoul be 14 stil")
    
        ace_of_spades.set_trump('Spades')
        v = ace_of_spades.get_value()
        self.assertEqual(v, 114, "A trump, shoul be 14+100 stil")      
    
    
    
# Run the tests    
suite = unittest.TestLoader().loadTestsFromTestCase(CardUTest)
unittest.TextTestRunner(verbosity=2).run(suite)

