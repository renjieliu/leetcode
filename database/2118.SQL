/*
2118. Build the Equation


Table: Terms

+-------------+------+
| Column Name | Type |
+-------------+------+
| power       | int  |
| factor      | int  |
+-------------+------+
power is the primary key column for this table.
Each row of this table contains information about one term of the equation.
power is an integer in the range [0, 100].
factor is an integer in the range [-100, 100] and cannot be zero.
 

You have a very powerful program that can solve any equation of one variable in the world. The equation passed to the program has to follow the following rules:

The LHS should contain all the terms.
The RHS should be zero.
Each term of the LHS should follow the format "sign factor X ^power" after removing the white spaces where:
sign is either "+" or "-".
factor is the absolute value of the factor.
power is the value of the power.
If the power is 1, do not add "^power".
For example, if power = 1 and factor = 3, the term will be "+3X".
If the power is 0, add neither "X" nor "^power".
For example, if power = 0 and factor = -3, the term will be "-3".
The powers in the RHS should be sorted in descending order.
Write an SQL query to build the equation.

The query result format is in the following example.

 

Example 1:

Input: 
Terms table:
+-------+--------+
| power | factor |
+-------+--------+
| 2     | 1      |
| 1     | -4     |
| 0     | 2      |
+-------+--------+
Output: 
+--------------+
| equation     |
+--------------+
| +1X^2-4X+2=0 |
+--------------+
Example 2:

Input: 
Terms table:
+-------+--------+
| power | factor |
+-------+--------+
| 4     | -4     |
| 2     | 1      |
| 1     | -1     |
+-------+--------+
Output: 
+-----------------+
| equation        |
+-----------------+
| -4X^4+1X^2-1X=0 |
+-----------------+
 

Follow up: What will be changed in your solution if the power is not a primary key and each power should be unique in the answer?


*/

Create table Terms (power int, factor int)
Truncate table Terms
insert into Terms (power, factor) values ('2', '1')
insert into Terms (power, factor) values ('1', '-4')
insert into Terms (power, factor) values ('0', '2')


/* Write your T-SQL query statement below */
with base as --this is used to solve the follow up question. No need to aggregate to solve the original problem
(select power, factor = sum(factor) from Terms group by power)
, rpt as 
(select 
combo = '+' + cast(factor as varchar(20)) + case when power > 1 then 'X^' + cast(power as varchar(20)) 
                                   when power = 1 then 'X' 
                                   when power = 0 then ''
                              end                                    
, power
from base
) 
select 
equation = replace(replace(string_agg(combo, '+') within group(order by power desc) , '++' , '+'), '+-', '-') + '=0'
from rpt




