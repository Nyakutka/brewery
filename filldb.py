from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy.engine import URL

connection_string = "DRIVER={SQL Server};SERVER=localhost;DATABASE=brewery;Truster_Connections=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

with engine.begin() as conn:
	conn.execute("exec InsertCustomer ?, ?, ?, ?, ?", 'Красное&Белое', 'red_white@mail.ru', '88005553535', 'ул. Пушкина, д.10', 'ilovebeer')
	conn.execute("exec InsertCustomer ?, ?, ?, ?, ?", 'РосАл', 'rosal@mail.ru', '88005553536', 'ул. Пушкина, д.11', 'ilovevodka')
	conn.execute("exec InsertCustomer ?, ?, ?, ?, ?", 'Beerka', 'beerka@mail.ru', '88125553536', 'ул. Пушкина, д.12', 'ilovedrinking')

	conn.execute("INSERT INTO users(username, user_password, user_role) VALUES ('admin', HASHBYTES('SHA2_256', 'admin'), 'admin')")
	conn.execute("INSERT INTO workers(user_id, email, first_name, second_name) VALUES ((select user_id from users where username='admin'), 'admin@brewery.com', 'Nikita', 'Tsapov')")

	conn.execute("exec InsertWorker ?, ?, ?, ?", 'v.pupkin@brewery.com', 'Василий', 'Пупкин', 'vpupkinpass')
	conn.execute("exec InsertWorker ?, ?, ?, ?", 'n.pechkin@brewery.com', 'Николай', 'Печкин', 'npechkinpass')

	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nyak Fici', 'Beer', '123456789121', 67, 0.10, 1)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nyak Malt', 'Beer', '123456789122', 68, 0, 2)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nyak Dark', 'Beer', '123456789123', 69, 0.20, 3)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nyak Dark Brown', 'Beer', '123456789124', 57, 0, 4)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nononti', 'Beer', '123456789125', 58, 0.0, 5)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Narmara', 'Beer', '123456789126', 60, 0.0, 5)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nara Nuzu', 'Beer', '123456789127', 75, 0.20, 5)
	conn.execute("exec InsertProduct ?, ?, ?, ?, ?, ?", 'Nera', 'Beer', '123456789128', 80, 0.10, 5)

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

	conn.execute("exec InsertOrder ?, ?", 3, '2022-05-30T14:25:10')
	conn.execute("exec UpdateOrderStatus ?, ?", 6, 'completed')
	conn.execute("exec InsertOrder_details ?, ?, ?", 6, 1, 4)
	conn.execute("exec InsertOrder_details ?, ?, ?", 6, 5, 2)
	conn.execute("exec InsertOrder_details ?, ?, ?", 6, 4, 10)

	conn.execute("exec InsertOrder ?, ?", 3, '2022-07-27T14:25:10')
	conn.execute("exec UpdateOrderStatus ?, ?", 7, 'completed')
	conn.execute("exec InsertOrder_details ?, ?, ?", 7, 7, 6)
	conn.execute("exec InsertOrder_details ?, ?, ?", 7, 3, 30)
	conn.execute("exec InsertOrder_details ?, ?, ?", 7, 6, 15)
