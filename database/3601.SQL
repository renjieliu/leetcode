/*
3601. Find Drivers with Improved Fuel Efficiency

Table: drivers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| driver_id   | int     |
| driver_name | varchar |
+-------------+---------+
driver_id is the unique identifier for this table.
Each row contains information about a driver.
Table: trips

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trip_id       | int     |
| driver_id     | int     |
| trip_date     | date    |
| distance_km   | decimal |
| fuel_consumed | decimal |
+---------------+---------+
trip_id is the unique identifier for this table.
Each row represents a trip made by a driver, including the distance traveled and fuel consumed for that trip.
Write a solution to find drivers whose fuel efficiency has improved by comparing their average fuel efficiency in the first half of the year with the second half of the year.

Calculate fuel efficiency as distance_km / fuel_consumed for each trip
First half: January to June, Second half: July to December
Only include drivers who have trips in both halves of the year
Calculate the efficiency improvement as (second_half_avg - first_half_avg)
Round all results to 2 decimal places
Return the result table ordered by efficiency improvement in descending order, then by driver name in ascending order.

The result format is in the following example.

 

Example:

Input:

drivers table:

+-----------+---------------+
| driver_id | driver_name   |
+-----------+---------------+
| 1         | Alice Johnson |
| 2         | Bob Smith     |
| 3         | Carol Davis   |
| 4         | David Wilson  |
| 5         | Emma Brown    |
+-----------+---------------+
trips table:

+---------+-----------+------------+-------------+---------------+
| trip_id | driver_id | trip_date  | distance_km | fuel_consumed |
+---------+-----------+------------+-------------+---------------+
| 1       | 1         | 2023-02-15 | 120.5       | 10.2          |
| 2       | 1         | 2023-03-20 | 200.0       | 16.5          |
| 3       | 1         | 2023-08-10 | 150.0       | 11.0          |
| 4       | 1         | 2023-09-25 | 180.0       | 12.5          |
| 5       | 2         | 2023-01-10 | 100.0       | 9.0           |
| 6       | 2         | 2023-04-15 | 250.0       | 22.0          |
| 7       | 2         | 2023-10-05 | 200.0       | 15.0          |
| 8       | 3         | 2023-03-12 | 80.0        | 8.5           |
| 9       | 3         | 2023-05-18 | 90.0        | 9.2           |
| 10      | 4         | 2023-07-22 | 160.0       | 12.8          |
| 11      | 4         | 2023-11-30 | 140.0       | 11.0          |
| 12      | 5         | 2023-02-28 | 110.0       | 11.5          |
+---------+-----------+------------+-------------+---------------+
Output:

+-----------+---------------+------------------+-------------------+------------------------+
| driver_id | driver_name   | first_half_avg   | second_half_avg   | efficiency_improvement |
+-----------+---------------+------------------+-------------------+------------------------+
| 2         | Bob Smith     | 11.24            | 13.33             | 2.10                   |
| 1         | Alice Johnson | 11.97            | 14.02             | 2.05                   |
+-----------+---------------+------------------+-------------------+------------------------+
Explanation:

Alice Johnson (driver_id = 1):
First half trips (Jan-Jun): Feb 15 (120.5/10.2 = 11.81), Mar 20 (200.0/16.5 = 12.12)
First half average efficiency: (11.81 + 12.12) / 2 = 11.97
Second half trips (Jul-Dec): Aug 10 (150.0/11.0 = 13.64), Sep 25 (180.0/12.5 = 14.40)
Second half average efficiency: (13.64 + 14.40) / 2 = 14.02
Efficiency improvement: 14.02 - 11.97 = 2.05
Bob Smith (driver_id = 2):
First half trips: Jan 10 (100.0/9.0 = 11.11), Apr 15 (250.0/22.0 = 11.36)
First half average efficiency: (11.11 + 11.36) / 2 = 11.24
Second half trips: Oct 5 (200.0/15.0 = 13.33)
Second half average efficiency: 13.33
Efficiency improvement: 13.33 - 11.24 = 2.10 (rounded to 2 decimal places)
Drivers not included:
Carol Davis (driver_id = 3): Only has trips in first half (Mar, May)
David Wilson (driver_id = 4): Only has trips in second half (Jul, Nov)
Emma Brown (driver_id = 5): Only has trips in first half (Feb)
The output table is ordered by efficiency improvement in descending order then by name in ascending order.



*/



CREATE TABLE drivers (
    driver_id INT,
    driver_name VARCHAR(255)
)
CREATE TABLE trips (
    trip_id INT,
    driver_id INT,
    trip_date DATE,
    distance_km DECIMAL(8, 2),
    fuel_consumed DECIMAL(6, 2)
)
Truncate table drivers
insert into drivers (driver_id, driver_name) values ('1', 'Alice Johnson')
insert into drivers (driver_id, driver_name) values ('2', 'Bob Smith')
insert into drivers (driver_id, driver_name) values ('3', 'Carol Davis')
insert into drivers (driver_id, driver_name) values ('4', 'David Wilson')
insert into drivers (driver_id, driver_name) values ('5', 'Emma Brown')
Truncate table trips
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('1', '1', '2023-02-15', '120.5', '10.2')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('2', '1', '2023-03-20', '200.0', '16.5')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('3', '1', '2023-08-10', '150.0', '11.0')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('4', '1', '2023-09-25', '180.0', '12.5')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('5', '2', '2023-01-10', '100.0', '9.0')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('6', '2', '2023-04-15', '250.0', '22.0')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('7', '2', '2023-10-05', '200.0', '15.0')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('8', '3', '2023-03-12', '80.0', '8.5')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('9', '3', '2023-05-18', '90.0', '9.2')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('10', '4', '2023-07-22', '160.0', '12.8')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('11', '4', '2023-11-30', '140.0', '11.0')
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed) values ('12', '5', '2023-02-28', '110.0', '11.5')




/* Write your T-SQL query statement below */

;with base as 
(
    select 
    driver_id
    , trip_date
    , fuel_eff = distance_km / fuel_consumed
     from trips 
)
select 
d.driver_id
, d.driver_name
, first_half_avg = cast(avg(case when month(trip_date) between 1 and 6 then fuel_eff else NULL end) as decimal(10,2))
, second_half_avg = cast(avg(case when month(trip_date) between 7 and 12 then fuel_eff else NULL end) as decimal(10, 2))
, efficiency_improvement = cast(avg(case when month(trip_date) between 7 and 12 then fuel_eff else NULL end) - avg(case when month(trip_date) between 1 and 6 then fuel_eff else NULL end)  as decimal(10, 2))
from base b inner join drivers d 
on b.driver_id = d.driver_id 
group by 
d.driver_id
, d.driver_name
having avg(case when month(trip_date) between 7 and 12 then fuel_eff else NULL end) > avg(case when month(trip_date) between 1 and 6 then fuel_eff else NULL end)
order by 
avg(case when month(trip_date) between 7 and 12 then fuel_eff else NULL end) - avg(case when month(trip_date) between 1 and 6 then fuel_eff else NULL end) desc 
, d.driver_name 




