from PyQt5.QtWidgets import *
from view1 import Ui_window_boss_choice
from view2 import Ui_window_move_select
from boss_setup import Boss
from player_setup import Player
bsu = Boss()
psu = Player()


class ControllerBossChoice(QMainWindow, Ui_window_boss_choice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.boss_select())

    def boss_select(self) -> None:
        """
        Decides what boss the user selected in the combo box then closes the window
        """
        boss_choices = ["sephiroth", "tendo"]
        boss_choice = self.comboBox.currentText().lower()
        for name in boss_choices:
            if boss_choice == name:
                bsu.boss_selection(boss_choice)
                self.close()


class ControllerMoveChoice(QMainWindow, Ui_window_move_select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.move_select())

    def move_select(self) -> None:
        """
        Decides what the user selected on the radio buttons and sends the info
        when the user has selected 4 unique radio buttons the window is closed
        """
        moves_left = int(self.label_2.text())
        move_list_length = len(psu.player_move_list)
        if self.radio_firaga.isChecked():
            psu.move_choice("firaga")
            if len(psu.player_move_list) > move_list_length:
                self.label_2.setText(str(moves_left - 1))

        if self.radio_splash.isChecked():
            psu.move_choice("sparkling splash")
            if len(psu.player_move_list) > move_list_length:
                self.label_2.setText(str(moves_left - 1))

        if self.radio_pigeon.isChecked():
            psu.move_choice("pigeon raid")
            if len(psu.player_move_list) > move_list_length:
                self.label_2.setText(str(moves_left - 1))

        if self.radio_slash.isChecked():
            psu.move_choice("cross slash")
            if len(psu.player_move_list) > move_list_length:
                self.label_2.setText(str(moves_left - 1))

        if self.radio_curaga.isChecked():
            psu.move_choice("curaga")
            if len(psu.player_move_list) > move_list_length:
                self.label_2.setText(str(moves_left - 1))

        if self.radio_spark.isChecked():
            psu.move_choice("stamina spark")
            if len(psu.player_move_list) > move_list_length:
                self.label_2.setText(str(moves_left - 1))

        if len(psu.player_move_list) == 6:
            self.close()
