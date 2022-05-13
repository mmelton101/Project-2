from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_boss_choice(object):
    def setupUi(self, window_boss_choice):
        window_boss_choice.setObjectName("window_boss_choice")
        window_boss_choice.resize(346, 280)
        window_boss_choice.setMinimumSize(QtCore.QSize(346, 280))
        window_boss_choice.setMaximumSize(QtCore.QSize(346, 280))
        self.centralwidget = QtWidgets.QWidget(window_boss_choice)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 261, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.label_boss_name = QtWidgets.QLabel(self.centralwidget)
        self.label_boss_name.setGeometry(QtCore.QRect(40, 120, 81, 16))
        self.label_boss_name.setObjectName("label_boss_name")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(120, 170, 93, 71))
        self.button_enter.setObjectName("button_enter")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 120, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        window_boss_choice.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_boss_choice)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 26))
        self.menubar.setObjectName("menubar")
        window_boss_choice.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_boss_choice)
        self.statusbar.setObjectName("statusbar")
        window_boss_choice.setStatusBar(self.statusbar)

        self.retranslateUi(window_boss_choice)
        QtCore.QMetaObject.connectSlotsByName(window_boss_choice)

    def retranslateUi(self, window_boss_choice):
        _translate = QtCore.QCoreApplication.translate
        window_boss_choice.setWindowTitle(_translate("window_boss_choice", "Boss Choice"))
        self.textBrowser.setHtml(_translate("window_boss_choice", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose one of the following Bosses to fight:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Sephiroth</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - Tendo</p></body></html>"))
        self.label_boss_name.setText(_translate("window_boss_choice", "Boss Name: "))
        self.button_enter.setText(_translate("window_boss_choice", "Enter"))
        self.comboBox.setItemText(0, _translate("window_boss_choice", "Sephiroth"))
        self.comboBox.setItemText(1, _translate("window_boss_choice", "Tendo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_boss_choice = QtWidgets.QMainWindow()
    ui = Ui_window_boss_choice()
    ui.setupUi(window_boss_choice)
    window_boss_choice.show()
    sys.exit(app.exec_())
