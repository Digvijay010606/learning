import random

def play():

    choices = ['r','p','s']

    while True:

        computer = random.choice(choices)

        player = input("Enter your choice (r = rock | p = paper | s = scissor): ").lower()

        if player ==  computer:
            print("tie")

        elif ((player == 'r' and computer == 's') or (player == 'p'  and computer == 'r') or (player == 's' and computer == 'p')):
            print("you win")

        else:
            print("you loss")

        again = input("do you want to play again (y/n): ")
        if again != 'y':
            break

if __name__ == '__main__':
    play()
