# Form implementation generated from reading ui file 'd:\учеба\бд\курсач\brewery\front\customer\ui\customer_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CustomerForm(object):
    def setupUi(self, CustomerForm):
        CustomerForm.setObjectName("CustomerForm")
        CustomerForm.resize(1001, 630)
        CustomerForm.setBaseSize(QtCore.QSize(1010, 618))
        self.customer_tab_widget = QtWidgets.QTabWidget(CustomerForm)
        self.customer_tab_widget.setGeometry(QtCore.QRect(0, 30, 1000, 600))
        self.customer_tab_widget.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.customer_tab_widget.setToolTip("")
        self.customer_tab_widget.setObjectName("customer_tab_widget")
        self.catalog_tab = QtWidgets.QWidget()
        self.catalog_tab.setObjectName("catalog_tab")
        self.catalog_table_widget = QtWidgets.QTableWidget(self.catalog_tab)
        self.catalog_table_widget.setGeometry(QtCore.QRect(30, 20, 451, 521))
        self.catalog_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.catalog_table_widget.setObjectName("catalog_table_widget")
        self.catalog_table_widget.setColumnCount(5)
        self.catalog_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(4, item)
        self.new_order_button = QtWidgets.QPushButton(self.catalog_tab)
        self.new_order_button.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.new_order_button.setObjectName("new_order_button")
        self.new_order_table_widget = QtWidgets.QTableWidget(self.catalog_tab)
        self.new_order_table_widget.setEnabled(True)
        self.new_order_table_widget.setGeometry(QtCore.QRect(510, 50, 421, 491))
        self.new_order_table_widget.setAutoFillBackground(False)
        self.new_order_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.new_order_table_widget.setObjectName("new_order_table_widget")
        self.new_order_table_widget.setColumnCount(4)
        self.new_order_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.new_order_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_order_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_order_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_order_table_widget.setHorizontalHeaderItem(3, item)
        self.submit_new_order_button = QtWidgets.QPushButton(self.catalog_tab)
        self.submit_new_order_button.setGeometry(QtCore.QRect(650, 20, 75, 23))
        self.submit_new_order_button.setObjectName("submit_new_order_button")
        self.cancel_new_order_button = QtWidgets.QPushButton(self.catalog_tab)
        self.cancel_new_order_button.setGeometry(QtCore.QRect(740, 20, 75, 23))
        self.cancel_new_order_button.setObjectName("cancel_new_order_button")
        self.total_cost_label = QtWidgets.QLabel(self.catalog_tab)
        self.total_cost_label.setGeometry(QtCore.QRect(840, 0, 61, 20))
        self.total_cost_label.setObjectName("total_cost_label")
        self.total_cost_label_value = QtWidgets.QLabel(self.catalog_tab)
        self.total_cost_label_value.setGeometry(QtCore.QRect(840, 20, 61, 20))
        self.total_cost_label_value.setObjectName("total_cost_label_value")
        self.customer_tab_widget.addTab(self.catalog_tab, "")
        self.orders_tab = QtWidgets.QWidget()
        self.orders_tab.setObjectName("orders_tab")
        self.status_filter_comboBox = QtWidgets.QComboBox(self.orders_tab)
        self.status_filter_comboBox.setGeometry(QtCore.QRect(630, 40, 231, 31))
        self.status_filter_comboBox.setObjectName("status_filter_comboBox")
        self.status_filter_label = QtWidgets.QLabel(self.orders_tab)
        self.status_filter_label.setGeometry(QtCore.QRect(630, 20, 81, 21))
        self.status_filter_label.setScaledContents(False)
        self.status_filter_label.setObjectName("status_filter_label")
        self.orders_table_widget = QtWidgets.QTableWidget(self.orders_tab)
        self.orders_table_widget.setGeometry(QtCore.QRect(30, 20, 571, 521))
        self.orders_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.orders_table_widget.setObjectName("orders_table_widget")
        self.orders_table_widget.setColumnCount(6)
        self.orders_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(5, item)
        self.details_table_widget = QtWidgets.QTableWidget(self.orders_tab)
        self.details_table_widget.setEnabled(True)
        self.details_table_widget.setGeometry(QtCore.QRect(630, 200, 301, 341))
        self.details_table_widget.setAutoFillBackground(False)
        self.details_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.details_table_widget.setObjectName("details_table_widget")
        self.details_table_widget.setColumnCount(4)
        self.details_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.details_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.details_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.details_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.details_table_widget.setHorizontalHeaderItem(3, item)
        self.order_number_label = QtWidgets.QLabel(self.orders_tab)
        self.order_number_label.setEnabled(True)
        self.order_number_label.setGeometry(QtCore.QRect(630, 170, 111, 21))
        self.order_number_label.setObjectName("order_number_label")
        self.hide_details_button = QtWidgets.QPushButton(self.orders_tab)
        self.hide_details_button.setGeometry(QtCore.QRect(770, 170, 75, 23))
        self.hide_details_button.setObjectName("hide_details_button")
        self.date_filter_comboBox = QtWidgets.QComboBox(self.orders_tab)
        self.date_filter_comboBox.setGeometry(QtCore.QRect(630, 100, 231, 31))
        self.date_filter_comboBox.setObjectName("date_filter_comboBox")
        self.date_filter_label = QtWidgets.QLabel(self.orders_tab)
        self.date_filter_label.setGeometry(QtCore.QRect(630, 80, 81, 21))
        self.date_filter_label.setScaledContents(False)
        self.date_filter_label.setObjectName("date_filter_label")
        self.customer_tab_widget.addTab(self.orders_tab, "")
        self.account_tab = QtWidgets.QWidget()
        self.account_tab.setObjectName("account_tab")
        self.username_line = QtWidgets.QLineEdit(self.account_tab)
        self.username_line.setGeometry(QtCore.QRect(40, 40, 113, 20))
        self.username_line.setReadOnly(True)
        self.username_line.setObjectName("username_line")
        self.username_label = QtWidgets.QLabel(self.account_tab)
        self.username_label.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.username_label.setObjectName("username_label")
        self.email_label = QtWidgets.QLabel(self.account_tab)
        self.email_label.setGeometry(QtCore.QRect(40, 120, 47, 13))
        self.email_label.setObjectName("email_label")
        self.telephone_number_label = QtWidgets.QLabel(self.account_tab)
        self.telephone_number_label.setGeometry(QtCore.QRect(40, 170, 101, 16))
        self.telephone_number_label.setObjectName("telephone_number_label")
        self.address_label = QtWidgets.QLabel(self.account_tab)
        self.address_label.setGeometry(QtCore.QRect(40, 220, 47, 13))
        self.address_label.setObjectName("address_label")
        self.email_line = QtWidgets.QLineEdit(self.account_tab)
        self.email_line.setGeometry(QtCore.QRect(40, 140, 211, 20))
        self.email_line.setReadOnly(True)
        self.email_line.setObjectName("email_line")
        self.telephone_number_line = QtWidgets.QLineEdit(self.account_tab)
        self.telephone_number_line.setGeometry(QtCore.QRect(40, 190, 151, 20))
        self.telephone_number_line.setReadOnly(True)
        self.telephone_number_line.setObjectName("telephone_number_line")
        self.name_label = QtWidgets.QLabel(self.account_tab)
        self.name_label.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.name_label.setObjectName("name_label")
        self.name_line = QtWidgets.QLineEdit(self.account_tab)
        self.name_line.setGeometry(QtCore.QRect(40, 90, 211, 20))
        self.name_line.setReadOnly(True)
        self.name_line.setObjectName("name_line")
        self.address_line = QtWidgets.QTextEdit(self.account_tab)
        self.address_line.setGeometry(QtCore.QRect(40, 240, 271, 71))
        self.address_line.setReadOnly(True)
        self.address_line.setObjectName("address_line")
        self.change_telephone_number_button = QtWidgets.QPushButton(self.account_tab)
        self.change_telephone_number_button.setGeometry(QtCore.QRect(210, 190, 75, 23))
        self.change_telephone_number_button.setObjectName("change_telephone_number_button")
        self.change_address_button = QtWidgets.QPushButton(self.account_tab)
        self.change_address_button.setGeometry(QtCore.QRect(330, 240, 75, 23))
        self.change_address_button.setObjectName("change_address_button")
        self.invalid_telephone_number_label = QtWidgets.QLabel(self.account_tab)
        self.invalid_telephone_number_label.setGeometry(QtCore.QRect(310, 190, 301, 31))
        self.invalid_telephone_number_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.invalid_telephone_number_label.setObjectName("invalid_telephone_number_label")
        self.invalid_address_label = QtWidgets.QLabel(self.account_tab)
        self.invalid_address_label.setGeometry(QtCore.QRect(420, 240, 201, 16))
        self.invalid_address_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.invalid_address_label.setObjectName("invalid_address_label")
        self.customer_tab_widget.addTab(self.account_tab, "")
        self.signed_label = QtWidgets.QLabel(CustomerForm)
        self.signed_label.setGeometry(QtCore.QRect(640, 20, 241, 20))
        self.signed_label.setObjectName("signed_label")
        self.sign_out_button = QtWidgets.QPushButton(CustomerForm)
        self.sign_out_button.setGeometry(QtCore.QRect(880, 10, 91, 31))
        self.sign_out_button.setObjectName("sign_out_button")
        self.welcome_label = QtWidgets.QLabel(CustomerForm)
        self.welcome_label.setGeometry(QtCore.QRect(0, -10, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")

        self.retranslateUi(CustomerForm)
        self.customer_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CustomerForm)

    def retranslateUi(self, CustomerForm):
        _translate = QtCore.QCoreApplication.translate
        CustomerForm.setWindowTitle(_translate("CustomerForm", "Form"))
        item = self.catalog_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("CustomerForm", "Name"))
        item = self.catalog_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("CustomerForm", "Type"))
        item = self.catalog_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("CustomerForm", "Retail price"))
        item = self.catalog_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("CustomerForm", "Discount price"))
        self.new_order_button.setText(_translate("CustomerForm", "New order"))
        item = self.new_order_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("CustomerForm", "Name"))
        item = self.new_order_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("CustomerForm", "Amount"))
        item = self.new_order_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("CustomerForm", "Price"))
        item = self.new_order_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("CustomerForm", "Cost"))
        self.submit_new_order_button.setText(_translate("CustomerForm", "Submit"))
        self.cancel_new_order_button.setText(_translate("CustomerForm", "Cancel"))
        self.total_cost_label.setText(_translate("CustomerForm", "Total Cost:"))
        self.total_cost_label_value.setText(_translate("CustomerForm", "0"))
        self.customer_tab_widget.setTabText(self.customer_tab_widget.indexOf(self.catalog_tab), _translate("CustomerForm", "Catalog"))
        self.status_filter_label.setText(_translate("CustomerForm", "Filter by status:"))
        item = self.orders_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("CustomerForm", "Order number"))
        item = self.orders_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("CustomerForm", "Date"))
        item = self.orders_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("CustomerForm", "Status"))
        item = self.orders_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("CustomerForm", "Cost"))
        item = self.details_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("CustomerForm", "Product Name"))
        item = self.details_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("CustomerForm", "Amount"))
        item = self.details_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("CustomerForm", "Price"))
        item = self.details_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("CustomerForm", "Cost"))
        self.order_number_label.setText(_translate("CustomerForm", "Details of Order: "))
        self.hide_details_button.setText(_translate("CustomerForm", "Hide"))
        self.date_filter_label.setText(_translate("CustomerForm", "Filter by date:"))
        self.customer_tab_widget.setTabText(self.customer_tab_widget.indexOf(self.orders_tab), _translate("CustomerForm", "My orders"))
        self.username_label.setText(_translate("CustomerForm", "Username"))
        self.email_label.setText(_translate("CustomerForm", "Email"))
        self.telephone_number_label.setText(_translate("CustomerForm", "Telephone number"))
        self.address_label.setText(_translate("CustomerForm", "Address"))
        self.name_label.setText(_translate("CustomerForm", "Name"))
        self.change_telephone_number_button.setText(_translate("CustomerForm", "Change"))
        self.change_address_button.setText(_translate("CustomerForm", "Change"))
        self.invalid_telephone_number_label.setText(_translate("CustomerForm", "Invalid telephone number, try again"))
        self.invalid_address_label.setText(_translate("CustomerForm", "Invalid address, try again"))
        self.customer_tab_widget.setTabText(self.customer_tab_widget.indexOf(self.account_tab), _translate("CustomerForm", "My account"))
        self.signed_label.setText(_translate("CustomerForm", "You are signed as"))
        self.sign_out_button.setText(_translate("CustomerForm", "Sign out"))
        self.welcome_label.setText(_translate("CustomerForm", "Nyakutka\'s Brewery"))
