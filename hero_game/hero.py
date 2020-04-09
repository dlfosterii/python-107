#this is the Hero character class.
#it will inherit the characteristics of Character

from character import Character

class Hero(Character):
    def __init__(self, name, health=10, power=5):
        self.name = name
        self.health = health
        self.power = power




