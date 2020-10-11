/*

Table: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
Table: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id is the auto-increment primary key,
CandidateId is the id appeared in Candidate table.
Write a sql to find the name of the winning candidate, the above example will return the winner B.

+------+
| Name |
+------+
| B    |
+------+
Notes:

You may assume there is no tie, in other words there will be at most one winning candidate.
 

*/



Create table  Candidate (id int, Name varchar(255))
Create table  Vote (id int, CandidateId int)
Truncate table Candidate
insert into Candidate (id, Name) values ('1', 'A')
insert into Candidate (id, Name) values ('2', 'B')
insert into Candidate (id, Name) values ('3', 'C')
insert into Candidate (id, Name) values ('4', 'D')
insert into Candidate (id, Name) values ('5', 'E')
Truncate table Vote
insert into Vote (id, CandidateId) values ('1', '2')
insert into Vote (id, CandidateId) values ('2', '4')
insert into Vote (id, CandidateId) values ('3', '3')
insert into Vote (id, CandidateId) values ('4', '2')
insert into Vote (id, CandidateId) values ('5', '5')


with temp as
(select distinct c.Name, 
cnt = COUNT(v.id) over (partition by v.CandidateId)
from 
Candidate c right outer join Vote v  on c.id = v.CandidateId
)
select Name from temp t1
where not exists(select * from temp t2 where t2.cnt > t1.cnt )
and name is not null 













