/* 
1867. Orders With Maximum Quantity Above Average

Table: OrdersDetails

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(order_id, product_id) is the primary key for this table.
Each row of this table contains the quantity ordered of the product product_id in the order order_id.
A single order with k different products will appear as k separate rows in this table.
 

The average quantity of an order is calculated as (total quantity of products in the order) / (number of different products in the order). The maximum average quantity is the highest average quantity among all orders.

The maximum quantity of an order is the highest quantity of any product purchased in the order.

Write an SQL query to find the order_id of all orders whose maximum quantity is strictly greater than the maximum average quantity.

Return the result table in any order.

The query result format is in the following example:

 

OrdersDetails table:
+----------+------------+----------+
| order_id | product_id | quantity |
+----------+------------+----------+
| 1        | 1          | 12       |
| 1        | 2          | 10       |
| 1        | 3          | 15       |
| 2        | 1          | 8        |
| 2        | 4          | 4        |
| 2        | 5          | 6        |
| 3        | 3          | 5        |
| 3        | 4          | 18       |
| 4        | 5          | 2        |
| 4        | 6          | 8        |
| 5        | 7          | 9        |
| 5        | 8          | 9        |
| 3        | 9          | 20       |
| 2        | 9          | 4        |
+----------+------------+----------+

Result table:
+----------+
| order_id |
+----------+
| 1        |
| 3        |
+----------+

The average quantity of each order is:
- order_id=1: (12+10+5)/3 = 9
- order_id=2: (8+4+6+4)/4 = 5.5
- order_id=3: (5+18+20)/3 = 14.333333
- order_id=4: (2+8)/2 = 5
- order_id=5: (9+9)/2 = 9
The maximum average quantity is 14.333333

The maximum quantity of each order is:
- order_id=1: max(12, 10, 5) = 12
- order_id=2: max(8, 4, 6, 4) = 8
- order_id=3: max(5, 18, 20) = 20
- order_id=4: max(2, 8) = 8
- order_id=5: max(9, 9) = 9
Only orders 1 and 3 have a maximum quantity strictly greater than the maximum average quantity.




*/



Create table OrdersDetails (order_id int, product_id int, quantity int)
Truncate table OrdersDetails
insert into OrdersDetails (order_id, product_id, quantity) values ('1', '1', '12')
insert into OrdersDetails (order_id, product_id, quantity) values ('1', '2', '10')
insert into OrdersDetails (order_id, product_id, quantity) values ('1', '3', '15')
insert into OrdersDetails (order_id, product_id, quantity) values ('2', '1', '8')
insert into OrdersDetails (order_id, product_id, quantity) values ('2', '4', '4')
insert into OrdersDetails (order_id, product_id, quantity) values ('2', '5', '6')
insert into OrdersDetails (order_id, product_id, quantity) values ('3', '3', '5')
insert into OrdersDetails (order_id, product_id, quantity) values ('3', '4', '18')
insert into OrdersDetails (order_id, product_id, quantity) values ('4', '5', '2')
insert into OrdersDetails (order_id, product_id, quantity) values ('4', '6', '8')
insert into OrdersDetails (order_id, product_id, quantity) values ('5', '7', '9')
insert into OrdersDetails (order_id, product_id, quantity) values ('5', '8', '9')
insert into OrdersDetails (order_id, product_id, quantity) values ('3', '9', '20')
insert into OrdersDetails (order_id, product_id, quantity) values ('2', '9', '4')




/* Write your T-SQL query statement below */
with a_quantity as 
(
select 
order_id
,avg_quantity = 1.0*sum(quantity) / count(product_id) 
from OrdersDetails 
group by order_id
)
select 
order_id
from OrdersDetails
group by order_id
having max(quantity*1.0) > (select max(avg_quantity) from a_quantity)
























