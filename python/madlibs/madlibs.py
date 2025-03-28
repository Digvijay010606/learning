# madlibs game

from colorama import init, Fore, Style
import os
import random

init()  # Initialize colorama

stories = [
    "The {adjective} {noun} loved to {verb} in {place}.",
    "In {place}, a {adjective} {noun} started to {verb}.",
    "A {adjective} {noun} was seen {verb}ing near {place}."
]

while True:
    os.system('cls')
    print(Fore.GREEN + "Welcome to the Madlib Game!\n" + Style.RESET_ALL)
    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    
    story = random.choice(stories).format(
        noun=noun, verb=verb, adjective=adjective, place=place
    )
    
    print("\n" + Fore.YELLOW + "="*60 + Style.RESET_ALL)
    print(Fore.CYAN + " Your Madlib Story ".center(60, "~") + Style.RESET_ALL)
    print(Fore.YELLOW + "="*60 + Style.RESET_ALL)
    print(story)
    print(Fore.YELLOW + "="*60 + Style.RESET_ALL)
    
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print(Fore.GREEN + "\nThanks for playing!" + Style.RESET_ALL)
        break