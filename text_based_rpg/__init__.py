__version__ = '0.1.0'

# Imports
import classes
import random

# Start Game
input_name = input(f"A girl is sleeping in her cottage, she starts to stir... What is her name?: ")
main = classes.Character(input_name, 1)
choice = input(f"You wake up, it's dark")
choice = input(f"There seems to be a strange light pulsing outside your dull wooden door...")
choice = input(f"Check out the light? (y/n): ")
if choice == "y":
    print(f"You crawl out of your admittedly uncomfortable bed.")
    print(f"You might want to find your stuff first though...")
    print(f"    1: BEDSIDE")
    print(f"    2: CREAKY OLD TABLE")
    print(f"    3: DOOR")
    choice = input("Look by?: ")
    if choice == 1:
        choice = input(f"You find your OLD CANDLE, it needs to be replaced, but it works...")
    if choice == 2:
        choice = input(f"You find you BASKET STICK, you typically use it for carrying your grocreies home, plus it makes you feel like a cool forest witch...")
    if choice == 3:
        choice = input(f"You find your OLD CLOAK, it's a hand down from your elder sister, when she went off to war they gave her a uniform and she gave you this...")