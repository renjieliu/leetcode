/*
Table: Players

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| player_id   | int   |
| group_id    | int   |
+-------------+-------+
player_id is the primary key of this table.
Each row of this table indicates the group of each player.
Table: Matches

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| first_player  | int     |
| second_player | int     | 
| first_score   | int     |
| second_score  | int     |
+---------------+---------+
match_id is the primary key of this table.
Each row is a record of a match, first_player and second_player contain the player_id of each match.
first_score and second_score contain the number of points of the first_player and second_player respectively.
You may assume that, in each match, players belongs to the same group.
 

The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

Write an SQL query to find the winner in each group.

The query result format is in the following example:

Players table:
+-----------+------------+
| player_id | group_id   |
+-----------+------------+
| 15        | 1          |
| 25        | 1          |
| 30        | 1          |
| 45        | 1          |
| 10        | 2          |
| 35        | 2          |
| 50        | 2          |
| 20        | 3          |
| 40        | 3          |
+-----------+------------+

Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | first_player | second_player | first_score | second_score |
+------------+--------------+---------------+-------------+--------------+
| 1          | 15           | 45            | 3           | 0            |
| 2          | 30           | 25            | 1           | 2            |
| 3          | 30           | 15            | 2           | 0            |
| 4          | 40           | 20            | 5           | 2            |
| 5          | 35           | 50            | 1           | 1            |
+------------+--------------+---------------+-------------+--------------+

Result table:
+-----------+------------+
| group_id  | player_id  |
+-----------+------------+ 
| 1         | 15         |
| 2         | 35         |
| 3         | 40         |
+-----------+------------+


*/



Create table Players (player_id int, group_id int)
Create table Matches (match_id int, first_player int, second_player int, first_score int, second_score int)
Truncate table Players
insert into Players (player_id, group_id) values ('10', '2')
insert into Players (player_id, group_id) values ('15', '1')
insert into Players (player_id, group_id) values ('20', '3')
insert into Players (player_id, group_id) values ('25', '1')
insert into Players (player_id, group_id) values ('30', '1')
insert into Players (player_id, group_id) values ('35', '2')
insert into Players (player_id, group_id) values ('40', '3')
insert into Players (player_id, group_id) values ('45', '1')
insert into Players (player_id, group_id) values ('50', '2')
Truncate table Matches
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('1', '15', '45', '3', '0')
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('2', '30', '25', '1', '2')
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('3', '30', '15', '2', '0')
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('4', '40', '20', '5', '2')
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('5', '35', '50', '1', '1')


--select * from Players 
--select * from Matches 



; with ps as 
(
select match_id ,player = first_player , score = first_score  from Matches
union
select match_id , second_player, second_score  from Matches 
), base as (
select p.group_id, p.player_id, total_score = isnull(sum(score), 0) from
ps right outer join players p
on p.player_id = ps.player
group by p.group_id, p.player_id
), staging as (
select 
group_id, player_id, rn = ROW_NUMBER() over (partition by group_id order by total_score desc , player_id)
from base 
)
select group_id, player_id from staging where rn = 1 