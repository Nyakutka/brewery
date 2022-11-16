use brewery
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