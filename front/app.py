from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6.QtWidgets import QTableView, QApplication
import sys

SERVER_NAME = 'localhost'
DATABASE_NAME = 'brewery'
USERNAME = ''
PASSWORD = ''

def createConnection():
	connString = f'DRIVER={{SQL Server}};'\
					f'SERVER={SERVER_NAME};'\
					f'DATABASE={DATABASE_NAME}'
	global db
	db = QSqlDatabase.addDatabase('QODBC')
	db.setDatabaseName(connString)
	if db.open():
		print('connected to SQL Server successfully')
		return True
	else:
		print('connected to SQL Server failed')
		return False

def displayData(sqlStatement):
	print('processing querry')
	qry = QSqlQuery(db)
	qry.prepare(sqlStatement)
	qry.exec()

	model = QSqlQueryModel()
	model.setQuery(qry)
	view = QTableView()
	view.setModel(model)
	return view

if __name__=='__main__':
	app = QApplication(sys.argv)

	if createConnection():
		SQL_STATEMENT = 'exec ShowProductsBase'
		dataView = displayData(SQL_STATEMENT)
		dataView.show()
	

	app.exit(app.exec())