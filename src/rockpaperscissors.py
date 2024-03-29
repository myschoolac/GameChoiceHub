# rock_paper_scissors.py
import random
from game import Game


class RockPaperScissors(Game):

  def __init__(self):
    super().__init__("Rock Paper Scissors")
    self.choices = ['rock', 'paper', 'scissors']

  def play(self):
    print("Let's play Rock Paper Scissors!")
    while True:
      player_choice = input(
          "Choose rock, paper, or scissors (type 'exit' to quit): ").strip(
          ).lower()
      if player_choice == 'exit':
        break
      elif player_choice not in self.choices:
        print(
            "Invalid choice. Please choose from 'rock', 'paper', or 'scissors'."
        )
      else:
        computer_choice = random.choice(self.choices)
        print(f"Computer chooses: {computer_choice}")
        if player_choice == computer_choice:
          print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
          print("You win!")
        else:
          print("Computer wins!")
        break
