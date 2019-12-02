/*

Table: Spending

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| spend_date  | date    |
| platform    | enum    | 
| amount      | int     |
+-------------+---------+
The table logs the spendings history of users that make purchases from an online shopping website which has a desktop and a mobile application.
(user_id, spend_date, platform) is the primary key of this table.
The platform column is an ENUM type of ('desktop', 'mobile').
Write an SQL query to find the total number of users and the total amount spent using mobile only, desktop only and both mobile and desktop together for each date.

The query result format is in the following example:

Spending table:
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+

Result table:
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+ 
On 2019-07-01, user 1 purchased using both desktop and mobile, user 2 purchased using mobile only and user 3 purchased using desktop only.
On 2019-07-02, user 2 purchased using mobile only, user 3 purchased using desktop only and no one purchased using both platforms.


*/


Create table Spending (user_id int, spend_date date, platform varchar(max), amount int)
Truncate table Spending
insert into Spending (user_id, spend_date, platform, amount) values ('1', '2019-07-01', 'mobile', '100')
insert into Spending (user_id, spend_date, platform, amount) values ('1', '2019-07-01', 'desktop', '100')
insert into Spending (user_id, spend_date, platform, amount) values ('1', '2019-07-01', 'desktop', '200')
insert into Spending (user_id, spend_date, platform, amount) values ('2', '2019-07-01', 'mobile', '100')
insert into Spending (user_id, spend_date, platform, amount) values ('2', '2019-07-02', 'mobile', '100')
insert into Spending (user_id, spend_date, platform, amount) values ('3', '2019-07-01', 'desktop', '100')
insert into Spending (user_id, spend_date, platform, amount) values ('3', '2019-07-02', 'desktop', '100')


;
with md_date as  --master data for all the possible dates
(select distinct spend_date  from Spending)
,md_platform as --master data for all the possible combination of dates and platform
(select distinct platform, md.spend_date from Spending, md_date md)
,one as  --users with only one platform 
(
select spend_date, user_id --, total_amount = sum(amount), total_users = count(distinct user_id)
from Spending 
group by spend_date, user_id
having count(distinct platform) = 1
)
,both as -- users with both platforms
(
select spend_date, user_id -- total_amount = sum(amount), total_users = count(distinct user_id)
from Spending 
group by spend_date, user_id
having count(distinct platform) = 2
),
combined as (
select md.spend_date 
, md.platform
, total_amount = isnull( sum(Spending.amount),0)
, total_users =  isnull( count(distinct Spending.user_id ) ,0)
from 
one inner join Spending on Spending.user_id = one.user_id and Spending.spend_date = one.spend_date
right outer join md_platform md on md.platform = Spending.platform and md.spend_date = Spending.spend_date
group by 
md.spend_date 
,md.platform 

union all

select dates.spend_date
, platform = 'both'
, total_amount = isnull( sum(Spending.amount),0)
, total_users = isnull( count(distinct Spending.user_id ) ,0)
from Spending 
inner join both on Spending.user_id = both.user_id and Spending.spend_date = both.spend_date
right outer join  md_date dates on dates.spend_date = Spending.spend_date
group by dates.spend_date
)
select * from combined 
order by spend_date, case when platform = 'both' then 'zzz' else platform end 






