/*
Get the highest answer rate question from a table survey_log with these columns: uid, action, question_id, answer_id, q_num, timestamp.

uid means user id; action has these kind of values: "show", "answer", "skip"; answer_id is not null when action column is "answer", while is null for "show" and "skip"; q_num is the numeral order of the question in current session.

Write a sql query to identify the question which has the highest answer rate.

Example:

Input:
+------+-----------+--------------+------------+-----------+------------+
| uid  | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
Output:
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+
Explanation:
question 285 has answer rate 1/1, while question 369 has 0/1 answer rate, so output 285.

*/

Create table survey_log (uid int, action varchar(255), question_id int, answer_id int, q_num int, timestamp int)
Truncate table survey_log
insert into survey_log (uid, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '285', 'None', '1', '123')
insert into survey_log (uid, action, question_id, answer_id, q_num, timestamp) values ('5', 'answer', '285', '124124', '1', '124')
insert into survey_log (uid, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '369', 'None', '2', '125')
insert into survey_log (uid, action, question_id, answer_id, q_num, timestamp) values ('5', 'skip', '369', 'None', '2', '126')



with show as (
select question_id , cnt = count(1)  from survey_log
where action = 'show'
group by question_id 
) , 
answer as (
select question_id , cnt =count(1)  from survey_log
where action = 'answer'
group by question_id 
), ratio as (
select a.question_id, a_cnt = a.cnt,s_cnt = s.cnt ,r = 1.0*a.cnt/(a.cnt+isnull(s.cnt,0)) from answer a left outer join show s on a.question_id = s.question_id
), tmp as 
(select question_id, rn = ROW_NUMBER() over(order by a_cnt desc, s_cnt desc, r desc ) from ratio)
select survey_log = question_id from tmp where rn = 1 
















