import random
from colorama import init, Fore, Style, Back
import os

init() # Initialize colorama

def user():
    while True:
        try:
            print(Fore.YELLOW + "="*60 + Fore.RESET)
            print(Fore.CYAN + "USER GUESS THE NUMBER".center(60,'~') + Fore.RESET)
            print(Fore.YELLOW + "="*60 + Fore.RESET)
            
            min_val = int(input("\n\nEnter minimum guess: "))
            max_val = int(input("\nEnter maximum guess: "))
            
            if min_val >= max_val:
                print(Fore.RED + "\nMinimum must be less than maximum!" + Fore.RESET)
                continue
                
            random_number = random.randint(min_val, max_val)
            while True:
                try:
                    guess = int(input("\nEnter your guess: "))
                    if guess > random_number:
                        print(Fore.GREEN + "\nYou guessed high" + Fore.RESET)
                    elif guess < random_number:
                        print(Fore.GREEN + "\nYou guessed low" + Fore.RESET)
                    else:
                        print(Fore.GREEN + "\nYou guessed correct" + Fore.RESET)
                        return
                except ValueError:
                    print(Fore.RED + "\nPlease enter a valid number!" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "\nPlease enter valid numbers!" + Fore.RESET)

def computer():
    while True:
        try:
            print(Fore.YELLOW + "="*60 + Fore.RESET)
            print(Fore.CYAN + "COMPUTER GUESS THE NUMBER".center(60,'~') + Fore.RESET)
            print(Fore.YELLOW + "="*60 + Fore.RESET)
            
            min_val = int(input("\n\nEnter minimum guess: "))
            max_val = int(input("\nEnter maximum guess: "))
            
            if min_val >= max_val:
                print(Fore.RED + "\nMinimum must be less than maximum!" + Fore.RESET)
                continue
                
            while True:
                guess = random.randint(min_val, max_val)
                print(f"\nComputer guesses: {guess}")
                ans = input(Fore.GREEN + "\nEnter c = correct / l = low / h = high: " + Fore.RESET).lower()
                
                if ans in ['c', 'l', 'h']:
                    if ans == 'c':
                        print(Fore.GREEN + "\nComputer finally guessed correct" + Fore.RESET)
                        return
                    elif ans == 'l':
                        min_val = max(min_val, guess + 1)
                    elif ans == 'h':
                        max_val = min(max_val, guess - 1)
                    
                    if min_val > max_val:
                        print(Fore.RED + "\nInconsistent answers detected!" + Fore.RESET)
                        break
                else:
                    print(Fore.RED + "\nPlease enter c, l, or h only!" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "\nPlease enter valid numbers!" + Fore.RESET)

def main():
    while True:
        os.system('cls')
        print(Fore.YELLOW + "="*60 + Fore.RESET)
        print(Fore.CYAN + "GUESS THE NUMBER GAME".center(60,'~') + Fore.RESET)
        print(Fore.YELLOW + "="*60 + Style.RESET_ALL)
        print(Fore.CYAN + "\n\n1. USER \n\n2. COMPUTER\n\n" + Fore.RESET)
        
        try:
            game = int(input("Enter which one to choose (1/2): "))
            os.system('cls')
            
            if game == 1:
                user()
            elif game == 2:
                computer()
            else:
                print(Fore.RED + "\nPlease enter 1 or 2 only!" + Fore.RESET)
                continue
                
            while True:
                again = input(Fore.GREEN + "\n\nWould you like to play again (yes/no): " + Fore.RESET).lower()
                if again in ['yes', 'no']:
                    if again == 'no':
                        print(Fore.YELLOW + "\nThanks for playing!" + Fore.RESET)
                        return
                    break
                else:
                    print(Fore.RED + "\nPlease enter yes or no only!" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "\nPlease enter a valid number!" + Fore.RESET)

if __name__ == "__main__":
    main()