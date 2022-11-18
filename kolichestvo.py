from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QSpinBox, QLabel, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3


con = sqlite3.connect("data.db")
x = []


class kolvo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('kolvo.ui', self)
        #con = sqlite3.connect("data.db")
        #cur = con.cursor()
        #result = cur.execute("""SELECT * FROM id
                    #WHERE """).fetchall()
        self.pushButton.clicked.connect(self.close)




