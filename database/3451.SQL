/*
Table:  logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| log_id      | int     |
| ip          | varchar |
| status_code | int     |
+-------------+---------+
log_id is the unique key for this table.
Each row contains server access log information including IP address and HTTP status code.
Write a solution to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:

Contains numbers greater than 255 in any octet
Has leading zeros in any octet (like 01.02.03.04)
Has less or more than 4 octets
Return the result table ordered by invalid_count, ip in descending order respectively. 

The result format is in the following example.

 

Example:

Input:

logs table:

+--------+---------------+-------------+
| log_id | ip            | status_code | 
+--------+---------------+-------------+
| 1      | 192.168.1.1   | 200         | 
| 2      | 256.1.2.3     | 404         | 
| 3      | 192.168.001.1 | 200         | 
| 4      | 192.168.1.1   | 200         | 
| 5      | 192.168.1     | 500         | 
| 6      | 256.1.2.3     | 404         | 
| 7      | 192.168.001.1 | 200         | 
+--------+---------------+-------------+
Output:

+---------------+--------------+
| ip            | invalid_count|
+---------------+--------------+
| 256.1.2.3     | 2            |
| 192.168.001.1 | 2            |
| 192.168.1     | 1            |
+---------------+--------------+
Explanation:

256.1.2.3 is invalid because 256 > 255
192.168.001.1 is invalid because of leading zeros
192.168.1 is invalid because it has only 3 octets
The output table is ordered by invalid_count, ip in descending order respectively.

*/


CREATE TABLE logs (
    log_id INT,
    ip VARCHAR(255),
    status_code INT
)

Truncate table logs
insert into logs (log_id, ip, status_code) values ('1', '192.168.1.1', '200')
insert into logs (log_id, ip, status_code) values ('2', '256.1.2.3', '404')
insert into logs (log_id, ip, status_code) values ('3', '192.168.001.1', '200')
insert into logs (log_id, ip, status_code) values ('4', '192.168.1.1', '200')
insert into logs (log_id, ip, status_code) values ('5', '192.168.1', '500')
insert into logs (log_id, ip, status_code) values ('6', '256.1.2.3', '404')
insert into logs (log_id, ip, status_code) values ('7', '192.168.001.1', '200')




; with base as
(
select
log_id
, ip
, status_code
, ip_1 = parsename(ip, 1)
, ip_2 = parsename(ip, 2)
, ip_3 = parsename(ip, 3)
, ip_4 = parsename(ip, 4)
, ip_5 = parsename(ip, 5) -- just to check if it has more than 4 parts
from
logs
) , cte as (
select
*
, invalid = case when isnull(ip_1, '') = '' or isnull(ip_2, '') = '' or isnull(ip_3, '') = '' or isnull(ip_4, '') = '' or isnull(ip_5, '') != '' then 1 -- exactly 4 parts
             when ip_1 like '%[^0-9]%' or ip_2 like '%[^0-9]%' or ip_3 like '%[^0-9]%' or ip_4 like '%[^0-9]%' then 1 -- each part are number only
             when left(ip_1, 1) = '0' or left(ip_2, 1) = '0' or left(ip_3, 1) = '0' or left(ip_4, 1) = '0' then 1  -- all the parts need to be number
             when try_cast(ip_1 as int) not between 0 and 255 -- between 0 and 255
                    or
                  try_cast(ip_2 as int) not between 0 and 255
                    or
                  try_cast(ip_3 as int) not between 0 and 255
                    or
                  try_cast(ip_4 as int) not between 0 and 255
                  then 1
             else 0
        end
from base
)
select ip, invalid_count = count(*) from cte
where invalid = 1
group by ip
order by invalid_count desc, ip desc







