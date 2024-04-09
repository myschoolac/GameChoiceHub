# Import game classes
from rock_paper_scissors import RockPaperScissors
from coin_flip import CoinFlip
from hangman import Hangman
from war import War


# Game Hub class
class GameHub:
    def __init__(self):
        self.games = {
            "Rock Paper Scissors": RockPaperScissors(),
            "Coin Flip": CoinFlip(),
            "Hangman": Hangman("python"),
            "War": War()
        }

    def display_intro(self):
        print("Welcome to the Game Hub where you can choose from different minigames. Please select a game to play:")
        print("Here are the available games:")
        for game_name in self.games:
            print("-", game_name)

    def play(self):
        self.display_intro()
        while True:
            print("\nChoose a game to play or type 'exit' to quit-")
            game_name = input(">> ").strip()
            if game_name.lower() == 'exit':
                print("Thanks for playing! Goodbye!")
                break
            elif game_name in self.games:
                game = self.games[game_name]
                game.play()
                print("\nFinished playing", game_name)
            else:
                print("Invalid game choice. Please choose from the available games.")

# Create a game hub and play games
game_hub = GameHub()
# Place the modification here
def wait_for_keypress():
  input("Press any key to start the Game Hub, and then press enter after typing the keypress:")
def start_game_hub():
    game_hub.play()
wait_for_keypress()  # Wait for any keypress to start the game hub
start_game_hub()


game_hub.play()
