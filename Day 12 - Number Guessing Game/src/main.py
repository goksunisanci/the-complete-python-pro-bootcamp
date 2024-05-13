# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from src.art import logo
from random import randint


def get_answer(question, valid_options):
    while True:
        answer = input(question)
        if answer in valid_options:
            return answer
        else:
            print("There is no such option! Try again.")


def get_turn_by_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    else:
        return 5


if __name__ == "__main__":

    while True:
        game = get_answer("Do you want to play the Number Guessing Game? 'y' or 'n': ", ["y", "n"])
        if game == "n":
            break

        number = randint(1, 100)

        welcome_screen_text = f'{logo}\nWelcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.'

        print(welcome_screen_text)
        difficulty_mode = get_answer("Choose a difficulty. Type 'easy' of 'hard': ", ["easy", "hard"])

        turns = get_turn_by_difficulty(difficulty_mode)

        for current_turn in range(turns, 0, -1):
            print(f'You have {current_turn} attempts remaining to guess the number.')
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f'You win! The answer was {number}.')
                break
            elif guess < number:
                print("Too low.")
            else:
                print("Too high.")

            if current_turn == 0:
                print("You lose!")
            else:
                print("Guess again.")
