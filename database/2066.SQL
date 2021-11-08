/* 2066. Account Balance

Table: Transactions

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| day         | date |
| type        | ENUM |
| amount      | int  |
+-------------+------+
(account_id, day) is the primary key for this table.
Each row contains information about one transaction including the transaction type and the amount.
type is ENUM of the type ('Deposit','Withdraw') 
 

Write an SQL query to report the balance of each user after each transaction. You may assume that the balance of each account before any transaction is 0 and you may assume that the balance will not be below 0 at any moment.

Return the result table ordered by account_id and day in ascending order.

The query result format is in the following example.

 

Example 1:

Input: 
Transactions table:
+------------+------------+----------+--------+
| account_id | day        | type     | amount |
+------------+------------+----------+--------+
| 1          | 2021-11-07 | Deposit  | 2000   |
| 1          | 2021-11-09 | Withdraw | 1000   |
| 1          | 2021-11-11 | Deposit  | 3000   |
| 2          | 2021-12-07 | Deposit  | 7000   |
| 2          | 2021-12-12 | Withdraw | 7000   |
+------------+------------+----------+--------+
Output: 
+------------+------------+---------+
| account_id | day        | balance |
+------------+------------+---------+
| 1          | 2021-11-07 | 2000    |
| 1          | 2021-11-09 | 1000    |
| 1          | 2021-11-11 | 4000    |
| 2          | 2021-12-07 | 7000    |
| 2          | 2021-12-12 | 0       |
+------------+------------+---------+
Explanation: 
User 1:
- Initial balance is 0.
- 2021-11-07 --> deposit of 2000. Balance is 2000.
- 2021-11-09 --> withdraw of 1000. Balance is 1000.
- 2021-11-11 --> deposit of 3000. Balance is 4000.
User 2:
- Initial balance is 0.
- 2021-12-07 --> deposit of 7000. Balance is 7000.
- 2021-12-12 --> withdraw of 7000. Balance is 0.


*/


Create table Transactions (account_id int, day date, type ENUM('Deposit', 'Withdraw'), amount int)
Truncate table Transactions
insert into Transactions (account_id, day, type, amount) values ('1', '2021-11-07', 'Deposit', '2000')
insert into Transactions (account_id, day, type, amount) values ('1', '2021-11-09', 'Withdraw', '1000')
insert into Transactions (account_id, day, type, amount) values ('1', '2021-11-11', 'Deposit', '3000')
insert into Transactions (account_id, day, type, amount) values ('2', '2021-12-07', 'Deposit', '7000')
insert into Transactions (account_id, day, type, amount) values ('2', '2021-12-12', 'Withdraw', '7000')


/* Write your T-SQL query statement below */
with base as 
(select 
 account_id
 , day
 , amount = case when type = 'Withdraw' then -amount else amount end 
 from Transactions
)
select
account_id
,day
--,balance = isnull((select sum(amount) from base b1 where b1.account_id = b.account_id and b1.day <= b.day), 0)
,balance = isnull(sum(amount) over(partition by account_id order by day rows between unbounded preceding and current row),0)
from base b
order by account_id, day


