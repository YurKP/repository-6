import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from UI_file import Ui_MainWindow

from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        rad = randint(10, 100)
        rad2 = randint(10, 200)
        rad3 = randint(10, 200)
        rad4 = randint(10, 100)

        r1, g1, b1 = randint(0, 255), randint(0, 255), randint(0, 255)
        r2, g2, b2 = randint(0, 255), randint(0, 255), randint(0, 255)
        r3, g3, b3 = randint(0, 255), randint(0, 255), randint(0, 255)
        r4, g4, b4 = randint(0, 255), randint(0, 255), randint(0, 255)

        qp.setBrush(QColor(r1, g1, b1))
        qp.drawEllipse(100, 100, rad, rad)

        qp.setBrush(QColor(r2, g2, b2))
        qp.drawEllipse(500, 100, rad2, rad2)

        qp.setBrush(QColor(r3, g3, b3))
        qp.drawEllipse(100, 300, rad3, rad3)

        qp.setBrush(QColor(r4, g4, b4))
        qp.drawEllipse(500, 400, rad4, rad4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())