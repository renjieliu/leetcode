/*
3554. Find Category Recommendation Pairs

+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) is the unique identifier for this table. 
Each row represents a purchase of a product by a user in a specific quantity.
Table: ProductInfo

+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the unique identifier for this table.
Each row assigns a category and price to a product.
Amazon wants to understand shopping patterns across product categories. Write a solution to:

Find all category pairs (where category1 < category2)
For each category pair, determine the number of unique customers who purchased products from both categories
A category pair is considered reportable if at least 3 different customers have purchased products from both categories.

Return the result table of reportable category pairs ordered by customer_count in descending order, and in case of a tie, by category1 in ascending order lexicographically, and then by category2 in ascending order.

The result format is in the following example.

 

Example:

Input:

ProductPurchases table:

+---------+------------+----------+
| user_id | product_id | quantity |
+---------+------------+----------+
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 201        | 3        |
| 1       | 301        | 1        |
| 2       | 101        | 1        |
| 2       | 102        | 2        |
| 2       | 103        | 1        |
| 2       | 201        | 5        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 301        | 4        |
| 3       | 401        | 2        |
| 4       | 101        | 1        |
| 4       | 201        | 3        |
| 4       | 301        | 1        |
| 4       | 401        | 2        |
| 5       | 102        | 2        |
| 5       | 103        | 1        |
| 5       | 201        | 2        |
| 5       | 202        | 3        |
+---------+------------+----------+
ProductInfo table:

+------------+-------------+-------+
| product_id | category    | price |
+------------+-------------+-------+
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Books       | 35    |
| 201        | Clothing    | 45    |
| 202        | Clothing    | 60    |
| 301        | Sports      | 75    |
| 401        | Kitchen     | 50    |
+------------+-------------+-------+
Output:

+-------------+-------------+----------------+
| category1   | category2   | customer_count |
+-------------+-------------+----------------+
| Books       | Clothing    | 3              |
| Books       | Electronics | 3              |
| Clothing    | Electronics | 3              |
| Electronics | Sports      | 3              |
+-------------+-------------+----------------+
Explanation:

Books-Clothing:
User 1 purchased products from Books (102) and Clothing (201)
User 2 purchased products from Books (102, 103) and Clothing (201)
User 5 purchased products from Books (102, 103) and Clothing (201, 202)
Total: 3 customers purchased from both categories
Books-Electronics:
User 1 purchased products from Books (102) and Electronics (101)
User 2 purchased products from Books (102, 103) and Electronics (101)
User 3 purchased products from Books (103) and Electronics (101)
Total: 3 customers purchased from both categories
Clothing-Electronics:
User 1 purchased products from Clothing (201) and Electronics (101)
User 2 purchased products from Clothing (201) and Electronics (101)
User 4 purchased products from Clothing (201) and Electronics (101)
Total: 3 customers purchased from both categories
Electronics-Sports:
User 1 purchased products from Electronics (101) and Sports (301)
User 3 purchased products from Electronics (101) and Sports (301)
User 4 purchased products from Electronics (101) and Sports (301)
Total: 3 customers purchased from both categories
Other category pairs like Clothing-Sports (only 2 customers: Users 1 and 4) and Books-Kitchen (only 1 customer: User 3) have fewer than 3 shared customers and are not included in the result.
The result is ordered by customer_count in descending order. Since all pairs have the same customer_count of 3, they are ordered by category1 (then category2) in ascending order.

*/


CREATE TABLE   ProductPurchases (
    user_id INT,
    product_id INT,
    quantity INT
)

CREATE TABLE  ProductInfo (
    product_id INT,
    category VARCHAR(100),
    price DECIMAL(10, 2)
)

Truncate table ProductPurchases
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '101', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '102', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '201', '3')
insert into ProductPurchases (user_id, product_id, quantity) values ('1', '301', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '101', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '102', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '103', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('2', '201', '5')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '101', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '103', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '301', '4')
insert into ProductPurchases (user_id, product_id, quantity) values ('3', '401', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '101', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '201', '3')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '301', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('4', '401', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('5', '102', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('5', '103', '1')
insert into ProductPurchases (user_id, product_id, quantity) values ('5', '201', '2')
insert into ProductPurchases (user_id, product_id, quantity) values ('5', '202', '3')
Truncate table ProductInfo
insert into ProductInfo (product_id, category, price) values ('101', 'Electronics', '100')
insert into ProductInfo (product_id, category, price) values ('102', 'Books', '20')
insert into ProductInfo (product_id, category, price) values ('103', 'Books', '35')
insert into ProductInfo (product_id, category, price) values ('201', 'Clothing', '45')
insert into ProductInfo (product_id, category, price) values ('202', 'Clothing', '60')
insert into ProductInfo (product_id, category, price) values ('301', 'Sports', '75')
insert into ProductInfo (product_id, category, price) values ('401', 'Kitchen', '50')


/* Write your T-SQL query statement below */
; with pair as -- to find all the possible pairs
(select 
p1 = p1.product_id
, p2 = p2.product_id 
, category1 = p1.category
, category2 = p2.category
from ProductInfo p1 
inner join ProductInfo p2 on p1.category < p2.category
)
select 
pair.category1
, pair.category2
, customer_count = count(distinct pp1.user_id)
 from pair 
inner join ProductPurchases pp1 on pair.p1 = pp1.product_id 
inner join ProductPurchases pp2 on pair.p2 = pp2.product_id and pp2.user_id = pp1.user_id
group by 
pair.category1
, pair.category2
having count(distinct pp1.user_id) >= 3 
order by 3 desc, 1, 2 

