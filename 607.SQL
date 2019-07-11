/*

Description

Given three tables: salesperson, company, orders.
Output all the names in the table salesperson, who didn’t have sales to company 'RED'.

Example
Input

Table: salesperson

+----------+------+--------+-----------------+-----------+
| sales_id | name | salary | commission_rate | hire_date |
+----------+------+--------+-----------------+-----------+
|   1      | John | 100000 |     6           | 4/1/2006  |
|   2      | Amy  | 120000 |     5           | 5/1/2010  |
|   3      | Mark | 65000  |     12          | 12/25/2008|
|   4      | Pam  | 25000  |     25          | 1/1/2005  |
|   5      | Alex | 50000  |     10          | 2/3/2007  |
+----------+------+--------+-----------------+-----------+
The table salesperson holds the salesperson information. Every salesperson has a sales_id and a name.
Table: company

+---------+--------+------------+
| com_id  |  name  |    city    |
+---------+--------+------------+
|   1     |  RED   |   Boston   |
|   2     | ORANGE |   New York |
|   3     | YELLOW |   Boston   |
|   4     | GREEN  |   Austin   |
+---------+--------+------------+
The table company holds the company information. Every company has a com_id and a name.
Table: orders

+----------+------------+---------+----------+--------+
| order_id | order_date | com_id  | sales_id | amount |
+----------+------------+---------+----------+--------+
| 1        |   1/1/2014 |    3    |    4     | 100000 |
| 2        |   2/1/2014 |    4    |    5     | 5000   |
| 3        |   3/1/2014 |    1    |    1     | 50000  |
| 4        |   4/1/2014 |    1    |    4     | 25000  |
+----------+----------+---------+----------+--------+
The table orders holds the sales record information, salesperson and customer company are represented by sales_id and com_id.
output

+------+
| name | 
+------+
| Amy  | 
| Mark | 
| Alex |
+------+
Explanation

According to order '3' and '4' in table orders, it is easy to tell only salesperson 'John' and 'Alex' have sales to company 'RED',
so we need to output all the other names in table salesperson.
*/



Create table salesperson (sales_id int, name varchar(255), salary int,commission_rate int, hire_date varchar(255))
Create table company (com_id int, name varchar(255), city varchar(255))
Create table orders (order_id int, order_date varchar(255), com_id int, sales_id int, amount int)
Truncate table salesperson
insert into salesperson (sales_id, name, salary, commission_rate, hire_date) values ('1', 'John', '100000', '6', '4/1/2006')
insert into salesperson (sales_id, name, salary, commission_rate, hire_date) values ('2', 'Amy', '12000', '5', '5/1/2010')
insert into salesperson (sales_id, name, salary, commission_rate, hire_date) values ('3', 'Mark', '65000', '12', '12/25/2008')
insert into salesperson (sales_id, name, salary, commission_rate, hire_date) values ('4', 'Pam', '25000', '25', '1/1/2005')
insert into salesperson (sales_id, name, salary, commission_rate, hire_date) values ('5', 'Alex', '5000', '10', '2/3/2007')
Truncate table company
insert into company (com_id, name, city) values ('1', 'RED', 'Boston')
insert into company (com_id, name, city) values ('2', 'ORANGE', 'New York')
insert into company (com_id, name, city) values ('3', 'YELLOW', 'Boston')
insert into company (com_id, name, city) values ('4', 'GREEN', 'Austin')
Truncate table orders
insert into orders (order_id, order_date, com_id, sales_id, amount) values ('1', '1/1/2014', '3', '4', '10000')
insert into orders (order_id, order_date, com_id, sales_id, amount) values ('2', '2/1/2014', '4', '5', '5000')
insert into orders (order_id, order_date, com_id, sales_id, amount) values ('3', '3/1/2014', '1', '1', '50000')
insert into orders (order_id, order_date, com_id, sales_id, amount) values ('4', '4/1/2014', '1', '4', '25000')




;with cte as (
select s.sales_id, s.name, c_name = c.name  from salesperson s 
left outer join orders o 
on s.sales_id = o.sales_id
left outer join company c 
on o.com_id = c.com_id
)
select distinct c1.name from cte c1 
where not exists 
(select * from cte c2 where c1.sales_id = c2.sales_id and c2.c_name = 'RED')
































