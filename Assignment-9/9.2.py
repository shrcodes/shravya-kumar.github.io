Write a txt file which has a word in each line like:
Hands
Legs
India
Crow
Rain
...
Write a python code to read the file and store the words in the list
def read_words(filename):
 with open(filename, 'r') as file:
 words = file.read().splitlines()
 return words
Write a function to guess a word randomly from the list.
import random
def random_word(words):
 return random.choice(words)
Now, write a function which asks user to guess the chosen word letter by letter.
Show "incorrect" message to the wrong guessed letter.
Display letters in the clue word that were guessed correctly.
Let say word is EVAPORATE
>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
You left with 5 chances to guess.
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on.
1)Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed.
2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
3)When the player wins or loses, let them start a new game.
def hangman(word):
 print("Welcome to Hangman!")
 guesses = []
 turns = 6
 while turns > 0:
 failed = 0
 for char in word:
 if char in guesses:
 print(char, end=' ')
 else:
 print("_", end=' ')
 failed += 1
 if failed == 0:
 print("\nYou win!")
 break
 guess = input("\nGuess a letter: ").lower()
 if guess in guesses:
 print("You already guessed that letter!")
 elif guess in word:
 guesses.append(guess)
 else:
 turns -= 1
 print("Incorrect! You have", turns, "guesses left.")
 if turns == 0:
 print("\nYou lose! The word was", word)
if __name__ == '__main__':
 words = read_words('words.txt')
 while True:
 word = random_word(words)
 hangman(word)
 play_again = input("Do you want to play again? (y/n) ").lower()
 if play_again != 'y':
 break