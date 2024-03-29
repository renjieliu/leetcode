/*
2346. Compute the Rank as a Percentage

Table: Students

+---------------+------+
| Column Name   | Type |
+---------------+------+
| student_id    | int  |
| department_id | int  |
| mark          | int  |
+---------------+------+
user_id is the primary key of this table.
Each row of this table indicates a student's ID, the ID of the department in which the student enrolled, and their mark in the exam.
 

Write an SQL query that reports the rank of each student in their department as a percentage, where the rank as a percentage is computed using the following formula: (student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1). The percentage should be rounded to 2 decimal places. student_rank_in_the_department is determined by descending mark, such that the student with the highest mark is rank 1.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Students table:
+------------+---------------+------+
| student_id | department_id | mark |
+------------+---------------+------+
| 2          | 2             | 650  |
| 8          | 2             | 650  |
| 7          | 1             | 920  |
| 1          | 1             | 610  |
| 3          | 1             | 530  |
+------------+---------------+------+
Output: 
+------------+---------------+------------+
| student_id | department_id | percentage |
+------------+---------------+------------+
| 7          | 1             | 0.0        |
| 1          | 1             | 50.0       |
| 3          | 1             | 100.0      |
| 2          | 2             | 0.0        |
| 8          | 2             | 0.0        |
+------------+---------------+------------+
Explanation: 
For Department 1:
 - Student 7: percentage = (1 - 1) * 100 / (3 - 1) = 0.0
 - Student 1: percentage = (2 - 1) * 100 / (3 - 1) = 50.0
 - Student 3: percentage = (3 - 1) * 100 / (3 - 1) = 100.0
For Department 2:
 - Student 2: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
 - Student 8: percentage = (1 - 1) * 100 / (2 - 1) = 0.0


*/


Create table Students (student_id int, department_id int, mark int)
Truncate table Students
insert into Students (student_id, department_id, mark) values ('2', '2', '650')
insert into Students (student_id, department_id, mark) values ('8', '2', '650')
insert into Students (student_id, department_id, mark) values ('7', '1', '920')
insert into Students (student_id, department_id, mark) values ('1', '1', '610')
insert into Students (student_id, department_id, mark) values ('3', '1', '530')




-- solution using cross apply

/* Write your T-SQL query statement below */
select 
student_id
, department_id
, percentage = cast(case when t2.cnt = 0 then 0 else 100.0*t.cnt/t2.cnt end as decimal(5,2)) --0.00 to 100.00, total should be 5 digits
from Students s1
cross apply (select cnt = count(*) from Students s2 where s2.department_id = s1.department_id and s2.mark > s1.mark) t -- how many people with marks > current student
cross apply (select cnt = count(*)-1 from Students s3 where s3.department_id = s1.department_id) t2 -- how mnay students in the same department - 1



-- solution using internal function 
/* Write your T-SQL query statement below */
select 
student_id
, department_id
, percentage = round(100.00 * percent_rank() over(partition by department_id order by mark desc),2)
from students


