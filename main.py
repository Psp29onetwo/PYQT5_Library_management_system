from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql
pymysql.install_as_MySQLdb()

from PyQt5.uic import loadUiType

ui, _ =  loadUiType('library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hiding_Themes()

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)
        self.pushButton.clicked.connect(self.Open_day_to_day_tabs)
        self.pushButton_2.clicked.connect(self.Open_books_tab)
        self.pushButton_3.clicked.connect(self.Open_users_tab)
        self.pushButton_4.clicked.connect(self.Open_settings_tab)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()


    #Opening Tabs


    def Open_day_to_day_tabs(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)


    def Open_users_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_settings_tab(self):
        self.tabWidget.setCurrentIndex(3)




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()