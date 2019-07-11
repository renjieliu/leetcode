/*
In facebook, there is a follow table with two columns: followee, follower.

Please write a sql query to get the amount of each follower’s follower if he/she has one.

For example:

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+
should output:
+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+
Explaination:
Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.
 

 

Note:
Followee would not follow himself/herself in all cases.
Please display the result in follower's alphabet order.

*/


Create table follow (followee varchar(255), follower varchar(255))
Truncate table follow
insert into follow (followee, follower) values ('A', 'B')
insert into follow (followee, follower) values ('B', 'C')
insert into follow (followee, follower) values ('B', 'D')
insert into follow (followee, follower) values ('D', 'E')



# Write your MySQL query statement below
select er.follower, count(distinct ee.follower) num from follow er inner join follow ee
on er.follower = ee.followee
group by er.follower
order by 1 













