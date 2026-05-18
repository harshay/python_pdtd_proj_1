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
    
    
#   2. Store a random number as the answer/solution.
    answer = random.randint(1,10)
    print(answer)  
    
    guess_count = 0

#   3. Continuously prompt the player for a guess.
    while True:             

        player_guess = int(input("Enter your guess "))
        print("your guess is",player_guess) 
        guess_count = guess_count + 1
        print("Your total guesses are ",guess_count)

        if player_guess > answer:
            print("It's Lower")   
        elif player_guess < answer:
            print("It's Higher")
        else:
            print("You got the answer in ",guess_count," guesses! The game will now end.")
            break

                                 
start_game()