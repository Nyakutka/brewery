from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from ui_worker_window import Ui_WorkerWindow
from datetime import datetime
import sys
# sys.path.append('D:/учеба/brewery/db_connection')
# sys.path.append('D:/учеба/brewery/front/authorisation')
sys.path.append('D:/учеба/бд/курсач/brewery/db_connection')
sys.path.append('D:/учеба/бд/курсач/brewery/front/authorisation')
from db_connection import DataBaseConnection

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
        self.all_customer_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.total_income_filter_comboBox.currentTextChanged.connect(self.initTab)

    def initTab(self):
        if (self.worker_tab_widget.currentIndex() == 0):
            self.__initCatalogTab()
        elif (self.worker_tab_widget.currentIndex() == 1):
            self.__initOrdersTab()

    ##add edit
    def __initCatalogTab(self):
        query = QSqlQuery('exec ShowProductsBase')
        self.catalog_table_widget.setRowCount(0)
        self.catalog_table_widget.setColumnCount(7)
        while query.next():   
            rows = self.catalog_table_widget.rowCount()
            self.catalog_table_widget.setRowCount(rows + 1)
            for i in range(self.catalog_table_widget.columnCount()):
                value = str(query.value(i))
                self.catalog_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))
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
        
    def __initOrdersTab(self):
        if self.status_filter_comboBox.count() == 0:
            self.status_filter_comboBox.addItems(['all', 'pending', 'processing', 'cancelled'])

        if self.customer_filter_comboBox.count() == 0:
            customer_names_query = QSqlQuery()
            customer_names_query.exec('select customer_name from customers')
            customer_names = ['all']
            while customer_names_query.next():
                customer_names.append(customer_names_query.value(0))
            self.customer_filter_comboBox.addItems(customer_names)

        self.order_number_label.hide()
        self.details_table_widget.hide()
        self.hide_details_button.hide()
        self.lack_label.hide()
        self.lack_table_widget.hide()
        self.orders_table_widget.setRowCount(0)
        if (self.status_filter_comboBox.currentText() == 'all' and self.customer_filter_comboBox.currentText() == 'all'):
            query = QSqlQuery(f'exec ShowAllOrders')
        elif (self.status_filter_comboBox.currentText() == 'all'):
            query = QSqlQuery(f'exec ShowOrdersByCustomer_name_ForWorker "{self.customer_filter_comboBox.currentText()}"')
        elif (self.customer_filter_comboBox.currentText() == 'all'):
            query = QSqlQuery(f'exec ShowOrdersByOrder_status_ForWorker {self.status_filter_comboBox.currentText()}')
        else:
            query = QSqlQuery(f'exec ShowOrdersByCustomer_nameAndOrder_status_ForWorker "{self.customer_filter_comboBox.currentText()}", {self.status_filter_comboBox.currentText()}')

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
            if query.value(2) != 'cancelled':
                cancel_order_button = QtWidgets.QPushButton('change\nstatus')
                # cancel_order_button.clicked.connect(self.__cancel_order)
                self.orders_table_widget.setCellWidget(rows,self.orders_table_widget.columnCount() -1, cancel_order_button)
            self.orders_table_widget.resizeRowsToContents()
        
        self.orders_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

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