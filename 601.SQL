select * from stadium where id in (
    select id from stadium s1 where 
    people >= 100 and 
    exists (select * from stadium s2 where s2.people >= 100 and s2.id = s1.id - 1)
    and exists (
            select * from stadium s3 where s3.people >= 100 and s3.id = s1.id + 1)
    )
or 
id +1 in (
    select id from stadium s1 where 
    people >= 100 and 
    exists (select * from stadium s2 where s2.people >= 100 and s2.id = s1.id - 1)
    and exists (
            select * from stadium s3 where s3.people >= 100 and s3.id = s1.id + 1)
    )
or id-1 in (
    select id from stadium s1 where 
    people >= 100 and 
    exists (select * from stadium s2 where s2.people >= 100 and s2.id = s1.id - 1)
    and exists (
            select * from stadium s3 where s3.people >= 100 and s3.id = s1.id + 1)
    )