/*
The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+
Write a query to find the median of all numbers and name the result as median.

*/


Create table Numbers (Number int, Frequency int)
Truncate table Numbers
insert into Numbers (Number, Frequency) values ('0', '7')
insert into Numbers (Number, Frequency) values ('1', '1')
insert into Numbers (Number, Frequency) values ('2', '3')
insert into Numbers (Number, Frequency) values ('3', '1')


;with pos as 
(select rn = case when sum(Frequency)%2 = 1 then sum(Frequency)/2+1  else  sum(Frequency)/2 end  from Numbers  
union all 
select rn = sum(Frequency)/2+1 from Numbers  
),
tmp as (select *, runningcnt = (select sum(Frequency) from Numbers n2 where n2.Number <= n1.Number ) from Numbers n1
), stg as(
select pick =  min(Number) from tmp 
where runningcnt >= (select min(rn) from pos) --to pick the first number
union all 
select min(Number) from tmp 
where runningcnt >= (select max(rn) from pos) --to pick the second number
)
select median = avg(pick*1.0) from stg
