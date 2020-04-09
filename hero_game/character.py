#this is the top class of a character. All characters will begin
#with these basic properties.

class Character():
    def __init__(self, name, health=2, power=2):
        self.name = name
        self.health = health
        self.power = power


