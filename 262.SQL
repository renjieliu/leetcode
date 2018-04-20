select 
Day = dts.Request_at
, [Cancellation Rate] = case when count(status) = 0 then 0.00
							 else 
							 cast(round (sum(case when Status like 'cancell%' then 1.0 else 0.0 end )/count(status),2)  as numeric(36,2))
							end
 from 
(select distinct Request_at from  Trips) dts
left outer join 
(select * from Trips 
where Client_Id not in (select Users_Id from Users where Banned = 'Yes' and Role = 'client')
) c 
on dts. Request_at = c.Request_at 
where dts.Request_at between '2013-10-01' and '2013-10-03' 
group by dts.Request_at
