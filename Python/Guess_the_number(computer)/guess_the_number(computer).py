import random

x = int(input("enter the number upto which computer will guess: "))

low = 1
high = x+1

ans = input("enter answer(s-start): ")

while ans != 'c':
    guess = random.randint(low,high)
    print(guess)
    ans = input("enter answer(c-correct, l-low, h-high): ")
    if ans == 'l':
        low = guess+1
    elif ans == 'h':
        high = guess
print("you guessed correct")    