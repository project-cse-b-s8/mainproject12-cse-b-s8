

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(404, 300)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 401, 291))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_7.addWidget(self.textEdit, 1, 0, 1, 2)
        self.CancelButton = QtWidgets.QPushButton(self.widget)
        self.CancelButton.setObjectName("CancelButton")
        self.gridLayout_7.addWidget(self.CancelButton, 2, 0, 1, 1)
        self.SummarizeButton = QtWidgets.QPushButton(self.widget)
        self.SummarizeButton.setObjectName("SummarizeButton")
        self.gridLayout_7.addWidget(self.SummarizeButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CancelButton.setText(_translate("Dialog", "PushButton"))
        self.SummarizeButton.setText(_translate("Dialog", "Summarize"))
        self.label.setText(_translate("Dialog", "Enter the text below"))

