from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from ui_registration_window import Ui_RegistrationWindow
from datetime import datetime
import sys
# sys.path.append('D:/учеба/brewery/db_connection')
sys.path.append('D:/учеба/бд/курсач/brewery/db_connection')
from db_connection import DataBaseConnection

class RegistrationWindow(QtWidgets.QMainWindow, Ui_RegistrationWindow):
    def __init__(self, app_widget, db, *args, **kwargs):
        super(RegistrationWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app_widget = app_widget
        self.app_widget.setFixedWidth(550)
        self.app_widget.setFixedHeight(450)
        self.db = db
        self.invalid_company_name_label.hide()
        self.invalid_email_label.hide()
        self.invalid_phone_number_label.hide()
        self.invalid_address_label.hide()
        self.invalid_password_label.hide()
        self.passwords_match_label.hide()
        self.registration_label.hide()
        self.register_button.clicked.connect(self.__register)
        self.authorisation_button.clicked.connect(self.__back_to_authorisation)

    def __back_to_authorisation(self):
        self.app_widget.setFixedWidth(500)
        self.app_widget.setFixedHeight(500)
        self.app_widget.setCurrentIndex(0)

    def __register(self):
        self.invalid_company_name_label.hide()
        self.invalid_email_label.hide()
        self.invalid_phone_number_label.hide()
        self.invalid_address_label.hide()
        self.invalid_password_label.hide()
        self.passwords_match_label.hide()
        company_name = self.company_name_line.text()
        email = self.email_line.text()
        phone_number = self.phone_number_line.text()
        address = self.address_line.text()
        password = self.password_line.text()
        confirmed_password = self.confirm_password_line.text()
        print('--', company_name, email, phone_number, address, password, confirmed_password)
        query = QSqlQuery()
        query.exec(f'exec InsertCustomer {company_name}, "{email}", "{phone_number}", "{address}", "{password}"')
        if query.lastError().text() == '':
            self.company_name_line.setReadOnly(True)
            self.email_line.setReadOnly(True)
            self.phone_number_line.setReadOnly(True)
            self.address_line.setReadOnly(True)
            self.password_line.setReadOnly(True)
            self.confirm_password_line.setReadOnly(True)
            self.register_button.setEnabled(False)
            self.registration_label.show()
        else:
            print(query.lastError().text())
            if company_name == '':
                self.invalid_company_name_label.setText('\u274c Empty field')
                self.invalid_company_name_label.show()
            if email == '':
                self.invalid_email_label.setText('\u274c Empty field')
                self.invalid_email_label.show()
            if query.lastError().text().__contains__('LEFT'):
                self.invalid_email_label.setText('\u274c Incorrect email')
                self.invalid_email_label.show() 
            if query.lastError().databaseText().__contains__('@'):
                self.invalid_email_label.setText('\u274c This email is already used!')
                self.invalid_email_label.show()
            if phone_number == '':
                self.invalid_phone_number_label.setText('\u274c Empty field')
                self.invalid_phone_number_label.show()
            if query.lastError().text().__contains__('CK_CUSTOMER_PHONE_NUMBER'):
                self.invalid_phone_number_label.setText('\u274c Incorrect number')
                self.invalid_phone_number_label.show()
            if query.lastError().text().__contains__('UQ_CUSTOMER_PHONE_NUMBER'):
                self.invalid_phone_number_label.setText('\u274c This phone number is already used!')
                self.invalid_phone_number_label.show()   
                print('aboba')
            if address == '':
                self.invalid_address_label.setText('\u274c Empty field')
                self.invalid_address_label.show()
            if password == '':
                self.invalid_password_label.setText('\u274c Empty field')
                self.invalid_password_label.show()
            if confirmed_password != password:
                self.passwords_match_label.setText("\u274c Passwords don't match")
                self.passwords_match_label.show()
            