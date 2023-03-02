# A card that is contained in a deck.
class Card:
    
    # value is the numeric value of the card 
    # rank is 2,3,4,5,6,7,8,9,J,Q,K,A
    def __init__(self, suit:str, rank:str):
        
        self.suit = suit
        self.rank = rank
        
        if rank == "2":
            self.value = 2
        elif rank == "3":
            self.value = 3
        elif rank == "3":
            self.value = 3
        elif rank == "4":
            self.value = 4
        elif rank == "5":
            self.value = 5
        elif rank == "6":
            self.value = 6
        elif rank == "7":
            self.value = 7
        elif rank == "8":
            self.value = 8
        elif rank == "9":
            self.value = 9
        elif rank == "10" or rank == "J" or rank == "Q" or rank == "K":
            self.value = 10
        elif rank == "A":
            self.value = 11  # TODO:  this should be 1 or 11
        else:
            raise Exception(f"rank is '{rank}' but it should be a value of 2,3,4,5,6,7,8,9,J,Q,K,A")

        if suit == "diamond":
            self.suite_image = "♦️"
        elif suit == "heart":
            self.suite_image = "❤️"
        elif suit == "spade":
            self.suite_image = "♠️"
        elif suit == "club":
            self.suite_image = "♣️"
        else:
            raise Exception(f"suit is '{suit}' but it should diamond, heart, spade or club")

