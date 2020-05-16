/*
Question Title:

Find Common Pairs in draw history

Reason:
The question is asked during a inteview with a financial institution. It's a good interview question, and it can have multiple follow up questions.

Description:
"Common Pair" is two numbers appear in more than one draw.

We have 5 unique numbers for each draw, write a query to return all the Common Pairs in the draw history, along with the occurance. 

The result set should be in the following format:

1. Ordered descendingly by occurance, if same occurance happens for different Common Pairs, order ascendingly by the first_number
2. first_number should be smaller than second_number

Table - Draw

 ID int
 N1 int
 N2 int
 N3 int
 N4 int
 N5 int
It's guaranteed all the numbers within the same draw meet the condition: N1 < N2 < N3 < N4 < N5

For Example - 

Draw Table:

ID  N1   N2   N3  N4   N5
--- ---- ---- --- ---- ---
1   8    22   36  37   52
2   14   22   52  54   59
3   5    8    29  37   38
4   8    22   36  40   51
5   7    8    19  26   36

Result Table:

occurance   first_number second_number
----------- ------------ -------------
3           8            36
2           8            22
2           8            37
2           22           36
2           22           52

 

Explanation:

The pair of (8,36) happened 3 times in ID 1,4,5
The pair of (8,22) happened 2 times in ID 1,4 
The pair of (8,37) happened 2 times in ID 1,3
The pair of (22,36) happened 2 times in ID 1,4
The pair of (22,52) happened 2 times in ID 1,2

We don't report other pairs like (5,8), (36, 52) etc, as they appear only once in the draw history. 





Solutions:

select occurance = count(1), first_number , second_number  from 
(
	select N1 first_number, N2 second_number from draw union all
	select N1, N3 from draw union all
	select N1, N4 from draw union all
	select N1, N5 from draw union all
	select N2, N3 from draw union all
	select N2, N4 from draw union all
	select N2, N5 from draw union all
	select N3, N4 from draw union all
	select N3, N5 from draw union all
	select N4, N5 from draw
) T 
group by first_number , second_number
having count(*) > 1
order by 1 desc,2,3


Explanation -  

Step 1: Find all the possible combination of numbers picked each time. Since we only have 5 numbers and N1 < N2 < N3 < N4 < N5, so only have 10 possible combinations.
Step 2: Find the occurance of each pair.
Step 3: Return the pair with occurance > 1
Step 4: Sort the result set



Test Cases:


Input -

create table draw(
	ID int NULL,
	N1 int NULL,
	N2 int NULL,
	N3 int NULL,
	N4 int NULL,
	N5 int NULL
); 

insert into draw (ID, N1, N2, N3, N4, N5) VALUES (851, 8, 24, 42, 54, 64);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (745, 18, 31, 32, 45, 48);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (740, 23, 33, 42, 46, 59);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (189, 4, 30, 35, 57, 59);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (917, 7, 14, 23, 38, 55);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (849, 6, 8, 26, 52, 53);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (870, 6, 10, 15, 25, 36);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (364, 9, 23, 40, 53, 58);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (319, 3, 17, 19, 25, 32);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (782, 11, 21, 28, 33, 45);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (510, 11, 12, 46, 47, 50);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (514, 14, 15, 47, 49, 59);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (940, 1, 2, 3, 7, 39);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (392, 13, 23, 24, 27, 40);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (212, 1, 10, 37, 52, 57);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (734, 5, 28, 33, 38, 42);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (559, 29, 41, 48, 52, 54);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (866, 1, 21, 31, 45, 49);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (1042, 12, 33, 54, 57, 60);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (893, 25, 41, 53, 57, 67);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (323, 6, 10, 23, 41, 45);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (527, 10, 14, 18, 34, 51);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (500, 6, 36, 38, 48, 51);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (192, 5, 18, 33, 43, 45);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (706, 1, 25, 28, 31, 54);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (268, 1, 6, 7, 20, 49);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (260, 5, 6, 13, 36, 50);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (767, 5, 22, 43, 57, 63);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (300, 15, 23, 40, 44, 55);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (77, 20, 24, 25, 53, 59);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (766, 5, 21, 57, 66, 69);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (801, 1, 3, 13, 19, 69);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (55, 7, 10, 22, 23, 52);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (385, 3, 9, 19, 33, 38);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (572, 4, 22, 27, 28, 52);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (467, 24, 28, 30, 38, 39);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (330, 11, 23, 26, 46, 55);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (236, 9, 12, 20, 44, 59);
insert into draw (ID, N1, N2, N3, N4, N5) VALUES (539, 33, 39, 40, 41, 54);

Output - 

occurance   first_number second_number
----------- ------------ -------------
3           3            19
3           6            36
3           23           40
3           23           55
2           1            3
2           1            7
2           1            31
2           1            49
2           5            33
2           5            43
2           5            57
2           6            10
2           7            23
2           10           23
2           10           52
2           11           46
2           18           45
2           20           59
2           21           45
2           22           52
2           23           46
2           25           53
2           28           33
2           28           38
2           31           45
2           33           38
2           33           42
2           33           45
2           33           54
2           41           54

*/


select occurance = count(1), first_number , second_number  from 
(
	select N1 first_number, N2 second_number from draw union all
	select N1, N3 from draw union all
	select N1, N4 from draw union all
	select N1, N5 from draw union all
	select N2, N3 from draw union all
	select N2, N4 from draw union all
	select N2, N5 from draw union all
	select N3, N4 from draw union all
	select N3, N5 from draw union all
	select N4, N5 from draw
) T 
group by first_number , second_number
having count(*) > 1
order by 1 desc,2,3





--My Test, not submitted to Leetcode
alter table draw alter column N1 int
alter table draw alter column N2 int
alter table draw alter column N3 int
alter table draw alter column N4 int
alter table draw alter column N5 int

declare @n1 int = 22
declare @n2 int = 32
select * from powerball 
where (N1 = @n1 or N2 = @n1 or N3 = @n1 or N4 = @n1 or N5 = @n1) 
	  and
	 (N1 = @n2 or N2 = @n2 or N3 = @n2 or N4 = @n2 or N5 = @n2)

--commit


