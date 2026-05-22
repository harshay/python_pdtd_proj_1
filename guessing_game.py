"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random 

# Create the start_game function.
def start_game():    


#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
    print("Hey! Welcome to the Guessing Game! Choose a number between 1 and 10")
    
    last_guess_count = 999999999
    
#   2. Store a random number as the answer/solution.    

    while True:

        answer = random.randint(1,10)
        guess_count = 0


#   3. Continuously prompt the player for a guess.
        while True:             
            
            try:            
                player_guess = int(input("Enter your guess "))
                if player_guess < 1 or player_guess > 10:
                    print("oops! you guess needs to be a number between 1 and 10. Try again.")
            except ValueError: 
                print("oh no! we ran into an issue. Please try again. Enter numbers only")
            else: 
                print("your guess is",player_guess) 
                guess_count = guess_count + 1
                print("Your total guesses are ",guess_count," ")

                if player_guess > answer:
                    print("It's Lower")   
                elif player_guess < answer:
                    print("It's Higher")
                else:
                    print("You got the answer in ",guess_count," guesses!")
                    break

        play_again_val = input("do you want to play again? Enter Yes if you want to play again, No if you don't ") 

        if play_again_val.lower() == 'no':
            print("The game will now end. Goodbye!")
            break 
            
        else:
            if guess_count < last_guess_count:
                last_guess_count = guess_count
                print("your best score in this game is ",last_guess_count)

start_game()