/*
1972. First and Last Call On the Same Day

Table: Calls

+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
+--------------+----------+
(caller_id, recipient_id, call_time) is the primary key for this table.
Each row contains information about a call the time of a call between caller_id and recipient_id.
 

Write an SQL query to report the IDs of the user who had the first and the last call with the same person on any day.

Return the result table in any order.

The query result format is in the following example:

 

Calls table:
+-----------+--------------+---------------------+
| caller_id | recipient_id | call_time           |
+-----------+--------------+---------------------+
| 8         | 4            | 2021-08-24 17:46:07 |
| 4         | 8            | 2021-08-24 19:57:13 |
| 5         | 1            | 2021-08-11 05:28:44 |
| 8         | 3            | 2021-08-17 04:04:15 |
| 11        | 3            | 2021-08-17 13:07:00 |
| 8         | 11           | 2021-08-17 22:22:22 |
+-----------+--------------+---------------------+

Result table:
+---------+
| user_id |
+---------+
| 1       |
| 4       |
| 5       |
| 8       |
+---------+

On 2021-08-24, the first and last call of this day for user 8 was with user 4. User 8 should be included in the answer.
Similary, User 4 had the first and last call on 2021-08-24 with user 8. User 4 should be included in the answer.
On 2021-08-11, user 1 and 5 had a call. The call was the only call for both of them on this day. Since this call is the first and last call of the day for both of them, they both should be included in the answr.

*/


Create table Calls (caller_id int, recipient_id int, call_time datetime)
Truncate table Calls
insert into Calls (caller_id, recipient_id, call_time) values ('8', '4', '2021-08-24 17:46:07')
insert into Calls (caller_id, recipient_id, call_time) values ('4', '8', '2021-08-24 19:57:13')
insert into Calls (caller_id, recipient_id, call_time) values ('5', '1', '2021-08-11 05:28:44')
insert into Calls (caller_id, recipient_id, call_time) values ('8', '3', '2021-08-17 04:04:15')
insert into Calls (caller_id, recipient_id, call_time) values ('11', '3', '2021-08-17 13:07:00')
insert into Calls (caller_id, recipient_id, call_time) values ('8', '11', '2021-08-17 22:22:22')


--MySQL solution
# Write your MySQL query statement below
with cte as
(select caller_id user_id , recipient_id user2_id , call_time from calls
 union 
 select recipient_id, caller_id, call_time from calls
) 
select distinct cte.user_id from cte 
inner join cte firstCalling 
on cte.user_id = firstCalling.user_id and left(cte.call_time, 10) = left(firstCalling.call_time, 10)
inner join cte lastCalling
on cte.user_id = lastCalling.user_id and firstCalling.user2_id = lastCalling.user2_id and left(cte.call_time, 10) = left(lastCalling.call_time, 10)
where not exists 
(select * from 
 cte a 
 where a.user_id = cte.user_id and left(a.call_time, 10) = left(firstCalling.call_time, 10)
 and a.call_time < firstCalling.call_time
)
and not exists
(select * from 
 cte b 
 where b.user_id = cte.user_id and left(b.call_time, 10) = left(lastCalling.call_time, 10)
 and b.call_time > lastCalling.call_time
)



--Oracle Solution
/* Write your PL/SQL query statement below */
with cte as
(select caller_id user_id , recipient_id user2_id , call_time from calls
 union 
 select recipient_id, caller_id, call_time from calls
) 
select distinct cte.user_id from cte 
inner join cte firstCalling 
on cte.user_id = firstCalling.user_id and to_char(cte.call_time, 'YYYYMMDD') = to_char(firstCalling.call_time, 'YYYYMMDD')
inner join cte lastCalling
on cte.user_id = lastCalling.user_id and firstCalling.user2_id = lastCalling.user2_id and to_char(cte.call_time, 'YYYYMMDD') = to_char(lastCalling.call_time, 'YYYYMMDD')
where not exists 
(select * from 
 cte a 
 where a.user_id = cte.user_id and to_char(a.call_time, 'YYYYMMDD') = to_char(firstCalling.call_time, 'YYYYMMDD')
 and a.call_time < firstCalling.call_time
)
and not exists
(select * from 
 cte b 
 where b.user_id = cte.user_id and to_char(b.call_time, 'YYYYMMDD') = to_char(lastCalling.call_time, 'YYYYMMDD')
 and b.call_time > lastCalling.call_time
)




--SQL Server approach - same idea, but got TLE

/* Write your T-SQL query statement below */
with cte as
(select user_id = caller_id, user2_id = recipient_id, call_time from calls
 union 
 select recipient_id, caller_id, call_time from calls
) 
select distinct cte.user_id from cte 
inner join cte firstCalling 
on cte.user_id = firstCalling.user_id and format(cte.call_time, 'yyyyMMdd') = format(firstCalling.call_time, 'yyyyMMdd')
inner join cte lastCalling
on cte.user_id = lastCalling.user_id and firstCalling.user2_id = lastCalling.user2_id and format(cte.call_time, 'yyyyMMdd') = format(lastCalling.call_time, 'yyyyMMdd')
where not exists 
(select * from 
 cte a 
 where a.user_id = cte.user_id and format(a.call_time, 'yyyyMMdd') = format(firstCalling.call_time, 'yyyyMMdd')
 and a.call_time < firstCalling.call_time
)
and not exists
(select * from 
 cte b 
 where b.user_id = cte.user_id and format(b.call_time, 'yyyyMMdd') = format(lastCalling.call_time, 'yyyyMMdd')
 and b.call_time > lastCalling.call_time
)


































