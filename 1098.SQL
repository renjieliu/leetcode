/*
Table: Books

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| name           | varchar |
| available_from | date    |
+----------------+---------+
book_id is the primary key of this table.
Table: Orders

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| order_id       | int     |
| book_id        | int     |
| quantity       | int     |
| dispatch_date  | date    |
+----------------+---------+
order_id is the primary key of this table.
book_id is a foreign key to the Books table.
 

Write an SQL query that reports the books that have sold less than 10 copies in the last year, excluding books that have been available for less than 1 month from today. Assume today is 2019-06-23.

The query result format is in the following example:

Books table:
+---------+--------------------+----------------+
| book_id | name               | available_from |
+---------+--------------------+----------------+
| 1       | "Kalila And Demna" | 2010-01-01     |
| 2       | "28 Letters"       | 2012-05-12     |
| 3       | "The Hobbit"       | 2019-06-10     |
| 4       | "13 Reasons Why"   | 2019-06-01     |
| 5       | "The Hunger Games" | 2008-09-21     |
+---------+--------------------+----------------+

Orders table:
+----------+---------+----------+---------------+
| order_id | book_id | quantity | dispatch_date |
+----------+---------+----------+---------------+
| 1        | 1       | 2        | 2018-07-26    |
| 2        | 1       | 1        | 2018-11-05    |
| 3        | 3       | 8        | 2019-06-11    |
| 4        | 4       | 6        | 2019-06-05    |
| 5        | 4       | 5        | 2019-06-20    |
| 6        | 5       | 9        | 2009-02-02    |
| 7        | 5       | 8        | 2010-04-13    |
+----------+---------+----------+---------------+

Result table:
+-----------+--------------------+
| book_id   | name               |
+-----------+--------------------+
| 1         | "Kalila And Demna" |
| 2         | "28 Letters"       |
| 5         | "The Hunger Games" |
+-----------+--------------------+

*/

Create table Books (book_id int, name varchar(50), available_from date)
Create table Orders (order_id int, book_id int, quantity int, dispatch_date date)
Truncate table Books
insert into Books (book_id, name, available_from) values ('1', 'Kalila And Demna', '2010-01-01')
insert into Books (book_id, name, available_from) values ('2', '28 Letters', '2012-05-12')
insert into Books (book_id, name, available_from) values ('3', 'The Hobbit', '2019-06-10')
insert into Books (book_id, name, available_from) values ('4', '13 Reasons Why', '2019-06-01')
insert into Books (book_id, name, available_from) values ('5', 'The Hunger Games', '2008-09-21')
Truncate table Orders
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('1', '1', '2', '2018-07-26')
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('2', '1', '1', '2018-11-05')
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('3', '3', '8', '2019-06-11')
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('4', '4', '6', '2019-06-05')
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('5', '4', '5', '2019-06-20')
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('6', '5', '9', '2009-02-02')
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('7', '5', '8', '2010-04-13')


/* Write your T-SQL query statement below */
select distinct b.book_id, b.name from 
(select * from books where available_from < dateadd(month, -1, '2019-06-23') )b 
left outer join
(select * from Orders where dispatch_date between '2018-06-23' and '2019-06-23') o
on  b.book_id = o.book_id
group by  b.book_id, b.name
having sum(isnull(o.quantity,0)) <10 
order by 1   
























