/*
2004. The Number of Seniors and Juniors to Join the Company


Table: Candidates

+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| experience  | enum |
| salary      | int  |
+-------------+------+
employee_id is the primary key column for this table.
experience is an enum with one of the values ('Senior', 'Junior').
Each row of this table indicates the id of a candidate, their monthly salary, and their experience.
 

A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

Hiring the largest number of seniors.
After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 20000  |
| 11          | Senior     | 20000  |
| 13          | Senior     | 50000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
Output: 
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 2                   |
| Junior     | 2                   |
+------------+---------------------+
Explanation: 
We can hire 2 seniors with IDs (2, 11). Since the budget is $70000 and the sum of their salaries is $40000, we still have $30000 but they are not enough to hire the senior candidate with ID 13.
We can hire 2 juniors with IDs (1, 9). Since the remaining budget is $30000 and the sum of their salaries is $20000, we still have $10000 but they are not enough to hire the junior candidate with ID 4.
Example 2:

Input: 
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 80000  |
| 11          | Senior     | 80000  |
| 13          | Senior     | 80000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
Output: 
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 0                   |
| Junior     | 3                   |
+------------+---------------------+
Explanation: 
We cannot hire any seniors with the current budget as we need at least $80000 to hire one senior.
We can hire all the three juniors with the remaining budget.


*/

Create table Candidates (employee_id int, experience ENUM('Senior', 'Junior'), salary int)
Truncate table Candidates
insert into Candidates (employee_id, experience, salary) values ('1', 'Junior', '10000')
insert into Candidates (employee_id, experience, salary) values ('9', 'Junior', '10000')
insert into Candidates (employee_id, experience, salary) values ('2', 'Senior', '20000')
insert into Candidates (employee_id, experience, salary) values ('11', 'Senior', '20000')
insert into Candidates (employee_id, experience, salary) values ('13', 'Senior', '50000')
insert into Candidates (employee_id, experience, salary) values ('4', 'Junior', '40000')



/* Write your T-SQL query statement below */
with sn as ( -- get the senior list
    select 
    employee_id
    ,runningSum = sum(salary) over(order by salary)
    from Candidates
    where experience = 'Senior' 
)
, jn as -- get the junior list
(
    select 
    employee_id
    ,runningSum = sum(salary) over(order by salary)
    from Candidates
    where experience = 'Junior' 
)
, staging as ( -- get the senior to hire and the junior to hire
    select employee_id, exp = 'Senior' from sn 
    where runningSum <=70000 
    union all 
    select employee_id, 'Junior' from jn
    where runningSum <= isnull(70000 - (select max(runningSum) from sn where runningSum <=70000), 70000)
)
select -- generate the final report
lkp.experience 
,accepted_candidates = isnull(count(staging.employee_id),0)
from (values('Junior'), ('Senior')) lkp(experience)
left outer join staging on lkp.experience = staging.exp
group by lkp.experience
order by 1 desc 
























































