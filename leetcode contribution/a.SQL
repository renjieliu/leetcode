/*

We have a product table and a sales table.

The product table has 4 columns. product_id, start_date, end_date, product_name.

The product_id and product_name are self-explanatory.
The start_date indicates when the product_name became effective.
The end_date indicates the last effective date of the current product_name.
Both start_date and end_dates are inclusive.
The sales table has 4 columns as following.

product_id, period_start, period_end and average_daily_sales

period_start and period_end indicates the start and end date for sales period, both dates are inclusive.
The average_daily_sales column holds the average daily sales amount of the items for the period.
Your task is to report the Total sales amount of each item for each year, with corresponding product name, order by the product_id, product_name and report_year, all ascendingly.

Note: The product is guaranteed to be valid during the sales period.

Example: 

product table:

product_id  start_date end_date   product_name
----------- ---------- ---------- --------------------
1           2015-01-01 2015-11-01 apple0
1           2015-11-02 2019-12-31 apple1
2           2013-01-02 2016-12-29 google1
2           2016-12-30 2019-02-02 google2


sales table: 

product_id  period_start period_end average_daily_sales
----------- ------------ ---------- -------------------
1           2015-03-01   2019-12-17 20
2           2013-03-01   2017-12-17 15

Result: 

product_name  		 report_year total_amount
-------------------- ----------- ------------
apple0               2015        4920
apple1               2015        1200
apple1               2016        7320
apple1               2017        7300
apple1               2018        7300
apple1               2019        7000
google1              2013        4590
google1              2014        5475
google1              2015        5475
google1              2016        5460
google2              2016        30
google2              2017        5250


Explanation:

For the year of 2015, product1 started transaction from 2015-03-01, it was named as 'apple0' for the period of 2015-03-01 to 2015-11-01, and there're 246 days for this period. 
Since the daily average is 20 for the above period, the total_amount for product1 named as 'apple0' for 2015 is 246*20 = 4920

For the year of 2016, product 1 was named as apple1 for the whole year, since there are 366 days in 2016, the total report amount is 366*20 = 7320. 

*/



drop table product
drop table sales

create table product(product_id int,start_date date, end_date date,  product_name varchar(20));
create table sales (product_id int, period_start date, period_end date, average_daily_sales int);
 
insert into product values (1, '2015-01-01', '2015-11-01', 'apple0');
insert into product values (1, '2015-11-02', '2019-12-31', 'apple1');
insert into product values (2, '2013-01-02', '2016-12-29', 'google1');
insert into product values (2, '2016-12-30', '2019-02-02', 'google2');

insert into sales values(1, '2015-03-01', '2019-12-17', 20);
insert into sales values(2, '2013-03-01', '2017-12-17', 15);

select * from product
select * from sales 



;with all_sale_dates as 
(select product_id, dates = period_start, day_end = period_end from sales 
	union all
select a.product_id, dateadd(day, 1, dates), day_end from all_sale_dates a
inner join sales s on a.product_id = s.product_id and a.day_end = s.period_end
where dateadd(day, 1, dates) < day_end
)
select 
p.product_id
, p.product_name
, report_year = year(d.dates)
, total_amount = sum(s.average_daily_sales)
from all_sale_dates d 
left outer join sales s 
on d.product_id = s.product_id and d.dates between s.period_start and s.period_end
left outer join product p on d.product_id  = p.product_id and d.dates between p.start_date and p.end_date
group by p.product_id, p.product_name, year(d.dates), p.product_name
order by 1, 2 ,3
option(maxrecursion 0)


