# Form implementation generated from reading ui file 'd:\учеба\бд\курсач\brewery\front\worker\ui\worker_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WorkerWindow(object):
    def setupUi(self, WorkerWindow):
        WorkerWindow.setObjectName("WorkerWindow")
        WorkerWindow.resize(1200, 650)
        self.centralwidget = QtWidgets.QWidget(WorkerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.worker_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.worker_tab_widget.setGeometry(QtCore.QRect(0, 50, 1200, 600))
        self.worker_tab_widget.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.worker_tab_widget.setToolTip("")
        self.worker_tab_widget.setObjectName("worker_tab_widget")
        self.catalog_tab = QtWidgets.QWidget()
        self.catalog_tab.setObjectName("catalog_tab")
        self.catalog_table_widget = QtWidgets.QTableWidget(self.catalog_tab)
        self.catalog_table_widget.setGeometry(QtCore.QRect(10, 10, 711, 521))
        self.catalog_table_widget.setMouseTracking(False)
        self.catalog_table_widget.setTabletTracking(False)
        self.catalog_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.catalog_table_widget.setObjectName("catalog_table_widget")
        self.catalog_table_widget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.catalog_table_widget.setHorizontalHeaderItem(7, item)
        self.all_lack_table_widget = QtWidgets.QTableWidget(self.catalog_tab)
        self.all_lack_table_widget.setGeometry(QtCore.QRect(730, 350, 381, 181))
        self.all_lack_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.all_lack_table_widget.setObjectName("all_lack_table_widget")
        self.all_lack_table_widget.setColumnCount(2)
        self.all_lack_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.all_lack_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_lack_table_widget.setHorizontalHeaderItem(1, item)
        self.all_lack_label = QtWidgets.QLabel(self.catalog_tab)
        self.all_lack_label.setEnabled(True)
        self.all_lack_label.setGeometry(QtCore.QRect(730, 280, 141, 21))
        self.all_lack_label.setObjectName("all_lack_label")
        self.all_customer_filter_comboBox = QtWidgets.QComboBox(self.catalog_tab)
        self.all_customer_filter_comboBox.setGeometry(QtCore.QRect(730, 300, 231, 31))
        self.all_customer_filter_comboBox.setObjectName("all_customer_filter_comboBox")
        self.new_product_pushButton = QtWidgets.QPushButton(self.catalog_tab)
        self.new_product_pushButton.setGeometry(QtCore.QRect(730, 10, 91, 31))
        self.new_product_pushButton.setObjectName("new_product_pushButton")
        self.product_name_line_edit = QtWidgets.QLineEdit(self.catalog_tab)
        self.product_name_line_edit.setGeometry(QtCore.QRect(730, 60, 151, 20))
        self.product_name_line_edit.setObjectName("product_name_line_edit")
        self.product_name_label = QtWidgets.QLabel(self.catalog_tab)
        self.product_name_label.setGeometry(QtCore.QRect(730, 40, 81, 16))
        self.product_name_label.setObjectName("product_name_label")
        self.type_label = QtWidgets.QLabel(self.catalog_tab)
        self.type_label.setGeometry(QtCore.QRect(900, 40, 81, 16))
        self.type_label.setObjectName("type_label")
        self.type_line_edit = QtWidgets.QLineEdit(self.catalog_tab)
        self.type_line_edit.setGeometry(QtCore.QRect(900, 60, 151, 20))
        self.type_line_edit.setText("")
        self.type_line_edit.setObjectName("type_line_edit")
        self.upc_label = QtWidgets.QLabel(self.catalog_tab)
        self.upc_label.setGeometry(QtCore.QRect(730, 110, 81, 16))
        self.upc_label.setObjectName("upc_label")
        self.upc_line_edit = QtWidgets.QLineEdit(self.catalog_tab)
        self.upc_line_edit.setGeometry(QtCore.QRect(730, 130, 151, 20))
        self.upc_line_edit.setText("")
        self.upc_line_edit.setObjectName("upc_line_edit")
        self.prime_price_label = QtWidgets.QLabel(self.catalog_tab)
        self.prime_price_label.setGeometry(QtCore.QRect(900, 110, 81, 16))
        self.prime_price_label.setObjectName("prime_price_label")
        self.prime_price_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.catalog_tab)
        self.prime_price_doubleSpinBox.setGeometry(QtCore.QRect(900, 130, 81, 21))
        self.prime_price_doubleSpinBox.setMaximum(1000.0)
        self.prime_price_doubleSpinBox.setObjectName("prime_price_doubleSpinBox")
        self.amount_spinBox = QtWidgets.QSpinBox(self.catalog_tab)
        self.amount_spinBox.setGeometry(QtCore.QRect(1110, 130, 51, 21))
        self.amount_spinBox.setObjectName("amount_spinBox")
        self.amount_label = QtWidgets.QLabel(self.catalog_tab)
        self.amount_label.setGeometry(QtCore.QRect(1090, 110, 101, 16))
        self.amount_label.setObjectName("amount_label")
        self.submit_new_product_pushButton = QtWidgets.QPushButton(self.catalog_tab)
        self.submit_new_product_pushButton.setGeometry(QtCore.QRect(830, 10, 91, 31))
        self.submit_new_product_pushButton.setObjectName("submit_new_product_pushButton")
        self.cancel_new_product_pushButton = QtWidgets.QPushButton(self.catalog_tab)
        self.cancel_new_product_pushButton.setGeometry(QtCore.QRect(930, 10, 91, 31))
        self.cancel_new_product_pushButton.setObjectName("cancel_new_product_pushButton")
        self.discount_label = QtWidgets.QLabel(self.catalog_tab)
        self.discount_label.setGeometry(QtCore.QRect(990, 110, 81, 16))
        self.discount_label.setObjectName("discount_label")
        self.discount_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.catalog_tab)
        self.discount_doubleSpinBox.setGeometry(QtCore.QRect(990, 130, 81, 21))
        self.discount_doubleSpinBox.setMaximum(1.0)
        self.discount_doubleSpinBox.setSingleStep(0.01)
        self.discount_doubleSpinBox.setObjectName("discount_doubleSpinBox")
        self.retail_price_label = QtWidgets.QLabel(self.catalog_tab)
        self.retail_price_label.setGeometry(QtCore.QRect(900, 160, 81, 16))
        self.retail_price_label.setObjectName("retail_price_label")
        self.discount_price_label = QtWidgets.QLabel(self.catalog_tab)
        self.discount_price_label.setGeometry(QtCore.QRect(990, 160, 81, 16))
        self.discount_price_label.setObjectName("discount_price_label")
        self.retail_price__value_label = QtWidgets.QLabel(self.catalog_tab)
        self.retail_price__value_label.setGeometry(QtCore.QRect(900, 180, 81, 16))
        self.retail_price__value_label.setObjectName("retail_price__value_label")
        self.discount_price_value_label = QtWidgets.QLabel(self.catalog_tab)
        self.discount_price_value_label.setGeometry(QtCore.QRect(990, 180, 81, 16))
        self.discount_price_value_label.setObjectName("discount_price_value_label")
        self.invalid_upc_label = QtWidgets.QLabel(self.catalog_tab)
        self.invalid_upc_label.setGeometry(QtCore.QRect(730, 150, 151, 16))
        self.invalid_upc_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.invalid_upc_label.setObjectName("invalid_upc_label")
        self.invalid_product_name_label = QtWidgets.QLabel(self.catalog_tab)
        self.invalid_product_name_label.setGeometry(QtCore.QRect(730, 80, 151, 16))
        self.invalid_product_name_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.invalid_product_name_label.setObjectName("invalid_product_name_label")
        self.invalid_type_label = QtWidgets.QLabel(self.catalog_tab)
        self.invalid_type_label.setGeometry(QtCore.QRect(900, 80, 151, 16))
        self.invalid_type_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.invalid_type_label.setObjectName("invalid_type_label")
        self.submit_update_product_pushButton = QtWidgets.QPushButton(self.catalog_tab)
        self.submit_update_product_pushButton.setGeometry(QtCore.QRect(730, 200, 91, 31))
        self.submit_update_product_pushButton.setObjectName("submit_update_product_pushButton")
        self.cancel_update_product_pushButton = QtWidgets.QPushButton(self.catalog_tab)
        self.cancel_update_product_pushButton.setGeometry(QtCore.QRect(830, 200, 91, 31))
        self.cancel_update_product_pushButton.setObjectName("cancel_update_product_pushButton")
        self.worker_tab_widget.addTab(self.catalog_tab, "")
        self.orders_tab = QtWidgets.QWidget()
        self.orders_tab.setObjectName("orders_tab")
        self.status_filter_comboBox = QtWidgets.QComboBox(self.orders_tab)
        self.status_filter_comboBox.setGeometry(QtCore.QRect(770, 40, 231, 31))
        self.status_filter_comboBox.setObjectName("status_filter_comboBox")
        self.status_filter_label = QtWidgets.QLabel(self.orders_tab)
        self.status_filter_label.setGeometry(QtCore.QRect(770, 20, 81, 21))
        self.status_filter_label.setScaledContents(False)
        self.status_filter_label.setObjectName("status_filter_label")
        self.orders_table_widget = QtWidgets.QTableWidget(self.orders_tab)
        self.orders_table_widget.setGeometry(QtCore.QRect(30, 20, 721, 521))
        self.orders_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.orders_table_widget.setObjectName("orders_table_widget")
        self.orders_table_widget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table_widget.setHorizontalHeaderItem(7, item)
        self.details_table_widget = QtWidgets.QTableWidget(self.orders_tab)
        self.details_table_widget.setEnabled(True)
        self.details_table_widget.setGeometry(QtCore.QRect(770, 170, 381, 151))
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
        self.order_number_label.setGeometry(QtCore.QRect(770, 140, 111, 21))
        self.order_number_label.setObjectName("order_number_label")
        self.hide_details_button = QtWidgets.QPushButton(self.orders_tab)
        self.hide_details_button.setGeometry(QtCore.QRect(1070, 140, 75, 23))
        self.hide_details_button.setObjectName("hide_details_button")
        self.customer_filter_comboBox = QtWidgets.QComboBox(self.orders_tab)
        self.customer_filter_comboBox.setGeometry(QtCore.QRect(770, 100, 231, 31))
        self.customer_filter_comboBox.setObjectName("customer_filter_comboBox")
        self.customer_filter_label = QtWidgets.QLabel(self.orders_tab)
        self.customer_filter_label.setGeometry(QtCore.QRect(770, 80, 121, 21))
        self.customer_filter_label.setScaledContents(False)
        self.customer_filter_label.setObjectName("customer_filter_label")
        self.lack_table_widget = QtWidgets.QTableWidget(self.orders_tab)
        self.lack_table_widget.setGeometry(QtCore.QRect(770, 360, 381, 181))
        self.lack_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.lack_table_widget.setObjectName("lack_table_widget")
        self.lack_table_widget.setColumnCount(2)
        self.lack_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lack_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lack_table_widget.setHorizontalHeaderItem(1, item)
        self.lack_label = QtWidgets.QLabel(self.orders_tab)
        self.lack_label.setEnabled(True)
        self.lack_label.setGeometry(QtCore.QRect(770, 330, 141, 21))
        self.lack_label.setObjectName("lack_label")
        self.worker_tab_widget.addTab(self.orders_tab, "")
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
        self.email_label.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.email_label.setObjectName("email_label")
        self.email_line = QtWidgets.QLineEdit(self.account_tab)
        self.email_line.setGeometry(QtCore.QRect(40, 90, 211, 20))
        self.email_line.setReadOnly(True)
        self.email_line.setObjectName("email_line")
        self.first_name_label = QtWidgets.QLabel(self.account_tab)
        self.first_name_label.setGeometry(QtCore.QRect(40, 120, 81, 16))
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_line = QtWidgets.QLineEdit(self.account_tab)
        self.first_name_line.setGeometry(QtCore.QRect(40, 140, 211, 20))
        self.first_name_line.setReadOnly(True)
        self.first_name_line.setObjectName("first_name_line")
        self.second_name_label = QtWidgets.QLabel(self.account_tab)
        self.second_name_label.setGeometry(QtCore.QRect(40, 170, 81, 16))
        self.second_name_label.setObjectName("second_name_label")
        self.second_name_line = QtWidgets.QLineEdit(self.account_tab)
        self.second_name_line.setGeometry(QtCore.QRect(40, 190, 211, 20))
        self.second_name_line.setReadOnly(True)
        self.second_name_line.setObjectName("second_name_line")
        self.worker_tab_widget.addTab(self.account_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.customers_table_widget = QtWidgets.QTableWidget(self.tab)
        self.customers_table_widget.setGeometry(QtCore.QRect(10, 10, 561, 551))
        self.customers_table_widget.setObjectName("customers_table_widget")
        self.customers_table_widget.setColumnCount(4)
        self.customers_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.customers_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.customers_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.customers_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.customers_table_widget.setHorizontalHeaderItem(3, item)
        self.total_income_filter_comboBox = QtWidgets.QComboBox(self.tab)
        self.total_income_filter_comboBox.setGeometry(QtCore.QRect(740, 10, 151, 21))
        self.total_income_filter_comboBox.setObjectName("total_income_filter_comboBox")
        self.income_label = QtWidgets.QLabel(self.tab)
        self.income_label.setGeometry(QtCore.QRect(900, 10, 51, 16))
        self.income_label.setObjectName("income_label")
        self.total_income_label = QtWidgets.QLabel(self.tab)
        self.total_income_label.setGeometry(QtCore.QRect(590, 10, 141, 16))
        self.total_income_label.setObjectName("total_income_label")
        self.worker_tab_widget.addTab(self.tab, "")
        self.signed_label = QtWidgets.QLabel(self.centralwidget)
        self.signed_label.setGeometry(QtCore.QRect(870, 20, 211, 20))
        self.signed_label.setObjectName("signed_label")
        self.sign_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_out_button.setGeometry(QtCore.QRect(1080, 10, 91, 31))
        self.sign_out_button.setObjectName("sign_out_button")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(0, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        WorkerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WorkerWindow)
        self.worker_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WorkerWindow)

    def retranslateUi(self, WorkerWindow):
        _translate = QtCore.QCoreApplication.translate
        WorkerWindow.setWindowTitle(_translate("WorkerWindow", "MainWindow"))
        item = self.catalog_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("WorkerWindow", "Name"))
        item = self.catalog_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("WorkerWindow", "Type"))
        item = self.catalog_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("WorkerWindow", "UPC Code"))
        item = self.catalog_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("WorkerWindow", "Prime price"))
        item = self.catalog_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("WorkerWindow", "Retail price"))
        item = self.catalog_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("WorkerWindow", "Discount price"))
        item = self.catalog_table_widget.horizontalHeaderItem(6)
        item.setText(_translate("WorkerWindow", "Amount on stock"))
        item = self.all_lack_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("WorkerWindow", "Product Name"))
        item = self.all_lack_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("WorkerWindow", "Lack on stock"))
        self.all_lack_label.setText(_translate("WorkerWindow", "Products lack on stock"))
        self.new_product_pushButton.setText(_translate("WorkerWindow", "New product"))
        self.product_name_label.setText(_translate("WorkerWindow", "Product name"))
        self.type_label.setText(_translate("WorkerWindow", "Type"))
        self.upc_label.setText(_translate("WorkerWindow", "UPC"))
        self.prime_price_label.setText(_translate("WorkerWindow", "Prime price"))
        self.amount_label.setText(_translate("WorkerWindow", "Amount on stock"))
        self.submit_new_product_pushButton.setText(_translate("WorkerWindow", "Submit"))
        self.cancel_new_product_pushButton.setText(_translate("WorkerWindow", "Cancel"))
        self.discount_label.setText(_translate("WorkerWindow", "Discount"))
        self.retail_price_label.setText(_translate("WorkerWindow", "Retail price:"))
        self.discount_price_label.setText(_translate("WorkerWindow", "Discount price:"))
        self.retail_price__value_label.setText(_translate("WorkerWindow", "0"))
        self.discount_price_value_label.setText(_translate("WorkerWindow", "0"))
        self.invalid_upc_label.setText(_translate("WorkerWindow", "Invalid upc"))
        self.invalid_product_name_label.setText(_translate("WorkerWindow", "Invalid product name"))
        self.invalid_type_label.setText(_translate("WorkerWindow", "Invalid type"))
        self.submit_update_product_pushButton.setText(_translate("WorkerWindow", "Submit"))
        self.cancel_update_product_pushButton.setText(_translate("WorkerWindow", "Cancel"))
        self.worker_tab_widget.setTabText(self.worker_tab_widget.indexOf(self.catalog_tab), _translate("WorkerWindow", "Catalog"))
        self.status_filter_label.setText(_translate("WorkerWindow", "Filter by status:"))
        item = self.orders_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("WorkerWindow", "Order number"))
        item = self.orders_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("WorkerWindow", "Customer name"))
        item = self.orders_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("WorkerWindow", "Date"))
        item = self.orders_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("WorkerWindow", "Status"))
        item = self.orders_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("WorkerWindow", "Prime cost"))
        item = self.orders_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("WorkerWindow", "Cost"))
        item = self.details_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("WorkerWindow", "Product Name"))
        item = self.details_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("WorkerWindow", "Amount"))
        item = self.details_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("WorkerWindow", "Price"))
        item = self.details_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("WorkerWindow", "Cost"))
        self.order_number_label.setText(_translate("WorkerWindow", "Details of Order: "))
        self.hide_details_button.setText(_translate("WorkerWindow", "Hide"))
        self.customer_filter_label.setText(_translate("WorkerWindow", "Filter by customer:"))
        item = self.lack_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("WorkerWindow", "Product Name"))
        item = self.lack_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("WorkerWindow", "Lack on stock"))
        self.lack_label.setText(_translate("WorkerWindow", "Products lack on stock"))
        self.worker_tab_widget.setTabText(self.worker_tab_widget.indexOf(self.orders_tab), _translate("WorkerWindow", "Orders"))
        self.username_label.setText(_translate("WorkerWindow", "Username"))
        self.email_label.setText(_translate("WorkerWindow", "Email"))
        self.first_name_label.setText(_translate("WorkerWindow", "First name"))
        self.second_name_label.setText(_translate("WorkerWindow", "Second name"))
        self.worker_tab_widget.setTabText(self.worker_tab_widget.indexOf(self.account_tab), _translate("WorkerWindow", "My account"))
        item = self.customers_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("WorkerWindow", "Name"))
        item = self.customers_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("WorkerWindow", "Email"))
        item = self.customers_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("WorkerWindow", "Telephone Number"))
        item = self.customers_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("WorkerWindow", "Address"))
        self.income_label.setText(_translate("WorkerWindow", "Income"))
        self.total_income_label.setText(_translate("WorkerWindow", "Total income by customer"))
        self.worker_tab_widget.setTabText(self.worker_tab_widget.indexOf(self.tab), _translate("WorkerWindow", "Customers"))
        self.signed_label.setText(_translate("WorkerWindow", "You are signed as"))
        self.sign_out_button.setText(_translate("WorkerWindow", "Sign out"))
        self.welcome_label.setText(_translate("WorkerWindow", "Nyakutka\'s Brewery"))
