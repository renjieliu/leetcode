/*
1990. Count the Number of Experiments

Table: Experiments

+-----------------+------+
| Column Name     | Type |
+-----------------+------+
| experiment_id   | int  |
| platform        | enum |
| experiment_name | enum |
+-----------------+------+
experiment_id is the primary key for this table.
platform is an enum with one of the values ('Android', 'IOS', 'Web').
experiment_name is an enum with one of the values ('Reading', 'Sports', 'Programming').
This table contains information about the ID of an experiment done with a random person, the platform used to do the experiment, and the name of the experiment.
 

Write an SQL query to report the number of experiments done on each of the three platforms for each of the three given experiments. Notice that all the pairs of (platform, experiment) should be included in the output including the pairs with zero experiments.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input:
Experiments table:
+---------------+----------+-----------------+
| experiment_id | platform | experiment_name |
+---------------+----------+-----------------+
| 4             | IOS      | Programming     |
| 13            | IOS      | Sports          |
| 14            | Android  | Reading         |
| 8             | Web      | Reading         |
| 12            | Web      | Reading         |
| 18            | Web      | Programming     |
+---------------+----------+-----------------+
Output: 
+----------+-----------------+-----------------+
| platform | experiment_name | num_experiments |
+----------+-----------------+-----------------+
| Android  | Reading         | 1               |
| Android  | Sports          | 0               |
| Android  | Programming     | 0               |
| IOS      | Reading         | 0               |
| IOS      | Sports          | 1               |
| IOS      | Programming     | 1               |
| Web      | Reading         | 2               |
| Web      | Sports          | 0               |
| Web      | Programming     | 1               |
+----------+-----------------+-----------------+
Explanation: 
On the platform "Android", we had only one "Reading" experiment.
On the platform "IOS", we had one "Sports" experiment and one "Programming" experiment.
On the platform "Web", we had two "Reading" experiments and one "Programming" experiment.

*/


Create table Experiments (experiment_id int, platform ENUM('Android', 'IOS', 'Web'), experiment_name ENUM('Reading', 'Sports', 'Programming'))
Truncate table Experiments
insert into Experiments (experiment_id, platform, experiment_name) values ('4', 'IOS', 'Programming')
insert into Experiments (experiment_id, platform, experiment_name) values ('13', 'IOS', 'Sports')
insert into Experiments (experiment_id, platform, experiment_name) values ('14', 'Android', 'Reading')
insert into Experiments (experiment_id, platform, experiment_name) values ('8', 'Web', 'Reading')
insert into Experiments (experiment_id, platform, experiment_name) values ('12', 'Web', 'Reading')
insert into Experiments (experiment_id, platform, experiment_name) values ('18', 'Web', 'Programming')




/* Write your T-SQL query statement below */
with platform as 
(select p = 'Android' union all select 'IOS' union all select 'Web')
, ex as
(select * from (values ('Reading'),('Sports'),('Programming')) as _(e)) 
, fullList as (select platform.p, ex.e from platform , ex )
select 
platform = f.p
, experiment_name = f.e 
, num_experiments = isnull(count(distinct exp.experiment_id),0)
from 
fullList f left outer join Experiments exp 
on f.p= exp.platform and f.e = exp.experiment_name
group by f.p, f.e
order by 1

































