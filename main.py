import sys

from art import end_text, logo
from hangman import hangman


def validate_user_choice(user_input):
    if user_input == 0 or user_input == 1:
        return True
    return False


def validate_game_choice(game_input):
    valid_inputs = [0, 1, 2]
    if game_input in valid_inputs:
        return True
    return False


def main_menu():
    """This function is to execute the program"""
    while True:
        user_choice = int(input("Press 1 to play games or 0 to exit \n"))
        if not validate_user_choice(user_choice):
            print("Invalid choice. Enter again: ")
        if user_choice == 0:
            print(end_text)
            print("Glad to see you. \n Warm regards :) ")
            sys.exit()
        while user_choice != 0:
            print(logo)
            if user_choice == 1:
                game_choice = int(
                    input(
                        "Press 1 to play Hangman\n"
                        "Press 2 to play Turtle crossing game\n"
                        "Press 0 to exit\n"
                    )
                )
                if game_choice == 1:
                    print("Welcome to the Hangman game")
                    hangman.run_hangman()

                elif game_choice == 2:
                    print("Welcome to the turtle crossing game")
                else:
                    print(end_text)
                    sys.exit("Glad to see you. \n Warm regards :)")


if __name__ == "__main__":
    main_menu()
