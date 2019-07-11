/*

A U.S graduate school has students from Asia, Europe and America. The students' location information are stored in table student as below.
 

| name   | continent |
|--------|-----------|
| Jack   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jane   | America   |
 

Pivot the continent column in this table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia and Europe respectively. It is guaranteed that the student number from America is no less than either Asia or Europe.
 

For the sample input, the output is:
 

| America | Asia | Europe |
|---------|------|--------|
| Jack    | Xi   | Pascal |
| Jane    |      |        |
 

Follow-up: If it is unknown which continent has the most students, can you write a query to generate the student report?

*/

Create table student (name varchar(50), continent varchar(7))
Truncate table student
insert into student (name, continent) values ('Jane', 'America')
insert into student (name, continent) values ('Pascal', 'Europe')
insert into student (name, continent) values ('Xi', 'Asia')
insert into student (name, continent) values ('Jack', 'America')



/* Write your T-SQL query statement below */
select America = am.name, Asia = asia.name, Europe = e.name from 
(select id = ROW_NUMBER() over (order by name), name from student
where continent = 'America') Am
left outer join
(
select id = ROW_NUMBER() over (order by name), name from student
where continent = 'Asia'
)asia
on am.id = asia.id
left outer join
(
select id = ROW_NUMBER() over (order by name), name from student
where continent = 'Europe'
)e 
on am.id  = e.id



/*

--Not sure if it's possible to achieve without dynamic SQL

; with c1 as (
select continent, cnt = count(1), rn = ROW_NUMBER() over (order by count(1) desc ) from student 
group by continent
)
select America = a.name, Asia = b.name, Europe = c.name from 
(select id = ROW_NUMBER() over (order by name), name from student
where continent = (select continent from c1 where rn = 1 )) a
left outer join
(
select id = ROW_NUMBER() over (order by name), name from student
where continent = (select continent from c1 where rn = 2 )
)b
on a.id = b.id
left outer join
(
select id = ROW_NUMBER() over (order by name), name from student
where continent = (select continent from c1 where rn = 3 )
)c 
on a.id  = c.id



*/

























