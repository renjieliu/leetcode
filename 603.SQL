/*

Several friends at a cinema ticket office would like to reserve consecutive available seats.
Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
 

Your query should return the following result for the sample case above.
 

| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
Note:
The seat_id is an auto increment int, and free is bool ('1' means free, and '0' means occupied.).
Consecutive available seats are more than 2(inclusive) seats consecutively available.
*/


Create table cinema (seat_id int primary key auto_increment, free bool)
Truncate table cinema
insert into cinema (seat_id, free) values ('1', '1')
insert into cinema (seat_id, free) values ('2', '0')
insert into cinema (seat_id, free) values ('3', '1')
insert into cinema (seat_id, free) values ('4', '1')
insert into cinema (seat_id, free) values ('5', '1')



/* Write your T-SQL query statement below */
select seat_id from cinema c1
where 
 exists(select * from cinema c2 where c2.seat_id = c1.seat_id + 1 and c2.free = 1 )
and c1.free = 1
union 
select seat_id from cinema c1
where 
 exists(select * from cinema c2 where c2.seat_id = c1.seat_id - 1 and c2.free = 1 )
and c1.free = 1

















