__version__ = '0.1.0'

# Imports
import character
import scenes 
import item
import random

# Start Game
input_name = input(f"A girl is sleeping in her cottage, she starts to stir... What is her name?: ")
main = character.Character(input_name, 1)
scenes.Scene.intro()