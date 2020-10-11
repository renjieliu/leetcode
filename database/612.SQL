/*

Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.
 

Write a query to find the shortest distance between these points rounded to 2 decimals.
 

| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
 

The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
 

| shortest |
|----------|
| 1.00     |
 

Note: The longest distance among all the points are less than 10000.
*/


CREATE TABLE  point_2d (x INT NOT NULL, y INT NOT NULL)
Truncate table point_2d
insert into point_2d (x, y) values ('-1', '-1')
insert into point_2d (x, y) values ('0', '0')
insert into point_2d (x, y) values ('-1', '-2')


/* Write your T-SQL query statement below */
select shortest= min( power ( 1.00*(f.x-s.x)*(f.x-s.x) +  1.00*(f.y-s.y)*(f.y-s.y),0.5) )
from point_2d f, point_2d s
where 
power ( 1.00*(f.x-s.x)*(f.x-s.x) +  1.00*(f.y-s.y)*(f.y-s.y),0.5) > 0 --to avoid the same point

--cast(f.x as varchar(max)) + '-' + cast(f.y as varchar(max)) <> cast(s.x as varchar(max)) + '-' + cast(s.y as varchar(max))


























