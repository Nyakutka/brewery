use brewery
go
--PROCEDURES
create procedure ShowProductsBase 
as
select * from ProductsStockView
go
--
create procedure ShowProductsCatalog 
as
select product_name,
	   product_type,
	   retail_price, 
	   discount_price 
from ProductsStockView
go
--
create procedure ShowLackProducts
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
go
--
create procedure ShowAllOrders
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
go
--
create procedure ShowOrdersByCustomer_id
	@customer_id int
as
select order_id,
	order_date,
	order_status, 
	total_cost 
from Orders
where customer_id = @customer_id
go
--
create procedure ShowOrdersByCustomer_idAndOrder_status
	@customer_id int,
	@order_status varchar(30)
as
select order_id,
	order_date,
	order_status, 
	total_cost
from Orders
where customer_id = @customer_id and order_status = @order_status
go
---
create procedure ShowOrderDetails
@order_id int
as
select product_name, amount, price, cost
	from OrdersOrderDetailsCustomersView
	where order_id = @order_id
GO
---
create procedure ShowCustomers
as
select customer_name,
	email,
	phone_number,
	address
from customers
go
---
create procedure ShowAllIncome
as
select sum(total_cost - total_prime_cost) as income 
	from Orders
where order_status='completed'
go
---
create procedure ShowIncomeByCustomer_id
	@customer_id int
as
select sum(total_cost - total_prime_cost) as income 
	from Orders
where order_status='completed' and customer_id=@customer_id
go
---
create procedure ShowLackProductsByOrder_id
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
go
---
create procedure ShowLackProductsByCustomer_name
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
go
---
create procedure ShowWorkers
as
select email, 
	username, 
	first_name, 
	second_name 
from workers 
	join users on workers.user_id=users.user_id
go
---
create procedure InsertProduct
	@product_name varchar(30),
	@product_type varchar(30),
	@upc_code varchar(12),
	@prime_price decimal(8, 2)
as
INSERT INTO products(product_name, product_type, upc_code, prime_price) 
	VALUES (@product_name, @product_type, @upc_code, @prime_price)
GO

---
create procedure InsertWorker
	@email varchar(30),
	@first_name varchar(30),
	@second_name varchar(30),
	@user_password varchar(30)
as
BEGIN
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
END
GO

create procedure InsertCustomer
	@customer_name varchar(30),
	@email varchar(30),
	@phone_number varchar(30),
	@address varchar(30),
	@user_password varchar(30)
as
BEGIN
	INSERT INTO users(username,
			user_password,
			user_role) 
		VALUES (left(@email, charindex('@', @email) - 1),
				HASHBYTES('SHA2_256', @user_password), 
				'customer');
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
END
GO

create procedure InsertOrder
	@customer_id INT,
	@order_date DATETIME
as
	INSERT INTO orders(customer_id, order_date) 
		VALUES (@customer_id, @order_date)
go

create procedure InsertOrder_details
	@order_id INT,
	@product_id INT,
	@amount INT
as
	INSERT INTO order_details(order_id, product_id, amount) 
		VALUES (@order_id, @product_id, @amount)
GO

create procedure UpdateProduct
	@product_id int,
	@product_name varchar(30),
	@product_type varchar(30),
	@upc_code varchar(30),
	@prime_price varchar(30)
as
	UPDATE products
		set product_name = @product_name,
			product_type = @product_type,
			upc_code = @upc_code,
			prime_price = @prime_price
	where product_id=@product_id
GO

create procedure UpdateDiscount
	@product_id int,
	@discount decimal(3, 2)
as
	UPDATE discounts
		set discount = @discount
	where product_id=@product_id
go

create procedure UpdateAmountOnStock
	@product_id int,
	@amount int
as
	UPDATE stock
		set amount = @amount
	where product_id=@product_id
go

create procedure UpdateCustomer
	@customer_id int,
	@phone_number varchar(30),
	@address varchar(30)
as
	UPDATE customers
		set phone_number = @phone_number,
			address = @address
	where customer_id=@customer_id
go

create procedure UpdateOrderStatus
	@order_id int,
	@order_status varchar(30)
as
	UPDATE orders
		set order_status = @order_status
	where order_id=@order_id
go