/*
1623. All Valid Triplets That Can Represent a Country

Table: SchoolA

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key for this table.
Each row of this table contains the name and the id of a student in school A.
All student_name are distinct.
 

Table: SchoolB

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key for this table.
Each row of this table contains the name and the id of a student in school B.
All student_name are distinct.
 

Table: SchoolC

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key for this table.
Each row of this table contains the name and the id of a student in school C.
All student_name are distinct.
 

There is a country with three schools, where each student is enrolled in exactly one school. The country is joining a competition and wants to select one student from each school to represent the country such that:

member_A is selected from SchoolA,
member_B is selected from SchoolB,
member_C is selected from SchoolC, and
The selected students' names and IDs are pairwise distinct (i.e. no two students share the same name, and no two students share the same ID).
Write an SQL query to find all the possible triplets representing the country under the given constraints.

Return the result table in any order.

The query result format is in the following example.

 

SchoolA table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
+------------+--------------+

SchoolB table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 3          | Tom          |
+------------+--------------+

SchoolC table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 3          | Tom          |
| 2          | Jerry        |
| 10         | Alice        |
+------------+--------------+

Result table:
+----------+----------+----------+
| member_A | member_B | member_C |
+----------+----------+----------+
| Alice    | Tom      | Jerry    |
| Bob      | Tom      | Alice    |
+----------+----------+----------+
Let us see all the possible triplets.
- (Alice, Tom, Tom) --> Rejected because member_B and member_C have the same name and the same ID.
- (Alice, Tom, Jerry) --> Valid triplet.
- (Alice, Tom, Alice) --> Rejected because member_A and member_C have the same name.
- (Bob, Tom, Tom) --> Rejected because member_B and member_C have the same name and the same ID.
- (Bob, Tom, Jerry) --> Rejected because member_A and member_C have the same ID.
- (Bob, Tom, Alice) --> Valid triplet.


*/


Create table SchoolA (student_id int, student_name varchar(20))
Create table SchoolB (student_id int, student_name varchar(20))
Create table SchoolC (student_id int, student_name varchar(20))
Truncate table SchoolA
insert into SchoolA (student_id, student_name) values ('1', 'Alice')
insert into SchoolA (student_id, student_name) values ('2', 'Bob')
Truncate table SchoolB
insert into SchoolB (student_id, student_name) values ('3', 'Tom')
Truncate table SchoolC
insert into SchoolC (student_id, student_name) values ('3', 'Tom')
insert into SchoolC (student_id, student_name) values ('2', 'Jerry')
insert into SchoolC (student_id, student_name) values ('10', 'Alice')



/* Write your T-SQL query statement below */
select distinct
member_A = A.student_name
,member_B=B.student_name
,member_C=c.student_name 
from 
SchoolA A, SchoolB B, SchoolC C
where A.student_name != B.student_name 
and B.student_name != C.student_name
and A.student_name != C.student_name
and A.student_Id != B.student_Id 
and A.student_id != C.student_Id 
and B.student_Id != C.student_Id












