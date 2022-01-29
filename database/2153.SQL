/*
2153. The Number of Passengers in Each Bus II

Table: Buses

+--------------+------+
| Column Name  | Type |
+--------------+------+
| bus_id       | int  |
| arrival_time | int  |
| capacity     | int  |
+--------------+------+
bus_id is the primary key column for this table.
Each row of this table contains information about the arrival time of a bus at the Leetcode station and its capacity (i.e., the number of empty seats it has).
There will be no two buses that arrive at the same time and capacity will be a positive integer.
 

Table: Passengers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| passenger_id | int  |
| arrival_time | int  |
+--------------+------+
passenger_id is the primary key column for this table.
Each row of this table contains information about the arrival time of a passenger at the Leetcode station.
 

Buses and passengers arrive at the Leetcode station. If a bus arrives at the station at a time tbus and a passenger arrived at a time tpassenger where tpassenger <= tbus and the passenger did not catch any bus, the passenger will use that bus. In addition, each bus has a capacity. If at the moment the bus arrives at the station there are more passengers waiting than its capacity capacity, only capacity passengers will use the bus.

Write an SQL query to report the number of users that used each bus.

Return the result table ordered by bus_id in ascending order.

The query result format is in the following example.

 

Example 1:

Input: 
Buses table:
+--------+--------------+----------+
| bus_id | arrival_time | capacity |
+--------+--------------+----------+
| 1      | 2            | 1        |
| 2      | 4            | 10       |
| 3      | 7            | 2        |
+--------+--------------+----------+
Passengers table:
+--------------+--------------+
| passenger_id | arrival_time |
+--------------+--------------+
| 11           | 1            |
| 12           | 1            |
| 13           | 5            |
| 14           | 6            |
| 15           | 7            |
+--------------+--------------+
Output: 
+--------+----------------+
| bus_id | passengers_cnt |
+--------+----------------+
| 1      | 1              |
| 2      | 1              |
| 3      | 2              |
+--------+----------------+
Explanation: 
- Passenger 11 arrives at time 1.
- Passenger 12 arrives at time 1.
- Bus 1 arrives at time 2 and collects passenger 11 as it has one empty seat.

- Bus 2 arrives at time 4 and collects passenger 12 as it has ten empty seats.

- Passenger 12 arrives at time 5.
- Passenger 13 arrives at time 6.
- Passenger 14 arrives at time 7.
- Bus 3 arrives at time 7 and collects passengers 12 and 13 as it has two empty seats.

*/

Create table Buses (bus_id int, arrival_time int, capacity int)
Create table Passengers (passenger_id int, arrival_time int)
Truncate table Buses
insert into Buses (bus_id, arrival_time, capacity) values ('1', '2', '1')
insert into Buses (bus_id, arrival_time, capacity) values ('2', '4', '10')
insert into Buses (bus_id, arrival_time, capacity) values ('3', '7', '2')
Truncate table Passengers
insert into Passengers (passenger_id, arrival_time) values ('11', '1')
insert into Passengers (passenger_id, arrival_time) values ('12', '1')
insert into Passengers (passenger_id, arrival_time) values ('13', '5')
insert into Passengers (passenger_id, arrival_time) values ('14', '6')
insert into Passengers (passenger_id, arrival_time) values ('15', '7')



/* Write your T-SQL query statement below */
with c1 as -- Find the previous bus arrival time 
(
    select
		rn = row_number() over (order by  arrival_time)  -- create a row number for the sequence of the bus.
		,bus_id
		,arrival_time
		,prev_time = lag(arrival_time, 1 , -999) over(order by arrival_time)  
		,capacity
    from Buses
)
, c2 as -- Find how many people current bus needs to take, without thinking of the remaining passengers from the previous buses
(
	select 
		c1.rn
		, c1.bus_id
		, c1.capacity
		, curr_passenger_cnt = count(p.passenger_id) 
	from c1 left outer join Passengers p on p.arrival_time <= c1.arrival_time and p.arrival_time > c1.prev_time
	group by c1.rn, c1.bus_id, c1.capacity
)
, cte as  -- find how many people previous bus left, and how many current bus can take.
          -- current bus pick = prev_remaining + current_Passenger
		  -- current bus remaining = max(0, prev_remaining + current_Passenger - capacity)
(
	select 
		rn
		, bus_id
		, capacity
		, curr_passenger_cnt
		, accumulated_remaining = case when curr_passenger_cnt - capacity <= 0 then 0 else curr_passenger_cnt - capacity end  
	from c2 where rn = 1 --starting from the first arrival bus

	union all 
		
	select    
		 c2.rn 
		,c2.bus_id
		,c2.capacity
		,curr_passenger_cnt = c2.curr_passenger_cnt + c.accumulated_remaining
		,accumulated_remaining = case when c2.curr_passenger_cnt + c.accumulated_remaining - c2.capacity <= 0 then 0 else c2.curr_passenger_cnt + c.accumulated_remaining - c2.capacity end
	from cte c inner join c2 on c2.rn = c.rn + 1
)
select 
bus_id
, passengers_cnt = case when accumulated_remaining > 0 then capacity else curr_passenger_cnt end  
from cte
order by bus_id



