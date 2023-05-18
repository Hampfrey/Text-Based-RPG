# Classes
class Character:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = int(lvl)

    def __str__(self):
        return f"{self.name}({self.lvl})"
    
    def increase_level(self):
        self.lvl += 1
        print(str(self.lvl))