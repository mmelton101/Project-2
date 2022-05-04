from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_move_select(object):
    def setupUi(self, window_move_select):
        window_move_select.setObjectName("window_move_select")
        window_move_select.resize(400, 450)
        window_move_select.setMinimumSize(QtCore.QSize(400, 450))
        window_move_select.setMaximumSize(QtCore.QSize(400, 450))
        self.centralwidget = QtWidgets.QWidget(window_move_select)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 10, 371, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.radio_firaga = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_firaga.setGeometry(QtCore.QRect(20, 270, 95, 20))
        self.radio_firaga.setObjectName("radio_firaga")
        self.radio_splash = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_splash.setGeometry(QtCore.QRect(140, 270, 121, 20))
        self.radio_splash.setObjectName("radio_splash")
        self.radio_pigeon = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_pigeon.setGeometry(QtCore.QRect(280, 270, 95, 20))
        self.radio_pigeon.setObjectName("radio_pigeon")
        self.radio_slash = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_slash.setGeometry(QtCore.QRect(20, 320, 95, 20))
        self.radio_slash.setObjectName("radio_slash")
        self.radio_curaga = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_curaga.setGeometry(QtCore.QRect(140, 320, 95, 20))
        self.radio_curaga.setObjectName("radio_curaga")
        self.radio_spark = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_spark.setGeometry(QtCore.QRect(280, 320, 111, 20))
        self.radio_spark.setObjectName("radio_spark")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(160, 360, 93, 28))
        self.button_enter.setObjectName("button_enter")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 370, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 370, 55, 16))
        self.label_2.setObjectName("label_2")
        window_move_select.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_move_select)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        window_move_select.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_move_select)
        self.statusbar.setObjectName("statusbar")
        window_move_select.setStatusBar(self.statusbar)

        self.retranslateUi(window_move_select)
        QtCore.QMetaObject.connectSlotsByName(window_move_select)

    def retranslateUi(self, window_move_select):
        _translate = QtCore.QCoreApplication.translate
        window_move_select.setWindowTitle(_translate("window_move_select", "Move Select"))
        self.textBrowser.setHtml(_translate("window_move_select", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please Select 4 of the following moves:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Firaga: Powerful fire spell, can inflict Burn. 25MP</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Sparkling Splash: Splashes enemy with freezing water, can inflict Cold. 25MP</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Pigeon Raid: Summon a swarm of pigeons to attack the enemy. 50HP</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Cross Slash: Powerful multi-slash sword attack, can inflict Bleed. 100HP</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Curaga: A powerful healing spell that returns user to full health. 50MP</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Stamina Spark: An energy drink that totally revitalizes the user\'s HP and MP. You have 3 per match </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select 1 move at a time and press the Enter button each time you select a move</p></body></html>"))
        self.radio_firaga.setText(_translate("window_move_select", "Firaga"))
        self.radio_splash.setText(_translate("window_move_select", "Sparkling Splash"))
        self.radio_pigeon.setText(_translate("window_move_select", "Pigeon Raid"))
        self.radio_slash.setText(_translate("window_move_select", "Cross Slash"))
        self.radio_curaga.setText(_translate("window_move_select", "Curaga"))
        self.radio_spark.setText(_translate("window_move_select", "Stamina Spark"))
        self.button_enter.setText(_translate("window_move_select", "Enter"))
        self.label.setText(_translate("window_move_select", "Moves Left:"))
        self.label_2.setText(_translate("window_move_select", "4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_move_select = QtWidgets.QMainWindow()
    ui = Ui_window_move_select()
    ui.setupUi(window_move_select)
    window_move_select.show()
    sys.exit(app.exec_())
