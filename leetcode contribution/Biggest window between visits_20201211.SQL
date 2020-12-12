/*
Question Title:
Biggest window between visits

Reason:
The question was asked by a leading retailer. I think reflects real business scenario, and it would help other candidates to prepare.

Description:

Assuming today's date is Dec-1, 2020, find the largest window between each visit for each customer in the visits table

Order the result by userid.


Table:

visits: 

userID (int). The ID of user
visit_date (date). Date when the user visit the store


For Example - 

visits table

userid      visit_date
----------- ----------
1           2017-01-01
1           2017-01-08
1           2019-01-01
2           2016-01-01
2           2019-07-05
3           2015-01-01


Result:

userid      window
----------- -----------
1           723
2           1281
3           2161





Explanation:

For userid 1, there are 3 visits. The first visit window is 7 days (from 2017-01-01 to 2017-01-08), the second window is 723 days (from 2017-01-08 to 2019-01-01), and last window is 700 days (from 2019-01-01 to today, 2020-12-01). Therfore we return 723 for user1 
For userid 2, there are 2 visits. The first visit window is 1281 days (from 2016-01-01 to 2019-07-05), the second window is 515 days (from 2020-07-05 to 2020-12-01). Therfore we return 1281 for user2
For userid 3, there is only 1 visit. As the user has not visited since 2015-01-01, and today is Dec-1, 2020, there're 2161 days in between. Therfore we return 2161 for user3


Solutions:

with filled_dates as (
	select userid, visit_date from visits
	union all 
	select distinct userid, today.d 
	from visits cross join (select d = cast('2020-12-01' as date) ) today
)
, seq as(
	select 
	userid
	,visit_date
	,visit_seq = ROW_NUMBER() over(partition by userid order by visit_date)
	from filled_dates
)
, ans as (
select
c1.userid
,window = datediff(day, c1.visit_date, isnull(c2.visit_date, c1.visit_date))
from seq c1 left outer join seq c2 
on c1.userid = c2.userid and c2.visit_seq = c1.visit_seq + 1
)
select * from ans a
where not exists(select * from ans a2 where a2.userid = a.userid and a2.window > a.window)
order by a.userid


Thoughts - 

Step 1: Assuming the user is visiting the store today (2020-12-01), and plug the visit to the visits table
Step 2: Get the sequence number for each visit,
Step 3: Count the difference from each visit - this is the "window" in question. 
Step 4: Get the largest window for each user
Step 5: Sort the result set as required.



Test Cases:

create table visits (userid int, visit_date date) 

insert into visits values(1, '2019-01-01')
insert into visits values(1, '2017-01-01')
insert into visits values(1, '2017-01-08')
insert into visits values(2, '2016-01-01')
insert into visits values(2, '2019-07-05')
insert into visits values(3, '2015-01-01')


visits Table:

userid      visit_date
----------- ----------
1           2019-01-01
1           2017-01-01
1           2017-01-08
2           2016-01-01
2           2019-07-05
3           2015-01-01


Result:

userid      window
----------- -----------
1           723
2           1281
3           2161



*/



create table visits (userid int, visit_date date) 

insert into visits values(1, '2019-01-01')
insert into visits values(1, '2017-01-01')
insert into visits values(1, '2017-01-08')
insert into visits values(2, '2016-01-01')
insert into visits values(2, '2019-07-05')
insert into visits values(3, '2015-01-01')


select * from visits

;
with filled_dates as (
	select userid, visit_date from visits
	union all 
	select distinct userid, today.d 
	from visits cross join (select d = cast('2020-12-01' as date) ) today
)
, seq as(
	select 
	userid
	,visit_date
	,visit_seq = ROW_NUMBER() over(partition by userid order by visit_date)
	from filled_dates
)
, ans as (
select
c1.userid
,window = datediff(day, c1.visit_date, isnull(c2.visit_date, c1.visit_date))
from seq c1 left outer join seq c2 
on c1.userid = c2.userid and c2.visit_seq = c1.visit_seq + 1
)
select * from ans a
where not exists(select * from ans a2 where a2.userid = a.userid and a2.window > a.window)
order by a.userid





select datediff(day, '2016-01-01', '2019-07-05')

select datediff(day, '2019-07-05', '2020-12-01')





























