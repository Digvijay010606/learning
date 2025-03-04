import random

print("LET THE COMPUTER GUESS THE NUMBER")
print("now guess any number")
start=input("start guessing from: ")
end=input("guess till: ")
while True:
    guess=random.randrange(start,end)
    answer=input("high,low,correct: ")
    if answer=="high":
        