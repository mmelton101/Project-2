from PyQt5.QtWidgets import *
from view3 import Ui_window_battle
from controller import bsu, psu
from move_processor import MoveProcessor

mp = MoveProcessor()


class ControllerBattle(QMainWindow, Ui_window_battle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_turn = True
        self.turn_end = True
        self.setupUi(self)
        self.label_bHealth.setText(str(bsu.boss_hp))
        self.label_bMana.setText(str(bsu.boss_mp))
        self.label_pHealth.setText(str(psu.player_hp))
        self.label_pMana.setText(str(psu.player_mp))

        self.button_move1.setText(psu.player_move_list[2].move_name)
        if psu.player_move_list[2].move_hp_cost == 0:
            self.label_move1.setText("MP:")
            self.label_move1cost.setText(str(psu.player_move_list[2].move_mp_cost))
        else:
            self.label_move1.setText("HP:")
            self.label_move1cost.setText(str(psu.player_move_list[2].move_hp_cost))
        self.button_move2.setText(psu.player_move_list[3].move_name)
        if psu.player_move_list[3].move_hp_cost == 0:
            self.label_move2.setText("MP:")
            self.label_move2cost.setText(str(psu.player_move_list[3].move_mp_cost))
        else:
            self.label_move2.setText("HP:")
            self.label_move2cost.setText(str(psu.player_move_list[3].move_hp_cost))
        self.button_move3.setText(psu.player_move_list[4].move_name)
        if psu.player_move_list[4].move_hp_cost == 0:
            self.label_move3.setText("MP:")
            self.label_move3cost.setText(str(psu.player_move_list[4].move_mp_cost))
        else:
            self.label_move3.setText("HP:")
            self.label_move3cost.setText(str(psu.player_move_list[4].move_hp_cost))
        self.button_move4.setText(psu.player_move_list[5].move_name)
        if psu.player_move_list[5].move_hp_cost == 0:
            self.label_move4.setText("MP:")
            self.label_move4cost.setText(str(psu.player_move_list[5].move_mp_cost))
        else:
            self.label_move4.setText("HP:")
            self.label_move4cost.setText(str(psu.player_move_list[5].move_hp_cost))

        self.button_move1.clicked.connect(lambda: self.move_choice(self.button_move1.text()))
        self.button_move2.clicked.connect(lambda: self.move_choice(self.button_move2.text()))
        self.button_move3.clicked.connect(lambda: self.move_choice(self.button_move3.text()))
        self.button_move4.clicked.connect(lambda: self.move_choice(self.button_move4.text()))
        self.button_move5.clicked.connect(lambda: self.move_choice(self.button_move5.text()))
        self.button_move6.clicked.connect(lambda: self.move_choice(self.button_move6.text()))

    def move_choice(self, move):
        self.turn_end = False
        if self.player_turn and self.win_condition(psu, bsu):
            self.turn_end, text = mp.player_move(psu, move, bsu)
            self.text_battle_info.append(text)
            if self.turn_end:
                self.player_turn = False

        if not self.player_turn and self.win_condition(psu, bsu):
            while self.turn_end:
                self.turn_end, text = mp.boss_turn(bsu, psu)
            self.text_battle_info.append(text)
            self.player_turn = True
            self.win_condition(psu, bsu)

        self.label_bHealth.setText(str(bsu.boss_hp))
        self.label_bMana.setText(str(bsu.boss_mp))
        self.label_pHealth.setText(str(psu.player_hp))
        self.label_pMana.setText(str(psu.player_mp))

        self.button_move1.setText(psu.player_move_list[2].move_name)
        if psu.player_move_list[2].move_hp_cost == 0:
            self.label_move1.setText("MP:")
            self.label_move1cost.setText(str(psu.player_move_list[2].move_mp_cost))
        else:
            self.label_move1.setText("HP:")
            self.label_move1cost.setText(str(psu.player_move_list[2].move_hp_cost))
        self.button_move2.setText(psu.player_move_list[3].move_name)
        if psu.player_move_list[3].move_hp_cost == 0:
            self.label_move2.setText("MP:")
            self.label_move2cost.setText(str(psu.player_move_list[3].move_mp_cost))
        else:
            self.label_move2.setText("HP:")
            self.label_move2cost.setText(str(psu.player_move_list[3].move_hp_cost))
        self.button_move3.setText(psu.player_move_list[4].move_name)
        if psu.player_move_list[4].move_hp_cost == 0:
            self.label_move3.setText("MP:")
            self.label_move3cost.setText(str(psu.player_move_list[4].move_mp_cost))
        else:
            self.label_move3.setText("HP:")
            self.label_move3cost.setText(str(psu.player_move_list[4].move_hp_cost))
        self.button_move4.setText(psu.player_move_list[5].move_name)
        if psu.player_move_list[5].move_hp_cost == 0:
            self.label_move4.setText("MP:")
            self.label_move4cost.setText(str(psu.player_move_list[5].move_mp_cost))
        else:
            self.label_move4.setText("HP:")
            self.label_move4cost.setText(str(psu.player_move_list[5].move_hp_cost))

    def win_condition(self, player, boss):
        if player.player_hp <= 0:
            self.text_battle_info.append("GAME OVER. YOU LOSE")
            self.button_move1.setEnabled(False)
            self.button_move2.setEnabled(False)
            self.button_move3.setEnabled(False)
            self.button_move4.setEnabled(False)
            self.button_move5.setEnabled(False)
            self.button_move6.setEnabled(False)
            return False
        elif boss.boss_hp <= 0:
            self.text_battle_info.append("GAME OVER. YOU WIN")
            self.button_move1.setEnabled(False)
            self.button_move2.setEnabled(False)
            self.button_move3.setEnabled(False)
            self.button_move4.setEnabled(False)
            self.button_move5.setEnabled(False)
            self.button_move6.setEnabled(False)
            return False
        else:
            return True
