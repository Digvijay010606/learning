# importing random library
import random

# defining the function for guessing the numbers
def guess_num(x):

    random_number=random.randint(1,x+1) # guessed the random number

    guess=0 # seted 0 so that it do not guess accidentally

    while guess != random_number: # continue guessing till right guess

        # input from the user
        guess=int(input(f"Enter a number between 1 and {x}: "))

        # guessed greater
        if guess > random_number:
            print("guess is high")
        
        # guessed smaller    
        elif guess < random_number:
            print("guess is low")
    
    # guessed right        
    print("you guessed correct!")

# inputing number from the user upto which you want to guess
num=int(input("Enter a number upto which you want to guess: "))

# calling the function
guess_num(num)