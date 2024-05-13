from data import data
from art import logo, vs

if __name__ == "__main__":
    while True:
        game = input("Dou you want to play the Higher Lower Game? 'y' for yes, 'n' for no: ")

        if game == "n":
            break

        welcome_screen_text = f'{logo}\nWelcome to the Higher Lower Game!'
        print(welcome_screen_text)


