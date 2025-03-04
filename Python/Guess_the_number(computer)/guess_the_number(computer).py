# importing random library
import random

# inputing number from user upto which computer will guess
x = int(input("Enter the number upto which computer will guess: "))

# setting low and high values for the guess
low = 1
high = x+1

# starting the game
ans = input("enter answer(s-start): ").lower()

# checking if user entered s for start or not
if ans == "s":

    # running loop till user enter c for correct answer
    while ans != 'c':
        
        # guessing random number in range
        guess = random.randint(low,high)

        print(guess) # printing guessed number

        ans = input("Enter answer(c-correct, l-low, h-high): ").lower() # inputing answer from the user

        # low guess
        if ans == 'l':
            low = guess+1 # increasing low value to upper value of the guess
        
        # high guess
        elif ans == 'h':
            high = guess # decrasing high value to guess

    # printing when guessed correctly        
    print("Finally guessed correct")
    
else:
    print("You didn't entered s!")