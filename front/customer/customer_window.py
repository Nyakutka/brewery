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
    
    def _initCatalogTab(self):
        model = QSqlQueryModel()
        model.setQuery('exec ShowProductsCatalog', self.db)
        view = QtWidgets.QTableView()
        view.setModel(model)
        self.catalog_table_widget(view)
    
    #add customer_id
    #add button add_order
    #add button cancel_order
    def _initOrdersTab(self):
        model = QSqlQueryModel()
        if (self.status_filter_comboBox.currentText() == 'all'):
             model.setQuery(f'exec ShowOrdersByCustomer_id {1}', self.db)
        else:
            model.setQuery(f'exec ShowOrdersByCustomer_idAndOrder_status {1}, {self.status_filter_comboBox.currentText()}', self.db)
        print(model.rowCount())
        

        for i in range(model.rowCount()):
            model.setData(model.index(i, 0), "PushButton")
            self.order_table_view.setIndexWidget(model.index(i, 1), QtWidgets.QPushButton("PushButton"))

        self.order_table_view.setModel(model)
        # print(self.order_table_view.setIndexWidget(QtWidgets.QPushButton()))
        # for index in self.order_table_view.

    def initTab(self):
        if (self.customer_tab_widget.currentIndex() == 0):
            self._initCatalogTab()
        elif (self.customer_tab_widget.currentIndex() == 1):
            self._initOrdersTab()

app = QtWidgets.QApplication(sys.argv)
window = CustomerWindow()
window.show()
app.exec()
