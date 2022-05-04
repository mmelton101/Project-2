from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_battle(object):
    def setupUi(self, window_battle):
        window_battle.setObjectName("window_battle")
        window_battle.resize(858, 464)
        window_battle.setMinimumSize(QtCore.QSize(858, 464))
        window_battle.setMaximumSize(QtCore.QSize(858, 464))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        window_battle.setFont(font)
        self.centralwidget = QtWidgets.QWidget(window_battle)
        self.centralwidget.setObjectName("centralwidget")
        self.text_battle_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_battle_info.setGeometry(QtCore.QRect(40, 30, 391, 281))
        self.text_battle_info.setObjectName("text_battle_info")
        self.button_move1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move1.setGeometry(QtCore.QRect(460, 30, 161, 101))
        self.button_move1.setObjectName("button_move1")
        self.button_move2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move2.setGeometry(QtCore.QRect(650, 30, 171, 101))
        self.button_move2.setObjectName("button_move2")
        self.button_move3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move3.setGeometry(QtCore.QRect(460, 160, 161, 101))
        self.button_move3.setObjectName("button_move3")
        self.button_move4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move4.setGeometry(QtCore.QRect(650, 160, 171, 101))
        self.button_move4.setObjectName("button_move4")
        self.label_pHP = QtWidgets.QLabel(self.centralwidget)
        self.label_pHP.setGeometry(QtCore.QRect(40, 340, 71, 16))
        self.label_pHP.setObjectName("label_pHP")
        self.label_pHealth = QtWidgets.QLabel(self.centralwidget)
        self.label_pHealth.setGeometry(QtCore.QRect(130, 340, 55, 16))
        self.label_pHealth.setObjectName("label_pHealth")
        self.label_pMP = QtWidgets.QLabel(self.centralwidget)
        self.label_pMP.setGeometry(QtCore.QRect(40, 380, 71, 16))
        self.label_pMP.setObjectName("label_pMP")
        self.label_pMana = QtWidgets.QLabel(self.centralwidget)
        self.label_pMana.setGeometry(QtCore.QRect(130, 380, 55, 16))
        self.label_pMana.setObjectName("label_pMana")
        self.label_bHP = QtWidgets.QLabel(self.centralwidget)
        self.label_bHP.setGeometry(QtCore.QRect(210, 340, 55, 16))
        self.label_bHP.setObjectName("label_bHP")
        self.label_bMP = QtWidgets.QLabel(self.centralwidget)
        self.label_bMP.setGeometry(QtCore.QRect(210, 380, 55, 16))
        self.label_bMP.setObjectName("label_bMP")
        self.label_bHealth = QtWidgets.QLabel(self.centralwidget)
        self.label_bHealth.setGeometry(QtCore.QRect(290, 340, 55, 16))
        self.label_bHealth.setObjectName("label_bHealth")
        self.label_bMana = QtWidgets.QLabel(self.centralwidget)
        self.label_bMana.setGeometry(QtCore.QRect(290, 380, 55, 16))
        self.label_bMana.setObjectName("label_bMana")
        self.button_move5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move5.setGeometry(QtCore.QRect(460, 290, 161, 101))
        self.button_move5.setObjectName("button_move5")
        self.button_move6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move6.setGeometry(QtCore.QRect(650, 290, 161, 101))
        self.button_move6.setObjectName("button_move6")
        self.label_move1 = QtWidgets.QLabel(self.centralwidget)
        self.label_move1.setGeometry(QtCore.QRect(470, 130, 55, 16))
        self.label_move1.setObjectName("label_move1")
        self.label_move1cost = QtWidgets.QLabel(self.centralwidget)
        self.label_move1cost.setGeometry(QtCore.QRect(530, 130, 55, 16))
        self.label_move1cost.setObjectName("label_move1cost")
        self.label_move2 = QtWidgets.QLabel(self.centralwidget)
        self.label_move2.setGeometry(QtCore.QRect(660, 130, 55, 16))
        self.label_move2.setObjectName("label_move2")
        self.label_move2cost = QtWidgets.QLabel(self.centralwidget)
        self.label_move2cost.setGeometry(QtCore.QRect(720, 130, 55, 16))
        self.label_move2cost.setObjectName("label_move2cost")
        self.label_move3 = QtWidgets.QLabel(self.centralwidget)
        self.label_move3.setGeometry(QtCore.QRect(470, 260, 55, 16))
        self.label_move3.setObjectName("label_move3")
        self.label_move3cost = QtWidgets.QLabel(self.centralwidget)
        self.label_move3cost.setGeometry(QtCore.QRect(530, 260, 55, 16))
        self.label_move3cost.setObjectName("label_move3cost")
        self.label_move4 = QtWidgets.QLabel(self.centralwidget)
        self.label_move4.setGeometry(QtCore.QRect(660, 260, 55, 16))
        self.label_move4.setObjectName("label_move4")
        self.label_move4cost = QtWidgets.QLabel(self.centralwidget)
        self.label_move4cost.setGeometry(QtCore.QRect(720, 260, 55, 16))
        self.label_move4cost.setObjectName("label_move4cost")
        window_battle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_battle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
        self.menubar.setObjectName("menubar")
        window_battle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_battle)
        self.statusbar.setObjectName("statusbar")
        window_battle.setStatusBar(self.statusbar)

        self.retranslateUi(window_battle)
        QtCore.QMetaObject.connectSlotsByName(window_battle)

    def retranslateUi(self, window_battle):
        _translate = QtCore.QCoreApplication.translate
        window_battle.setWindowTitle(_translate("window_battle", "Fight"))
        self.button_move1.setText(_translate("window_battle", "PushButton"))
        self.button_move2.setText(_translate("window_battle", "PushButton"))
        self.button_move3.setText(_translate("window_battle", "PushButton"))
        self.button_move4.setText(_translate("window_battle", "PushButton"))
        self.label_pHP.setText(_translate("window_battle", "Player HP"))
        self.label_pHealth.setText(_translate("window_battle", "0"))
        self.label_pMP.setText(_translate("window_battle", "Player MP"))
        self.label_pMana.setText(_translate("window_battle", "0"))
        self.label_bHP.setText(_translate("window_battle", "Boss HP"))
        self.label_bMP.setText(_translate("window_battle", "Boss MP"))
        self.label_bHealth.setText(_translate("window_battle", "0"))
        self.label_bMana.setText(_translate("window_battle", "0"))
        self.button_move5.setText(_translate("window_battle", "Attack"))
        self.button_move6.setText(_translate("window_battle", "Guard"))
        self.label_move1.setText(_translate("window_battle", "TextLabel"))
        self.label_move1cost.setText(_translate("window_battle", "0"))
        self.label_move2.setText(_translate("window_battle", "TextLabel"))
        self.label_move2cost.setText(_translate("window_battle", "0"))
        self.label_move3.setText(_translate("window_battle", "TextLabel"))
        self.label_move3cost.setText(_translate("window_battle", "0"))
        self.label_move4.setText(_translate("window_battle", "TextLabel"))
        self.label_move4cost.setText(_translate("window_battle", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_battle = QtWidgets.QMainWindow()
    ui = Ui_window_battle()
    ui.setupUi(window_battle)
    window_battle.show()
    sys.exit(app.exec_())
