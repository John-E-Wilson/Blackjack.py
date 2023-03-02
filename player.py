class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []
        self.score = 0
        self.current_bet = 0

    def is_player_busted(self):
      if self.score > 21:
          return True
      else:
          return False

    def add_card(self, card):
      self.cards.append(card)
      self.score = self.score + card.value
