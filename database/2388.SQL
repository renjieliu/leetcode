/*
2388. Change Null Values in a Table to the Previous Value

Table: CoffeeShop

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| drink       | varchar |
+-------------+---------+
id is the primary key for this table.
Each row in this table shows the order id and the name of the drink ordered. Some drink rows are nulls.
 

Write an SQL query to replace the null values of drink with the name of the drink of the previous row that is not null. It is guaranteed that the drink of the first row of the table is not null.

Return the result table in the same order as the input.

The query result format is shown in the following example.

 

Example 1:

Input: 
CoffeeShop table:
+----+------------------+
| id | drink            |
+----+------------------+
| 9  | Mezcal Margarita |
| 6  | null             |
| 7  | null             |
| 3  | Americano        |
| 1  | Daiquiri         |
| 2  | null             |
+----+------------------+
Output: 
+----+------------------+
| id | drink            |
+----+------------------+
| 9  | Mezcal Margarita |
| 6  | Mezcal Margarita |
| 7  | Mezcal Margarita |
| 3  | Americano        |
| 1  | Daiquiri         |
| 2  | Daiquiri         |
+----+------------------+
Explanation: 
For ID 6, the previous value that is not null is from ID 9. We replace the null with "Mezcal Margarita".
For ID 7, the previous value that is not null is from ID 9. We replace the null with "Mezcal Margarita".
For ID 2, the previous value that is not null is from ID 1. We replace the null with "Daiquiri".
Note that the rows in the output are the same as in the input.


*/


Create table CoffeeShop (id int, drink varchar(20))
Truncate table CoffeeShop
insert into CoffeeShop (id, drink) values ('9', 'Mezcal Margarita')
insert into CoffeeShop (id, drink) values ('6', NULL)
insert into CoffeeShop (id, drink) values ('7', NULL)
insert into CoffeeShop (id, drink) values ('3', 'Americano')
insert into CoffeeShop (id, drink) values ('1', 'Daiquiri')
insert into CoffeeShop (id, drink) values ('2', NULL)


/* Write your T-SQL query statement below */
; with cte as
(
  select rn = row_number() over (order by (select null))  -- set a dummy row number with the current record sequence
    , * 
  from coffeeshop
)
select -- to find the most recent previous row with non-null drink
id
, drink = isnull(drink, (select drink from cte c1 where c1.drink is not null and c1.rn < c.rn and not exists (select * from cte c3 where c3.rn < c.rn and c3.rn > c1.rn and c3.drink is not null ) ) )
from cte c


--drop table coffeeshop;


