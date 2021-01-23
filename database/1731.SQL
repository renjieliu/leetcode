/*
1731. The Number of Employees Which Report to Each Employee


+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the primary key for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). 
 

Write an SQL query to report the ids and the names of the people that other employees reported to (excluding null values), the number of employees who report to them, and the average age of those members rounded to the nearest integer.

Return the result table ordered by employee_id.

The query result format is in the following example:

 

Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+

Result table:
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
Alice and Bob report to Hercy, hence Hercy has 2 people report to him, and the average of their age is (41+36)/2 = 38.5 which is 39 after rounding it to the nearest integer.




*/

Create table Employees(employee_id int, name varchar(20), reports_to int, age int)
Truncate table Employees
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', 'None', '43')
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', 'None', '37')


/* Write your T-SQL query statement below */
select 
e.employee_id
, e.name
, reports_count = count(r.employee_id)
, average_age = cast(avg(r.age*1.0) as decimal(38,0))
from Employees e 
inner join Employees r on r.reports_to = e.employee_id 
group by e.employee_id, e.name
order by 1
























