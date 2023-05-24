__version__ = '0.1.0'

# Imports
import character
import random

# Functions
def broadcast(msg):
    return_choice = ""
    broadcast_complete = False
    while broadcast_complete == False:
        return_choice = input(msg)
        if return_choice == "EXIT":
            exit()
        elif return_choice == "I":
            print(character.Inventory)
        else:
            broadcast_complete = True
    return return_choice

# Scenes
def intro():
    choice = broadcast(f"You wake up, it's dark...")
    choice = broadcast(f"There seems to be a strange light pulsing outside your dull wooden door...")
    choice = broadcast(f"Check out the light? (y/n): ")
    if choice == "y":
        print(f"You crawl out of your admittedly uncomfortable bed.")
        choice_check = False
        while choice_check == False:
            print(f"You might want to find your stuff first though...")
            print(f"    1: BEDSIDE")
            print(f"    2: CREAKY OLD TABLE")
            print(f"    3: DOOR")
            choice = broadcast("Look by?: ")

            # Candle
            if choice == "1":
                if "OLD CANDLE" in main.inv:
                    broadcast(f"There is nothing here...")
                else:
                    choice = broadcast(f"You find your OLD CANDLE, it needs to be replaced, but it works...")
                    main.inv.append("OLD CANDLE")

            # Basket
            if choice == "2":
                choice = input(f"You find you BASKET STICK, you typically use it for carrying your grocreies home, plus it makes you feel like a cool forest witch...")

            # Cloak
            if choice == "3":
                choice = input(f"You find your OLD CLOAK, it's a hand down from your elder sister, when she went off to war they gave her a uniform and she gave you this...")

# Start Game
input_name = broadcast(f"A girl is sleeping in her cottage, she starts to stir... What is her name?: ")
main = character.Character(input_name, 1)
intro()
