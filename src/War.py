import random
from game import Game

class War(Game):
    def __init__(self):
        super().__init__("War")
        self.deck = []
        self.player1_hand = []
        self.player2_hand = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.deck.append((rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        self.player1_hand = self.deck[:26]
        self.player2_hand = self.deck[26:]

      # filename:war.py
    def play(self):
       print("Let's play War!")
       # Add the game logic here
       print("Game Over! The game of War has ended.")
       # Remove the direct return statement at the end
