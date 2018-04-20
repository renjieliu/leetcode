select Employee = e.Name  from Employee e inner join Employee m 
on e.ManagerId = m.Id
where isnull(e.Salary, 0)> isnull(m.Salary, 0)