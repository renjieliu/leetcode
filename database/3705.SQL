/*
3705. Find Golden Hour Customers


Table: restaurant_orders

+------------------+----------+
| Column Name      | Type     | 
+------------------+----------+
| order_id         | int      |
| customer_id      | int      |
| order_timestamp  | datetime |
| order_amount     | decimal  |
| payment_method   | varchar  |
| order_rating     | int      |
+------------------+----------+
order_id is the unique identifier for this table.
payment_method can be cash, card, or app.
order_rating is between 1 and 5, where 5 is the best (NULL if not rated).
order_timestamp contains both date and time information.
Write a solution to find golden hour customers - customers who consistently order during peak hours and provide high satisfaction. A customer is a golden hour customer if they meet ALL the following criteria:

Made at least 3 orders.
At least 60% of their orders are during peak hours (11:00-14:00 or 18:00-21:00).
Their average rating for rated orders is at least 4.0, round it to 2 decimal places.
Have rated at least 50% of their orders.
Return the result table ordered by average_rating in descending order, then by customer_id​​​​​​​ in descending order.

The result format is in the following example.

 

Example:

Input:

restaurant_orders table:

+----------+-------------+---------------------+--------------+----------------+--------------+
| order_id | customer_id | order_timestamp     | order_amount | payment_method | order_rating |
+----------+-------------+---------------------+--------------+----------------+--------------+
| 1        | 101         | 2024-03-01 12:30:00 | 25.50        | card           | 5            |
| 2        | 101         | 2024-03-02 19:15:00 | 32.00        | app            | 4            |
| 3        | 101         | 2024-03-03 13:45:00 | 28.75        | card           | 5            |
| 4        | 101         | 2024-03-04 20:30:00 | 41.00        | app            | NULL         |
| 5        | 102         | 2024-03-01 11:30:00 | 18.50        | cash           | 4            |
| 6        | 102         | 2024-03-02 12:00:00 | 22.00        | card           | 3            |
| 7        | 102         | 2024-03-03 15:30:00 | 19.75        | cash           | NULL         |
| 8        | 103         | 2024-03-01 19:00:00 | 55.00        | app            | 5            |
| 9        | 103         | 2024-03-02 20:45:00 | 48.50        | app            | 4            |
| 10       | 103         | 2024-03-03 18:30:00 | 62.00        | card           | 5            |
| 11       | 104         | 2024-03-01 10:00:00 | 15.00        | cash           | 3            |
| 12       | 104         | 2024-03-02 09:30:00 | 18.00        | cash           | 2            |
| 13       | 104         | 2024-03-03 16:00:00 | 20.00        | card           | 3            |
| 14       | 105         | 2024-03-01 12:15:00 | 30.00        | app            | 4            |
| 15       | 105         | 2024-03-02 13:00:00 | 35.50        | app            | 5            |
| 16       | 105         | 2024-03-03 11:45:00 | 28.00        | card           | 4            |
+----------+-------------+---------------------+--------------+----------------+--------------+
Output:

+-------------+--------------+----------------------+----------------+
| customer_id | total_orders | peak_hour_percentage | average_rating |
+-------------+--------------+----------------------+----------------+
| 103         | 3            | 100                  | 4.67           |
| 101         | 4            | 100                  | 4.67           |
| 105         | 3            | 100                  | 4.33           |
+-------------+--------------+----------------------+----------------+
Explanation:

Customer 101:
Total orders: 4 (at least 3) 
Peak hour orders: 4 out of 4 (12:30, 19:15, 13:45, and 20:30 are in peak hours)
Peak hour percentage: 100% (at least 60%) 
Rated orders: 3 out of 4 (75% rating completion) 
Average rating: (5+4+5)/3 = 4.67 (at least 4.0) 
Result: Golden hour customer
Customer 102:
Total orders: 3 (at least 3) 
Peak hour orders: 2 out of 3 (11:30, 12:00 are in peak hours; 15:30 is not)
Peak hour percentage: 2/3 = 66.67% (at least 60%) 
Rated orders: 2 out of 3 (66.67% rating completion) 
Average rating: (4+3)/2 = 3.5 (less than 4.0) 
Result: Not a golden hour customer (average rating too low)
Customer 103:
Total orders: 3 (at least 3) 
Peak hour orders: 3 out of 3 (19:00, 20:45, 18:30 all in evening peak)
Peak hour percentage: 3/3 = 100% (at least 60%) 
Rated orders: 3 out of 3 (100% rating completion) 
Average rating: (5+4+5)/3 = 4.67 (at least 4.0) 
Result: Golden hour customer
Customer 104:
Total orders: 3 (at least 3) 
Peak hour orders: 0 out of 3 (10:00, 09:30, 16:00 all outside peak hours)
Peak hour percentage: 0/3 = 0% (less than 60%) 
Result: Not a golden hour customer (insufficient peak hour orders)
Customer 105:
Total orders: 3 (at least 3) 
Peak hour orders: 3 out of 3 (12:15, 13:00, 11:45 all in lunch peak)
Peak hour percentage: 3/3 = 100% (at least 60%) 
Rated orders: 3 out of 3 (100% rating completion) 
Average rating: (4+5+4)/3 = 4.33 (at least 4.0) 
Result: Golden hour customer
The results table is ordered by average_rating DESC, then customer_id DESC.

*/

