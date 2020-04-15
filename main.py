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
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):

        # Handleing Themes
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

        # Switching Tabs
        self.pushButton.clicked.connect(self.Open_day_to_day_tabs)
        self.pushButton_2.clicked.connect(self.Open_books_tab)
        self.pushButton_3.clicked.connect(self.Open_users_tab)
        self.pushButton_4.clicked.connect(self.Open_settings_tab)
        self.pushButton_7.clicked.connect(self.Add_new_book)



        # DATABASE OPERATIONS

        self.pushButton_14.clicked.connect(self.Add_category)
        self.pushButton_15.clicked.connect(self.Add_author)
        self.pushButton_16.clicked.connect(self.Add_publisher)


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


    #Books @ DB


    def Add_new_book(self):
        self.db = pymysql.connect(host = 'localhost', user = 'root' , password = '1234' , db = 'library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_4.text()


    def Search_book(self):
        pass

    def Edit_book(self):
        pass

    def Delete_book(self):
        pass


    # Users @ DB


    def Add_new_user(self):
        pass

    def Login(self):
        pass

    def Edit_users(self):
        pass


    #Settings @ DB

    def Add_category(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
        INSERT INTO category (category_name) VALUES (%s)
        ''', (category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')


    def Add_author(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute('''
                INSERT INTO authors (author_name) VALUES (%s)
                ''', (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')

    def Add_publisher(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()

        self.cur.execute('''
                        INSERT INTO publisher (publisher_name) VALUES (%s)
                        ''', (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')





def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()