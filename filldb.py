from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy.engine import URL

connection_string = "DRIVER={SQL Server};SERVER=localhost;DATABASE=brewery;Truster_Connections=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

with engine.begin() as conn:
	conn.execute("exec InsertCustomer ?, ?, ?, ?, ?", 'Красное&Белое', 'red_white@mail.ru', '88005553535', 'ул. Пушкина, д.10', 'ilovebeer')
	conn.execute("exec InsertCustomer ?, ?, ?, ?, ?", 'РосАл', 'rosal@mail.ru', '88005553536', 'ул. Пушкина, д.11', 'ilovevodka')

	conn.execute("exec InsertWorker ?, ?, ?, ?", 'v.pupkin@brewery.com', 'Василий', 'Пупкин', 'vpupkinpass')
	conn.execute("exec InsertWorker ?, ?, ?, ?", 'n.pechkin@brewery.com', 'Николай', 'Печкин', 'npechkinpass')

	conn.execute("exec InsertProduct ?, ?, ?, ?", 'Балтика 7', 'Пиво', '123456789121', 67)
	conn.execute("exec InsertProduct ?, ?, ?, ?", 'Балтика 8', 'Пиво', '123456789122', 68)
	conn.execute("exec InsertProduct ?, ?, ?, ?", 'Балтика 9', 'Пиво', '123456789123', 69)
	conn.execute("exec InsertProduct ?, ?, ?, ?", 'Strongbow яблоко', 'Сидр', '123456789124', 57)
	conn.execute("exec InsertProduct ?, ?, ?, ?", 'Strongbow груша', 'Сидр', '123456789125', 58)

	conn.execute("exec UpdateAmountOnStock ?, ?", 1, 1)
	conn.execute("exec UpdateAmountOnStock ?, ?", 2, 2)
	conn.execute("exec UpdateAmountOnStock ?, ?", 3, 3)
	conn.execute("exec UpdateAmountOnStock ?, ?", 4, 4)
	conn.execute("exec UpdateAmountOnStock ?, ?", 5, 5)

	conn.execute("exec UpdateDiscount ?, ?", 1, 0.10)
	conn.execute("exec UpdateDiscount ?, ?", 3, 0.20)
	conn.execute("exec UpdateDiscount ?, ?", 5, 0.30)

	conn.execute("exec InsertOrder ?, ?", 1, '2022-05-23T14:25:10')
	conn.execute("exec InsertOrder_details ?, ?, ?", 1, 1, 1)
	conn.execute("exec InsertOrder_details ?, ?, ?", 1, 2, 2)
	conn.execute("exec InsertOrder_details ?, ?, ?", 1, 3, 4)

	conn.execute("exec InsertOrder ?, ?", 1, '2022-05-24T14:25:10')
	conn.execute("exec UpdateOrderStatus ?, ?", 2, 'processing')
	conn.execute("exec InsertOrder_details ?, ?, ?", 2, 2, 2)
	conn.execute("exec InsertOrder_details ?, ?, ?", 2, 3, 3)
	conn.execute("exec InsertOrder_details ?, ?, ?", 2, 4, 4)

	conn.execute("exec InsertOrder ?, ?", 2, '2022-05-25T14:25:10')
	conn.execute("exec InsertOrder_details ?, ?, ?", 3, 1, 5)
	conn.execute("exec InsertOrder_details ?, ?, ?", 3, 3, 6)
	conn.execute("exec InsertOrder_details ?, ?, ?", 3, 5, 7)

	conn.execute("exec InsertOrder ?, ?", 2, '2022-05-26T14:25:10')
	conn.execute("exec UpdateOrderStatus ?, ?", 4, 'completed')
	conn.execute("exec InsertOrder_details ?, ?, ?", 4, 2, 2)
	conn.execute("exec InsertOrder_details ?, ?, ?", 4, 3, 4)
	conn.execute("exec InsertOrder_details ?, ?, ?", 4, 4, 8)

	conn.execute("exec InsertOrder ?, ?", 2, '2022-05-27T14:25:10')
	conn.execute("exec UpdateOrderStatus ?, ?", 5, 'cancelled')
	conn.execute("exec InsertOrder_details ?, ?, ?", 5, 1, 6)
	conn.execute("exec InsertOrder_details ?, ?, ?", 5, 3, 24)
	conn.execute("exec InsertOrder_details ?, ?, ?", 5, 4, 10)