CREATE TABLE restaurant_orders (
    order_id INT,
    customer_id INT,
    order_timestamp DATETIME,
    order_amount DECIMAL(10,2),
    payment_method VARCHAR(10),
    order_rating INT
)
Truncate table restaurant_orders
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('1', '101', '2024-03-01 12:30:00', '25.5', 'card', '5')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('2', '101', '2024-03-02 19:15:00', '32.0', 'app', '4')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('3', '101', '2024-03-03 13:45:00', '28.75', 'card', '5')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('4', '101', '2024-03-04 20:30:00', '41.0', 'app', NULL)
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('5', '102', '2024-03-01 11:30:00', '18.5', 'cash', '4')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('6', '102', '2024-03-02 12:00:00', '22.0', 'card', '3')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('7', '102', '2024-03-03 15:30:00', '19.75', 'cash', NULL)
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('8', '103', '2024-03-01 19:00:00', '55.0', 'app', '5')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('9', '103', '2024-03-02 20:45:00', '48.5', 'app', '4')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('10', '103', '2024-03-03 18:30:00', '62.0', 'card', '5')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('11', '104', '2024-03-01 10:00:00', '15.0', 'cash', '3')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('12', '104', '2024-03-02 09:30:00', '18.0', 'cash', '2')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('13', '104', '2024-03-03 16:00:00', '20.0', 'card', '3')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('14', '105', '2024-03-01 12:15:00', '30.0', 'app', '4')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('15', '105', '2024-03-02 13:00:00', '35.5', 'app', '5')
insert into restaurant_orders (order_id, customer_id, order_timestamp, order_amount, payment_method, order_rating) values ('16', '105', '2024-03-03 11:45:00', '28.0', 'card', '4')



/* Write your T-SQL query statement below */
; with base as 
(
    select 
    customer_id
    , order_cnt = count(order_id)
    , peak_order_cnt = count(case when datepart(hour, order_timestamp) between 11 and 13 or datepart(hour, order_timestamp) between 18 and 20 then 1 else NULL end )
    , avg_rating = cast(avg(order_rating*1.0) as decimal(5, 2))
    , rated_cnt = count(order_rating)
    from restaurant_orders
    group by customer_id
)

select 
customer_id
, total_orders = order_cnt
, peak_hour_percentage = cast(100.0*peak_order_cnt / nullif(order_cnt, 0)  as decimal(38, 0))
, average_rating = avg_rating
from base 
where order_cnt >= 3
and cast(100.0*peak_order_cnt / nullif(order_cnt, 0)  as decimal(38, 1)) >= 60.0
and avg_rating >= 4.0
and rated_cnt*1.0 / order_cnt >= 0.50
order by average_rating desc , customer_id desc


