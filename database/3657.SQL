/*
3657. Find Loyal Customers


Table: customer_transactions

+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| transaction_id   | int     |
| customer_id      | int     |
| transaction_date | date    |
| amount           | decimal |
| transaction_type | varchar |
+------------------+---------+
transaction_id is the unique identifier for this table.
transaction_type can be either 'purchase' or 'refund'.
Write a solution to find loyal customers. A customer is considered loyal if they meet ALL the following criteria:

Made at least 3 purchase transactions.
Have been active for at least 30 days.
Their refund rate is less than 20% .
Refund rate is the proportion of transactions that are refunds, calculated as the number of refund transactions divided by the total number of transactions (purchases plus refunds).

Return the result table ordered by customer_id in ascending order.

The result format is in the following example.

 

Example:

Input:

customer_transactions table:

+----------------+-------------+------------------+--------+------------------+
| transaction_id | customer_id | transaction_date | amount | transaction_type |
+----------------+-------------+------------------+--------+------------------+
| 1              | 101         | 2024-01-05       | 150.00 | purchase         |
| 2              | 101         | 2024-01-15       | 200.00 | purchase         |
| 3              | 101         | 2024-02-10       | 180.00 | purchase         |
| 4              | 101         | 2024-02-20       | 250.00 | purchase         |
| 5              | 102         | 2024-01-10       | 100.00 | purchase         |
| 6              | 102         | 2024-01-12       | 120.00 | purchase         |
| 7              | 102         | 2024-01-15       | 80.00  | refund           |
| 8              | 102         | 2024-01-18       | 90.00  | refund           |
| 9              | 102         | 2024-02-15       | 130.00 | purchase         |
| 10             | 103         | 2024-01-01       | 500.00 | purchase         |
| 11             | 103         | 2024-01-02       | 450.00 | purchase         |
| 12             | 103         | 2024-01-03       | 400.00 | purchase         |
| 13             | 104         | 2024-01-01       | 200.00 | purchase         |
| 14             | 104         | 2024-02-01       | 250.00 | purchase         |
| 15             | 104         | 2024-02-15       | 300.00 | purchase         |
| 16             | 104         | 2024-03-01       | 350.00 | purchase         |
| 17             | 104         | 2024-03-10       | 280.00 | purchase         |
| 18             | 104         | 2024-03-15       | 100.00 | refund           |
+----------------+-------------+------------------+--------+------------------+
Output:

+-------------+
| customer_id |
+-------------+
| 101         |
| 104         |
+-------------+
Explanation:

Customer 101:
Purchase transactions: 4 (IDs: 1, 2, 3, 4) 
Refund transactions: 0
Refund rate: 0/4 = 0% (less than 20%) 
Active period: Jan 5 to Feb 20 = 46 days (at least 30 days) 
Qualifies as loyal 
Customer 102:
Purchase transactions: 3 (IDs: 5, 6, 9) 
Refund transactions: 2 (IDs: 7, 8)
Refund rate: 2/5 = 40% (exceeds 20%) 
Not loyal 
Customer 103:
Purchase transactions: 3 (IDs: 10, 11, 12) 
Refund transactions: 0
Refund rate: 0/3 = 0% (less than 20%) 
Active period: Jan 1 to Jan 3 = 2 days (less than 30 days) 
Not loyal 
Customer 104:
Purchase transactions: 5 (IDs: 13, 14, 15, 16, 17) 
Refund transactions: 1 (ID: 18)
Refund rate: 1/6 = 16.67% (less than 20%) 
Active period: Jan 1 to Mar 15 = 73 days (at least 30 days) 
Qualifies as loyal 
The result table is ordered by customer_id in ascending order.


*/




CREATE TABLE  customer_transactions (
    transaction_id INT,
    customer_id INT,
    transaction_date DATE,
    amount DECIMAL(10,2),
    transaction_type VARCHAR(20)
)
Truncate table customer_transactions
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('1', '101', '2024-01-05', '150.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('2', '101', '2024-01-15', '200.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('3', '101', '2024-02-10', '180.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('4', '101', '2024-02-20', '250.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('5', '102', '2024-01-10', '100.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('6', '102', '2024-01-12', '120.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('7', '102', '2024-01-15', '80.0', 'refund')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('8', '102', '2024-01-18', '90.0', 'refund')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('9', '102', '2024-02-15', '130.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('10', '103', '2024-01-01', '500.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('11', '103', '2024-01-02', '450.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('12', '103', '2024-01-03', '400.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('13', '104', '2024-01-01', '200.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('14', '104', '2024-02-01', '250.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('15', '104', '2024-02-15', '300.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('16', '104', '2024-03-01', '350.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('17', '104', '2024-03-10', '280.0', 'purchase')
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type) values ('18', '104', '2024-03-15', '100.0', 'refund')


/* Write your T-SQL query statement below */
; with base as 
(
    select 
    *,  
    active_days = datediff(day
                            , first_value(transaction_date) over (partition by customer_id order by transaction_date rows between unbounded preceding and unbounded following)
                            , last_value(transaction_date) over (partition by customer_id order by transaction_date rows between unbounded preceding and unbounded following)
                            )
    from customer_transactions
)

, cte as 
(
    select 
    customer_id
    , active_days
    , purchase_cnt = sum(case when transaction_type = 'purchase' then 1 else 0 end)
    , refund_cnt = sum(case when transaction_type = 'refund' then 1 else 0 end)
    from base
    group by customer_id, active_days
)
select 
customer_id
from cte 
where active_days >= 30 
and purchase_cnt >= 3
and refund_cnt *1.0 / (refund_cnt + purchase_cnt) < 0.2
order by customer_id 




