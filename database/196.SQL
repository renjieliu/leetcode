delete t1 
from Person t1 inner join (select Email, min(Id) as K from Person group by Email ) t2
on t1.Email =  t2.Email
where t1.Id <> t2.K