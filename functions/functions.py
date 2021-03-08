import json
import os


class Style:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    ITALICS = "\033[3m"
    UNDERLINE = "\033[4m"
    NEWLINE = "\n> "
    CLEAR = "\033[K"
    END = "\033[0m"


def clean_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    os.system("mode con: cols=120 lines=30")
    print('\33]0;EsCape Sequence - v1.0\a', end='', flush=True)


def read_game_data():
    with open("data/game_data.json", "r") as in_file:
        game_data = json.load(in_file)
    return game_data


def write_game_data(game_data):
    with open("data/game_data.json", "w") as out_file:
        json.dump(game_data, out_file, indent=4, sort_keys=True)


def player_actions(char_name, quest=False):
    actions = [
        "[ q ] Attack",
        "[ w ] Walk Forward",
        "[ a ] Walk Left",
        "[ s ] Walk Back",
        "[ d ] Walk Right",
        "[ p ] Open Pack",
        "[ x ] Exit Game"
    ]
    if not quest:
        clean_terminal()
    for char in read_game_data()["characters"]:
        if char_name in char:
            level = str(char[char_name]["level"])
            health = str(char[char_name]["health"])
            print(Style.BOLD + char_name + " | Level: " + level + " | Health " + health + Style.END + "\n")
    for action in actions:
        print(action)
    return input(Style.NEWLINE).lower()
