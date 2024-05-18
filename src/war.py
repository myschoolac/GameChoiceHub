# war.py
import random
from game import Game

class War(Game):
    def __init__(self):
        super().__init__("War")
        self.deck = self.create_deck()
        self.shuffle_deck(self.deck)

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'value': value, 'suit': suit} for value in values for suit in suits]
        return deck

    def shuffle_deck(self, deck):
        random.shuffle(deck)

    def deal_cards(self, num_players, cards_per_player):
        hands = [[] for _ in range(num_players)]
        for _ in range(cards_per_player):
            for hand in hands:
                hand.append(self.deck.pop(0))
        return hands

    def play(self):
        print("Let's play War!")
        hands = self.deal_cards(2, 26)
        player1 = hands[0]
        player2 = hands[1]

        while player1 and player2:
            card1 = player1.pop(0)
            card2 = player2.pop(0)

            print(f"Player 1: {card1['value']} of {card1['suit']} -- Player 2: {card2['value']} of {card2['suit']}")

            if card1['value'] == card2['value']:
                print("War!")
                player1.extend([card1] + self.deal_cards(1, 3)[0])
                player2.extend([card2] + self.deal_cards(1, 3)[0])
            elif card1['value'] > card2['value']:
                print("Player 1 wins the round!")
                player1.extend([card1, card2])
            else:
                print("Player 2 wins the round!")
                player2.extend([card2, card1])

        if not player1:
            print("Player 2 wins the game!")
        else:
            print("Player 1 wins the game!")
