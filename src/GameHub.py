# Game Hub class
class GameHub:
    def __init__(self):
        self.games = {
            "Rock Paper Scissors": RockPaperScissors(),
            "Coin Flip": CoinFlip(),
            "Hangman": Hangman("python"),
            "War": War()
        }
