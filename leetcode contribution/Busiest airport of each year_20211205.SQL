/*
Question Title:

Busiest airport of each year

Reason:
The question was asked by the leading online retailer, for Business Intelligence Engineer. It can be useful for other candidates.

Description:

We have an Airlines table, with number of flights for the departure and arrival airports of each year.

The busiest airport is defined as the one with the most arrival or departure flights.

Write a query to report the busiest airport of each year, with the number of flights. If there's a tie, please return all the airports in question.

Sort the result set by year, and the name of airport.


Table - 
 
Airlines:  
- calendar_year (int): The calendar year
- departure (varchar(10)): The departure airport
- arrival (varchar(10)): The arrival airport
- number_of_flights (int): The number of flights 


For Example - 

Airlines table

calendar_year departure  arrival    number_of_flights
------------- ---------- ---------- -----------------
2019          DEN        NYC        50
2019          DEN        SEA        20
2019          LAX        NYC        10
2019          LAX        DEN        200
2020          DEN        CHI        180
2020          NYC        SEA        100
2020          NYC        DEN        200
2020          SEA        NYC        80
2021          SEA        DEN        95
2021          SEA        NYC        10


Result - 

calendar_year airport    total_number_of_flights
------------- ---------- -----------------------
2019          DEN        270
2020          DEN        380
2020          NYC        380
2021          SEA        105



Explanation - 

For 2019 - There are 70 departure flights (50+20) + 200 arrival flights at DEN airport. In total, there're 270 flights at DEN airport. 
		   There are 210 departure flights (10+200) + 0 arrival flights at LAX airport. In total, there're 210 flights at LAX airport.
		   There are 0 departure flights + 60 arrival flights at NYC airport. In total, there're 60 flights at NYC airport.
		   Therfore, DEN is the busiest airport of 2019.
		   
For 2020 - There are 380 departure or arrival flights at DEN. 
		   There are 380 departure or arrival flights at NYC.
		   There are 180 departure or arrival flights at CHI. 
		   There are 180 departure or arrival flights at SEA.
		   Therefore, both DEN and NYC with 380 flights will be reported.

For 2021 - There are 105 departure or arrival flights at SEA.
		   There are 95 departure or arrival flights at DEN.
		   There are 10 departure or arrival flights at NYC.




Solutions:

WITH merged AS (
	SELECT calendar_year, airport = departure, number_of_flights FROM Airlines 
	UNION 
	SELECT calendar_year, airport = arrival, number_of_flights FROM Airlines 
)
, report AS (
	SELECT 
	  calendar_year
	, airport
	, total_number_of_flights = SUM(number_of_flights) 
	FROM merged 
	GROUP BY calendar_year, airport 
) 
SELECT 
  calendar_year
, airport
, total_number_of_flights 
FROM report r1 
WHERE NOT EXISTS 
(
 SELECT * FROM report r2 
 WHERE 
 r1.calendar_year = r2.calendar_year 
 AND 
 r2.total_number_of_flights > r1.total_number_of_flights
)
ORDER BY calendar_year, airport

Thoughts - 

Step 1: Merge the departure and arrival airports into one column, airport.
Step 2: Find total_number_of_flights of the airport for each year. 
Step 3: Use NOT EXISTS to find the busiest the airport of each year and return the result.


Test Cases (MSSQL):


drop table if exists Airlines; 

create table Airlines (
calendar_year int
,departure  varchar(10) 
,arrival  varchar(10)
,number_of_flights int 
)
;
insert into Airlines values
( 2020, 'NYC','DEN', 200)
,( 2019, 'DEN','NYC', 50)
,(2020,  'DEN', 'CHI', 180)
,( 2020, 'NYC','SEA', 100)
,( 2020, 'SEA','NYC', 80)
,( 2021, 'SEA','DEN', 95)
,( 2019, 'DEN','SEA', 20)
,( 2021, 'SEA','NYC', 10)
,( 2019, 'LAX','NYC', 10)
,( 2019, 'LAX','DEN', 200)

; 


WITH merged AS (
	SELECT calendar_year, airport = departure, number_of_flights FROM Airlines 
	UNION 
	SELECT calendar_year, airport = arrival, number_of_flights FROM Airlines 
)
, report AS (
	SELECT 
	  calendar_year
	, airport
	, total_number_of_flights = SUM(number_of_flights) 
	FROM merged 
	GROUP BY calendar_year, airport 
) 
SELECT 
  calendar_year
, airport
, total_number_of_flights 
FROM report r1 
WHERE NOT EXISTS 
(
 SELECT * FROM report r2 
 WHERE 
 r1.calendar_year = r2.calendar_year 
 AND 
 r2.total_number_of_flights > r1.total_number_of_flights
)
ORDER BY calendar_year, airport




*/




























