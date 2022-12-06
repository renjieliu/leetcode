/*
2494. Merge Overlapping Events in the Same Hall

Table: HallEvents

+-------------+------+
| Column Name | Type |
+-------------+------+
| hall_id     | int  |
| start_day   | date |
| end_day     | date |
+-------------+------+
There is no primary key in this table. It may contain duplicates.
Each row of this table indicates the start day and end day of an event and the hall in which the event is held.
 

Write an SQL query to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
HallEvents table:
+---------+------------+------------+
| hall_id | start_day  | end_day    |
+---------+------------+------------+
| 1       | 2023-01-13 | 2023-01-14 |
| 1       | 2023-01-14 | 2023-01-17 |
| 1       | 2023-01-18 | 2023-01-25 |
| 2       | 2022-12-09 | 2022-12-23 |
| 2       | 2022-12-13 | 2022-12-17 |
| 3       | 2022-12-01 | 2023-01-30 |
+---------+------------+------------+
Output: 
+---------+------------+------------+
| hall_id | start_day  | end_day    |
+---------+------------+------------+
| 1       | 2023-01-13 | 2023-01-17 |
| 1       | 2023-01-18 | 2023-01-25 |
| 2       | 2022-12-09 | 2022-12-23 |
| 3       | 2022-12-01 | 2023-01-30 |
+---------+------------+------------+
Explanation: There are three halls.
Hall 1:
- The two events ["2023-01-13", "2023-01-14"] and ["2023-01-14", "2023-01-17"] overlap. We merge them in one event ["2023-01-13", "2023-01-17"].
- The event ["2023-01-18", "2023-01-25"] does not overlap with any other event, so we leave it as it is.
Hall 2:
- The two events ["2022-12-09", "2022-12-23"] and ["2022-12-13", "2022-12-17"] overlap. We merge them in one event ["2022-12-09", "2022-12-23"].
Hall 3:
- The hall has only one event, so we return it. Note that we only consider the events of each hall separately.



*/


Create table  HallEvents (hall_id int, start_day date, end_day date)
Truncate table HallEvents
insert into HallEvents (hall_id, start_day, end_day) values ('1', '2023-01-13', '2023-01-14')
insert into HallEvents (hall_id, start_day, end_day) values ('1', '2023-01-14', '2023-01-17')
insert into HallEvents (hall_id, start_day, end_day) values ('1', '2023-01-18', '2023-01-25')
insert into HallEvents (hall_id, start_day, end_day) values ('2', '2022-12-09', '2022-12-23')
insert into HallEvents (hall_id, start_day, end_day) values ('2', '2022-12-13', '2022-12-17')
insert into HallEvents (hall_id, start_day, end_day) values ('3', '2022-12-01', '2023-01-30')

go

/* Write your T-SQL query statement below */

with base as
(
	select 
	rn = ROW_NUMBER() over (partition by Hall_id order by start_day)
	, *
	from HallEvents 
)
,cte as 
(select rn, hall_id, start_day, end_day, root_start = start_day from base
	union all 
 select h.rn, h.hall_id, h.start_day, h.end_day, c.root_start from base h inner join cte c 
 on h.hall_id = c.hall_id and (h.start_day between c.start_day and c.end_day or h.end_day between c.start_day and c.end_day)
    and h.rn > c.rn -- to avoid infinite loop, to find the range other than current line, to avoid infinite loop
)
, s_date as (
select 
hall_id
, end_day
, start_day = min(root_start) -- find the root date for each date range
from cte 
group by hall_id, end_day
)
select 
hall_id
, start_day
, end_day = max(end_day) -- find when the range ends
from s_date
group by 
hall_id
, start_day
order by 1


