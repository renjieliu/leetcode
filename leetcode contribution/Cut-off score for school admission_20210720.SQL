/*
Question Title:
Cut-off score for school admission

Reason:
The question was asked by a non-profit organization in New York City. I have not seen this type of question on Leetcode. I think it might inspire other candidates.

Description:

We have 2 tables, school and exam. 

For each school, we have a quota for the number of students to be admitted. 

The task is to find the lowest cut-off score from the exam table. All the student with higher or equal score with be admitted.

To be fair, we will take the "all or none" approach, meaning if there're more than 1 student with the same cut-off score, and admitting all of them will surpass the quota, we will admit none of them. 

In case the school is not listed in the exam table, we show -1 in the result table for the school. 

Order the result by cut-off score descendingly.


Table:

school: 
- school_id (int). The ID of school
- quota (int). The number of students to be admitted

exam:
- school_id (int): The ID of school.
- score (int): score of the exam.
- number_of_student (int): Number of students with the same score.


For Example - 

school table

school_id   quota
----------- -----------
1           10
2           10
3           25
4           50


exam table

school_id   score       number_of_student
----------- ----------- -----------------
1           700         1
1           600         2
1           500         5
1           400         2
1           200         9
2           60          3
2           50          3
2           40          1
2           30          7
3           4           4
3           3           10
3           2           6
3           1           5



Result - 

school_id   cut_off_score
----------- ------------
1           400
2           40
3           1
4           -1



Explanation:

For school_id = 1, the quota is to admit 10 students. 
We have 1 student with score 700, 2 students with score 600, 5 students with score 500, 2 students with score 400. 
(1+2+5+2) = 10. Therefore, 400 is the lowest cut off score for the students to be admitted.

For school_id = 2, the quota is to admit 10 students. 
We have 3 student with score 60, 3 students with score 50, 1 students with score 40, 7 students with score 30. 
(3+3+1+7) = 14, which surpasses the quota (10). 
We then take out the last 7 students with score 30, and set the cut-off score to be 40, to meet the quota.

For school_id = 3, the quota is to admit 25 students. 
We have 4 student with score 4, 10 students with score 3, 6 students with score 2, 5 students with score 1. 
(4+10+6+5) = 25. Therefore, 1 is the lowest cut off score for the students to be admitted.

For school_id = 4, it does not appear in the exam table, we simply return -1 as the answer.




Solutions:

with cte as (
	select 
		s.school_id
		, s.quota
		, e1.score 
		, students_with_ge_score = (select sum(e2.number_of_student) from exam e2 where e2.school_id = e1.school_id and e2.score >= e1.score)
	from 
	school s left outer join exam e1 on s.school_id = e1.school_id
)
select 
	school_id
, 	cut_off_score = isnull(min(score), -1) 
from cte 
where 
	isnull(students_with_ge_score, -1) <= quota
group by 
	school_id
order by 
	cut_off_score desc 


Thoughts - 

Step 1: For each row in the exam table, count the students from the same school, with same or greater score, this is the column "students_with_ge_score" in the CTE
Step 2: Find the rows in the CTE, with students_with_ge_score <= quota, those are the students to be admitted
Step 3: Find the lowest score from Step2 for each school, which is the cut-off score for admission
Step 4: Return the result and order by cut-off score descendingly. 


Test Cases:


create table school (school_id int, quota int)

create table exam(school_id int, score int, number_of_student int)

insert into exam(school_id, score, number_of_student) values (1, 700, 1)
insert into exam(school_id, score, number_of_student) values (1, 600, 2)
insert into exam(school_id, score, number_of_student) values (1, 500, 5)
insert into exam(school_id, score, number_of_student) values (1, 400, 2)
insert into exam(school_id, score, number_of_student) values (1, 200, 9)
insert into exam(school_id, score, number_of_student) values (2, 60, 3)
insert into exam(school_id, score, number_of_student) values (2, 50, 3)
insert into exam(school_id, score, number_of_student) values (2, 40, 1)
insert into exam(school_id, score, number_of_student) values (2, 30, 7)
insert into exam(school_id, score, number_of_student) values (3, 4, 4)
insert into exam(school_id, score, number_of_student) values (3, 3, 10)
insert into exam(school_id, score, number_of_student) values (3, 2, 6)
insert into exam(school_id, score, number_of_student) values (3, 1, 5)

insert into dbo.school(school_id, quota) values (1, 10)
insert into dbo.school(school_id, quota) values (2, 10)
insert into dbo.school(school_id, quota) values (3, 25)
insert into dbo.school(school_id, quota) values (4, 50)


with cte as (
	select 
		s.school_id
		, s.quota
		, e1.score 
		, students_with_ge_score = (select sum(e2.number_of_student) from exam e2 where e2.school_id = e1.school_id and e2.score >= e1.score)
	from 
	school s left outer join exam e1 on s.school_id = e1.school_id
)
select 
	school_id
, 	cut_off_score = isnull(min(score), -1) 
from cte 
where 
	isnull(students_with_ge_score, -1) <= quota
group by 
	school_id
order by 
	cut_off_score desc 

*/




























