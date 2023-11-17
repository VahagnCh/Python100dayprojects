import random
from hangman_words import  word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6
end_of_game = False

print(logo)
#Testing code
#print(f"Pssst, the solution is {chosen_word}.")

#To show all the guesses 
inputs = []

display = []
for _ in range (word_lenght):
    display += "_"
    
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    inputs.append(guess)

    if guess in display:
        print(f"You have already guessed {guess}")

    #Checks guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    #Prints lives 
    if guess not in chosen_word:
        print(f"You guessed {guess} that is not in the word, also: {','.join(inputs)}. You lose a life.")
        lives -= 1
        print(guess)
        if lives == 0:
            end_of_game = True
            print(f"You lose, the word was {chosen_word}")
            
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f"You win! The word is {chosen_word}")
        
    print(stages[lives])