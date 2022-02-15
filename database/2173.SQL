/*
2173. Longest Winning Streak

Table: Matches

+-------------+------+
| Column Name | Type |
+-------------+------+
| player_id   | int  |
| match_day   | date |
| result      | enum |
+-------------+------+
(player_id, match_day) is the primary key for this table.
Each row of this table contains the ID of a player, the day of the match they played, and the result of that match.
The result column is an ENUM type of ('Win', 'Draw', 'Lose').
 

The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.

Write an SQL query to count the longest winning streak for each player.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Matches table:
+-----------+------------+--------+
| player_id | match_day  | result |
+-----------+------------+--------+
| 1         | 2022-01-17 | Win    |
| 1         | 2022-01-18 | Win    |
| 1         | 2022-01-25 | Win    |
| 1         | 2022-01-31 | Draw   |
| 1         | 2022-02-08 | Win    |
| 2         | 2022-02-06 | Lose   |
| 2         | 2022-02-08 | Lose   |
| 3         | 2022-03-30 | Win    |
+-----------+------------+--------+
Output: 
+-----------+----------------+
| player_id | longest_streak |
+-----------+----------------+
| 1         | 3              |
| 2         | 0              |
| 3         | 1              |
+-----------+----------------+
Explanation: 
Player 1:
From 2022-01-17 to 2022-01-25, player 1 won 3 consecutive matches.
On 2022-01-31, player 1 had a draw.
On 2022-02-08, player 1 won a match.
The longest winning streak was 3 matches.

Player 2:
From 2022-02-06 to 2022-02-08, player 2 lost 2 consecutive matches.
The longest winning streak was 0 matches.

Player 3:
On 2022-03-30, player 3 won a match.
The longest winning streak was 1 match.


Follow up: If we are interested in calculating the longest streak without losing (i.e., win or draw), how will your solution change?

*/


Create table Matches (player_id int, match_day date, result ENUM('Win', 'Draw', 'Lose'))
Truncate table Matches
insert into Matches (player_id, match_day, result) values ('1', '2022-01-17', 'Win')
insert into Matches (player_id, match_day, result) values ('1', '2022-01-18', 'Win')
insert into Matches (player_id, match_day, result) values ('1', '2022-01-25', 'Win')
insert into Matches (player_id, match_day, result) values ('1', '2022-01-31', 'Draw')
insert into Matches (player_id, match_day, result) values ('1', '2022-02-08', 'Win')
insert into Matches (player_id, match_day, result) values ('2', '2022-02-06', 'Lose')
insert into Matches (player_id, match_day, result) values ('2', '2022-02-08', 'Lose')
insert into Matches (player_id, match_day, result) values ('3', '2022-03-30', 'Win')

-- same approach T-SQL TLE error

/* Write your PL/SQL query statement below */
with base as
(select 
 ROW_NUMBER() over (partition by player_id order by match_day) rn
 ,player_id
 ,match_day
 ,result
 from Matches
), cte (player_id, streak, rn) as 
(select player_id, 1 streak, rn from base where result = 'Win'
    union all 
select c.player_id, c.streak+1, b.rn from cte c inner join base b
on c.player_id = b.player_id and c.rn+1 = b.rn and b.result = 'Win'
)  
select 
    m.player_id, 
    max(coalesce(streak, 0)) longest_streak
from Matches m left outer join cte c on m.player_id = c.player_id
group by m.player_id
order by 1




/* Write your T-SQL query statement below */
-- with base as
-- (select 
--  rn = row_number() over (partition by player_id order by match_day)
--  ,* 
--  from Matches)
--  , cte as 
--  (select player_id, streak=1, rn from base where result = 'Win'
--   union all 
--   select c.player_id, c.streak+1, b.rn from cte c inner join base b
--   on c.player_id = b.player_id and c.rn+1 = b.rn and b.result = 'Win'
--  )
--  select 
--  m.player_id, 
--  longest_streak = max(isnull(streak, 0))
--  from Matches m left outer join cte c
--  on m.player_id = c.player_id
--  group by m.player_id
--  order by 1
 
