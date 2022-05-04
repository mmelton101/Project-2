from controller import *


def main():
    app = QApplication([])
    window1 = ControllerBossChoice()
    window3 = ControllerBattle()
    window1.show()
    app.exec_()
    window3.show()
    app.exec_()


if __name__ == "__main__":
    main()
