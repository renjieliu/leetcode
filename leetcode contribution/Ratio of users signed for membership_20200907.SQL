/*
Question Title:
Percentage of users signed for membership.

Reason:
The question is asked during a inteview with a leading online retailer, it could be asked frequently.


Description:
Find the percentage of users signed for members for each movie trailer.

Given the user table, return the percentage of users signed for membership after watching the trailer, round to 2 decimal points.

Order the result by percentage descendingly, if there's a tie, sort the TrailerID ascendingly.


Tables:

Users: 

UserID (int). The ID of user
TrailerID (int), The ID of the movie trailer
Signed (Int): It has 2 values, 0 or 1, which indicates if the user signed for membership after watching the movie trailer. 0 for not signed, 1 for signed.

 
For Example - 

Users table

UserID      TrailerID   Signed
----------- ----------- -----------
1           1           1
2           1           0
2           2           1
4           2           0
5           2           1
6           3           0
7           1           1
8           1           1



Result:

TrailerID   SignedPercentage
----------- ----------------
1           75.00
2           66.67
3           0.00



Explanation:

For Trailer 1, there are 4 users watched it, and 3 of them signed for membership, so the signing percentage is 3/4 = 75.00%
For Trailer 2, there are 3 users watched it, and 2 of them signed for membership, so the signing percentage is 2/3 = 66.67%
For Trailer 3, there are 1 users watched it, the user did not sign for the membership, so the signing percentage is 0/1 = 0.00%





Solutions:

with TrailerList as
(select distinct TrailerID from users)
select
T.TrailerID,
SignedPercentage = cast( 100.0*count(distinct u.UserID) 
						 / 
					    (select count(distinct u2.UserID) from users u2 where u2.TrailerID = T.TrailerID)
				       as decimal(10,2)
					   )
from 
TrailerList T
left outer join users u on t.TrailerID = u.TrailerID and u.Signed = 1 
group by T.TrailerID,u.TrailerID
order by 2 desc, 1 


Thoughts - 

Step 1: Get all the trailers in the user table
Step 2: Count distinct users watched the trailer
Step 3: Count distinct users signed for the membership
Step 4: Calculate the signing percentage for each trailer.
Step 5: Sort the result set as required.



Test Cases:

create table users (UserID int, TrailerID int, Signed int)

insert into users values(1,1,1)
insert into users values(2,1,0)
insert into users values(2,2,1)
insert into users values(4,2,0)
insert into users values(5,2,1)
insert into users values(6,3,0)
insert into users values(7,1,1)
insert into users values(8,1,1)


Users Table:

UserID      TrailerID   Signed
----------- ----------- -----------
1           1           1
2           1           0
2           2           1
4           2           0
5           2           1
6           3           0
7           1           1
8           1           1



Result:

TrailerID   SignedPercentage
----------- -----------------
1           75.00
2           66.67
3           0.00



*/


create table users (UserID int, TrailerID int, Signed int)

insert into users values(1,1,1)
insert into users values(2,1,0)
insert into users values(2,2,1)
insert into users values(4,2,0)
insert into users values(5,2,1)
insert into users values(6,3,0)
insert into users values(7,1,1)
insert into users values(8,1,1)


select * from users

; with TrailerList as
(select distinct TrailerID from users)
select
T.TrailerID,
SignedPercentage = cast( 100.0*count(distinct u.UserID) 
						 / 
					    (select count(distinct u2.UserID) from users u2 where u2.TrailerID = T.TrailerID)
				       as decimal(10,2)
					   )
from 
TrailerList T
left outer join users u on t.TrailerID = u.TrailerID and u.Signed = 1 
group by T.TrailerID,u.TrailerID
order by 2 desc, 1 











--select * from Student
--select * from Exam 
