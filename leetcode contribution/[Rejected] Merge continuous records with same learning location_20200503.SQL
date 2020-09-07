/*
Question Title:

Merge continuous records with same learning location


Reason:
The question is asked during a inteview for a Financial database related position. 
The question itself is easy to understand, but it took me some time to figure it out.
It needs knowledge of recursive CTE and aggregate functions.
I believe this has some real use in the project, and it can have many follow-up scenarios.


Description:
Students are allowed to take online courses from different places, as long as they report their location.

Our administrative team has compiled a table for the Student-Location information, but the table was not very well built. 

Your task is to reorgnize the table, make sure all the continuous records are merged, as long as the student is at the same location.

Order the result table by StudentID, and FromDate

Continuous records meaning there's no day gap between the 2 records.

student_location table - 

StudentID: ID of the student 
StudentName: Name of the student 
Location: Learning Location 
FromDate: The date when the student started learning at the location
ToDate: The date when the student stopped learning at the location
For Example - 

student_location Table:

StudentID   StudentName          Location   FromDate   ToDate
----------- -------------------- ---------- ---------- ----------
1           Tom                  Paris      2020-03-01 2020-03-07
1           Tom                  Paris      2020-03-08 2020-03-09
1           Tom                  New York   2020-03-10 2020-03-12
1           Tom                  New York   2020-03-13 2020-03-15
2           Betty                London     2020-03-01 2020-05-31
3           Steve                Rome       2020-02-13 2020-03-12
3           Steve                Rome       2020-03-13 2020-03-15
3           Steve                Rome       2020-03-16 2020-03-18
3           Steve                New York   2020-03-19 2020-03-21
3           Steve                Rome       2020-03-22 2020-03-23

3           Steve                Rome       2020-03-24 2020-04-23

 


Result Table:

StudentID   StudentName          Location   FromDate   ToDate
----------- -------------------- ---------- ---------- ----------
1           Tom                  Paris      2020-03-01 2020-03-09
1           Tom                  New York   2020-03-10 2020-03-15
2           Betty                London     2020-03-01 2020-05-31
3           Steve                Rome       2020-02-13 2020-03-18
3           Steve                New York   2020-03-19 2020-03-21
3           Steve                Rome       2020-03-22 2020-04-23
 

Explanation:

1. Tom was taking course in Paris from 2020-03-01 to 2020-03-07 and he was at still at Paris from next day, 2020-03-08 to 2020-03-09, therfore the records are merged
2. Betty only has one record, therefore, the same record is returned
3. Steve was taking the course in Rome, from 2020-02-13 to 2020-03-18 (merged from 3 records), and then he went to New York, stay there from 2020-03-19 to 2020-03-21, and back to Rome to take course from 2020-03-22 to 2020-04-23
 
 



Solutions:


with cte as 
(
	select root_start = FromDate,  StudentID, StudentName, Location, FromDate, ToDate from student_location
	union all
	select c.root_start, s.StudentID, s.StudentName, s.Location, s.FromDate, s.ToDate 
	from student_location s 
	inner join cte c on 
	s.StudentID = c.StudentID 
	and dateadd(day, 1, c.ToDate) = s.FromDate
	and c.Location = s.Location
)
, toDate as 
(
	select StudentID, StudentName, Location, FromDate = root_start, ToDate = max(ToDate)
	from cte 
	group by StudentID, StudentName, Location, root_start
)
select StudentID, StudentName, Location, FromDate = min(FromDate), ToDate
from toDate 
group by StudentID, StudentName, Location, ToDate
order by StudentID, FromDate, ToDate


Thoughts -  

1. Using recursive CTEs to get the continuous records.
2. With the help of root_start, there could be more than one ToDate for the period, I am using Max() to get the actual ToDate, for the period
3. Again, for the same ToDate, there might be more than one FromDate, using the Min() to get the actual FromDate of the period



Test Cases:


Input -

create table student_location
(

  StudentID int,
  StudentName  varchar(20),
  Location varchar(10),
  FromDate date,
  ToDate date
)

insert into student_location values(1, 'Tom','Paris', '2020-03-01', '2020-03-07')
insert into student_location values(1, 'Tom','Paris', '2020-03-08', '2020-03-09')
insert into student_location values(1, 'Tom','New York', '2020-03-10', '2020-03-12')
insert into student_location values(1, 'Tom','New York', '2020-03-13', '2020-03-15')
insert into student_location values(2, 'Betty','London', '2020-03-01', '2020-05-31')
insert into student_location values(3, 'Steve','Rome', '2020-02-13', '2020-03-12')
insert into student_location values(3, 'Steve','Rome', '2020-03-13', '2020-03-15')
insert into student_location values(3, 'Steve','Rome', '2020-03-16', '2020-03-18')
insert into student_location values(3, 'Steve','New York', '2020-03-19', '2020-03-21')
insert into student_location values(3, 'Steve','Rome', '2020-03-22', '2020-03-23')
insert into student_location values(3, 'Steve','Rome', '2020-03-24', '2020-04-23')



Output - 

StudentID   StudentName          Location   FromDate   ToDate
----------- -------------------- ---------- ---------- ----------
1           Tom                  Paris      2020-03-01 2020-03-09
1           Tom                  New York   2020-03-10 2020-03-15
2           Betty                London     2020-03-01 2020-05-31
3           Steve                Rome       2020-02-13 2020-03-18
3           Steve                New York   2020-03-19 2020-03-21
3           Steve                Rome       2020-03-22 2020-04-23



*/





