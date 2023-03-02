from card import Card
import random
# A deck of cards
class Deck:
     def __init__(self):
        self.current_index = 0
        self.cards = [\
            Card("spade", "2"),\
            Card("spade", "3"),\
            Card("spade", "4"),\
            Card("spade", "5"),\
            Card("spade", "6"),\
            Card("spade", "7"),\
            Card("spade", "8"),\
            Card("spade", "9"),\
            Card("spade", "10"),\
            Card("spade", "J"),\
            Card("spade", "Q"),\
            Card("spade", "K"),\
            Card("spade", "A"),\
            Card("club", "2"),\
            Card("club", "3"),\
            Card("club", "4"),\
            Card("club", "5"),\
            Card("club", "6"),\
            Card("club", "7"),\
            Card("club", "8"),\
            Card("club", "9"),\
            Card("club", "10"),\
            Card("club", "J"),\
            Card("club", "Q"),\
            Card("club", "K"),\
            Card("club", "A"),\
            Card("diamond", "2"),\
            Card("diamond", "3"),\
            Card("diamond", "4"),\
            Card("diamond", "5"),\
            Card("diamond", "6"),\
            Card("diamond", "7"),\
            Card("diamond", "8"),\
            Card("diamond", "9"),\
            Card("diamond", "10"),\
            Card("diamond", "J"),\
            Card("diamond", "Q"),\
            Card("diamond", "K"),\
            Card("diamond", "A"),\
            Card("diamond", "2"),\
            Card("diamond", "3"),\
            Card("diamond", "4"),\
            Card("diamond", "5"),\
            Card("diamond", "6"),\
            Card("diamond", "7"),\
            Card("diamond", "8"),\
            Card("diamond", "9"),\
            Card("diamond", "10"),\
            Card("diamond", "J"),\
            Card("diamond", "Q"),\
            Card("diamond", "K"),\
            Card("diamond", "A") ]

     def get_next_card(self):
        card = self.cards [self.current_index]
        self.current_index = self.current_index + 1
        return card

     def shuffle_cards(self):
        random.shuffle(self.cards)

