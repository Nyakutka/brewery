import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QTableView, QApplication, QWidget, QLabel
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle('PyQt')
   w.show()
   sys.exit(app.exec())
	
if __name__ == '__main__':
   window()