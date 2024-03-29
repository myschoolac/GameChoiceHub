# coin_flip.py
import random
from game import Game


class CoinFlip(Game):

  def __init__(self):
    super().__init__("Coin Flip")
    self.coin_sides = ['heads', 'tails']

  def play(self):
    print("Let's play Coin Flip!")
    while True:
      player_choice = input(
          "Guess heads or tails (type 'exit' to quit): ").strip().lower()
      if player_choice == 'exit':
        break
      elif player_choice not in self.coin_sides:
        print("Invalid choice. Please choose 'heads' or 'tails'.")
      else:
        computer_choice = random.choice(self.coin_sides)
        print(f"Computer chooses: {computer_choice}")
        if player_choice == computer_choice:
          print("You win!")
        else:
          print("Computer wins!")
        break
