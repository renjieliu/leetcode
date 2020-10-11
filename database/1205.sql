/*
Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
Table: Chargebacks

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| trans_id       | int     |
| charge_date    | date    |
+----------------+---------+
Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
trans_id is a foreign key to the id column of Transactions table.
Each chargeback corresponds to a transaction made previously even if they were not approved.
 

Write an SQL query to find for each month and country, the number of approved transactions and their total amount, the number of chargebacks and their total amount.

Note: In your query, given the month and country, ignore rows with all zeros.

The query result format is in the following example:

Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 101  | US      | approved | 1000   | 2019-05-18 |
| 102  | US      | declined | 2000   | 2019-05-19 |
| 103  | US      | approved | 3000   | 2019-06-10 |
| 104  | US      | approved | 4000   | 2019-06-13 |
| 105  | US      | approved | 5000   | 2019-06-15 |
+------+---------+----------+--------+------------+

Chargebacks table:
+------------+------------+
| trans_id   | trans_date |
+------------+------------+
| 102        | 2019-05-29 |
| 101        | 2019-06-30 |
| 105        | 2019-09-18 |
+------------+------------+

Result table:
+----------+---------+----------------+-----------------+-------------------+--------------------+
| month    | country | approved_count | approved_amount | chargeback_count  | chargeback_amount  |
+----------+---------+----------------+-----------------+-------------------+--------------------+
| 2019-05  | US      | 1              | 1000            | 1                 | 2000               |
| 2019-06  | US      | 3              | 12000           | 1                 | 1000               |
| 2019-09  | US      | 0              | 0               | 1                 | 5000               |
+----------+---------+----------------+-----------------+-------------------+--------------------+

*/


create table Transactions (id int, country varchar(4), state varchar(max), amount int, trans_date date)
create table Chargebacks (trans_id int, trans_date date)
Truncate table Transactions
insert into Transactions (id, country, state, amount, trans_date) values ('101', 'US', 'approved', '1000', '2019-05-18')
insert into Transactions (id, country, state, amount, trans_date) values ('102', 'US', 'declined', '2000', '2019-05-19')
insert into Transactions (id, country, state, amount, trans_date) values ('103', 'US', 'approved', '3000', '2019-06-10')
insert into Transactions (id, country, state, amount, trans_date) values ('104', 'US', 'declined', '4000', '2019-06-13')
insert into Transactions (id, country, state, amount, trans_date) values ('105', 'US', 'approved', '5000', '2019-06-15')
Truncate table Chargebacks
insert into Chargebacks (trans_id, trans_date) values ('102', '2019-05-29')
insert into Chargebacks (trans_id, trans_date) values ('101', '2019-06-30')
insert into Chargebacks (trans_id, trans_date) values ('105', '2019-09-18')

select * from Transactions

select * from Chargebacks 




;with cb_base  as 
(select  c_id = c1.trans_id , c_country = t1.country, c_date = c1.trans_date, c_amount = t1.amount from  Chargebacks c1 inner join Transactions t1 on c1.trans_id = t1.id)
, approved as (
select 
month = format(t.trans_date, 'yyyy-MM')
,t.country
,approved_count = sum(case when t.state = 'approved' then 1 else 0 end) 
,approved_amount = sum(case when t.state = 'approved' then amount  else 0 end)
,chargeback_count = 0
,chargeback_amount = 0
from Transactions t 
group by format(t.trans_date, 'yyyy-MM') , country   
) 
,cb as (
select 
month = format(cb_base.c_date, 'yyyy-MM')
,c_country
,approved_count = 0
,approved_amount = 0
,chargeback_count = count(*)
,chargeback_amount = sum(cb_base.c_amount)
from cb_base
group by format(c_date, 'yyyy-MM') , c_country 
)
select 
month, 
country, 
approved_count = sum(approved_count),
approved_amount = sum(approved_amount),
chargeback_count = sum(chargeback_count),
chargeback_amount = sum(chargeback_amount)
from(
	select * from approved 
	union all 
	select * from cb
) t 
group by month, country
having sum(approved_count) >0 or  sum(approved_amount)> 0 or sum(chargeback_count) > 0 or sum(chargeback_amount) > 0
