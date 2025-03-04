# importing random library
import random

# defining the function for guessing the numbers
def guess_num(x):
    random_number=random.randint(1,x+1) # guessed the random number
    guess=0 # seted 0 so that we can continue guessing
    while guess != random_number: # continue guessing till right guess
        # input from the user
        guess=int(input(f"enter a number between 1 and {x}: "))
        # guessed greater
        if guess > random_number:
            print("guess is greater")
        # guessed smaller    
        elif guess < random_number:
            print("guess is smaller")
    # guessed right        
    print("you guessed correct!")

# calling the function 
num=int(input("Enter a number: "))
guess_num(num)