/*
2082. The Number of Rich Customers

Table: Store

+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
bill_id is the primary key for this table.
Each row contains information about the amount of one bill and the customer associated with it.
 

Write an SQL query to report the number of customers who had at least one bill with an amount strictly greater than 500.

The query result format is in the following example.

 

Example 1:

Input: 
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
Output: 
+------------+
| rich_count |
+------------+
| 2          |
+------------+
Explanation: 
Customer 1 has two bills with amounts strictly greater than 500.
Customer 2 does not have any bills with an amount strictly greater than 500.
Customer 3 has one bill with an amount strictly greater than 500.


*/


Create table Store (bill_id int, customer_id int, amount int)
Truncate table Store
insert into Store (bill_id, customer_id, amount) values ('6', '1', '549')
insert into Store (bill_id, customer_id, amount) values ('8', '1', '834')
insert into Store (bill_id, customer_id, amount) values ('4', '2', '394')
insert into Store (bill_id, customer_id, amount) values ('11', '3', '657')
insert into Store (bill_id, customer_id, amount) values ('13', '3', '257')


/* Write your T-SQL query statement below */
select 
rich_count = isnull(count(distinct customer_id), 0)
from store
where amount > 500 

