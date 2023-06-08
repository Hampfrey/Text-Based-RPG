__version__ = '0.1.0'

# Imports
import classes
import random

# Functions
def broadcast(msg):
    return_choice = ""
    broadcast_complete = False
    while broadcast_complete == False:
        return_choice = input(msg)
        if return_choice == "X":
            exit()
        elif return_choice == "I":
            main.inventory()
        else:
            broadcast_complete = True
    return return_choice

def battle(enemy):
    broadcast(f"A {enemy.name} approached!")
    while enemy.health < 0:
        broadcast(f"They attack!...")
        main.health -= main.take_hit(enemy.give_hit)
        broadcast(f"You attack!...")
        enemy.health -= enemy.take_hit(main.give_hit)
    
        


# Scenes
def intro():
    choice = broadcast(f"You wake up, it's dark...")
    choice = broadcast(f"There seems to be a strange light pulsing outside your dull wooden door...")
    choice = broadcast(f"Check out the light? (y/n): ")
    wizard_mood = choice
    if choice == "n":
        broadcast(f"You ignore the light and go back to sleep...")
        broadcast(f"Not long after, you wake again, there's a pounding at your door...")
        broadcast(f"Before you can even climb out of bed, the door flies open, an old looking mage cloaked in white angrily wispers to you...")
        broadcast(f"\"Move you Fool! They're coming! Grab what you can you need to move!...\"")
        prompt = "Grab what you can!..."
    else:
        print(f"You crawl out of your admittedly uncomfortable bed.")
        prompt = "You might want to find your stuff first though..."

    choice_check = False
    while choice_check == False:
        print(prompt)
        print(f"    1: BEDSIDE")
        print(f"    2: CREAKY OLD TABLE")
        print(f"    3: DOOR")
        choice = broadcast("Look by?: ")

        # Candle
        if choice == "1":
            if main.in_inventory("OLD CANDLE"):
                broadcast(f"There is nothing here...")
            else:
                broadcast(f"You find your OLD CANDLE, it needs to be replaced, but it works...")
                main.inv.append(classes.Item("OLD CANDLE", "A flimsy old candle, the wick is nearly burnt through, but it's got a few hours left.", 0, 4))

        # Basket
        if choice == "2":
            if "BASKET STICK" in main.inv:
                broadcast(f"There is nothing here...")
            else:
                broadcast(f"You find you BASKET STICK, you typically use it for carrying your grocreies home, plus it makes you feel like a cool forest witch...")
                main.inv.append(classes.Item("BASKET STICK", "A stick with a basket attached, it certainly isn't made for it but it can fight off a couple raccoons at least.", 1, 0))

        # Cloak
        if choice == "3":
            if "OLD CLOAK" in main.inv:
                broadcast(f"There is nothing here...")
            else:
                broadcast(f"You find your OLD CLOAK, it's a hand down from your elder sister, when she went off to war they gave her a uniform and she gave you this...")
                main.inv.append(classes.Item("OLD CLOAK", "More or less a piece of leather thrown over your shoulders, it still works though.", 1, 2))
        if len(main.inv) == 5:
            choice_check = True
    if wizard_mood == "y":
        broadcast(f"You open your door and find a tall mage cloaked in white, they talk in a wisper...")
        broadcast(f"\"Hello {main.name}, I'm sorry for the hour but you need to leave and now...\"")
        broadcast(f"\"The LORD and his guard have tampered with the record and are coming to loot your home, I doubt you'd survive if you stay...\"")
    if wizard_mood == "n":
        broadcast(f"Once you've got your things the mage ushers you out the door quickly...")
        broadcast(f"\"You don't have much time {main.name}, the LORD and his guard have done their shenanigans with the record and are coming here NOW!...\"")
        broadcast(f"\"I fear you would not survive if you stay here\"")
    broadcast(f"\"Leave for Brikleborough, I've sent an owl to the INN KEEP to inform her of the situation, there you should find shelter and further direction...\"")
    broadcast(f"\"That dastardly LORD falsly convicted you an a few others of treasonary witchcraft, he wants to take all he can to fuel his expansion...\"")
    broadcast(f"\"I have business to attend to first, but I'll meet you there when I can, although don't expect me to look like this, I will be in civil cloth and go by the name of WHITTLEMAN...\"")
    broadcast(f"\"WHITTLEMAN will have my beard, but he'll be shorter and have my elvish ears hidden...\"")
    broadcast(f"\"Now you must leave!...\"")
    broadcast(f"----------------------------------------")

# Dark Trail
def dark_trail():
    broadcast(f"You got moving quickly the trail is dark but you can see in the moonlight...")
    battle(classes.Enemy(5, 2, 0, classes.Item("BONE", "A bone from something, it works as a weapon I guess.", 2, 0)))

# Start Game
input_name = broadcast(f"A girl is sleeping in her cottage, she starts to stir... What is her name?: ")
main = classes.Character(input_name, 1)
intro()
dark_trail()
