/*
1709. Biggest Window Between Visits

Table: UserVisits

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| visit_date  | date |
+-------------+------+
This table does not have a primary key.
This table contains logs of the dates that users vistied a certain retailer.
 

Assume today's date is '2021-1-1'.

Write an SQL query that will, for each user_id, find out the largest window of days between each visit and the one right after it (or today if you are considering the last visit).

Return the result table ordered by user_id.

The query result format is in the following example:

 

UserVisits table:
+---------+------------+
| user_id | visit_date |
+---------+------------+
| 1       | 2020-11-28 |
| 1       | 2020-10-20 |
| 1       | 2020-12-3  |
| 2       | 2020-10-5  |
| 2       | 2020-12-9  |
| 3       | 2020-11-11 |
+---------+------------+
Result table:
+---------+---------------+
| user_id | biggest_window|
+---------+---------------+
| 1       | 39            |
| 2       | 65            |
| 3       | 51            |
+---------+---------------+
For the first user, the windows in question are between dates:
    - 2020-10-20 and 2020-11-28 with a total of 39 days. 
    - 2020-11-28 and 2020-12-3 with a total of 5 days. 
    - 2020-12-3 and 2021-1-1 with a total of 29 days.
Making the biggest window the one with 39 days.
For the second user, the windows in question are between dates:
    - 2020-10-5 and 2020-12-9 with a total of 65 days.
    - 2020-12-9 and 2021-1-1 with a total of 23 days.
Making the biggest window the one with 65 days.
For the third user, the only window in question is between dates 2020-11-11 and 2021-1-1 with a total of 51 days.


*/



Create table If Not Exists UserVisits(user_id int, visit_date date)
Truncate table UserVisits
insert into UserVisits (user_id, visit_date) values ('1', '2020-11-28')
insert into UserVisits (user_id, visit_date) values ('1', '2020-10-20')
insert into UserVisits (user_id, visit_date) values ('1', '2020-12-3')
insert into UserVisits (user_id, visit_date) values ('2', '2020-10-5')
insert into UserVisits (user_id, visit_date) values ('2', '2020-12-9')
insert into UserVisits (user_id, visit_date) values ('3', '2020-11-11')



/* Write your T-SQL query statement below */
select 
user_id 
, biggest_window = max(calc)
from
(select 
user_id
, calc = datediff(day, visit_date, lead(visit_date,1,'2021-01-01') over(partition by user_id order by visit_date))
from UserVisits
) t
group by user_id
order by 1 



/* Write your T-SQL query statement below */
with base as
(
    select * from UserVisits
    union all 
    select u.*, d.date from 
        (select distinct user_id from UserVisits) u cross join (select '2021-01-01' date) d
)
, t as
(
    select 
    rn = row_number() over(partition by user_id order by visit_date)
    , user_id 
    , visit_date 
    from base
)
select 
t.user_id ,
biggest_window = max(datediff(day, t.visit_date, isnull(t1.visit_date,  t.visit_date)) ) 
from t left outer join t t1
on t.user_id = t1.user_id 
and t.rn+1=t1.rn
group by t.user_id
order by t.user_id 



































