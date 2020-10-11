with a as 
(select cnt = count(id) over (partition by Email), * from Person) 
select distinct Email from a where cnt > 1 