/*
2480. Form a Chemical Bond

Table: Elements

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| symbol      | varchar |
| type        | enum    |
| electrons   | int     |
+-------------+---------+
symbol is the primary key for this table.
Each row of this table contains information of one element.
type is an ENUM of type ('Metal', 'Nonmetal', 'Noble')
 - If type is Noble, electrons is 0.
 - If type is Metal, electrons is the number of electrons that one atom of this element can give.
 - If type is Nonmetal, electrons is the number of electrons that one atom of this element needs.
 

Two elements can form a bond if one of them is 'Metal' and the other is 'Nonmetal'.

Write an SQL query to find all the pairs of elements that can form a bond.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Elements table:
+--------+----------+-----------+
| symbol | type     | electrons |
+--------+----------+-----------+
| He     | Noble    | 0         |
| Na     | Metal    | 1         |
| Ca     | Metal    | 2         |
| La     | Metal    | 3         |
| Cl     | Nonmetal | 1         |
| O      | Nonmetal | 2         |
| N      | Nonmetal | 3         |
+--------+----------+-----------+
Output: 
+-------+----------+
| metal | nonmetal |
+-------+----------+
| La    | Cl       |
| Ca    | Cl       |
| Na    | Cl       |
| La    | O        |
| Ca    | O        |
| Na    | O        |
| La    | N        |
| Ca    | N        |
| Na    | N        |
+-------+----------+
Explanation: 
Metal elements are La, Ca, and Na.
Nonmeal elements are Cl, O, and N.
Each Metal element pairs with a Nonmetal element in the output table.

*/


Create table Elements (symbol varchar(2), type ENUM('Metal','Nonmetal','Noble'), electrons int)
Truncate table Elements
insert into Elements (symbol, type, electrons) values ('He', 'Noble', '0')
insert into Elements (symbol, type, electrons) values ('Na', 'Metal', '1')
insert into Elements (symbol, type, electrons) values ('Ca', 'Metal', '2')
insert into Elements (symbol, type, electrons) values ('La', 'Metal', '3')
insert into Elements (symbol, type, electrons) values ('Cl', 'Nonmetal', '1')
insert into Elements (symbol, type, electrons) values ('O', 'Nonmetal', '2')
insert into Elements (symbol, type, electrons) values ('N', 'Nonmetal', '3')

/* Write your T-SQL query statement below */
select 
metal = e1.symbol
, nonmetal = e2.symbol from 
elements e1 cross join elements e2
where e1.type = 'Metal' and e2.type = 'Nonmetal'


