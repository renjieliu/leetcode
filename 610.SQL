/*

A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.
 

However, this assignment is very heavy because there are hundreds of records to calculate.
 

Could you help Tim by writing a query to judge whether these three sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.
 

| x  | y  | z  |
|----|----|----|
| 13 | 15 | 30 |
| 10 | 20 | 15 |
For the sample data above, your query should return the follow result:
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
*/


Create table triangle (x int, y int, z int)
Truncate table triangle
insert into triangle (x, y, z) values ('13', '15', '30')
insert into triangle (x, y, z) values ('10', '20', '15')



/* Write your T-SQL query statement below */
select x,y,z, 
triangle = case when isnull(x+y,0) >isnull(z,0) and isnull(z+y,0)>isnull(x,0) and isnull(x+z,0)>isnull(y,0) then 'Yes'
			else 'No'
		end 
from triangle



































