# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.launch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.launch.setGeometry(QtCore.QRect(30, 10, 181, 61))
        self.launch.setObjectName("launch")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 741, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add.setGeometry(QtCore.QRect(584, 12, 191, 61))
        self.add.setObjectName("add")
        self.change = QtWidgets.QPushButton(parent=self.centralwidget)
        self.change.setGeometry(QtCore.QRect(260, 10, 281, 61))
        self.change.setObjectName("change")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.launch.setText(_translate("MainWindow", "Запуск"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.change.setText(_translate("MainWindow", "Изменить"))