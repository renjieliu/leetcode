select 
case 
when mod((select count(*) from seat), 2) <> 0 and id +1 not in (select id from seat) then id 
when mod(id,2)=1 then id+1 
when mod(id,2)<>1 then id -1 
end as id, student from seat
order by 1