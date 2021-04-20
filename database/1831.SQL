/*
1831. Maximum Transaction Each Day

Table: Transactions

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| transaction_id | int      |
| day            | datetime |
| amount         | int      |
+----------------+----------+
transaction_id is the primary key for this table.
Each row contains information about one transaction.
 

Write an SQL query to report the IDs of the transactions with the maximum amount on their respective day. If in one day there are multiple such transactions, return all of them.

Return the result table in ascending order by transaction_id.

The query result format is in the following example:

 

Transactions table:
+----------------+--------------------+--------+
| transaction_id | day                | amount |
+----------------+--------------------+--------+
| 8              | 2021-4-3 15:57:28  | 57     |
| 9              | 2021-4-28 08:47:25 | 21     |
| 1              | 2021-4-29 13:28:30 | 58     |
| 5              | 2021-4-28 16:39:59 | 40     |
| 6              | 2021-4-29 23:39:28 | 58     |
+----------------+--------------------+--------+

Result table:
+----------------+
| transaction_id |
+----------------+
| 1              |
| 5              |
| 6              |
| 8              |
+----------------+
"2021-4-3"  --> We have one transaction with ID 8, so we add 8 to the result table.
"2021-4-28" --> We have two transactions with IDs 5 and 9. The transaction with ID 5 has an amount of 40, while the transaction with ID 9 has an amount of 21. We only include the transaction with ID 5 as it has the maximum amount this day.
"2021-4-29" --> We have two transactions with IDs 1 and 6. Both transactions have the same amount of 58, so we include both in the result table.
We order the result table by transaction_id after collecting these IDs.
 

Follow up: Could you solve it without using the MAX() function?



*/

Create table Transactions (transaction_id int, day datetime, amount int)
Truncate table Transactions
insert into Transactions (transaction_id, day, amount) values ('8', '2021-4-3 15:57:28', '57')
insert into Transactions (transaction_id, day, amount) values ('9', '2021-4-28 08:47:25', '21')
insert into Transactions (transaction_id, day, amount) values ('1', '2021-4-29 13:28:30', '58')
insert into Transactions (transaction_id, day, amount) values ('5', '2021-4-28 16:39:59', '40')
insert into Transactions (transaction_id, day, amount) values ('6', '2021-4-29 23:39:28', '58')

/* Write your T-SQL query statement below */
select transaction_id from Transactions t1
where not exists (select * from Transactions t2 where cast(t1.day as date) = cast(t2.day as date) and t2.amount > t1.amount)
order by 1 


































