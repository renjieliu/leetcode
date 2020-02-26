Find the start and end number of continuous ranges

Say we have a table column holding integers.

Your task is to find the start and end number of continuous ranges


Input:
+------+
| id   |
+------+
|   -1 |
|    0 |
|    1 |
|    2 |
|    4 |
|    5 |
|    6 |
|    6 |
|    7 |
|    8 |
|   10 |
+------+

Output:
+-------------+-----------+
| range_start | range_end |
+-------------+-----------+
|          -1 |         2 |
|           4 |         8 |
|          10 |        10 |
+-------------+-----------+



1. If to use SQL Server,  Oracle or MySQL (version > 8.0), this can be elegantly solved with Windows function.  Sample code as below - 
select
range_start = min(id), 
range_end = max(id)
from 
(select id, RNK = dense_rank() over (order by id ) from T) tmp
group by RNK - id
order by 1 

2. If to use MySQL prior to version 8.0, we need to figure out a way to mimic the dense_rank funcion, and use the same approach as solution 1. Sample code as below - 

select min(id) range_start ,  max(id) range_end 
from 
(select id, (select 1+count(distinct id) as rnk  from T t1 where t1.id<T.id) RNK  from T) temp
group by RNK - id
order by 1 ;

