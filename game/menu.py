import json
import os
import sys
import time

from functions import functions
from game import game


def load(delay=True):
    try:
        width = os.get_terminal_size().columns
        with open("data/game_data.json") as in_file:
            data = json.load(in_file)
        print(functions.Style.BOLD + data["welcome"].center(width) + functions.Style.END)
        if delay:
            time.sleep(2)
        menu(data)
    except(IOError, OSError):
        sys.exit(1)


def menu(data):
    menu_items = [
        "[ p ] Play",
        "[ n ] New Game",
        "[ h ] Hints",
        "[ t ] Tools",
        "[ q ] Quit"
    ]
    print(functions.Style.UNDERLINE + functions.Style.BOLD + "Menu" + functions.Style.END)
    for item in menu_items:
        print(item)
    listen(data, input(functions.Style.NEWLINE))


def listen(data, player_input):
    try:
        if player_input.lower() == "p":
            functions.clean_terminal()
            try:
                game.load_game(input(data["login"]))
            except KeyError:
                print(data["exists_error"])
                load(delay=False)
                listen(data, input())
        elif player_input.lower() == "n":
            functions.clean_terminal()
            game.create_character()
        elif player_input.lower() == "h":
            # game.load_hints()
            return
        elif player_input.lower() == "t":
            # functions.load_tools()
            return
        elif player_input.lower() == "q":
            print(data["quit"])
            sys.exit(0)
        else:
            functions.clean_terminal()
            load(delay=False)
            listen(data, input())
    except ValueError:
        print(data["game_error"])
        sys.exit(1)
