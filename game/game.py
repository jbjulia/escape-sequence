import sys
import time

from functions import functions
from game import levels


def create_character(character_name, character_race):
    try:
        """
        char_name = str(input("Please enter your desired player name: ")).title()
        char_race = str(input("What race would you like to play as [Human, Elf, Orc, Troll]: ")).title()
        char_class = str(input("What class would you like to master [Warrior, Mage, Archer, Monk]: ")).title()
        """
        game_data = functions.read_game_data()
        for char in game_data["characters"]:
            if character_name in char:
                return KeyError
        game_data["characters"].append(
            {
                character_name: {
                    "race": character_race,
                    "level": 1,
                    "health": 100,
                    "gold": 25
                }
            }
        )
        functions.write_game_data(game_data)
        # load_game(char_name)
    except ValueError:
        sys.exit(1)


def load_game(char_name):
    functions.clean_terminal()
    for char in functions.read_game_data()["characters"]:
        if char_name in char:
            level = char[char_name]["level"]
            char_race = char[char_name]["race"]
            char_class = char[char_name]["class"]
            load_level(level, char_name, char_race, char_class)


def load_level(level, char_name, char_race, char_class):
    functions.clean_terminal()
    print("Welcome, "
          + functions.Style.BOLD + char_name.title()
          + functions.Style.END + ", let your adventure begin...\n")
    time.sleep(2)
    if level == 1:
        levels.level_one(char_name, char_race, char_class)
