import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QLabel, QComboBox


class Add_Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.pushButton.clicked.connect(self.click_btn)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        result = [i[0] for i in self.cur.execute("""SELECT название FROM Сорта""").fetchall()]
        result2 = [i[0] for i in self.cur.execute("""SELECT название FROM обжарка""").fetchall()]

        self.variety.addItems(result)
        self.roast.addItems(result2)

    def click_btn(self):
        variety = self.cur.execute(f"""SELECT ID FROM Сорта WHERE название = 
        '{self.variety.currentText()}'""").fetchall()[0][0]

        roast = self.cur.execute(f"""SELECT ID FROM обжарка WHERE название 
        = '{self.roast.currentText()}'""").fetchall()[0][0]

        text = self.lineEdit.text()
        taste = self.taste.text()
        price = self.price.text()
        volume = self.volume.text()

        self.cur.execute(f"""INSERT INTO кофе(сорт, степень_обжарки, молотый_в_зернах, описание_вкуса, цена, 
        объем_упаковки) VALUES({variety}, {roast}, '{text}', '{taste}', {price}, {volume})""")
        self.con.commit()

        self.variety.setEnabled(False)
        self.roast.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.taste.setEnabled(False)
        self.price.setEnabled(False)
        self.volume.setEnabled(False)

        ind = self.cur.execute("""SELECT ID FROM кофе""").fetchall()[-1][0]
        final_label = QLabel(self)
        final_label.setText(f"В БД добавлена запись с ID = {ind}")
        final_label.move(160, 10)
        final_label.show()


class Change_Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        label0 = QLabel(self)
        label0.setText("ID")
        label0.move(130, 20)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        self.combo_box_id = QComboBox(self)
        self.combo_box_id.move(170, 20)

        result = [str(i[0]) for i in self.cur.execute("""SELECT ID FROM кофе""").fetchall()]
        self.combo_box_id.addItems(result)
        self.on_combobox_changed()

        result1 = [i[0] for i in self.cur.execute("""SELECT название FROM Сорта""").fetchall()]
        result2 = [i[0] for i in self.cur.execute("""SELECT название FROM обжарка""").fetchall()]

        self.variety.addItems(result1)
        self.roast.addItems(result2)

        self.pushButton.clicked.connect(self.click_btn)
        self.combo_box_id.currentTextChanged.connect(self.on_combobox_changed)

    def on_combobox_changed(self):
        self.variety.setCurrentText(self.cur.execute(f"""SELECT название FROM Сорта WHERE ID = 
        (SELECT сорт FROM кофе WHERE ID = {self.combo_box_id.currentText()})""").fetchall()[0][0])

        self.roast.setCurrentText(self.cur.execute(f"""SELECT название FROM обжарка WHERE ID = 
        (SELECT степень_обжарки FROM кофе WHERE ID = {self.combo_box_id.currentText()})""").fetchall()[0][0])

        result = self.cur.execute(f"""SELECT молотый_в_зернах, 
        описание_вкуса, цена, объем_упаковки FROM кофе WHERE ID = {self.combo_box_id.currentText()}""").fetchall()[0]

        self.lineEdit.setText(result[0])
        self.taste.setText(result[1])
        self.price.setText(str(result[2]))
        self.volume.setText(str(result[3]))

    def click_btn(self):
        variety = self.cur.execute(f"""SELECT ID FROM Сорта WHERE название = 
        '{self.variety.currentText()}'""").fetchall()[0][0]

        roast = self.cur.execute(f"""SELECT ID FROM обжарка WHERE название 
        = '{self.roast.currentText()}'""").fetchall()[0][0]

        text = self.lineEdit.text()
        taste = self.taste.text()
        price = self.price.text()
        volume = self.volume.text()

        self.cur.execute(f"""UPDATE кофе
                            SET 
                            сорт = {variety},
                            степень_обжарки = {roast},
                            молотый_в_зернах = '{text}',
                            описание_вкуса = '{taste}',
                            цена = {price},
                            объем_упаковки = {volume}
                            WHERE ID = {self.combo_box_id.currentText()}""")
        self.con.commit()

        self.combo_box_id.setEnabled(False)
        self.variety.setEnabled(False)
        self.roast.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.taste.setEnabled(False)
        self.price.setEnabled(False)
        self.volume.setEnabled(False)

        final_label = QLabel(self)
        final_label.setText(f"В БД изменена запись с ID = {self.combo_box_id.currentText()}")
        final_label.move(160, 3)
        final_label.show()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.launch.clicked.connect(self.click_launch)
        self.add.clicked.connect(self.click_add)
        self.change.clicked.connect(self.click_change)

    def click_launch(self):

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT
                                    кофе.ID,
                                    Сорта.название,
                                    обжарка.название,
                                    кофе.молотый_в_зернах,
                                    кофе.описание_вкуса,
                                    кофе.цена,
                                    кофе.объем_упаковки
                                FROM 
                                    кофе
                                JOIN Сорта ON кофе.сорт = Сорта.ID
                                JOIN обжарка ON кофе.степень_обжарки = обжарка.ID""").fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "сорт", "степень обжарки",
                                                    "молотый/в зернах", "описание вкуса",
                                                    "цена", "объем упаковки"])

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        con.close()

    def click_add(self):
        kek = Add_Window()
        kek.show()
        kek.exec()

    def click_change(self):
        kek = Change_Window()
        kek.show()
        kek.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())