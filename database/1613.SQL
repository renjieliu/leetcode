/*
1613. Find the Missing IDs

Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the primary key for this table.
Each row of this table contains the name and the id customer.
 

Write an SQL query to find the missing customer IDs. The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.

Notice that the maximum customer_id will not exceed 100.

Return the result table ordered by ids in ascending order.

The query result format is in the following example.

 

Customer table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+

Result table:
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+
The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.


*/



Create table Customers (customer_id int, customer_name varchar(20))
Truncate table Customers
insert into Customers (customer_id, customer_name) values ('1', 'Alice')
insert into Customers (customer_id, customer_name) values ('4', 'Bob')
insert into Customers (customer_id, customer_name) values ('5', 'Charlie')


/* Write your T-SQL query statement below */
with id_max as 
(   
    select id = max(customer_id) from Customers
)
, cte as
(
    select ids = 1 from Customers
     union all 
    select ids+1 from cte 
     where ids+1 < (select id from id_max)
)
select ids from cte 
except 
select customer_id from Customers
order by 1 





































