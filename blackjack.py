from card import Card
from player import Player
from deck import Deck

def take_player_bets(players):
    for player in players:
        while True:

            bet = input(f"Player {player.name} has {player.money}, how much does {player.name} bet ? (1-5000)")
            if bet > player.money:
                print("Player has bet more than they have....")
            else:
                player.current_bet = bet
                break

# This function will cause the dealer to raise until it wins with 17-21 or busts higher.
def dealer_decision(deck_of_cards, dealer, players):
    highest_score = 0
    for player in players:
        if player.score <= 21 and player.score > highest_score:
            highest_score = player.score

    while dealer.score < highest_score and dealer.score < 17:
        if dealer.score == 21: # dealer wins with 21
            print("Dealer Wins")
            break
        elif dealer.score > 21: # if dealer exceeds 21 they lose
            print("The Dealer has busted :)")
            break
        else: # dealer getting next card if not at 21
            card = deck_of_cards.get_next_card()
            dealer.add_card(card)
            print_cards(dealer)
            print(dealer.score)






def player_decision(deck_of_cards, players):
    for player in players:
        player_is_done = False
        while player_is_done == False:
            decision = input(f"What is {player.name}'s decision ? (H/S)")
            if decision == "H":
                card = deck_of_cards.get_next_card()
                player.add_card(card)
                print_cards(player)
                print(player.score)
                if player.is_player_busted():
                    player_is_done = True
                    print("Player just Busted a fatty")

            else:
                player_is_done = True



def create_players():
    players = []
    name = ""
    while True:
        name = input("Players Name")
        if name == "done":
            break
        money = input("Players Money")
        player = Player (name,money)
        players.append(player)
    return players


def create_dealer():
    money = 100
    name = "Randall the Dealer 69 420"
    return Player(name,money)



def deal_cards(deck_of_cards, players, dealer):
    for player in players:
        card = deck_of_cards.get_next_card()
        player.add_card(card)
        print_cards(player)
    card = deck_of_cards.get_next_card()
    dealer.add_card(card)
    print_cards(dealer)


def print_cards(player):
    print(f"Player {player.name} ")
    for card in player.cards:
        print(f"   {card.rank} {card.suite_image}")





players = create_players()
dealer = create_dealer()
deck = Deck()
deck.shuffle_cards()
take_player_bets(players)
deal_cards(deck, players, dealer)
deal_cards(deck, players, dealer)
player_decision(deck, players)
dealer_decision(deck, dealer, players)
print("GAME OVER")




