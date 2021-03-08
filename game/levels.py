import os
import time
from random import randrange

from functions import functions


def level_one(char_name, char_race, char_class):
    options = [
        "[ a ] Accept",
        "[ d ] Decline"
    ]
    print("*You slowly regain consciousness*", end="\r", flush=True)
    time.sleep(3)
    print(functions.Style.BOLD + "Vortigern: " + functions.Style.END
          + functions.Style.CLEAR
          + "C'mon, " + char_name + ", get back up and brush the dirt off!", end="\r", flush=True)
    time.sleep(3)
    print(functions.Style.BOLD + "Vortigern: " + functions.Style.END
          + functions.Style.CLEAR
          + "I though you said you were a " + char_class
          + "! A " + char_race
          + " should be tougher than that!", end="\r", flush=True)
    time.sleep(3)
    print(functions.Style.BOLD + "Vortigern: " + functions.Style.END
          + functions.Style.CLEAR
          + "That's enough training for today, I'm sending you on a quest.\n")
    for option in options:
        print(option)
    listen("quest", input(functions.Style.NEWLINE), char_name)


def listen(l_type, player_input, char_name):
    if l_type == "quest":
        if player_input.lower() == "a":
            functions.clean_terminal()
            print(functions.Style.BOLD + "Quest Accepted: The High Lord's Gold" + functions.Style.END)
            os.system("notepad.exe data/quests/The-High-Lord's-Gold.md")
            functions.player_actions(char_name, quest=True)
            for char in functions.read_game_data()["characters"]:
                if char_name in char:
                    # health = char[char_name]["health"]
                    combat(char_name)


def combat(char_name):
    functions.clean_terminal()
    game_data = functions.read_game_data()
    for monster in game_data["monsters"]:
        while monster["Taro"]["health"] > 0:
            health = monster["Taro"]["health"]
            hit_splat = randrange(0, 999)
            if hit_splat > health:
                hit_splat = health
            damage = health - hit_splat
            time.sleep(2)
            print("You swing your sword and hit a " + str(hit_splat) + "!")
            monster["Taro"].update(health=damage)
            functions.write_game_data(game_data)
    victory(char_name)


def victory(char_name):
    game_data = functions.read_game_data()
    print(functions.Style.BOLD
          + "Congratulations "
          + char_name
          + "! You've defeated Red Dragon Taro!"
          + functions.Style.END)
    time.sleep(3)
    functions.clean_terminal()
    for char in functions.read_game_data()["characters"]:
        if char_name in char:
            reward = char[char_name]["gold"] + 100
            experience = char[char_name]["level"] + 1
            char[char_name].update(gold=reward, level=experience)
            functions.write_game_data(game_data)
    time.sleep(3)
    print("*Magic gathers around you, lifting your feet from the ground*", end="\r", flush=True)
    print(functions.Style.BOLD + "Vortigern: " + functions.Style.END
          + functions.Style.CLEAR
          + "Great job, " + char_name + ", thank you for returning with my gold!", end="\r", flush=True)
    time.sleep(3)
    print(functions.Style.BOLD + "Vortigern: " + functions.Style.END
          + functions.Style.CLEAR
          + "Kneel before me so that I can reward you.", end="\r", flush=True)
    time.sleep(3)
