/*
1459. Rectangles Area

Table: Points

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| x_value       | int     |
| y_value       | int     |
+---------------+---------+
id is the primary key for this table.
Each point is represented as a 2D Dimensional (x_value, y_value).
Write an SQL query to report of all possible rectangles which can be formed by any two points of the table. 

Each row in the result contains three columns (p1, p2, area) where:

p1 and p2 are the id of two opposite corners of a rectangle and p1 < p2.
Area of this rectangle is represented by the column area.
Report the query in descending order by area in case of tie in ascending order by p1 and p2.

Points table:
+----------+-------------+-------------+
| id       | x_value     | y_value     |
+----------+-------------+-------------+
| 1        | 2           | 8           |
| 2        | 4           | 7           |
| 3        | 2           | 10          |
+----------+-------------+-------------+

Result table:
+----------+-------------+-------------+
| p1       | p2          | area        |
+----------+-------------+-------------+
| 2        | 3           | 6           |
| 1        | 2           | 2           |
+----------+-------------+-------------+

p1 should be less than p2 and area greater than 0.
p1 = 1 and p2 = 2, has an area equal to |2-4| * |8-7| = 2.
p1 = 2 and p2 = 3, has an area equal to |4-2| * |7-10| = 2.
p1 = 1 and p2 = 3 It's not possible because has an area equal to 0.


*/


Create table Points (id int, x_value int, y_value int)
Truncate table Points
insert into Points (id, x_value, y_value) values ('1', '2', '8')
insert into Points (id, x_value, y_value) values ('2', '4', '7')
insert into Points (id, x_value, y_value) values ('3', '2', '10')


/* Write your T-SQL query statement below */
select distinct
po1.id p1
,po2.id p2
,abs( (po1.x_value - po2.x_value) * (po1.y_value - po2.y_value)) area 
from Points po1 
inner join Points po2 on po1.id < po2.id
where (po1.x_value - po2.x_value) * (po1.y_value - po2.y_value) != 0
order by 3 desc, 1 ,2




























