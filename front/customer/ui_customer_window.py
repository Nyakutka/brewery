# Form implementation generated from reading ui file 'd:\учеба\brewery\front\customer\customer_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CustomerForm(object):
    def setupUi(self, CustomerForm):
        CustomerForm.setObjectName("CustomerForm")
        CustomerForm.resize(1200, 800)
        self.customer_tab_widget = QtWidgets.QTabWidget(CustomerForm)
        self.customer_tab_widget.setGeometry(QtCore.QRect(-1, 29, 1201, 771))
        self.customer_tab_widget.setObjectName("customer_tab_widget")
        self.catalog_tab = QtWidgets.QWidget()
        self.catalog_tab.setObjectName("catalog_tab")
        self.catalog_table_widget = QtWidgets.QTableWidget(self.catalog_tab)
        self.catalog_table_widget.setGeometry(QtCore.QRect(20, 20, 800, 600))
        self.catalog_table_widget.setObjectName("catalog_table_view")
        # self.catalog_table_view = QtWidgets.QTableView(self.catalog_tab)
        # self.catalog_table_view.setGeometry(QtCore.QRect(20, 20, 800, 600))
        # self.catalog_table_view.setObjectName("catalog_table_view")
        self.customer_tab_widget.addTab(self.catalog_tab, "")
        self.orders_tab = QtWidgets.QWidget()
        self.orders_tab.setObjectName("orders_tab")
        self.order_table_view = QtWidgets.QTableView(self.orders_tab)
        self.order_table_view.setGeometry(QtCore.QRect(20, 20, 800, 600))
        self.order_table_view.setObjectName("order_table_view")
        self.status_filter_comboBox = QtWidgets.QComboBox(self.orders_tab)
        self.status_filter_comboBox.setGeometry(QtCore.QRect(850, 40, 231, 31))
        self.status_filter_comboBox.setObjectName("status_filter_comboBox")
        self.status_filter_label = QtWidgets.QLabel(self.orders_tab)
        self.status_filter_label.setGeometry(QtCore.QRect(850, 20, 81, 21))
        self.status_filter_label.setScaledContents(False)
        self.status_filter_label.setObjectName("status_filter_label")
        self.customer_tab_widget.addTab(self.orders_tab, "")

        self.retranslateUi(CustomerForm)
        self.customer_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CustomerForm)

    def retranslateUi(self, CustomerForm):
        _translate = QtCore.QCoreApplication.translate
        CustomerForm.setWindowTitle(_translate("CustomerForm", "Form"))
        self.customer_tab_widget.setTabText(self.customer_tab_widget.indexOf(self.catalog_tab), _translate("CustomerForm", "Catalog"))
        self.status_filter_label.setText(_translate("CustomerForm", "Filter by status:"))
        self.customer_tab_widget.setTabText(self.customer_tab_widget.indexOf(self.orders_tab), _translate("CustomerForm", "My orders"))
