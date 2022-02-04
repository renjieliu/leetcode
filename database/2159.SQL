/*
2159. Order Two Columns Independently


Table: Data

+-------------+------+
| Column Name | Type |
+-------------+------+
| first_col   | int  |
| second_col  | int  |
+-------------+------+
There is no primary key for this table and it may contain duplicates.
 

Write an SQL query to independently:

order first_col in ascending order.
order second_col in descending order.
The query result format is in the following example.

 

Example 1:

Input: 
Data table:
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 4         | 2          |
| 2         | 3          |
| 3         | 1          |
| 1         | 4          |
+-----------+------------+
Output: 
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 1         | 4          |
| 2         | 3          |
| 3         | 2          |
| 4         | 1          |
+-----------+------------+


*/

Create table Data (first_col int, second_col int)
Truncate table Data
insert into Data (first_col, second_col) values ('4', '2')
insert into Data (first_col, second_col) values ('2', '3')
insert into Data (first_col, second_col) values ('3', '1')
insert into Data (first_col, second_col) values ('1', '4')
;
/* Write your T-SQL query statement below */
with cte as 
(
    select 
     row_number() over(order by first_col) rn_1
     , first_col
     , row_number() over(order by second_col desc) rn_2 
     , second_col
     from data
)
select 
c1.first_col
, c2.second_col
from cte c1 inner join cte c2 on c1.rn_1 = c2.rn_2
order by 1, 2 desc


