/*
Table: books

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| book_id     | int     |
| title       | varchar |
| author      | varchar |
| genre       | varchar |
| pages       | int     |
+-------------+---------+
book_id is the unique ID for this table.
Each row contains information about a book including its genre and page count.
Table: reading_sessions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| session_id     | int     |
| book_id        | int     |
| reader_name    | varchar |
| pages_read     | int     |
| session_rating | int     |
+----------------+---------+
session_id is the unique ID for this table.
Each row represents a reading session where someone read a portion of a book. session_rating is on a scale of 1-5.
Write a solution to find books that have polarized opinions - books that receive both very high ratings and very low ratings from different readers.

A book has polarized opinions if it has at least one rating ≥ 4 and at least one rating ≤ 2
Only consider books that have at least 5 reading sessions
Calculate the rating spread as (highest_rating - lowest_rating)
Calculate the polarization score as the number of extreme ratings (ratings ≤ 2 or ≥ 4) divided by total sessions
Only include books where polarization score ≥ 0.6 (at least 60% extreme ratings)
Return the result table ordered by polarization score in descending order, then by title in descending order.

The result format is in the following example.

 

Example:

Input:

books table:

+---------+------------------------+---------------+----------+-------+
| book_id | title                  | author        | genre    | pages |
+---------+------------------------+---------------+----------+-------+
| 1       | The Great Gatsby       | F. Scott      | Fiction  | 180   |
| 2       | To Kill a Mockingbird  | Harper Lee    | Fiction  | 281   |
| 3       | 1984                   | George Orwell | Dystopian| 328   |
| 4       | Pride and Prejudice    | Jane Austen   | Romance  | 432   |
| 5       | The Catcher in the Rye | J.D. Salinger | Fiction  | 277   |
+---------+------------------------+---------------+----------+-------+
reading_sessions table:

+------------+---------+-------------+------------+----------------+
| session_id | book_id | reader_name | pages_read | session_rating |
+------------+---------+-------------+------------+----------------+
| 1          | 1       | Alice       | 50         | 5              |
| 2          | 1       | Bob         | 60         | 1              |
| 3          | 1       | Carol       | 40         | 4              |
| 4          | 1       | David       | 30         | 2              |
| 5          | 1       | Emma        | 45         | 5              |
| 6          | 2       | Frank       | 80         | 4              |
| 7          | 2       | Grace       | 70         | 4              |
| 8          | 2       | Henry       | 90         | 5              |
| 9          | 2       | Ivy         | 60         | 4              |
| 10         | 2       | Jack        | 75         | 4              |
| 11         | 3       | Kate        | 100        | 2              |
| 12         | 3       | Liam        | 120        | 1              |
| 13         | 3       | Mia         | 80         | 2              |
| 14         | 3       | Noah        | 90         | 1              |
| 15         | 3       | Olivia      | 110        | 4              |
| 16         | 3       | Paul        | 95         | 5              |
| 17         | 4       | Quinn       | 150        | 3              |
| 18         | 4       | Ruby        | 140        | 3              |
| 19         | 5       | Sam         | 80         | 1              |
| 20         | 5       | Tara        | 70         | 2              |
+------------+---------+-------------+------------+----------------+
Output:

+---------+------------------+---------------+-----------+-------+---------------+--------------------+
| book_id | title            | author        | genre     | pages | rating_spread | polarization_score |
+---------+------------------+---------------+-----------+-------+---------------+--------------------+
| 1       | The Great Gatsby | F. Scott      | Fiction   | 180   | 4             | 1.00               |
| 3       | 1984             | George Orwell | Dystopian | 328   | 4             | 1.00               |
+---------+------------------+---------------+-----------+-------+---------------+--------------------+
Explanation:

The Great Gatsby (book_id = 1):
Has 5 reading sessions (meets minimum requirement)
Ratings: 5, 1, 4, 2, 5
Has ratings ≥ 4: 5, 4, 5 (3 sessions)
Has ratings ≤ 2: 1, 2 (2 sessions)
Rating spread: 5 - 1 = 4
Extreme ratings (≤2 or ≥4): All 5 sessions (5, 1, 4, 2, 5)
Polarization score: 5/5 = 1.00 (≥ 0.6, qualifies)
1984 (book_id = 3):
Has 6 reading sessions (meets minimum requirement)
Ratings: 2, 1, 2, 1, 4, 5
Has ratings ≥ 4: 4, 5 (2 sessions)
Has ratings ≤ 2: 2, 1, 2, 1 (4 sessions)
Rating spread: 5 - 1 = 4
Extreme ratings (≤2 or ≥4): All 6 sessions (2, 1, 2, 1, 4, 5)
Polarization score: 6/6 = 1.00 (≥ 0.6, qualifies)
Books not included:
To Kill a Mockingbird (book_id = 2): All ratings are 4-5, no low ratings (≤2)
Pride and Prejudice (book_id = 4): Only 2 sessions (< 5 minimum)
The Catcher in the Rye (book_id = 5): Only 2 sessions (< 5 minimum)
The result table is ordered by polarization score in descending order, then by book title in descending order.



*/


