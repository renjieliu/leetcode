/* Write your T-SQL query statement below */
with r as 
(select 2 rnk), 
base as (
select rnk  = dense_rank() over(order by salary desc), * from Employee
)
select distinct SecondHighestSalary = base.Salary from
r left outer join base on r.rnk = base.rnk