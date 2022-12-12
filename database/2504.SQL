/*
2504. Concatenate the Name and the Profession

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| name        | varchar |
| profession  | ENUM    |
+-------------+---------+
person_id is the primary key for this table.
Each row in this table contains a person's ID, name, and profession.
The profession   column in an enum of the type ('Doctor', 'Singer', 'Actor', 'Player', 'Engineer', or 'Lawyer')
 

Write an SQL query to report each person's name followed by the first letter of their profession enclosed in parentheses.

Return the result table ordered by person_id in descending order.

The query result format is shown in the following example.

 

Example 1:

Input: 
Person table:
+-----------+-------+------------+
| person_id | name  | profession |
+-----------+-------+------------+
| 1         | Alex  | Singer     |
| 3         | Alice | Actor      |
| 2         | Bob   | Player     |
| 4         | Messi | Doctor     |
| 6         | Tyson | Engineer   |
| 5         | Meir  | Lawyer     |
+-----------+-------+------------+
Output: 
+-----------+----------+
| person_id | name     |
+-----------+----------+
| 6         | Tyson(E) |
| 5         | Meir(L)  |
| 4         | Messi(D) |
| 3         | Alice(A) |
| 2         | Bob(P)   |
| 1         | Alex(S)  |
+-----------+----------+
Explanation: Note that there should not be any white space between the name and the first letter of the profession.




*/

Create table Person (person_id int, name varchar(30), profession ENUM('Doctor','Singer','Actor','Player','Engineer','Lawyer'))
Truncate table Person
insert into Person (person_id, name, profession) values ('1', 'Alex', 'Singer')
insert into Person (person_id, name, profession) values ('3', 'Alice', 'Actor')
insert into Person (person_id, name, profession) values ('2', 'Bob', 'Player')
insert into Person (person_id, name, profession) values ('4', 'Messi', 'Doctor')
insert into Person (person_id, name, profession) values ('6', 'Tyson', 'Engineer')
insert into Person (person_id, name, profession) values ('5', 'Meir', 'Lawyer')



/* Write your T-SQL query statement below */
select 
person_id
, name = name + quotename(left(profession,1), '(')
from Person
order by person_id desc







