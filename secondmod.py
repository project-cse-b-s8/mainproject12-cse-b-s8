import sys
from PyQt5.QtWidgets import QFrame, QApplication
from second import Ui_Frame

class AppWindow(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.show()  

def self.te.toPlainText();

app = QApplication([])
w = AppWindow()
w.show()
#sys.exit(app.exec_())
app.exec_()
