/*
1949. Strong Friendship


Table: Friendship

+-------------+------+
| Column Name | Type |
+-------------+------+
| user1_id    | int  |
| user2_id    | int  |
+-------------+------+
(user1_id, user2_id) is the primary key for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.
 

A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

Write an SQL query to find all the strong friendships.

Note that the result table should not contain duplicates with user1_id < user2_id.

Return the result table in any order.

The query result format is in the following example:

 

Friendship table:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 2        |
| 1        | 3        |
| 2        | 3        |
| 1        | 4        |
| 2        | 4        |
| 1        | 5        |
| 2        | 5        |
| 1        | 7        |
| 3        | 7        |
| 1        | 6        |
| 3        | 6        |
| 2        | 6        |
+----------+----------+

Result table:
+----------+----------+---------------+
| user1_id | user2_id | common_friend |
+----------+----------+---------------+
| 1        | 2        | 4             |
| 1        | 3        | 3             |
+----------+----------+---------------+
Users 1 and 2 have 4 common friends (3, 4, 5, and 6).
Users 1 and 3 have 3 common friends (2, 6, and 7).
We did not include the friendship of users 2 and 3 because they only have two common friends (1 and 6).


*/


Create table Friendship (user1_id int, user2_id int)
Truncate table Friendship
insert into Friendship (user1_id, user2_id) values ('1', '2')
insert into Friendship (user1_id, user2_id) values ('1', '3')
insert into Friendship (user1_id, user2_id) values ('2', '3')
insert into Friendship (user1_id, user2_id) values ('1', '4')
insert into Friendship (user1_id, user2_id) values ('2', '4')
insert into Friendship (user1_id, user2_id) values ('1', '5')
insert into Friendship (user1_id, user2_id) values ('2', '5')
insert into Friendship (user1_id, user2_id) values ('1', '7')
insert into Friendship (user1_id, user2_id) values ('3', '7')
insert into Friendship (user1_id, user2_id) values ('1', '6')
insert into Friendship (user1_id, user2_id) values ('3', '6')
insert into Friendship (user1_id, user2_id) values ('2', '6')

go

/* Write your T-SQL query statement below */
with base as 
(select user1_id, user2_id from Friendship
  union all 
 select user2_id, user1_id from Friendship
) 
select 
user1_id = main.user1_id
,user2_id = main.user2_id
,common_friend = count(distinct b.user2_id)
from Friendship main 
left outer join base a 
on main.user1_id = a.user1_id and a.user2_id != main.user1_id -- find friends of a
left outer join base b 
on main.user2_id = b.user1_id and b.user2_id = a.user2_id -- find friends of b, and which happens to be the friends of a as well. 
group by main.user1_id, main.user2_id
having count(distinct b.user2_id)>=3
order by 1, 2 


--previous approach
-- /* Write your T-SQL query statement below */
-- with base as 
-- (select user1_id, user2_id from Friendship
--   union all 
--  select user2_id, user1_id from Friendship
-- ) 
-- select 
-- user1_id = case when main.user1_id <= main.user2_id then main.user1_id else main.user2_id end
-- ,user2_id = case when main.user1_id > main.user2_id then main.user1_id else main.user2_id end
-- ,common_friend = count(distinct b.user2_id)
-- from base main 
-- left outer join base a 
-- on main.user1_id = a.user1_id -- find friends of a 
-- left outer join base b 
-- on main.user2_id = b.user1_id and b.user2_id = a.user2_id -- find friends of b, and which happens to be the friends of a as well. 
-- group by case when main.user1_id <= main.user2_id then main.user1_id else main.user2_id end
-- , case when main.user1_id > main.user2_id then main.user1_id else main.user2_id end
-- having count(distinct b.user2_id)>=3
-- order by 1, 2 







































