import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.btn.clicked.connect(self.run)

    def run(self):

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT
                                    кофе.ID,
                                    Сорта.название,
                                    кофе.степень_обжарки,
                                    кофе.молотый_в_зернах,
                                    кофе.описание_вкуса,
                                    кофе.цена,
                                    кофе.объем_упаковки
                                FROM 
                                    кофе
                                JOIN Сорта ON кофе.сорт = Сорта.ID""").fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "сорт", "степень обжарки",
                                                    "молотый/в зернах", "описание вкуса",
                                                    "цена", "объем упаковки"])

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())