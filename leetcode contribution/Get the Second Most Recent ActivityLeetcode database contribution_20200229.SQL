Question Title
Get the Second Most Recent Activity

Reason
My friend received this question when interviewing at Microsoft. And we believe this is a very common question for interview. 


Description
We have an UserActivity table with below columns - 

UserName: Name of the user
Activity: The name of the Activity
StartDate: The StartDate of the Activity
EndDate: The endDate of the Activity
Your task is to generate a report to show the second most recent activity of each user.

If the user only has one activity, return that one.

 

For Example - 

UserActivity Table

UserName       Activity    StartDate  EndDate
-------------- ----------- ---------- ----------
Mike           Travel      2020-01-01 2020-01-08
Mike           Training    2020-02-01 2020-02-08
Mike           Travel      2020-02-09 2020-02-09
Jim            Travel      2016-01-01 2016-01-08
 

Result:

UserName    Activity     StartDate  EndDate
----------- ------------ ---------- ----------
Mike        Training     2020-02-01 2020-02-08
Jim         Travel       2016-01-01 2016-01-08

 

Explanation 

Mike has 3 activities, the most recent one is Travel, start on 2020-02-09 and end on 2020-02-09, the one before that is the one we want -  

Training, start on 2020-02-01 and end on 2020-02-08.

Jim only has one record, and we just take that one.

 
 
The idea is to take the 2nd recent record from the ones with more than 2 records, union the ones with only one record

select UserName,Activity,StartDate,EndDate
from 
(select *, rn = ROW_NUMBER() over(partition by UserName order by StartDate desc) from UserActivity u1) T 
where rn = 2 

union 

select UserName,Activity,StartDate,EndDate
from UserActivity u1 
where UserName in (
					select UserName from UserActivity 
					group by UserName
					having count(StartDate) = 1
				   )
	and 
	not exists(select * from UserActivity u2 where u1.UserName = u2.UserName and u1.StartDate > u2.StartDate)
 
 
Input:

create table UserActivity (
UserName varchar(20),
Activity varchar(20),
StartDate date,
EndDate date)

truncate table UserActivity

insert into UserActivity select 'Mike', 'Travel', '2020-01-01', '2020-01-08'
insert into UserActivity select 'Mike', 'Training', '2020-02-01', '2020-02-08'
insert into UserActivity select 'Mike', 'Travel', '2020-02-09', '2020-02-09'
insert into UserActivity select 'Jim', 'Travel', '2016-01-01', '2016-01-08'
 
Output:

UserName             Activity             StartDate  EndDate
-------------------- -------------------- ---------- ----------
Jim                  Travel               2016-01-01 2016-01-08
Mike                 Training             2020-02-01 2020-02-08







 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
