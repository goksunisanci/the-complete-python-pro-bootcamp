from data import data as data_list
from art import logo, vs
from random import choice, sample


def get_new_options(selected, datas):
    option_1 = selected
    new_second_option = choice(datas)

    while new_second_option == option_1:
        new_second_option = choice(datas)

    return option_1, new_second_option


def format_data(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    return f'{name}, a {description}, from {country}'


if __name__ == "__main__":
    while True:
        game = input("Dou you want to play the Higher Lower Game? 'y' for yes, 'n' for no: ")

        if game == "n":
            break

        score = 0
        welcome_screen_text = f'{logo}\nWelcome to the Higher Lower Game!'
        print(welcome_screen_text)

        first_option, second_option = sample(data_list, k=2)

        while True:
            print(f'Compare A: {format_data(first_option)}')
            print(vs)
            print(f'Compare B: {format_data(second_option)}')
            guess = input("Who has more followers? Type 'A' or 'B': ")

            selected_option = first_option if guess == "A" else second_option
            not_selected_option = second_option if guess == "A" else first_option

            if selected_option["follower_count"] > not_selected_option["follower_count"]:
                score += 1
            else:
                print(f'Sorry, that\'s wrong. Final score: {score}')
                break

            print(f'You\'re right. Your score: {score}')
            first_option, second_option = get_new_options(selected_option, data_list)
