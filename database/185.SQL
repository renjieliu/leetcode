with a as (
select Employee= e.name, Salary, Department = d.Name, rnk = dense_rank() over(partition by d.name order by salary desc )  from Employee e inner join Department d
on e.DepartmentId = d.Id
) 
select Department, Employee, Salary  from a 
where rnk <=3