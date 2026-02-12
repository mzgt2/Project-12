import random
from art import logo
print(logo)
game_over = False
#guesses = []
attempts = 0
while not game_over:
    start = input("""Welcome to the Number Guessing Game!
I\'m thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """).lower()
    computer_guess = 0
    random_num = random.randint(1,100)
    computer_guess += random_num
    if start == 'easy':
        attempts = 10

    elif start == 'hard':
        attempts = 5
    else:
        print("Invalid input, please enter either 'easy' or 'hard'.")
        continue
    while attempts > 0:
        raw_guess = input("Make a guess: ")
        if not raw_guess.isdigit():
            print("Invalid input, please guess a whole number.")
            continue
        guess = int(raw_guess)
        if guess < computer_guess:
            attempts -= 1
            print(f"Too low.\nGuess again.\nYou have {attempts} remaining to guess the number.")
            continue
        elif guess > computer_guess:
            attempts -= 1
            print(f"Too high.\nGuess again.\nYou have {attempts} remaining to guess the number.")
            continue
        elif guess == computer_guess:
            game_over = True
            print(f"You guessed correct! The random number was {computer_guess}.")
            break

    if attempts == 0:
        print(f"You have run out of attempts the random number was {computer_guess}.")
        rerun = input("Do you want to try again? Enter 'yes' or 'no'. ").lower()
        if rerun == 'yes':
            continue
        else:
            game_over = True
            print("Until next time, see ya!")
