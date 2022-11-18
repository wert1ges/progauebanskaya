from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class finish_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('last_page.ui', self)
        self.pushButton_2.clicked.connect(self.close)
