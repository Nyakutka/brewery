from PyQt6.QtSql import QSqlQuery
from PyQt6 import QtWidgets
from ui.ui_authorisation_window import Ui_AuthorisationWindow
from registration_window import RegistrationWindow

import sys

sys.path.append('D:/учеба/бд/курсач/brewery/db_connection')
sys.path.append('D:/учеба/бд/курсач/brewery/front/customer')
sys.path.append('D:/учеба/бд/курсач/brewery/front/worker')
sys.path.append('D:/учеба/бд/курсач/brewery/front/admin')
from db_connection import DataBaseConnection
from customer_window import CustomerWindow
from worker_window import WorkerWindow
from admin_window import AdminWindow

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
        query.exec(f"select user_role from users where username='{username}' and user_password=HASHBYTES('SHA2_256', '{password}')")
        query.first()
        self.role = query.value(0)
        if (self.role is None):
            self.invalid_auth_label.show()
        else:
            if self.role == 'customer':
                query.exec(f"select customer_id from customers join users on customers.user_id=users.user_id where username='{username}' and user_password=HASHBYTES('SHA2_256', '{password}')")
                query.first()
                self.customer_id = query.value(0)
                self.invalid_auth_label.hide()
                window = CustomerWindow(app_widget=self.app_widget, db=self.db, customer_id=self.customer_id, customer_username=username)
                self.username_line_edit.setText('')
                self.password_line_edit.setText('')
                self.app_widget.setFixedWidth(1000)
                self.app_widget.setFixedHeight(650)
                self.app_widget.addWidget(window)
                self.app_widget.setCurrentIndex(self.app_widget.count() - 1)
            elif self.role == 'worker':
                query.exec(f"select worker_id from workers join users on workers.user_id=users.user_id where username='{username}' and user_password=HASHBYTES('SHA2_256', '{password}')")
                query.first()
                self.worker_id = query.value(0)
                self.invalid_auth_label.hide()
                window = WorkerWindow(app_widget=self.app_widget, db=self.db, worker_id=self.worker_id, worker_username=username)
                self.username_line_edit.setText('')
                self.password_line_edit.setText('')
                self.app_widget.setFixedWidth(1200)
                self.app_widget.setFixedHeight(650)
                self.app_widget.addWidget(window)
                self.app_widget.setCurrentIndex(self.app_widget.count() - 1)
            elif self.role == 'admin':
                query.exec(f"select worker_id from workers join users on workers.user_id=users.user_id where username='{username}' and user_password=HASHBYTES('SHA2_256', '{password}')")
                query.first()
                self.worker_id = query.value(0)
                self.invalid_auth_label.hide()
                window = AdminWindow(app_widget=self.app_widget, db=self.db, worker_id=self.worker_id, worker_username=username)
                self.username_line_edit.setText('')
                self.password_line_edit.setText('')
                self.app_widget.setFixedWidth(1200)
                self.app_widget.setFixedHeight(650)
                self.app_widget.addWidget(window)
                self.app_widget.setCurrentIndex(self.app_widget.count() - 1)

    def __register(self):
        window = RegistrationWindow(app_widget=self.app_widget, db=self.db)
        self.username_line_edit.setText('')
        self.password_line_edit.setText('')
        self.app_widget.setFixedWidth(550)
        self.app_widget.setFixedHeight(450)
        self.app_widget.addWidget(window)
        self.app_widget.setCurrentIndex(self.app_widget.count() - 1)
            