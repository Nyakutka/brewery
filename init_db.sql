--DATABASE
IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'brewery')
    BEGIN
        CREATE DATABASE brewery
    END
GO

USE brewery
GO

--TABLES
CREATE FUNCTION dbo.isValidEmail(@EMAIL varchar(30))
RETURNS bit as
BEGIN     
    DECLARE @bitRetVal as Bit
    IF (@EMAIL = '' OR @EMAIL NOT LIKE '_%@__%.__%')
        SET @bitRetVal = 0  -- Invalid
    ELSE 
        SET @bitRetVal = 1   -- Valid
    RETURN @bitRetVal
END
GO

CREATE FUNCTION dbo.isValidPhoneNumber(@PHONE_NUMBER varchar(30))
RETURNS bit as
BEGIN     
    DECLARE @bitRetVal as Bit
    IF (LEN(@PHONE_NUMBER) != 11 or iSNUMERIC(@PHONE_NUMBER) = 0)
        SET @bitRetVal = 0  -- Invalid
    ELSE 
        SET @bitRetVal = 1   -- Valid
    RETURN @bitRetVal
END
GO

IF OBJECT_ID(N'dbo.users', N'U') IS NULL 
    CREATE TABLE users (
        [user_id] [int] PRIMARY KEY IDENTITY(1,1) NOT NULL,
        [username] [varchar](30) NOT NULL UNIQUE CHECK(username !=''),
        [user_password] [varchar](30) NOT NULL CHECK(user_password !=''),
        [user_role] [varchar](10) NOT NULL
    );
GO

IF OBJECT_ID(N'dbo.workers', N'U') IS NULL 
    CREATE TABLE workers (
        [user_id] [int] NOT NULL FOREIGN KEY([user_id]) REFERENCES [dbo].[users] ([user_id]),
        [worker_id] [int] PRIMARY KEY IDENTITY(1,1) NOT NULL,
        [email] [varchar](30) NOT NULL UNIQUE 
            CONSTRAINT CK_WORKER_EMAIL CHECK(dbo.isValidEmail(email) = 1),
        [first_name] [varchar](30) NOT NULL CHECK(first_name !=''),
        [second_name] [varchar](30) NOT NULL CHECK(second_name !='')
    );
GO

IF OBJECT_ID(N'dbo.customers', N'U') IS NULL 
    CREATE TABLE customers (
        [user_id] [int] NOT NULL FOREIGN KEY([user_id]) REFERENCES [dbo].[users] ([user_id]),
        [customer_id] [int] PRIMARY KEY IDENTITY(1,1) NOT NULL,
        [customer_name] [varchar](30) NOT NULL CHECK(customer_name !=''),
        [email] [varchar](30) NOT NULL UNIQUE
            CONSTRAINT CK_CUSTOMER_EMAIL CHECK(dbo.isValidEmail(email) = 1),
        [phone_number] [varchar](30) NOT NULL UNIQUE
            CONSTRAINT CK_CUSTOMER_PHONE_NUMBER CHECK(dbo.isValidPhoneNumber(phone_number) = 1),
        [address] [varchar](30) NOT NULL CHECK(address !='')
    );
GO

IF OBJECT_ID(N'dbo.orders', N'U') IS NULL 
    CREATE TABLE orders (
        [order_id] [int] PRIMARY KEY IDENTITY(1,1) NOT NULL,
        [customer_id] [int] NOT NULL FOREIGN KEY([customer_id]) REFERENCES [dbo].[customers] ([customer_id]),
        [order_date] [datetime] NOT NULL,
        [order_status] [varchar](30) NOT NULL,
        [total_cost] [decimal](8, 2) NULL
    );
GO

IF OBJECT_ID(N'dbo.products', N'U') IS NULL 
    CREATE TABLE products (
        [product_id] [int] PRIMARY KEY IDENTITY(1,1) NOT NULL,
        [product_name] [varchar](30) NOT NULL UNIQUE CHECK(product_name !=''),
        [product_type] [varchar](30) NOT NULL,
        [cost_price] [decimal](8, 2) NOT NULL,
        [retail_price] as cost_price * 1.38,
        [discount_price] [decimal](8, 2)
    );
GO

CREATE TRIGGER Products_Discount_Price_On_Insert_Products
    ON products
    AFTER INSERT AS
        UPDATE products
            set discount_price = retail_price
                where product_id = (select product_id from inserted)
GO

IF OBJECT_ID(N'dbo.discounts', N'U') IS NULL 
    CREATE TABLE discounts (
        [product_id] [int] NOT NULL FOREIGN KEY([product_id]) REFERENCES [dbo].[products] ([product_id]),
        [discount] [decimal](3, 2) NOT NULL
    );
GO

CREATE TRIGGER Products_Discount_Price_On_Insert_Or_Update_Discount
    ON discounts
    AFTER INSERT, UPDATE AS
        UPDATE products
            set discount_price = retail_price * (1 - (select discount from inserted))
                where product_id = (select product_id from inserted)
GO

CREATE TRIGGER Products_Discount_Price_On_Delete_Discount
    ON discounts
    AFTER DELETE AS
        UPDATE products
            set discount_price = retail_price
                where product_id = (select product_id from deleted)
GO

IF OBJECT_ID(N'dbo.order_details', N'U') IS NULL 
    CREATE TABLE order_details (
        [order_id] [int] NOT NULL FOREIGN KEY([order_id]) REFERENCES [dbo].[orders] ([order_id]),
        [product_id] [int] NOT NULL FOREIGN KEY([product_id]) REFERENCES [dbo].[products] ([product_id]),
        [amount] [int] NOT NULL
    );
GO

CREATE TRIGGER Orders_Total_cost_On_Insert_Order_Details
    ON order_details
    AFTER INSERT AS
        UPDATE orders
        set total_cost = (select sum(discount_price * order_details.amount) 
						      from inserted,
								  orders join order_details on orders.order_id = order_details.order_id
								  join products on order_details.product_id=products.product_id
						      where inserted.order_id = order_details.order_id)
                where order_id = (select order_id from inserted)
GO

IF OBJECT_ID(N'dbo.stock', N'U') IS NULL 
    CREATE TABLE stock (
        [product_id] [int] NOT NULL FOREIGN KEY([product_id]) REFERENCES [dbo].[products] ([product_id]),
        [amount] [int] NOT NULL
    );
GO


--VIEWS
create view ProductsStockView as
	select product_name,
		   product_type,
		   cost_price,
		   retail_price,
		   discount_price, 
		   amount 
		   from products
				join stock on products.product_id=stock.product_id
GO

create view OrdersOrderDetailsCustomersView as
select orders.order_id,
	   customer_name,
	   order_date,
	   orders.order_status,
       products.product_id,
	   product_name,
	   discount_price,
	   amount,
	   total_cost
		from orders 
			join order_details on orders.order_id=order_details.order_id 
			join products on order_details.product_id=products.product_id
			join customers on orders.customer_id=customers.customer_id
go
