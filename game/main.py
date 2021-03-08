import os
import sys

import pygame
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGraphicsOpacityEffect

from functions import functions
from game import styles


def quit_game():
    """
    Clear all events and quit application.
    :return:
    """
    sys.exit()


def load_music(track, running=False):
    """
    Initialize PyGame mixer to play game soundtrack on loop.
    :return:
    """
    if not running:
        pygame.init()
        pygame.mixer.init()
    pygame.mixer.music.load(os.path.abspath(track))
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(loops=-1)
    volume = pygame.mixer.music.get_volume()
    while volume < 0.35:
        volume += 0.00001
        pygame.mixer.music.set_volume(volume)


def play_sound(sound):
    """
    Initialize PyGame Mixer and play sound effect.
    :param sound:
    :return:
    """
    sound_effect = pygame.mixer.Sound(os.path.abspath(sound))
    sound_effect.play()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/escape-sequence.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.effect = None
        self.animation = None
        self.character_name = None
        self.character_race = None
        self.widgets_list = [
            "lblCompass",
            "lblGP",
            "btnGold",
            "lblName",
            "btnCharacter",
            "lblLevel",
            "lblHP",
            "btnHealth",
            "btnExit",
            "btnBack",
            "btnNext",
            "btnMelee",
            "btnMagic",
            "btnRange",
            "btnEscape",
            "btnUp",
            "btnDown",
            "btnLeft",
            "btnRight",
            "btnMap"
        ]
        self.setup_ui()
        self.map_buttons()

    def map_buttons(self):
        """
        Map QPushButtons with respective functions.
        :return:
        """
        self.btnPlayNow.clicked.connect(self.load_saved_game)
        self.btnNewUser.clicked.connect(self.new_user)
        self.btnSettings.clicked.connect(self.settings)
        self.btnExit.clicked.connect(self.setup_ui)
        self.btnQuit.clicked.connect(quit_game)
        self.btnGold.clicked.connect((lambda: play_sound("music/sounds/gold.wav")))
        self.btnHealth.clicked.connect((lambda: play_sound("music/sounds/heartbeat.wav")))
        self.btnMelee.clicked.connect(lambda: play_sound("music/sounds/melee.wav"))
        self.btnMagic.clicked.connect(lambda: play_sound("music/sounds/magic.wav"))
        self.btnRange.clicked.connect(lambda: play_sound("music/sounds/range.wav"))
        self.btnEscape.clicked.connect(lambda: play_sound("music/sounds/escape.wav"))
        self.btnBack.clicked.connect(lambda: self.turn_page("back"))
        self.btnNext.clicked.connect(lambda: self.turn_page("next"))
        self.btnMap.clicked.connect(lambda: play_sound("music/sounds/map.wav"))
        self.btnOrc.clicked.connect(lambda: self.select_character("orc"))
        self.btnElf.clicked.connect(lambda: self.select_character("elf"))
        self.btnGoblin.clicked.connect(lambda: self.select_character("goblin"))
        self.btnDwarf.clicked.connect(lambda: self.select_character("dwarf"))
        self.btnTroll.clicked.connect(lambda: self.select_character("troll"))
        self.btnMusic.clicked.connect(lambda: self.toggle_button("music"))
        # self.btnSoundEffects.clicked.connect(lambda: self.toggle_button("sound-effects"))
        # self.btnLanguageFilter.clicked.connect(lambda: self.toggle_button("language-filter"))
        # self.btnCheats.clicked.connect(lambda: self.toggle_button("cheats"))

    def setup_ui(self):
        """
        Set QStackedWidget default index and hide irrelevant buttons.
        :return:
        """
        self.stackedWidget.setCurrentIndex(0)
        self.btnOrc.setStyleSheet(styles.normal_style)
        self.btnElf.setStyleSheet(styles.normal_style)
        self.btnGoblin.setStyleSheet(styles.normal_style)
        self.btnDwarf.setStyleSheet(styles.normal_style)
        self.btnTroll.setStyleSheet(styles.normal_style)
        for widget in self.centralwidget.children():
            if widget.objectName() in self.widgets_list:
                widget.setVisible(False)
        self.fade_in(self.centralWidget())
        load_music("music/Heroic-Minority.mp3")

    def load_saved_game(self):
        self.stackedWidget.setCurrentIndex(1)
        self.btnExit.setVisible(True)
        self.btnBack.setVisible(True)
        self.btnNext.setVisible(True)
        self.btnOrc.setEnabled(False)
        self.btnElf.setEnabled(False)
        self.btnGoblin.setEnabled(False)
        self.btnDwarf.setEnabled(False)
        self.btnTroll.setEnabled(False)
        self.lblOrc.setText("Empty")
        self.lblElf.setText("Empty")
        self.lblGoblin.setText("Empty")
        self.lblDwarf.setText("Empty")
        self.lblTroll.setText("Empty")
        self.lblCharacterRace.setText("Please select your character:")
        for char in functions.read_game_data()["characters"]:
            for name in char.keys():
                if char[name]["race"] == "orc":
                    self.btnOrc.setEnabled(True)
                    self.lblOrc.setText(name)
                elif char[name]["race"] == "elf":
                    self.btnElf.setEnabled(True)
                    self.lblElf.setText(name)
                elif char[name]["race"] == "goblin":
                    self.btnGoblin.setEnabled(True)
                    self.lblGoblin.setText(name)
                elif char[name]["race"] == "dwarf":
                    self.btnDwarf.setEnabled(True)
                    self.lblDwarf.setText(name)
                elif char[name]["race"] == "troll":
                    self.btnTroll.setEnabled(True)
                    self.lblTroll.setText(name)

    def new_user(self):
        """
        Change QStackedWidget index to character creation page.
        :return:
        """
        self.stackedWidget.setCurrentIndex(1)
        self.btnExit.setVisible(True)
        self.btnBack.setVisible(True)
        self.btnNext.setVisible(True)
        self.btnOrc.setEnabled(True)
        self.btnElf.setEnabled(True)
        self.btnGoblin.setEnabled(True)
        self.btnDwarf.setEnabled(True)
        self.btnTroll.setEnabled(True)
        self.btnOrc.setStyleSheet(styles.normal_style)
        self.btnElf.setStyleSheet(styles.normal_style)
        self.btnGoblin.setStyleSheet(styles.normal_style)
        self.btnDwarf.setStyleSheet(styles.normal_style)
        self.btnTroll.setStyleSheet(styles.normal_style)
        self.lblOrc.setText("ORC")
        self.lblElf.setText("ELF")
        self.lblGoblin.setText("GOBLIN")
        self.lblDwarf.setText("DWARF")
        self.lblTroll.setText("TROLL")

    def turn_page(self, action):
        """
        Get current index of QStackedWidget and switch accordingly.
        :param action:
        :return:
        """
        index = self.stackedWidget.currentIndex()
        if action == "next":
            if index == 0:
                self.btnOrc.setStyleSheet(styles.normal_style)
                self.btnElf.setStyleSheet(styles.normal_style)
                self.btnGoblin.setStyleSheet(styles.normal_style)
                self.btnDwarf.setStyleSheet(styles.normal_style)
                self.btnTroll.setStyleSheet(styles.normal_style)
            elif index == 1:
                if self.character_name:
                    self.load_game(self.character_name)
                else:
                    self.stackedWidget.setCurrentIndex(2)
                """
                try:
                    data = functions.read_game_data()
                    for char in data["characters"]:
                        if character_name in char:
                            char[character_name].update(race=self.character_race)
                            functions.write_game_data(data)
                except (KeyError, ValueError):
                    self.setup_ui()
                """
            elif index == 2:
                character_name = self.txtCharacterName.toPlainText().title()
                if len(character_name) == 0 or len(character_name) > 10:
                    self.txtCharacterName.setStyleSheet(
                        "background: transparent;"
                        "border: 2px solid;"
                        "border-color: red;"
                        "color: rgb(0, 0, 0);"
                    )
                    return
                else:
                    data = functions.read_game_data()
                    for char in data["characters"]:
                        if character_name in char:
                            self.lblWarning.setText("That character already exists!")
                            self.txtCharacterName.setStyleSheet(
                                "background: transparent;"
                                "border: 2px solid;"
                                "border-color: red;"
                                "color: rgb(0, 0, 0);"
                            )
                            return
                    data["characters"].append(
                        {
                            character_name: {
                                "race": self.character_race,
                                "level": 1,
                                "health": 100,
                                "gold": 25
                            }
                        }
                    )
                    functions.write_game_data(data)
                    self.load_game(character_name)
        elif action == "back":
            if index == 1:
                self.setup_ui()
            elif index == 4:
                self.setup_ui()
            else:
                self.stackedWidget.setCurrentIndex(index - 1)
        play_sound("music/sounds/page-turning.wav")

    def select_character(self, race):
        """
        Change styleSheet of selected QPushButton.
        :param race:
        :return:
        """
        self.character_race = race
        if race == "orc":
            self.btnOrc.setStyleSheet(styles.selected_style)
            self.btnElf.setStyleSheet(styles.normal_style)
            self.btnGoblin.setStyleSheet(styles.normal_style)
            self.btnDwarf.setStyleSheet(styles.normal_style)
            self.btnTroll.setStyleSheet(styles.normal_style)
            self.character_name = self.lblOrc.text()
        elif race == "elf":
            self.btnOrc.setStyleSheet(styles.normal_style)
            self.btnElf.setStyleSheet(styles.selected_style)
            self.btnGoblin.setStyleSheet(styles.normal_style)
            self.btnDwarf.setStyleSheet(styles.normal_style)
            self.btnTroll.setStyleSheet(styles.normal_style)
            self.character_name = self.lblElf.text()
        elif race == "goblin":
            self.btnOrc.setStyleSheet(styles.normal_style)
            self.btnElf.setStyleSheet(styles.normal_style)
            self.btnGoblin.setStyleSheet(styles.selected_style)
            self.btnDwarf.setStyleSheet(styles.normal_style)
            self.btnTroll.setStyleSheet(styles.normal_style)
            self.character_name = self.lblGoblin.text()
        elif race == "dwarf":
            self.btnOrc.setStyleSheet(styles.normal_style)
            self.btnElf.setStyleSheet(styles.normal_style)
            self.btnGoblin.setStyleSheet(styles.normal_style)
            self.btnDwarf.setStyleSheet(styles.selected_style)
            self.btnTroll.setStyleSheet(styles.normal_style)
            self.character_name = self.lblDwarf.text()
        elif race == "troll":
            self.btnOrc.setStyleSheet(styles.normal_style)
            self.btnElf.setStyleSheet(styles.normal_style)
            self.btnGoblin.setStyleSheet(styles.normal_style)
            self.btnDwarf.setStyleSheet(styles.normal_style)
            self.btnTroll.setStyleSheet(styles.selected_style)
            self.character_name = self.lblTroll.text()

    def load_game(self, character_name):
        """
        Load character stats and setup window for gameplay.
        :param character_name:
        :return:
        """
        self.fade_out(self.centralWidget())
        self.stackedWidget.setCurrentIndex(3)
        for widget in self.centralwidget.children():
            if widget.objectName() in self.widgets_list:
                if widget.objectName() == "btnBack":
                    widget.setVisible(False)
                else:
                    widget.setVisible(True)
        for char in functions.read_game_data()["characters"]:
            if character_name in char:
                gold = char[character_name]["gold"]
                level = char[character_name]["level"]
                char_race = char[character_name]["race"]
                health = char[character_name]["health"]
                self.lblGP.setText(str(gold) + " GP")
                self.lblName.setText(character_name)
                self.lblLevel.setText("LVL " + str(level))
                self.lblHP.setText(str(health) + " HP")
                if char_race == "orc":
                    self.btnCharacter.setIcon(QIcon("images/orc-head-color.png"))
                elif char_race == "elf":
                    self.btnCharacter.setIcon(QIcon("images/woman-elf-face-color.png"))
                elif char_race == "goblin":
                    self.btnCharacter.setIcon(QIcon("images/goblin-face-color.png"))
                elif char_race == "dwarf":
                    self.btnCharacter.setIcon(QIcon("images/dwarf-face-color.png"))
                elif char_race == "troll":
                    self.btnCharacter.setIcon(QIcon("images/troll-color.png"))
        volume = pygame.mixer.music.get_volume()
        while volume > 0:
            volume -= 0.000001
            pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.stop()
        self.fade_in(self.centralWidget())
        load_music("music/No-More-Magic.mp3", running=True)

    def settings(self):
        """
        Change QStackedWidget index to settings page.
        :return:
        """
        self.stackedWidget.setCurrentIndex(4)
        self.btnBack.setVisible(True)

    def toggle_button(self, button):
        torch_unlit = QIcon()
        torch_lit = QIcon()
        torch_lit.addPixmap(QPixmap("images/torch-lit.png"))
        torch_unlit.addPixmap(QPixmap("images/torch-unlit.png"))
        if button == "music":
            self.btnMusic.setIcon(torch_unlit)

    def fade_out(self, widget):
        """
        Fade out window over 5 seconds to 0 opacity.
        :param widget:
        :return:
        """
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(5000)
        self.animation.setStartValue(.95)
        self.animation.setEndValue(0)
        self.animation.start()

    def fade_in(self, widget):
        """
        Fade in window over 5 seconds to .95 opacity.
        :param widget:
        :return:
        """
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(5000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(.95)
        self.animation.start()
