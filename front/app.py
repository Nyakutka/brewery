from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from datetime import datetime
import sys
sys.path.append('D:/учеба/brewery/db_connection')
sys.path.append('D:/учеба/brewery/front/authorisation')
from authorisation_window import AuthorisationWindow
            
app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(500)
widget.setFixedHeight(450)
window = AuthorisationWindow(app_widget=widget)
widget.addWidget(window)
widget.show()
app.exec()
