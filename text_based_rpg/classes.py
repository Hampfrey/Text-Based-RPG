# Imports
import random

# Character
class Character:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = int(lvl)
        self.inv = [Item("Hand", "It's your hand.", 1, 0), Item("Clothes", "Basicly just some rags sewn together.", 0, 2)]
        self.health = 10
        self.defense = 0
        self.attack = 0
        self.selected_weapon = 0
        self.selected_armor = 1

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
            print(f"    {i}: " + str(self.inv[i]))
            i += 1
        read = int(input("Look at?: "))
        if read >= 0 and read < len(self.inv):
            self.inv[read].analyze()
    
    def in_inventory(self, item):
        length = len(self.inv)
        i = 0
        return_val = False
        while i < length:
            print(str(self.inv[i]))
            if item == str(self.inv[i]):
                return_val = True
            i += 1
        return return_val
    
    def give_hit(self):
        
        return self.attack + self.inv[self.selected_weapon].value
    
    def take_hit(self, damage):
        damage -= self.defense - self.inv[self.selected_armor].value
        if damage < 0:
            print("You take no damage!")
            return 0
        else:
            print(f"You take {damage} damage!")
            return damage
    

        

                

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
    
    def analyze(self):
        print(f"{self.name}")
        print(f"- {self.description}")
        msg = "Undef: "
        if self.type == 0 or 1:
            msg = "Attack"
        if self.type == 2:
            msg = "Defense"
        if self.type == 3:
            msg = "Consume Value"
        if self.type == 4:
            msg = "Value"
        print(f"- {msg}: {self.value}")

class Enemy:
    def __init__(self, name, health, attack, defense, loot):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.loot = loot
    
    def give_hit(self):
        return self.attack
    
    def take_hit(self, damage):
        damage -= self.defense
        if damage < 0:
            print("It deals no damage!")
            return 0
        else:
            print(f"It deals {damage} damage!")
            return damage

