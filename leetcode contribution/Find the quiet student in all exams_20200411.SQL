/*
Question Title:
Find the quiet student in all exams

Reason:
The question is asked during a inteview with an investment bank. It's a good interview question, and I don't see a similar one on Leetcode 


Description:
A "quiet" student is the one not getting the highest or the lowest score in the exam.

Given Student and Exam tables, return the students being "quiet" in ALL exams.

Student: 

Student_ID (int), is the primary key of the student table
Student_Name (varchar),  the name of the student
Exam:  Column names are self-explanatory. It might have duplicated records, as a student can take the same test more than once.

Exam_ID (int)
Student_ID (int)
Score (int)
Result:  Return Id and name of the student who has been quiet in ALL the exams. Do not return the student who has never taken any exam. 

 

For Example - 

Student table

Student_ID  Student_Name
----------- ----------------
1           Tim
2           Steve
3           Bill
4           Mark
 

Exam table

Exam_ID     Student_ID  Score
----------- ----------- -----------
1           1           48
1           1           52
1           2           50
1           3           70
2           1           99
2           2           60
2           1           50
3           1           48
3           2           50
3           3           60

 

Result:

Student_ID  Student_Name
----------- ------------
2           Steve
 

Explanation:

For exam 1: Student 1 and 3 hold the lowest and high score 

For exam 2: Student 1 hold both highest and lowest score

For exam 3: Studnet 1 and 3 hold the lowest and high score

Student 2 and 4 have never got the highest or lowest in any of the exam.

Since student 4 is not taking any exam, he/she is excluded from the result.

So, we only return the information of Student 2.


Solutions:

select * from Student
where Student_ID not in (
	select Student_ID from Exam e1
	where not exists (select * from Exam e2 where e2.Exam_ID = e1.Exam_ID and e2.Score > e1.Score)
	union 
	select Student_ID from Exam e1
	where not exists (select * from Exam e2 where e2.Exam_ID = e1.Exam_ID and e2.Score < e1.Score)
)
and 
Student_ID in (select Student_ID from Exam)

Step 1: Get all the student with the highest score in any exam 
Step 2: Get all the student with the lowest score in any exam 
Step 3: Union the result of Step 1 and Step 2, those are the students to be excluded from the result 
Step 4: Find the ones never taken any exam. (or find the ones taking at least one exam)

Combine step 3 and step 4, we can get the desired result.

Test Cases:

create table Student(Student_ID  int, Student_Name   varchar(200))

insert into Student values(1, 'Tim')
insert into Student values(2, 'Steve')
insert into Student values(3, 'Bill')
insert into Student values(4, 'Mark')

create table Exam (Exam_ID int, Student_ID int, Score int)

insert into Exam values(1, 1, 48)
insert into Exam values(1, 1, 52)
insert into Exam values(1, 2, 50)
insert into Exam values(1, 3, 70)
insert into Exam values(2, 1, 99)
insert into Exam values(2, 2, 60)
insert into Exam values(2, 1, 50)
insert into Exam values(3, 1, 48)
insert into Exam values(3, 2, 50)
insert into Exam values(3, 3, 60)


Student Table:

Student_ID  Student_Name
----------- ---------------
1           Tim
2           Steve
3           Bill
4           Mark


Exam Table:

Exam_ID     Student_ID  Score
----------- ----------- -----------
1           1           48
1           1           52
1           2           50
1           3           70
2           1           99
2           2           60
2           1           50
3           1           48
3           2           50
3           3           60



Result:

Student_ID  Student_Name
----------- ------------
2           Steve



*/



create table Student(Student_ID  int, Student_Name   varchar(200))

insert into Student values(1, 'Tim')
insert into Student values(2, 'Steve')
insert into Student values(3, 'Bill')
insert into Student values(4, 'Mark')



create table Exam (Exam_ID int, Student_ID int, Score int)

insert into Exam values(1, 1, 48)
insert into Exam values(1, 1, 52)
insert into Exam values(1, 2, 50)
insert into Exam values(1, 3, 70)
insert into Exam values(2, 1, 99)
insert into Exam values(2, 2, 60)
insert into Exam values(2, 1, 50)
insert into Exam values(3, 1, 48)
insert into Exam values(3, 2, 50)
insert into Exam values(3, 3, 60)



select * from Student
where Student_ID not in (
	select Student_ID from Exam e1
	where not exists (select * from Exam e2 where e2.Exam_ID = e1.Exam_ID and e2.Score > e1.Score)
	union 
	select Student_ID from Exam e1
	where not exists (select * from Exam e2 where e2.Exam_ID = e1.Exam_ID and e2.Score < e1.Score)
)
and 
Student_ID in (select Student_ID from Exam)


--select * from Student
--select * from Exam 
