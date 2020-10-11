/*
1435. Create a Session Bar Chart



Table: Sessions

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| session_id          | int     |
| duration            | int     |
+---------------------+---------+
session_id is the primary key for this table.
duration is the time in seconds that a user has visited the application.
 

You want to know how long a user visits your application. You decided to create bins of "[0-5>", "[5-10>", "[10-15>" and "15 minutes or more" and count the number of sessions on it.

Write an SQL query to report the (bin, total) in any order.

The query result format is in the following example.

Sessions table:
+-------------+---------------+
| session_id  | duration      |
+-------------+---------------+
| 1           | 30            |
| 2           | 199           |
| 3           | 299           |
| 4           | 580           |
| 5           | 1000          |
+-------------+---------------+

Result table:
+--------------+--------------+
| bin          | total        |
+--------------+--------------+
| [0-5>        | 3            |
| [5-10>       | 1            |
| [10-15>      | 0            |
| 15 or more   | 1            |
+--------------+--------------+

For session_id 1, 2 and 3 have a duration greater or equal than 0 minutes and less than 5 minutes.
For session_id 4 has a duration greater or equal than 5 minutes and less than 10 minutes.
There are no session with a duration greater or equial than 10 minutes and less than 15 minutes.
For session_id 5 has a duration greater or equal than 15 minutes.


*/


Create table Sessions (session_id int, duration int)
Truncate table Sessions
insert into Sessions (session_id, duration) values ('1', '30')
insert into Sessions (session_id, duration) values ('2', '199')
insert into Sessions (session_id, duration) values ('3', '299')
insert into Sessions (session_id, duration) values ('4', '580')
insert into Sessions (session_id, duration) values ('5', '1000')



with cte as (select '[0-5>' as BIN union select '[5-10>' union select '[10-15>' union select '15 or more')
select 
cte.bin BIN
,count(session_id) total
from 
cte 
left outer join Sessions 
on cte.bin = case when duration >= 0 and duration<300 then '[0-5>'
                           when duration >= 300 and duration<600 then '[5-10>'
                           when duration >= 600 and duration<900 then '[10-15>'
                           when duration >= 900 then '15 or more'
             end
group by 
cte.bin
order by --Optional Order By
len(cte.bin)








