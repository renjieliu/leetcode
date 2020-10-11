CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
	declare @SecondHighestSalary int
	;
	with r as 
	(select @N rnk), 
	base as (
	select rnk  = dense_rank() over(order by salary desc), * from Employee
	)
	select distinct @SecondHighestSalary = base.Salary from
	r left outer join base on r.rnk = base.rnk


    RETURN @SecondHighestSalary
END