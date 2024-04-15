import random

print("Welcome to the Falls of Eternity. This is a simple RPG simulator written in Python."
      " You may choose from the following playable races:\n 1. Human\n 2. Elf\n 3. Dwarf")


class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


class Humans(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma):
        super().__init__(height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma)
        self.modify_attribute()

    def modify_attribute(self):
        attribute = input("Choose an attribute to add two points strength, dexterity, constitution, wisdom and charisma ")
        setattr(self, attribute, getattr(self, attribute) + 2)


class Elves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma):
        super().__init__(height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma)
        self.resistance_to_sleep = True
        self.dexterity += 2
        self.charisma += 2


class Dwarves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma):
        super().__init__(height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma)
        self.resistance_to_magic = True
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2


strength = random.randint(1,18)
dexterity = random.randint(1,18)
constitution = random.randint(1,18)
intelligence = random.randint(1,18)
wisdom = random.randint(1,18)
charisma = random.randint(1,18)

def characterCreation():
    while True:
        race = input("Choose a race (Human/Elf/Dwarf): ")
        if race.lower() in ["human", "elf", "dwarf"]:
            break
        else:
            print("Invalid race choice.")

    while True:
        height = input("Enter height (3-7 feet): ")
        if height.isdigit() and 3 <= int(height) <= 7:
            break
        else:
            print("Invalid height. Height should be between 3-7 feet.")

    while True:
        weight = input("Enter weight (60-300 pounds): ")
        if weight.isdigit() and 60 <= int(weight) <= 300:
            break
        else:
            print("Invalid weight. Weight should be between 60-300 pounds.")

    while True:
        hair_color = input("Enter hair color (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde): ")
        if hair_color.lower() in ["white", "black", "silver", "gray", "black", "brown", "green", "blue", "yellow", "pink", "red", "blonde"]:
            break
        else:
            print("Invalid hair color. Please choose from the given options.")

    while True:
        eye_color = input("Enter eye color (white, black, red, brown, green, blue, purple, amber): ")
        if eye_color.lower() in ["white", "black", "red", "brown", "green", "blue", "purple", "amber"]:
            break
        else:
            print("Invalid eye color. Please choose from the given options.")

    print("\nThese are your random attributes ")
    print("strength "+str(strength))
    print("dexterity "+str(dexterity))
    print("constitution "+str(constitution))
    print("wisdom "+str(wisdom))
    print("charisma "+str(charisma))


    if race.lower() == "human":
        character = Humans(height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma)
        print("Choose an attribute to add two points, strength, dexterity, constitution, wisdom and charisma ")
    elif race.lower() == "elf":
        character = Elves(height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,wisdom,charisma)
        print("Elves get a 100% Resistance to sleep and add 2 points to their Dexterity and Charisma scores.")
    elif race.lower() == "dwarf":
        character = Dwarves(height, weight, hair_color, eye_color,strength,dexterity,constitution,intelligence,
                 wisdom,charisma)
        print("Dwarfs get a 20% resistance to magic, add 2 bonus points to their strength and constitution, and deduct 2 points from their charisma.")
    else:
        print("Invalid race choice.")
        return

    print(f"\nYou have chosen the "+race+" clan, your traits are: ")
    print("Character Details:")
    print(f"Height: {character.height}")
    print(f"Weight: {character.weight}")
    print(f"Hair Color: {character.hair_color}")
    print(f"Eye Color: {character.eye_color}")
    print(f"Strength: {character.strength}")
    print(f"Dexterity: {character.dexterity}")
    print(f"Constitution: {character.constitution}")
    print(f"Intelligence: {character.intelligence}")
    print(f"Wisdom: {character.wisdom}")
    print(f"Charisma: {character.charisma}")


def main():
    characterCreation()


if __name__ == '__main__':
    main()
