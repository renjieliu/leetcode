select Id from Weather w1 
where exists (select * from Weather w2 where w2.Temperature < w1.Temperature and w2.RecordDate = dateadd (day,  - 1 , w1.RecordDate))