CREATE TABLE books (
    book_id INT,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(100),
    pages INT
)
CREATE TABLE reading_sessions (
    session_id INT,
    book_id INT,
    reader_name VARCHAR(255),
    pages_read INT,
    session_rating INT
)
Truncate table books
insert into books (book_id, title, author, genre, pages) values ('1', 'The Great Gatsby', 'F. Scott', 'Fiction', '180')
insert into books (book_id, title, author, genre, pages) values ('2', 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', '281')
insert into books (book_id, title, author, genre, pages) values ('3', '1984', 'George Orwell', 'Dystopian', '328')
insert into books (book_id, title, author, genre, pages) values ('4', 'Pride and Prejudice', 'Jane Austen', 'Romance', '432')
insert into books (book_id, title, author, genre, pages) values ('5', 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', '277')
Truncate table reading_sessions
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('1', '1', 'Alice', '50', '5')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('2', '1', 'Bob', '60', '1')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('3', '1', 'Carol', '40', '4')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('4', '1', 'David', '30', '2')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('5', '1', 'Emma', '45', '5')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('6', '2', 'Frank', '80', '4')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('7', '2', 'Grace', '70', '4')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('8', '2', 'Henry', '90', '5')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('9', '2', 'Ivy', '60', '4')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('10', '2', 'Jack', '75', '4')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('11', '3', 'Kate', '100', '2')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('12', '3', 'Liam', '120', '1')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('13', '3', 'Mia', '80', '2')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('14', '3', 'Noah', '90', '1')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('15', '3', 'Olivia', '110', '4')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('16', '3', 'Paul', '95', '5')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('17', '4', 'Quinn', '150', '3')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('18', '4', 'Ruby', '140', '3')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('19', '5', 'Sam', '80', '1')
insert into reading_sessions (session_id, book_id, reader_name, pages_read, session_rating) values ('20', '5', 'Tara', '70', '2')



/* Write your T-SQL query statement below */
; with cte as
(
    select 
    highest_rating = max(session_rating) over(partition by book_id)
    , lowest_rating = min(session_rating) over(partition by book_id)
    , sessions_cnt = count(session_rating) over(partition by book_id)
    , rating_spread = max(session_rating) over(partition by book_id) - min(session_rating) over(partition by book_id)
    , p_score = cast( 1.0*count(case when session_rating <> 3 then session_id else null end) over (partition by book_id) /  count(session_rating) over(partition by book_id) as decimal(10, 2))
    , *
    from reading_sessions
)
select 
distinct 
b.book_id
, b.title 
, b.author
, b.genre
, b.pages
, c.rating_spread
, polarization_score = c.p_score
from cte c inner join books b 
on c.book_id = b.book_id
where 
highest_rating >=4 
and lowest_rating <= 2 
and sessions_cnt>=5
and p_score>= 0.6
order by polarization_score desc, b.title desc


