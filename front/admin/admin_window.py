from PyQt6.QtSql import QSqlQuery
from PyQt6 import QtWidgets, QtGui
from ui.ui_admin_window import Ui_AdminWindow
import re

regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, app_widget, db, worker_id: int, worker_username: str, *args, **kwargs):
        super(AdminWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app_widget = app_widget
        self.username = worker_username
        self.signed_label.setText(f"You are signed in as admin: {worker_username}")
        self.db = db
        self.worker_id = worker_id
        self.__init_window()
        self.role_filter_comboBox.currentTextChanged.connect(self.__init_window)
        self.sign_out_button.clicked.connect(self.__sign_out)
        self.new_worker_button.clicked.connect(self.__new_worker)
        self.cancel_new_worker_button.clicked.connect(self.__init_window)
        self.submit_new_worker_button.clicked.connect(self.__submit_new_worker)

    def __sign_out(self):
        qm = QtWidgets.QMessageBox()
        ret = qm.question(self,'Confirmation', "Sign out?", qm.StandardButton.Yes | qm.StandardButton.No)

        if ret == qm.StandardButton.Yes:
            self.app_widget.setFixedWidth(500)
            self.app_widget.setFixedHeight(500)
            self.app_widget.setCurrentIndex(0)

    def __init_window(self):
        self.new_worker_button.setEnabled(True)
        self.submit_new_worker_button.hide()
        self.cancel_new_worker_button.hide()
        self.email_label.hide()
        self.email_lineEdit.hide()
        self.email_lineEdit.setText('')
        self.first_name_label.hide()
        self.first_name_line.hide()
        self.first_name_line.setText('')
        self.second_name_label.hide()
        self.second_name_line.hide()
        self.second_name_line.setText('')
        self.password_label.hide()
        self.password_line.hide()
        self.password_line.setText('')
        self.invalid_email_label.hide()
        self.invalid_first_name_label.hide()
        self.invalid_password_label.hide()
        self.invalid_second_name_label.hide()

        if self.role_filter_comboBox.currentText() == 'all':
            query = QSqlQuery('exec ShowWorkers')
        elif self.role_filter_comboBox.currentText() == 'worker':
            query = QSqlQuery("exec ShowWorkersByRole 'worker'")
        elif self.role_filter_comboBox.currentText() == 'admin':
            query = QSqlQuery("exec ShowWorkersByRole 'admin'")

        self.workers_table_widget.setRowCount(0)
        self.workers_table_widget.setColumnCount(6)
        while query.next():   
            rows = self.workers_table_widget.rowCount()
            self.workers_table_widget.setRowCount(rows + 1)
            for i in range(self.workers_table_widget.columnCount() - 1):
                value = str(query.value(i))
                self.workers_table_widget.setItem(rows, i, QtWidgets.QTableWidgetItem(value))

            if query.value(4) != 'admin':
                delete_button = QtWidgets.QPushButton('delete')
                delete_button.clicked.connect(self.__delete_worker)
                self.workers_table_widget.setCellWidget(rows,self.workers_table_widget.columnCount() -1, delete_button)
        self.workers_table_widget.resizeRowsToContents()

        self.workers_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def __new_worker(self):
        self.new_worker_button.setEnabled(False)
        self.submit_new_worker_button.show()
        self.cancel_new_worker_button.show()
        self.email_label.show()
        self.email_lineEdit.show()
        self.first_name_label.show()
        self.first_name_line.show()
        self.second_name_label.show()
        self.second_name_line.show()
        self.password_label.show()
        self.password_line.show()

    def __submit_new_worker(self):
        email = self.email_lineEdit.text()
        first_name = self.first_name_line.text()
        second_name = self.second_name_line.text()
        password = self.password_line.text()
        username = self.email_lineEdit.text().split('@')[0]

        query = QSqlQuery()
        query.exec(f"exec InsertWorker '{email}', '{first_name}', '{second_name}', {password}")

        if query.lastError().text() == '':
            qm = QtWidgets.QMessageBox()
            qm.setText(f"Registration of new worker successful, his username is: {username}")
            qm.setWindowTitle("Successful")
            qm.setStandardButtons(qm.StandardButton.Ok)
            qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_ok.jpg"))
            ret = qm.exec()
            if ret == qm.StandardButton.Ok:
                self.__init_window()
        else:
            print(query.lastError().databaseText())
            if query.lastError().text().__contains__('LEFT') or re.fullmatch(regex, email) is None:
                self.invalid_email_label.setText('\u274c Incorrect email')
                self.invalid_email_label.show() 
            elif query.lastError().databaseText().__contains__('UQ_WORKER_EMAIL'):
                self.invalid_email_label.setText('\u274c This email is already used!')
                self.invalid_email_label.show()
            else:
                self.invalid_email_label.setText('\u2713')
                self.invalid_email_label.show()
            if first_name == '':
                self.invalid_first_name_label.setText('\u274c Empty field')
                self.invalid_first_name_label.show()
            else:
                self.invalid_first_name_label.setText('\u2713')
                self.invalid_first_name_label.show()
            if second_name == '':
                self.invalid_second_name_label.setText('\u274c Empty field')
                self.invalid_second_name_label.show()
            else:
                self.invalid_second_name_label.setText('\u2713')
                self.invalid_second_name_label.show()    
            if password == '':
                self.invalid_password_label.setText('\u274c Empty field')
                self.invalid_password_label.show()
            else:
                self.invalid_password_label.setText('\u2713')
                self.invalid_password_label.show()

    def __delete_worker(self):
        username = self.workers_table_widget.item(self.workers_table_widget.currentRow(), 0).text()
        qm = QtWidgets.QMessageBox()
        qm = QtWidgets.QMessageBox()
        qm.setText(f"Delete worker {username}?")
        qm.setWindowTitle("Confirmation")
        qm.setStandardButtons(qm.StandardButton.Yes | qm.StandardButton.No)
        qm.setIconPixmap(QtGui.QPixmap("D:\учеба\бд\курсач\\brewery\\front\cadian_question.jpg"))
        ret = qm.exec()

        if ret == qm.StandardButton.Yes:
            query = QSqlQuery()
            email = self.workers_table_widget.item(self.workers_table_widget.currentRow(), 1).text()

            query.exec(f"select users.user_id from users join workers on workers.user_id=users.user_id where email='{email}'")
            query.first()
            user_id = query.value(0)
            query.exec(f'exec DeleteWorker {user_id}')
        self.__init_window()