use brewery
--PROCEDURES
CREATE procedure ShowProductsBase AS
SELECT * FROM ProductsStockView

CREATE procedure ShowAllOrders AS
SELECT * FROM OrdersOrderDetailsCustomersView

CREATE procedure ShowProductsCatalog AS
SELECT product_name, product_type, retail_price, discount_price FROM OrdersOrderDetailsCustomersView

CREATE procedure ShowMissingProducts AS
SELECT * FROM OrdersOrderDetailsCustomersView