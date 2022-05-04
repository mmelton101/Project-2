from PyQt5.QtWidgets import *
from view1 import Ui_window_boss_choice
from view3 import Ui_window_battle
from boss_setup import BossSetup
bsu = BossSetup()


class ControllerBossChoice(QMainWindow, Ui_window_boss_choice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.boss_select())

    def boss_select(self):
        boss_choices = ["sephiroth", "tendo"]
        boss_choice = self.line_boss_name.text().lower().strip()
        for name in boss_choices:
            if boss_choice == name:
                bsu.boss_selection(boss_choice)
                self.close()
        self.line_boss_name.setText("That is not a valid boss name")


class ControllerBattle(QMainWindow, Ui_window_battle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_bHealth.setText(str(bsu.boss_hp))

        self.button_move1.clicked.connect(lambda: self.move_choice())
        self.button_move2.clicked.connect(lambda: self.move_choice())
        self.button_move3.clicked.connect(lambda: self.move_choice())
        self.button_move4.clicked.connect(lambda: self.move_choice())

    def move_choice(self):
        pass

