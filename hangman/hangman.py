import random
import sys
from .hangman_art import stages, logo
from .hangman_words import word_list


def play_hangman():
    # choose a random word from the list of words
    chosen_word = random.choice(word_list)
    # extracting length of the word
    word_length = len(chosen_word)
    # variable to determine if user has guessed all the letters
    end_of_game = False
    lives = 6
    # Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print(f"You've already guessed {guess}")
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"{guess} not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        # print the art figures to indicate different stages
        print(stages[lives])


def run_hangman():
    user_choice_game1 = int(input("Enter 1 to continue\n"
          "Enter 0 to exit\n"
          "Enter any other key to return to main\n"))
    if user_choice_game1 == 0:
        sys.exit("Thank you for playing. \n Warm regards :)")
    elif user_choice_game1 == 1:
        # printing logo at the start of the game
        print(logo)
        play_hangman()
    else:
        return


if __name__ =="__main__":
    run_hangman()
