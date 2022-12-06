from PyQt6.QtSql import QSqlQuery
from PyQt6 import QtCore, QtWidgets, QtGui
from ui.ui_worker_window import Ui_WorkerWindow

class WorkerWindow(QtWidgets.QMainWindow, Ui_WorkerWindow):
    def __init__(self, app_widget, db, worker_id: int, worker_username: str, *args, **kwargs):
        super(WorkerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app_widget = app_widget
        self.username = worker_username
        self.signed_label.setText(f"You are signed in as worker: {worker_username}")
        self.db = db
        self.worker_id = worker_id
        self.initTab()
        self.worker_tab_widget.currentChanged.connect(self.initTab)
        self.status_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.customer_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.date_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.all_customer_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.total_income_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.sign_out_button.clicked.connect(self.__sign_out)
        self.new_product_pushButton.clicked.connect(self.__new_product)
        self.cancel_new_product_pushButton.clicked.connect(self.__initCatalogTab)
        self.submit_new_product_pushButton.clicked.connect(self.__submit_new_product)
        self.prime_price_doubleSpinBox.valueChanged.connect(self.__update_retail_price_label)
        self.prime_price_doubleSpinBox.valueChanged.connect(self.__update_discount_price_label)
        self.discount_doubleSpinBox.valueChanged.connect(self.__update_discount_price_label)
        self.submit_update_product_pushButton.clicked.connect(self.__submit_update_product)
        self.cancel_update_product_pushButton.clicked.connect(self.__initCatalogTab)

    def __submit_update_product(self):
        product_name = self.product_name_line_edit.text()
        type = self.type_line_edit.text()
        upc = self.upc_line_edit.text()
        prime_price = self.prime_price_doubleSpinBox.value()
        discount = self.discount_doubleSpinBox.value()
        amount = self.amount_spinBox.value()
        prew_product_name = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 0).text()

        qm = QtWidgets.QMessageBox()
        qm.setText(f"Update product {prew_product_name}?")
        qm.setWindowTitle("Confirmation")
        qm.setStandardButtons(qm.StandardButton.Yes | qm.StandardButton.No)
        qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_question.jpg"))
        ret = qm.exec()

        if ret == qm.StandardButton.Yes:
            query = QSqlQuery()
            query.exec(f"select product_id from products where product_name='{prew_product_name}'")
            query.first()
            product_id = query.value(0)
            query = QSqlQuery()
            
            query.exec(f'exec UpdateProduct {product_id}, "{product_name}", {type}, {upc}, {prime_price}, {discount}, {amount}')
            if query.lastError().text() == '':
                qm = QtWidgets.QMessageBox()
                qm.setText(f"Product {product_name} was updated")
                qm.setWindowTitle("Successful")
                qm.setStandardButtons(qm.StandardButton.Ok)
                qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_ok.jpg"))
                ret = qm.exec()

                if ret == qm.StandardButton.Ok:
                    self.__initCatalogTab()
            else:
                if product_name == '':
                    self.invalid_product_name_label.setText('Invalid product name')
                    self.invalid_product_name_label.show()
                elif query.lastError().text().__contains__('UQ_PRODUCT_NAME'):
                    self.invalid_product_name_label.setText('Product with this name exists')
                    self.invalid_product_name_label.show()
                else:
                    self.invalid_product_name_label.hide()
                if len(upc) != 12:
                    self.invalid_upc_label.setText('Invalid upc')
                    self.invalid_upc_label.show()
                elif query.lastError().text().__contains__('UQ_PRODUCT_UPC'):
                    self.invalid_upc_label.setText('Product with this upc exists')
                    self.invalid_upc_label.show()
                else:
                    self.invalid_upc_label.hide()
                if type == '':
                    self.invalid_type_label.show()
                else:
                    self.invalid_type_label.hide()
            

    def __update_discount_price_label(self):
        retail_price = float(self.retail_price__value_label.text())
        discount = self.discount_doubleSpinBox.value()
        self.discount_price_value_label.setText(str(round(retail_price * (1 - discount), 2)))

    def __update_retail_price_label(self):
        prime_price = self.prime_price_doubleSpinBox.value()
        self.retail_price__value_label.setText(str(round(prime_price * 1.38, 2)))

    def __new_product(self):
        self.new_product_pushButton.setEnabled(False)
        self.submit_new_product_pushButton.show()
        self.cancel_new_product_pushButton.show()
        self.product_name_label.show()
        self.product_name_line_edit.show()
        self.product_name_line_edit.setText('')
        self.type_label.show()
        self.type_line_edit.show()
        self.type_line_edit.setText('')
        self.upc_label.show()
        self.upc_line_edit.show()
        self.upc_line_edit.setText('')
        self.prime_price_label.show()
        self.prime_price_doubleSpinBox.show()
        self.prime_price_doubleSpinBox.setValue(0)
        self.retail_price_label.show()
        self.retail_price__value_label.show()
        self.discount_label.show()
        self.discount_doubleSpinBox.show()
        self.discount_doubleSpinBox.setValue(0)
        self.discount_price_label.show()
        self.discount_price_value_label.show()
        self.amount_label.show()
        self.amount_spinBox.show()
        self.amount_spinBox.setValue(0)

    def __submit_new_product(self):
        product_name = self.product_name_line_edit.text()
        type = self.type_line_edit.text()
        upc = self.upc_line_edit.text()
        prime_price = self.prime_price_doubleSpinBox.value()
        discount = self.discount_doubleSpinBox.value()
        amount = self.amount_spinBox.value()
        
        query = QSqlQuery()
        query.exec(f'exec InsertProduct "{product_name}", {type}, {upc}, {prime_price}, {discount}, {amount}')
        if query.lastError().text() == '':
            qm = QtWidgets.QMessageBox()
            qm.setText(f"Product {product_name} was added to catalog")
            qm.setWindowTitle("Successful")
            qm.setStandardButtons(qm.StandardButton.Ok)
            qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_ok.jpg"))
            ret = qm.exec()

            if ret == qm.StandardButton.Ok:
                self.initTab()

        else:
            if product_name == '':
                self.invalid_product_name_label.setText('Invalid product name')
                self.invalid_product_name_label.show()
            elif query.lastError().text().__contains__('UQ_PRODUCT_NAME'):
                self.invalid_product_name_label.setText('Product with this name exists')
                self.invalid_product_name_label.show()
            else:
                self.invalid_product_name_label.hide()
            if len(upc) != 12:
                self.invalid_upc_label.setText('Invalid upc')
                self.invalid_upc_label.show()
            elif query.lastError().text().__contains__('UQ_PRODUCT_UPC'):
                self.invalid_upc_label.setText('product with this upc exists')
                self.invalid_upc_label.show()
            else:
                self.invalid_upc_label.hide()
            if type == '':
                self.invalid_type_label.show()
            else:
                self.invalid_type_label.hide()

    def __sign_out(self):
        qm = QtWidgets.QMessageBox()
        qm.setText(f"Sign out?")
        qm.setWindowTitle("Confirmation")
        qm.setStandardButtons(qm.StandardButton.Yes | qm.StandardButton.No)
        qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_question.jpg"))
        ret = qm.exec()

        if ret == qm.StandardButton.Yes:
            self.app_widget.setFixedWidth(500)
            self.app_widget.setFixedHeight(500)
            self.app_widget.setCurrentIndex(0)

    def initTab(self):
        if (self.worker_tab_widget.currentIndex() == 0):
            self.__initCatalogTab()
        elif (self.worker_tab_widget.currentIndex() == 1):
            self.__initOrdersTab()
        elif (self.worker_tab_widget.currentIndex() == 2):
            self.__initAccountTab()
        elif (self.worker_tab_widget.currentIndex() == 3):
            self.__initCustomersTab()

    def __initCustomersTab(self):
        query = QSqlQuery('exec ShowCustomers')
        self.customers_table_widget.setRowCount(0)
        self.customers_table_widget.setColumnCount(4)
        while query.next():   
            rows = self.customers_table_widget.rowCount()
            self.customers_table_widget.setRowCount(rows + 1)
            for i in range(self.customers_table_widget.columnCount()):
                value = str(query.value(i))
                self.customers_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
        self.customers_table_widget.resizeRowsToContents()
        self.customers_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        if self.total_income_filter_comboBox.count() == 0:
            customer_names_query = QSqlQuery()
            customer_names_query.exec('select customer_name from customers')
            customer_names = ['all']
            while customer_names_query.next():
                customer_names.append(customer_names_query.value(0))
            self.total_income_filter_comboBox.addItems(customer_names)
        if self.total_income_filter_comboBox.currentText() == 'all':
            query = QSqlQuery(f'exec ShowAllIncome')
        else:
            query = QSqlQuery(f'exec ShowIncomeByCustomer_name "{self.total_income_filter_comboBox.currentText()}"')
        query.next()
        value = str(query.value(0))
        self.income_label.setText(value)
        

    def __initAccountTab(self):
        query = QSqlQuery()
        query.exec(f'select email, first_name, second_name from workers where worker_id={self.worker_id}')
        query.first()
        self.username_line.setText(self.username)
        self.email_line.setText(query.value(0))
        self.first_name_line.setText(query.value(1))
        self.second_name_line.setText(query.value(2))        

    def __initCatalogTab(self):
        self.new_product_pushButton.setEnabled(True)
        self.submit_new_product_pushButton.hide()
        self.cancel_new_product_pushButton.hide()
        self.product_name_label.hide()
        self.product_name_line_edit.hide()
        self.type_label.hide()
        self.type_line_edit.hide()
        self.upc_label.hide()
        self.upc_line_edit.hide()
        self.prime_price_label.hide()
        self.prime_price_doubleSpinBox.hide()
        self.retail_price_label.hide()
        self.retail_price__value_label.hide()
        self.discount_label.hide()
        self.discount_doubleSpinBox.hide()
        self.discount_price_label.hide()
        self.discount_price_value_label.hide()
        self.amount_label.hide()
        self.amount_spinBox.hide()
        self.invalid_product_name_label.hide()
        self.invalid_type_label.hide()
        self.invalid_upc_label.hide()
        self.submit_update_product_pushButton.hide()
        self.cancel_update_product_pushButton.hide()
        query = QSqlQuery('exec ShowProductsBase')
        self.catalog_table_widget.setRowCount(0)
        self.catalog_table_widget.setColumnCount(8)
        while query.next():   
            rows = self.catalog_table_widget.rowCount()
            self.catalog_table_widget.setRowCount(rows + 1)
            for i in range(self.catalog_table_widget.columnCount() - 1):
                value = str(query.value(i))
                self.catalog_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
            update_button = QtWidgets.QPushButton('update\ninfo')
            update_button.clicked.connect(self.__update_product)
            self.catalog_table_widget.setCellWidget(rows,self.catalog_table_widget.columnCount() -1, update_button)
        self.catalog_table_widget.resizeRowsToContents()

        self.catalog_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.all_lack_table_widget.setRowCount(0)
        if self.all_customer_filter_comboBox.count() == 0:
            customer_names_query = QSqlQuery()
            customer_names_query.exec('select customer_name from customers')
            customer_names = ['all']
            while customer_names_query.next():
                customer_names.append(customer_names_query.value(0))
            self.all_customer_filter_comboBox.addItems(customer_names)
        if self.all_customer_filter_comboBox.currentText() == 'all':
            query = QSqlQuery(f'exec ShowLackProducts')
        else:
            query = QSqlQuery(f'exec ShowLackProductsByCustomer_name "{self.all_customer_filter_comboBox.currentText()}"')

        while query.next():
            rows = self.all_lack_table_widget.rowCount()
            self.all_lack_table_widget.setRowCount(rows + 1)
            for i in range(self.all_lack_table_widget.columnCount()):
                value = str(query.value(i))
                self.all_lack_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))

    def __update_product(self):
        self.new_product_pushButton.setEnabled(False)
        self.submit_update_product_pushButton.show()
        self.cancel_update_product_pushButton.show()
        self.product_name_label.show()
        self.product_name_line_edit.show()
        row = self.catalog_table_widget.currentRow()
        self.product_name_line_edit.setText(self.catalog_table_widget.item(row, 0).text())
        self.type_label.show()
        self.type_line_edit.show()
        self.type_line_edit.setText(self.catalog_table_widget.item(row, 1).text())
        self.upc_label.show()
        self.upc_line_edit.show()
        self.upc_line_edit.setText(self.catalog_table_widget.item(row, 2).text())
        self.prime_price_label.show()
        self.prime_price_doubleSpinBox.show()
        self.prime_price_doubleSpinBox.setValue(float(self.catalog_table_widget.item(row, 3).text()))
        self.retail_price_label.show()
        self.retail_price__value_label.show()
        self.discount_label.show()
        self.discount_doubleSpinBox.show()
        prime_price = round(float(self.catalog_table_widget.item(row, 3).text()), 2)
        discount_price = round(float(self.catalog_table_widget.item(row, 5).text()), 2)
        discount = round(1 - (discount_price / (prime_price * 1.38)), 2)
        self.discount_doubleSpinBox.setValue(discount)
        self.discount_price_label.show()
        self.discount_price_value_label.show()
        self.amount_label.show()
        self.amount_spinBox.show()
        self.amount_spinBox.setValue(int(self.catalog_table_widget.item(row, 6).text()))

    def __initOrdersTab(self):
        if self.status_filter_comboBox.count() == 0:
            self.status_filter_comboBox.addItems(['all', 'pending', 'processing', 'cancelled', 'completed'])

        if self.customer_filter_comboBox.count() == 0:
            customer_names_query = QSqlQuery()
            customer_names_query.exec('select customer_name from customers')
            customer_names = ['all']
            while customer_names_query.next():
                customer_names.append(customer_names_query.value(0))
            self.customer_filter_comboBox.addItems(customer_names)

        if self.date_filter_comboBox.count() == 0:
            self.date_filter_comboBox.addItems(['all', 'Last week', 'Last month', 'Last year'])
        self.order_number_label.hide()
        self.details_table_widget.hide()
        self.hide_details_button.hide()
        self.lack_label.hide()
        self.lack_table_widget.hide()
        self.orders_table_widget.setRowCount(0)
        
        status_filter = self.status_filter_comboBox.currentText()
        customer_filter = self.customer_filter_comboBox.currentText()
        date_filter = self.date_filter_comboBox.currentText()
        if date_filter == 'Last week':
            period = 7
        if date_filter == 'Last month':
            period = 30
        if date_filter == 'Last year':
            period = 365

        if status_filter == 'all' and customer_filter == 'all' and date_filter == 'all':
            query = QSqlQuery(f'exec ShowAllOrders')
        elif status_filter == 'all' and date_filter == 'all':
            query = QSqlQuery(f'exec ShowOrdersByCustomer_name_ForWorker "{customer_filter}"')
        elif customer_filter == 'all' and date_filter == 'all':
            query = QSqlQuery(f'exec ShowOrdersByOrder_status_ForWorker {status_filter}')
        elif status_filter == 'all' and customer_filter == 'all':
            query = QSqlQuery(f'exec ShowAllOrders_Period_ForWorker {period}')
        elif status_filter == 'all':
            query = QSqlQuery(f'exec ShowOrdersByCustomer_nameAnd_Period_ForWorker "{customer_filter}", {period}')
        elif customer_filter == 'all':
            query = QSqlQuery(f'exec ShowOrdersByOrder_statusAnd_Period_ForWorker "{status_filter}", {period}')
        elif date_filter == 'all':
            query = QSqlQuery(f'exec ShowOrdersByCustomer_nameAndOrder_status_ForWorker "{customer_filter}", {status_filter}')
        else:
            query = QSqlQuery(f'exec ShowOrdersByCustomer_nameAndOrder_statusAnd_Period_ForWorker "{customer_filter}", {status_filter}, {period}')

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
            
            order_status_comboBox = QtWidgets.QComboBox()
            order_status_comboBox.addItems(['Set status', 'cancelled', 'pending', 'processing', 'completed'])
            order_status_comboBox.currentTextChanged.connect(self.__change_order_status)
            self.orders_table_widget.setCellWidget(rows,self.orders_table_widget.columnCount() -1, order_status_comboBox)
        self.orders_table_widget.resizeRowsToContents()
        
        self.orders_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def __change_order_status(self):
        state = self.orders_table_widget.cellWidget(self.orders_table_widget.currentRow(), 7).currentText()
        order_id = self.orders_table_widget.item(self.orders_table_widget.currentRow(), 0).text()
        if state == 'Set status':
            return
        else:
            qm = QtWidgets.QMessageBox()
            qm.setText(f"Change status of order {order_id} to {state}?")
            qm.setWindowTitle("Confirmation")
            qm.setStandardButtons(qm.StandardButton.Yes | qm.StandardButton.No)
            qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_question.jpg"))
            ret = qm.exec()

            if ret == qm.StandardButton.Yes:
                query = QSqlQuery(f'exec UpdateOrderStatus {order_id}, {state}')
                qm = QtWidgets.QMessageBox()
                qm.setText(f"Status of order {order_id} updated to {state}")
                qm.setWindowTitle("Successful")
                qm.setStandardButtons(qm.StandardButton.Ok)
                qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_ok.jpg"))
                ret = qm.exec()

                if ret == qm.StandardButton.Ok:
                    self.initTab()
            self.initTab()
                
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

        self.lack_label.show()
        self.lack_table_widget.show()
        self.lack_table_widget.setRowCount(0)
        self.lack_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        qry = QSqlQuery(f'exec ShowLackProductsByOrder_id {order_number}')
        while qry.next():
            rows = self.lack_table_widget.rowCount()
            self.lack_table_widget.setRowCount(rows + 1)
            for i in range(self.lack_table_widget.columnCount()):
                value = str(qry.value(i))
                self.lack_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
