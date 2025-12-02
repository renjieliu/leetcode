/*

Table: students

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| student_name | varchar |
| major        | varchar |
+--------------+---------+
student_id is the unique identifier for this table.
Each row contains information about a student and their academic major.
Table: study_sessions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| session_id    | int     |
| student_id    | int     |
| subject       | varchar |
| session_date  | date    |
| hours_studied | decimal |
+---------------+---------+
session_id is the unique identifier for this table.
Each row represents a study session by a student for a specific subject.
Write a solution to find students who follow the Study Spiral Pattern - students who consistently study multiple subjects in a rotating cycle.

A Study Spiral Pattern means a student studies at least 3 different subjects in a repeating sequence
The pattern must repeat for at least 2 complete cycles (minimum 6 study sessions)
Sessions must be consecutive dates with no gaps longer than 2 days between sessions
Calculate the cycle length (number of different subjects in the pattern)
Calculate the total study hours across all sessions in the pattern
Only include students with cycle length of at least 3 subjects
Return the result table ordered by cycle length in descending order, then by total study hours in descending order.

The result format is in the following example.

 

Example:

Input:

students table:

+------------+--------------+------------------+
| student_id | student_name | major            |
+------------+--------------+------------------+
| 1          | Alice Chen   | Computer Science |
| 2          | Bob Johnson  | Mathematics      |
| 3          | Carol Davis  | Physics          |
| 4          | David Wilson | Chemistry        |
| 5          | Emma Brown   | Biology          |
+------------+--------------+------------------+
study_sessions table:

+------------+------------+------------+--------------+---------------+
| session_id | student_id | subject    | session_date | hours_studied |
+------------+------------+------------+--------------+---------------+
| 1          | 1          | Math       | 2023-10-01   | 2.5           |
| 2          | 1          | Physics    | 2023-10-02   | 3.0           |
| 3          | 1          | Chemistry  | 2023-10-03   | 2.0           |
| 4          | 1          | Math       | 2023-10-04   | 2.5           |
| 5          | 1          | Physics    | 2023-10-05   | 3.0           |
| 6          | 1          | Chemistry  | 2023-10-06   | 2.0           |
| 7          | 2          | Algebra    | 2023-10-01   | 4.0           |
| 8          | 2          | Calculus   | 2023-10-02   | 3.5           |
| 9          | 2          | Statistics | 2023-10-03   | 2.5           |
| 10         | 2          | Geometry   | 2023-10-04   | 3.0           |
| 11         | 2          | Algebra    | 2023-10-05   | 4.0           |
| 12         | 2          | Calculus   | 2023-10-06   | 3.5           |
| 13         | 2          | Statistics | 2023-10-07   | 2.5           |
| 14         | 2          | Geometry   | 2023-10-08   | 3.0           |
| 15         | 3          | Biology    | 2023-10-01   | 2.0           |
| 16         | 3          | Chemistry  | 2023-10-02   | 2.5           |
| 17         | 3          | Biology    | 2023-10-03   | 2.0           |
| 18         | 3          | Chemistry  | 2023-10-04   | 2.5           |
| 19         | 4          | Organic    | 2023-10-01   | 3.0           |
| 20         | 4          | Physical   | 2023-10-05   | 2.5           |
+------------+------------+------------+--------------+---------------+
Output:

+------------+--------------+------------------+--------------+-------------------+
| student_id | student_name | major            | cycle_length | total_study_hours |
+------------+--------------+------------------+--------------+-------------------+
| 2          | Bob Johnson  | Mathematics      | 4            | 26.0              |
| 1          | Alice Chen   | Computer Science | 3            | 15.0              |
+------------+--------------+------------------+--------------+-------------------+
Explanation:

Alice Chen (student_id = 1):
Study sequence: Math → Physics → Chemistry → Math → Physics → Chemistry
Pattern: 3 subjects (Math, Physics, Chemistry) repeating for 2 complete cycles
Consecutive dates: Oct 1-6 with no gaps > 2 days
Cycle length: 3 subjects
Total hours: 2.5 + 3.0 + 2.0 + 2.5 + 3.0 + 2.0 = 15.0 hours
Bob Johnson (student_id = 2):
Study sequence: Algebra → Calculus → Statistics → Geometry → Algebra → Calculus → Statistics → Geometry
Pattern: 4 subjects (Algebra, Calculus, Statistics, Geometry) repeating for 2 complete cycles
Consecutive dates: Oct 1-8 with no gaps > 2 days
Cycle length: 4 subjects
Total hours: 4.0 + 3.5 + 2.5 + 3.0 + 4.0 + 3.5 + 2.5 + 3.0 = 26.0 hours
Students not included:
Carol Davis (student_id = 3): Only 2 subjects (Biology, Chemistry) - doesn't meet minimum 3 subjects requirement
David Wilson (student_id = 4): Only 2 study sessions with a 4-day gap - doesn't meet consecutive dates requirement
Emma Brown (student_id = 5): No study sessions recorded
The result table is ordered by cycle_length in descending order, then by total_study_hours in descending order.





*/


 CREATE TABLE  students (
    student_id INT,
    student_name VARCHAR(255),
    major VARCHAR(100)
)


