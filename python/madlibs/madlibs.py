import random
import os
import time
from colorama import init, Fore

init()

stories = {
    1: f"The {{adjective}} {{noun}} loved to {{verb}} in {{place}}.",
    2: f"In {{place}}, a {{adjective}} {{noun}} started to {{verb}}.",
    3: f"A {{adjective}} {{noun}} was seen {{verb}}ing near {{place}}."
}

stories_no = [1, 2, 3]

while True:
    os.system('cls')
    print(Fore.GREEN + "Welcome to the Madlib Game!\n\n" + Fore.RESET)

    adjective = input("(Word: 1 / 4)Enter an adjective: ")
    noun = input("(Word: 2 / 4)Enter a noun: ")
    verb = input("(Word: 3 / 4)Enter a verb: ")
    place = input("(Word: 4 / 4)Enter a place: ")

    story_number = random.choice(stories_no)
    story = stories[story_number].format(adjective=adjective, noun=noun, verb=verb, place=place)

    print("\n" + Fore.YELLOW + "=" * 60 + Fore.RESET)
    print(Fore.CYAN + " Your Madlib Story ".center(60, "~") + Fore.RESET)
    print(Fore.YELLOW + "=" * 60 + Fore.RESET)
    print(story)
    print(Fore.YELLOW + "=" * 60 + Fore.RESET)

    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print(Fore.GREEN + "Thanks for playing!" + Fore.RESET)
        break