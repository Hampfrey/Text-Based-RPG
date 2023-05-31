# Imports
import random

# Character
class Character:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = int(lvl)
        self.inv = []

    def __str__(self):
        return f"{self.name}({self.lvl})"
    
    def increase_level(self):
        self.lvl += 1
        print(str(self.lvl))

    def decrease_level(self):
        self.lvl -= 1

    def inventory(self):
        print("Inventory")
        length = len(self.inv)
        i = 0
        while i < length:
            print("- " + str(self.inv[i]))
            i += 1
    
    def in_inventory(self, item):
        length = len(self.inv)
        i = 0
        return_val = False
        while i < length:
            if item == str(self.name[i]):
                return_val = True
        return return_val
                

# Items
# Types,
#   0 : Melee
#   1 : Bow
#   2 : Armor
#   3 : Consumable
#   4 : Other
    
class Item:
    def __init__(self, name, description, value, type):
        self.name = name
        self.description = description
        self.value = value
        self.type = type
    
    def __str__(self):
        return f"{self.name}"