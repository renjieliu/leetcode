/*
1777. Product's Price for Each Store

Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | enum    |
| price       | int     |
+-------------+---------+
(product_id,store) is the primary key for this table.
store is an ENUM of type ('store1', 'store2', 'store3') where each represents the store this product is available at.
price is the price of the product at this store.
 

Write an SQL query to find the price of each product in each store.

Return the result table in any order.

The query result format is in the following example:

 

Products table:
+-------------+--------+-------+
| product_id  | store  | price |
+-------------+--------+-------+
| 0           | store1 | 95    |
| 0           | store3 | 105   |
| 0           | store2 | 100   |
| 1           | store1 | 70    |
| 1           | store3 | 80    |
+-------------+--------+-------+
Result table:
+-------------+--------+--------+--------+
| product_id  | store1 | store2 | store3 |
+-------------+--------+--------+--------+
| 0           | 95     | 100    | 105    |
| 1           | 70     | null   | 80     |
+-------------+--------+--------+--------+
Product 0 price's are 95 for store1, 100 for store2 and, 105 for store3.
Product 1 price's are 70 for store1, 80 for store3 and, it's not sold in store2.



*/


Create table Products (product_id int, store ENUM('store1', 'store2', 'store3'), price int)
Truncate table Products
insert into Products (product_id, store, price) values ('0', 'store1', '95')
insert into Products (product_id, store, price) values ('0', 'store3', '105')
insert into Products (product_id, store, price) values ('0', 'store2', '100')
insert into Products (product_id, store, price) values ('1', 'store1', '70')
insert into Products (product_id, store, price) values ('1', 'store3', '80')


/* Write your T-SQL query statement below */
-- select
-- product_id =  product_id
-- , store1 = sum(case when store = 'store1' then price else NULL end)
-- , store2 = sum(case when store = 'store2' then price else NULL end)
-- , store3 = sum(case when store = 'store3' then price else NULL end)
-- from products
-- group by product_id

select 
product_id
, store1
, store2
, store3 
from 
(select * from products) base 
pivot(
sum(price)
for store in 
    ([store1], [store2], [store3])
) pvt





















































