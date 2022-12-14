# Form implementation generated from reading ui file 'd:\учеба\бд\курсач\brewery\front\authorisation\ui\registration_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(550, 450)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.registration_label = QtWidgets.QLabel(self.centralwidget)
        self.registration_label.setGeometry(QtCore.QRect(190, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.registration_label.setFont(font)
        self.registration_label.setObjectName("registration_label")
        self.company_name_label = QtWidgets.QLabel(self.centralwidget)
        self.company_name_label.setGeometry(QtCore.QRect(140, 40, 121, 16))
        self.company_name_label.setObjectName("company_name_label")
        self.company_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.company_name_line.setGeometry(QtCore.QRect(140, 60, 171, 20))
        self.company_name_line.setObjectName("company_name_line")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(140, 90, 81, 16))
        self.email_label.setObjectName("email_label")
        self.email_line = QtWidgets.QLineEdit(self.centralwidget)
        self.email_line.setGeometry(QtCore.QRect(140, 110, 171, 20))
        self.email_line.setObjectName("email_line")
        self.phone_number_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_number_label.setGeometry(QtCore.QRect(140, 140, 81, 16))
        self.phone_number_label.setObjectName("phone_number_label")
        self.phone_number_line = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_number_line.setGeometry(QtCore.QRect(140, 160, 171, 20))
        self.phone_number_line.setObjectName("phone_number_line")
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(140, 190, 81, 16))
        self.address_label.setObjectName("address_label")
        self.address_line = QtWidgets.QLineEdit(self.centralwidget)
        self.address_line.setGeometry(QtCore.QRect(140, 210, 171, 41))
        self.address_line.setObjectName("address_line")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(140, 260, 81, 16))
        self.password_label.setObjectName("password_label")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(140, 280, 171, 20))
        self.password_line.setObjectName("password_line")
        self.confirm_password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_line.setGeometry(QtCore.QRect(140, 330, 171, 20))
        self.confirm_password_line.setObjectName("confirm_password_line")
        self.confirm_password_label = QtWidgets.QLabel(self.centralwidget)
        self.confirm_password_label.setGeometry(QtCore.QRect(140, 310, 101, 16))
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(50, 360, 171, 51))
        self.register_button.setObjectName("register_button")
        self.invalid_email_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_email_label.setGeometry(QtCore.QRect(320, 110, 161, 16))
        self.invalid_email_label.setStyleSheet("")
        self.invalid_email_label.setObjectName("invalid_email_label")
        self.invalid_phone_number_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_phone_number_label.setGeometry(QtCore.QRect(320, 160, 221, 16))
        self.invalid_phone_number_label.setStyleSheet("")
        self.invalid_phone_number_label.setObjectName("invalid_phone_number_label")
        self.invalid_address_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_address_label.setGeometry(QtCore.QRect(320, 210, 161, 16))
        self.invalid_address_label.setStyleSheet("")
        self.invalid_address_label.setObjectName("invalid_address_label")
        self.invalid_password_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_password_label.setGeometry(QtCore.QRect(320, 280, 161, 16))
        self.invalid_password_label.setStyleSheet("")
        self.invalid_password_label.setObjectName("invalid_password_label")
        self.passwords_match_label = QtWidgets.QLabel(self.centralwidget)
        self.passwords_match_label.setGeometry(QtCore.QRect(320, 310, 161, 16))
        self.passwords_match_label.setStyleSheet("")
        self.passwords_match_label.setObjectName("passwords_match_label")
        self.authorisation_button = QtWidgets.QPushButton(self.centralwidget)
        self.authorisation_button.setGeometry(QtCore.QRect(240, 380, 161, 31))
        self.authorisation_button.setObjectName("authorisation_button")
        self.invalid_company_name_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_company_name_label.setGeometry(QtCore.QRect(320, 60, 161, 16))
        self.invalid_company_name_label.setStyleSheet("")
        self.invalid_company_name_label.setObjectName("invalid_company_name_label")
        RegistrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "MainWindow"))
        self.registration_label.setText(_translate("RegistrationWindow", "Registration"))
        self.company_name_label.setText(_translate("RegistrationWindow", "Company name"))
        self.email_label.setText(_translate("RegistrationWindow", "Email"))
        self.phone_number_label.setText(_translate("RegistrationWindow", "Phone number"))
        self.address_label.setText(_translate("RegistrationWindow", "Address"))
        self.password_label.setText(_translate("RegistrationWindow", "Password"))
        self.confirm_password_label.setText(_translate("RegistrationWindow", "Confirm password"))
        self.register_button.setText(_translate("RegistrationWindow", "Register"))
        self.invalid_email_label.setText(_translate("RegistrationWindow", "✓"))
        self.invalid_phone_number_label.setText(_translate("RegistrationWindow", "✓"))
        self.invalid_address_label.setText(_translate("RegistrationWindow", "✓"))
        self.invalid_password_label.setText(_translate("RegistrationWindow", "✓"))
        self.passwords_match_label.setText(_translate("RegistrationWindow", "✓"))
        self.authorisation_button.setText(_translate("RegistrationWindow", "Back to authorisation"))
        self.invalid_company_name_label.setText(_translate("RegistrationWindow", "✓"))
