from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from kolichestvo import kolvo


class Burger_choise(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('burgers2.ui', self)
        self.pushButton.clicked.connect(self.kolvo1)
        self.pushButton_2.clicked.connect(self.kolvo1)
        self.pushButton_3.clicked.connect(self.kolvo1)
        self.pushButton_4.clicked.connect(self.kolvo1)
        self.pushButton_6.clicked.connect(self.close)

    def kolvo1(self):
        global menu_global
        menu_global = kolvo()
        menu_global.show()

