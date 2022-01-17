/* 2142. The Number of Passengers in Each Bus I

Table: Buses

+--------------+------+
| Column Name  | Type |
+--------------+------+
| bus_id       | int  |
| arrival_time | int  |
+--------------+------+
bus_id is the primary key column for this table.
Each row of this table contains information about the arrival time of a bus at the Leetcode station.
There will be no two buses that arrive at the same time.
 

Table: Passengers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| passenger_id | int  |
| arrival_time | int  |
+--------------+------+
passenger_id is the primary key column for this table.
Each row of this table contains information about the arrival time of a passenger at the Leetcode station.
 

Buses and passengers arrive at the Leetcode station. If a bus arrives at the station at a time tbus and a passenger arrived at a time tpassenger where tpassenger <= tbus and the passenger did not catch any bus, the passenger will use that bus.

Write an SQL query to report the number of users that used each bus.

Return the result table ordered by bus_id in ascending order.

The query result format is in the following example.

 

Example 1:

Input: 
Buses table:
+--------+--------------+
| bus_id | arrival_time |
+--------+--------------+
| 1      | 2            |
| 2      | 4            |
| 3      | 7            |
+--------+--------------+
Passengers table:
+--------------+--------------+
| passenger_id | arrival_time |
+--------------+--------------+
| 11           | 1            |
| 12           | 5            |
| 13           | 6            |
| 14           | 7            |
+--------------+--------------+
Output: 
+--------+----------------+
| bus_id | passengers_cnt |
+--------+----------------+
| 1      | 1              |
| 2      | 0              |
| 3      | 3              |
+--------+----------------+
Explanation: 
- Passenger 11 arrives at time 1.
- Bus 1 arrives at time 2 and collects passenger 11.

- Bus 2 arrives at time 4 and does not collect any passengers.

- Passenger 12 arrives at time 5.
- Passenger 13 arrives at time 6.
- Passenger 14 arrives at time 7.
- Bus 3 arrives at time 7 and collects passengers 12, 13, and 14.


*/

Create table Buses (bus_id int, arrival_time int)
Create table Passengers (passenger_id int, arrival_time int)
Truncate table Buses
insert into Buses (bus_id, arrival_time) values ('1', '2')
insert into Buses (bus_id, arrival_time) values ('2', '4')
insert into Buses (bus_id, arrival_time) values ('3', '7')
Truncate table Passengers
insert into Passengers (passenger_id, arrival_time) values ('11', '1')
insert into Passengers (passenger_id, arrival_time) values ('12', '5')
insert into Passengers (passenger_id, arrival_time) values ('13', '6')
insert into Passengers (passenger_id, arrival_time) values ('14', '7')


/* Write your T-SQL query statement below */
with bus as 
(
select bus_id
, prev = lag(arrival_time, 1,  -1) over(order by arrival_time) -- find the previous bus arrival time
, arrival_time 
from buses
)
select
b.bus_id
, passengers_cnt = count(p.passenger_id)
from bus b left outer join passengers p on p.arrival_time <= b.arrival_time and p.arrival_time > b.prev 
group by b.bus_id
order by b.bus_id


