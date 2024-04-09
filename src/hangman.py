# hangman.py
import random
from game import Game

class Hangman(Game):
  def __init__(self, name):
     super().__init__(name)
     self.words = ['apple', 'banana', 'cherry', 'dog', 'cat', 'elephant', 'guitar', 'keyboard', 'mountain', 
                              'ocean', 'sunshine', 'moon', 'pizza', 'coffee', 'cake', 'book', 'pencil', 'chair', 
                              'television', 'soccer', 'basketball', 'football', 'volleyball', 'swimming', 'running', 
                              'hiking', 'dancing', 'singing', 'garden', 'flower', 'butterfly', 'airplane', 'train', 
                              'car', 'bicycle', 'shoes', 'hat', 'jacket', 'glasses', 'phone', 'computer', 'mouse', 
                              'keyboard', 'desk', 'lamp', 'table', 'couch', 'bed']
     self.word = random.choice(self.words)
     self.guesses_left = 6
     self.guessed_letters = []

def display_word(self):
    display = ''
    for letter in self.word:
       if letter in self.guessed_letters:
           display += letter + ' '
       else:
           display += '_ '
           return display.strip()

def make_guess(self, letter):
   if letter in self.guessed_letters:
       return "You've already guessed that letter."
   elif letter in self.word:
        self.guessed_letters.append(letter)
        return "Correct guess!"
   else:
        self.guessed_letters.append(letter)
        self.guesses_left -= 1
        return "Incorrect guess."

def check_win(self):
    for letter in self.word:
        if letter not in self.guessed_letters:
          return False
        return True

# filename:hangman.py
def play(self):
    print("Let's play Hangman!")
    print("Guess the word before running out of guesses.")
    while self.guesses_left > 0:
       print("Word:", self.display_word())
       print("Guesses left:", self.guesses_left)
       guess = input("Enter a letter guess: ").lower()
       if len(guess) != 1 or not guess.isalpha():
          print("Invalid input. Please enter a single letter.")
          continue
       result = self.make_guess(guess)
       print(result)
       if self.check_win():
         print("Congratulations! You've won!")
         break
       if self.guesses_left == 0:
         print("Sorry, you've run out of guesses. The word was:", self.word)
         break