CREATE TABLE study_sessions (
    session_id INT,
    student_id INT,
    subject VARCHAR(100),
    session_date DATE,
    hours_studied DECIMAL(4, 2)
)

Truncate table students

insert into students (student_id, student_name, major) values ('1', 'Alice Chen', 'Computer Science')
insert into students (student_id, student_name, major) values ('2', 'Bob Johnson', 'Mathematics')
insert into students (student_id, student_name, major) values ('3', 'Carol Davis', 'Physics')
insert into students (student_id, student_name, major) values ('4', 'David Wilson', 'Chemistry')
insert into students (student_id, student_name, major) values ('5', 'Emma Brown', 'Biology')
Truncate table study_sessions

--insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('1', '1', 'English', '2023-09-30', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('1', '1', 'Math', '2023-10-01', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('2', '1', 'Physics', '2023-10-01', '3.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('3', '1', 'Chemistry', '2023-10-01', '2.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('4', '1', 'Math', '2023-10-02', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('5', '1', 'Physics', '2023-10-02', '3.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('6', '1', 'Chemistry', '2023-10-02', '2.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('7', '2', 'Algebra', '2023-10-01', '4.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('8', '2', 'Calculus', '2023-10-02', '3.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('9', '2', 'Statistics', '2023-10-03', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('10', '2', 'Geometry', '2023-10-04', '3.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('11', '2', 'Algebra', '2023-10-05', '4.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('12', '2', 'Calculus', '2023-10-06', '3.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('13', '2', 'Statistics', '2023-10-07', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('14', '2', 'Geometry', '2023-10-08', '3.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('15', '3', 'Biology', '2023-10-01', '2.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('16', '3', 'Chemistry', '2023-10-02', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('17', '3', 'Biology', '2023-10-03', '2.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('18', '3', 'Chemistry', '2023-10-04', '2.5')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('19', '3', 'Organic', '2023-10-01', '3.0')
insert into study_sessions (session_id, student_id, subject, session_date, hours_studied) values ('20', '3', 'Physical', '2023-10-05', '2.5')

go 


-- select * from study_sessions 

; with base as 
(
    select rn = ROW_NUMBER() over(partition by student_id order by session_date, subject)
         ,  *
    from study_sessions

)
, cte as (
select
rn
, student_id
, subject
, session_date
, cycle_Start = session_date
, courses = cast(subject as varchar(max))
, course_cnt = 1 
from base 
union all 

select
b.rn 
, b.student_id 
, b.subject 
, b.session_date
, cycle_Start
, cast(courses+ ',' + b.subject as varchar(max))
, course_cnt + 1
from cte c inner join base b 
on c.student_id = b.student_id and b.rn = c.rn + 1 and DATEDIFF(day, c.session_date, b.session_date) <= 2
where charindex(b.subject, c.courses) = 0 
), staging1 as 
(
select 
c1.student_id
, c1.courses
, c1.course_cnt
, c1.cycle_Start
, c1.session_date
, session_cnt = count(*) over (partition by student_id, courses) from cte c1
where not exists (select * from cte c2 where c2.student_id = c1.student_id and c2.course_cnt > c1.course_cnt)
and c1.course_cnt >= 3
), staging2 as 
(
select *
, nxt_session_starts_in_2_days = iif( 2 >= DATEDIFF(day, session_date, lead(cycle_start, 1) over (partition by student_id, courses order by cycle_Start))  , 1, 0)
from staging1
where session_cnt  > 1
) 

select 
distinct
c1.student_id
, student_name = s.student_name
, s.major
, cycle_length = c1.course_cnt
, total_study_hours = (select sum(hours_studied) from study_sessions ss where ss.student_id = s.student_id)
from staging2 c1 inner join students s on c1.student_id = s.student_id
where c1.nxt_session_starts_in_2_days = 1
order by c1.course_cnt desc , total_study_hours desc 




