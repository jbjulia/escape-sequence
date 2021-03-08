import sys

from PyQt5 import QtWidgets

from game import main

"""
EsCape Sequence is a fantasy RPG programmed entirely in Python and PyQt.
You can kill monsters, complete quests and obtain loot, all with a few
simple clicks. Your imagination is the limit, so let your adventure 
begin. Visit https://www.github/jbjulia/escape-sequence to find updates
and tips to download and begin your adventure.
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main.MainWindow()
    window.show()
    sys.exit(app.exec_())
    # menu.load()
