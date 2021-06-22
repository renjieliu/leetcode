/*
1907. Count Salary Categories


Table: Accounts

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key for this table.
Each row contains information about the monthly income for one bank account.
 

Write an SQL query to report the number of bank accounts of each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, then report 0. Return the result table in any order.

The query result format is in the following example.

 

Accounts table:
+------------+------------+
| account_id | max_income |
+------------+------------+
| 3          | 108939     |
| 2          | 12747      |
| 8          | 87709      |
| 6          | 91796      |
+------------+------------+

Result table:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+

Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.


*/

Create table Accounts (account_id int, income int)
Truncate table Accounts
insert into Accounts (account_id, income) values ('3', '108939')
insert into Accounts (account_id, income) values ('2', '12747')
insert into Accounts (account_id, income) values ('8', '87709')
insert into Accounts (account_id, income) values ('6', '91796')


--MySQL
-- # Write your MySQL query statement below
with cte as
(
select 'Low Salary'category
union all 
select 'Average Salary'
union all 
select 'High Salary'
)
select
cte.category
, coalesce(count(a.account_id),0) accounts_count
from cte left outer join accounts a 
on cte.category = case when a.income < 20000 then 'Low Salary'
                       when a.income <= 50000 then 'Average Salary'
                       when a.income > 50000 then 'High Salary'
                  end 
group by cte.category



--MSSQL - TLE as of 2021-06-22

/* Write your T-SQL query statement below */
with cte as
(
select 'Low Salary'category
union all 
select 'Average Salary'
union all 
select 'High Salary'
)
select
cte.category
, coalesce(count(a.account_id),0) accounts_count
from cte left outer join accounts a 
on cte.category = case when a.income < 20000 then 'Low Salary'
                       when a.income <= 50000 then 'Average Salary'
                       when a.income > 50000 then 'High Salary'
                  end 
group by cte.category


--Oracle

/* Write your PL/SQL query statement below */
with cte as
(
select 'Low Salary'category from dual
union all 
select 'Average Salary' from dual
union all 
select 'High Salary' from dual
)
select
cte.category
, coalesce(count(a.account_id),0) accounts_count
from cte left outer join accounts a 
on cte.category = case when a.income < 20000 then 'Low Salary'
                       when a.income <= 50000 then 'Average Salary'
                       when a.income > 50000 then 'High Salary'
                  end 
group by cte.category





































