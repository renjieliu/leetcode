/*
2339. All the Matches of the League

Table: Teams

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| team_name   | varchar |
+-------------+---------+
team_name is the primary key of this table.
Each row of this table shows the name of a team.
 

Write an SQL query that reports all the possible matches of the league. Note that every two teams play two matches: home and away. 

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Teams table:
+-------------+
| team_name   |
+-------------+
| Leetcode FC |
| Ahly SC     |
| Real Madrid |
+-------------+
Output: 
+-------------+-------------+
| home_team   | away_team   |
+-------------+-------------+
| Real Madrid | Leetcode FC |
| Real Madrid | Ahly SC     |
| Leetcode FC | Real Madrid |
| Leetcode FC | Ahly SC     |
| Ahly SC     | Real Madrid |
| Ahly SC     | Leetcode FC |
+-------------+-------------+
Explanation: All the matches of the league are shown in the table.


*/


Create table Teams (team_name varchar(50))
Truncate table Teams
insert into Teams (team_name) values ('Leetcode FC')
insert into Teams (team_name) values ('Ahly SC')
insert into Teams (team_name) values ('Real Madrid')


/* Write your T-SQL query statement below */
select 
home_team = t1.team_name 
, away_team = t2.team_name
from Teams t1 , Teams t2 
where t1.team_name != t2.team_name


