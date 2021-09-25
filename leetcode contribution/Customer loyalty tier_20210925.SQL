/*
Question Title:
Customer loyalty tier

Reason:
The question was asked by a consumer product company, headquatered in upstate New York. I think this kind of question should be very common for retailing companies.

Description:

There're 3 tiers of our memberships. Diamond, Gold and Silver. They are determined by the conversion rate of the member. 

Conversion Rate is defined as - 

100.0 * Times_of_purchase / Total_visits_of_the_member

If the ratio is between 80 to 100, the member is considered Diamond tier.
If the ratio is between 50 to 79, the member is considered Gold tier.
If the ratio is between 0 to 49, the member is considered Silver tier.

Given 3 tables as below, generate a report to show the tier of each member. Sort the report by the member Id

Table:
 
Members:  (Id) is the primary key of the table
 - member_id (int): Id of the Member.
 - name (varchar(10)): Name of the member

Visits: (visit_id) is the primary key of the table.
 - visit_id (int): The Id of the visit, foreign key of the Purchase table
 - member_id (int): Id of the member
 - visit_date (date): The date of member visit
 - visit_location (varchar(20)): The store which the member visited
 
Purchase: (visit_id) is the primary key of the table.
 - visit_id (int): The Id of the visit.
 - charged_amount (int): Total amount charged on the bill, this will always be a positve number.


For Example - 

Members table

member_id   name
----------- -------
1           Eddie
2           Jones
3           Mike
4           Ted


Visits table

visit_id    member_id   visit_date visit_location
----------- ----------- ---------- ---------------
1           1           2021-01-01 New York
2           1           2021-01-02 New York
3           3           2021-01-03 Chicago
4           3           2021-01-02 Boston
5           3           2021-01-05 Boston
6           4           2021-01-09 New York


Purchase table

visit_id    charged_amount
----------- --------------
1           200
3           500
4           20
6           100


Result

member_id   name       tier
----------- ---------- -------
1           Eddie      Gold
2           Jones      Silver
3           Mike       Gold
4           Ted        Diamond



Explanation:

For member 1, Eddie, visited store 2 times, as visit_id 1 and 2. and made 1 purchase with visit_id = 1. The conversion rate is 100.0*1/2 = 50.0, therefore, Eddie is a Gold Tier member
For member 2, Jones, visited store 0 times, made no purchase. Therefore, Jones is a silver tier member.
For member 3, Mike, visited store 3 times, as visit_id 3,4 and 5, and made 2 purchases with visit_id = 3 and 4. The conversion rate is 100.0*2/3 = 66.67, therefore, Mike is a Gold Tier member
For member 4, Ted, visited store 1 time, as visit_id 6, and made 1 purchases with that visit. The conversion rate is 100.0*1/1 = 100.00, therefore, Ted is a Diamond Tier member




Solutions:

select 
m.member_id
,m.name
,tier = case when count(distinct v.visit_id) = 0 then 'Silver'
			 when 100.0*count(distinct p.visit_id) / count(distinct v.visit_id) between 80 and 100  then 'Diamond'
			 when 100.0*count(distinct p.visit_id) / count(distinct v.visit_id) between 50 and 79 then 'Gold'
			 else 'Silver'
		end
from Members m 
left outer join Visits v 
on m.member_id = v.member_id
left outer join Purchase p
on v.visit_id = p.visit_id
group by m.member_id, m.name
order by m.member_id


Thoughts - 

Step 1: Join the 3 tables together.
Step 2: Find the count of visits for each member
Step 3: Find the count of purchase for each member
Step 4: Calculate the ratio and generate the tier per requirement.


Test Cases:


create table Members (member_id int, name varchar(10))

create table Visits (visit_id int, member_id int, visit_date date, visit_location varchar(20))

create table Purchase(visit_id int, charged_amount int)

insert into Members values (1, 'Eddie'), (2, 'Jones'), (3, 'Mike'), (4, 'Ted')

insert into Visits values  
(1, 1, '2021-01-01', 'New York')
,(2, 1, '2021-01-02', 'New York')
,(3, 3, '2021-01-03', 'Chicago')
,(4, 3, '2021-01-02', 'Boston')
,(5, 3, '2021-01-05', 'Boston')
,(6, 4, '2021-01-09', 'New York')

insert into Purchase values (1, 200), (3, 500), (4, 20), (6, 100)

 
select 
m.member_id
,m.name
,tier = case when count(distinct v.visit_id) = 0 then 'Silver'
			 when 100.0*count(distinct p.visit_id) / count(distinct v.visit_id) between 80 and 100  then 'Diamond'
			 when 100.0*count(distinct p.visit_id) / count(distinct v.visit_id) between 50 and 79 then 'Gold'
			 else 'Silver'
		end
from Members m 
left outer join Visits v 
on m.member_id = v.member_id
left outer join Purchase p
on v.visit_id = p.visit_id
group by m.member_id, m.name
order by m.member_id


*/




























