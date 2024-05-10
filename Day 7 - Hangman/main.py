import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

# TODO-11: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this:
# word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-4: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False

# TODO-8: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

# TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
#  all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while not end_of_game:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # TODO-12: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You have already guessed {guess}')

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # TODO-5: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # TODO-9: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1

        # TODO-13: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You guessed {guess}, that is not in the word. You lose a life.')

    if lives == 0:
        end_of_game = True
        print("You lose!")

    # TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter
    #  replace with "_".
    # Join all the elements in the list and turn it into a String.
    print(f'{" ".join(display)}')

    if "_" not in display:
        end_of_game = True
        print("You win!")

    # TODO-10: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user
    #  has remaining.
    print(stages[lives])
