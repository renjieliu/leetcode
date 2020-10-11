/*
1454. Active Users

Table Accounts:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
the id is the primary key for this table.
This table contains the account id and the user name of each account.
 

Table Logins:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| login_date    | date    |
+---------------+---------+
There is no primary key for this table, it may contain duplicates.
This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.
 

Write an SQL query to find the id and the name of active users.

Active users are those who logged in to their accounts for 5 or more consecutive days.

Return the result table ordered by the id.

The query result format is in the following example:

Accounts table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Winston  |
| 7  | Jonathan |
+----+----------+

Logins table:
+----+------------+
| id | login_date |
+----+------------+
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
+----+------------+

Result table:
+----+----------+
| id | name     |
+----+----------+
| 7  | Jonathan |
+----+----------+
User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.
Follow up question: Can you write a general solution if the active users are those who logged in to their accounts for n or more consecutive days?




*/


Create table Accounts (id int, name varchar(10))
Create table Logins (id int, login_date date)
Truncate table Accounts
insert into Accounts (id, name) values ('1', 'Winston')
insert into Accounts (id, name) values ('7', 'Jonathan')
Truncate table Logins
insert into Logins (id, login_date) values ('7', '2020-05-30')
insert into Logins (id, login_date) values ('1', '2020-05-30')
insert into Logins (id, login_date) values ('7', '2020-05-31')
insert into Logins (id, login_date) values ('7', '2020-06-01')
insert into Logins (id, login_date) values ('7', '2020-06-02')
insert into Logins (id, login_date) values ('7', '2020-06-02')
insert into Logins (id, login_date) values ('7', '2020-06-03')
insert into Logins (id, login_date) values ('1', '2020-06-07')
insert into Logins (id, login_date) values ('7', '2020-06-10')


/* Write your T-SQL query statement below */
with cte as 
(select id, days = 1, login_date from Logins 
 union all
 select l.id, c.days+1, l.login_date from cte c 
 inner join Logins l 
 on c.id = l.id and dateadd(day, 1, c.login_date) = l.login_date
)
select * from Accounts
where id in
(select id from cte where days = 5)
order by 1












