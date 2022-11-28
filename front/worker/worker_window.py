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
    def __init__(self, app_widget, worker_id: int, worker_username: str, *args, **kwargs):
        super(WorkerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app_widget = app_widget
        self.username = worker_username
        self.signed_label.setText(f"You are signed in as worker: {worker_username}")
        self.status_filter_comboBox.addItems(['all', 'pending', 'processing', 'cancelled'])
        self.db = DataBaseConnection().database
        self.worker_id = worker_id
        self.initTab()
        self.customer_tab_widget.currentChanged.connect(self.initTab)
        self.status_filter_comboBox.currentTextChanged.connect(self.initTab)
        self.hide_details_button.clicked.connect(self.__initOrdersTab)
        self.new_order_button.clicked.connect(self.__initCatalogTab_new_order_mode)
        self.submit_new_order_button.clicked.connect(self.__submit_order)
        self.cancel_new_order_button.clicked.connect(self.__cancel_new_order_mode)
        self.sign_out_button.clicked.connect(self.__sign_out)
        self.change_telephone_number_button.clicked.connect(self.__change_phone_number)
        self.change_address_button.clicked.connect(self.__change_address)
        