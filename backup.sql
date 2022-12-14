USE [master]
GO
/****** Object:  Database [brewery]    Script Date: 06.12.2022 19:04:16 ******/
CREATE DATABASE [brewery]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'brewery', FILENAME = N'D:\Programs\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\brewery.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'brewery_log', FILENAME = N'D:\Programs\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\brewery_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [brewery] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [brewery].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [brewery] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [brewery] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [brewery] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [brewery] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [brewery] SET ARITHABORT OFF 
GO
ALTER DATABASE [brewery] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [brewery] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [brewery] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [brewery] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [brewery] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [brewery] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [brewery] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [brewery] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [brewery] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [brewery] SET  ENABLE_BROKER 
GO
ALTER DATABASE [brewery] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [brewery] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [brewery] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [brewery] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [brewery] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [brewery] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [brewery] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [brewery] SET RECOVERY FULL 
GO
ALTER DATABASE [brewery] SET  MULTI_USER 
GO
ALTER DATABASE [brewery] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [brewery] SET DB_CHAINING OFF 
GO
ALTER DATABASE [brewery] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [brewery] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [brewery] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [brewery] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'brewery', N'ON'
GO
ALTER DATABASE [brewery] SET QUERY_STORE = OFF
GO
USE [brewery]
GO
/****** Object:  UserDefinedFunction [dbo].[isValidEmail]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

--TABLES
CREATE FUNCTION [dbo].[isValidEmail](@EMAIL varchar(30))
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
/****** Object:  UserDefinedFunction [dbo].[isValidPhoneNumber]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE FUNCTION [dbo].[isValidPhoneNumber](@PHONE_NUMBER varchar(30))
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
/****** Object:  Table [dbo].[products]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[products](
	[product_id] [int] IDENTITY(1,1) NOT NULL,
	[product_name] [varchar](30) NOT NULL,
	[product_type] [varchar](30) NOT NULL,
	[upc_code] [varchar](12) NOT NULL,
	[prime_price] [decimal](8, 2) NOT NULL,
	[retail_price]  AS ([prime_price]*(1.38)),
	[discount_price] [decimal](8, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[product_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_PRODUCT_NAME] UNIQUE NONCLUSTERED 
(
	[product_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_PRODUCT_UPC] UNIQUE NONCLUSTERED 
(
	[upc_code] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[stock]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[stock](
	[product_id] [int] NOT NULL,
	[amount] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[ProductsStockView]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


--VIEWS
create view [dbo].[ProductsStockView] as
	select product_name,
		   product_type,
           upc_code,
		   prime_price,
		   retail_price,
		   discount_price, 
		   amount 
		   from products
				join stock on products.product_id=stock.product_id
GO
/****** Object:  Table [dbo].[customers]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[customers](
	[user_id] [int] NOT NULL,
	[customer_id] [int] IDENTITY(1,1) NOT NULL,
	[email] [varchar](30) NOT NULL,
	[customer_name] [varchar](30) NOT NULL,
	[phone_number] [varchar](30) NOT NULL,
	[address] [varchar](30) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[customer_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_CUSTOMER_EMAIL] UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_CUSTOMER_PHONE_NUMBER] UNIQUE NONCLUSTERED 
(
	[phone_number] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[orders]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[orders](
	[order_id] [int] IDENTITY(1,1) NOT NULL,
	[customer_id] [int] NOT NULL,
	[order_date] [datetime] NOT NULL,
	[order_status] [varchar](30) NULL,
	[total_prime_cost] [decimal](8, 2) NULL,
	[total_cost] [decimal](8, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[order_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[order_details]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[order_details](
	[order_id] [int] NOT NULL,
	[product_id] [int] NOT NULL,
	[amount] [int] NOT NULL,
	[price] [decimal](8, 2) NULL,
	[cost]  AS ([price]*[amount])
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[OrdersOrderDetailsCustomersView]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create view [dbo].[OrdersOrderDetailsCustomersView] as
    select orders.order_id,
	   customer_name,
	   order_date,
	   orders.order_status,
       products.product_id,
	   product_name,
       amount,
	   price,
	   cost
		from orders 
			join order_details on orders.order_id=order_details.order_id 
			join products on order_details.product_id=products.product_id
			join customers on orders.customer_id=customers.customer_id
GO
/****** Object:  Table [dbo].[discounts]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[discounts](
	[product_id] [int] NOT NULL,
	[discount] [decimal](3, 2) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[user_id] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](30) NOT NULL,
	[user_password] [varbinary](256) NOT NULL,
	[user_role] [varchar](10) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[workers]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[workers](
	[user_id] [int] NOT NULL,
	[worker_id] [int] IDENTITY(1,1) NOT NULL,
	[email] [varchar](30) NOT NULL,
	[first_name] [varchar](30) NOT NULL,
	[second_name] [varchar](30) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[worker_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_WORKER_EMAIL] UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[orders] ADD  DEFAULT ('pending') FOR [order_status]
GO
ALTER TABLE [dbo].[customers]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
GO
ALTER TABLE [dbo].[discounts]  WITH CHECK ADD FOREIGN KEY([product_id])
REFERENCES [dbo].[products] ([product_id])
GO
ALTER TABLE [dbo].[order_details]  WITH CHECK ADD FOREIGN KEY([order_id])
REFERENCES [dbo].[orders] ([order_id])
GO
ALTER TABLE [dbo].[order_details]  WITH CHECK ADD FOREIGN KEY([product_id])
REFERENCES [dbo].[products] ([product_id])
GO
ALTER TABLE [dbo].[orders]  WITH CHECK ADD FOREIGN KEY([customer_id])
REFERENCES [dbo].[customers] ([customer_id])
GO
ALTER TABLE [dbo].[stock]  WITH CHECK ADD FOREIGN KEY([product_id])
REFERENCES [dbo].[products] ([product_id])
GO
ALTER TABLE [dbo].[workers]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[customers]  WITH CHECK ADD CHECK  (([address]<>''))
GO
ALTER TABLE [dbo].[customers]  WITH CHECK ADD CHECK  (([customer_name]<>''))
GO
ALTER TABLE [dbo].[customers]  WITH CHECK ADD  CONSTRAINT [CK_CUSTOMER_EMAIL] CHECK  (([dbo].[isValidEmail]([email])=(1)))
GO
ALTER TABLE [dbo].[customers] CHECK CONSTRAINT [CK_CUSTOMER_EMAIL]
GO
ALTER TABLE [dbo].[customers]  WITH CHECK ADD  CONSTRAINT [CK_CUSTOMER_PHONE_NUMBER] CHECK  (([dbo].[isValidPhoneNumber]([phone_number])=(1)))
GO
ALTER TABLE [dbo].[customers] CHECK CONSTRAINT [CK_CUSTOMER_PHONE_NUMBER]
GO
ALTER TABLE [dbo].[products]  WITH CHECK ADD CHECK  (([product_name]<>''))
GO
ALTER TABLE [dbo].[products]  WITH CHECK ADD  CONSTRAINT [CK_PRODUCT_UPC] CHECK  ((len([upc_code])=(12)))
GO
ALTER TABLE [dbo].[products] CHECK CONSTRAINT [CK_PRODUCT_UPC]
GO
ALTER TABLE [dbo].[users]  WITH CHECK ADD CHECK  (([username]<>''))
GO
ALTER TABLE [dbo].[users]  WITH CHECK ADD  CONSTRAINT [CK_USER_PASSWORD] CHECK  (([user_password]<>''))
GO
ALTER TABLE [dbo].[users] CHECK CONSTRAINT [CK_USER_PASSWORD]
GO
ALTER TABLE [dbo].[workers]  WITH CHECK ADD CHECK  (([first_name]<>''))
GO
ALTER TABLE [dbo].[workers]  WITH CHECK ADD CHECK  (([second_name]<>''))
GO
ALTER TABLE [dbo].[workers]  WITH CHECK ADD  CONSTRAINT [CK_WORKER_EMAIL] CHECK  (([dbo].[isValidEmail]([email])=(1)))
GO
ALTER TABLE [dbo].[workers] CHECK CONSTRAINT [CK_WORKER_EMAIL]
GO
/****** Object:  StoredProcedure [dbo].[DeleteWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--DELETE--
create   procedure [dbo].[DeleteWorker]
	@user_id int
as
	DELETE from users
		where user_id=@user_id
GO
/****** Object:  StoredProcedure [dbo].[InsertCustomer]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[InsertCustomer]
	@customer_name varchar(30),
	@email varchar(30),
	@phone_number varchar(30),
	@address varchar(30),
	@user_password varchar(30)
as
	BEGIN TRANSACTION;
		INSERT INTO users(username,
				user_password,
				user_role) 
			VALUES (left(@email, charindex('@', @email) - 1),
					HASHBYTES('SHA2_256', @user_password), 
					'customer')
		IF (@@error <> 0)
        	ROLLBACK
		INSERT INTO customers(user_id, 
				email,
				customer_name, 
				phone_number,
				address)
			VALUES ((select user_id from users
					where username=left(@email,  charindex('@', @email) - 1)),
				@email,
				@customer_name,
				@phone_number,
				@address
			)
	COMMIT TRANSACTION;
GO
/****** Object:  StoredProcedure [dbo].[InsertOrder]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[InsertOrder]
	@customer_id INT,
	@order_date DATETIME
as
	INSERT INTO orders(customer_id, order_date) 
		VALUES (@customer_id, @order_date)
GO
/****** Object:  StoredProcedure [dbo].[InsertOrder_details]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[InsertOrder_details]
	@order_id INT,
	@product_id INT,
	@amount INT
as
	INSERT INTO order_details(order_id, product_id, amount) 
		VALUES (@order_id, @product_id, @amount)
GO
/****** Object:  StoredProcedure [dbo].[InsertProduct]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
--INSERT--
create   procedure [dbo].[InsertProduct]
	@product_name varchar(30),
	@product_type varchar(30),
	@upc_code varchar(12),
	@prime_price decimal(8, 2),
	@discount decimal(8, 2),
	@amount int
as
BEGIN TRANSACTION
	INSERT INTO products(product_name, product_type, upc_code, prime_price) 
		VALUES (@product_name, @product_type, @upc_code, @prime_price)
	Declare @product_id INT
	Set @product_id=(select product_id from products where product_name=@product_name)
	EXEC UpdateDiscount @product_id, @discount
	EXEC UpdateAmountOnStock @product_id, @amount
	IF (@@error <> 0)
		ROLLBACK
COMMIT
GO
/****** Object:  StoredProcedure [dbo].[InsertWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

---
create   procedure [dbo].[InsertWorker]
	@email varchar(30),
	@first_name varchar(30),
	@second_name varchar(30),
	@user_password varchar(30)
as
BEGIN
BEGIN TRANSACTION
	INSERT INTO users(username, user_password, user_role) 
		VALUES (left(@email, charindex('@', @email) - 1), HASHBYTES('SHA2_256', @user_password), 'worker');
	INSERT INTO workers(user_id, email, first_name, second_name)
		VALUES (
			(select user_id from users
				where username=left(@email,  charindex('@', @email) - 1)),
			@email,
			@first_name,
			@second_name
		)
COMMIT
END
GO
/****** Object:  StoredProcedure [dbo].[ShowAllIncome]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowAllIncome]
as
select sum(total_cost - total_prime_cost) as income 
	from Orders
where order_status='completed'
GO
/****** Object:  StoredProcedure [dbo].[ShowAllOrders]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowAllOrders]
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders 
	join customers 
		on orders.customer_id=customers.customer_id
GO
/****** Object:  StoredProcedure [dbo].[ShowAllOrders_Period_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowAllOrders_Period_ForWorker]
	@period int
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders 
	join customers 
		on orders.customer_id=customers.customer_id
where DATEDIFF(day, order_date, GETDATE()) < @period
GO
/****** Object:  StoredProcedure [dbo].[ShowCustomers]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowCustomers]
as
select customer_name,
	email,
	phone_number,
	address
from customers
GO
/****** Object:  StoredProcedure [dbo].[ShowIncomeByCustomer_name]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowIncomeByCustomer_name]
	@customer_name varchar(30)
as
select sum(total_cost - total_prime_cost) as income 
	from Orders
		join customers 
			on orders.customer_id=customers.customer_id
where order_status='completed' and customer_name=@customer_name
GO
/****** Object:  StoredProcedure [dbo].[ShowLackProducts]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowLackProducts]
as
select product_name, 
	   abs(amount_on_stock - ordered) as lack_on_stock 
from (select product_name, 
			 sum(OrdersOrderDetailsCustomersView.amount) as ordered, 
			 stock.amount as amount_on_stock
	  from OrdersOrderDetailsCustomersView 
	  	  join stock 
		  	  on OrdersOrderDetailsCustomersView.product_id=stock.product_id
	  where order_status != 'completed'
	  group by product_name, stock.amount) 
as a
where (amount_on_stock - ordered) < 0
GO
/****** Object:  StoredProcedure [dbo].[ShowLackProductsByCustomer_name]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowLackProductsByCustomer_name]
	@customer_name varchar(30)
as
select product_name, 
	abs(amount_on_stock - ordered) as lack_on_stock 
from
	(select product_name, 
		sum(OrdersOrderDetailsCustomersView.amount) as ordered, 
		stock.amount as amount_on_stock
	from OrdersOrderDetailsCustomersView join stock on OrdersOrderDetailsCustomersView.product_id=stock.product_id
	where order_status != 'completed' and customer_name = @customer_name
	group by product_name, stock.amount) 
as a
where (amount_on_stock - ordered) < 0
GO
/****** Object:  StoredProcedure [dbo].[ShowLackProductsByOrder_id]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowLackProductsByOrder_id]
	@order_id int
as
select product_name, 
	abs(amount_on_stock - ordered) as lack_on_stock 
from
	(select product_name, 
		sum(OrdersOrderDetailsCustomersView.amount) as ordered, 
		stock.amount as amount_on_stock
	from OrdersOrderDetailsCustomersView 
		join stock on OrdersOrderDetailsCustomersView.product_id=stock.product_id
	where order_status != 'completed' and order_id = @order_id
group by product_name, stock.amount) 
as a
where (amount_on_stock - ordered) < 0
GO
/****** Object:  StoredProcedure [dbo].[ShowOrderDetails]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowOrderDetails]
@order_id int
as
select product_name,
		amount, 
		price, 
		cost
	from OrdersOrderDetailsCustomersView
	where order_id = @order_id
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_id_ForCustomer]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowOrdersByCustomer_id_ForCustomer]
	@customer_id int
as
select order_id,
	order_date,
	order_status, 
	total_cost 
from Orders
where customer_id = @customer_id
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_id_Period_ForCustomer]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowOrdersByCustomer_id_Period_ForCustomer]
	@customer_id int,
	@period int
as
select order_id,
	order_date,
	order_status, 
	total_cost
from Orders
where customer_id = @customer_id and DATEDIFF(day, order_date, GETDATE()) < @period
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_idAndOrder_status_ForCustomer]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowOrdersByCustomer_idAndOrder_status_ForCustomer]
	@customer_id int,
	@order_status varchar(30)
as
select order_id,
	order_date,
	order_status, 
	total_cost
from Orders
where customer_id = @customer_id and order_status = @order_status
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_idAndOrder_status_Period_ForCustomer]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowOrdersByCustomer_idAndOrder_status_Period_ForCustomer]
	@customer_id int,
	@order_status varchar(30),
	@period int
as
select order_id,
	order_date,
	order_status, 
	total_cost
from Orders
where customer_id = @customer_id and order_status = @order_status and DATEDIFF(day, order_date, GETDATE()) < @period
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_name_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowOrdersByCustomer_name_ForWorker]
	@customer_name varchar(30)
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders
	join customers 
		on orders.customer_id=customers.customer_id
where customer_name = @customer_name
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_nameAnd_Period_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowOrdersByCustomer_nameAnd_Period_ForWorker]
	@customer_name varchar(30),
	@period int
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders
	join customers 
		on orders.customer_id=customers.customer_id
where customer_name = @customer_name and DATEDIFF(day, order_date, GETDATE()) < @period
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_nameAndOrder_status_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowOrdersByCustomer_nameAndOrder_status_ForWorker]
	@customer_name varchar(30),
	@order_status varchar(30)
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders
	join customers 
		on orders.customer_id=customers.customer_id
where customer_name = @customer_name and order_status = @order_status
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByCustomer_nameAndOrder_statusAnd_Period_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowOrdersByCustomer_nameAndOrder_statusAnd_Period_ForWorker]
	@customer_name varchar(30),
	@order_status varchar(30),
	@period int
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders
	join customers 
		on orders.customer_id=customers.customer_id
where customer_name = @customer_name and order_status = @order_status and DATEDIFF(day, order_date, GETDATE()) < @period
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByOrder_status_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--
create   procedure [dbo].[ShowOrdersByOrder_status_ForWorker]
	@order_status varchar(30)
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders
	join customers 
		on orders.customer_id=customers.customer_id
where order_status = @order_status
GO
/****** Object:  StoredProcedure [dbo].[ShowOrdersByOrder_statusAnd_Period_ForWorker]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowOrdersByOrder_statusAnd_Period_ForWorker]
	@order_status varchar(30),
	@period int
as
select order_id, 
	   customer_name, 
	   order_date,
	   order_status,
	   total_prime_cost,
	   total_cost 
from Orders
	join customers 
		on orders.customer_id=customers.customer_id
where order_status = @order_status and DATEDIFF(day, order_date, GETDATE()) < @period
GO
/****** Object:  StoredProcedure [dbo].[ShowProductsBase]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--PROCEDURES
---Просмотр базы товаров
create   procedure [dbo].[ShowProductsBase] 
as
select product_name,
		product_type,
		upc_code,
		prime_price,
		retail_price,
		discount_price, 
		amount
from ProductsStockView
GO
/****** Object:  StoredProcedure [dbo].[ShowProductsCatalog]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowProductsCatalog] 
as
select product_name,
	    product_type,
	    retail_price, 
	    discount_price 
from ProductsStockView
GO
/****** Object:  StoredProcedure [dbo].[ShowWorkers]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---

---

---
create   procedure [dbo].[ShowWorkers]
as
select username, 
	email,
	first_name, 
	second_name,
	user_role
from workers 
	join users on workers.user_id=users.user_id
GO
/****** Object:  StoredProcedure [dbo].[ShowWorkersByRole]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---
create   procedure [dbo].[ShowWorkersByRole]
	@user_role varchar(10)
as
select username, 
	email,
	first_name, 
	second_name,
	user_role
from workers 
	join users on workers.user_id=users.user_id
	where user_role = @user_role
GO
/****** Object:  StoredProcedure [dbo].[UpdateAmountOnStock]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[UpdateAmountOnStock]
	@product_id int,
	@amount int
as
	UPDATE stock
		set amount = @amount
	where product_id=@product_id
GO
/****** Object:  StoredProcedure [dbo].[UpdateCustomer]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[UpdateCustomer]
	@customer_id int,
	@phone_number varchar(30),
	@address varchar(30)
as
	UPDATE customers
		set phone_number = @phone_number,
			address = @address
	where customer_id=@customer_id
GO
/****** Object:  StoredProcedure [dbo].[UpdateDiscount]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[UpdateDiscount]
	@product_id int,
	@discount decimal(3, 2)
as
	UPDATE discounts
		set discount = @discount
	where product_id=@product_id
GO
/****** Object:  StoredProcedure [dbo].[UpdateOrderStatus]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[UpdateOrderStatus]
	@order_id int,
	@order_status varchar(30)
as
	UPDATE orders
		set order_status = @order_status
	where order_id=@order_id
GO
/****** Object:  StoredProcedure [dbo].[UpdateProduct]    Script Date: 06.12.2022 19:04:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--UPDATE--
create   procedure [dbo].[UpdateProduct]
	@product_id int,
	@product_name varchar(30),
	@product_type varchar(30),
	@upc_code varchar(30),
	@prime_price varchar(30),
	@discount decimal(8, 2),
	@amount int
as
begin TRANSACTION
	UPDATE products
		set product_name = @product_name,
			product_type = @product_type,
			upc_code = @upc_code,
			prime_price = @prime_price
	where product_id=@product_id
	EXEC UpdateDiscount @product_id = @product_id, @discount = @discount
	EXEC UpdateAmountOnStock @product_id = @product_id, @amount = @amount
	IF (@@error <> 0)
        	ROLLBACK
COMMIT
GO
USE [master]
GO
ALTER DATABASE [brewery] SET  READ_WRITE 
GO
