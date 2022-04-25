/*
2252. Dynamic Pivoting of a Table


Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | varchar |
| price       | int     |
+-------------+---------+
(product_id, store) is the primary key for this table.
Each row of this table indicates the price of product_id in store.
There will be at most 30 different stores in the table.
price is the price of the product at this store.
 

Important note: This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.

Implement the procedure PivotProducts to reorganize the Products table so that each row has the id of one product and its price in each store. The price should be null if the product is not sold in a store. The columns of the table should contain each store and they should be sorted in lexicographical order.

The procedure should return the table after reorganizing it.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Products table:
+------------+----------+-------+
| product_id | store    | price |
+------------+----------+-------+
| 1          | Shop     | 110   |
| 1          | LC_Store | 100   |
| 2          | Nozama   | 200   |
| 2          | Souq     | 190   |
| 3          | Shop     | 1000  |
| 3          | Souq     | 1900  |
+------------+----------+-------+
Output: 
+------------+----------+--------+------+------+
| product_id | LC_Store | Nozama | Shop | Souq |
+------------+----------+--------+------+------+
| 1          | 100      | null   | 110  | null |
| 2          | null     | 200    | null | 190  |
| 3          | null     | null   | 1000 | 1900 |
+------------+----------+--------+------+------+
Explanation: 
We have 4 stores: Shop, LC_Store, Nozama, and Souq. We first order them lexicographically to be: LC_Store, Nozama, Shop, and Souq.
Now, for product 1, the price in LC_Store is 100 and in Shop is 110. For the other two stores, the product is not sold so we set the price as null.
Similarly, product 2 has a price of 200 in Nozama and 190 in Souq. It is not sold in the other two stores.
For product 3, the price is 1000 in Shop and 1900 in Souq. It is not sold in the other two stores.

*/

Create table Products (product_id int, store varchar(7), price int)
Truncate table Products
insert into Products (product_id, store, price) values ('1', 'Shop', '110')
insert into Products (product_id, store, price) values ('1', 'LC_Store', '100')
insert into Products (product_id, store, price) values ('2', 'Nozama', '200')
insert into Products (product_id, store, price) values ('2', 'Souq', '190')
insert into Products (product_id, store, price) values ('3', 'Shop', '1000')
insert into Products (product_id, store, price) values ('3', 'Souq', '1900')


CREATE PROCEDURE PivotProducts AS
BEGIN
    /* Write your T-SQL query statement below. */
    SET NOCOUNT ON;
    
    drop table if exists #base; 
    
    select rn = ROW_NUMBER() over (order by store),  store into #base from Products
	group by store
    
    declare @n int = 1
    declare @sql__ nvarchar(4000) = 'select product_id '
    
    while @n <= (select cnt = count(*) from #base)
    begin 
    set @sql__ += ',' + (select store from #base where rn = @n) + '= min(case when store = ''' + (select store from #base where rn = @n) + ' '' then price end) '
    set @n += 1
    end 

    set @sql__ += 'from Products group by product_id'
    
    exec sp_executesql @sql__    
   
    
END


