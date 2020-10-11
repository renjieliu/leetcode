/*
1336. Number of Transactions per Visit

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| visit_date    | date    |
+---------------+---------+
(user_id, visit_date) is the primary key for this table.
Each row of this table indicates that user_id has visited the bank in visit_date.
 

Table: Transactions

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| user_id          | int     |
| transaction_date | date    |
| amount           | int     |
+------------------+---------+
There is no primary key for this table, it may contain duplicates.
Each row of this table indicates that user_id has done a transaction of amount in transaction_date.
It is guaranteed that the user has visited the bank in the transaction_date.(i.e The Visits table contains (user_id, transaction_date) in one row)
 

Write an SQL query to find how many users visited the bank and didn't do any transactions, how many visited the bank and did one transaction and so on.

The result table will contain two columns transactions_count which is the number of transactions done in one visit and visits_count which is the corresponding number of users who did transactions_count in one visit to the bank. transactions_count should take all values from 0 to max(transactions_count) done by one or more users.

Order the result table by transactions_count.

The query result format is in the following example:

Visits table:
+---------+------------+
| user_id | visit_date |
+---------+------------+
| 1       | 2020-01-01 |
| 2       | 2020-01-02 |
| 12      | 2020-01-01 |
| 19      | 2020-01-03 |
| 1       | 2020-01-02 |
| 2       | 2020-01-03 |
| 1       | 2020-01-04 |
| 7       | 2020-01-11 |
| 9       | 2020-01-25 |
| 8       | 2020-01-28 |
+---------+------------+
Transactions table:
+---------+------------------+--------+
| user_id | transaction_date | amount |
+---------+------------------+--------+
| 1       | 2020-01-02       | 120    |
| 2       | 2020-01-03       | 22     |
| 7       | 2020-01-11       | 232    |
| 1       | 2020-01-04       | 7      |
| 9       | 2020-01-25       | 33     |
| 9       | 2020-01-25       | 66     |
| 8       | 2020-01-28       | 1      |
| 9       | 2020-01-25       | 99     |
+---------+------------------+--------+
Result table:
+--------------------+--------------+
| transactions_count | visits_count |
+--------------------+--------------+
| 0                  | 4            |
| 1                  | 5            |
| 2                  | 0            |
| 3                  | 1            |
+--------------------+--------------+
Users 1, 2, 12 and 19 visited the bank in 2020-01-01, 2020-01-02, 2020-01-01 and 2020-01-03 respectively, and didn't do any transactions.
So we have visits_count = 4 for transactions_count = 0.
Users 2, 7 and 8 visited the bank in 2020-01-03, 2020-01-11 and 2020-01-28 respectively, and did one transaction.
User 1 Also visited the bank in 2020-01-02 and 2020-01-04 and did one transaction each day.
So we have total visits_count = 5 for transactions_count = 1.
For transactions_count = 2 we don't have any users who visited the bank and did two transactions.
For transactions_count = 3 we have user 9 who visited the bank in 2020-01-25 and did three transactions.
Note that we stopped at transactions_count = 3 as this is the maximum number of transactions done by one user in one visit to the bank.

*/


Create table Visits (user_id int, visit_date date)
Create table Transactions (user_id int, transaction_date date, amount int)
Truncate table Visits
insert into Visits (user_id, visit_date) values ('1', '2020-01-01')
insert into Visits (user_id, visit_date) values ('2', '2020-01-02')
insert into Visits (user_id, visit_date) values ('12', '2020-01-01')
insert into Visits (user_id, visit_date) values ('19', '2020-01-03')
insert into Visits (user_id, visit_date) values ('1', '2020-01-02')
insert into Visits (user_id, visit_date) values ('2', '2020-01-03')
insert into Visits (user_id, visit_date) values ('1', '2020-01-04')
insert into Visits (user_id, visit_date) values ('7', '2020-01-11')
insert into Visits (user_id, visit_date) values ('9', '2020-01-25')
insert into Visits (user_id, visit_date) values ('8', '2020-01-28')
Truncate table Transactions
insert into Transactions (user_id, transaction_date, amount) values ('1', '2020-01-02', '120')
insert into Transactions (user_id, transaction_date, amount) values ('2', '2020-01-03', '22')
insert into Transactions (user_id, transaction_date, amount) values ('7', '2020-01-11', '232')
insert into Transactions (user_id, transaction_date, amount) values ('1', '2020-01-04', '7')
insert into Transactions (user_id, transaction_date, amount) values ('9', '2020-01-25', '33')
insert into Transactions (user_id, transaction_date, amount) values ('9', '2020-01-25', '66')
insert into Transactions (user_id, transaction_date, amount) values ('8', '2020-01-28', '1')
insert into Transactions (user_id, transaction_date, amount) values ('9', '2020-01-25', '99')

/* Write your T-SQL query statement below */
;with temp as ( -- how many visists in that day, and how many transactions
select 
	v.user_id
	,v.visit_date
	,visits_count = count(v.user_id)
	,transactions_count = isnull(sum(case when t.transaction_date is null then 0 else 1 end), 0)
from Visits v left outer join Transactions t
on v.visit_date = t.transaction_date and v.user_id = t.user_id
group by v.user_id, v.visit_date 
),
fill as --using recursive CTE to fill from 0 to max... 
(select id = 0, e = max(transactions_count) from temp
	union all
select id + 1 , e from fill
where id < e
) 
select 
transactions_count = f.id   --count how many 1 transaction, 2 transactions and so on..
,visits_count = isnull(count(visits_count),0)
from fill f 
left outer join temp t on f.id = t.transactions_count
group by f.id
order by 1

