
class Character():
    max_health = 100
    current_health = 100
    strength = 10
    energy = 10
    dexterity = 10

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def attack_damage(self):
        return self.strength*2


class Fighter(Character):

    def __init__(self, name):
        self.max_health += 10
        self.strength += 10
        self.dexterity += 5
        super(Fighter, self).__init__(name)

class Mage(Character):

    def __init__(self, name):
        self.max_health += 5
        self.energy += 15
        self.dexterity += 5
        super(Mage, self).__init__(name)

class Monster(Character):

    def __init__(self, name):
        self.max_health += 15
        self.strength += 15
        self.dexterity += 5
        self.energy -= 15
        super(Monster, self).__init__(name)
