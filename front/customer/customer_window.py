from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from ui_customer_window import Ui_CustomerForm
import sys
sys.path.append('D:/учеба/brewery/db_connection')
from db_connection import DataBaseConnection

class CustomerWindow(QtWidgets.QMainWindow, Ui_CustomerForm):
    def __init__(self, *args, **kwargs):
        super(CustomerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.status_filter_comboBox.addItems(['all', 'pending', 'processing', 'cancelled'])
        self.db = DataBaseConnection().database
        self.initTab()
        self.customer_tab_widget.currentChanged.connect(self.initTab)
        self.status_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.hide_details_button.clicked.connect(self.__initOrdersTab)
        self.new_order_button.clicked.connect(self.__initCatalogTab_new_order_mode)
        self.cancel_new_order_button.clicked.connect(self.__initCatalogTab)

    def handle_show_details_button_clicked(self):
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
        self.new_order_table_widget.show()
        self.submit_new_order_button.show()
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
        print(self.new_order_table_widget.rowCount())
        if self.new_order_table_widget.rowCount() == 0:
            self.total_cost_label_value.setText(str(0))
        else:
            self.total_cost_label_value.setText(str(round(sum([float(x.text()) for x in [self.new_order_table_widget.item(i, 3) for i in range(self.new_order_table_widget.rowCount())]]), 2)))

    def handle_add_to_cart_button(self):
        if self.catalog_table_widget.cellWidget(self.catalog_table_widget.currentRow(), self.catalog_table_widget.currentColumn()).text() == '+':
            self.catalog_table_widget.cellWidget(self.catalog_table_widget.currentRow(), self.catalog_table_widget.currentColumn()).setText('-')
            rows = self.new_order_table_widget.rowCount()
            self.new_order_table_widget.setRowCount(rows + 1)
            product_name = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 0).text()
            price = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 3).text()

            self.new_order_table_widget.setItem(rows, 0, QtWidgets.QTableWidgetItem(product_name))
            self.new_order_table_widget.setItem(rows, 2, QtWidgets.QTableWidgetItem(price))
            self.new_order_table_widget.setItem(rows, 3, QtWidgets.QTableWidgetItem(str(0)))
            amount_spin_box = QtWidgets.QSpinBox()
            amount_spin_box.setMaximum(500)
            amount_spin_box.valueChanged.connect(lambda x: self.new_order_table_widget.setItem(self.new_order_table_widget.currentRow(), 3, QtWidgets.QTableWidgetItem(str(round(float(price)*float(amount_spin_box.value()), 2)))))
            amount_spin_box.valueChanged.connect(self.update_total_cost_value)
            self.new_order_table_widget.setCellWidget(rows, 1, amount_spin_box)
        else:
            product_name = self.catalog_table_widget.item(self.catalog_table_widget.currentRow(), 0).text()
            self.catalog_table_widget.cellWidget(self.catalog_table_widget.currentRow(), self.catalog_table_widget.currentColumn()).setText('+')
            self.new_order_table_widget.removeRow(self.new_order_table_widget.row(self.new_order_table_widget.findItems(product_name, QtCore.Qt.MatchFlag.MatchExactly)[0]))
        
    #add customer_id
    #add button add_order
    def __initOrdersTab(self):
        self.order_number_label.hide()
        self.details_table_widget.hide()
        self.hide_details_button.hide()
        self.orders_table_widget.setRowCount(0)
        if (self.status_filter_comboBox.currentText() == 'all'):
            query = QSqlQuery(f'exec ShowOrdersByCustomer_id {1}')
        else:
            query = QSqlQuery(f'exec ShowOrdersByCustomer_idAndOrder_status {1}, {self.status_filter_comboBox.currentText()}')

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
                cancel_order = QtWidgets.QPushButton('cancel\norder')
                cancel_order.clicked.connect(self.__initCatalogTab)
                self.orders_table_widget.setCellWidget(rows,self.orders_table_widget.columnCount() -1, cancel_order)
            self.orders_table_widget.resizeRowsToContents()
        
        self.orders_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def initTab(self):
        if (self.customer_tab_widget.currentIndex() == 0):
            self.__initCatalogTab()
        elif (self.customer_tab_widget.currentIndex() == 1):
            self.__initOrdersTab()

app = QtWidgets.QApplication(sys.argv)
window = CustomerWindow()
window.show()
app.exec()
