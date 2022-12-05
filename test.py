import os
import sys
from PyQt6.QtSql import QSqlQuery
from PyQt6 import QtCore, QtWidgets, QtGui

app = QtWidgets.QApplication([])

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.resize(300, 100)
        self.setLayout(QtWidgets.QVBoxLayout())

        button = QtWidgets.QPushButton('Submit')
        button.clicked.connect(self.onclick)
        self.layout().addWidget(button)

    def onclick(self):
        self.close()
        messagebox = QtWidgets.QMessageBox()
        messagebox.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\worker\CadiaN.jpg"))

        exe = messagebox.exec()
        print ('messagebox.exec_(): %s'%exe    )



dialog = Dialog()
dialog.show()     
app.exec()