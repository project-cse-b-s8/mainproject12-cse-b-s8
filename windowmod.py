import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow
from main import Everything

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionReset.triggered.connect(self.resetFields)
        self.ui.actionClose.triggered.connect(self.close)
        self.show()


    def doit(self, boolVal=False):
        s=self.ui.InputTextBox.toPlainText()
        s=Everything().mine(s)
        self.ui.SummaryTextBox.setPlainText(s)

    def resetFields(self):
        self.ui.SummaryTextBox.setPlainText('')
        self.ui.InputTextBox.setPlainText('')	

    def actionClose(self):
        self.resetFields()
	

app = QApplication([])
w = AppWindow()
w.show()
app.exec_()

#on quitting: Are you sure you wanna quit? Yes|No
