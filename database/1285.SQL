
/*

Table: Logs

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
id is the primary key for this table.
Each row of this table contains the ID in a log Table.

Since some IDs have been removed from Logs. Write an SQL query to find the start and end number of continuous ranges in table Logs.

Order the result table by start_id.

The query result format is in the following example:

Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+

Result table:
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
The result table should contain all ranges in table Logs.
From 1 to 3 is contained in the table.
From 4 to 6 is missing in the table
From 7 to 8 is contained in the table.
Number 9 is missing in the table.
Number 10 is contained in the table.

*/


Create table   Logs (log_id int)
Truncate table Logs
insert into Logs (log_id) values ('1')
insert into Logs (log_id) values ('2')
insert into Logs (log_id) values ('3')
insert into Logs (log_id) values ('7')
insert into Logs (log_id) values ('8')
insert into Logs (log_id) values ('10')



with cte as (
select log_id,  rk = rank() over (order by log_id) from logs
 )
select  start_id = min(log_id), end_id = max(log_id)
  from cte 
group by log_id-rk

