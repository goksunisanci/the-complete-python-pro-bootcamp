############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

from src.art import logo
from random import choices, choice

all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_game = False


def is_player_lose(player_cards, computer_cards):
    sum_player_cards = sum(player_cards)
    sum_computer_cards = sum(computer_cards)
    if sum_player_cards > 21:
        return True
    elif sum_player_cards < sum_computer_cards and sum(computer_cards) <= 21:
        return True
    else:
        return False


def check_ace(cards):
    if sum(cards) > 21:
        for index, card in enumerate(cards):
            if card == 11:
                cards[index] = 1
                break


if __name__ == "__main__":
    while not end_game:
        play_game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_game == "n":
            end_game = True
            continue

        print(logo)

        player_cards = choices(all_cards, k=2)
        computer_cards = [choice(all_cards)]
        player_lose = False

        if sum(player_cards) == 21:
            final_context = (f'Your final cards: {player_cards}, current score: {sum(player_cards)}\n'
                             f'Computer\'s final cards: {computer_cards}, final score: {sum(computer_cards)}')

            print(final_context)
            print("Blackjack! You win.")
            continue

        check_ace(player_cards)
        while sum(player_cards) < 21:
            context = (f'Your cards: {player_cards}, current score: {sum(player_cards)}\n'
                       f'Computer\'s first card: {computer_cards}')

            print(context)
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card == "n":
                break
            elif get_another_card == "y":
                player_cards.append(choice(all_cards))
                check_ace(player_cards)

            else:
                print("Type 'y' or 'n'!")

        check_ace(computer_cards)
        while sum(computer_cards) < 21:
            player_lose = is_player_lose(player_cards, computer_cards)

            if player_lose:
                break
            elif sum(computer_cards) >= 21:
                break
            else:
                computer_cards.append(choice(all_cards))
                check_ace(computer_cards)

        final_context = (f'Your final cards: {player_cards}, current score: {sum(player_cards)}\n'
                         f'Computer\'s final cards: {computer_cards}, final score: {sum(computer_cards)}')

        print(final_context)

        player_lose = is_player_lose(player_cards, computer_cards)

        if player_lose:
            print("You lose!")
        else:
            print("You win!")
