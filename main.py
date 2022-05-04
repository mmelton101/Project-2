from controller import *
from controller_battle import *


def main():
    app = QApplication([])
    window1 = ControllerBossChoice()
    window1.show()
    app.exec_()
    if bsu.boss_name != "":
        window2 = ControllerMoveChoice()
        window2.show()
        app.exec_()
        if len(psu.player_move_list) == 6:
            window3 = ControllerBattle()
            window3.show()
            app.exec_()


if __name__ == "__main__":
    main()
