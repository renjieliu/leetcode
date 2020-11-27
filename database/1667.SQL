/*
1667. Fix Names in a Table


Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The query result format is in the following example:

 

Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+

Result table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+



*/



Create table Activity (user_id int, name varchar(40))
Truncate table Activity
insert into Activity (user_id, name) values ('1', 'aLice')
insert into Activity (user_id, name) values ('2', 'bOB')



/* Write your T-SQL query statement below */
select 
user_id
,name = upper(left(name,1)) + lower(right(name , len(name)-1))
from Activity 
order by user_id







































