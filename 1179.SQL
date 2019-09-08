Create table   Department (id int, revenue int, month varchar(5))
Truncate table Department
insert into Department (id, revenue, month) values ('1', '8000', 'Jan')
insert into Department (id, revenue, month) values ('2', '9000', 'Jan')
insert into Department (id, revenue, month) values ('3', '10000', 'Feb')
insert into Department (id, revenue, month) values ('1', '7000', 'Feb')
insert into Department (id, revenue, month) values ('1', '6000', 'Mar')



select id
, Jan_Revenue = sum(case when [MONTH] = 'Jan' then revenue end)
, Feb_Revenue = sum(case when [MONTH] = 'Feb' then revenue end) 
, Mar_Revenue = sum(case when [MONTH] = 'Mar' then revenue end)
, Apr_Revenue = sum(case when [MONTH] = 'Apr' then revenue end)  
, May_Revenue = sum(case when [MONTH] = 'May' then revenue end)  
, Jun_Revenue = sum(case when [MONTH] = 'Jun' then revenue end)  
, Jul_Revenue = sum(case when [MONTH] = 'Jul' then revenue end)  
, Aug_Revenue = sum(case when [MONTH] = 'Aug' then revenue end) 
, Sep_Revenue = sum(case when [MONTH] = 'Sep' then revenue end)  
, Oct_Revenue = sum(case when [MONTH] = 'Oct' then revenue end)  
, Nov_Revenue = sum(case when [MONTH] = 'Nov' then revenue end)  
, Dec_Revenue = sum(case when [MONTH] = 'Dec' then revenue end)  
from Department
group by id








