from random import randint
from art import logo

difficulty_level_easy = 10
difficulty_level_hard = 5

def check_answer(guess, answer, turns):
    """Checks answer againt guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too low. ")
        return turns -1
    else:
        print(f"You got it! The anser was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Typer 'easy' or 'hard': ")
    if level == "easy":
        return difficulty_level_easy
    else:
        return difficulty_level_hard

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attemtps remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose! ")
            return
        elif guess != answer:
            print("Guess again.")

game()


