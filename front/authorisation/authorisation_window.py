from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from ui_authorisation_window import Ui_AuthorisationWindow
from registration_window import RegistrationWindow
from datetime import datetime
import sys
# sys.path.append('D:/учеба/brewery/db_connection')
# sys.path.append('D:/учеба/brewery/front/customer')
sys.path.append('D:/учеба/бд/курсач/brewery/db_connection')
sys.path.append('D:/учеба/бд/курсач/brewery/front/customer')
from db_connection import DataBaseConnection
from customer_window import CustomerWindow

class AuthorisationWindow(QtWidgets.QMainWindow, Ui_AuthorisationWindow):
    def __init__(self, app_widget, *args, **kwargs):
        super(AuthorisationWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app_widget = app_widget
        self.app_widget.setFixedWidth(500)
        self.app_widget.setFixedHeight(450)
        self.invalid_auth_label.hide()
        self.sign_in_button.clicked.connect(self.__sign_up)
        self.sign_up_button.clicked.connect(self.__register)
        self.db = DataBaseConnection().database

    def __sign_up(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()
        query = QSqlQuery()
        query.exec(f"select user_id, user_role from users where username='{username}' and user_password=HASHBYTES('SHA2_256', '{password}')")
        query.first()
        self.user_id = query.value(0)
        self.role = query.value(1)
        if (self.user_id is None):
            self.invalid_auth_label.show()
        else:
            if self.role == 'customer':
                self.invalid_auth_label.hide()
                window = CustomerWindow(app_widget=self.app_widget, db=self.db, customer_id=self.user_id, customer_username=username)
                self.username_line_edit.setText('')
                self.password_line_edit.setText('')
                self.app_widget.setFixedWidth(1000)
                self.app_widget.setFixedHeight(650)
                self.app_widget.addWidget(window)
                self.app_widget.setCurrentIndex(self.app_widget.count() - 1)
            # self.close()

    def __register(self):
        window = RegistrationWindow(app_widget=self.app_widget, db=self.db)
        self.username_line_edit.setText('')
        self.password_line_edit.setText('')
        self.app_widget.setFixedWidth(550)
        self.app_widget.setFixedHeight(450)
        self.app_widget.addWidget(window)
        self.app_widget.setCurrentIndex(self.app_widget.count() - 1)
            
