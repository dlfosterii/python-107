#this is the Goblin class.
#it will be a sub-class of the Character class

from character import Character

class Goblin(Character):
    def __init__(self, name, health=6, power=2):
        self.name = name
        self.health = health
        self.power = power



