select Customers = c.Name from  Customers c 
where not exists (select * from orders o  where o.CustomerId = c. id)
