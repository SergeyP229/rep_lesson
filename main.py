import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPoint
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()
        
    def draw(self, qp):
        size = random.randint(10, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(random.randint(0, 500), random.randint(0, 500), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())