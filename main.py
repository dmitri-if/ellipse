import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from random import randint
from PyQt6 import uic


class Exemple(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ellipse.ui', self)
        self.pushButton.clicked.connect(self.update)
    
    def paintEvent(self, event):
        qp = QPainter(self)

        size = randint(20, 101)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(0, 800), randint(0, 600), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exemple()
    ex.show()
    sys.exit(app.exec())