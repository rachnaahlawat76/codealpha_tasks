
import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "science"]

# Randomly select a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect attempts.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    # Check if the player has won
    if "_" not in display_word:
        print("\nCongratulations! YOU WON!")
        break

    # Take input from player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    # Check duplicate guesses
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check losing condition
if incorrect_guesses == max_attempts:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThanks for playing!")