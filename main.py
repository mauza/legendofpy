import utils as u
from characters import Fighter, Mage, Monster
from stories import (
    Awakening
)

char_map = {
    1: Fighter,
    2: Mage,
    3: Monster
}

def character_choice():
    u.output("What type of champion are you?")
    u.output("1. Fighter")
    u.output("2. Mage")
    u.output("3. Monster")
    choice = u.ensure_choice(3)
    name = input("What is your name? ")
    character = char_map[choice](name)
    return character

def main():
    u.output("The Imaginary PY")
    character = character_choice()
    u.output(f"Hello {character}")
    u.output(f"You are a {type(character).__name__} ready to start your quest!")
    awakening_story = Awakening(character)
    awakening_story.start()

if __name__ == "__main__":
    main()


