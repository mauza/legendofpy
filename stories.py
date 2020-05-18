import utils as u


class Story():

    def __init__(self, character):
        self.character = character


class Awakening(Story):

    def start(self):
        self.beginning()
        self.woods()

    def beginning(self):
        u.output("This is the Link's Awakening Story!")
        u.output(".")
        u.output(".")
        u.output(".")
        u.output("You are in the enchanted forest.")

    def woods(self):
        choice = u.question(
            "What do you want to do next?",
            ["Fight monsters", "Go exploring", "Follow that intersting tinkling noise"]
        )
        if choice == 1:
            self.fight_monsters()
        elif choice == 2:
            self.explore()
        elif choice == 3:
            self.go_to_village()
        else:
            self.disaster()

    def fight_monsters(self):
        pass
