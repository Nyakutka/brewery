from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery

SERVER = 'localhost'
# SERVER = 'NYAKUTKA'

class DataBaseConnection():
    def __init__(self, 
                driver = 'SQL Server',
                server = SERVER,
                database = 'brewery') -> None:
        self.connection_string = f'DRIVER={driver};'\
                                f'SERVER={server};'\
                                f'DATABASE={database}'
        self.database = QSqlDatabase.addDatabase('QODBC')
        self.database.setDatabaseName(self.connection_string)
        if self.database.open():
            print('Connected to SQL Server successfully')
        else:
            print('Connection to SQL Server failed')
