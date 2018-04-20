select distinct ConsecutiveNums = Num from Logs l1
where exists (select * from logs l2 where l1.Num  = l2.Num and l2.id = l1.id + 1 and exists
	(select * from Logs l3 where l3.Num = l2.Num and l3.Id = l2.Id + 1 )
 )