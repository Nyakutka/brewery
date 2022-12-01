from PyQt6.QtSql import QSqlQuery
from PyQt6 import QtCore, QtWidgets
from ui.ui_customer_window import Ui_CustomerForm

class CustomerWindow(QtWidgets.QMainWindow, Ui_CustomerForm):
    def __init__(self, app_widget, db, customer_id: int, customer_username: str, *args, **kwargs):
        super(CustomerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app_widget = app_widget
        self.db = db
        self.username = customer_username
        self.signed_label.setText(f"You are signed in as customer: {customer_username}")
        self.customer_id = customer_id
        self.initTab()
        self.customer_tab_widget.currentChanged.connect(self.initTab)
        self.cancel_new_order_button.clicked.connect(self.__cancel_new_order_mode)
        self.new_order_button.clicked.connect(self.__initCatalogTab_new_order_mode)
        self.submit_new_order_button.clicked.connect(self.__submit_order)
        self.sign_out_button.clicked.connect(self.__sign_out)

    def __cancel_new_order_mode(self):
        qm = QtWidgets.QMessageBox()
        ret = qm.question(self,'Confirmation', "Cancel creating order?", qm.StandardButton.Yes | qm.StandardButton.No)

        if ret == qm.StandardButton.Yes:
            self.__initCatalogTab()

    def __sign_out(self):
        qm = QtWidgets.QMessageBox()
        ret = qm.question(self,'Confirmation', "Sign out?", qm.StandardButton.Yes | qm.StandardButton.No)

        if ret == qm.StandardButton.Yes:
            self.app_widget.setFixedWidth(500)
            self.app_widget.setFixedHeight(500)
            self.app_widget.setCurrentIndex(0)

    def handle_show_details_button_clicked(self):
        self.hide_details_button.clicked.connect(self.__initOrdersTab)
        self.order_number_label.show()
        self.details_table_widget.show()
        self.hide_details_button.show()
        self.details_table_widget.setRowCount(0)
        self.details_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        order_number = self.orders_table_widget.item(self.orders_table_widget.currentRow(), 0).text()
        self.order_number_label.setText("Details of Order: " + order_number)
        qry = QSqlQuery(f'exec ShowOrderDetails {order_number}')
        while qry.next():
            rows = self.details_table_widget.rowCount()
            self.details_table_widget.setRowCount(rows + 1)
            for i in range(self.details_table_widget.columnCount()):
                value = str(qry.value(i))
                self.details_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))

    def __initCatalogTab(self):
        self.new_order_button.setEnabled(True)
        
        self.submit_new_order_button.hide()
        self.new_order_table_widget.hide()
        self.cancel_new_order_button.hide()
        
        self.total_cost_label.hide()
        self.total_cost_label_value.setText('0')
        self.total_cost_label_value.hide()
        query = QSqlQuery('exec ShowProductsCatalog')
        self.catalog_table_widget.setRowCount(0)
        self.new_order_table_widget.setRowCount(0)
        self.catalog_table_widget.setColumnCount(4)
        while query.next():
            rows = self.catalog_table_widget.rowCount()
            self.catalog_table_widget.setRowCount(rows + 1)
            for i in range(self.catalog_table_widget.columnCount()):
                value = str(query.value(i))
                self.catalog_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
            self.catalog_table_widget.resizeRowsToContents()

        self.catalog_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def __initCatalogTab_new_order_mode(self):
        self.new_order_button.setEnabled(False)
        self.new_order_table_widget.show()

        
        if self.new_order_table_widget.rowCount() > 0:
            self.submit_new_order_button.show()
        else:
            self.submit_new_order_button.hide()
        
        self.cancel_new_order_button.show()
        self.total_cost_label.show()
        self.total_cost_label_value.show()
        query = QSqlQuery('exec ShowProductsCatalog')
        self.catalog_table_widget.setRowCount(0)
        self.catalog_table_widget.setColumnCount(5)
        self.catalog_table_widget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem())
        self.catalog_table_widget.horizontalHeaderItem(4).setText("")
        while query.next():
            rows = self.catalog_table_widget.rowCount()
            self.catalog_table_widget.setRowCount(rows + 1)
            for i in range(self.catalog_table_widget.columnCount() - 1):
                value = str(query.value(i))
                self.catalog_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
            self.catalog_table_widget.resizeRowsToContents()
            add_to_cart = QtWidgets.QPushButton('+')

            add_to_cart.clicked.connect(self.handle_add_to_cart_button)
            add_to_cart.clicked.connect(self.update_total_cost_value)

            self.catalog_table_widget.setCellWidget(rows, self.catalog_table_widget.columnCount() - 1, add_to_cart)

        self.catalog_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def update_total_cost_value(self):
        if self.new_order_table_widget.rowCount() == 0:
            self.total_cost_label_value.setText(str(0))
            self.submit_new_order_button.hide()
        else:
            self.total_cost_label_value.setText(str(round(sum([float(x.text()) for x in [self.new_order_table_widget.item(i, 3) for i in range(self.new_order_table_widget.rowCount())]]), 2)))
            self.submit_new_order_button.show()

    def handle_add_to_cart_button(self):
        if self.catalog_table_widget.cellWidget(self.catalog_table_widget.currentRow(), self.catalog_table_widget.currentColumn()).text() == '+':
            self.catalog_table_widget.cellWidget(self.catalog_table_widget.currentRow(), self.catalog_table_widget.currentColumn()).setText('-')
            rows = self.new_order_table_widget.rowCount()
            self.new_order_table_widget.setRowCount(rows + 1)
            product_name = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 0).text()
            price = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 3).text()

            self.new_order_table_widget.setItem(rows, 0, QtWidgets.QTableWidgetItem(product_name))
            self.new_order_table_widget.setItem(rows, 2, QtWidgets.QTableWidgetItem(price))
            self.new_order_table_widget.setItem(rows, 3, QtWidgets.QTableWidgetItem(price))
            self.update_total_cost_value()
            amount_spin_box = QtWidgets.QSpinBox()
            amount_spin_box.setMaximum(500)
            amount_spin_box.setValue(1)
            amount_spin_box.valueChanged.connect(lambda x: self.new_order_table_widget.setItem(self.new_order_table_widget.currentRow(), 3, QtWidgets.QTableWidgetItem(str(round(float(price)*float(amount_spin_box.value()), 2)))))
            amount_spin_box.valueChanged.connect(lambda x: self.catalog_table_widget.cellWidget(self.catalog_table_widget.row(self.catalog_table_widget.findItems(self.new_order_table_widget.item(self.new_order_table_widget.currentRow(), 0).text(), QtCore.Qt.MatchFlag.MatchExactly)[0]), 4).setText('+') if amount_spin_box.value() == 0 else 1)
            amount_spin_box.valueChanged.connect(lambda x: self.new_order_table_widget.removeRow(self.new_order_table_widget.currentRow()) if amount_spin_box.value() == 0 else 1)
            amount_spin_box.valueChanged.connect(self.update_total_cost_value)
            self.new_order_table_widget.setCellWidget(rows, 1, amount_spin_box)
        else:
            product_name = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 0).text()
            self.catalog_table_widget.cellWidget(self.catalog_table_widget.currentRow(), self.catalog_table_widget.currentColumn()).setText('+')
            self.new_order_table_widget.removeRow(self.new_order_table_widget.row(self.new_order_table_widget.findItems(product_name, QtCore.Qt.MatchFlag.MatchExactly)[0]))

        if self.new_order_table_widget.rowCount() > 0:
            self.submit_new_order_button.show()
        else:
            self.submit_new_order_button.hide()
        
    def __submit_order(self):
        qm = QtWidgets.QMessageBox()
        ret = qm.question(self,'Confirmation', "Submit new order?", qm.StandardButton.Yes | qm.StandardButton.No)

        if ret == qm.StandardButton.Yes:
            query = QSqlQuery(f'exec InsertOrder {self.customer_id}, "{QtCore.QDateTime.currentDateTime().toString(QtCore.Qt.DateFormat.ISODate)}"')
            query.exec()
            self.__initOrdersTab()
            order_number = int(self.orders_table_widget.item(self.orders_table_widget.rowCount() - 1, 0).text())
            for i in range(self.new_order_table_widget.rowCount()):
                product_name = self.new_order_table_widget.item(i, 0).text()
                qry = QSqlQuery()
                qry.exec(f"select product_id from products where product_name='{product_name}'")
                qry.first()
                product_id = qry.value(0)
                amount = self.new_order_table_widget.cellWidget(i, 1).value()
                query = QSqlQuery(f'exec InsertOrder_details {order_number}, {product_id}, {amount}')
                query.exec()
        
            self.__initCatalogTab()

    def __initOrdersTab(self):
        if self.status_filter_comboBox.count() == 0:
            self.status_filter_comboBox.addItems(['all', 'pending', 'processing', 'cancelled', 'completed'])
        self.status_filter_comboBox.currentTextChanged.connect(self.initTab)
        
        self.order_number_label.hide()
        self.details_table_widget.hide()
        self.hide_details_button.hide()
        self.orders_table_widget.setRowCount(0)
        if (self.status_filter_comboBox.currentText() == 'all'):
            query = QSqlQuery(f'exec ShowOrdersByCustomer_id_ForCustomer {self.customer_id}')
        else:
            query = QSqlQuery(f'exec ShowOrdersByCustomer_idAndOrder_status_ForCustomer {self.customer_id}, {self.status_filter_comboBox.currentText()}')

        while query.next():
            rows = self.orders_table_widget.rowCount()
            self.orders_table_widget.setRowCount(rows + 1)
            for i in range(self.orders_table_widget.columnCount() - 2):
                if (isinstance(query.value(i), QtCore.QDateTime)):
                    value = query.value(i).toString(format= QtCore.Qt.DateFormat.TextDate)
                else:
                    value = str(query.value(i))
                self.orders_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
            show_details_button = QtWidgets.QPushButton('show\ndetails')
            show_details_button.clicked.connect(self.handle_show_details_button_clicked)
            self.orders_table_widget.setCellWidget(rows,self.orders_table_widget.columnCount() -2, show_details_button)
            if query.value(2) == 'pending':
                cancel_order_button = QtWidgets.QPushButton('cancel\norder')
                cancel_order_button.clicked.connect(self.__cancel_order)
                self.orders_table_widget.setCellWidget(rows,self.orders_table_widget.columnCount() -1, cancel_order_button)
            self.orders_table_widget.resizeRowsToContents()
        
        self.orders_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def __cancel_order(self):
        qm = QtWidgets.QMessageBox()
        ret = qm.question(self,'Confirmation', "Cancel order?", qm.StandardButton.Yes | qm.StandardButton.No)

        if ret == qm.StandardButton.Yes:
            order_id = self.orders_table_widget.item(self.orders_table_widget.currentRow(), 0).text()
            query = QSqlQuery(f'exec UpdateOrderStatus {order_id}, "cancelled"')
            query.exec()
            self.__initOrdersTab()

    def __change_phone_number(self):
        if self.change_telephone_number_button.text() == 'Change':
            self.change_address_button.setEnabled(False)
            self.change_telephone_number_button.setText('submit')
            self.telephone_number_line.setReadOnly(False)
            self.telephone_number_line.setFocus()
        else:
            phone_number = self.telephone_number_line.text()
            address = self.address_line.toPlainText()
            query = QSqlQuery()
            query.exec(f'exec UpdateCustomer {self.customer_id}, "{phone_number}", "{address}"')
            if query.isActive() == False:
                if query.lastError().text().__contains__('UNIQUE'):
                    self.invalid_telephone_number_label.setText('This number belongs to another customer,\n try again or ask administrator to help')
                else:
                    self.invalid_telephone_number_label.setText('Invalid telephone number, try again')
                self.invalid_telephone_number_label.show()
                self.change_telephone_number_button.setText('Change')
                self.__change_phone_number()
            else:
                qm = QtWidgets.QMessageBox()
                ret = qm.question(self,'Confirmation', "Update telephon number?", qm.StandardButton.Yes | qm.StandardButton.No)

                if ret == qm.StandardButton.Yes:
                    self.change_address_button.setEnabled(True)
                    self.invalid_telephone_number_label.hide()
                    self.change_telephone_number_button.setText('Change')
                    self.telephone_number_line.setReadOnly(True)
            
    def __change_address(self):
        if self.change_address_button.text() == 'Change':
            self.change_telephone_number_button.setEnabled(False)
            self.change_address_button.setText('submit')
            self.address_line.setReadOnly(False)
            self.address_line.setFocus()
        else:
            phone_number = self.telephone_number_line.text()
            address = self.address_line.toPlainText()
            query = QSqlQuery()
            query.exec(f'exec UpdateCustomer {self.customer_id}, "{phone_number}", "{address}"')
            if query.isActive() == False:
                self.invalid_address_label.show()
                self.change_address_button.setText('Change')
                self.__change_address()
            else:
                qm = QtWidgets.QMessageBox()
                ret = qm.question(self,'Confirmation', "Update address?", qm.StandardButton.Yes | qm.StandardButton.No)

                if ret == qm.StandardButton.Yes:
                    self.change_telephone_number_button.setEnabled(True)
                    self.invalid_address_label.hide()
                    self.change_address_button.setText('Change')
                    self.address_line.setReadOnly(True)

    def __init_account_tab(self):
        self.invalid_address_label.hide()
        self.invalid_telephone_number_label.hide()
        self.change_telephone_number_button.clicked.connect(self.__change_phone_number)
        self.change_address_button.clicked.connect(self.__change_address)
        self.telephone_number_line.setReadOnly(True)
        self.change_telephone_number_button.setText('Change')
        self.address_line.setReadOnly(True)
        self.change_address_button.setText('Change')
        query = QSqlQuery()
        query.exec(f'select customer_name, email, phone_number, address from customers where customer_id={self.customer_id}')
        query.first()
        self.username_line.setText(self.username)
        self.name_line.setText(query.value(0))
        self.email_line.setText(query.value(1))
        self.telephone_number_line.setText(query.value(2))
        self.address_line.setText(query.value(3))

    def initTab(self):
        if (self.customer_tab_widget.currentIndex() == 0):
            self.__initCatalogTab()
        elif (self.customer_tab_widget.currentIndex() == 1):
            self.__initOrdersTab()
        elif(self.customer_tab_widget.currentIndex() == 2):
            self.__init_account_tab()
