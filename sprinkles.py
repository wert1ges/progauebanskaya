import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from burgers import Burger_choise
#from snacks import Snack_choise
from drinks import Drink_choise
from deserts import Desert_choise
from last import finish_window
#from png import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main.ui', self)

        self.pushButton.clicked.connect(self.burgers)
        #self.pushButton_2.clicked.connect(self.snacks)
        self.pushButton_3.clicked.connect(self.drinks)
        self.pushButton_4.clicked.connect(self.deserts)
        self.pushButton_5.clicked.connect(self.finish_win)


    def burgers(self):
        global menu2_global
        menu2_global = Burger_choise()
        menu2_global.show()

    #def snacks(self):
    #    global menu3_global
    #    menu3_global = Snack_choise()
    #    menu3_global.show()

    def drinks(self):
        global menu4_global
        menu4_global = Drink_choise()
        menu4_global.show()

    def deserts(self):
        global menu5_global
        menu5_global = Desert_choise()
        menu5_global.show()

    def finish_win(self):
        global finish123
        finish123 = finish_window()
        finish123.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
