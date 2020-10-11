/*

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
 

Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

The query result format is in the following example:

Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+

Result table:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+

*/


Create table   Products (product_id int, new_price int, change_date date)
Truncate table Products
insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14')
insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14')
insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15')
insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16')
insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17')
insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18')

--select * from Products 


; with t as 
(select distinct product_id, new_price, change_date from Products
where change_date <='2019-08-16'
union all
select distinct product_id, 10, '1990-01-01' from Products 
)  
select product_id, price = new_price from t 
where not exists (select * from t t1 where t1.product_id = t.product_id and t1.change_date > t.change_date)