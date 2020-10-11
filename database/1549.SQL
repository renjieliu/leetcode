/*
1549. The Most Recent Orders for Each Product

Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
+---------------+---------+
customer_id is the primary key for this table.
This table contains information about the customers.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| product_id    | int     |
+---------------+---------+
order_id is the primary key for this table.
This table contains information about the orders made by customer_id.
There will be no product ordered by the same user more than once in one day.
 

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| price         | int     |
+---------------+---------+
product_id is the primary key for this table.
This table contains information about the Products.
 

Write an SQL query to find the most recent order(s) of each product.

Return the result table sorted by product_name in ascending order and in case of a tie by the product_id in ascending order. If there still a tie, order them by the order_id in ascending order.

The query result format is in the following example:

Customers
+-------------+-----------+
| customer_id | name      |
+-------------+-----------+
| 1           | Winston   |
| 2           | Jonathan  |
| 3           | Annabelle |
| 4           | Marwan    |
| 5           | Khaled    |
+-------------+-----------+

Orders
+----------+------------+-------------+------------+
| order_id | order_date | customer_id | product_id |
+----------+------------+-------------+------------+
| 1        | 2020-07-31 | 1           | 1          |
| 2        | 2020-07-30 | 2           | 2          |
| 3        | 2020-08-29 | 3           | 3          |
| 4        | 2020-07-29 | 4           | 1          |
| 5        | 2020-06-10 | 1           | 2          |
| 6        | 2020-08-01 | 2           | 1          |
| 7        | 2020-08-01 | 3           | 1          |
| 8        | 2020-08-03 | 1           | 2          |
| 9        | 2020-08-07 | 2           | 3          |
| 10       | 2020-07-15 | 1           | 2          |
+----------+------------+-------------+------------+

Products
+------------+--------------+-------+
| product_id | product_name | price |
+------------+--------------+-------+
| 1          | keyboard     | 120   |
| 2          | mouse        | 80    |
| 3          | screen       | 600   |
| 4          | hard disk    | 450   |
+------------+--------------+-------+

Result table:
+--------------+------------+----------+------------+
| product_name | product_id | order_id | order_date |
+--------------+------------+----------+------------+
| keyboard     | 1          | 6        | 2020-08-01 |
| keyboard     | 1          | 7        | 2020-08-01 |
| mouse        | 2          | 8        | 2020-08-03 |
| screen       | 3          | 3        | 2020-08-29 |
+--------------+------------+----------+------------+
keyboard's most recent order is in 2020-08-01, it was ordered two times this day.
mouse's most recent order is in 2020-08-03, it was ordered only once this day.
screen's most recent order is in 2020-08-29, it was ordered only once this day.
The hard disk was never ordered and we don't include it in the result table.



*/

Create table Customers (customer_id int, name varchar(10))
Create table Orders (order_id int, order_date date, customer_id int, product_id int)
Create table Products (product_id int, product_name varchar(20), price int)
Truncate table Customers
insert into Customers (customer_id, name) values ('1', 'Winston')
insert into Customers (customer_id, name) values ('2', 'Jonathan')
insert into Customers (customer_id, name) values ('3', 'Annabelle')
insert into Customers (customer_id, name) values ('4', 'Marwan')
insert into Customers (customer_id, name) values ('5', 'Khaled')
Truncate table Orders
insert into Orders (order_id, order_date, customer_id, product_id) values ('1', '2020-07-31', '1', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('2', '2020-7-30', '2', '2')
insert into Orders (order_id, order_date, customer_id, product_id) values ('3', '2020-08-29', '3', '3')
insert into Orders (order_id, order_date, customer_id, product_id) values ('4', '2020-07-29', '4', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('5', '2020-06-10', '1', '2')
insert into Orders (order_id, order_date, customer_id, product_id) values ('6', '2020-08-01', '2', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('7', '2020-08-01', '3', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('8', '2020-08-03', '1', '2')
insert into Orders (order_id, order_date, customer_id, product_id) values ('9', '2020-08-07', '2', '3')
insert into Orders (order_id, order_date, customer_id, product_id) values ('10', '2020-07-15', '1', '2')
Truncate table Products
insert into Products (product_id, product_name, price) values ('1', 'keyboard', '120')
insert into Products (product_id, product_name, price) values ('2', 'mouse', '80')
insert into Products (product_id, product_name, price) values ('3', 'screen', '600')
insert into Products (product_id, product_name, price) values ('4', 'hard disk', '450')


/* Write your T-SQL query statement below */
select 
p.product_name
,p.product_id
,t.order_id
,t.order_date
from Products p 
cross apply (Select top 1 with ties * from Orders o where o.product_id = p.product_id order by order_date desc) t 
order by p.product_name, p.product_id, t.order_id 
























