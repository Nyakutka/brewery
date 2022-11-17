use brewery

INSERT INTO users(username, user_password, user_role)
values
    ('admin', 'admin', 'admin'),--1
    ('red_white', 'cust1', 'customer'),--2
    ('rosal', 'cust2', 'customer'),--3
    ('v.pupkin', 'work1', 'worker'),--4
    ('n.peckin', 'work2', 'worker')--5

INSERT INTO customers(user_id, customer_name, email, phone_number, address)
VALUES
    (2, 'Красное&Белое', 'red_white@mail.ru', '88005553535', 'ул. Пушкина, д.10'),--1
    (3, 'РосАл', 'rosal@mail.ru', '88005553536', 'ул. Пушкина, д.11')--2

INSERT INTO workers(user_id, email, first_name, second_name)
VALUES
    (4, 'v.pupkin@brewery.com', 'Василий', 'Пупкин'),--1
    (5, 'n.pechkin@brewery.com', 'Николай', 'Печкин')--2

INSERT INTO products(product_name, product_type, upc_code, prime_price) VALUES ('Балтика 7', 'Пиво', '123456789121', 67)--1
GO

INSERT INTO products(product_name, product_type, upc_code, prime_price) VALUES ('Балтика 8', 'Пиво', '123456789122', 68)--2
GO

INSERT INTO products(product_name, product_type, upc_code, prime_price) VALUES ('Балтика 9', 'Пиво', '123456789123', 69)--3
GO

INSERT INTO products(product_name, product_type, upc_code, prime_price) VALUES ('Strongbow яблоко', 'Сидр', '123456789124', 57)--4
GO

INSERT INTO products(product_name, product_type, upc_code, prime_price) VALUES ('Strongbow груша', 'Сидр', '123456789125', 58)--5
GO

UPDATE stock
    set amount = 1
    where product_id=1
go

UPDATE stock
    set amount = 2
    where product_id=2
go

UPDATE stock
    set amount = 3
    where product_id=3
go

UPDATE stock
    set amount = 4
    where product_id=4
go

UPDATE stock
    set amount = 5
    where product_id=5
go

INSERT INTO discounts(product_id, discount) VALUES (1, 0.1)
GO

INSERT INTO discounts(product_id, discount) VALUES (3, 0.2)
GO

INSERT INTO discounts(product_id, discount) VALUES (5, 0.3)
GO

INSERT INTO orders(customer_id, order_date, order_status)
VALUES
    (1, '2022-05-23T14:25:10', 'pending'),--1
    (1, '2004-05-23T14:25:10', 'processing'),--2
    (2, '2004-05-23T14:25:10', 'pending'),--3
    (2, '2004-05-23T14:25:10', 'completed'),--4
    (2, '2004-05-23T14:25:10', 'cancelled')--5

INSERT INTO order_details(order_id, product_id, amount) VALUES (1, 1, 1)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (1, 2, 2)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (1, 3, 4)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (2, 2, 2)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (2, 3, 3)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (2, 4, 4)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (3, 1, 5)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (3, 3, 6)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (3, 5, 7)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (4, 2, 2)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (4, 3, 4)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (4, 4, 8)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (5, 1, 6)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (5, 3, 24)
GO

INSERT INTO order_details(order_id, product_id, amount) VALUES (5, 4, 10)
GO
