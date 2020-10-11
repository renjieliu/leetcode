/*

In social network like Facebook or Twitter, people send friend requests and accept others' requests as well.
 

Table request_accepted holds the data of friend acceptance, while requester_id and accepter_id both are the id of a person.
 

| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
Write a query to find the the people who has most friends and the most friends number. For the sample data above, the result is:
| id | num |
|----|-----|
| 3  | 3   |
Note:
It is guaranteed there is only 1 people having the most friends.
The friend request could only been accepted once, which mean there is no multiple records with the same requester_id and accepter_id value.
 

Explanation:
The person with id '3' is a friend of people '1', '2' and '4', so he has 3 friends in total, which is the most number than any others.
 

Follow-up:
In the real world, multiple people could have the same most number of friends, can you find all these people in this case?
*/


Create table request_accepted ( requester_id INT NOT NULL, accepter_id INT NULL, accept_date DATE NULL)
Truncate table request_accepted
insert into request_accepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09')




/* Write your T-SQL query statement below */
select top 1 id, num =  sum(cnt) from 
(
	select id = accepter_id, cnt =  count (1)  from request_accepted
	where isnull(requester_id, 0) <> isnull(accepter_id,0)
	group by accepter_id
	union all
	select requester_id, cnt = count(1) from request_accepted
	where isnull(requester_id, 0) <> isnull(accepter_id,0)
	group by requester_id
) T 
group by id
order by 2 desc 





























