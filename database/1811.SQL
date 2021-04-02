/*
1811. Find Interview Candidates

Table: Contests

+--------------+------+
| Column Name  | Type |
+--------------+------+
| contest_id   | int  |
| gold_medal   | int  |
| silver_medal | int  |
| bronze_medal | int  |
+--------------+------+
contest_id is the primary key for this table.
This table contains the LeetCode contest ID and the user IDs of the gold, silver, and bronze medalists.
It is guaranteed that any consecutive contests have consecutive IDs and that no ID is skipped.
 

Table: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| mail        | varchar |
| name        | varchar |
+-------------+---------+
user_id is the primary key for this table.
This table contains information about the users.
 

Write an SQL query to report the name and the mail of all interview candidates. A user is an interview candidate if at least one of these two conditions is true:

The user won any medal in three or more consecutive contests.
The user won the gold medal in three or more different contests (not necessarily consecutive).
Return the result table in any order.

The query result format is in the following example:

 

Contests table:
+------------+------------+--------------+--------------+
| contest_id | gold_medal | silver_medal | bronze_medal |
+------------+------------+--------------+--------------+
| 190        | 1          | 5            | 2            |
| 191        | 2          | 3            | 5            |
| 192        | 5          | 2            | 3            |
| 193        | 1          | 3            | 5            |
| 194        | 4          | 5            | 2            |
| 195        | 4          | 2            | 1            |
| 196        | 1          | 5            | 2            |
+------------+------------+--------------+--------------+

Users table:
+---------+--------------------+-------+
| user_id | mail               | name  |
+---------+--------------------+-------+
| 1       | sarah@leetcode.com | Sarah |
| 2       | bob@leetcode.com   | Bob   |
| 3       | alice@leetcode.com | Alice |
| 4       | hercy@leetcode.com | Hercy |
| 5       | quarz@leetcode.com | Quarz |
+---------+--------------------+-------+

Result table:
+-------+--------------------+
| name  | mail               |
+-------+--------------------+
| Sarah | sarah@leetcode.com |
| Bob   | bob@leetcode.com   |
| Alice | alice@leetcode.com |
| Quarz | quarz@leetcode.com |
+-------+--------------------+

Sarah won 3 gold medals (190, 193, and 196), so we include her in the result table.
Bob won a medal in 3 consecutive contests (190, 191, and 192), so we include him in the result table.
    - Note that he also won a medal in 3 other consecutive contests (194, 195, and 196).
Alice won a medal in 3 consecutive contests (191, 192, and 193), so we include her in the result table.
Quarz won a medal in 5 consecutive contests (190, 191, 192, 193, and 194), so we include them in the result table.
 

Follow up:

What if the first condition changed to be "any medal in n or more consecutive contests"? How would you change your solution to get the interview candidates? Imagine that n is the parameter of a stored procedure.
Suppose we tracked which contests each user participated in. What if we wanted to consider candidates that won any medal in three or more consecutive contests where they were a participant? How would this change your solution?


*/


Create table Contests (contest_id int, gold_medal int, silver_medal int, bronze_medal int)
Create table Users (user_id int, mail varchar(50), name varchar(30))
Truncate table Contests
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('190', '1', '5', '2')
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('191', '2', '3', '5')
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('192', '5', '2', '3')
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('193', '1', '3', '5')
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('194', '4', '5', '2')
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('195', '4', '2', '1')
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('196', '1', '5', '2')
Truncate table Users
insert into Users (user_id, mail, name) values ('1', 'sarah@leetcode.com', 'Sarah')
insert into Users (user_id, mail, name) values ('2', 'bob@leetcode.com', 'Bob')
insert into Users (user_id, mail, name) values ('3', 'alice@leetcode.com', 'Alice')
insert into Users (user_id, mail, name) values ('4', 'hercy@leetcode.com', 'Hercy')
insert into Users (user_id, mail, name) values ('5', 'quarz@leetcode.com', 'Quarz')


/* Write your T-SQL query statement below */
with base as (
select contest_id, user_id = gold_medal, medal = 'gold' from contests 
union 
select contest_id, user_id = silver_medal, medal = 'silver' from contests 
union 
select contest_id, user_id = bronze_medal, medal = 'bronze' from contests 
), cte as 
(select contest_id, user_id, cnt = 1 from base
union all 
select base.contest_id, cte.user_id, cte.cnt+1
from cte inner join base on base.contest_id = cte.contest_id + 1 and base.user_id = cte.user_id
), usr as(
select user_id from cte 
where cnt >= 3
union 
select user_id from base  
where medal = 'gold'
group by user_id
having count(distinct contest_id) >=3
)
select distinct 
main.name
, main.mail
from usr u inner join Users main on u.user_id = main.user_id



































